"""
Test the real event flow with proper event loop setup.

This test simulates the actual application environment where the EventBus
has access to the main event loop and can properly execute async handlers.
"""

import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom
from server.realtime.event_handler import RealTimeEventHandler


class TestRealEventFlow:
    """Test the real event flow with proper async handling."""

    @pytest.fixture
    def event_loop_setup(self):
        """Set up a proper event loop that EventBus can use."""
        # Create a new event loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        # Create EventBus and set the main loop
        event_bus = EventBus()
        event_bus.set_main_loop(loop)

        return loop, event_bus

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        cm = AsyncMock()
        cm._get_player = Mock()
        cm.persistence = Mock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.unsubscribe_from_room = AsyncMock()
        cm.send_personal_message = AsyncMock()
        return cm

    @pytest.mark.asyncio
    async def test_real_event_flow_with_proper_loop(self, event_loop_setup, mock_connection_manager):
        """Test that events are properly processed with a real event loop."""
        loop, event_bus = event_loop_setup

        # Create event handler
        event_handler = RealTimeEventHandler(event_bus)
        event_handler.connection_manager = mock_connection_manager

        # Setup mock player and room
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create event
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_123", room_id="test_room_001")

        # Publish event
        event_bus.publish(event)

        # Wait for background processing
        await asyncio.sleep(0.3)

        # Verify that the event handler was called
        mock_connection_manager.broadcast_to_room.assert_called_once()

        # Verify the message content
        call_args = mock_connection_manager.broadcast_to_room.call_args
        message = call_args[0][1]
        assert message["event_type"] == "player_entered"
        assert message["data"]["player_name"] == "TestPlayer"

    @pytest.mark.asyncio
    async def test_websocket_connection_flow_simulation(self, event_loop_setup, mock_connection_manager):
        """Simulate the actual WebSocket connection flow."""
        loop, event_bus = event_loop_setup

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
        mock_connection_manager.persistence.get_room.return_value = room

        # Simulate player entering room (this should trigger event)
        room.player_entered("test_player_123")

        # Wait for event processing
        await asyncio.sleep(0.3)

        # Verify that broadcast was called
        mock_connection_manager.broadcast_to_room.assert_called_once()

        # Reset for next test
        mock_connection_manager.broadcast_to_room.reset_mock()

        # Simulate player leaving room
        room.player_left("test_player_123")

        # Wait for event processing
        await asyncio.sleep(0.3)

        # Verify that broadcast was called for leave event
        mock_connection_manager.broadcast_to_room.assert_called_once()

        # Verify it was a player_left message
        call_args = mock_connection_manager.broadcast_to_room.call_args
        message = call_args[0][1]
        assert message["event_type"] == "player_left"

    def test_event_bus_loop_detection(self):
        """Test that EventBus properly detects running event loops."""
        # Test with no running loop
        bus1 = EventBus()
        assert bus1._main_loop is None

        # Test with running loop
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        bus2 = EventBus()
        bus2.set_main_loop(loop)

        assert bus2._main_loop is loop
        assert bus2._main_loop.is_running() is False  # Not started yet

        # Test with running loop
        async def test_with_running_loop():
            bus3 = EventBus()
            bus3.set_main_loop(asyncio.get_running_loop())
            assert bus3._main_loop.is_running() is True
            return bus3

        bus3 = asyncio.run(test_with_running_loop())
        assert bus3._main_loop.is_running() is True
