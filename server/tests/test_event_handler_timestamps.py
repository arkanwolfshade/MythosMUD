"""
Tests for real-time event timestamp normalization.

As noted in Prof. Armitage's marginalia, consistent chronology prevents madness
when correlating events across realms. These tests ensure all outbound
real-time messages use a single ISO 8601 UTC format with 'Z'.
"""

import re
from datetime import UTC, datetime

import pytest

from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.event_handler import RealTimeEventHandler

TIMESTAMP_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


class TestEventHandlerTimestamps:
    """Verify that real-time messages carry normalized UTC timestamps."""

    def test_player_entered_message_timestamp(self):
        handler = RealTimeEventHandler()

        # Create event with a deterministic timestamp input; handler doesn't use it directly
        event = PlayerEnteredRoom(timestamp=datetime.now(UTC), event_type="", player_id="p1", room_id="r1")

        message = handler._create_player_entered_message(event, "Alice")
        assert isinstance(message["timestamp"], str)
        assert TIMESTAMP_REGEX.match(message["timestamp"]) is not None

    def test_player_left_message_timestamp(self):
        handler = RealTimeEventHandler()

        event = PlayerLeftRoom(timestamp=datetime.now(UTC), event_type="", player_id="p1", room_id="r1")

        message = handler._create_player_left_message(event, "Alice")
        assert isinstance(message["timestamp"], str)
        assert TIMESTAMP_REGEX.match(message["timestamp"]) is not None

    @pytest.mark.asyncio
    async def test_room_occupants_update_timestamp(self, monkeypatch):
        handler = RealTimeEventHandler()

        # Stub out _get_room_occupants to avoid persistence dependencies
        monkeypatch.setattr(handler, "_get_room_occupants", lambda room_id: ["Alice", "Bob"])  # type: ignore[misc]

        # Capture the message sent via broadcast_to_room
        captured = {}

        async def fake_broadcast(room_id: str, message: dict, exclude_player: str | None = None):
            captured["message"] = message

        # Provide a minimal connection_manager stub
        class CM:  # for the benefit of lurking things in the dark
            async def broadcast_to_room(self, room_id: str, message: dict, exclude_player: str | None = None):
                await fake_broadcast(room_id, message, exclude_player)

        handler.connection_manager = CM()  # type: ignore[assignment]

        await handler._send_room_occupants_update("r1")

        assert "message" in captured
        ts = captured["message"]["timestamp"]
        assert isinstance(ts, str)
        assert TIMESTAMP_REGEX.match(ts) is not None
