"""
Test self-message exclusion for movement events.

This test verifies that players do not see their own movement messages
when they move between rooms.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from ..realtime.connection_manager import ConnectionManager
from ..realtime.event_handler import RealTimeEventHandler


class TestSelfMessageExclusion:
    """Test that players don't see their own movement messages."""

    @pytest.fixture
    def connection_manager(self):
        """Create a connection manager for testing."""
        cm = ConnectionManager()
        cm.send_personal_message = AsyncMock()
        # Mock _canonical_room_id to return the original room_id
        cm._canonical_room_id = MagicMock(side_effect=lambda x: x)
        return cm

    @pytest.fixture
    def event_handler(self, connection_manager):
        """Create an event handler for testing."""
        eh = RealTimeEventHandler()
        eh.connection_manager = connection_manager
        return eh

    @pytest.mark.asyncio
    async def test_player_entered_excludes_self(self, event_handler, connection_manager):
        """Test that PlayerEnteredRoom event excludes the entering player."""
        # Mock broadcast_to_room for this test
        connection_manager.broadcast_to_room = AsyncMock()

        # Create a PlayerEnteredRoom event
        event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id="test_player_123", room_id="test_room_456"
        )

        # Mock the player lookup
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        connection_manager._get_player = MagicMock(return_value=mock_player)

        # Handle the event
        await event_handler._handle_player_entered(event)

        # Verify broadcast_to_room was called with exclude_player
        connection_manager.broadcast_to_room.assert_called()
        call_args = connection_manager.broadcast_to_room.call_args
        assert call_args[1]["exclude_player"] == "test_player_123"

    @pytest.mark.asyncio
    async def test_player_left_excludes_self(self, event_handler, connection_manager):
        """Test that PlayerLeftRoom event excludes the leaving player."""
        # Mock broadcast_to_room for this test
        connection_manager.broadcast_to_room = AsyncMock()

        # Create a PlayerLeftRoom event
        event = PlayerLeftRoom(
            timestamp=None, event_type="player_left", player_id="test_player_123", room_id="test_room_456"
        )

        # Mock the player lookup
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        connection_manager._get_player = MagicMock(return_value=mock_player)

        # Handle the event
        await event_handler._handle_player_left(event)

        # Verify broadcast_to_room was called with exclude_player
        connection_manager.broadcast_to_room.assert_called()
        call_args = connection_manager.broadcast_to_room.call_args
        assert call_args[1]["exclude_player"] == "test_player_123"

    @pytest.mark.asyncio
    async def test_broadcast_to_room_excludes_player(self, connection_manager):
        """Test that broadcast_to_room properly excludes the specified player."""
        # Mock room subscriptions
        connection_manager.room_subscriptions = {"test_room": {"player1", "player2", "player3"}}

        # Create a test event
        test_event = {"event_type": "test", "data": "test"}

        # Broadcast to room with exclude_player
        await connection_manager.broadcast_to_room("test_room", test_event, exclude_player="player2")

        # Verify send_personal_message was called for all players except player2
        assert connection_manager.send_personal_message.call_count == 2

        # Get the calls
        calls = connection_manager.send_personal_message.call_args_list
        player_ids_sent_to = [call[0][0] for call in calls]

        # Should have sent to player1 and player3, but not player2
        assert "player1" in player_ids_sent_to
        assert "player3" in player_ids_sent_to
        assert "player2" not in player_ids_sent_to

    @pytest.mark.asyncio
    async def test_broadcast_to_room_no_exclude(self, connection_manager):
        """Test that broadcast_to_room sends to all players when no exclude_player."""
        # Mock room subscriptions
        connection_manager.room_subscriptions = {"test_room": {"player1", "player2", "player3"}}

        # Create a test event
        test_event = {"event_type": "test", "data": "test"}

        # Broadcast to room without exclude_player
        await connection_manager.broadcast_to_room("test_room", test_event)

        # Verify send_personal_message was called for all players
        assert connection_manager.send_personal_message.call_count == 3

        # Get the calls
        calls = connection_manager.send_personal_message.call_args_list
        player_ids_sent_to = [call[0][0] for call in calls]

        # Should have sent to all players
        assert "player1" in player_ids_sent_to
        assert "player2" in player_ids_sent_to
        assert "player3" in player_ids_sent_to
