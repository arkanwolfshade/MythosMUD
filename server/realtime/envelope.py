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
from collections.abc import Mapping
from datetime import UTC, datetime
from typing import Protocol, cast, override

from ..constants.message_category import MessageCategory


class _SupportsEventSequence(Protocol):
    """Minimal typing for connection_manager passed to build_event (sequence_counter only)."""

    sequence_counter: int


class UUIDEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles UUID objects."""

    @override
    def default(self, o: object) -> object:
        if isinstance(o, uuid.UUID):
            return str(o)
        return cast(object, super().default(o))


# The ONE process-wide event sequence counter. Every sequence_number sent to a client must come from
# next_event_sequence(): the client rejects a room_occupants update whose seq is <= the last it applied for
# that room, which is only sound if all sources share a single total order. Independent per-source counters
# let whichever ran ahead silently shadow the others (stale occupants panel).
_global_sequence_counter = 0  # pylint: disable=invalid-name  # Reason: Private module-level variable, intentionally uses _ prefix
_sequence_lock = None  # pylint: disable=invalid-name  # Reason: Private module-level variable, intentionally uses _ prefix


def next_event_sequence() -> int:
    """Thread-safe next value of the process-wide event sequence."""
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
    data: Mapping[str, object] | None = None,
    *,
    room_id: str | None = None,
    player_id: uuid.UUID | str | None = None,
    sequence_number: int | None = None,
    connection_manager: _SupportsEventSequence | None = None,
) -> dict[str, object]:
    """
    Create a normalized event envelope.

    Args:
        event_type: Type of event
        data: Event data payload
        room_id: Optional room ID for room-scoped events
        player_id: Optional player ID for player-scoped events (UUID or string)
        sequence_number: Optional explicit sequence number
        connection_manager: Optional object with sequence_counter (see _SupportsEventSequence)

    If sequence_number is not provided the next process-wide sequence is used. When a connection_manager is
    passed, its sequence_counter is set to the value issued ("last issued"), so callers that read it still work.

    AI Agent: connection_manager is now optional parameter instead of global import
    """
    # Prefer explicit sequence_number; otherwise draw from the single process-wide counter.
    if sequence_number is not None:
        seq = sequence_number
    else:
        seq = next_event_sequence()
        if connection_manager is not None:
            connection_manager.sequence_counter = seq
    payload: Mapping[str, object] = {} if data is None else data
    if event_type == "command_response" and "category" not in payload:
        # Shared floor for every direct command_response emitter (follow, party, spell, catch-up, ...);
        # the websocket command chokepoint and chat/look/error paths set a more specific category first.
        payload = {**payload, "category": MessageCategory.COMMAND_OUTPUT}
    event: dict[str, object] = {
        "event_type": event_type,
        "timestamp": utc_now_z(),
        "sequence_number": seq,
        "data": payload,
    }
    if room_id is not None:
        event["room_id"] = room_id
    if player_id is not None:
        # Keep UUID as UUID object - JSON serialization will handle it
        event["player_id"] = player_id
    return event
