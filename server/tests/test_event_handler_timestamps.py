"""
Tests for real-time event timestamp normalization.

As noted in Prof. Armitage's marginalia, consistent chronology prevents madness
when correlating events across realms. These tests ensure all outbound
real-time messages use a single ISO 8601 UTC format with 'Z'.
"""

import re
from datetime import UTC, datetime

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

    def test_timestamp_format_consistency(self):
        """Test that all timestamp formats are consistent across different message types."""
        handler = RealTimeEventHandler()

        # Test multiple events to ensure consistent formatting
        event1 = PlayerEnteredRoom(timestamp=datetime.now(UTC), event_type="", player_id="p1", room_id="r1")
        event2 = PlayerLeftRoom(timestamp=datetime.now(UTC), event_type="", player_id="p2", room_id="r1")

        message1 = handler._create_player_entered_message(event1, "Alice")
        message2 = handler._create_player_left_message(event2, "Bob")

        # Both should have the same timestamp format
        assert TIMESTAMP_REGEX.match(message1["timestamp"]) is not None
        assert TIMESTAMP_REGEX.match(message2["timestamp"]) is not None

        # Verify both follow the exact same format pattern
        assert len(message1["timestamp"]) == len(message2["timestamp"])
        assert message1["timestamp"].endswith("Z")
        assert message2["timestamp"].endswith("Z")

        # Verify the format structure is consistent
        assert message1["timestamp"][-1] == "Z"  # Both end with Z
        assert message2["timestamp"][-1] == "Z"  # Both end with Z

        # Verify the timestamp format structure (YYYY-MM-DDTHH:MM:SSZ)
        assert len(message1["timestamp"]) == 20  # 19 chars + Z
        assert message1["timestamp"][4] == "-"  # Year-month separator
        assert message1["timestamp"][7] == "-"  # Month-day separator
        assert message1["timestamp"][10] == "T"  # Date-time separator
        assert message1["timestamp"][13] == ":"  # Hour-minute separator
        assert message1["timestamp"][16] == ":"  # Minute-second separator
