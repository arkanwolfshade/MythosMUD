"""
Test to reproduce the self-message bug where players see their own movement messages.

This test verifies that players do NOT see their own movement messages,
only other players should see them.
"""

from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from server.events import PlayerEnteredRoom
from server.realtime.connection_manager import ConnectionManager
from server.realtime.event_handler import RealTimeEventHandler


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
        connection_manager._get_player = AsyncMock(return_value=mock_player)

        # Create event for Ithaqua entering a room
        player_id = uuid4()
        room_id = "test_room_001"
        event = PlayerEnteredRoom(player_id=str(player_id), room_id=room_id)

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

        # The exclude_player should match the player_id from the event (as string)
        assert exclude_player == str(player_id), f"Expected exclude_player to be {str(player_id)}, got {exclude_player}"

    @pytest.mark.asyncio
    async def test_player_left_excludes_self(self, event_handler, connection_manager):
        """Test that PlayerLeftRoom event excludes the leaving player."""
        from server.events.event_types import PlayerLeftRoom

        # CRITICAL: Assign the mocked connection manager to the event handler
        event_handler.connection_manager = connection_manager

        # Mock broadcast_to_room for this test
        connection_manager.broadcast_to_room = AsyncMock()

        # Use UUID for player_id
        player_id = uuid4()

        # Create a PlayerLeftRoom event
        event = PlayerLeftRoom(player_id=str(player_id), room_id="test_room_456")
        event.timestamp = None

        # Mock the player lookup
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        connection_manager._get_player = AsyncMock(return_value=mock_player)

        # Mock persistence.get_room for chat logging
        mock_room = Mock()
        mock_room.name = "Test Room"
        connection_manager.persistence = Mock()
        connection_manager.persistence.get_room = AsyncMock(return_value=mock_room)

        # Mock the room sync service to just pass through the event
        event_handler.room_sync_service._process_event_with_ordering = Mock(return_value=event)

        # Mock the chat logger to avoid errors
        event_handler.chat_logger.log_player_left_room = Mock()

        # Mock _send_room_occupants_update to avoid errors
        event_handler._send_room_occupants_update = AsyncMock()

        # Mock _create_player_left_message to return a test message
        event_handler._create_player_left_message = Mock(
            return_value={"event_type": "player_left", "player_id": str(player_id)}
        )

        # Handle the event
        await event_handler._handle_player_left(event)

        # Verify broadcast_to_room was called with exclude_player
        connection_manager.broadcast_to_room.assert_called()
        call_args = connection_manager.broadcast_to_room.call_args
        assert call_args[1]["exclude_player"] == str(player_id)

    @pytest.mark.asyncio
    async def test_broadcast_to_room_excludes_player(self):
        """Test that broadcast_to_room properly excludes the specified player."""
        # Generate UUIDs for test players
        player_id1 = uuid4()
        player_id2 = uuid4()
        player_id3 = uuid4()

        # Create a fresh connection manager without broadcast_to_room mocked
        cm = ConnectionManager()
        cm.send_personal_message = AsyncMock()

        # Mock room_manager to return subscribers (use UUID strings)
        mock_room_manager = Mock()
        mock_room_manager.get_room_subscribers = AsyncMock(return_value={str(player_id1), str(player_id2), str(player_id3)})
        cm.room_manager = mock_room_manager

        # Create a test event
        test_event = {"event_type": "test", "data": "test"}

        # Broadcast to room with exclude_player (use UUID string)
        await cm.broadcast_to_room("test_room", test_event, exclude_player=str(player_id2))

        # Verify send_personal_message was called for all players except player2
        assert cm.send_personal_message.call_count == 2

        # Get the calls
        calls = cm.send_personal_message.call_args_list
        player_ids_sent_to = [call[0][0] for call in calls]

        # Should have sent to player1 and player3, but not player2
        assert player_id1 in player_ids_sent_to
        assert player_id3 in player_ids_sent_to
        assert player_id2 not in player_ids_sent_to

    @pytest.mark.asyncio
    async def test_broadcast_to_room_no_exclude(self):
        """Test that broadcast_to_room sends to all players when no exclude_player."""
        # Generate UUIDs for test players
        player_id1 = uuid4()
        player_id2 = uuid4()
        player_id3 = uuid4()

        # Create a fresh connection manager without broadcast_to_room mocked
        cm = ConnectionManager()
        cm.send_personal_message = AsyncMock()

        # Mock room_manager to return subscribers (use UUID strings)
        mock_room_manager = Mock()
        mock_room_manager.get_room_subscribers = AsyncMock(return_value={str(player_id1), str(player_id2), str(player_id3)})
        cm.room_manager = mock_room_manager

        # Create a test event
        test_event = {"event_type": "test", "data": "test"}

        # Broadcast to room without exclude_player
        await cm.broadcast_to_room("test_room", test_event)

        # Verify send_personal_message was called for all players
        assert cm.send_personal_message.call_count == 3

        # Get the calls
        calls = cm.send_personal_message.call_args_list
        player_ids_sent_to = [call[0][0] for call in calls]

        # Should have sent to all players
        assert player_id1 in player_ids_sent_to
        assert player_id2 in player_ids_sent_to
        assert player_id3 in player_ids_sent_to
