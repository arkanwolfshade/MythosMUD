"""
Tests for WebSocket connection event firing and processing.

This module tests the critical multiplayer connection messaging system
to ensure that PlayerEnteredRoom and PlayerLeftRoom events are properly
fired and broadcast to other players in the same room.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from ..events import EventBus
from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from ..models.player import Player
from ..models.room import Room
from ..realtime.connection_manager import connection_manager
from ..realtime.event_handler import RealTimeEventHandler


class TestWebSocketConnectionEvents:
    """Test WebSocket connection event firing and processing."""

    @pytest.fixture
    def mock_room(self):
        """Create a mock room for testing."""
        room = MagicMock(spec=Room)
        room.id = "test_room_001"
        room.name = "Test Room"
        room.description = "A test room for multiplayer testing"
        room.exits = {"north": "test_room_002"}
        room.has_player = MagicMock(return_value=False)
        room.player_entered = MagicMock()
        room.player_left = MagicMock()
        room.get_players = MagicMock(return_value=[])
        room.to_dict = MagicMock(
            return_value={
                "id": "test_room_001",
                "name": "Test Room",
                "description": "A test room for multiplayer testing",
                "exits": {"north": "test_room_002"},
            }
        )
        # Add _event_bus attribute to mock
        room._event_bus = None
        return room

    @pytest.fixture
    def mock_player(self):
        """Create a mock player for testing."""
        player = MagicMock(spec=Player)
        player.player_id = "test_player_001"
        player.name = "TestPlayer"
        player.current_room_id = "test_room_001"
        player.level = 1
        player.get_stats = MagicMock(
            return_value={
                "health": 100,
                "sanity": 100,
                "strength": 10,
                "dexterity": 10,
                "constitution": 10,
                "intelligence": 10,
                "wisdom": 10,
                "charisma": 10,
            }
        )
        return player

    @pytest.fixture
    def event_bus(self):
        """Create a test event bus."""
        return EventBus()

    @pytest.fixture
    def real_time_event_handler(self, event_bus):
        """Create a real-time event handler for testing."""
        handler = RealTimeEventHandler(event_bus)
        handler.connection_manager = connection_manager
        return handler

    @pytest.mark.asyncio
    async def test_room_player_entered_fires_event(self, event_bus):
        """Test that Room.player_entered() fires PlayerEnteredRoom event."""
        # Create a real Room instance with event bus
        room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room for multiplayer testing",
            "exits": {"north": "test_room_002"},
        }
        room = Room(room_data, event_bus)

        # Track published events
        published_events = []

        def track_event(event):
            published_events.append(event)

        # Subscribe to PlayerEnteredRoom events
        event_bus.subscribe(PlayerEnteredRoom, track_event)

        # Call player_entered
        player_id = "test_player_001"
        room.player_entered(player_id)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify event was fired
        assert len(published_events) == 1
        event = published_events[0]
        assert isinstance(event, PlayerEnteredRoom)
        assert event.player_id == player_id
        assert event.room_id == room.id

    @pytest.mark.asyncio
    async def test_room_player_left_fires_event(self, event_bus):
        """Test that Room.player_left() fires PlayerLeftRoom event."""
        # Create a real Room instance with event bus
        room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room for multiplayer testing",
            "exits": {"north": "test_room_002"},
        }
        room = Room(room_data, event_bus)

        # Add player first
        player_id = "test_player_001"
        room.player_entered(player_id)

        # Track published events
        published_events = []

        def track_event(event):
            published_events.append(event)

        # Subscribe to PlayerLeftRoom events
        event_bus.subscribe(PlayerLeftRoom, track_event)

        # Call player_left
        room.player_left(player_id)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify event was fired
        assert len(published_events) == 1
        event = published_events[0]
        assert isinstance(event, PlayerLeftRoom)
        assert event.player_id == player_id
        assert event.room_id == room.id

    @pytest.mark.asyncio
    async def test_websocket_connection_calls_player_entered(self, mock_room, mock_player):
        """Test that WebSocket connection calls room.player_entered()."""
        with patch("server.realtime.websocket_handler.connection_manager") as mock_cm:
            # Set up connection manager mocks
            async def mock_connect_websocket(websocket, player_id, session_id=None):
                # Don't call player_entered here - the real handler will do it
                return True

            mock_cm.connect_websocket = mock_connect_websocket
            mock_cm._get_player = MagicMock(return_value=mock_player)
            mock_cm.get_room_occupants = MagicMock(return_value=[])
            mock_cm.broadcast_to_room = AsyncMock()
            mock_cm.disconnect_websocket = AsyncMock()
            mock_cm.persistence = MagicMock()
            mock_cm.persistence.get_room = MagicMock(return_value=mock_room)

            # Set up WebSocket mock
            mock_websocket = AsyncMock()
            mock_websocket.send_json = AsyncMock()
            mock_websocket.receive_text = AsyncMock(side_effect=asyncio.CancelledError())

            # Import and call the handler
            from ..realtime.websocket_handler import handle_websocket_connection

            # This should raise CancelledError when trying to receive messages
            with pytest.raises(asyncio.CancelledError):
                await handle_websocket_connection(mock_websocket, "test_player_001")

            # Verify that player_entered was called
            mock_room.player_entered.assert_called_once_with("test_player_001")

    @pytest.mark.asyncio
    async def test_real_time_event_handler_processes_player_entered(self, event_bus):
        """Test that RealTimeEventHandler processes PlayerEnteredRoom events."""
        # Set up the event bus with the current event loop
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create real-time event handler
        real_time_event_handler = RealTimeEventHandler(event_bus)

        # Set up connection manager mocks
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        real_time_event_handler.connection_manager._get_player = MagicMock(return_value=mock_player)
        real_time_event_handler.connection_manager.broadcast_to_room = AsyncMock()
        real_time_event_handler.connection_manager.persistence = MagicMock()
        real_time_event_handler.connection_manager.persistence.get_room = MagicMock(return_value=MagicMock())

        # Create and publish event
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_001", room_id="test_room_001")

        # Publish event
        event_bus.publish(event)

        # Wait for event processing
        await asyncio.sleep(0.2)

        # Verify that broadcast_to_room was called (should be called twice: player_entered + room_occupants)
        assert real_time_event_handler.connection_manager.broadcast_to_room.call_count == 2

        # Verify the first broadcast call (player_entered event)
        first_call = real_time_event_handler.connection_manager.broadcast_to_room.call_args_list[0]
        room_id = first_call[0][0]  # First positional argument
        message = first_call[0][1]  # Second positional argument
        exclude_player = first_call[1].get("exclude_player")  # Keyword argument

        assert room_id == "test_room_001"
        assert message["event_type"] == "player_entered"
        assert message["data"]["player_name"] == "TestPlayer"
        assert message["data"]["message"] == "TestPlayer enters the room."
        assert exclude_player == "test_player_001"

        # Verify the second broadcast call (room_occupants event)
        second_call = real_time_event_handler.connection_manager.broadcast_to_room.call_args_list[1]
        room_id2 = second_call[0][0]  # First positional argument
        message2 = second_call[0][1]  # Second positional argument
        exclude_player2 = second_call[1].get("exclude_player")  # Keyword argument

        assert room_id2 == "test_room_001"
        assert message2["event_type"] == "room_occupants"
        assert exclude_player2 == "test_player_001"

    @pytest.mark.asyncio
    async def test_real_time_event_handler_processes_player_left(self, event_bus):
        """Test that RealTimeEventHandler processes PlayerLeftRoom events."""
        # Set up the event bus with the current event loop
        event_bus.set_main_loop(asyncio.get_running_loop())

        # Create real-time event handler
        real_time_event_handler = RealTimeEventHandler(event_bus)

        # Set up connection manager mocks
        mock_player = MagicMock()
        mock_player.name = "TestPlayer"
        real_time_event_handler.connection_manager._get_player = MagicMock(return_value=mock_player)
        real_time_event_handler.connection_manager.broadcast_to_room = AsyncMock()
        real_time_event_handler.connection_manager.persistence = MagicMock()
        real_time_event_handler.connection_manager.persistence.get_room = MagicMock(return_value=MagicMock())

        # Create and publish event
        event = PlayerLeftRoom(timestamp=None, event_type="", player_id="test_player_001", room_id="test_room_001")

        # Publish event
        event_bus.publish(event)

        # Wait for event processing
        await asyncio.sleep(0.2)

        # Verify that broadcast_to_room was called (should be called twice: player_left + room_occupants)
        assert real_time_event_handler.connection_manager.broadcast_to_room.call_count == 2

        # Verify the first broadcast call (player_left event)
        first_call = real_time_event_handler.connection_manager.broadcast_to_room.call_args_list[0]
        room_id = first_call[0][0]  # First positional argument
        message = first_call[0][1]  # Second positional argument
        exclude_player = first_call[1].get("exclude_player")  # Keyword argument

        assert room_id == "test_room_001"
        assert message["event_type"] == "player_left"
        assert message["data"]["player_name"] == "TestPlayer"
        assert message["data"]["message"] == "TestPlayer leaves the room."
        assert exclude_player == "test_player_001"

        # Verify the second broadcast call (room_occupants event)
        second_call = real_time_event_handler.connection_manager.broadcast_to_room.call_args_list[1]
        room_id2 = second_call[0][0]  # First positional argument
        message2 = second_call[0][1]  # Second positional argument
        exclude_player2 = second_call[1].get("exclude_player")  # Keyword argument

        assert room_id2 == "test_room_001"
        assert message2["event_type"] == "room_occupants"
        assert exclude_player2 == "test_player_001"

    @pytest.mark.asyncio
    async def test_event_bus_integration(self, event_bus):
        """Test that EventBus properly integrates with event publishing and subscription."""
        # Track published events
        published_events = []

        def track_event(event):
            published_events.append(event)

        # Subscribe to events
        event_bus.subscribe(PlayerEnteredRoom, track_event)
        event_bus.subscribe(PlayerLeftRoom, track_event)

        # Publish events
        entered_event = PlayerEnteredRoom(
            timestamp=None, event_type="", player_id="test_player_001", room_id="test_room_001"
        )
        left_event = PlayerLeftRoom(timestamp=None, event_type="", player_id="test_player_001", room_id="test_room_001")

        event_bus.publish(entered_event)
        event_bus.publish(left_event)

        # Wait for event processing
        await asyncio.sleep(0.1)

        # Verify events were received
        assert len(published_events) == 2
        assert isinstance(published_events[0], PlayerEnteredRoom)
        assert isinstance(published_events[1], PlayerLeftRoom)

    def test_room_model_has_event_bus_attribute(self):
        """Test that Room model has _event_bus attribute for event publishing."""
        # Create a real Room instance
        room_data = {
            "id": "test_room_001",
            "name": "Test Room",
            "description": "A test room for multiplayer testing",
            "exits": {"north": "test_room_002"},
        }
        room = Room(room_data)

        # This test ensures the Room model can publish events
        assert hasattr(room, "_event_bus")

        # Test that setting event bus works
        event_bus = EventBus()
        room._event_bus = event_bus
        assert room._event_bus is event_bus

    def test_player_entered_message_format(self, real_time_event_handler):
        """Test that player_entered message has correct format."""
        event = PlayerEnteredRoom(timestamp=None, event_type="", player_id="test_player_001", room_id="test_room_001")

        message = real_time_event_handler._create_player_entered_message(event, "TestPlayer")

        # Verify message structure
        assert message["event_type"] == "player_entered"
        assert "timestamp" in message
        assert "sequence_number" in message
        assert message["room_id"] == "test_room_001"
        assert message["data"]["player_id"] == "test_player_001"
        assert message["data"]["player_name"] == "TestPlayer"
        assert message["data"]["message"] == "TestPlayer enters the room."

    def test_player_left_message_format(self, real_time_event_handler):
        """Test that player_left message has correct format."""
        event = PlayerLeftRoom(timestamp=None, event_type="", player_id="test_player_001", room_id="test_room_001")

        message = real_time_event_handler._create_player_left_message(event, "TestPlayer")

        # Verify message structure
        assert message["event_type"] == "player_left"
        assert "timestamp" in message
        assert "sequence_number" in message
        assert message["room_id"] == "test_room_001"
        assert message["data"]["player_id"] == "test_player_001"
        assert message["data"]["player_name"] == "TestPlayer"
        assert message["data"]["message"] == "TestPlayer leaves the room."
