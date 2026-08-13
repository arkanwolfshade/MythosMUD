"""
Chat NATS publishing utilities.

This module provides NATS subject building and message publishing functionality
for chat messages, handling standardized subject patterns and NATS connectivity.
"""

# pylint: disable=too-many-return-statements  # Reason: NATS publishing methods require multiple return statements for early validation returns (subject validation, connection checks, error handling)

from typing import TYPE_CHECKING, Any, cast

from ..services.nats_exceptions import NATSPublishError
from ..services.nats_subject_manager import SubjectValidationError
from ..structured_logging.enhanced_logging_config import get_logger
from .chat_validator import validate_chat_message, validate_room_access

if TYPE_CHECKING:
    from .chat_message import ChatMessage

logger = get_logger("communications.chat_nats_publisher")


def _extract_subzone_from_room(room_id: str | None) -> str:
    """Extract subzone from room_id, returning 'unknown' if extraction fails."""
    from ..utils.room_utils import extract_subzone_from_room_id

    if room_id is None:
        return "unknown"
    subzone_result = extract_subzone_from_room_id(room_id)
    return subzone_result if subzone_result else "unknown"


def _subject_whisper_standardized(chat_message: "ChatMessage", subject_manager: Any) -> str:
    """Build whisper subject; returns fallback 'chat.whisper' if no target_id."""
    target_id = getattr(chat_message, "target_id", None)
    if target_id:
        return cast(str, subject_manager.build_subject("chat_whisper_player", target_id=target_id))
    return "chat.whisper"


def _subject_party_standardized(chat_message: "ChatMessage", subject_manager: Any) -> str | None:
    """Build party subject; returns None if no party_id."""
    party_id = getattr(chat_message, "party_id", None)
    if party_id:
        return cast(str, subject_manager.build_subject("chat_party_group", party_id=party_id))
    return None


def _subject_system_standardized(chat_message: "ChatMessage", subject_manager: Any) -> str | None:
    """System subject; personal system (quest lifecycle) routes like whisper when target_id is set."""
    if getattr(chat_message, "target_id", None):
        return _subject_whisper_standardized(chat_message, subject_manager)
    return cast(str, subject_manager.build_subject("chat_system"))


def _build_standardized_subject(chat_message: "ChatMessage", room_id: str | None, subject_manager: Any) -> str | None:
    """Build NATS subject using standardized patterns via subject_manager."""
    try:
        channel = chat_message.channel
        if channel == "say":
            return cast(str, subject_manager.build_subject("chat_say_room", room_id=room_id))
        if channel == "local":
            subzone = _extract_subzone_from_room(room_id)
            return cast(str, subject_manager.build_subject("chat_local_subzone", subzone=subzone))
        if channel == "global":
            return cast(str, subject_manager.build_subject("chat_global"))
        if channel == "system":
            return _subject_system_standardized(chat_message, subject_manager)
        if channel == "whisper":
            return _subject_whisper_standardized(chat_message, subject_manager)
        if channel == "emote":
            return cast(str, subject_manager.build_subject("chat_emote_room", room_id=room_id))
        if channel == "pose":
            return cast(str, subject_manager.build_subject("chat_pose_room", room_id=room_id))
        if channel == "party":
            return _subject_party_standardized(chat_message, subject_manager)
        return f"chat.{channel}.{room_id}"
    except (ValueError, TypeError, KeyError, SubjectValidationError) as e:
        logger.warning(
            "Failed to build subject with NATSSubjectManager, falling back to legacy construction",
            error=str(e),
            channel=chat_message.channel,
            room_id=room_id,
        )
        return None


def _build_legacy_subject(chat_message: "ChatMessage", room_id: str | None) -> str:
    """Build NATS subject using legacy construction (backward compatibility)."""
    match chat_message.channel:
        case "local":
            subzone = _extract_subzone_from_room(room_id)
            return f"chat.local.subzone.{subzone}"
        case "global":
            return "chat.global"
        case "system":
            target_id = getattr(chat_message, "target_id", None)
            if target_id:
                return f"chat.whisper.player.{target_id}"
            return "chat.system"
        case "whisper":
            target_id = getattr(chat_message, "target_id", None)
            if target_id:
                return f"chat.whisper.player.{target_id}"
            return "chat.whisper"
        case "party":
            party_id = getattr(chat_message, "party_id", None)
            if party_id:
                return f"chat.party.group.{party_id}"
            return "chat.party.group.unknown"
        case _:
            return f"chat.{chat_message.channel}.{room_id}"


def build_nats_subject(chat_message: "ChatMessage", room_id: str | None, subject_manager: Any | None = None) -> str:
    """
    Build NATS subject using standardized patterns or fallback to legacy construction.

    Args:
        chat_message: The chat message to build subject for
        room_id: The room ID for the message
        subject_manager: Optional NATSSubjectManager instance for standardized patterns

    Returns:
        NATS subject string
    """
    if subject_manager:
        standardized_subject = _build_standardized_subject(chat_message, room_id, subject_manager)
        if standardized_subject is not None:
            return standardized_subject

    # Fall back to legacy construction
    return _build_legacy_subject(chat_message, room_id)


def _nats_service_ready(nats_service: Any, chat_message: "ChatMessage", room_id: str | None) -> bool:
    """Return True when NATS is present, connected, and pool-ready."""
    if not nats_service:
        logger.error(
            "NATS service not available - NATS is mandatory for chat functionality",
            message_id=chat_message.id,
            room_id=room_id,
        )
        return False
    if not nats_service.is_connected():
        logger.error(
            "NATS service not connected - NATS is mandatory for chat functionality",
            message_id=chat_message.id,
            room_id=room_id,
            nats_service_type=type(nats_service).__name__,
        )
        return False
    # Default True when attribute missing (services without pooling).
    if not getattr(nats_service, "_pool_initialized", True):
        logger.error(
            "NATS connection pool not initialized - cannot publish",
            message_id=chat_message.id,
            room_id=room_id,
        )
        return False
    logger.debug(
        "NATS service available and connected",
        nats_service_type=type(nats_service).__name__,
        nats_connected=True,
        message_id=chat_message.id,
    )
    return True


def _build_nats_message_data(chat_message: "ChatMessage", room_id: str | None) -> dict[str, Any]:
    """Build the NATS payload dict for a chat message."""
    message_data: dict[str, Any] = {
        "message_id": chat_message.id,
        "sender_id": chat_message.sender_id,
        "sender_name": chat_message.sender_name,
        "channel": chat_message.channel,
        "content": chat_message.content,
        "timestamp": chat_message.timestamp.isoformat(),
        "room_id": room_id,
    }
    if getattr(chat_message, "target_id", None):
        message_data["target_id"] = chat_message.target_id
    if getattr(chat_message, "target_name", None):
        message_data["target_name"] = chat_message.target_name
    if getattr(chat_message, "party_id", None):
        message_data["party_id"] = chat_message.party_id
    speaker_kind = getattr(chat_message, "speaker_kind", None)
    if speaker_kind:
        message_data["speaker_kind"] = speaker_kind
    return message_data


def _chat_passes_nats_validation(chat_message: "ChatMessage", room_id: str | None) -> bool:
    """Return True when message content and room access checks pass."""
    if not validate_chat_message(chat_message):
        logger.warning("Chat message validation failed", message_id=chat_message.id)
        return False
    if not validate_room_access(chat_message.sender_id, room_id):
        logger.warning("Room access validation failed", sender_id=chat_message.sender_id, room_id=room_id)
        return False
    return True


def _log_nats_publish_error(error: NATSPublishError, chat_message: "ChatMessage", room_id: str | None) -> None:
    """Log a NATSPublishError from chat publish."""
    logger.error(
        "Failed to publish chat message to NATS",
        error=str(error),
        error_type=type(error).__name__,
        message_id=chat_message.id,
        subject=getattr(error, "subject", None),
        room_id=room_id,
        original_error=str(getattr(error, "original_error", None)) if hasattr(error, "original_error") else None,
    )


def _log_nats_unexpected_error(error: Exception, chat_message: "ChatMessage", room_id: str | None) -> None:
    """Log an unexpected failure from chat publish."""
    logger.error(
        "Unexpected error publishing chat message to NATS",
        error=str(error),
        error_type=type(error).__name__,
        message_id=chat_message.id,
        room_id=room_id,
        exc_info=True,
    )


async def publish_chat_message_to_nats(
    chat_message: "ChatMessage",
    room_id: str | None,
    nats_service: Any,
    subject_manager: Any | None = None,
) -> bool:
    """Publish a chat message to NATS for real-time distribution."""
    try:
        if not _chat_passes_nats_validation(chat_message, room_id):
            return False
        if not _nats_service_ready(nats_service, chat_message, room_id):
            return False

        message_data = _build_nats_message_data(chat_message, room_id)
        subject = build_nats_subject(chat_message, room_id, subject_manager)
        logger.debug(
            "NATS subject determined",
            subject=subject,
            channel=chat_message.channel,
            room_id=room_id,
            using_subject_manager=subject_manager is not None,
        )

        # publish() returns None on success, raises NATSPublishError on failure
        await nats_service.publish(subject, message_data)
        logger.info(
            "Chat message published to NATS successfully",
            message_id=chat_message.id,
            subject=subject,
            sender_id=chat_message.sender_id,
            room_id=room_id,
        )
        return True
    except NATSPublishError as e:
        _log_nats_publish_error(e, chat_message, room_id)
        return False
    except (AttributeError, TypeError, ValueError, KeyError, RuntimeError) as e:
        _log_nats_unexpected_error(e, chat_message, room_id)
        return False
