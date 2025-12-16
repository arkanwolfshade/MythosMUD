"""
Tests for connection session management.

This module tests functions for handling WebSocket connection session
management operations.
"""

from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.realtime.connection_session_management import (
    _cleanup_old_session_tracking,
    _cleanup_player_data_for_session,
    _disconnect_all_connections_for_session,
    _disconnect_connection_for_session,
    _is_websocket_connected,
    handle_new_game_session_impl,
)


class TestIsWebSocketConnected:
    """Test _is_websocket_connected function."""

    def test_is_websocket_connected_true(self):
        """Test when WebSocket is connected."""
        mock_websocket = MagicMock()
        mock_websocket.client_state.name = "CONNECTED"

        result = _is_websocket_connected(mock_websocket)

        assert result is True

    def test_is_websocket_connected_false(self):
        """Test when WebSocket is not connected."""
        mock_websocket = MagicMock()
        mock_websocket.client_state.name = "DISCONNECTED"

        result = _is_websocket_connected(mock_websocket)

        assert result is False

    def test_is_websocket_connected_error(self):
        """Test when WebSocket raises an error."""
        mock_websocket = MagicMock()
        mock_websocket.client_state = None

        result = _is_websocket_connected(mock_websocket)

        assert result is False


class TestDisconnectConnectionForSession:
    """Test _disconnect_connection_for_session function."""

    @pytest.mark.asyncio
    async def test_disconnect_connection_for_session_success(self):
        """Test successfully disconnecting a connection."""
        connection_id = "conn-123"
        player_id = uuid4()
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "CONNECTED"
        mock_websocket.close = AsyncMock()

        mock_manager = MagicMock()
        mock_manager.active_websockets = {connection_id: mock_websocket}

        with patch("server.realtime.connection_session_management.logger"):
            result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

            assert result is True
            mock_websocket.close.assert_called_once_with(code=1000, reason="New game session established")
            assert connection_id not in mock_manager.active_websockets

    @pytest.mark.asyncio
    async def test_disconnect_connection_for_session_not_in_active(self):
        """Test disconnecting a connection that's not in active_websockets."""
        connection_id = "conn-123"
        player_id = uuid4()
        mock_manager = MagicMock()
        mock_manager.active_websockets = {}

        result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

        assert result is False

    @pytest.mark.asyncio
    async def test_disconnect_connection_for_session_not_connected(self):
        """Test disconnecting a connection that's not connected."""
        connection_id = "conn-123"
        player_id = uuid4()
        mock_websocket = MagicMock()
        mock_websocket.client_state.name = "DISCONNECTED"

        mock_manager = MagicMock()
        mock_manager.active_websockets = {connection_id: mock_websocket}

        with patch("server.realtime.connection_session_management.logger"):
            result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

            assert result is True
            assert connection_id not in mock_manager.active_websockets

    @pytest.mark.asyncio
    async def test_disconnect_connection_for_session_error(self):
        """Test disconnecting when an error occurs."""
        connection_id = "conn-123"
        player_id = uuid4()
        mock_websocket = AsyncMock()
        mock_websocket.client_state.name = "CONNECTED"
        mock_websocket.close = AsyncMock(side_effect=AttributeError("Error"))

        mock_manager = MagicMock()
        mock_manager.active_websockets = {connection_id: mock_websocket}

        with patch("server.realtime.connection_session_management.logger"):
            result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

            assert result is True
            assert connection_id not in mock_manager.active_websockets


class TestDisconnectAllConnectionsForSession:
    """Test _disconnect_all_connections_for_session function."""

    @pytest.mark.asyncio
    async def test_disconnect_all_connections_for_session_success(self):
        """Test successfully disconnecting all connections."""
        player_id = uuid4()
        connection_id1 = "conn-1"
        connection_id2 = "conn-2"

        mock_websocket1 = AsyncMock()
        mock_websocket1.client_state.name = "CONNECTED"
        mock_websocket1.close = AsyncMock()

        mock_websocket2 = AsyncMock()
        mock_websocket2.client_state.name = "CONNECTED"
        mock_websocket2.close = AsyncMock()

        mock_manager = MagicMock()
        mock_manager.active_websockets = {
            connection_id1: mock_websocket1,
            connection_id2: mock_websocket2,
        }
        mock_manager.connection_metadata = {
            connection_id1: MagicMock(),
            connection_id2: MagicMock(),
        }
        mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}

        with patch("server.realtime.connection_session_management.logger"):
            result = await _disconnect_all_connections_for_session(
                [connection_id1, connection_id2], player_id, mock_manager
            )

            assert result == 2
            assert connection_id1 not in mock_manager.active_websockets
            assert connection_id2 not in mock_manager.active_websockets
            assert connection_id1 not in mock_manager.connection_metadata
            assert connection_id2 not in mock_manager.connection_metadata
            assert player_id not in mock_manager.player_websockets

    @pytest.mark.asyncio
    async def test_disconnect_all_connections_for_session_partial(self):
        """Test disconnecting when some connections don't exist."""
        player_id = uuid4()
        connection_id1 = "conn-1"
        connection_id2 = "conn-2"

        mock_websocket1 = AsyncMock()
        mock_websocket1.client_state.name = "CONNECTED"
        mock_websocket1.close = AsyncMock()

        mock_manager = MagicMock()
        mock_manager.active_websockets = {connection_id1: mock_websocket1}
        mock_manager.connection_metadata = {}
        mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}

        with patch("server.realtime.connection_session_management.logger"):
            result = await _disconnect_all_connections_for_session(
                [connection_id1, connection_id2], player_id, mock_manager
            )

            assert result == 1
            assert connection_id1 not in mock_manager.active_websockets


class TestCleanupOldSessionTracking:
    """Test _cleanup_old_session_tracking function."""

    def test_cleanup_old_session_tracking_success(self):
        """Test successfully cleaning up old session tracking."""
        player_id = uuid4()
        old_session_id = "session-123"

        mock_manager = MagicMock()
        mock_manager.player_sessions = {player_id: old_session_id}
        mock_manager.session_connections = {old_session_id: ["conn-1"]}

        _cleanup_old_session_tracking(player_id, mock_manager)

        assert old_session_id not in mock_manager.session_connections

    def test_cleanup_old_session_tracking_no_player(self):
        """Test cleanup when player has no session."""
        player_id = uuid4()
        mock_manager = MagicMock()
        mock_manager.player_sessions = {}

        _cleanup_old_session_tracking(player_id, mock_manager)

        # Should return early without error

    def test_cleanup_old_session_tracking_no_session_connection(self):
        """Test cleanup when session connection doesn't exist."""
        player_id = uuid4()
        old_session_id = "session-123"

        mock_manager = MagicMock()
        mock_manager.player_sessions = {player_id: old_session_id}
        mock_manager.session_connections = {}

        _cleanup_old_session_tracking(player_id, mock_manager)

        # Should handle KeyError gracefully


class TestCleanupPlayerDataForSession:
    """Test _cleanup_player_data_for_session function."""

    def test_cleanup_player_data_for_session_success(self):
        """Test successfully cleaning up player data."""
        player_id = uuid4()

        mock_rate_limiter = MagicMock()
        mock_rate_limiter.remove_player_data = MagicMock()

        mock_message_queue = MagicMock()
        mock_message_queue.remove_player_messages = MagicMock()

        mock_room_manager = MagicMock()
        mock_room_manager.remove_player_from_all_rooms = MagicMock()

        mock_manager = MagicMock()
        mock_manager.rate_limiter = mock_rate_limiter
        mock_manager.message_queue = mock_message_queue
        mock_manager.room_manager = mock_room_manager
        mock_manager.last_seen = {player_id: 1000.0}
        mock_manager.last_active_update_times = {player_id: 1000.0}

        _cleanup_player_data_for_session(player_id, mock_manager)

        mock_rate_limiter.remove_player_data.assert_called_once_with(str(player_id))
        mock_message_queue.remove_player_messages.assert_called_once_with(str(player_id))
        assert player_id not in mock_manager.last_seen
        mock_room_manager.remove_player_from_all_rooms.assert_called_once_with(str(player_id))

    def test_cleanup_player_data_for_session_no_last_seen(self):
        """Test cleanup when player has no last_seen entry."""
        player_id = uuid4()

        mock_rate_limiter = MagicMock()
        mock_message_queue = MagicMock()
        mock_room_manager = MagicMock()

        mock_manager = MagicMock()
        mock_manager.rate_limiter = mock_rate_limiter
        mock_manager.message_queue = mock_message_queue
        mock_manager.room_manager = mock_room_manager
        mock_manager.last_seen = {}
        mock_manager.last_active_update_times = {}

        _cleanup_player_data_for_session(player_id, mock_manager)

        # Should not raise error when last_seen is empty


class TestHandleNewGameSessionImpl:
    """Test handle_new_game_session_impl function."""

    @pytest.mark.asyncio
    async def test_handle_new_game_session_impl_success(self):
        """Test successfully handling a new game session."""
        player_id = uuid4()
        new_session_id = "session-new"
        old_session_id = "session-old"
        connection_id1 = "conn-1"
        connection_id2 = "conn-2"

        mock_websocket1 = AsyncMock()
        mock_websocket1.client_state.name = "CONNECTED"
        mock_websocket1.close = AsyncMock()

        mock_websocket2 = AsyncMock()
        mock_websocket2.client_state.name = "CONNECTED"
        mock_websocket2.close = AsyncMock()

        mock_rate_limiter = MagicMock()
        mock_rate_limiter.remove_player_data = MagicMock()

        mock_message_queue = MagicMock()
        mock_message_queue.remove_player_messages = MagicMock()

        mock_room_manager = MagicMock()
        mock_room_manager.remove_player_from_all_rooms = MagicMock()

        mock_manager = MagicMock()
        mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}
        mock_manager.active_websockets = {
            connection_id1: mock_websocket1,
            connection_id2: mock_websocket2,
        }
        mock_manager.connection_metadata = {
            connection_id1: MagicMock(),
            connection_id2: MagicMock(),
        }
        mock_manager.player_sessions = {player_id: old_session_id}
        mock_manager.session_connections = {old_session_id: [connection_id1, connection_id2]}
        mock_manager.last_seen = {player_id: 1000.0}
        mock_manager.last_active_update_times = {player_id: 1000.0}
        mock_manager.rate_limiter = mock_rate_limiter
        mock_manager.message_queue = mock_message_queue
        mock_manager.room_manager = mock_room_manager

        with patch("server.realtime.connection_session_management.logger"):
            result = await handle_new_game_session_impl(player_id, new_session_id, mock_manager)

            assert result["success"] is True
            assert result["player_id"] == player_id
            assert result["new_session_id"] == new_session_id
            assert result["previous_session_id"] == old_session_id
            assert result["connections_disconnected"] == 2
            assert result["websocket_connections"] == 2
            assert mock_manager.player_sessions[player_id] == new_session_id
            assert new_session_id in mock_manager.session_connections
            assert mock_manager.session_connections[new_session_id] == []

    @pytest.mark.asyncio
    async def test_handle_new_game_session_impl_no_existing_connections(self):
        """Test handling new session when player has no existing connections."""
        player_id = uuid4()
        new_session_id = "session-new"

        mock_rate_limiter = MagicMock()
        mock_message_queue = MagicMock()
        mock_room_manager = MagicMock()

        mock_manager = MagicMock()
        mock_manager.player_websockets = {}
        mock_manager.active_websockets = {}
        mock_manager.connection_metadata = {}
        mock_manager.player_sessions = {}
        mock_manager.session_connections = {}
        mock_manager.last_seen = {}
        mock_manager.last_active_update_times = {}
        mock_manager.rate_limiter = mock_rate_limiter
        mock_manager.message_queue = mock_message_queue
        mock_manager.room_manager = mock_room_manager

        with patch("server.realtime.connection_session_management.logger"):
            result = await handle_new_game_session_impl(player_id, new_session_id, mock_manager)

            assert result["success"] is True
            assert result["connections_disconnected"] == 0
            assert result["websocket_connections"] == 0
            assert result["previous_session_id"] is None

    @pytest.mark.asyncio
    async def test_handle_new_game_session_impl_error(self):
        """Test handling new session when an error occurs."""
        player_id = uuid4()
        new_session_id = "session-new"

        mock_manager = MagicMock()
        mock_manager.player_websockets = {player_id: ["conn-1"]}
        mock_manager.active_websockets = {}
        mock_manager.connection_metadata = {}
        mock_manager.player_sessions = {}
        mock_manager.session_connections = {}
        mock_manager.last_seen = {}
        mock_manager.last_active_update_times = {}
        # Cause an error by making rate_limiter raise an exception
        mock_manager.rate_limiter = MagicMock()
        mock_manager.rate_limiter.remove_player_data = MagicMock(side_effect=AttributeError("Error"))
        mock_manager.message_queue = MagicMock()
        mock_manager.room_manager = MagicMock()

        with patch("server.realtime.connection_session_management.logger"):
            result = await handle_new_game_session_impl(player_id, new_session_id, mock_manager)

            assert result["success"] is False
            assert len(result["errors"]) > 0
