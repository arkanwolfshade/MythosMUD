"""Message sending helpers for system and whisper messages."""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Message sending handlers require multiple return statements for early validation returns (permission checks, validation, error handling). Message sending requires extensive handlers for multiple message types and delivery methods.

import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .chat_message import ChatMessage
from .chat_message_helpers import (
    create_and_log_chat_message,
    store_global_message_in_history,
    store_message_in_room_history,
)
from .chat_nats_publisher import publish_chat_message_to_nats
from .chat_validation_helpers import (
    check_channel_permissions,
    check_global_level_requirement,
    validate_global_message,
    validate_say_message,
)

logger = get_logger("communications.chat_message_senders")


def normalize_player_id(player_id: Any) -> str:
    """Normalize player identifiers to string form."""
    return str(player_id)


async def send_system_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many parameters for context and routing
    player_id: uuid.UUID | str,
    message: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    chat_logger: Any,
    room_messages: dict[str, list[ChatMessage]],
    max_messages_per_room: int,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """
    Send a system message to all players.

    This function publishes the system message to NATS for real-time distribution
    to all players. System messages require admin privileges and are subject to rate limiting.

    Args:
        player_id: ID of the player sending the system message
        message: Message content
        player_service: Player service instance
        user_manager: User manager instance
        rate_limiter: Rate limiter instance
        chat_logger: Chat logger instance
        room_messages: Dictionary storing room messages
        max_messages_per_room: Maximum messages to store per room
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    logger.debug("=== CHAT SERVICE DEBUG: send_system_message called ===", player_id=player_id, message=message)
    logger.debug("Processing system message")

    # Validate input
    if not message or not message.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty message ===")
        return {"success": False, "error": "Message cannot be empty"}

    if len(message.strip()) > 2000:  # Limit for system messages
        logger.debug("=== CHAT SERVICE DEBUG: Message too long ===")
        return {"success": False, "error": "Message too long (max 2000 characters)"}

    # Get player information
    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for system message")
        return {"success": False, "error": "Player not found"}

    # Check admin requirement
    if not user_manager.is_admin(player_id):
        logger.debug("=== CHAT SERVICE DEBUG: Player not admin ===")
        return {"success": False, "error": "You must be an admin to send system messages"}

    # Load player's mute data to ensure it's available for permission checks
    user_manager.load_player_mutes(player_id)

    # Check rate limits before allowing system message
    if not rate_limiter.check_rate_limit(player_id, "system", player.name):
        logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===")
        return {"success": False, "error": "Rate limit exceeded for system messages", "rate_limited": True}

    # Note: Admins can send system messages even when globally muted
    # This ensures admins can always communicate important system information

    # Create chat message
    # ChatMessage accepts UUID | str and converts internally
    chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="system", content=message.strip())

    # Log the chat message for AI processing
    chat_logger.log_chat_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "content": chat_message.content,
            "room_id": None,  # System messages don't have a specific room
            "filtered": False,
            "moderation_notes": None,
        }
    )

    # Log to system channel specific log file
    chat_logger.log_system_channel_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "content": chat_message.content,
            "filtered": False,
            "moderation_notes": None,
        }
    )

    # Record message for rate limiting
    rate_limiter.record_message(player_id, "system", player.name)

    # Also log to communications log (existing behavior)
    chat_message.log_message()

    logger.debug("=== CHAT SERVICE DEBUG: System chat message created ===")

    # Store message in system history
    if "system" not in room_messages:
        room_messages["system"] = []

    room_messages["system"].append(chat_message)

    # Maintain message history limit
    if len(room_messages["system"]) > max_messages_per_room:
        room_messages["system"] = room_messages["system"][-max_messages_per_room:]

    logger.info(
        "System message created successfully",
        player_id=player_id,
        player_name=player.name,
        message_id=chat_message.id,
    )

    # Publish message to NATS for real-time distribution
    logger.debug("=== CHAT SERVICE DEBUG: About to publish system message to NATS ===")
    success = await publish_chat_message_to_nats(
        chat_message, None, nats_service, subject_manager
    )  # System messages don't have room_id
    if not success:
        # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            player_id=player_id,
            player_name=player.name,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: System NATS publishing completed ===")

    return {"success": True, "message": chat_message.to_dict()}


async def send_whisper_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Message sending requires many parameters and intermediate variables for complex routing logic
    sender_id: uuid.UUID | str,
    target_id: uuid.UUID | str,
    message: str,
    player_service: Any,
    rate_limiter: Any,
    chat_logger: Any,
    whisper_tracker: Any,
    room_messages: dict[str, list[ChatMessage]],
    max_messages_per_room: int,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """
    Send a whisper message from one player to another.

    This function publishes the whisper message to NATS for real-time distribution
    to the target player. Whisper messages are subject to rate limiting.

    Args:
        sender_id: ID of the player sending the whisper
        target_id: ID of the player receiving the whisper
        message: Message content
        player_service: Player service instance
        rate_limiter: Rate limiter instance
        chat_logger: Chat logger instance
        whisper_tracker: Whisper tracker instance
        room_messages: Dictionary storing room messages
        max_messages_per_room: Maximum messages to store per room
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    sender_id = normalize_player_id(sender_id)
    target_id = normalize_player_id(target_id)

    logger.debug("=== CHAT SERVICE DEBUG: send_whisper_message called ===", sender_id=sender_id, target_id=target_id)
    logger.debug("Processing whisper message", sender_id=sender_id, target_id=target_id, message_length=len(message))

    # Validate input
    if not message or not message.strip():
        logger.debug("=== CHAT SERVICE DEBUG: Empty whisper message ===")
        return {"success": False, "error": "Message content cannot be empty"}

    # Strip whitespace
    message = message.strip()

    # Check message length
    if len(message) > 2000:
        logger.debug("=== CHAT SERVICE DEBUG: Whisper message too long ===")
        return {"success": False, "error": "Message too long (maximum 2000 characters)"}

    # Get sender player object
    sender_obj = await player_service.get_player_by_id(sender_id)
    if not sender_obj:
        logger.debug("=== CHAT SERVICE DEBUG: Sender not found ===")
        return {"success": False, "error": "Sender not found"}

    # Get target player object
    target_obj = await player_service.get_player_by_id(target_id)
    if not target_obj:
        logger.debug("=== CHAT SERVICE DEBUG: Target not found ===")
        return {"success": False, "error": "You whisper into the aether."}

    # Check rate limiting
    sender_name = getattr(sender_obj, "name", "UnknownPlayer")
    if not rate_limiter.check_rate_limit(sender_id, "whisper", sender_name):
        logger.debug("=== CHAT SERVICE DEBUG: Whisper rate limited ===")
        return {"success": False, "error": "You are sending messages too quickly. Please wait a moment."}

    # Create chat message
    # ChatMessage accepts UUID | str and converts internally
    chat_message = ChatMessage(
        sender_id=sender_id,
        sender_name=sender_name,
        target_id=target_id,
        target_name=getattr(target_obj, "name", "UnknownPlayer"),
        channel="whisper",
        content=message,
    )

    # Log the whisper message for AI processing
    chat_logger.log_chat_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "target_id": chat_message.target_id,
            "target_name": chat_message.target_name,
            "content": chat_message.content,
            "room_id": None,  # Whisper messages don't have a specific room
            "filtered": False,
            "moderation_notes": None,
        }
    )

    # Log to whisper channel specific log file
    chat_logger.log_whisper_channel_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "target_id": chat_message.target_id,
            "target_name": chat_message.target_name,
            "content": chat_message.content,
            "filtered": False,
            "moderation_notes": None,
        }
    )

    # Record message for rate limiting
    rate_limiter.record_message(sender_id, "whisper", sender_name)

    # Store last whisper sender for reply functionality
    target_name = getattr(target_obj, "name", "UnknownPlayer")
    whisper_tracker.store_sender(target_name, sender_name)

    # Also log to communications log (existing behavior)
    chat_message.log_message()

    logger.debug("=== CHAT SERVICE DEBUG: Whisper chat message created ===", message_id=chat_message.id)

    # Store message in whisper history
    if "whisper" not in room_messages:
        room_messages["whisper"] = []

    room_messages["whisper"].append(chat_message)

    # Maintain message history limit
    if len(room_messages["whisper"]) > max_messages_per_room:
        room_messages["whisper"] = room_messages["whisper"][-max_messages_per_room:]

    logger.info(
        "Whisper message created successfully",
        sender_id=sender_id,
        target_id=target_id,
        sender_name=sender_name,
        target_name=getattr(target_obj, "name", "UnknownPlayer"),
        message_id=chat_message.id,
    )

    # Publish message to NATS for real-time distribution
    logger.debug("=== CHAT SERVICE DEBUG: About to publish whisper message to NATS ===")
    success = await publish_chat_message_to_nats(
        chat_message, None, nats_service, subject_manager
    )  # Whisper messages don't have room_id
    if not success:
        # NATS publishing failed - detailed error already logged in _publish_chat_message_to_nats
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            sender_id=sender_id,
            sender_name=sender_name,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: Whisper NATS publishing completed ===")

    return {"success": True, "message": chat_message.to_dict()}


async def send_global_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many parameters for context and routing
    player_id: uuid.UUID | str,
    message: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    chat_logger: Any,
    room_messages: dict[str, list[ChatMessage]],
    max_messages_per_room: int,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """
    Send a global message to all players.

    This function publishes the global message to NATS for real-time distribution
    to all players. Global messages require level 1+ and are subject to rate limiting.

    Args:
        player_id: ID of the player sending the global message
        message: Message content
        player_service: Player service instance
        user_manager: User manager instance
        rate_limiter: Rate limiter instance
        chat_logger: Chat logger instance
        room_messages: Dictionary storing room messages
        max_messages_per_room: Maximum messages to store per room
        nats_service: NATS service instance
        subject_manager: NATS subject manager instance (optional)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    logger.debug("=== CHAT SERVICE DEBUG: send_global_message called ===", player_id=player_id, message=message)
    logger.debug("Processing global message")

    error_result = validate_global_message(message)
    if error_result:
        return error_result

    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for global message")
        return {"success": False, "error": "Player not found"}

    error_result = check_global_level_requirement(player, player_id)
    if error_result:
        return error_result

    user_manager.load_player_mutes(player_id)

    if not rate_limiter.check_rate_limit(player_id, "global", player.name):
        logger.debug("=== CHAT SERVICE DEBUG: Rate limit exceeded ===")
        return {"success": False, "error": "Rate limit exceeded for global chat", "rate_limited": True}

    error_result = check_channel_permissions(user_manager, player_id, "global")
    if error_result:
        return error_result

    chat_message = create_and_log_chat_message(player_id, player.name, message, None, "global")
    chat_logger.log_global_channel_message(
        {
            "message_id": chat_message.id,
            "channel": chat_message.channel,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "content": chat_message.content,
            "filtered": False,
            "moderation_notes": None,
        }
    )
    rate_limiter.record_message(player_id, "global", player.name)
    logger.debug("=== CHAT SERVICE DEBUG: Global chat message created ===")

    store_global_message_in_history(room_messages, chat_message, max_messages_per_room)

    logger.info(
        "Global message created successfully",
        player_id=player_id,
        player_name=player.name,
        message_id=chat_message.id,
    )

    logger.debug("=== CHAT SERVICE DEBUG: About to publish global message to NATS ===")
    success = await publish_chat_message_to_nats(chat_message, None, nats_service, subject_manager)
    if not success:
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            player_id=player_id,
            player_name=player.name,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: Global NATS publishing completed ===")

    return {"success": True, "message": chat_message.to_dict()}


async def send_predefined_emote(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Emote sending requires many parameters and intermediate variables for complex emote logic
    player_id: uuid.UUID | str,
    emote_command: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    chat_logger: Any,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
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
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    room_messages: dict[str, list[ChatMessage]],
    max_messages_per_room: int,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
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
