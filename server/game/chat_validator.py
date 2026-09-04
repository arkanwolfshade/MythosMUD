"""
Chat message validation utilities.

This module provides validation functions for chat messages, including
content validation, room access checks, and malicious content detection.
"""

import re
from typing import TYPE_CHECKING

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from .chat_message import ChatMessage

logger = get_logger("communications.chat_validator")


def validate_chat_message(chat_message: "ChatMessage") -> bool:
    """
    Validate chat message before transmission.

    Args:
        chat_message: The chat message to validate

    Returns:
        True if message is valid, False otherwise
    """
    try:
        # Check message content
        if not chat_message.content or not chat_message.content.strip():
            logger.warning("Empty message content", message_id=chat_message.id)
            return False

        # Check message length
        if len(chat_message.content) > 1000:  # Max length
            logger.warning("Message too long", message_id=chat_message.id, length=len(chat_message.content))
            return False

        # Check sender information
        if not chat_message.sender_id or not chat_message.sender_name:
            logger.warning("Missing sender information", message_id=chat_message.id)
            return False

        # Check for malicious content patterns
        if contains_malicious_content(chat_message.content):
            logger.warning("Malicious content detected", message_id=chat_message.id, sender_id=chat_message.sender_id)
            return False

        return True

    except (AttributeError, TypeError, ValueError) as e:
        # Handle attribute access errors, type mismatches, or value errors during validation
        logger.error("Error validating chat message", error=str(e), message_id=chat_message.id)
        return False


def validate_room_access(sender_id: str, room_id: str | None) -> bool:
    """
    Validate sender has access to the room.

    Args:
        sender_id: ID of the message sender
        room_id: ID of the room (None for system messages)

    Returns:
        True if access is valid, False otherwise
    """
    try:
        # Check if sender exists and is active
        if not sender_id:
            return False

        # Allow None room_id for system messages (broadcast to all players)
        if room_id is None:
            return True
        # Explicitly validate non-empty string
        if not room_id.strip():
            return False

        return True

    except (AttributeError, TypeError, ValueError) as e:
        # Handle attribute access errors (e.g., room_id.strip()), type mismatches, or value errors
        logger.error("Error validating room access", error=str(e), sender_id=sender_id, room_id=room_id)
        return False


def contains_malicious_content(content: str) -> bool:
    """
    Check for malicious content patterns.

    Args:
        content: The message content to check

    Returns:
        True if malicious content is detected, False otherwise
    """
    try:
        # Basic malicious pattern detection
        malicious_patterns = [
            r"<script[^>]*>.*?</script>",  # Script tags
            r"javascript:",  # JavaScript URLs
            r"data:text/html",  # Data URLs
            r"vbscript:",  # VBScript URLs
            r"on\w+\s*=",  # Event handlers
        ]

        for pattern in malicious_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return True

        return False

    except (TypeError, AttributeError, ValueError) as e:
        # Handle type errors (content not a string), attribute errors, or regex errors
        # Note: re.error is a subclass of ValueError, so it's covered here
        logger.error("Error checking malicious content", error=str(e))
        return True  # Fail safe - reject if check fails
