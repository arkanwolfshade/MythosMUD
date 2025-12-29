"""
Unit tests for connection establishment.

Tests the connection_establishment module functions.
"""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import WebSocket

from server.realtime.connection_establishment import (
    _cleanup_dead_connections,
    _cleanup_failed_connection,
    _find_dead_connections,
    _register_new_connection,
    _remove_dead_connection,
    _setup_connection_metadata,
    _setup_player_and_room,
    _setup_session_tracking,
    _track_player_presence,
    _update_player_connection_list,
    establish_websocket_connection,
)


def test_find_dead_connections_no_player():
    """Test _find_dead_connections() returns empty list when player not found."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}

    result = _find_dead_connections(player_id, mock_manager)

    assert result == []


def test_find_dead_connections_all_active():
    """Test _find_dead_connections() returns empty list when all connections are active."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_websocket = MagicMock()
    mock_websocket.client_state.name = "CONNECTED"
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: mock_websocket}

    result = _find_dead_connections(player_id, mock_manager)

    assert result == []


def test_find_dead_connections_not_in_active():
    """Test _find_dead_connections() skips connections not in active_websockets."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {}

    result = _find_dead_connections(player_id, mock_manager)

    assert result == []


def test_find_dead_connections_none_websocket():
    """Test _find_dead_connections() raises ConnectionError when websocket is None."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: None}

    with pytest.raises(ConnectionError, match="WebSocket is None"):
        _find_dead_connections(player_id, mock_manager)


def test_find_dead_connections_not_connected():
    """Test _find_dead_connections() finds dead connections."""
    player_id = uuid.uuid4()
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_websocket = MagicMock()
    mock_websocket.client_state.name = "DISCONNECTED"
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: mock_websocket}

    result = _find_dead_connections(player_id, mock_manager)

    assert connection_id in result


def test_remove_dead_connection():
    """Test _remove_dead_connection() removes connection from tracking."""
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.active_websockets = {connection_id: MagicMock()}
    mock_manager.connection_metadata = {connection_id: {"key": "value"}}

    _remove_dead_connection(connection_id, mock_manager)

    assert connection_id not in mock_manager.active_websockets
    assert connection_id not in mock_manager.connection_metadata


def test_remove_dead_connection_not_present():
    """Test _remove_dead_connection() handles connection not present."""
    connection_id = "conn_123"
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}
    mock_manager.connection_metadata = {}

    _remove_dead_connection(connection_id, mock_manager)

    # Should not raise


def test_update_player_connection_list_no_player():
    """Test _update_player_connection_list() handles player not in player_websockets."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}

    _update_player_connection_list(player_id, mock_manager)

    # Should not raise


def test_update_player_connection_list_with_active():
    """Test _update_player_connection_list() keeps active connections."""
    player_id = uuid.uuid4()
    active_conn = "conn_active"
    dead_conn = "conn_dead"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {player_id: [active_conn, dead_conn]}
    mock_manager.active_websockets = {active_conn: MagicMock()}

    _update_player_connection_list(player_id, mock_manager)

    assert mock_manager.player_websockets[player_id] == [active_conn]


def test_update_player_connection_list_no_active():
    """Test _update_player_connection_list() removes player when no active connections."""
    player_id = uuid.uuid4()
    dead_conn = "conn_dead"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {player_id: [dead_conn]}
    mock_manager.active_websockets = {}

    _update_player_connection_list(player_id, mock_manager)

    assert player_id not in mock_manager.player_websockets


@pytest.mark.asyncio
async def test_cleanup_dead_connections_empty_list():
    """Test _cleanup_dead_connections() handles empty list."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.disconnect_lock = asyncio.Lock()

    await _cleanup_dead_connections([], player_id, mock_manager)

    # Should not raise


@pytest.mark.asyncio
async def test_cleanup_dead_connections_with_dead():
    """Test _cleanup_dead_connections() cleans up dead connections."""
    player_id = uuid.uuid4()
    dead_conn = "conn_dead"
    mock_manager = MagicMock()
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.active_websockets = {dead_conn: MagicMock()}
    mock_manager.connection_metadata = {dead_conn: {"key": "value"}}
    mock_manager.player_websockets = {player_id: [dead_conn]}
    mock_manager.active_websockets = {}

    await _cleanup_dead_connections([dead_conn], player_id, mock_manager)

    assert dead_conn not in mock_manager.active_websockets
    assert dead_conn not in mock_manager.connection_metadata


def test_register_new_connection():
    """Test _register_new_connection() registers new connection."""
    mock_websocket = MagicMock(spec=WebSocket)
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}
    mock_manager.player_websockets = {}

    connection_id = _register_new_connection(mock_websocket, player_id, mock_manager)

    assert connection_id is not None
    assert connection_id in mock_manager.active_websockets
    assert mock_manager.active_websockets[connection_id] == mock_websocket
    assert player_id in mock_manager.player_websockets
    assert connection_id in mock_manager.player_websockets[player_id]


def test_register_new_connection_existing_player():
    """Test _register_new_connection() adds to existing player connections."""
    mock_websocket = MagicMock(spec=WebSocket)
    player_id = uuid.uuid4()
    existing_conn = "existing_conn"
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}
    mock_manager.player_websockets = {player_id: [existing_conn]}

    connection_id = _register_new_connection(mock_websocket, player_id, mock_manager)

    assert connection_id in mock_manager.player_websockets[player_id]
    assert len(mock_manager.player_websockets[player_id]) == 2


def test_setup_connection_metadata():
    """Test _setup_connection_metadata() creates metadata."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    session_id = "session_123"
    token = "jwt_token"
    mock_manager = MagicMock()
    mock_manager.connection_metadata = {}

    _setup_connection_metadata(connection_id, player_id, mock_manager, session_id, token)

    assert connection_id in mock_manager.connection_metadata
    metadata = mock_manager.connection_metadata[connection_id]
    assert metadata.connection_id == connection_id
    assert metadata.player_id == player_id
    assert metadata.session_id == session_id
    assert metadata.token == token


def test_setup_connection_metadata_no_session_token():
    """Test _setup_connection_metadata() handles None session and token."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.connection_metadata = {}

    _setup_connection_metadata(connection_id, player_id, mock_manager, None, None)

    metadata = mock_manager.connection_metadata[connection_id]
    assert metadata.session_id is None
    assert metadata.token is None
    assert metadata.last_token_validation is None


def test_setup_session_tracking_no_session_id():
    """Test _setup_session_tracking() handles None session_id."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}

    _setup_session_tracking(connection_id, player_id, None, mock_manager)

    # Should not modify anything
    assert connection_id not in str(mock_manager.session_connections.values())


def test_setup_session_tracking_new_session():
    """Test _setup_session_tracking() creates new session entry."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    session_id = "session_123"
    mock_manager = MagicMock()
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}

    _setup_session_tracking(connection_id, player_id, session_id, mock_manager)

    assert session_id in mock_manager.session_connections
    assert connection_id in mock_manager.session_connections[session_id]
    assert mock_manager.player_sessions[player_id] == session_id


def test_setup_session_tracking_existing_session():
    """Test _setup_session_tracking() adds to existing session."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    session_id = "session_123"
    existing_conn = "existing_conn"
    mock_manager = MagicMock()
    mock_manager.session_connections = {session_id: [existing_conn]}
    mock_manager.player_sessions = {player_id: session_id}

    _setup_session_tracking(connection_id, player_id, session_id, mock_manager)

    assert len(mock_manager.session_connections[session_id]) == 2
    assert connection_id in mock_manager.session_connections[session_id]


@pytest.mark.asyncio
async def test_setup_player_and_room_success():
    """Test _setup_player_and_room() successfully sets up player and room."""
    player_id = uuid.uuid4()
    room_id = "room_123"
    mock_manager = MagicMock()
    mock_player = MagicMock()
    mock_player.current_room_id = room_id
    mock_manager._get_player = AsyncMock(return_value=mock_player)
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.subscribe_to_room = MagicMock()
    mock_manager.async_persistence = MagicMock()

    success, player = await _setup_player_and_room(player_id, mock_manager)

    assert success is True
    assert player == mock_player
    mock_manager.room_manager.subscribe_to_room.assert_called_once_with(str(player_id), room_id)


@pytest.mark.asyncio
async def test_setup_player_and_room_no_player():
    """Test _setup_player_and_room() returns False when player not found."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager._get_player = AsyncMock(return_value=None)
    mock_manager.async_persistence = MagicMock()

    success, player = await _setup_player_and_room(player_id, mock_manager)

    assert success is False
    assert player is None


@pytest.mark.asyncio
async def test_setup_player_and_room_no_persistence():
    """Test _setup_player_and_room() handles no persistence."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager._get_player = AsyncMock(return_value=None)
    mock_manager.async_persistence = None
    # When persistence is None, it logs warning but continues (returns True, None)
    # This allows connection without player tracking

    success, player = await _setup_player_and_room(player_id, mock_manager)

    # When persistence is None, it allows connection without player tracking
    # The function returns True, None to allow connection to proceed
    assert success is True
    assert player is None


@pytest.mark.asyncio
async def test_setup_player_and_room_no_room_id():
    """Test _setup_player_and_room() handles player with no room_id."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_player = MagicMock()
    del mock_player.current_room_id  # Remove room_id
    mock_manager._get_player = AsyncMock(return_value=mock_player)
    mock_manager.room_manager = MagicMock()
    mock_manager.async_persistence = MagicMock()

    success, player = await _setup_player_and_room(player_id, mock_manager)

    assert success is True
    assert player == mock_player
    mock_manager.room_manager.subscribe_to_room.assert_not_called()


@pytest.mark.asyncio
async def test_track_player_presence_new_player():
    """Test _track_player_presence() tracks new player."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_manager = MagicMock()
    mock_manager.online_players = {}
    mock_manager._track_player_connected = AsyncMock()

    await _track_player_presence(player_id, mock_player, mock_manager)

    mock_manager._track_player_connected.assert_called_once_with(player_id, mock_player, "websocket")


@pytest.mark.asyncio
async def test_track_player_presence_existing_player():
    """Test _track_player_presence() broadcasts for existing player."""
    player_id = uuid.uuid4()
    mock_player = MagicMock()
    mock_manager = MagicMock()
    mock_manager.online_players = {player_id: mock_player}
    mock_manager._broadcast_connection_message = AsyncMock()

    await _track_player_presence(player_id, mock_player, mock_manager)

    mock_manager._broadcast_connection_message.assert_called_once_with(player_id, mock_player)


def test_cleanup_failed_connection_none():
    """Test _cleanup_failed_connection() handles None connection_id."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()

    _cleanup_failed_connection(None, player_id, mock_manager)

    # Should not raise or modify anything


def test_cleanup_failed_connection_success():
    """Test _cleanup_failed_connection() cleans up connection."""
    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.active_websockets = {connection_id: MagicMock()}
    mock_manager.connection_metadata = {connection_id: {"key": "value"}}

    _cleanup_failed_connection(connection_id, player_id, mock_manager)

    assert connection_id not in mock_manager.active_websockets
    assert connection_id not in mock_manager.connection_metadata


def test_cleanup_failed_connection_error():
    """Test _cleanup_failed_connection() handles errors during cleanup."""

    connection_id = "conn_123"
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.active_websockets = {}
    del mock_manager.connection_metadata  # Cause AttributeError

    _cleanup_failed_connection(connection_id, player_id, mock_manager)

    # Should not raise, just log warning


@pytest.mark.asyncio
async def test_establish_websocket_connection_success():
    """Test establish_websocket_connection() successfully establishes connection."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = uuid.uuid4()
    session_id = "session_123"
    token = "jwt_token"
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}
    mock_manager.active_websockets = {}
    mock_manager.connection_metadata = {}
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.subscribe_to_room = MagicMock()
    mock_manager.online_players = {}
    mock_manager.performance_tracker = MagicMock()
    mock_manager.performance_tracker.record_connection_establishment = MagicMock()
    mock_manager.async_persistence = MagicMock()

    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager._get_player = AsyncMock(return_value=mock_player)
    mock_manager._track_player_connected = AsyncMock()

    success, connection_id = await establish_websocket_connection(
        mock_websocket, player_id, mock_manager, session_id, token
    )

    assert success is True
    assert connection_id is not None
    mock_websocket.accept.assert_called_once()
    assert connection_id in mock_manager.active_websockets
    mock_manager.performance_tracker.record_connection_establishment.assert_called_once()


@pytest.mark.asyncio
async def test_establish_websocket_connection_player_not_found():
    """Test establish_websocket_connection() returns False when player not found."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}
    mock_manager.active_websockets = {}
    mock_manager.connection_metadata = {}
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.async_persistence = MagicMock()
    mock_manager._get_player = AsyncMock(return_value=None)

    success, connection_id = await establish_websocket_connection(mock_websocket, player_id, mock_manager)

    assert success is False
    assert connection_id is not None  # Connection was registered before player check


@pytest.mark.asyncio
async def test_establish_websocket_connection_error():
    """Test establish_websocket_connection() handles errors."""
    from server.exceptions import DatabaseError

    mock_websocket = AsyncMock(spec=WebSocket)
    mock_websocket.accept = AsyncMock(side_effect=DatabaseError("Database error"))
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.player_websockets = {}
    mock_manager.active_websockets = {}
    mock_manager.connection_metadata = {}
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}
    mock_manager.disconnect_lock = asyncio.Lock()

    success, connection_id = await establish_websocket_connection(mock_websocket, player_id, mock_manager)

    assert success is False
    # Connection should be cleaned up on error
    assert connection_id is None or connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_establish_websocket_connection_cleans_dead_connections():
    """Test establish_websocket_connection() cleans up dead connections."""
    mock_websocket = AsyncMock(spec=WebSocket)
    player_id = uuid.uuid4()
    dead_conn = "dead_conn"
    mock_manager = MagicMock()
    mock_dead_websocket = MagicMock()
    mock_dead_websocket.client_state.name = "DISCONNECTED"
    mock_manager.player_websockets = {player_id: [dead_conn]}
    mock_manager.active_websockets = {dead_conn: mock_dead_websocket}
    mock_manager.connection_metadata = {}
    mock_manager.session_connections = {}
    mock_manager.player_sessions = {}
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.subscribe_to_room = MagicMock()
    mock_manager.online_players = {}
    mock_manager.performance_tracker = MagicMock()
    mock_manager.performance_tracker.record_connection_establishment = MagicMock()
    mock_manager.async_persistence = MagicMock()

    mock_player = MagicMock()
    mock_player.current_room_id = "room_123"
    mock_manager._get_player = AsyncMock(return_value=mock_player)
    mock_manager._track_player_connected = AsyncMock()

    success, connection_id = await establish_websocket_connection(mock_websocket, player_id, mock_manager)

    assert success is True
    # Dead connection should be cleaned up
    assert dead_conn not in mock_manager.active_websockets
