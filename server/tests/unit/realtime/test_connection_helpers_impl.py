"""
Unit tests for connection helpers implementation functions.

Tests the implementation functions in connection_helpers.py.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_helpers import (
    _optimize_payload,
    _queue_message_if_needed,
    _send_to_websockets,
    _update_delivery_status,
    broadcast_global_event_impl,
    broadcast_room_event_impl,
    handle_new_login_impl,
    mark_player_seen_impl,
    send_personal_message_old_impl,
)


@pytest.fixture
def mock_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.player_websockets = {}
    manager.active_websockets = {}
    manager.message_queue = MagicMock()
    manager.message_queue.pending_messages = {}
    manager.last_seen = {}
    manager.last_active_update_times = {}
    manager.last_active_update_interval = 60.0
    manager.async_persistence = MagicMock()
    manager.force_disconnect_player = AsyncMock()
    manager.broadcast_to_room = AsyncMock(return_value={})
    manager.broadcast_global = AsyncMock(return_value={})
    manager._cleanup_dead_websocket = AsyncMock()
    return manager


def test_optimize_payload(mock_manager):
    """Test _optimize_payload() optimizes payload."""
    event = {"event_type": "test", "data": {"player_id": uuid.uuid4()}}
    with patch("server.realtime.payload_optimizer.get_payload_optimizer") as mock_get_optimizer:
        mock_optimizer = MagicMock()
        mock_optimizer.optimize_payload = MagicMock(return_value=event)
        mock_get_optimizer.return_value = mock_optimizer
        result = _optimize_payload(event, "player_001")
        assert "event_type" in result


@pytest.mark.asyncio
async def test_send_to_websockets(mock_manager):
    """Test _send_to_websockets() sends to websockets."""
    player_id = uuid.uuid4()
    mock_manager.player_websockets = {player_id: {"conn_001"}}
    mock_websocket = MagicMock()
    mock_websocket.send_json = AsyncMock()
    mock_manager.active_websockets = {"conn_001": mock_websocket}
    delivery_status = {"websocket_delivered": 0, "websocket_failed": 0, "active_connections": 0}
    event = {"event_type": "test"}
    result = await _send_to_websockets(player_id, event, mock_manager, delivery_status)
    assert result is True
    assert delivery_status["websocket_delivered"] == 1


@pytest.mark.asyncio
async def test_send_to_websockets_no_connections(mock_manager):
    """Test _send_to_websockets() returns False when no connections."""
    player_id = uuid.uuid4()
    delivery_status = {"websocket_delivered": 0, "websocket_failed": 0, "active_connections": 0}
    event = {"event_type": "test"}
    result = await _send_to_websockets(player_id, event, mock_manager, delivery_status)
    assert result is False


def test_queue_message_if_needed(mock_manager):
    """Test _queue_message_if_needed() queues message."""
    player_id = uuid.uuid4()
    event = {"event_type": "test"}
    _queue_message_if_needed(player_id, event, mock_manager, event)
    assert str(player_id) in mock_manager.message_queue.pending_messages
    assert len(mock_manager.message_queue.pending_messages[str(player_id)]) == 1


def test_update_delivery_status_success(mock_manager):
    """Test _update_delivery_status() updates status for success."""
    delivery_status = {"websocket_delivered": 1, "active_connections": 1}
    _update_delivery_status(delivery_status, True)
    assert delivery_status["success"] is True


def test_update_delivery_status_failed(mock_manager):
    """Test _update_delivery_status() updates status for failure."""
    delivery_status = {"websocket_delivered": 0, "websocket_failed": 1, "active_connections": 0}
    _update_delivery_status(delivery_status, True)
    assert delivery_status["success"] is False


@pytest.mark.asyncio
async def test_send_personal_message_old_impl(mock_manager):
    """Test send_personal_message_old_impl() sends message."""
    player_id = uuid.uuid4()
    mock_manager.player_websockets = {player_id: {"conn_001"}}
    mock_websocket = MagicMock()
    mock_websocket.send_json = AsyncMock()
    mock_manager.active_websockets = {"conn_001": mock_websocket}
    event = {"event_type": "test"}
    with patch("server.realtime.connection_helpers._optimize_payload", return_value=event):
        result = await send_personal_message_old_impl(player_id, event, mock_manager)
        assert "success" in result


@pytest.mark.asyncio
async def test_handle_new_login_impl(mock_manager):
    """Test handle_new_login_impl() handles new login."""
    player_id = uuid.uuid4()
    with patch("server.realtime.connection_helpers.open", create=True) as mock_open:
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file
        await handle_new_login_impl(player_id, mock_manager)
        mock_manager.force_disconnect_player.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_broadcast_room_event_impl(mock_manager):
    """Test broadcast_room_event_impl() broadcasts room event."""
    mock_manager.broadcast_to_room = AsyncMock(return_value={"room_id": "room_001", "total_targets": 1})
    result = await broadcast_room_event_impl("test_event", "room_001", {"data": "test"}, mock_manager)
    assert "room_id" in result or "total_targets" in result


@pytest.mark.asyncio
async def test_broadcast_global_event_impl(mock_manager):
    """Test broadcast_global_event_impl() broadcasts global event."""
    mock_manager.broadcast_global = AsyncMock(return_value={"total_players": 1, "successful_deliveries": 1})
    result = await broadcast_global_event_impl("test_event", {"data": "test"}, mock_manager)
    assert "total_players" in result or "successful_deliveries" in result


def test_mark_player_seen_impl(mock_manager):
    """Test mark_player_seen_impl() marks player as seen."""
    player_id = uuid.uuid4()
    mock_manager.player_websockets = {player_id: {"conn_001"}}
    mock_manager.connection_metadata = {"conn_001": MagicMock()}
    mark_player_seen_impl(player_id, mock_manager)
    assert player_id in mock_manager.last_seen
