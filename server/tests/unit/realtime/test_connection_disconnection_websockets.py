"""
Unit tests for connection disconnection websocket functions.

Tests the websocket disconnection functions in connection_disconnection.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.connection_disconnection import _disconnect_all_websockets, disconnect_connection_by_id_impl


@pytest.fixture
def mock_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.active_websockets = {}
    manager.connection_metadata = {}
    manager.rate_limiter = MagicMock()
    manager.rate_limiter.remove_connection_message_data = MagicMock()
    manager._safe_close_websocket = AsyncMock()
    return manager


@pytest.mark.asyncio
async def test_disconnect_all_websockets_empty_list(mock_manager):
    """Test _disconnect_all_websockets() with empty connection list."""
    player_id = uuid.uuid4()
    await _disconnect_all_websockets([], player_id, mock_manager)
    # Should complete without errors


@pytest.mark.asyncio
async def test_disconnect_all_websockets_none_websocket(mock_manager):
    """Test _disconnect_all_websockets() handles None websocket."""
    player_id = uuid.uuid4()
    connection_id = "conn_001"
    mock_manager.active_websockets = {connection_id: None}
    await _disconnect_all_websockets([connection_id], player_id, mock_manager)
    assert connection_id not in mock_manager.active_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_by_id_impl_not_found(mock_manager):
    """Test disconnect_connection_by_id_impl() returns False when connection not found."""
    result = await disconnect_connection_by_id_impl("conn_001", mock_manager)
    assert result is False


@pytest.mark.asyncio
async def test_disconnect_connection_by_id_impl_websocket(mock_manager):
    """Test disconnect_connection_by_id_impl() disconnects websocket connection."""
    connection_id = "conn_001"
    player_id = uuid.uuid4()
    mock_metadata = MagicMock()
    mock_metadata.player_id = player_id
    mock_metadata.connection_type = "websocket"
    mock_manager.connection_metadata = {connection_id: mock_metadata}
    mock_manager.active_websockets = {connection_id: MagicMock()}
    mock_manager.player_websockets = {player_id: {connection_id}}
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    mock_manager.rate_limiter.remove_player_data = MagicMock()
    mock_manager.message_queue = MagicMock()
    mock_manager.message_queue.remove_player_messages = MagicMock()
    mock_manager.last_seen = {}
    mock_manager.last_active_update_times = {}
    mock_manager.room_manager = MagicMock()
    result = await disconnect_connection_by_id_impl(connection_id, mock_manager)
    assert result is True
