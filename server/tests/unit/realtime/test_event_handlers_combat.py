"""Tests for NATS EventHandler combat-related broadcasts (WebSocket shape)."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.event_handlers import EventHandler


@pytest.mark.asyncio
async def test_handle_npc_took_damage_flattens_event_data_for_websocket() -> None:
    """NATS uses EventMessageSchema; clients expect flat npc_id, current_dp in event.data."""
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)

    nats_message = {
        "room_id": "room_a",
        "event_data": {
            "room_id": "room_a",
            "npc_id": "uuid-here",
            "npc_name": "Nightgaunt",
            "damage": 25,
            "current_dp": 55,
            "max_dp": 80,
        },
    }

    await handler.handle_npc_took_damage_event(nats_message)

    cm.broadcast_room_event.assert_awaited_once()
    _event_type, room_id, payload = cm.broadcast_room_event.await_args[0]
    assert _event_type == "npc_took_damage"
    assert room_id == "room_a"
    assert payload["npc_name"] == "Nightgaunt"
    assert payload["current_dp"] == 55
    assert payload["damage"] == 25
