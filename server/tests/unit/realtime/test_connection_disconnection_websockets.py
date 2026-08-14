"""
Unit tests for connection disconnection websocket functions.

Tests the websocket disconnection functions in connection_disconnection.py.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests target connection_disconnection module helpers not exposed as public API.

import uuid
from collections.abc import Generator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_disconnection import disconnect_all_websockets_impl, disconnect_connection_by_id_impl
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
def mock_safe_close_websocket() -> Generator[AsyncMock, None, None]:
    """Patch safe_close_websocket_impl used by disconnection helpers."""
    with patch(
        "server.realtime.connection_disconnection.safe_close_websocket_impl",
        new_callable=AsyncMock,
    ) as mock_impl:
        yield mock_impl


@pytest.mark.asyncio
async def testdisconnect_all_websockets_impl_empty_list(mock_manager: MagicMock):
    """Test disconnect_all_websockets_impl() with empty connection list."""
    player_id = uuid.uuid4()
    await disconnect_all_websockets_impl([], player_id, mock_manager)
    # Should complete without errors


@pytest.mark.asyncio
async def testdisconnect_all_websockets_impl_idempotent_second_pass(
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
    await disconnect_all_websockets_impl([connection_id], player_id, mock_manager)
    await disconnect_all_websockets_impl([connection_id], player_id, mock_manager)
    assert connection_id not in active_websockets
    safe_close_websocket.assert_awaited_once()


@pytest.mark.asyncio
async def testdisconnect_all_websockets_impl_continues_after_none_websocket(
    mock_manager: MagicMock, mock_safe_close_websocket: AsyncMock
):
    """None websocket on one connection must not skip remaining connection ids."""
    safe_close_websocket = mock_safe_close_websocket
    player_id = uuid.uuid4()
    good_socket = MagicMock()
    active_websockets: dict[str, MagicMock | None] = {"conn_bad": None, "conn_good": good_socket}
    mock_manager.active_websockets = active_websockets
    mock_manager.connection_metadata = {}
    await disconnect_all_websockets_impl(["conn_bad", "conn_good"], player_id, mock_manager)
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


@pytest.mark.asyncio
async def test_safe_close_websocket_swallows_websocket_disconnect():
    """Regression: e2e logout hit WebSocketDisconnect on close and aborted leave cleanup."""
    from fastapi import WebSocketDisconnect

    from server.realtime.connection_manager_methods import safe_close_websocket_impl

    manager: MagicMock = MagicMock()
    manager.is_websocket_closed = MagicMock(return_value=False)
    manager.mark_websocket_closed = MagicMock()
    websocket = AsyncMock()
    websocket.close = AsyncMock(side_effect=WebSocketDisconnect(code=1006))
    with patch("server.realtime.connection_manager_methods.is_websocket_open_impl", return_value=True):
        await safe_close_websocket_impl(manager, websocket, code=1000, reason="Connection closed")
    manager.mark_websocket_closed.assert_called()


@pytest.mark.asyncio
async def test_cleanup_websocket_disconnect_continues_after_close_error():
    """Close failures must not skip intentional leave tracking / room cleanup."""
    import asyncio

    from server.realtime.connection_disconnection import cleanup_websocket_disconnect

    player_id = uuid.uuid4()
    manager: MagicMock = MagicMock()
    manager.disconnect_lock = asyncio.Lock()
    manager.processed_disconnect_lock = asyncio.Lock()
    manager.player_websockets = {player_id: ["conn_001"]}
    manager.intentional_disconnects = {player_id}
    manager.processed_disconnects = set()
    manager.has_websocket_connection = MagicMock(return_value=False)
    manager.room_manager = MagicMock()
    manager.rate_limiter = MagicMock()
    manager.message_queue = MagicMock()
    manager.last_seen = {}
    manager.last_active_update_times = {}

    with patch(
        "server.realtime.connection_disconnection.disconnect_all_websockets_impl",
        new_callable=AsyncMock,
        side_effect=RuntimeError("close failed"),
    ):
        result = await cleanup_websocket_disconnect(player_id, manager, is_force_disconnect=True)

    assert result is True
    manager.room_manager.remove_player_from_all_rooms.assert_called()
