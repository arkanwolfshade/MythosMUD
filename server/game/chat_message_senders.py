"""Message sending helpers for system and whisper messages."""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Message sending handlers require multiple return statements for early validation returns (permission checks, validation, error handling). Message sending requires extensive handlers for multiple message types and delivery methods.

import uuid

from ..structured_logging.enhanced_logging_config import get_logger
from .chat_channel_message_senders import (
    ChatLogger,
    ChatPlayerService,
    ChatRateLimiter,
    ChatSendServices,
    ChatUserManager,
    send_global_message,
    send_system_message,
    send_whisper_message,
)
from .chat_message import ChatMessage
from .chat_message_helpers import (
    create_and_log_chat_message,
    store_message_in_room_history,
)
from .chat_nats_publisher import publish_chat_message_to_nats
from .chat_validation_helpers import (
    check_channel_permissions,
    validate_say_message,
)

logger = get_logger("communications.chat_message_senders")

# Re-exported for callers that import senders from this module (mypy no-implicit-reexport).
__all__ = [
    "ChatSendServices",
    "normalize_player_id",
    "send_global_message",
    "send_local_message",
    "send_party_message",
    "send_predefined_emote",
    "send_system_message",
    "send_whisper_message",
]


def normalize_player_id(player_id: uuid.UUID | str) -> str:
    """Normalize player identifiers to string form."""
    return str(player_id)


async def send_party_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many parameters for context and routing
    player_id: uuid.UUID | str,
    message: str,
    party_id: str,
    player_service: ChatPlayerService,
    rate_limiter: ChatRateLimiter,
    chat_logger: ChatLogger,
    nats_service: object | None,
    subject_manager: object | None,
) -> dict[str, object]:
    """
    Send a party (ephemeral group) chat message to party members only.

    Message is published to NATS on chat.party.group.{party_id}; delivery to
    only current party members is enforced by PartyChannelStrategy. Rate limit
    uses the configured party channel limit (e.g. 30 msg/min).

    Args:
        player_id: ID of the sender
        message: Message content
        party_id: Party ID (sender must be in this party; caller validates)
        player_service: Player service instance
        rate_limiter: Rate limiter instance
        chat_logger: Chat logger instance
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    if not message or not message.strip():
        return {"success": False, "error": "Message cannot be empty"}
    if len(message.strip()) > 2000:
        return {"success": False, "error": "Message too long (max 2000 characters)"}

    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for party message")
        return {"success": False, "error": "Player not found"}

    if not rate_limiter.check_rate_limit(player_id, "party", player.name):
        return {"success": False, "error": "Rate limit exceeded for party chat", "rate_limited": True}

    chat_message = ChatMessage(
        sender_id=player_id,
        sender_name=player.name,
        channel="party",
        content=message.strip(),
        party_id=party_id,
    )
    chat_logger.log_chat_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "content": chat_message.content,
            "room_id": None,
            "filtered": False,
            "moderation_notes": None,
        }
    )
    rate_limiter.record_message(player_id, "party", player.name)
    chat_message.log_message()

    success = await publish_chat_message_to_nats(chat_message, None, nats_service, subject_manager)
    if not success:
        logger.error(
            "NATS publishing failed for party message",
            player_id=player_id,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    return {"success": True, "message": chat_message.to_dict()}


async def send_predefined_emote(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Emote sending requires many parameters and intermediate variables for complex emote logic
    player_id: uuid.UUID | str,
    emote_command: str,
    player_service: ChatPlayerService,
    user_manager: ChatUserManager,
    rate_limiter: ChatRateLimiter,
    chat_logger: ChatLogger,
    nats_service: object | None,
    subject_manager: object | None,
) -> dict[str, object]:
    """
    Send a predefined emote message using the EmoteService.

    This function uses predefined emote definitions to send formatted messages
    to both the player and room occupants.

    Args:
        player_id: ID of the player sending the emote
        emote_command: The emote command (e.g., 'twibble', 'dance')
        player_service: Player service instance
        user_manager: User manager instance
        rate_limiter: Rate limiter instance
        chat_logger: Chat logger instance
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    logger.debug(
        "=== CHAT SERVICE DEBUG: send_predefined_emote called ===", player_id=player_id, emote_command=emote_command
    )

    # Import EmoteService here to avoid circular imports
    from .emote_service import EmoteService

    # Initialize emote service
    emote_service = EmoteService()

    # Check if this is a valid emote command
    if not emote_service.is_emote_alias(emote_command):
        logger.warning("Invalid emote command")
        return {"success": False, "error": f"Unknown emote: {emote_command}"}

    # Get player information
    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for predefined emote")
        return {"success": False, "error": "Player not found"}

    # Load player's mute data to ensure it's available for permission checks
    user_manager.load_player_mutes(player_id)

    # Check rate limits before allowing emote
    if not rate_limiter.check_rate_limit(player_id, "emote", player.name):
        logger.warning("Rate limit exceeded for predefined emote", player_id=player_id, player_name=player.name)
        return {
            "success": False,
            "error": "Rate limit exceeded. Please wait before sending another emote.",
            "rate_limited": True,
        }

    # Get player's current room
    room_id = player.current_room_id
    if not room_id:
        logger.warning("Player not in a room")
        return {"success": False, "error": "Player not in a room"}

    # Check if player is muted in say channel (emotes use same channel as say)
    if user_manager.is_channel_muted(player_id, "say"):
        logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
        return {"success": False, "error": "You are muted in the say channel"}

    # Check if player is globally muted
    if user_manager.is_globally_muted(player_id):
        logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
        return {"success": False, "error": "You are globally muted and cannot send messages"}

    # Check if player can send messages (admin check, etc.)
    if not user_manager.can_send_message(player_id, channel="say"):
        logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
        return {"success": False, "error": "You cannot send messages at this time"}

    try:
        # Format the emote messages
        self_message, other_message = emote_service.format_emote_messages(emote_command, player.name)
    except ValueError as e:
        logger.error("Failed to format emote messages", player_id=player_id, emote_command=emote_command, error=str(e))
        return {"success": False, "error": str(e)}

    # Create chat message for the predefined emote
    # ChatMessage accepts UUID | str and converts internally
    chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="emote", content=other_message)

    # Log the emote message for AI processing
    chat_logger.log_chat_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "content": chat_message.content,
            "room_id": room_id,
            "filtered": False,
            "moderation_notes": None,
        }
    )

    logger.info(
        "Predefined emote message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        emote_command=emote_command,
        message_id=chat_message.id,
    )

    # Publish message to NATS for real-time distribution
    logger.debug("=== CHAT SERVICE DEBUG: About to publish predefined emote message to NATS ===")
    success = await publish_chat_message_to_nats(chat_message, room_id, nats_service, subject_manager)
    if not success:
        # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

    return {
        "success": True,
        "self_message": self_message,
        "other_message": other_message,
        "message": chat_message.to_dict(),
        "room_id": room_id,
    }


async def send_local_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Message sending requires many parameters and intermediate variables for complex routing logic
    player_id: uuid.UUID | str,
    message: str,
    player_service: ChatPlayerService,
    user_manager: ChatUserManager,
    rate_limiter: ChatRateLimiter,
    room_messages: dict[str, list[ChatMessage]],
    max_messages_per_room: int,
    nats_service: object | None,
    subject_manager: object | None,
) -> dict[str, object]:
    """
    Send a local message to players in the same sub-zone.

    This function publishes the message to NATS for real-time distribution
    to all players in the same sub-zone. NATS is mandatory for this functionality.

    Args:
        player_id: ID of the player sending the message
        message: Message content
        player_service: Player service instance
        user_manager: User manager instance
        rate_limiter: Rate limiter instance
        room_messages: Dictionary storing room messages
        max_messages_per_room: Maximum messages to store per room
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    logger.debug(
        "=== CHAT SERVICE DEBUG: send_local_message called ===",
        player_id=player_id,
        message=message,
    )
    logger.debug("Processing local message")

    error_result = validate_say_message(message)
    if error_result:
        return error_result

    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for local message")
        return {"success": False, "error": "Player not found"}

    user_manager.load_player_mutes(player_id)

    if not rate_limiter.check_rate_limit(player_id, "local", player.name):
        logger.warning("Rate limit exceeded for local message", player_id=player_id, player_name=player.name)
        return {
            "success": False,
            "error": "Rate limit exceeded. Please wait before sending another message.",
            "rate_limited": True,
        }

    room_id = player.current_room_id
    if not room_id:
        logger.warning("Player not in a room")
        return {"success": False, "error": "Player not in a room"}

    logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

    error_result = check_channel_permissions(user_manager, player_id, "local")
    if error_result:
        return error_result

    chat_message = create_and_log_chat_message(player_id, player.name, message, room_id, "local")
    rate_limiter.record_message(player_id, "local", player.name)
    logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===")

    store_message_in_room_history(room_messages, chat_message, room_id, max_messages_per_room)

    logger.info(
        "Local message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        message_id=chat_message.id,
    )

    logger.debug("=== CHAT SERVICE DEBUG: About to publish message to NATS ===")
    success = await publish_chat_message_to_nats(chat_message, room_id, nats_service, subject_manager)
    if not success:
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            player_id=player_id,
            player_name=player.name,
            room_id=room_id,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

    chat_message.echo_sent = True
    message_dict = chat_message.to_dict()
    message_dict["echo_sent"] = True
    logger.debug(
        "=== CHAT SERVICE DEBUG: Emote message response payload ===",
        payload_keys=list(message_dict.keys()),
    )
    try:
        from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
    except ImportError as import_error:  # pragma: no cover - defensive guard for import cycles
        logger.debug(
            "=== CHAT SERVICE DEBUG: Failed to register echo suppression token ===",
            error=str(import_error),
            message_id=chat_message.id,
        )
    else:
        SUPPRESS_ECHO_MESSAGE_IDS.add(chat_message.id)
        logger.debug(
            "=== CHAT SERVICE DEBUG: Registered echo suppression token ===",
            message_id=chat_message.id,
            token_count=len(SUPPRESS_ECHO_MESSAGE_IDS),
        )

    return {"success": True, "message": message_dict, "room_id": room_id}
