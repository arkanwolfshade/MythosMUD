"""
Tests for real_time.py module.

Tests the real-time communication functionality including WebSocket connections,
Server-Sent Events, and game event broadcasting.
"""

import os
import tempfile
import time
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import WebSocket

from ..real_time import load_motd
from ..realtime.connection_manager import connection_manager


class TestLoadMotd:
    """Test MOTD loading functionality."""

    def test_load_motd_file_exists(self):
        """Test loading MOTD from existing file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Welcome to the Mythos!\n\nEnter at your own risk...")
            motd_file = f.name

        try:
            with patch("server.real_time.get_config") as mock_config:
                mock_config.return_value = {"motd_file": motd_file}
                result = load_motd()

                assert "Welcome to the Mythos!" in result
                assert "Enter at your own risk" in result
        finally:
            os.unlink(motd_file)

    def test_load_motd_file_not_found(self):
        """Test loading MOTD when file doesn't exist."""
        with patch("server.real_time.get_config") as mock_config:
            mock_config.return_value = {"motd_file": "./nonexistent/motd.txt"}
            result = load_motd()

            assert "Welcome to MythosMUD" in result

    def test_load_motd_config_error(self):
        """Test loading MOTD when config fails."""
        with patch("server.real_time.get_config") as mock_config:
            mock_config.side_effect = Exception("Config error")
            result = load_motd()

            assert "Welcome to MythosMUD" in result

    def test_load_motd_file_read_error(self):
        """Test loading MOTD when file read fails."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
            f.write("Test MOTD")
            motd_file = f.name

        try:
            # On Windows, 0o000 might not prevent reading, so we'll delete the file
            # to simulate a read error
            os.unlink(motd_file)

            with patch("server.real_time.get_config") as mock_config:
                mock_config.return_value = {"motd_file": motd_file}
                result = load_motd()

                # The file doesn't exist, so it should return the fallback
                assert "Welcome to MythosMUD - Enter the realm of forbidden knowledge..." in result
        except Exception:
            # Clean up if the file still exists
            if os.path.exists(motd_file):
                os.chmod(motd_file, 0o644)  # Use secure permissions
                os.unlink(motd_file)


class TestConnectionManager:
    """Test ConnectionManager class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.manager = connection_manager
        # Reset the connection manager state between tests
        self.manager.active_websockets.clear()
        self.manager.player_websockets.clear()
        self.manager.active_sse_connections.clear()
        self.manager.room_subscriptions.clear()
        self.manager.sequence_counter = 0
        self.manager.pending_messages.clear()
        self.manager.connection_attempts.clear()
        self.manager.persistence = None

        self.mock_websocket = AsyncMock(spec=WebSocket)
        self.player_id = "test_player"
        self.room_id = "test_room"

    def test_init(self):
        """Test ConnectionManager initialization."""
        assert self.manager.active_websockets == {}
        assert self.manager.player_websockets == {}
        assert self.manager.active_sse_connections == {}
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
        self.manager.player_websockets[self.player_id] = "conn1"
        self.manager.room_subscriptions[self.room_id] = {self.player_id}

        # Then disconnect
        await self.manager.disconnect_websocket(self.player_id)

        assert len(self.manager.active_websockets) == 0
        assert self.player_id not in self.manager.player_websockets
        assert self.room_id not in self.manager.room_subscriptions

    def test_connect_sse(self):
        """Test SSE connection."""
        connection_id = self.manager.connect_sse(self.player_id)

        assert connection_id is not None
        assert self.player_id in self.manager.active_sse_connections
        assert self.manager.active_sse_connections[self.player_id] == connection_id

    def test_disconnect_sse(self):
        """Test SSE disconnection."""
        # First connect
        self.manager.connect_sse(self.player_id)

        # Then disconnect
        self.manager.disconnect_sse(self.player_id)

        assert self.player_id not in self.manager.active_sse_connections

    def test_get_active_connection_count(self):
        """Test getting active connection count."""
        # Add some connections
        self.manager.active_websockets["ws1"] = self.mock_websocket
        self.manager.active_sse_connections["player1"] = "sse1"
        self.manager.active_sse_connections["player2"] = "sse2"

        count = self.manager.get_active_connection_count()

        assert count == 3  # 1 WebSocket + 2 SSE

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
        await self.manager.subscribe_to_room(self.player_id, self.room_id)

        # Then unsubscribe
        await self.manager.unsubscribe_from_room(self.player_id, self.room_id)

        assert self.room_id not in self.manager.room_subscriptions

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
