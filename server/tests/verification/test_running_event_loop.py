"""
Test EventBus with a properly running event loop.

This test simulates the real application environment where the main event loop
is running and the EventBus can properly execute async handlers.
"""

import asyncio
from unittest.mock import AsyncMock, Mock

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
        mock_connection_manager._get_player = Mock()
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

        # Create and publish event
        event = PlayerEnteredRoom(player_id="test_player_123", room_id="test_room_001")

        # Publish event
        event_bus.publish(event)

        # Wait for background processing
        await asyncio.sleep(0.5)

        # Verify that the event handler was called (enhanced synchronization sends 2 events)
        assert mock_connection_manager.broadcast_to_room.call_count == 2

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
        mock_connection_manager._get_player = Mock()
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

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup the room with proper mock - use the real room for persistence
        mock_connection_manager.persistence.get_room.return_value = room

        # Test 1: Player enters room
        room.player_entered("test_player_123")
        await asyncio.sleep(0.3)

        # Verify player entered event was broadcast (enhanced sync sends 2 events)
        assert mock_connection_manager.broadcast_to_room.call_count == 2
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        player_entered_call = calls[0]  # First call should be player_entered
        message = player_entered_call[0][1]
        assert message["event_type"] == "player_entered"

        # Reset for next test
        mock_connection_manager.broadcast_to_room.reset_mock()

        # Test 2: Player leaves room
        room.player_left("test_player_123")
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
        mock_connection_manager._get_player = Mock()
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

        # Create multiple events
        events = [
            PlayerEnteredRoom(player_id="player1", room_id="room1"),
            PlayerEnteredRoom(player_id="player2", room_id="room1"),
            PlayerLeftRoom(player_id="player1", room_id="room1"),
        ]

        # Publish all events
        for event in events:
            event_bus.publish(event)

        # Wait for processing
        await asyncio.sleep(0.5)

        # Verify that broadcast_to_room was called for each event (enhanced sync sends 2 events per player action)
        assert mock_connection_manager.broadcast_to_room.call_count == 6

        # Verify the message types (check every other call for the main events)
        calls = mock_connection_manager.broadcast_to_room.call_args_list
        assert calls[0][0][1]["event_type"] == "player_entered"  # First event
        assert calls[2][0][1]["event_type"] == "player_entered"  # Second event
        assert calls[4][0][1]["event_type"] == "player_left"  # Third event
