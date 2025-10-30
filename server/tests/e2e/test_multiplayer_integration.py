"""
Integration tests for multiplayer functionality.

This module tests the integration between the EventBus, RealTimeEventHandler,
and ConnectionManager to ensure players can see each other in real-time.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models import Player
from server.models.room import Room


class TestMultiplayerIntegration:
    """Test multiplayer integration functionality."""

    @pytest.fixture
    def event_bus(self):
        """Create a test event bus."""
        from server.events import EventBus

        return EventBus()

    @pytest.fixture
    def connection_manager(self, event_bus):
        """Create a test connection manager."""
        from server.realtime.connection_manager import ConnectionManager

        return ConnectionManager(event_publisher=event_bus)

    @pytest.fixture
    def event_handler(self, event_bus, connection_manager):
        """Create a test event handler."""
        from server.realtime.event_handler import RealTimeEventHandler

        handler = RealTimeEventHandler(event_bus)
        handler.connection_manager = connection_manager
        return handler

    @pytest.fixture
    def mock_player(self):
        """Create a mock player."""
        player = MagicMock(spec=Player)
        player.name = "TestPlayer"
        player.level = 1
        player.current_room_id = "test_room_001"
        return player

    @pytest.fixture
    def mock_room(self):
        """Create a mock room."""
        room = MagicMock(spec=Room)
        room.id = "test_room_001"
        room.name = "Test Room"
        room.get_players.return_value = ["player1", "player2"]
        return room

    def test_event_handler_initialization(self, event_handler):
        """Test that the event handler initializes correctly."""
        assert event_handler is not None
        assert event_handler.event_bus is not None
        assert event_handler.connection_manager is not None

    def test_event_handler_subscribes_to_events(self, event_handler, event_bus):
        """Test that the event handler subscribes to the correct events."""
        # Check that subscribers were added
        player_entered_subscribers = event_bus._subscribers.get(PlayerEnteredRoom, [])
        player_left_subscribers = event_bus._subscribers.get(PlayerLeftRoom, [])

        assert len(player_entered_subscribers) > 0
        assert len(player_left_subscribers) > 0

    @pytest.mark.asyncio
    async def test_player_entered_event_handling(self, event_handler, event_bus, mock_player):
        """Test handling of player entered events."""
        # Setup mock player - properly mock the connection manager methods
        with patch.object(event_handler.connection_manager, "_get_player", return_value=mock_player):
            with patch.object(event_handler.connection_manager, "subscribe_to_room") as mock_subscribe:
                with patch.object(event_handler.connection_manager, "broadcast_to_room") as mock_broadcast:
                    # Create and publish a player entered event
                    event = PlayerEnteredRoom(
                        timestamp=None, event_type="player_entered", player_id="player1", room_id="test_room_001"
                    )

                    # Call the event handler directly instead of using the EventBus
                    await event_handler._handle_player_entered(event)

                    # Verify that the connection manager methods were called
                    mock_subscribe.assert_called_once_with("player1", "test_room_001")
                    mock_broadcast.assert_called()

    @pytest.mark.asyncio
    async def test_player_left_event_handling(self, event_handler, event_bus, mock_player):
        """Test handling of player left events."""
        # Setup mock player - properly mock the connection manager methods
        with patch.object(event_handler.connection_manager, "_get_player", return_value=mock_player):
            with patch.object(event_handler.connection_manager, "unsubscribe_from_room") as mock_unsubscribe:
                with patch.object(event_handler.connection_manager, "broadcast_to_room") as mock_broadcast:
                    # Create and publish a player left event
                    event = PlayerLeftRoom(
                        timestamp=None, event_type="player_left", player_id="player1", room_id="test_room_001"
                    )

                    # Call the event handler directly instead of using the EventBus
                    await event_handler._handle_player_left(event)

                    # Verify that the connection manager methods were called
                    mock_unsubscribe.assert_called_once_with("player1", "test_room_001")
                    mock_broadcast.assert_called()

    def test_message_format_player_entered(self, event_handler):
        """Test that player entered messages are formatted correctly."""
        event = PlayerEnteredRoom(
            timestamp=None, event_type="player_entered", player_id="player1", room_id="test_room_001"
        )

        message = event_handler._create_player_entered_message(event, "TestPlayer")

        assert message["event_type"] == "player_entered"
        assert message["room_id"] == "test_room_001"
        assert message["data"]["player_id"] == "player1"
        assert message["data"]["player_name"] == "TestPlayer"
        assert "enters the room" in message["data"]["message"]

    def test_message_format_player_left(self, event_handler):
        """Test that player left messages are formatted correctly."""
        event = PlayerLeftRoom(timestamp=None, event_type="player_left", player_id="player1", room_id="test_room_001")

        message = event_handler._create_player_left_message(event, "TestPlayer")

        assert message["event_type"] == "player_left"
        assert message["room_id"] == "test_room_001"
        assert message["data"]["player_id"] == "player1"
        assert message["data"]["player_name"] == "TestPlayer"
        assert "leaves the room" in message["data"]["message"]

    @pytest.mark.asyncio
    async def test_connection_manager_player_tracking(self, connection_manager, mock_player):
        """Test that the connection manager tracks player presence correctly."""
        # Test player connection tracking
        connection_manager.online_players = {}
        connection_manager.room_occupants = {}

        # Mock the persistence (it's None by default, need to create it first)
        mock_persistence = MagicMock()
        mock_room = MagicMock()
        mock_room.id = mock_player.current_room_id
        mock_persistence.get_room.return_value = mock_room
        connection_manager.persistence = mock_persistence

        # Simulate player connection
        await connection_manager._track_player_connected("player1", mock_player)

        assert "player1" in connection_manager.online_players
        assert connection_manager.online_players["player1"]["player_name"] == "TestPlayer"
        # Check that the player is tracked in their current room
        player_room_id = mock_player.current_room_id
        assert player_room_id in connection_manager.room_occupants
        assert "player1" in connection_manager.room_occupants[player_room_id]

    def test_connection_manager_room_occupants(self, connection_manager, mock_player):
        """Test that the connection manager tracks room occupants correctly."""
        # Setup test data
        connection_manager.online_players = {
            "player1": {
                "player_id": "player1",
                "player_name": "TestPlayer1",
                "level": 1,
                "current_room_id": "test_room_001",
            },
            "player2": {
                "player_id": "player2",
                "player_name": "TestPlayer2",
                "level": 2,
                "current_room_id": "test_room_001",
            },
        }
        connection_manager.room_occupants = {"test_room_001": {"player1", "player2"}}

        # Test getting room occupants
        occupants = connection_manager.get_room_occupants("test_room_001")

        assert len(occupants) == 2
        assert any(o["player_id"] == "player1" for o in occupants)
        assert any(o["player_id"] == "player2" for o in occupants)

    def test_sequence_number_increment(self, event_handler):
        """Test that sequence numbers increment correctly."""
        initial_seq = event_handler._get_next_sequence()
        next_seq = event_handler._get_next_sequence()

        assert next_seq == initial_seq + 1
