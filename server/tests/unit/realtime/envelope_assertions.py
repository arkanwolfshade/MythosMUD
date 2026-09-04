"""Shared contract assertions for realtime event envelopes produced via build_event."""

from __future__ import annotations

from typing import Any


def assert_event_envelope(
    event: dict[str, Any],
    *,
    event_type: str,
    require_player_id: bool = False,
    require_room_id: bool = False,
) -> None:
    """Assert a fan-out producer event matches the build_event envelope shape."""
    assert isinstance(event, dict)
    assert event.get("event_type") == event_type
    assert "timestamp" in event
    assert isinstance(event.get("timestamp"), str)
    assert "sequence_number" in event
    assert isinstance(event.get("sequence_number"), int)
    assert "data" in event
    assert isinstance(event.get("data"), dict)
    if require_player_id:
        assert "player_id" in event
        assert event["player_id"] is not None
    if require_room_id:
        assert "room_id" in event
        assert event["room_id"] is not None
