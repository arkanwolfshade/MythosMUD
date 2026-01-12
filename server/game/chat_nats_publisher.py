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


def _build_standardized_subject(chat_message: "ChatMessage", room_id: str | None, subject_manager: Any) -> str | None:
    """Build NATS subject using standardized patterns via subject_manager."""
    try:
        match chat_message.channel:
            case "say":
                return cast(str, subject_manager.build_subject("chat_say_room", room_id=room_id))
            case "local":
                subzone = _extract_subzone_from_room(room_id)
                return cast(str, subject_manager.build_subject("chat_local_subzone", subzone=subzone))
            case "global":
                return cast(str, subject_manager.build_subject("chat_global"))
            case "system":
                return cast(str, subject_manager.build_subject("chat_system"))
            case "whisper":
                target_id = getattr(chat_message, "target_id", None)
                if target_id:
                    return cast(str, subject_manager.build_subject("chat_whisper_player", target_id=target_id))
                return "chat.whisper"
            case "emote":
                return cast(str, subject_manager.build_subject("chat_emote_room", room_id=room_id))
            case "pose":
                return cast(str, subject_manager.build_subject("chat_pose_room", room_id=room_id))
            case _:
                return f"chat.{chat_message.channel}.{room_id}"
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
            return "chat.system"
        case "whisper":
            target_id = getattr(chat_message, "target_id", None)
            if target_id:
                return f"chat.whisper.player.{target_id}"
            return "chat.whisper"
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


async def publish_chat_message_to_nats(
    chat_message: "ChatMessage",
    room_id: str | None,
    nats_service: Any,
    subject_manager: Any | None = None,
) -> bool:
    """
    Publish a chat message to NATS for real-time distribution.

    This function publishes the message to the appropriate NATS subject
    for distribution to all subscribers.

    Args:
        chat_message: The chat message to publish
        room_id: The room ID for the message
        nats_service: NATS service instance for publishing
        subject_manager: Optional NATSSubjectManager for subject building

    Returns:
        True if published successfully, False otherwise
    """
    from .chat_validator import validate_chat_message, validate_room_access

    try:
        # Pre-transmission validation
        if not validate_chat_message(chat_message):
            logger.warning("Chat message validation failed", message_id=chat_message.id)
            return False

        if not validate_room_access(chat_message.sender_id, room_id):
            logger.warning("Room access validation failed", sender_id=chat_message.sender_id, room_id=room_id)
            return False

        # Check if NATS service is available and connected
        if not nats_service:
            logger.error(
                "NATS service not available - NATS is mandatory for chat functionality",
                message_id=chat_message.id,
                room_id=room_id,
            )
            return False

        # Check connection status before attempting publish
        if not nats_service.is_connected():
            logger.error(
                "NATS service not connected - NATS is mandatory for chat functionality",
                message_id=chat_message.id,
                room_id=room_id,
                nats_service_type=type(nats_service).__name__,
            )
            return False

        # Check connection pool initialization (if available)
        # Using getattr to avoid accessing protected member directly
        # Default to True if attribute doesn't exist (for services without pooling)
        pool_initialized = getattr(nats_service, "_pool_initialized", True)
        if not pool_initialized:
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

        # Create message data for NATS
        message_data = {
            "message_id": chat_message.id,
            "sender_id": chat_message.sender_id,
            "sender_name": chat_message.sender_name,
            "channel": chat_message.channel,
            "content": chat_message.content,
            "timestamp": chat_message.timestamp.isoformat(),
            "room_id": room_id,
        }

        # Add target information for whisper messages
        if hasattr(chat_message, "target_id") and chat_message.target_id:
            # target_id is guaranteed to be str | None after ChatMessage.__init__
            message_data["target_id"] = chat_message.target_id
        if hasattr(chat_message, "target_name") and chat_message.target_name:
            message_data["target_name"] = chat_message.target_name

        # Build NATS subject using standardized patterns
        subject = build_nats_subject(chat_message, room_id, subject_manager)
        logger.debug(
            "NATS subject determined",
            subject=subject,
            channel=chat_message.channel,
            room_id=room_id,
            using_subject_manager=subject_manager is not None,
        )

        # Publish to NATS
        # Note: publish() returns None on success, raises NATSPublishError on failure
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
        # NATS publish failed with specific error
        logger.error(
            "Failed to publish chat message to NATS",
            error=str(e),
            error_type=type(e).__name__,
            message_id=chat_message.id,
            subject=getattr(e, "subject", None),
            room_id=room_id,
            original_error=str(getattr(e, "original_error", None)) if hasattr(e, "original_error") else None,
        )
        return False

    except (AttributeError, TypeError, ValueError, KeyError, RuntimeError) as e:
        # Unexpected error during publish (attribute access, type issues, value errors, etc.)
        logger.error(
            "Unexpected error publishing chat message to NATS",
            error=str(e),
            error_type=type(e).__name__,
            message_id=chat_message.id,
            room_id=room_id,
            exc_info=True,
        )
        return False
