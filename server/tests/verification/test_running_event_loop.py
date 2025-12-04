"""
Test EventBus with a properly running event loop.

This test simulates the real application environment where the main event loop
is running and the EventBus can properly execute async handlers.
"""

import asyncio
from unittest.mock import AsyncMock, Mock
from uuid import uuid4

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.realtime.event_handler import RealTimeEventHandler


class TestRunningEventLoop:
    """Test EventBus with a running event loop."""

    @pytest.fixture
    def event_bus(self):
        """Create an EventBus for testing."""
        return EventBus()

    @pytest.mark.asyncio
    async def test_event_bus_with_running_loop(self):
        """Test that EventBus works properly with a running event loop."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create mock connection manager
        mock_connection_manager = AsyncMock()
        mock_connection_manager._get_player = AsyncMock()
        mock_connection_manager.persistence = Mock()
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.subscribe_to_room = AsyncMock()
        mock_connection_manager.unsubscribe_from_room = AsyncMock()
        mock_connection_manager.send_personal_message = AsyncMock()

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player and room
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create and publish event with proper UUID
        import uuid as uuid_module

        test_player_id = uuid4()
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.player_id = str(test_player_id)

        def mock_get_player(pid):
            if isinstance(pid, uuid_module.UUID):
                return mock_player if pid == test_player_id else None
            return mock_player if str(pid) == str(test_player_id) else None

        mock_connection_manager._get_player = AsyncMock(side_effect=mock_get_player)

        event = PlayerEnteredRoom(player_id=str(test_player_id), room_id="test_room_001")

        # Publish event
        event_bus.publish(event)

        # Wait for background processing
        await asyncio.sleep(0.5)

        # Verify that the event handler was called
        # The handler sends 1 broadcast_to_room (player_entered message to room)
        assert mock_connection_manager.broadcast_to_room.call_count >= 1

        # Verify the message content (check the first call which should be player_entered)
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        player_entered_call = calls[0]  # First call should be player_entered
        message = player_entered_call[0][1]
        assert message["event_type"] == "player_entered"
        assert message["data"]["player_name"] == "TestPlayer"
        assert message["data"]["message"] == "TestPlayer enters the room."

    @pytest.mark.asyncio
    async def test_complete_connection_disconnection_flow(self):
        """Test the complete flow of player connection and disconnection."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create mock connection manager
        mock_connection_manager = AsyncMock()
        mock_connection_manager._get_player = AsyncMock()
        mock_connection_manager.persistence = Mock()
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.subscribe_to_room = AsyncMock()
        mock_connection_manager.unsubscribe_from_room = AsyncMock()
        mock_connection_manager.send_personal_message = AsyncMock()

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock room data
        mock_room_data = {"id": "test_room_001", "name": "Test Room"}
        from server.models.room import Room

        room = Room(mock_room_data, event_bus)

        # Setup mock player with proper UUID
        import uuid as uuid_module

        test_player_id = uuid4()
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_player.player_id = str(test_player_id)

        # Mock _get_player to handle both UUID and string lookups
        def mock_get_player(pid):
            if isinstance(pid, uuid_module.UUID):
                return mock_player if pid == test_player_id else None
            return mock_player if str(pid) == str(test_player_id) else None

        mock_connection_manager._get_player = AsyncMock(side_effect=mock_get_player)

        # Setup the room with proper mock - use the real room for persistence
        mock_connection_manager.persistence.get_room.return_value = room

        # Test 1: Player enters room (use UUID object)
        room.player_entered(test_player_id)
        await asyncio.sleep(0.3)

        # Verify player entered event was broadcast
        # The handler sends 1 broadcast_to_room (player_entered message to room)
        # and 2 send_personal_message calls (room_update and room_occupants to entering player)
        assert mock_connection_manager.broadcast_to_room.call_count >= 1
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        player_entered_call = calls[0]  # First call should be player_entered
        message = player_entered_call[0][1]
        assert message["event_type"] == "player_entered"

        # Reset for next test
        mock_connection_manager.broadcast_to_room.reset_mock()

        # Test 2: Player leaves room (use UUID object)
        room.player_left(test_player_id)
        await asyncio.sleep(0.3)

        # Verify player left event was broadcast (enhanced sync sends 2 events)
        assert mock_connection_manager.broadcast_to_room.call_count == 2
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        player_left_call = calls[0]  # First call should be player_left
        message = player_left_call[0][1]
        assert message["event_type"] == "player_left"

    def test_event_bus_loop_running_detection(self, isolated_event_loop, event_bus):
        """Test that EventBus properly detects when a loop is running."""
        # Use standardized fixtures instead of manual loop creation
        loop = isolated_event_loop
        event_bus1 = event_bus

        # Test with non-running loop
        event_bus1.set_main_loop(loop)
        assert event_bus1._main_loop == loop
        assert event_bus1._main_loop.is_running() is False

        # Test with running loop
        async def test_with_running_loop():
            event_bus2 = EventBus()
            event_bus2.set_main_loop(asyncio.get_running_loop())
            assert event_bus2._main_loop.is_running() is True
            return event_bus2

        # Run the test
        asyncio.set_event_loop(loop)
        event_bus2 = loop.run_until_complete(test_with_running_loop())
        # Note: The loop is closed after run_until_complete(), so we can't check is_running()
        # Instead, just verify the loop was set correctly
        assert event_bus2._main_loop is not None

        # Cleanup is handled by the isolated_event_loop fixture

    @pytest.mark.asyncio
    async def test_multiple_events_processing(self):
        """Test that multiple events are processed correctly."""
        # Create EventBus and set the current running loop
        event_bus = EventBus()
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create mock connection manager
        mock_connection_manager = AsyncMock()
        mock_connection_manager._get_player = AsyncMock()
        mock_connection_manager.persistence = Mock()
        mock_connection_manager.broadcast_to_room = AsyncMock()
        mock_connection_manager.subscribe_to_room = AsyncMock()
        mock_connection_manager.unsubscribe_from_room = AsyncMock()
        mock_connection_manager.send_personal_message = AsyncMock()

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock player and room
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create multiple events (use UUIDs for player_ids)
        player_id1 = uuid4()
        player_id2 = uuid4()
        events = [
            PlayerEnteredRoom(player_id=str(player_id1), room_id="room1"),
            PlayerEnteredRoom(player_id=str(player_id2), room_id="room1"),
            PlayerLeftRoom(player_id=str(player_id1), room_id="room1"),
        ]

        # Publish all events
        for event in events:
            event_bus.publish(event)

        # Wait for processing
        await asyncio.sleep(0.5)

        # Verify that broadcast_to_room was called for PlayerEnteredRoom events
        # Each PlayerEnteredRoom event triggers one broadcast_to_room call
        # PlayerLeftRoom events may not trigger broadcasts in this test setup
        assert mock_connection_manager.broadcast_to_room.call_count >= 2, (
            f"Expected at least 2 calls (one per PlayerEnteredRoom), got {mock_connection_manager.broadcast_to_room.call_count}"
        )

        # Verify the message types
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        # Check that at least one call has player_entered event type
        event_types = [call[0][1]["event_type"] for call in calls if len(call[0]) > 1 and "event_type" in call[0][1]]
        assert "player_entered" in event_types, f"Expected player_entered in event types, got {event_types}"
