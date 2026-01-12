"""
Event envelope utilities for MythosMUD real-time messages.

Provides a single, consistent schema for events emitted over WebSocket:
- event_type: str
- timestamp: ISO 8601 UTC with 'Z'
- sequence_number: int (monotonic per-process)
- room_id: optional
- player_id: optional
- data: dict payload

As noted in the Pnakotic Manuscripts, chronology must be preserved lest causality unravel.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event envelope building requires many parameters for complete event context

from __future__ import annotations

import json
import uuid
from datetime import UTC, datetime
from typing import Any


class UUIDEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles UUID objects."""

    def default(self, obj: Any) -> Any:  # pylint: disable=arguments-renamed  # Reason: JSONEncoder interface requires 'obj' parameter name, parent class uses 'o'
        if isinstance(obj, uuid.UUID):
            return str(obj)
        return super().default(obj)


# Global sequence counter for events (when connection_manager not available)
_global_sequence_counter = 0  # pylint: disable=invalid-name  # Reason: Private module-level variable, intentionally uses _ prefix
_sequence_lock = None  # pylint: disable=invalid-name  # Reason: Private module-level variable, intentionally uses _ prefix


def _get_next_global_sequence() -> int:
    """Thread-safe global sequence number generation (fallback when no connection_manager)."""
    import threading

    global _global_sequence_counter, _sequence_lock  # pylint: disable=global-statement  # Reason: Singleton pattern for sequence counter
    if _sequence_lock is None:
        _sequence_lock = threading.Lock()

    with _sequence_lock:
        _global_sequence_counter += 1
        return _global_sequence_counter


def utc_now_z() -> str:
    """Return current UTC time in ISO 8601 format with 'Z' suffix."""
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def build_event(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event building requires many parameters for complete event context
    event_type: str,
    data: dict[str, Any] | None = None,
    *,
    room_id: str | None = None,
    player_id: uuid.UUID | str | None = None,
    sequence_number: int | None = None,
    connection_manager=None,
) -> dict[str, Any]:
    """
    Create a normalized event envelope.

    Args:
        event_type: Type of event
        data: Event data payload
        room_id: Optional room ID for room-scoped events
        player_id: Optional player ID for player-scoped events (UUID or string)
        sequence_number: Optional explicit sequence number
        connection_manager: Optional ConnectionManager for sequence generation

    If sequence_number is not provided and connection_manager is available,
    uses connection_manager's sequence counter. Otherwise uses global fallback.

    AI Agent: connection_manager is now optional parameter instead of global import
    """
    if sequence_number is not None:
        seq = sequence_number
    elif connection_manager is not None:
        seq = connection_manager._get_next_sequence()  # pylint: disable=protected-access  # Reason: Internal sequence number generation required
    else:
        seq = _get_next_global_sequence()  # Fallback for backward compatibility
    event: dict[str, Any] = {
        "event_type": event_type,
        "timestamp": utc_now_z(),
        "sequence_number": seq,
        "data": data or {},
    }
    if room_id is not None:
        event["room_id"] = room_id
    if player_id is not None:
        # Keep UUID as UUID object - JSON serialization will handle it
        event["player_id"] = player_id
    return event
