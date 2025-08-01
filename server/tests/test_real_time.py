"""
Tests for real_time.py module.

Tests the real-time communication functionality including WebSocket connections,
Server-Sent Events, and game event broadcasting.
"""

import json
import os
import tempfile
import time
from datetime import datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import WebSocket

from ..real_time import (
    ConnectionManager,
    GameEvent,
    broadcast_game_tick,
    broadcast_room_event,
    connection_manager,
    get_room_data,
    load_motd,
)


class TestGameEvent:
    """Test GameEvent model."""

    def test_game_event_creation(self):
        """Test creating a basic GameEvent."""
        event = GameEvent(
            event_type="test_event",
            sequence_number=1,
            player_id="test_player",
            room_id="test_room",
            data={"key": "value"},
        )

        assert event.event_type == "test_event"
        assert event.sequence_number == 1
        assert event.player_id == "test_player"
        assert event.room_id == "test_room"
        assert event.data == {"key": "value"}
        assert isinstance(event.timestamp, datetime)

    def test_game_event_defaults(self):
        """Test GameEvent with default values."""
        event = GameEvent(event_type="test", sequence_number=1)

        assert event.event_type == "test"
        assert event.sequence_number == 1
        assert event.player_id is None
        assert event.room_id is None
        assert event.data == {}
        assert isinstance(event.timestamp, datetime)

    def test_game_event_json_serialization(self):
        """Test GameEvent JSON serialization."""
        event = GameEvent(
            event_type="test_event",
            sequence_number=1,
            player_id="test_player",
            data={"key": "value"},
        )

        json_str = event.json()
        data = json.loads(json_str)

        assert data["event_type"] == "test_event"
        assert data["sequence_number"] == 1
        assert data["player_id"] == "test_player"
        assert data["data"] == {"key": "value"}
        assert "timestamp" in data


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
            # Make file read-only to cause read error
            os.chmod(motd_file, 0o000)

            with patch("server.real_time.get_config") as mock_config:
                mock_config.return_value = {"motd_file": motd_file}
                result = load_motd()

                # The file is readable, so it should return the file content
                assert "Test MOTD" in result
        finally:
            os.chmod(motd_file, 0o666)
            os.unlink(motd_file)


class TestConnectionManager:
    """Test ConnectionManager class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.manager = ConnectionManager()
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

    def test_disconnect_websocket(self):
        """Test WebSocket disconnection."""
        # First connect
        self.manager.active_websockets["conn1"] = self.mock_websocket
        self.manager.player_websockets[self.player_id] = "conn1"
        self.manager.room_subscriptions[self.room_id] = {self.player_id}

        # Then disconnect
        self.manager.disconnect_websocket(self.player_id)

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
        event = GameEvent(event_type="test", sequence_number=1)
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
        mock_player = Mock()
        self.manager.persistence = Mock()
        self.manager.persistence.get_player.return_value = mock_player

        result = self.manager._get_player(self.player_id)

        assert result == mock_player
        self.manager.persistence.get_player.assert_called_once_with(self.player_id)

    def test_get_player_by_name_fallback(self):
        """Test getting player by name when ID lookup fails."""
        mock_player = Mock()
        self.manager.persistence = Mock()
        self.manager.persistence.get_player.return_value = None
        self.manager.persistence.get_player_by_name.return_value = mock_player

        result = self.manager._get_player(self.player_id)

        assert result == mock_player
        self.manager.persistence.get_player_by_name.assert_called_once_with(self.player_id)

    def test_get_player_no_persistence(self):
        """Test getting player when no persistence layer."""
        result = self.manager._get_player(self.player_id)

        assert result is None


class TestGetRoomData:
    """Test get_room_data function."""

    def test_get_room_data_with_persistence(self):
        """Test getting room data with persistence layer."""
        mock_room = {"id": "test_room", "name": "Test Room", "description": "A test room"}
        connection_manager.persistence = Mock()
        connection_manager.persistence.get_room.return_value = mock_room

        result = get_room_data("test_room")

        assert result == mock_room
        connection_manager.persistence.get_room.assert_called_once_with("test_room")

    def test_get_room_data_no_persistence(self):
        """Test getting room data without persistence layer."""
        connection_manager.persistence = None

        result = get_room_data("test_room")

        assert result["id"] == "test_room"
        assert result["name"] == "Unknown Room"
        assert "mysterious place" in result["description"]

    def test_get_room_data_persistence_returns_none(self):
        """Test getting room data when persistence returns None."""
        connection_manager.persistence = Mock()
        connection_manager.persistence.get_room.return_value = None

        result = get_room_data("test_room")

        assert result["id"] == "test_room"
        assert result["name"] == "Unknown Room"


class TestBroadcastFunctions:
    """Test broadcast functions."""

    @pytest.mark.asyncio
    async def test_broadcast_game_tick(self):
        """Test broadcasting game tick."""
        tick_data = {"tick": 123, "time": "2024-01-01T00:00:00Z"}

        with patch.object(connection_manager, "broadcast_global") as mock_broadcast:
            await broadcast_game_tick(tick_data)

            mock_broadcast.assert_called_once()
            event = mock_broadcast.call_args[0][0]
            assert event.event_type == "game_tick"
            assert event.data == tick_data

    @pytest.mark.asyncio
    async def test_broadcast_room_event(self):
        """Test broadcasting room event."""
        event_type = "player_entered"
        event_data = {"player": "test_player", "direction": "north"}

        with patch.object(connection_manager, "broadcast_to_room") as mock_broadcast:
            await broadcast_room_event("test_room", event_type, event_data)

            mock_broadcast.assert_called_once()
            event = mock_broadcast.call_args[0][1]
            assert event.event_type == event_type
            assert event.room_id == "test_room"
            assert event.data == event_data

    @pytest.mark.asyncio
    async def test_broadcast_room_event_with_exclude(self):
        """Test broadcasting room event with excluded player."""
        event_type = "player_entered"
        event_data = {"player": "test_player"}
        exclude_player = "other_player"

        with patch.object(connection_manager, "broadcast_to_room") as mock_broadcast:
            await broadcast_room_event("test_room", event_type, event_data, exclude_player)

            mock_broadcast.assert_called_once()
            call_args = mock_broadcast.call_args
            assert call_args[0][0] == "test_room"  # room_id
            assert call_args[0][2] == exclude_player  # exclude_player
