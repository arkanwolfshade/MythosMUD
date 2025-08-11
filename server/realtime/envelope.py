"""
Event envelope utilities for MythosMUD real-time messages.

Provides a single, consistent schema for events emitted over both SSE and WebSocket:
- event_type: str
- timestamp: ISO 8601 UTC with 'Z'
- sequence_number: int (monotonic per-process)
- room_id: optional
- player_id: optional
- data: dict payload

As noted in the Pnakotic Manuscripts, chronology must be preserved lest causality unravel.
"""

from __future__ import annotations

import json
from datetime import UTC, datetime
from typing import Any

# Importing here avoids circular imports (connection_manager does not import this module)
from .connection_manager import connection_manager


def utc_now_z() -> str:
    """Return current UTC time in ISO 8601 format with 'Z' suffix."""
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def build_event(
    event_type: str,
    data: dict[str, Any] | None = None,
    *,
    room_id: str | None = None,
    player_id: str | None = None,
    sequence_number: int | None = None,
) -> dict[str, Any]:
    """Create a normalized event envelope.

    If sequence_number is not provided, a global monotonic value is assigned.
    """

    seq = sequence_number if sequence_number is not None else connection_manager._get_next_sequence()  # noqa: SLF001
    event: dict[str, Any] = {
        "event_type": event_type,
        "timestamp": utc_now_z(),
        "sequence_number": seq,
        "data": data or {},
    }
    if room_id is not None:
        event["room_id"] = room_id
    if player_id is not None:
        event["player_id"] = player_id
    return event


def sse_line(event: dict[str, Any]) -> str:
    """Encode an event dict as an SSE data line."""
    return f"data: {json.dumps(event)}\n\n"
