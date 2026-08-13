"""Room-scoped message senders (say, local, custom/predefined emote)."""

# pylint: disable=too-many-return-statements,too-many-lines  # Reason: Message sending handlers require multiple return statements for early validation returns (permission checks, validation, error handling). Message sending requires extensive handlers for multiple message types and delivery methods.

import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .chat_channel_message_senders import (
    normalize_player_id,
    send_global_message,
    send_party_message,
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
    check_say_permissions,
    validate_emote_action,
    validate_say_message,
)

logger = get_logger("communications.chat_message_senders")

# Pairs room history store with its cap so senders stay under parameter-count limits.
RoomChatHistory = tuple[dict[str, list[ChatMessage]], int]

__all__ = [
    "normalize_player_id",
    "send_emote_message",
    "send_global_message",
    "send_local_message",
    "send_party_message",
    "send_predefined_emote",
    "send_say_message",
    "send_system_message",
    "send_whisper_message",
]


async def _resolve_predefined_emote_sender(
    player_id: str,
    emote_command: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    emote_service: Any,
) -> dict[str, Any] | tuple[Any, str]:
    """Validate emote sender; return error dict or (player, room_id)."""
    if not emote_service.is_emote_alias(emote_command):
        logger.warning("Invalid emote command")
        return {"success": False, "error": f"Unknown emote: {emote_command}"}

    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning("Player not found for predefined emote")
        return {"success": False, "error": "Player not found"}

    user_manager.load_player_mutes(player_id)

    if not rate_limiter.check_rate_limit(player_id, "emote", player.name):
        logger.warning("Rate limit exceeded for predefined emote", player_id=player_id, player_name=player.name)
        return {
            "success": False,
            "error": "Rate limit exceeded. Please wait before sending another emote.",
            "rate_limited": True,
        }

    room_id = player.current_room_id
    if not room_id:
        logger.warning("Player not in a room")
        return {"success": False, "error": "Player not in a room"}

    # Emotes share say-channel mute / global mute / can_send rules
    error_result = check_say_permissions(user_manager, player_id)
    if error_result:
        return error_result

    return player, room_id


def _log_predefined_emote_message(chat_logger: Any, chat_message: ChatMessage, room_id: str) -> None:
    """Log emote chat payload for AI processing."""
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


async def _publish_predefined_emote(
    player_id: str,
    player: Any,
    room_id: str,
    emote_command: str,
    emote_service: Any,
    chat_logger: Any,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """Format, log, and NATS-publish a predefined emote; return API payload."""
    try:
        self_message, other_message = emote_service.format_emote_messages(emote_command, player.name)
    except ValueError as e:
        logger.error("Failed to format emote messages", player_id=player_id, emote_command=emote_command, error=str(e))
        return {"success": False, "error": str(e)}

    # ChatMessage accepts UUID | str and converts internally
    chat_message = ChatMessage(sender_id=player_id, sender_name=player.name, channel="emote", content=other_message)
    _log_predefined_emote_message(chat_logger, chat_message, room_id)
    logger.info(
        "Predefined emote message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        emote_command=emote_command,
        message_id=chat_message.id,
    )

    logger.debug("=== CHAT SERVICE DEBUG: About to publish predefined emote message to NATS ===")
    if not await publish_chat_message_to_nats(chat_message, room_id, nats_service, subject_manager):
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


async def send_predefined_emote(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Emote sending requires many collaborator services and intermediates
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

    emote_service = EmoteService()
    resolved = await _resolve_predefined_emote_sender(
        player_id, emote_command, player_service, user_manager, rate_limiter, emote_service
    )
    if isinstance(resolved, dict):
        return resolved
    player, room_id = resolved

    return await _publish_predefined_emote(
        player_id, player, room_id, emote_command, emote_service, chat_logger, nats_service, subject_manager
    )


async def _resolve_room_chat_sender(
    player_id: str,
    message: str,
    channel: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    not_found_log: str,
    *,
    validate_content: bool = True,
) -> dict[str, Any] | tuple[Any, str]:
    """Validate room chat sender; return error dict or (player, room_id)."""
    # Emotes use validate_emote_action first; skip say content rules for that path.
    if validate_content:
        error_result = validate_say_message(message)
        if error_result:
            return error_result

    player = await player_service.get_player_by_id(player_id)
    if not player:
        logger.warning(not_found_log)
        return {"success": False, "error": "Player not found"}

    user_manager.load_player_mutes(player_id)

    if not rate_limiter.check_rate_limit(player_id, channel, player.name):
        logger.warning(
            "Rate limit exceeded for message",
            player_id=player_id,
            player_name=player.name,
            channel=channel,
        )
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
    return player, room_id


def _register_echo_suppression(message_id: str) -> None:
    """Register message id for sender echo suppression; tolerate import cycles."""
    # Deferred import: message_filtering can pull chat services (circular during startup).
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


async def _publish_room_chat_response(
    chat_message: ChatMessage,
    player_id: str,
    player_name: str,
    room_id: str,
    nats_service: Any,
    subject_manager: Any | None,
    *,
    include_echo_sent_in_dict: bool = False,
) -> dict[str, Any]:
    """Publish chat message to NATS and build the API success payload."""
    logger.debug("=== CHAT SERVICE DEBUG: About to publish message to NATS ===")
    success = await publish_chat_message_to_nats(chat_message, room_id, nats_service, subject_manager)
    if not success:
        logger.error(
            "NATS publishing failed - NATS is mandatory for chat functionality",
            player_id=player_id,
            player_name=player_name,
            room_id=room_id,
            message_id=chat_message.id,
        )
        return {"success": False, "error": "Chat system temporarily unavailable. Please try again in a moment."}
    logger.debug("=== CHAT SERVICE DEBUG: NATS publishing completed ===")

    chat_message.echo_sent = True
    message_dict = chat_message.to_dict()
    if include_echo_sent_in_dict:
        message_dict["echo_sent"] = True
        logger.debug(
            "=== CHAT SERVICE DEBUG: Emote message response payload ===",
            payload_keys=list(message_dict.keys()),
        )
    _register_echo_suppression(chat_message.id)
    return {"success": True, "message": message_dict, "room_id": room_id}


async def send_local_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many collaborator services
    player_id: uuid.UUID | str,
    message: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    room_history: RoomChatHistory,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """Send a local (sub-zone) message via NATS. Returns success status and message details."""
    player_id = normalize_player_id(player_id)
    room_messages, max_messages_per_room = room_history
    logger.debug(
        "=== CHAT SERVICE DEBUG: send_local_message called ===",
        player_id=player_id,
        message=message,
    )
    logger.debug("Processing local message")

    resolved = await _resolve_room_chat_sender(
        player_id, message, "local", player_service, user_manager, rate_limiter, "Player not found for local message"
    )
    if isinstance(resolved, dict):
        return resolved
    player, room_id = resolved

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

    return await _publish_room_chat_response(
        chat_message,
        player_id,
        player.name,
        room_id,
        nats_service,
        subject_manager,
        include_echo_sent_in_dict=True,
    )


async def send_say_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many collaborator services
    player_id: uuid.UUID | str,
    message: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    room_history: RoomChatHistory,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """Send a say (same-room) message via NATS. Returns success status and message details."""
    player_id = normalize_player_id(player_id)
    room_messages, max_messages_per_room = room_history
    logger.debug("=== CHAT SERVICE DEBUG: send_say_message called ===", player_id=player_id, message=message)
    logger.debug("Processing say message")

    resolved = await _resolve_room_chat_sender(
        player_id, message, "say", player_service, user_manager, rate_limiter, "Player not found for chat message"
    )
    if isinstance(resolved, dict):
        return resolved
    player, room_id = resolved

    error_result = check_say_permissions(user_manager, player_id)
    if error_result:
        return error_result

    chat_message = create_and_log_chat_message(player_id, player.name, message, room_id, "say")
    rate_limiter.record_message(player_id, "say", player.name)
    logger.debug("=== CHAT SERVICE DEBUG: Chat message created ===")
    store_message_in_room_history(room_messages, chat_message, room_id, max_messages_per_room)
    logger.info(
        "Say message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        message_id=chat_message.id,
    )

    logger.debug(
        "Chat service NATS service status",
        nats_service_object=nats_service,
        nats_service_type=type(nats_service).__name__,
        nats_connected=nats_service.is_connected() if nats_service else False,
    )

    return await _publish_room_chat_response(
        chat_message, player_id, player.name, room_id, nats_service, subject_manager
    )


async def send_emote_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many collaborator services
    player_id: uuid.UUID | str,
    action: str,
    player_service: Any,
    user_manager: Any,
    rate_limiter: Any,
    room_history: RoomChatHistory,
    nats_service: Any,
    subject_manager: Any | None,
) -> dict[str, Any]:
    """Send a custom room emote via NATS. Returns success status and message details."""
    player_id = normalize_player_id(player_id)
    room_messages, max_messages_per_room = room_history
    logger.debug("=== CHAT SERVICE DEBUG: send_emote_message called ===", player_id=player_id, action=action)
    logger.debug("Processing emote message")

    error_result = validate_emote_action(action)
    if error_result:
        return error_result

    resolved = await _resolve_room_chat_sender(
        player_id,
        action,
        "emote",
        player_service,
        user_manager,
        rate_limiter,
        "Player not found for emote message",
        validate_content=False,
    )
    if isinstance(resolved, dict):
        if resolved.get("rate_limited"):
            resolved["error"] = "Rate limit exceeded. Please wait before sending another emote."
        return resolved
    player, room_id = resolved

    error_result = check_channel_permissions(user_manager, player_id, "say")
    if error_result:
        return error_result

    chat_message = create_and_log_chat_message(player_id, player.name, action, room_id, "emote")
    rate_limiter.record_message(player_id, "emote", player.name)
    logger.debug("=== CHAT SERVICE DEBUG: Emote message created ===", message_id=chat_message.id)
    store_message_in_room_history(room_messages, chat_message, room_id, max_messages_per_room)
    logger.info(
        "Emote message created successfully",
        player_id=player_id,
        player_name=player.name,
        room_id=room_id,
        message_id=chat_message.id,
    )

    return await _publish_room_chat_response(
        chat_message, player_id, player.name, room_id, nats_service, subject_manager
    )
