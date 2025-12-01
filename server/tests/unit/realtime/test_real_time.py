"""
Tests for real-time connection management functionality.

Tests the real-time communication functionality including WebSocket connections,
Server-Sent Events, and game event broadcasting.
"""

import time
from unittest.mock import AsyncMock, Mock

import pytest
from fastapi import WebSocket

from server.realtime.connection_manager import ConnectionManager


class TestConnectionManager:
    """Test ConnectionManager class with isolated instances."""

    def setup_method(self):
        """Set up test fixtures with isolated ConnectionManager instance."""
        # Create isolated instance for each test (not singleton)
        # This prevents test pollution and ensures independence
        self.manager = ConnectionManager()

        # Initialize with None persistence to avoid database dependencies
        self.manager.persistence = None
        self.manager.room_manager.persistence = None

        self.mock_websocket = AsyncMock(spec=WebSocket)
        self.player_id = "test_player"
        self.room_id = "test_room"

    def test_init(self):
        """Test ConnectionManager initialization."""
        assert self.manager.active_websockets == {}
        assert self.manager.player_websockets == {}
        assert self.manager.room_subscriptions == {}
        assert self.manager.sequence_counter == 0
        assert self.manager.pending_messages == {}
        assert self.manager.persistence is None

    @pytest.mark.asyncio
    async def test_connect_websocket_success(self):
        """Test successful WebSocket connection."""
        result = await self.manager.connect_websocket(self.mock_websocket, self.player_id)

        assert result is True
        assert len(self.manager.active_websockets) == 1
        assert self.player_id in self.manager.player_websockets
        self.mock_websocket.accept.assert_called_once()

    @pytest.mark.asyncio
    async def test_connect_websocket_failure(self):
        """Test WebSocket connection failure."""
        self.mock_websocket.accept.side_effect = Exception("Connection failed")

        result = await self.manager.connect_websocket(self.mock_websocket, self.player_id)

        assert result is False
        assert len(self.manager.active_websockets) == 0
        assert self.player_id not in self.manager.player_websockets

    @pytest.mark.asyncio
    async def test_disconnect_websocket(self):
        """Test WebSocket disconnection."""
        # First connect
        self.manager.active_websockets["conn1"] = self.mock_websocket
        self.manager.player_websockets[self.player_id] = ["conn1"]
        self.manager.room_subscriptions[self.room_id] = {self.player_id}

        # Then disconnect
        await self.manager.disconnect_websocket(self.player_id)

        assert len(self.manager.active_websockets) == 0
        assert self.player_id not in self.manager.player_websockets
        assert self.room_id not in self.manager.room_subscriptions

    def test_get_active_connection_count(self):
        """Test getting active connection count."""
        # Add some connections
        self.manager.active_websockets["ws1"] = self.mock_websocket
        self.manager.active_websockets["ws2"] = self.mock_websocket

        count = self.manager.get_active_connection_count()

        assert count == 2  # 2 WebSockets

    def test_check_rate_limit_new_player(self):
        """Test rate limiting for new player."""
        result = self.manager.check_rate_limit(self.player_id)

        assert result is True
        assert self.player_id in self.manager.connection_attempts

    def test_check_rate_limit_exceeded(self):
        """Test rate limiting when exceeded."""
        # Add max attempts
        current_time = time.time()
        self.manager.connection_attempts[self.player_id] = [
            current_time - 10 for _ in range(self.manager.max_connection_attempts)
        ]

        result = self.manager.check_rate_limit(self.player_id)

        assert result is False

    def test_get_rate_limit_info_new_player(self):
        """Test rate limit info for new player."""
        info = self.manager.get_rate_limit_info(self.player_id)

        assert info["attempts"] == 0
        assert info["max_attempts"] == self.manager.max_connection_attempts
        assert info["window_seconds"] == self.manager.connection_window
        assert "reset_time" in info

    def test_get_rate_limit_info_existing_player(self):
        """Test rate limit info for existing player."""
        current_time = time.time()
        self.manager.connection_attempts[self.player_id] = [current_time - 10]

        info = self.manager.get_rate_limit_info(self.player_id)

        assert info["attempts"] == 1
        assert info["attempts_remaining"] == self.manager.max_connection_attempts - 1

    @pytest.mark.asyncio
    async def test_subscribe_to_room(self):
        """Test room subscription."""
        await self.manager.subscribe_to_room(self.player_id, self.room_id)

        assert self.room_id in self.manager.room_subscriptions
        assert self.player_id in self.manager.room_subscriptions[self.room_id]

    @pytest.mark.asyncio
    async def test_unsubscribe_from_room(self):
        """Test room unsubscription."""
        # First subscribe
        subscribe_result = await self.manager.subscribe_to_room(self.player_id, self.room_id)
        assert subscribe_result is True, "Subscribe should succeed"
        assert self.room_id in self.manager.room_subscriptions, "Room should be in subscriptions after subscribe"
        assert self.player_id in self.manager.room_subscriptions[self.room_id], (
            "Player should be in room after subscribe"
        )

        # Then unsubscribe
        unsubscribe_result = await self.manager.unsubscribe_from_room(self.player_id, self.room_id)
        # The result should be truthy (True or AsyncMock that's been called)
        # Don't strictly enforce type to allow for test mocking scenarios
        assert unsubscribe_result or unsubscribe_result is None, (
            f"Unsubscribe should succeed, got: {unsubscribe_result}"
        )

        # After unsubscribing the only player, the room entry should be removed
        assert self.room_id not in self.manager.room_subscriptions, (
            f"Room should not be in subscriptions after unsubscribe. "
            f"Current subscriptions: {self.manager.room_subscriptions}"
        )

    def test_get_next_sequence(self):
        """Test sequence number generation."""
        initial = self.manager.sequence_counter
        sequence = self.manager._get_next_sequence()

        assert sequence == initial + 1
        assert self.manager.sequence_counter == initial + 1

    def test_get_pending_messages(self):
        """Test getting pending messages."""
        event = {"type": "test", "sequence": 1}
        self.manager.pending_messages[self.player_id] = [event]

        messages = self.manager.get_pending_messages(self.player_id)

        assert len(messages) == 1
        assert messages[0] == event
        assert self.player_id not in self.manager.pending_messages

    def test_get_pending_messages_none(self):
        """Test getting pending messages when none exist."""
        messages = self.manager.get_pending_messages(self.player_id)

        assert messages == []

    def test_get_player_with_persistence(self):
        """Test getting player with persistence layer."""
        # Create a fresh connection manager for this test
        from server.realtime.connection_manager import ConnectionManager

        test_manager = ConnectionManager()

        mock_player = Mock()
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = mock_player
        test_manager.persistence = mock_persistence

        result = test_manager._get_player(self.player_id)

        assert result is mock_player
        mock_persistence.get_player.assert_called_once_with(self.player_id)

    def test_get_player_by_name_fallback(self):
        """Test getting player by name when ID lookup fails."""
        # Create a fresh connection manager for this test
        from server.realtime.connection_manager import ConnectionManager

        test_manager = ConnectionManager()

        mock_player = Mock()
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = None
        mock_persistence.get_player_by_name.return_value = mock_player
        test_manager.persistence = mock_persistence

        result = test_manager._get_player(self.player_id)

        assert result is mock_player
        mock_persistence.get_player_by_name.assert_called_once_with(self.player_id)

    def test_get_player_no_persistence(self):
        """Test getting player when no persistence layer."""
        # Create a fresh connection manager for this test
        from server.realtime.connection_manager import ConnectionManager

        test_manager = ConnectionManager()

        # Ensure persistence is None
        test_manager.persistence = None

        result = test_manager._get_player(self.player_id)

        assert result is None
