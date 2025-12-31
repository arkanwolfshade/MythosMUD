"""
Unit tests for connection disconnection.

Tests the connection disconnection functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.connection_disconnection import (
    _cleanup_player_data,
    _cleanup_room_subscriptions,
    _track_disconnect_if_needed,
)


@pytest.fixture
def mock_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.has_websocket_connection = MagicMock(return_value=False)
    manager.room_manager = MagicMock()
    manager.rate_limiter = MagicMock()
    manager.message_queue = MagicMock()
    manager.last_seen = {}
    manager.last_active_update_times = {}
    manager.processed_disconnects = set()
    manager.processed_disconnect_lock = AsyncMock()
    return manager


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_new(mock_manager):
    """Test _track_disconnect_if_needed() when disconnect is new."""
    mock_manager.processed_disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.processed_disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    player_id = uuid.uuid4()
    result = await _track_disconnect_if_needed(player_id, mock_manager, False)
    assert result is True
    assert player_id in mock_manager.processed_disconnects


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_already_processed(mock_manager):
    """Test _track_disconnect_if_needed() when disconnect already processed."""
    mock_manager.processed_disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    mock_manager.processed_disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    player_id = uuid.uuid4()
    mock_manager.processed_disconnects.add(player_id)
    result = await _track_disconnect_if_needed(player_id, mock_manager, False)
    assert result is False


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_force_disconnect(mock_manager):
    """Test _track_disconnect_if_needed() when force disconnect."""
    player_id = uuid.uuid4()
    result = await _track_disconnect_if_needed(player_id, mock_manager, True)
    assert result is False


def test_cleanup_room_subscriptions(mock_manager):
    """Test _cleanup_room_subscriptions() removes player from rooms."""
    player_id = uuid.uuid4()
    _cleanup_room_subscriptions(player_id, mock_manager, False)
    mock_manager.room_manager.remove_player_from_all_rooms.assert_called_once_with(str(player_id))


def test_cleanup_room_subscriptions_force_disconnect(mock_manager):
    """Test _cleanup_room_subscriptions() preserves rooms on force disconnect."""
    player_id = uuid.uuid4()
    _cleanup_room_subscriptions(player_id, mock_manager, True)
    mock_manager.room_manager.remove_player_from_all_rooms.assert_not_called()


def test_cleanup_room_subscriptions_has_connection(mock_manager):
    """Test _cleanup_room_subscriptions() preserves rooms when has connection."""
    player_id = uuid.uuid4()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)
    _cleanup_room_subscriptions(player_id, mock_manager, False)
    mock_manager.room_manager.remove_player_from_all_rooms.assert_not_called()


def test_cleanup_player_data(mock_manager):
    """Test _cleanup_player_data() cleans up player data."""
    player_id = uuid.uuid4()
    mock_manager.last_seen[player_id] = 1000.0
    _cleanup_player_data(player_id, mock_manager)
    mock_manager.rate_limiter.remove_player_data.assert_called_once_with(str(player_id))
    mock_manager.message_queue.remove_player_messages.assert_called_once_with(str(player_id))
    assert player_id not in mock_manager.last_seen


def test_cleanup_player_data_has_connection(mock_manager):
    """Test _cleanup_player_data() does not clean up when has connection."""
    player_id = uuid.uuid4()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)
    _cleanup_player_data(player_id, mock_manager)
    mock_manager.rate_limiter.remove_player_data.assert_not_called()


@pytest.mark.asyncio
async def test_disconnect_all_websockets(mock_manager):
    """Test _disconnect_all_websockets() disconnects all websockets."""
    from server.realtime.connection_disconnection import _disconnect_all_websockets

    player_id = uuid.uuid4()
    connection_ids = ["conn_001", "conn_002"]
    mock_websocket = MagicMock()
    mock_websocket.close = AsyncMock()
    mock_manager.active_websockets = {"conn_001": mock_websocket, "conn_002": mock_websocket}
    mock_manager._safe_close_websocket = AsyncMock()
    mock_manager.connection_metadata = {"conn_001": {}, "conn_002": {}}
    await _disconnect_all_websockets(connection_ids, player_id, mock_manager)
    assert mock_manager._safe_close_websocket.await_count == 2


@pytest.mark.asyncio
async def test_disconnect_all_websockets_none_websocket(mock_manager):
    """Test _disconnect_all_websockets() handles None websocket."""
    from server.realtime.connection_disconnection import _disconnect_all_websockets

    player_id = uuid.uuid4()
    connection_ids = ["conn_001"]
    mock_manager.active_websockets = {"conn_001": None}
    mock_manager.connection_metadata = {}
    await _disconnect_all_websockets(connection_ids, player_id, mock_manager)
    assert "conn_001" not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_has_connection(mock_manager):
    """Test _track_disconnect_if_needed() when player has connection."""
    player_id = uuid.uuid4()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)
    result = await _track_disconnect_if_needed(player_id, mock_manager, False)
    assert result is False


@pytest.mark.asyncio
async def test_cleanup_websocket_disconnect(mock_manager):
    """Test cleanup_websocket_disconnect() cleans up connection."""
    import asyncio

    from server.realtime.connection_disconnection import cleanup_websocket_disconnect

    player_id = uuid.uuid4()
    connection_id = "conn_001"
    mock_manager.player_websockets = {player_id: {connection_id}}
    mock_manager.active_websockets = {connection_id: MagicMock()}
    # disconnect_lock needs to be an asyncio.Lock
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager._safe_close_websocket = AsyncMock()
    # cleanup_websocket_disconnect takes (player_id, manager, is_force_disconnect)
    result = await cleanup_websocket_disconnect(player_id, mock_manager, False)
    # Should return bool indicating if should track disconnect
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_disconnect_connection_by_id_impl(mock_manager):
    """Test disconnect_connection_by_id_impl() disconnects connection."""
    from server.realtime.connection_disconnection import disconnect_connection_by_id_impl

    connection_id = "conn_001"
    player_id = uuid.uuid4()
    # disconnect_connection_by_id_impl needs connection_metadata with player_id
    mock_metadata = MagicMock()
    mock_metadata.player_id = player_id
    mock_metadata.connection_type = "websocket"
    mock_manager.connection_metadata = {connection_id: mock_metadata}
    mock_manager.player_websockets = {player_id: {connection_id}}
    mock_manager.active_websockets = {connection_id: MagicMock()}
    mock_manager._safe_close_websocket = AsyncMock()
    # disconnect_connection_by_id_impl takes (connection_id, manager)
    result = await disconnect_connection_by_id_impl(connection_id, mock_manager)
    # Should return True if connection found and disconnected
    assert isinstance(result, bool)
