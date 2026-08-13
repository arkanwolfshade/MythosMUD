"""Unit tests for PersonalMessageSender WebSocket send guards."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from starlette.websockets import WebSocketState

from server.realtime.messaging.personal_message_sender import PersonalMessageSender


def _make_sender() -> PersonalMessageSender:
    cleanup: AsyncMock = AsyncMock()
    sender = PersonalMessageSender(
        message_queue=MagicMock(),
        cleanup_dead_websocket_callback=cleanup,
        convert_uuids_to_strings=lambda event: event,
    )
    sender.cleanup_dead_websocket = cleanup
    return sender


@pytest.mark.asyncio
async def test_send_to_websocket_skips_non_connected_client_state():
    """Half-open Firefox sockets still look CONNECTED on application_state."""
    sender = _make_sender()
    websocket: MagicMock = MagicMock()
    websocket.client_state = WebSocketState.DISCONNECTED
    websocket.application_state = WebSocketState.CONNECTED
    websocket.send_json = AsyncMock()
    delivery_status = {"websocket_delivered": 0, "websocket_failed": 0, "active_connections": 0}
    player_id = uuid.uuid4()

    sent = await sender._send_to_websocket(player_id, "conn_1", websocket, {"type": "test"}, delivery_status)

    assert sent is False
    websocket.send_json.assert_not_called()
    assert delivery_status["websocket_failed"] == 1
    sender.cleanup_dead_websocket.assert_awaited_once_with(player_id, "conn_1")


@pytest.mark.asyncio
async def test_send_to_websocket_accept_first_is_expected_close():
    """Starlette send-after-close uses 'Need to call accept first'; treat as expected close."""
    sender = _make_sender()
    websocket: MagicMock = MagicMock()
    websocket.client_state = WebSocketState.CONNECTED
    websocket.application_state = WebSocketState.CONNECTED
    websocket.send_json = AsyncMock(side_effect=RuntimeError('Need to call "accept" first.'))
    delivery_status = {"websocket_delivered": 0, "websocket_failed": 0, "active_connections": 0}
    player_id = uuid.uuid4()

    with patch("server.realtime.messaging.personal_message_sender.logger.warning") as mock_warn:
        sent = await sender._send_to_websocket(player_id, "conn_1", websocket, {"type": "test"}, delivery_status)

    assert sent is False
    assert delivery_status["websocket_failed"] == 1
    mock_warn.assert_not_called()
    sender.cleanup_dead_websocket.assert_awaited_once_with(player_id, "conn_1")
