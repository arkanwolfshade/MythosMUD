"""Unit tests for PersonalMessageSender."""

import logging
import uuid
from collections import deque
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocketDisconnect

from server.exceptions import DatabaseError
from server.realtime.messaging.personal_message_sender import PersonalMessageSender


@pytest.fixture
def sender() -> PersonalMessageSender:
    queue = MagicMock()
    queue.pending_messages = {}
    queue.max_messages_per_player = 50
    return PersonalMessageSender(
        message_queue=queue,
        cleanup_dead_websocket_callback=AsyncMock(),
        convert_uuids_to_strings=lambda x: x,
    )


@pytest.mark.asyncio
async def test_send_message_delivers_via_websocket(sender: PersonalMessageSender) -> None:
    player_id = uuid.uuid4()
    websocket = MagicMock()
    websocket.send_json = AsyncMock()
    websocket.application_state = MagicMock()
    with patch("server.realtime.payload_optimizer.get_payload_optimizer") as opt:
        opt.return_value.optimize_payload.side_effect = lambda x: x
        status = await sender.send_message(
            player_id,
            {"event_type": "chat", "message": "hi"},
            {player_id: ["conn-1"]},
            {"conn-1": websocket},
        )
    assert status["success"] is True
    assert status["websocket_delivered"] == 1


@pytest.mark.asyncio
async def test_send_message_queues_when_offline(sender: PersonalMessageSender) -> None:
    player_id = uuid.uuid4()
    with patch("server.realtime.payload_optimizer.get_payload_optimizer") as opt:
        opt.return_value.optimize_payload.side_effect = lambda x: x
        status = await sender.send_message(player_id, {"event_type": "chat"}, {}, {})
    assert status["success"] is True
    assert str(player_id) in sender.message_queue.pending_messages


@pytest.mark.asyncio
async def test_prepare_payload_too_large(sender: PersonalMessageSender) -> None:
    player_id = uuid.uuid4()
    with patch("server.realtime.payload_optimizer.get_payload_optimizer") as opt:
        opt.return_value.max_payload_size = 100
        opt.return_value.optimize_payload.side_effect = ValueError("too big")
        payload = sender._prepare_payload(player_id, {"event_type": "chat", "data": "x"})
    assert payload["error_type"] == "payload_too_large"


@pytest.mark.asyncio
async def test_send_to_websocket_disconnect(sender: PersonalMessageSender) -> None:
    player_id = uuid.uuid4()
    websocket = MagicMock()
    websocket.application_state = MagicMock()
    websocket.send_json = AsyncMock(side_effect=WebSocketDisconnect())
    delivery_status = {"websocket_failed": 0, "websocket_delivered": 0, "active_connections": 0}
    ok = await sender._send_to_websocket(player_id, "conn-1", websocket, {"type": "chat"}, delivery_status)
    assert ok is False
    assert delivery_status["websocket_failed"] == 1


@pytest.mark.asyncio
async def test_send_to_websocket_accept_first_is_debug_not_warning(
    sender: PersonalMessageSender, caplog: pytest.LogCaptureFixture
) -> None:
    """E2E teardown: send after client drop must not warn."""
    player_id = uuid.uuid4()
    websocket = MagicMock()
    websocket.application_state = MagicMock()
    websocket.send_json = AsyncMock(
        side_effect=RuntimeError('WebSocket is not connected. Need to call "accept" first.')
    )
    delivery_status = {"websocket_failed": 0, "websocket_delivered": 0, "active_connections": 0}
    with caplog.at_level(logging.WARNING, logger="server.realtime.messaging.personal_message_sender"):
        ok = await sender._send_to_websocket(player_id, "conn-1", websocket, {"type": "chat"}, delivery_status)
    assert ok is False
    assert not any("WebSocket send failed" in r.message for r in caplog.records)


@pytest.mark.asyncio
async def test_send_to_websocket_empty_runtime_error_is_debug(
    sender: PersonalMessageSender, caplog: pytest.LogCaptureFixture
) -> None:
    player_id = uuid.uuid4()
    websocket = MagicMock()
    websocket.application_state = MagicMock()
    websocket.send_json = AsyncMock(side_effect=RuntimeError(""))
    delivery_status = {"websocket_failed": 0, "websocket_delivered": 0, "active_connections": 0}
    with caplog.at_level(logging.WARNING, logger="server.realtime.messaging.personal_message_sender"):
        ok = await sender._send_to_websocket(player_id, "conn-1", websocket, {"type": "chat"}, delivery_status)
    assert ok is False
    assert not any("WebSocket send failed" in r.message for r in caplog.records)


def test_get_delivery_stats(sender: PersonalMessageSender) -> None:
    player_id = uuid.uuid4()
    sender.message_queue.pending_messages[str(player_id)] = deque([{"event_type": "chat"}])
    stats = sender.get_delivery_stats(player_id, {player_id: ["conn-1"]})
    assert stats["pending_messages"] == 1
    assert stats["has_active_connections"] is True


@pytest.mark.asyncio
async def test_send_message_outer_exception(sender: PersonalMessageSender) -> None:
    player_id = uuid.uuid4()
    with patch.object(sender, "_prepare_payload", side_effect=DatabaseError("db")):
        status = await sender.send_message(player_id, {}, {}, {})
    assert status["success"] is False
