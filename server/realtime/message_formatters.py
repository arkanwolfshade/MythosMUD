"""
Message formatting utilities for NATS message handler.
"""

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
        elif channel == "local":
            return f"{sender_name} (local): {content}"
        elif channel == "global":
            return f"{sender_name} (global): {content}"
        elif channel == "emote":
            return f"{sender_name} {content}"
        elif channel == "pose":
            return f"{sender_name} {content}"
        elif channel == "whisper":
            return f"{sender_name} whispers: {content}"
        elif channel == "system":
            return f"[SYSTEM] {content}"
        elif channel == "admin":
            return f"[ADMIN] {sender_name}: {content}"
        else:
            # Default format for unknown channels
            return f"{sender_name} ({channel}): {content}"

    except NATSError as e:
        logger.error("Error formatting message content", error=str(e), channel=channel, sender_name=sender_name)
        return content  # Return original content if formatting fails
