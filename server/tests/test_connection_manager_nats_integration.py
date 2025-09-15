"""
Tests for ConnectionManager NATS integration.
"""

from unittest.mock import AsyncMock, Mock

import pytest

from server.realtime.connection_manager import ConnectionManager


class TestConnectionManagerNATSIntegration:
    """Test cases for ConnectionManager NATS integration."""

    def setup_method(self):
        """Set up test fixtures."""
        self.mock_event_publisher = Mock()
        self.mock_event_publisher.publish_player_entered_event = AsyncMock()
        self.mock_event_publisher.publish_player_left_event = AsyncMock()

        self.connection_manager = ConnectionManager()
        self.connection_manager.event_publisher = self.mock_event_publisher

    @pytest.mark.asyncio
    async def test_handle_player_entered_room_publishes_nats_event(self):
        """Test that _handle_player_entered_room publishes NATS event."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [
            {"player_name": "player1"},
            {"player_name": "player2"},
        ]
        self.connection_manager.online_players = {"player1": {}, "player2": {}}

        # Mock broadcast_to_room to avoid actual broadcasting
        self.connection_manager.broadcast_to_room = AsyncMock()

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        await self.connection_manager._handle_player_entered_room(event_data)

        # Verify NATS event was published
        self.mock_event_publisher.publish_player_entered_event.assert_called_once()
        call_args = self.mock_event_publisher.publish_player_entered_event.call_args

        assert call_args.kwargs["player_id"] == "player1"
        assert call_args.kwargs["room_id"] == "test_room_1"
        assert "timestamp" in call_args.kwargs
        assert call_args.kwargs["timestamp"] is not None

    @pytest.mark.asyncio
    async def test_handle_player_left_room_publishes_nats_event(self):
        """Test that _handle_player_left_room publishes NATS event."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [{"player_name": "player2"}]
        self.connection_manager.online_players = {"player2": {}}

        # Mock broadcast_to_room to avoid actual broadcasting
        self.connection_manager.broadcast_to_room = AsyncMock()

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        await self.connection_manager._handle_player_left_room(event_data)

        # Verify NATS event was published
        self.mock_event_publisher.publish_player_left_event.assert_called_once()
        call_args = self.mock_event_publisher.publish_player_left_event.call_args

        assert call_args.kwargs["player_id"] == "player1"
        assert call_args.kwargs["room_id"] == "test_room_1"
        assert "timestamp" in call_args.kwargs
        assert call_args.kwargs["timestamp"] is not None

    @pytest.mark.asyncio
    async def test_handle_player_entered_room_missing_room_id(self):
        """Test _handle_player_entered_room with missing room_id."""
        event_data = {"player_id": "player1"}

        await self.connection_manager._handle_player_entered_room(event_data)

        # Should not publish NATS event
        self.mock_event_publisher.publish_player_entered_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_left_room_missing_room_id(self):
        """Test _handle_player_left_room with missing room_id."""
        event_data = {"player_id": "player1"}

        await self.connection_manager._handle_player_left_room(event_data)

        # Should not publish NATS event
        self.mock_event_publisher.publish_player_left_event.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_entered_room_nats_publish_failure(self):
        """Test _handle_player_entered_room when NATS publish fails."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [{"player_name": "player1"}]
        self.connection_manager.online_players = {"player1": {}}

        # Mock broadcast_to_room to avoid actual broadcasting
        self.connection_manager.broadcast_to_room = AsyncMock()

        # Make NATS publish fail
        self.mock_event_publisher.publish_player_entered_event.return_value = False

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # Should not raise exception
        await self.connection_manager._handle_player_entered_room(event_data)

        # Verify NATS event was still attempted
        self.mock_event_publisher.publish_player_entered_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_left_room_nats_publish_failure(self):
        """Test _handle_player_left_room when NATS publish fails."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = []
        self.connection_manager.online_players = {}

        # Mock broadcast_to_room to avoid actual broadcasting
        self.connection_manager.broadcast_to_room = AsyncMock()

        # Make NATS publish fail
        self.mock_event_publisher.publish_player_left_event.return_value = False

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # Should not raise exception
        await self.connection_manager._handle_player_left_room(event_data)

        # Verify NATS event was still attempted
        self.mock_event_publisher.publish_player_left_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_entered_room_nats_exception(self):
        """Test _handle_player_entered_room when NATS publish raises exception."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [{"player_name": "player1"}]
        self.connection_manager.online_players = {"player1": {}}

        # Mock broadcast_to_room to avoid actual broadcasting
        self.connection_manager.broadcast_to_room = AsyncMock()

        # Make NATS publish raise exception
        self.mock_event_publisher.publish_player_entered_event.side_effect = Exception("NATS error")

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # Should not raise exception
        await self.connection_manager._handle_player_entered_room(event_data)

        # Verify NATS event was still attempted
        self.mock_event_publisher.publish_player_entered_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_left_room_nats_exception(self):
        """Test _handle_player_left_room when NATS publish raises exception."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = []
        self.connection_manager.online_players = {}

        # Mock broadcast_to_room to avoid actual broadcasting
        self.connection_manager.broadcast_to_room = AsyncMock()

        # Make NATS publish raise exception
        self.mock_event_publisher.publish_player_left_event.side_effect = Exception("NATS error")

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        # Should not raise exception
        await self.connection_manager._handle_player_left_room(event_data)

        # Verify NATS event was still attempted
        self.mock_event_publisher.publish_player_left_event.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_player_entered_room_still_broadcasts_room_occupants(self):
        """Test that _handle_player_entered_room still broadcasts room_occupants event."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [
            {"player_name": "player1"},
            {"player_name": "player2"},
        ]
        self.connection_manager.online_players = {"player1": {}, "player2": {}}

        # Mock broadcast_to_room
        self.connection_manager.broadcast_to_room = AsyncMock()

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        await self.connection_manager._handle_player_entered_room(event_data)

        # Verify room_occupants event was still broadcast
        self.connection_manager.broadcast_to_room.assert_called_once()
        call_args = self.connection_manager.broadcast_to_room.call_args

        assert call_args[0][0] == "test_room_1"  # room_id
        event_data = call_args[0][1]  # event
        assert event_data["event_type"] == "room_occupants"
        assert event_data["data"]["count"] == 2
        assert "player1" in event_data["data"]["occupants"]
        assert "player2" in event_data["data"]["occupants"]

    @pytest.mark.asyncio
    async def test_handle_player_left_room_still_broadcasts_room_occupants(self):
        """Test that _handle_player_left_room still broadcasts room_occupants event."""
        # Mock room manager and online players
        self.connection_manager.room_manager = Mock()
        self.connection_manager.room_manager.get_room_occupants.return_value = [{"player_name": "player2"}]
        self.connection_manager.online_players = {"player2": {}}

        # Mock broadcast_to_room
        self.connection_manager.broadcast_to_room = AsyncMock()

        event_data = {"room_id": "test_room_1", "player_id": "player1"}

        await self.connection_manager._handle_player_left_room(event_data)

        # Verify room_occupants event was still broadcast
        self.connection_manager.broadcast_to_room.assert_called_once()
        call_args = self.connection_manager.broadcast_to_room.call_args

        assert call_args[0][0] == "test_room_1"  # room_id
        event_data = call_args[0][1]  # event
        assert event_data["event_type"] == "room_occupants"
        assert event_data["data"]["count"] == 1
        assert "player2" in event_data["data"]["occupants"]
        assert "player1" not in event_data["data"]["occupants"]

    def test_connection_manager_initialization_without_event_publisher(self):
        """Test ConnectionManager initialization without event_publisher."""
        connection_manager = ConnectionManager()

        # Should initialize without event_publisher
        assert not hasattr(connection_manager, "event_publisher") or connection_manager.event_publisher is None

    def test_set_event_publisher(self):
        """Test setting event_publisher on ConnectionManager."""
        connection_manager = ConnectionManager()
        mock_event_publisher = Mock()

        connection_manager.event_publisher = mock_event_publisher

        assert connection_manager.event_publisher == mock_event_publisher
