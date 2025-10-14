"""
Integration tests for RealTimeEventHandler to verify event processing.

This test suite verifies that the RealTimeEventHandler properly receives
and processes PlayerEnteredRoom and PlayerLeftRoom events.
"""

import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from server.events import EventBus
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models.room import Room
from server.realtime.event_handler import RealTimeEventHandler


class TestRealTimeEventHandlerIntegration:
    """Test RealTimeEventHandler event processing integration."""

    @pytest.fixture
    def event_bus(self):
        """Create an EventBus instance for testing."""
        return EventBus()

    @pytest.fixture
    def mock_connection_manager(self):
        """Create a mock connection manager."""
        cm = AsyncMock()
        cm._get_player = Mock()
        cm.persistence = Mock()
        cm.broadcast_to_room = AsyncMock()
        cm.subscribe_to_room = AsyncMock()
        cm.send_personal_message = AsyncMock()
        return cm

    @pytest.fixture
    def event_handler(self, event_bus, mock_connection_manager):
        """Create a RealTimeEventHandler instance for testing."""
        handler = RealTimeEventHandler(event_bus)
        handler.connection_manager = mock_connection_manager
        return handler

    def test_event_handler_subscribes_to_events(self, event_bus):
        """Test that RealTimeEventHandler subscribes to the correct events."""
        handler = RealTimeEventHandler(event_bus)

        # Verify subscriptions were made
        subscriptions = event_bus._subscribers
        assert PlayerEnteredRoom in subscriptions
        assert PlayerLeftRoom in subscriptions
        assert handler._handle_player_entered in subscriptions[PlayerEnteredRoom]
        assert handler._handle_player_left in subscriptions[PlayerLeftRoom]

    @pytest.mark.asyncio
    async def test_event_handler_processes_player_entered_event(
        self, event_bus, event_handler, mock_connection_manager
    ):
        """Test that RealTimeEventHandler processes PlayerEnteredRoom events."""
        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create and publish event
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_123", room_id="test_room_001")

        # Publish the event
        event_bus.publish(event)

        # Give async handlers time to process
        await asyncio.sleep(0.1)

        # Verify connection manager methods were called
        mock_connection_manager._get_player.assert_called_with("test_player_123")
        mock_connection_manager.persistence.get_room.assert_called_with("test_room_001")
        # Enhanced synchronization sends both player_entered and room_occupants events
        assert mock_connection_manager.broadcast_to_room.call_count == 2
        mock_connection_manager.subscribe_to_room.assert_called_once()

    @pytest.mark.asyncio
    async def test_event_handler_processes_player_left_event(self, event_bus, event_handler, mock_connection_manager):
        """Test that RealTimeEventHandler processes PlayerLeftRoom events."""
        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create and publish event
        event = PlayerLeftRoom(timestamp=None, event_type="", player_id="test_player_123", room_id="test_room_001")

        # Publish the event
        event_bus.publish(event)

        # Give async handlers time to process
        await asyncio.sleep(0.1)

        # Verify connection manager methods were called
        mock_connection_manager._get_player.assert_called_with("test_player_123")
        mock_connection_manager.persistence.get_room.assert_called_with("test_room_001")
        mock_connection_manager.unsubscribe_from_room.assert_called_once()
        # Enhanced synchronization sends both player_left and room_occupants events
        assert mock_connection_manager.broadcast_to_room.call_count == 2

    @pytest.mark.asyncio
    async def test_room_publishes_events_to_event_handler(self, event_bus, event_handler, mock_connection_manager):
        """Test that Room publishes events that are received by RealTimeEventHandler."""
        # Set the main loop for async event handling
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Setup mock player
        mock_player = Mock()
        mock_player.name = "TestPlayer"
        mock_connection_manager._get_player.return_value = mock_player

        # Setup mock room
        mock_room = Mock()
        mock_room.name = "Test Room"
        mock_room.get_players.return_value = []  # Return empty list to avoid iteration errors
        mock_connection_manager.persistence.get_room.return_value = mock_room

        # Create room with event bus
        room_data = {"id": "test_room_001", "name": "Test Room"}
        room = Room(room_data, event_bus)

        # Reset mock to clear any calls from room creation
        mock_connection_manager.broadcast_to_room.reset_mock()
        mock_connection_manager.subscribe_to_room.reset_mock()

        # Add player to room (should trigger PlayerEnteredRoom event)
        room.player_entered("test_player_123")

        # Give async handlers time to process
        await asyncio.sleep(0.1)

        # Verify event handler processed the event
        mock_connection_manager._get_player.assert_called_with("test_player_123")
        # Enhanced synchronization sends both player_entered and room_occupants events
        assert mock_connection_manager.broadcast_to_room.call_count == 2
        mock_connection_manager.subscribe_to_room.assert_called_once()

        # Reset mocks for next test
        mock_connection_manager.broadcast_to_room.reset_mock()
        mock_connection_manager.unsubscribe_from_room.reset_mock()

        # Remove player from room (should trigger PlayerLeftRoom event)
        room.player_left("test_player_123")

        # Give async handlers time to process
        await asyncio.sleep(0.1)

        # Verify event handler processed the event
        mock_connection_manager.unsubscribe_from_room.assert_called_once()
        # Enhanced synchronization sends both player_left and room_occupants events
        assert mock_connection_manager.broadcast_to_room.call_count == 2

    @pytest.mark.asyncio
    async def test_event_bus_publish_method(self, event_bus):
        """Test that EventBus publish method works correctly."""
        # Track published events
        published_events = []

        def mock_handler(event):
            published_events.append(event)

        # Subscribe to events
        event_bus.subscribe(PlayerEnteredRoom, mock_handler)
        event_bus.subscribe(PlayerLeftRoom, mock_handler)

        # Create and publish events
        entered_event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player", room_id="test_room")
        left_event = PlayerLeftRoom(timestamp=None, event_type="", player_id="test_player", room_id="test_room")

        # Publish events
        event_bus.publish(entered_event)
        event_bus.publish(left_event)

        # Allow async event processing
        await asyncio.sleep(0.1)

        # Verify events were received
        assert len(published_events) == 2
        assert isinstance(published_events[0], PlayerEnteredRoom)
        assert isinstance(published_events[1], PlayerLeftRoom)
