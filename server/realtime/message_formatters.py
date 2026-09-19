"""
Message formatting utilities for NATS message handler.
"""

# pylint: disable=too-many-return-statements  # Reason: Message formatting requires multiple return statements for different channel types and formatting logic

from typing import TYPE_CHECKING

from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from collections.abc import Callable

logger = get_logger("communications.message_formatters")

# Channel -> formatter(sender_name, content). Whisper is handled separately since its format
# also depends on `for_recipient`.
_CHANNEL_FORMATTERS: dict[str, "Callable[[str, str], str]"] = {
    "say": lambda sender_name, content: f"{sender_name} says: {content}",
    "local": lambda sender_name, content: f"{sender_name} (local): {content}",
    "global": lambda sender_name, content: f"{sender_name} (global): {content}",
    "emote": lambda sender_name, content: f"{sender_name} {content}",
    "pose": lambda sender_name, content: f"{sender_name} {content}",
    "system": lambda _sender_name, content: f"[SYSTEM] {content}",
    "admin": lambda sender_name, content: f"[ADMIN] {sender_name}: {content}",
}


def format_message_content(channel: str, sender_name: str, content: str, *, for_recipient: bool = False) -> str:
    """
    Format message content based on channel type and sender name.

    Args:
        channel: Channel type (say, local, emote, pose, global, party, whisper, system, admin)
        sender_name: Name of the message sender
        content: Raw message content
        for_recipient: When True and channel is whisper, format as "X whispers to you: Y"
            for the recipient. Ignored for other channels.

    Returns:
        Formatted message content with sender name
    """
    try:
        if channel == "whisper":
            if for_recipient:
                return f"{sender_name} whispers to you: {content}"
            return f"{sender_name} whispers: {content}"
        formatter = _CHANNEL_FORMATTERS.get(channel)
        if formatter is not None:
            return formatter(sender_name, content)
        # Default format for unknown channels
        return f"{sender_name} ({channel}): {content}"

    except NATSError as e:
        logger.error("Error formatting message content", error=str(e), channel=channel, sender_name=sender_name)
        return content  # Return original content if formatting fails
