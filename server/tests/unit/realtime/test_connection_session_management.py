"""
Unit tests for connection session management.

Tests the connection_session_management module functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import WebSocket

from server.realtime.connection_session_management import (
    _cleanup_old_session_tracking,
    _cleanup_player_data_for_session,
    _disconnect_all_connections_for_session,
    _disconnect_connection_for_session,
    _is_websocket_connected,
    handle_new_game_session_impl,
)


def test_is_websocket_connected_connected():
    """Test _is_websocket_connected() returns True for connected websocket."""
    mock_websocket = MagicMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "CONNECTED"

    result = _is_websocket_connected(mock_websocket)

    assert result is True


def test_is_websocket_connected_disconnected():
    """Test _is_websocket_connected() returns False for disconnected websocket."""
    mock_websocket = MagicMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "DISCONNECTED"

    result = _is_websocket_connected(mock_websocket)

    assert result is False


def test_is_websocket_connected_no_client_state():
    """Test _is_websocket_connected() handles missing client_state."""
    mock_websocket = MagicMock(spec=WebSocket)
    del mock_websocket.client_state

    result = _is_websocket_connected(mock_websocket)

    assert result is False


def test_is_websocket_connected_no_name():
    """Test _is_websocket_connected() handles missing name attribute."""
    mock_websocket = MagicMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    del mock_websocket.client_state.name

    result = _is_websocket_connected(mock_websocket)

    assert result is False


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_success():
    """Test _disconnect_connection_for_session() successfully disconnects connection."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_websocket = AsyncMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "CONNECTED"
    mock_manager.active_websockets = {connection_id: mock_websocket}

    result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

    assert result is True
    mock_websocket.close.assert_called_once()
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_not_in_active():
    """Test _disconnect_connection_for_session() returns False when not in active_websockets."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}

    result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

    assert result is False


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_none_websocket():
    """Test _disconnect_connection_for_session() handles None websocket."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.active_websockets = {connection_id: None}

    result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

    assert result is False
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_not_connected():
    """Test _disconnect_connection_for_session() handles disconnected websocket."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_websocket = AsyncMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "DISCONNECTED"
    mock_manager.active_websockets = {connection_id: mock_websocket}

    result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

    assert result is True
    mock_websocket.close.assert_not_called()
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_close_error():
    """Test _disconnect_connection_for_session() handles close error."""
    from server.exceptions import DatabaseError

    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_websocket = AsyncMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "CONNECTED"
    mock_websocket.close = AsyncMock(side_effect=DatabaseError("Close error"))
    mock_manager.active_websockets = {connection_id: mock_websocket}

    result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

    assert result is True
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_for_session_key_error():
    """Test _disconnect_connection_for_session() handles KeyError when deleting."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_websocket = AsyncMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "CONNECTED"
    # Use a MagicMock dict that raises KeyError when deleting
    mock_active_websockets = MagicMock()
    mock_active_websockets.__contains__ = lambda self, key: key == connection_id
    mock_active_websockets.__getitem__ = lambda self, key: mock_websocket if key == connection_id else None
    mock_active_websockets.__delitem__ = MagicMock(side_effect=KeyError(connection_id))
    mock_manager.active_websockets = mock_active_websockets

    result = await _disconnect_connection_for_session(connection_id, player_id, mock_manager)

    assert result is True


@pytest.mark.asyncio
async def test_disconnect_all_connections_for_session():
    """Test _disconnect_all_connections_for_session() disconnects all connections."""
    connection_id1 = "conn_1"
    connection_id2 = "conn_2"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_websocket1 = AsyncMock(spec=WebSocket)
    mock_websocket1.client_state = MagicMock()
    mock_websocket1.client_state.name = "CONNECTED"
    mock_websocket2 = AsyncMock(spec=WebSocket)
    mock_websocket2.client_state = MagicMock()
    mock_websocket2.client_state.name = "CONNECTED"
    mock_manager.active_websockets = {connection_id1: mock_websocket1, connection_id2: mock_websocket2}
    mock_manager.connection_metadata = {connection_id1: {"key": "value1"}, connection_id2: {"key": "value2"}}
    mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}

    result = await _disconnect_all_connections_for_session([connection_id1, connection_id2], player_id, mock_manager)

    assert result == 2
    assert connection_id1 not in mock_manager.active_websockets
    assert connection_id2 not in mock_manager.active_websockets
    assert connection_id1 not in mock_manager.connection_metadata
    assert connection_id2 not in mock_manager.connection_metadata
    assert player_id not in mock_manager.player_websockets


@pytest.mark.asyncio
async def test_disconnect_all_connections_for_session_empty_list():
    """Test _disconnect_all_connections_for_session() handles empty list."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.connection_metadata = {}
    mock_manager.player_websockets = {}

    result = await _disconnect_all_connections_for_session([], player_id, mock_manager)

    assert result == 0


@pytest.mark.asyncio
async def test_disconnect_all_connections_for_session_partial_success():
    """Test _disconnect_all_connections_for_session() handles partial disconnections."""
    connection_id1 = "conn_1"
    connection_id2 = "conn_2"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_websocket1 = AsyncMock(spec=WebSocket)
    mock_websocket1.client_state = MagicMock()
    mock_websocket1.client_state.name = "CONNECTED"
    mock_manager.active_websockets = {connection_id1: mock_websocket1}  # Only conn_1 exists
    mock_manager.connection_metadata = {connection_id1: {"key": "value1"}}
    mock_manager.player_websockets = {player_id: [connection_id1, connection_id2]}

    result = await _disconnect_all_connections_for_session([connection_id1, connection_id2], player_id, mock_manager)

    assert result == 1
    assert connection_id1 not in mock_manager.active_websockets


def test_cleanup_old_session_tracking_no_player():
    """Test _cleanup_old_session_tracking() handles player not in player_sessions."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.player_sessions = {}

    _cleanup_old_session_tracking(player_id, mock_manager)

    # Should not raise


def test_cleanup_old_session_tracking_success():
    """Test _cleanup_old_session_tracking() cleans up old session."""
    player_id = uuid.uuid4()
    old_session_id = "old_session"
    mock_manager = MagicMock()
    mock_manager.player_sessions = {player_id: old_session_id}
    mock_manager.session_connections = {old_session_id: ["conn_1", "conn_2"]}

    _cleanup_old_session_tracking(player_id, mock_manager)

    assert old_session_id not in mock_manager.session_connections


def test_cleanup_old_session_tracking_session_not_in_connections():
    """Test _cleanup_old_session_tracking() handles session not in session_connections."""
    player_id = uuid.uuid4()
    old_session_id = "old_session"
    mock_manager = MagicMock()
    mock_manager.player_sessions = {player_id: old_session_id}
    mock_manager.session_connections = {}

    _cleanup_old_session_tracking(player_id, mock_manager)

    # Should not raise


def test_cleanup_player_data_for_session():
    """Test _cleanup_player_data_for_session() cleans up all player data."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_player_data = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.last_seen = {player_id: 1234567890}
    mock_manager.last_active_update_times = {player_id: 1234567890}
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.remove_player_from_all_rooms = MagicMock()

    _cleanup_player_data_for_session(player_id, mock_manager)

    mock_manager.rate_limiter.remove_player_data.assert_called_once_with(str(player_id))
    mock_manager.message_queue.remove_player_messages.assert_called_once_with(str(player_id))
    assert player_id not in mock_manager.last_seen
    assert player_id not in mock_manager.last_active_update_times
    mock_manager.room_manager.remove_player_from_all_rooms.assert_called_once_with(str(player_id))


def test_cleanup_player_data_for_session_no_last_seen():
    """Test _cleanup_player_data_for_session() handles player not in last_seen."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_player_data = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.last_seen = {}
    mock_manager.last_active_update_times = {}
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.remove_player_from_all_rooms = MagicMock()

    _cleanup_player_data_for_session(player_id, mock_manager)

    # Should not raise


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_success():
    """Test handle_new_game_session_impl() successfully handles new session."""
    player_id = uuid.uuid4()
    new_session_id = "new_session"
    old_session_id = "old_session"
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_websocket = AsyncMock(spec=WebSocket)
    mock_websocket.client_state = MagicMock()
    mock_websocket.client_state.name = "CONNECTED"
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: mock_websocket}
    mock_manager.connection_metadata = {connection_id: {"key": "value"}}
    mock_manager.player_sessions = {player_id: old_session_id}
    mock_manager.session_connections = {old_session_id: [connection_id]}
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_player_data = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.last_seen = {}
    mock_manager.last_active_update_times = {}
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.remove_player_from_all_rooms = MagicMock()

    result = await handle_new_game_session_impl(player_id, new_session_id, mock_manager)

    assert result["success"] is True
    assert result["player_id"] == player_id
    assert result["new_session_id"] == new_session_id
    assert result["previous_session_id"] == old_session_id
    assert result["connections_disconnected"] == 1
    assert result["websocket_connections"] == 1
    assert mock_manager.player_sessions[player_id] == new_session_id
    assert new_session_id in mock_manager.session_connections
    assert old_session_id not in mock_manager.session_connections


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_no_existing_session():
    """Test handle_new_game_session_impl() handles player with no existing session."""
    player_id = uuid.uuid4()
    new_session_id = "new_session"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}
    mock_manager.active_websockets = {}
    mock_manager.connection_metadata = {}
    mock_manager.player_sessions = {}
    mock_manager.session_connections = {}
    mock_manager.rate_limiter = MagicMock()
    mock_manager.rate_limiter.remove_player_data = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.last_seen = {}
    mock_manager.last_active_update_times = {}
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.remove_player_from_all_rooms = MagicMock()

    result = await handle_new_game_session_impl(player_id, new_session_id, mock_manager)

    assert result["success"] is True
    assert result["previous_session_id"] is None
    assert result["connections_disconnected"] == 0
    assert result["websocket_connections"] == 0


@pytest.mark.asyncio
async def test_handle_new_game_session_impl_error():
    """Test handle_new_game_session_impl() handles errors."""

    player_id = uuid.uuid4()
    new_session_id = "new_session"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}
    del mock_manager.player_sessions  # Cause AttributeError

    result = await handle_new_game_session_impl(player_id, new_session_id, mock_manager)

    assert result["success"] is False
    assert len(result["errors"]) > 0
