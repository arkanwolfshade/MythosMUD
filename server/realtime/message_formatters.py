"""
Message formatting utilities for NATS message handler.
"""

# pylint: disable=too-many-return-statements  # Reason: Message formatting requires multiple return statements for different channel types and formatting logic

from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("communications.message_formatters")


def format_message_content(channel: str, sender_name: str, content: str) -> str:
    """
    Format message content based on channel type and sender name.

    Args:
        channel: Channel type (say, local, emote, pose, global, party, whisper, system, admin)
        sender_name: Name of the message sender
        content: Raw message content

    Returns:
        Formatted message content with sender name
    """
    try:
        if channel == "say":
            return f"{sender_name} says: {content}"
        if channel == "local":
            return f"{sender_name} (local): {content}"
        if channel == "global":
            return f"{sender_name} (global): {content}"
        if channel == "emote":
            return f"{sender_name} {content}"
        if channel == "pose":
            return f"{sender_name} {content}"
        if channel == "whisper":
            return f"{sender_name} whispers: {content}"
        if channel == "system":
            return f"[SYSTEM] {content}"
        if channel == "admin":
            return f"[ADMIN] {sender_name}: {content}"
        # Default format for unknown channels
        return f"{sender_name} ({channel}): {content}"

    except NATSError as e:
        logger.error("Error formatting message content", error=str(e), channel=channel, sender_name=sender_name)
        return content  # Return original content if formatting fails
