"""Message sending helpers for system and whisper messages."""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Message sending handlers require multiple return statements for early validation returns (permission checks, validation, error handling). Message sending requires extensive handlers for multiple message types and delivery methods.

import uuid

from ..structured_logging.enhanced_logging_config import get_logger
from .chat_channel_message_senders import (
    ChatEmoteService,
    ChatLogger,
    ChatPlayerService,
    ChatPlayerView,
    ChatRateLimiter,
    ChatResult,
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


_NATS_UNAVAILABLE = "Chat system temporarily unavailable. Please try again in a moment."


async def _publish_chat_or_unavailable(
    chat_message: ChatMessage, room_id: str | None, ctx: ChatSendServices, extra: dict[str, object]
) -> ChatResult | None:
    """Publish to NATS, or a standard 'unavailable' error result; NATS is mandatory."""
    success = await publish_chat_message_to_nats(chat_message, room_id, ctx["nats_service"], ctx["subject_manager"])
    if success:
        return None
    logger.error("NATS publishing failed - NATS is mandatory for chat functionality", **extra)
    return {"success": False, "error": _NATS_UNAVAILABLE}


def _check_emote_permissions(user_manager: ChatUserManager, player_id: str) -> ChatResult | None:
    """Mute/admin checks shared by the say channel; emotes use the same channel as say."""
    if user_manager.is_channel_muted(player_id, "say"):
        logger.debug("=== CHAT SERVICE DEBUG: Player is muted ===")
        return {"success": False, "error": "You are muted in the say channel"}
    if user_manager.is_globally_muted(player_id):
        logger.debug("=== CHAT SERVICE DEBUG: Player is globally muted ===")
        return {"success": False, "error": "You are globally muted and cannot send messages"}
    if not user_manager.can_send_message(player_id, channel="say"):
        logger.debug("=== CHAT SERVICE DEBUG: Player cannot send messages ===")
        return {"success": False, "error": "You cannot send messages at this time"}
    return None


async def _authorize_emote_sender(
    player_id: str, ctx: ChatSendServices
) -> tuple[ChatPlayerView | None, str | None, ChatResult | None]:
    """Resolve the player, run rate-limit/mute checks, and confirm they're in a room.

    Returns (player, room_id, None) on success, or (None, None, error_result).
    """
    player = await ctx["player_service"].get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for predefined emote")
        return None, None, {"success": False, "error": "Player not found"}

    # Load player's mute data to ensure it's available for permission checks
    _ = ctx["user_manager"].load_player_mutes(player_id)

    if not ctx["rate_limiter"].check_rate_limit(player_id, "emote", player.name):
        logger.warning("Rate limit exceeded for predefined emote", player_id=player_id, player_name=player.name)
        return (
            None,
            None,
            {
                "success": False,
                "error": "Rate limit exceeded. Please wait before sending another emote.",
                "rate_limited": True,
            },
        )

    room_id = player.current_room_id
    if not room_id:
        logger.warning("Player not in a room")
        return None, None, {"success": False, "error": "Player not in a room"}

    permission_error = _check_emote_permissions(ctx["user_manager"], player_id)
    if permission_error:
        return None, None, permission_error

    return player, room_id, None


def _build_and_log_emote_message(
    player: ChatPlayerView,
    player_id: str,
    room_id: str,
    emote_command: str,
    emote_service: ChatEmoteService,
    ctx: ChatSendServices,
) -> tuple[ChatMessage, str, str] | ChatResult:
    """Format the emote text, build its ChatMessage, and log it for AI processing.

    Returns (chat_message, self_message, other_message) on success, or an error result if
    the emote command can't be formatted for this player.
    """
    try:
        self_message, other_message = emote_service.format_emote_messages(emote_command, player.name)
    except ValueError as e:
        logger.error("Failed to format emote messages", player_id=player_id, emote_command=emote_command, error=str(e))
        return {"success": False, "error": str(e)}

    # ChatMessage accepts UUID | str and converts internally
    chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="emote", content=other_message)
    ctx["chat_logger"].log_chat_message(
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
    return chat_message, self_message, other_message


async def send_predefined_emote(
    player_id: uuid.UUID | str,
    emote_command: str,
    ctx: ChatSendServices,
    emote_service: ChatEmoteService | None,
) -> dict[str, object]:
    """
    Send a predefined emote message using the EmoteService.

    This function uses predefined emote definitions to send formatted messages
    to both the player and room occupants.

    Args:
        player_id: ID of the player sending the emote
        emote_command: The emote command (e.g., 'twibble', 'dance')
        ctx: Shared chat delivery services (player/user/rate-limit/log/NATS)
        emote_service: Container-loaded EmoteService (server/container/bundles/game.py)

    Returns:
        Dictionary with success status and message details
    """
    player_id = normalize_player_id(player_id)
    logger.debug(
        "=== CHAT SERVICE DEBUG: send_predefined_emote called ===", player_id=player_id, emote_command=emote_command
    )

    if emote_service is None:
        logger.warning("EmoteService not available for predefined emote")
        return {"success": False, "error": "Emote functionality is not available."}

    if not emote_service.is_emote_alias(emote_command):
        logger.warning("Invalid emote command")
        return {"success": False, "error": f"Unknown emote: {emote_command}"}

    player, room_id, auth_error = await _authorize_emote_sender(player_id, ctx)
    if auth_error or player is None or room_id is None:
        return auth_error or {"success": False, "error": "Player not found"}

    built = _build_and_log_emote_message(player, player_id, room_id, emote_command, emote_service, ctx)
    if isinstance(built, dict):
        return built
    chat_message, self_message, other_message = built

    logger.info(
        "Predefined emote message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        emote_command=emote_command,
        message_id=chat_message.id,
    )

    logger.debug("=== CHAT SERVICE DEBUG: About to publish predefined emote message to NATS ===")
    nats_error = await _publish_chat_or_unavailable(
        chat_message,
        room_id,
        ctx,
        {"player_id": player_id, "player_name": player.name, "room_id": room_id, "message_id": chat_message.id},
    )
    if nats_error:
        return nats_error
    logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

    return {
        "success": True,
        "self_message": self_message,
        "other_message": other_message,
        "message": chat_message.to_dict(),
        "room_id": room_id,
    }


def _register_local_echo_suppression(message_id: str) -> None:
    """Suppress the sender's own echo of a local message they'll already see via this response.

    Near-duplicate of chat_service._register_echo_suppression: chat_service.py imports this
    module at module level, so importing back from it here would cycle; message_filtering
    itself can't be imported at module level for the same reason (see the inline import).
    """
    try:
        from server.realtime.message_filtering import SUPPRESS_ECHO_MESSAGE_IDS
    except ImportError as import_error:  # pragma: no cover - defensive guard for import cycles
        logger.debug(
            "=== CHAT SERVICE DEBUG: Failed to register echo suppression token ===",
            error=str(import_error),
            message_id=message_id,
        )
        return
    SUPPRESS_ECHO_MESSAGE_IDS.add(message_id)
    logger.debug(
        "=== CHAT SERVICE DEBUG: Registered echo suppression token ===",
        message_id=message_id,
        token_count=len(SUPPRESS_ECHO_MESSAGE_IDS),
    )


async def _authorize_local_sender(
    player_id: str, message: str, ctx: ChatSendServices
) -> tuple[ChatPlayerView | None, str | None, ChatResult | None]:
    """Validate the message, resolve the player, and run rate-limit/mute checks.

    Returns (player, room_id, None) on success, or (None, None, error_result).
    """
    error_result = validate_say_message(message)
    if error_result:
        return None, None, error_result

    player = await ctx["player_service"].get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for local message")
        return None, None, {"success": False, "error": "Player not found"}

    _ = ctx["user_manager"].load_player_mutes(player_id)

    if not ctx["rate_limiter"].check_rate_limit(player_id, "local", player.name):
        logger.warning("Rate limit exceeded for local message", player_id=player_id, player_name=player.name)
        return (
            None,
            None,
            {
                "success": False,
                "error": "Rate limit exceeded. Please wait before sending another message.",
                "rate_limited": True,
            },
        )

    room_id = player.current_room_id
    if not room_id:
        logger.warning("Player not in a room")
        return None, None, {"success": False, "error": "Player not in a room"}

    logger.debug("=== CHAT SERVICE DEBUG: Player found ===", player_id=player_id, player_name=player.name)

    permission_error = check_channel_permissions(ctx["user_manager"], player_id, "local")
    if permission_error:
        return None, None, permission_error

    return player, room_id, None


async def send_local_message(player_id: uuid.UUID | str, message: str, ctx: ChatSendServices) -> dict[str, object]:
    """
    Send a local message to players in the same sub-zone.

    This function publishes the message to NATS for real-time distribution
    to all players in the same sub-zone. NATS is mandatory for this functionality.

    Args:
        player_id: ID of the player sending the message
        message: Message content
        ctx: Shared chat delivery services (player/user/rate-limit/room-history/NATS)

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

    player, room_id, auth_error = await _authorize_local_sender(player_id, message, ctx)
    if auth_error or player is None or room_id is None:
        return auth_error or {"success": False, "error": "Player not found"}

    chat_message = create_and_log_chat_message(player_id, player.name, message, room_id, "local")
    ctx["rate_limiter"].record_message(player_id, "local", player.name)
    logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===")

    store_message_in_room_history(ctx["room_messages"], chat_message, room_id, ctx["max_messages_per_room"])

    logger.info(
        "Local message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        message_id=chat_message.id,
    )

    logger.debug("=== CHAT SERVICE DEBUG: About to publish message to NATS ===")
    nats_error = await _publish_chat_or_unavailable(
        chat_message,
        room_id,
        ctx,
        {"player_id": player_id, "player_name": player.name, "room_id": room_id, "message_id": chat_message.id},
    )
    if nats_error:
        return nats_error
    logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

    chat_message.echo_sent = True
    message_dict = chat_message.to_dict()
    message_dict["echo_sent"] = True
    logger.debug(
        "=== CHAT SERVICE DEBUG: Emote message response payload ===",
        payload_keys=list(message_dict.keys()),
    )
    _register_local_echo_suppression(chat_message.id)

    return {"success": True, "message": message_dict, "room_id": room_id}
