"""
Simple tests to investigate WebSocket connection event firing issues.

This test suite focuses on the core event publishing mechanism without complex async mocking.
"""

from unittest.mock import Mock

from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models.room import Room


class TestSimpleConnectionEvents:
    """Simple tests for connection event firing."""

    def test_room_player_entered_publishes_event(self):
        """Test that Room.player_entered publishes PlayerEnteredRoom event."""
        # Create mock event bus
        mock_event_bus = Mock()
        mock_event_bus.publish = Mock()

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, mock_event_bus)

        # Call player_entered
        room.player_entered("test_player_123")

        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        published_event = mock_event_bus.publish.call_args[0][0]
        assert isinstance(published_event, PlayerEnteredRoom)
        assert published_event.player_id == "test_player_123"
        assert published_event.room_id == "test_room_001"

    def test_room_player_left_publishes_event(self):
        """Test that Room.player_left publishes PlayerLeftRoom event."""
        # Create mock event bus
        mock_event_bus = Mock()
        mock_event_bus.publish = Mock()

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, mock_event_bus)

        # First add player to room
        room.player_entered("test_player_123")
        mock_event_bus.publish.reset_mock()  # Clear the enter event

        # Then remove player from room
        room.player_left("test_player_123")

        # Verify event was published
        mock_event_bus.publish.assert_called_once()
        published_event = mock_event_bus.publish.call_args[0][0]
        assert isinstance(published_event, PlayerLeftRoom)
        assert published_event.player_id == "test_player_123"
        assert published_event.room_id == "test_room_001"

    def test_room_without_event_bus_handles_gracefully(self):
        """Test that Room works without event bus (should not crash)."""
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data)  # No event bus

        # Should not crash
        room.player_entered("test_player_123")
        room.player_left("test_player_123")

        # Verify player was added and removed
        assert not room.has_player("test_player_123")

    def test_event_types_have_correct_attributes(self):
        """Test that event types have the correct attributes."""
        # Test PlayerEnteredRoom
        entered_event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player", room_id="test_room")
        assert entered_event.player_id == "test_player"
        assert entered_event.room_id == "test_room"
        assert entered_event.event_type == "PlayerEnteredRoom"

        # Test PlayerLeftRoom
        left_event = PlayerLeftRoom(timestamp=None, event_type="", player_id="test_player", room_id="test_room")
        assert left_event.player_id == "test_player"
        assert left_event.room_id == "test_room"
        assert left_event.event_type == "PlayerLeftRoom"
