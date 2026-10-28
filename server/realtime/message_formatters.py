"""
Message formatting utilities for NATS message handler.
"""

# pylint: disable=too-many-return-statements  # Reason: Message formatting requires multiple return statements for different channel types and formatting logic

from typing import TYPE_CHECKING

from ..constants.message_segments import (
    MessageSegment,
    SegmentPart,
    join_parts,
    message_with_segments,
    npc_name_segment,
)
from ..constants.npc_disposition import NpcDisposition
from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from collections.abc import Callable

logger = get_logger("communications.message_formatters")

# Channel -> parts(sender, content). The sender and the content are parts so either can carry a styled span (#1036).
# Whisper is handled separately since its format also depends on `for_recipient`.
_CHANNEL_PARTS: dict[str, "Callable[[SegmentPart, list[SegmentPart]], list[SegmentPart]]"] = {
    "say": lambda sender, content: [sender, " says: ", *content],
    "local": lambda sender, content: [sender, " (local): ", *content],
    "global": lambda sender, content: [sender, " (global): ", *content],
    "emote": lambda sender, content: [sender, " ", *content],
    "pose": lambda sender, content: [sender, " ", *content],
    "system": lambda _sender, content: ["[SYSTEM] ", *content],
    "quest": lambda _sender, content: ["[QUEST] ", *content],
    "admin": lambda sender, content: ["[ADMIN] ", sender, ": ", *content],
}


def format_message_parts(
    channel: str, sender: SegmentPart, content: list[SegmentPart], *, for_recipient: bool = False
) -> list[SegmentPart]:
    """The formatted line for a channel, as parts: the single source of truth for ``format_message_content``."""
    if channel == "whisper":
        return [sender, " whispers to you: " if for_recipient else " whispers: ", *content]
    formatter = _CHANNEL_PARTS.get(channel)
    if formatter is not None:
        return formatter(sender, content)
    # Default format for unknown channels
    return [sender, f" ({channel}): ", *content]


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
        # f-string coercion keeps the historical behaviour for non-str arguments (they were always interpolated).
        parts = format_message_parts(channel, f"{sender_name}", [f"{content}"], for_recipient=for_recipient)
        return join_parts(parts)

    except NATSError as e:
        logger.error("Error formatting message content", error=str(e), channel=channel, sender_name=sender_name)
        return content  # Return original content if formatting fails


def disposition_or_none(raw: object) -> NpcDisposition | None:
    """An ``NpcDisposition`` from a wire string, or None when absent or unrecognised (the name then stays plain)."""
    try:
        return NpcDisposition(raw) if isinstance(raw, str) else None
    except ValueError:
        return None


def format_message_segments(
    channel: str,
    sender_name: str,
    content: str,
    *,
    speaker_disposition: NpcDisposition | None = None,
    content_segments: list[MessageSegment] | None = None,
    for_recipient: bool = False,
) -> list[MessageSegment] | None:
    """
    The styled spans of the formatted line, or None when nothing in it is styled (#1036).

    ``speaker_disposition`` styles the sender's name (an NPC speaking). ``content_segments`` are spans that already
    describe ``content`` exactly; the caller drops them if the content has since been rewritten. Joined, the spans
    equal ``format_message_content`` for the same arguments.
    """
    sender: SegmentPart = (
        npc_name_segment(sender_name, speaker_disposition) if speaker_disposition is not None else sender_name
    )
    body: list[SegmentPart] = [*content_segments] if content_segments else [content]
    segments = message_with_segments(format_message_parts(channel, sender, body, for_recipient=for_recipient))[
        "segments"
    ]
    return segments if any("category" in segment for segment in segments) else None
