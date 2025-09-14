"""
Tests for ConnectionManager occupant event handling.

This module tests the event subscription and broadcasting functionality
for room occupant updates when players enter or leave rooms.
"""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from ..realtime.connection_manager import ConnectionManager


class TestConnectionManagerOccupantEvents:
    """Test ConnectionManager occupant event handling."""

    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        return ConnectionManager()

    @pytest.fixture
    def mock_event_bus(self):
        """Create a mock event bus for testing."""
        event_bus = Mock()
        event_bus.subscribe = AsyncMock()
        event_bus.unsubscribe = AsyncMock()
        return event_bus

    @pytest.fixture
    def mock_room_manager(self):
        """Create a mock room manager for testing."""
        room_manager = Mock()
        room_manager.get_room_occupants = Mock()
        return room_manager

    @pytest.fixture
    def sample_occupants(self):
        """Sample occupant data for testing."""
        return [
            {"player_name": "player1"},
            {"player_name": "player2"},
            {"player_name": "player3"},
        ]

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events(self, connection_manager, mock_event_bus):
        """Test that connection manager subscribes to room movement events."""
        # Mock the persistence layer to return event bus
        with patch.object(connection_manager, "_get_event_bus", return_value=mock_event_bus):
            await connection_manager.subscribe_to_room_events()

            # Verify subscription calls
            from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            mock_event_bus.subscribe.assert_any_call(PlayerEnteredRoom, connection_manager._handle_player_entered_room)
            mock_event_bus.subscribe.assert_any_call(PlayerLeftRoom, connection_manager._handle_player_left_room)

    @pytest.mark.asyncio
    async def test_handle_player_entered_room(self, connection_manager, mock_room_manager, sample_occupants):
        """Test handling of PlayerEnteredRoom events."""
        # Setup mocks
        connection_manager.room_manager = mock_room_manager
        connection_manager.broadcast_to_room = AsyncMock()
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Mock event data
        event_data = {"room_id": "test_room_001", "player_id": "new_player_123", "player_name": "NewPlayer"}

        # Call the handler
        await connection_manager._handle_player_entered_room(event_data)

        # Verify room manager was called to get occupants
        mock_room_manager.get_room_occupants.assert_called_once_with("test_room_001", connection_manager.online_players)

        # Verify broadcast was called with correct event
        connection_manager.broadcast_to_room.assert_called_once()
        call_args = connection_manager.broadcast_to_room.call_args
        assert call_args[0][0] == "test_room_001"  # room_id

        # Verify event structure
        event = call_args[0][1]
        assert event["event_type"] == "room_occupants"
        assert event["data"]["occupants"] == ["player1", "player2", "player3"]
        assert event["data"]["count"] == 3

    @pytest.mark.asyncio
    async def test_handle_player_left_room(self, connection_manager, mock_room_manager, sample_occupants):
        """Test handling of PlayerLeftRoom events."""
        # Setup mocks
        connection_manager.room_manager = mock_room_manager
        connection_manager.broadcast_to_room = AsyncMock()
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Mock event data
        event_data = {"room_id": "test_room_001", "player_id": "leaving_player_456", "player_name": "LeavingPlayer"}

        # Call the handler
        await connection_manager._handle_player_left_room(event_data)

        # Verify room manager was called to get occupants
        mock_room_manager.get_room_occupants.assert_called_once_with("test_room_001", connection_manager.online_players)

        # Verify broadcast was called with correct event
        connection_manager.broadcast_to_room.assert_called_once()
        call_args = connection_manager.broadcast_to_room.call_args
        assert call_args[0][0] == "test_room_001"  # room_id

        # Verify event structure
        event = call_args[0][1]
        assert event["event_type"] == "room_occupants"
        assert event["data"]["occupants"] == ["player1", "player2", "player3"]
        assert event["data"]["count"] == 3

    @pytest.mark.asyncio
    async def test_handle_player_entered_room_error_handling(self, connection_manager, mock_room_manager):
        """Test error handling in player entered room handler."""
        # Setup mocks to raise an exception
        connection_manager.room_manager = mock_room_manager
        connection_manager.broadcast_to_room = AsyncMock()
        mock_room_manager.get_room_occupants.side_effect = Exception("Room not found")

        # Mock event data
        event_data = {"room_id": "nonexistent_room", "player_id": "player_123", "player_name": "TestPlayer"}

        # Call should not raise exception
        await connection_manager._handle_player_entered_room(event_data)

        # Verify room manager was called
        mock_room_manager.get_room_occupants.assert_called_once()

        # Verify broadcast was not called due to error
        connection_manager.broadcast_to_room.assert_not_called()

    @pytest.mark.asyncio
    async def test_handle_player_left_room_error_handling(self, connection_manager, mock_room_manager):
        """Test error handling in player left room handler."""
        # Setup mocks to raise an exception
        connection_manager.room_manager = mock_room_manager
        connection_manager.broadcast_to_room = AsyncMock()
        mock_room_manager.get_room_occupants.side_effect = Exception("Room not found")

        # Mock event data
        event_data = {"room_id": "nonexistent_room", "player_id": "player_123", "player_name": "TestPlayer"}

        # Call should not raise exception
        await connection_manager._handle_player_left_room(event_data)

        # Verify room manager was called
        mock_room_manager.get_room_occupants.assert_called_once()

        # Verify broadcast was not called due to error
        connection_manager.broadcast_to_room.assert_not_called()

    @pytest.mark.asyncio
    async def test_room_occupants_event_format(self, connection_manager, mock_room_manager, sample_occupants):
        """Test that room_occupants events have the correct format."""
        # Setup mocks
        connection_manager.room_manager = mock_room_manager
        connection_manager.broadcast_to_room = AsyncMock()
        mock_room_manager.get_room_occupants.return_value = sample_occupants

        # Mock event data
        event_data = {"room_id": "test_room_001", "player_id": "player_123", "player_name": "TestPlayer"}

        # Call the handler
        await connection_manager._handle_player_entered_room(event_data)

        # Get the broadcasted event
        call_args = connection_manager.broadcast_to_room.call_args
        event = call_args[0][1]

        # Verify event structure matches expected format
        assert "event_type" in event
        assert "data" in event
        assert "room_id" in event

        assert event["event_type"] == "room_occupants"
        assert "occupants" in event["data"]
        assert "count" in event["data"]
        assert isinstance(event["data"]["occupants"], list)
        assert isinstance(event["data"]["count"], int)
        assert event["data"]["count"] == len(event["data"]["occupants"])

    def test_get_event_bus_from_persistence(self, connection_manager):
        """Test getting event bus from persistence layer."""
        # Mock persistence layer
        mock_persistence = Mock()
        mock_event_bus = Mock()
        mock_persistence._event_bus = mock_event_bus

        with patch("server.persistence.get_persistence", return_value=mock_persistence):
            event_bus = connection_manager._get_event_bus()
            assert event_bus == mock_event_bus

    def test_get_event_bus_returns_none_when_not_available(self, connection_manager):
        """Test that get_event_bus returns None when event bus is not available."""
        # Mock persistence layer without event bus
        mock_persistence = Mock()
        mock_persistence._event_bus = None

        with patch("server.persistence.get_persistence", return_value=mock_persistence):
            event_bus = connection_manager._get_event_bus()
            assert event_bus is None

    @pytest.mark.asyncio
    async def test_subscribe_to_room_events_handles_missing_event_bus(self, connection_manager):
        """Test that subscription handles missing event bus gracefully."""
        with patch.object(connection_manager, "_get_event_bus", return_value=None):
            # Should not raise exception
            await connection_manager.subscribe_to_room_events()

            # No subscriptions should be attempted
            # (We can't easily test this without more complex mocking, but the method should complete)

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room_events(self, connection_manager, mock_event_bus):
        """Test unsubscribing from room events."""
        with patch.object(connection_manager, "_get_event_bus", return_value=mock_event_bus):
            await connection_manager.unsubscribe_from_room_events()

            # Verify unsubscription calls
            from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            mock_event_bus.unsubscribe.assert_any_call(
                PlayerEnteredRoom, connection_manager._handle_player_entered_room
            )
            mock_event_bus.unsubscribe.assert_any_call(PlayerLeftRoom, connection_manager._handle_player_left_room)
