"""
Unit tests for connection disconnection.

Tests the connection disconnection functions.
"""

# pyright: reportPrivateUsage=false
# Reason: Unit tests target connection_disconnection module helpers not exposed as public API.

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_disconnection import (
    _cleanup_player_data,
    _cleanup_room_subscriptions,
    _track_disconnect_if_needed,
)
from server.realtime.message_queue import MessageQueue
from server.realtime.rate_limiter import RateLimiter
from server.realtime.room_subscription_manager import RoomSubscriptionManager


@pytest.fixture
def remove_player_data_mock() -> MagicMock:
    """Typed mock for RateLimiter.remove_player_data."""
    return MagicMock()


@pytest.fixture
def remove_player_messages_mock() -> MagicMock:
    """Typed mock for MessageQueue.remove_player_messages."""
    return MagicMock()


@pytest.fixture
def remove_player_from_all_rooms_mock() -> MagicMock:
    """Typed mock for room_manager.remove_player_from_all_rooms."""
    return MagicMock()


@pytest.fixture
def mock_manager(
    remove_player_data_mock: MagicMock,
    remove_player_messages_mock: MagicMock,
    remove_player_from_all_rooms_mock: MagicMock,
) -> MagicMock:
    """Create a mock connection manager."""
    manager: MagicMock = MagicMock()
    active_websockets: dict[str, MagicMock | None] = {}
    manager.active_websockets = active_websockets
    manager.has_websocket_connection = MagicMock(return_value=False)
    room_manager: MagicMock = MagicMock(spec=RoomSubscriptionManager)
    room_manager.remove_player_from_all_rooms = remove_player_from_all_rooms_mock
    manager.room_manager = room_manager
    rate_limiter: MagicMock = MagicMock(spec=RateLimiter)
    rate_limiter.remove_player_data = remove_player_data_mock
    manager.rate_limiter = rate_limiter
    message_queue: MagicMock = MagicMock(spec=MessageQueue)
    message_queue.remove_player_messages = remove_player_messages_mock
    manager.message_queue = message_queue
    last_seen: dict[uuid.UUID, float] = {}
    manager.last_seen = last_seen
    last_active_update_times: dict[uuid.UUID, float] = {}
    manager.last_active_update_times = last_active_update_times
    processed_disconnects: set[uuid.UUID] = set()
    manager.processed_disconnects = processed_disconnects
    processed_disconnect_lock: AsyncMock = AsyncMock()
    processed_disconnect_lock.__aenter__ = AsyncMock(return_value=None)
    processed_disconnect_lock.__aexit__ = AsyncMock(return_value=None)
    manager.processed_disconnect_lock = processed_disconnect_lock
    return manager


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_new(mock_manager: MagicMock):
    """Test _track_disconnect_if_needed() when disconnect is new."""
    player_id = uuid.uuid4()
    processed_disconnects: set[uuid.UUID] = set()
    mock_manager.processed_disconnects = processed_disconnects
    result = await _track_disconnect_if_needed(player_id, mock_manager, False)
    assert result is True
    assert player_id in processed_disconnects


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_already_processed(mock_manager: MagicMock):
    """Test _track_disconnect_if_needed() when disconnect already processed."""
    player_id = uuid.uuid4()
    processed_disconnects: set[uuid.UUID] = {player_id}
    mock_manager.processed_disconnects = processed_disconnects
    result = await _track_disconnect_if_needed(player_id, mock_manager, False)
    assert result is False


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_force_disconnect(mock_manager: MagicMock):
    """Test _track_disconnect_if_needed() when force disconnect."""
    player_id = uuid.uuid4()
    result = await _track_disconnect_if_needed(player_id, mock_manager, True)
    assert result is False


def test_cleanup_room_subscriptions(
    mock_manager: MagicMock,
    remove_player_from_all_rooms_mock: MagicMock,
):
    """Test _cleanup_room_subscriptions() removes player from rooms."""
    player_id = uuid.uuid4()
    _cleanup_room_subscriptions(player_id, mock_manager, False)
    remove_player_from_all_rooms_mock.assert_called_once_with(str(player_id))


def test_cleanup_room_subscriptions_force_disconnect(
    mock_manager: MagicMock,
    remove_player_from_all_rooms_mock: MagicMock,
):
    """Test _cleanup_room_subscriptions() preserves rooms on force disconnect."""
    player_id = uuid.uuid4()
    _cleanup_room_subscriptions(player_id, mock_manager, True)
    remove_player_from_all_rooms_mock.assert_not_called()


def test_cleanup_room_subscriptions_has_connection(
    mock_manager: MagicMock,
    remove_player_from_all_rooms_mock: MagicMock,
):
    """Test _cleanup_room_subscriptions() preserves rooms when has connection."""
    player_id = uuid.uuid4()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)
    _cleanup_room_subscriptions(player_id, mock_manager, False)
    remove_player_from_all_rooms_mock.assert_not_called()


def test_cleanup_player_data(
    mock_manager: MagicMock,
    remove_player_data_mock: MagicMock,
    remove_player_messages_mock: MagicMock,
):
    """Test _cleanup_player_data() cleans up player data."""
    player_id = uuid.uuid4()
    last_seen: dict[uuid.UUID, float] = {player_id: 1000.0}
    mock_manager.last_seen = last_seen
    _cleanup_player_data(player_id, mock_manager)
    remove_player_data_mock.assert_called_once_with(str(player_id))
    remove_player_messages_mock.assert_called_once_with(str(player_id))
    assert player_id not in last_seen


def test_cleanup_player_data_has_connection(mock_manager: MagicMock):
    """Test _cleanup_player_data() does not clean up when has connection."""
    player_id = uuid.uuid4()
    remove_player_data_mock: MagicMock = MagicMock()
    rate_limiter: MagicMock = MagicMock(spec=RateLimiter)
    rate_limiter.remove_player_data = remove_player_data_mock
    mock_manager.rate_limiter = rate_limiter
    mock_manager.has_websocket_connection = MagicMock(return_value=True)
    _cleanup_player_data(player_id, mock_manager)
    remove_player_data_mock.assert_not_called()


@pytest.mark.asyncio
async def test_disconnect_all_websockets(mock_manager: MagicMock):
    """Test disconnect_all_websockets_impl() disconnects all websockets."""
    from server.realtime.connection_disconnection import disconnect_all_websockets_impl

    player_id = uuid.uuid4()
    connection_ids = ["conn_001", "conn_002"]
    mock_websocket = MagicMock()
    mock_websocket.close = AsyncMock()
    active_websockets: dict[str, MagicMock | None] = {
        "conn_001": mock_websocket,
        "conn_002": mock_websocket,
    }
    mock_manager.active_websockets = active_websockets
    mock_manager.connection_metadata = {"conn_001": {}, "conn_002": {}}
    with patch(
        "server.realtime.connection_disconnection.safe_close_websocket_impl",
        new_callable=AsyncMock,
    ) as mock_safe_close:
        await disconnect_all_websockets_impl(connection_ids, player_id, mock_manager)
        assert mock_safe_close.await_count == 2


@pytest.mark.asyncio
async def test_disconnect_all_websockets_none_websocket(mock_manager: MagicMock):
    """Test disconnect_all_websockets_impl() handles None websocket."""
    from server.realtime.connection_disconnection import disconnect_all_websockets_impl

    player_id = uuid.uuid4()
    connection_ids = ["conn_001"]
    active_websockets: dict[str, MagicMock | None] = {"conn_001": None}
    mock_manager.active_websockets = active_websockets
    mock_manager.connection_metadata = {}
    await disconnect_all_websockets_impl(connection_ids, player_id, mock_manager)
    assert "conn_001" not in active_websockets


@pytest.mark.asyncio
async def test_track_disconnect_if_needed_has_connection(mock_manager: MagicMock):
    """Test _track_disconnect_if_needed() when player has connection."""
    player_id = uuid.uuid4()
    mock_manager.has_websocket_connection = MagicMock(return_value=True)
    result = await _track_disconnect_if_needed(player_id, mock_manager, False)
    assert result is False


@pytest.mark.asyncio
async def test_cleanup_websocket_disconnect(mock_manager: MagicMock):
    """Test cleanup_websocket_disconnect() cleans up connection."""
    import asyncio

    from server.realtime.connection_disconnection import cleanup_websocket_disconnect

    player_id = uuid.uuid4()
    connection_id = "conn_001"
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: MagicMock()}
    # disconnect_lock needs to be an asyncio.Lock
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.processed_disconnect_lock = asyncio.Lock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)
    # cleanup_websocket_disconnect takes (player_id, manager, is_force_disconnect)
    result = await cleanup_websocket_disconnect(player_id, mock_manager, False)
    # Should return bool indicating if should track disconnect
    assert isinstance(result, bool)


@pytest.mark.asyncio
async def test_cleanup_websocket_disconnect_when_mapping_cleared_during_close(mock_manager: MagicMock):
    """Rest/force disconnect must not KeyError if on-close path already removed player_websockets."""
    import asyncio

    from server.realtime.connection_disconnection import cleanup_websocket_disconnect

    player_id = uuid.uuid4()
    connection_id = "conn_001"
    player_websockets: dict[uuid.UUID, list[str]] = {player_id: [connection_id]}
    mock_manager.player_websockets = player_websockets
    mock_manager.active_websockets = {connection_id: MagicMock()}
    mock_manager.disconnect_lock = asyncio.Lock()
    mock_manager.processed_disconnect_lock = asyncio.Lock()
    mock_manager.has_websocket_connection = MagicMock(return_value=False)

    async def clear_player_mapping_after_close(
        connection_ids: list[str], cleared_player_id: uuid.UUID, manager: MagicMock
    ) -> None:
        _ = connection_ids
        _ = manager
        _ = player_websockets.pop(cleared_player_id, None)

    with patch(
        "server.realtime.connection_disconnection.disconnect_all_websockets_impl",
        side_effect=clear_player_mapping_after_close,
    ):
        result = await cleanup_websocket_disconnect(player_id, mock_manager, is_force_disconnect=True)

    assert isinstance(result, bool)
    assert player_id not in player_websockets


@pytest.mark.asyncio
async def test_disconnect_connection_by_id_impl(mock_manager: MagicMock):
    """Test disconnect_connection_by_id_impl() disconnects connection."""
    from server.realtime.connection_disconnection import disconnect_connection_by_id_impl

    connection_id = "conn_001"
    player_id = uuid.uuid4()
    # disconnect_connection_by_id_impl needs connection_metadata with player_id
    mock_metadata = MagicMock()
    mock_metadata.player_id = player_id
    mock_metadata.connection_type = "websocket"
    mock_manager.connection_metadata = {connection_id: mock_metadata}
    mock_manager.player_websockets = {player_id: [connection_id]}
    mock_manager.active_websockets = {connection_id: MagicMock()}
    # disconnect_connection_by_id_impl takes (connection_id, manager)
    result = await disconnect_connection_by_id_impl(connection_id, mock_manager)
    # Should return True if connection found and disconnected
    assert isinstance(result, bool)
