"""
Test to reproduce the self-message bug where players see their own movement messages.

This test verifies that players do NOT see their own movement messages,
only other players should see them.
"""

from unittest.mock import AsyncMock, Mock

import pytest

from ..events import PlayerEnteredRoom
from ..realtime.connection_manager import ConnectionManager
from ..realtime.event_handler import RealTimeEventHandler


class TestSelfMessageBug:
    """Test that players don't see their own movement messages."""

    @pytest.fixture
    def connection_manager(self):
        """Create a connection manager for testing."""
        cm = ConnectionManager()
        cm.send_personal_message = AsyncMock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.unsubscribe_from_room = AsyncMock()
        return cm

    @pytest.fixture
    def event_handler(self, connection_manager):
        """Create an event handler for testing."""
        return RealTimeEventHandler()

    @pytest.mark.asyncio
    async def test_player_does_not_see_own_entered_message(self, event_handler, connection_manager):
        """Test that a player doesn't see their own 'entered room' message."""
        # Setup
        event_handler.connection_manager = connection_manager

        # Mock player lookup
        mock_player = Mock()
        mock_player.name = "Ithaqua"
        connection_manager._get_player = Mock(return_value=mock_player)

        # Create event for Ithaqua entering a room
        player_id = "ithaqua_player_id"
        room_id = "test_room_001"
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id=player_id, room_id=room_id)

        # Handle the event
        await event_handler._handle_player_entered(event)

        # Verify that broadcast_to_room was called with exclude_player
        connection_manager.broadcast_to_room.assert_called()

        # Get the call arguments with debug output
        call_args_list = connection_manager.broadcast_to_room.call_args_list
        print(f"Number of calls: {len(call_args_list)}")

        # Get the first call (movement message broadcast)
        first_call = call_args_list[0]
        print(f"First call args: {first_call}")
        print(f"First call kwargs: {first_call[1] if len(first_call) > 1 else 'No kwargs'}")
        exclude_player = first_call[1].get("exclude_player")

        # The exclude_player should match the player_id from the event
        assert exclude_player == player_id, f"Expected exclude_player to be {player_id}, got {exclude_player}"
