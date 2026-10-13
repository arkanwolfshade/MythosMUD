"""
Styled spans inside one message line (#1025, slice 2).

A text event may carry ``segments`` next to its ``message``: an ordered list of ``{text, category?}`` spans whose
``text`` values concatenate to exactly ``message``. A span with no ``category`` takes the line's own. ``message`` is
never replaced: search, history, the E2E ``data-message-text`` attribute and screen readers all keep reading it, so
the client may drop ``segments`` (for example when corruption decay rewrites the line) and lose colour, never words.

Build a line from parts with ``message_with_segments``; the join invariant then holds by construction.

Import-free apart from sibling constants, like ``message_category.py``.
"""

from typing import NotRequired, TypedDict

from .message_category import MessageCategory
from .npc_disposition import NpcDisposition


class MessageSegment(TypedDict):
    """One span of a line; ``category`` is a ``MessageCategory`` value, omitted for the line's own."""

    text: str
    category: NotRequired[str]


SegmentPart = str | MessageSegment
"""A plain string, or a styled span, as a line is assembled."""


class SegmentedMessage(TypedDict):
    """The two keys a segmented text event adds to its payload."""

    message: str
    segments: list[MessageSegment]


def npc_name_segment(name: str, disposition: NpcDisposition) -> MessageSegment:
    """An NPC's name styled by its ``npc.<disposition>`` category. Phantoms pass ``AGGRESSIVE_MOB`` (ADR-024)."""
    return {"text": name, "category": MessageCategory(f"npc.{disposition.value}").value}


def default_name_line(line: str, name: str, rest: str, disposition: NpcDisposition) -> list[SegmentPart]:
    """
    ``[styled name, rest]`` when ``line`` is exactly the server's own default ``<name><rest>``.

    Authored text (an NPC's ``behavior_config`` messages) has no name placeholder, so it is never guessed at: it stays
    one plain part.
    """
    return [npc_name_segment(name, disposition), rest] if line == f"{name}{rest}" else [line]


def join_parts(parts: list[SegmentPart]) -> str:
    """The plain text of a line assembled from parts."""
    return "".join(part if isinstance(part, str) else part["text"] for part in parts)


def message_with_segments(parts: list[SegmentPart]) -> SegmentedMessage:
    """``message`` plus ``segments`` for a line built from parts; adjacent plain strings merge into one span."""
    segments: list[MessageSegment] = []
    for part in parts:
        span: MessageSegment = {"text": part} if isinstance(part, str) else part
        if not span["text"]:
            continue
        if "category" not in span and segments and "category" not in segments[-1]:
            segments[-1] = {"text": segments[-1]["text"] + span["text"]}
        else:
            segments.append(span)
    return {"message": join_parts(parts), "segments": segments}
