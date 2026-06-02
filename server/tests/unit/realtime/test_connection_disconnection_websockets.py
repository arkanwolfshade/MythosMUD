"""
Unit tests for connection disconnection websocket functions.

Tests the websocket disconnection functions in connection_disconnection.py.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests target connection_disconnection module helpers not exposed as public API.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_disconnection import _disconnect_all_websockets, disconnect_connection_by_id_impl
from server.realtime.message_queue import MessageQueue
from server.realtime.rate_limiter import RateLimiter


@pytest.fixture
def mock_manager() -> MagicMock:
    """Create a mock connection manager."""
    manager: MagicMock = MagicMock()
    active_websockets: dict[str, MagicMock | None] = {}
    manager.active_websockets = active_websockets
    manager.connection_metadata = {}
    rate_limiter: MagicMock = MagicMock(spec=RateLimiter)
    remove_connection_message_data_mock: MagicMock = MagicMock()
    rate_limiter.remove_connection_message_data = remove_connection_message_data_mock
    remove_player_data_mock: MagicMock = MagicMock()
    rate_limiter.remove_player_data = remove_player_data_mock
    manager.rate_limiter = rate_limiter
    return manager


@pytest.fixture
def mock_safe_close_websocket() -> AsyncMock:
    """Patch safe_close_websocket_impl used by disconnection helpers."""
    with patch(
        "server.realtime.connection_disconnection.safe_close_websocket_impl",
        new_callable=AsyncMock,
    ) as mock_impl:
        yield mock_impl


@pytest.mark.asyncio
async def test_disconnect_all_websockets_empty_list(mock_manager: MagicMock):
    """Test _disconnect_all_websockets() with empty connection list."""
    player_id = uuid.uuid4()
    await _disconnect_all_websockets([], player_id, mock_manager)
    # Should complete without errors


@pytest.mark.asyncio
async def test_disconnect_all_websockets_idempotent_second_pass(
    mock_manager: MagicMock, mock_safe_close_websocket: AsyncMock
):
    """Second disconnect pass must not KeyError when registry already cleared."""
    safe_close_websocket = mock_safe_close_websocket
    player_id = uuid.uuid4()
    connection_id = "conn_001"
    mock_websocket = MagicMock()
    active_websockets: dict[str, MagicMock | None] = {connection_id: mock_websocket}
    mock_manager.active_websockets = active_websockets
    mock_manager.connection_metadata = {connection_id: MagicMock()}
    await _disconnect_all_websockets([connection_id], player_id, mock_manager)
    await _disconnect_all_websockets([connection_id], player_id, mock_manager)
    assert connection_id not in active_websockets
    safe_close_websocket.assert_awaited_once()


@pytest.mark.asyncio
async def test_disconnect_all_websockets_continues_after_none_websocket(
    mock_manager: MagicMock, mock_safe_close_websocket: AsyncMock
):
    """None websocket on one connection must not skip remaining connection ids."""
    safe_close_websocket = mock_safe_close_websocket
    player_id = uuid.uuid4()
    good_socket = MagicMock()
    active_websockets: dict[str, MagicMock | None] = {"conn_bad": None, "conn_good": good_socket}
    mock_manager.active_websockets = active_websockets
    mock_manager.connection_metadata = {}
    await _disconnect_all_websockets(["conn_bad", "conn_good"], player_id, mock_manager)
    assert "conn_bad" not in active_websockets
    assert "conn_good" not in active_websockets
    safe_close_websocket.assert_awaited_once()


@pytest.mark.asyncio
async def test_disconnect_connection_by_id_impl_not_found(mock_manager: MagicMock):
    """Test disconnect_connection_by_id_impl() returns False when connection not found."""
    result = await disconnect_connection_by_id_impl("conn_001", mock_manager)
    assert result is False


@pytest.mark.asyncio
async def test_disconnect_connection_by_id_impl_websocket(mock_manager: MagicMock):
    """Test disconnect_connection_by_id_impl() disconnects websocket connection."""
    connection_id = "conn_001"
    player_id = uuid.uuid4()
    mock_metadata = MagicMock()
    mock_metadata.player_id = player_id
    mock_metadata.connection_type = "websocket"
    mock_manager.connection_metadata = {connection_id: mock_metadata}
    active_websockets: dict[str, MagicMock | None] = {connection_id: MagicMock()}
    mock_manager.active_websockets = active_websockets
    mock_manager.player_websockets = {player_id: {connection_id}}
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    message_queue: MagicMock = MagicMock(spec=MessageQueue)
    remove_player_messages_mock: MagicMock = MagicMock()
    message_queue.remove_player_messages = remove_player_messages_mock
    mock_manager.message_queue = message_queue
    mock_manager.last_seen = {}
    mock_manager.last_active_update_times = {}
    mock_manager.room_manager = MagicMock()
    result = await disconnect_connection_by_id_impl(connection_id, mock_manager)
    assert result is True
