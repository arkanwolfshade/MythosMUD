"""Tests for NATS EventHandler combat-related broadcasts (WebSocket shape)."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.event_handlers import (
    EventHandler,
    _as_event_data_dict,
    _npc_died_ids_or_warn,
    _participant_key_strings,
    _send_combat_participant_updates,
)


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


def test_as_event_data_dict_normalizes_mapping() -> None:
    assert _as_event_data_dict({"room_id": "room-a"}) == {"room_id": "room-a"}
    assert _as_event_data_dict("bad") == {}


def test_participant_key_strings() -> None:
    assert _participant_key_strings({"p1": {}, "p2": {}}) == ["p1", "p2"]
    assert _participant_key_strings(None) == []


def test_validate_event_message() -> None:
    handler = EventHandler(connection_manager=MagicMock())
    assert handler.validate_event_message("player_entered", {"room_id": "r1"}) is True
    assert handler.validate_event_message(None, {"room_id": "r1"}) is False


@pytest.mark.asyncio
async def test_handle_event_message_dispatches_handler() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_event_message(
        {"event_type": "player_entered", "event_data": {"room_id": "room-a", "player_id": "p1"}}
    )
    cm.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_event_message_invalid_skips() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_event_message({"event_type": None, "event_data": {}})
    cm.broadcast_room_event.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_combat_started_event() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    cm.get_player = AsyncMock(return_value=MagicMock())
    cm.send_personal_message = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    player_id = str(uuid.uuid4())
    await handler.handle_combat_started_event({"room_id": "room-a", "participants": {player_id: {"name": "Armitage"}}})
    cm.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_send_combat_participant_updates() -> None:
    cm = MagicMock()
    cm.get_player = AsyncMock(return_value=MagicMock())
    cm.send_personal_message = AsyncMock()
    player_id = str(uuid.uuid4())
    await _send_combat_participant_updates(cm, {player_id: {}}, in_combat=True)
    cm.send_personal_message.assert_awaited_once()


def test_npc_died_ids_or_warn_missing_fields() -> None:
    assert _npc_died_ids_or_warn({}) is None


@pytest.mark.asyncio
async def test_handle_npc_died_event() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    cm.event_bus = MagicMock()
    cm.refresh_room_occupants = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_npc_died_event(
        {
            "room_id": "room-a",
            "npc_id": "npc-1",
            "npc_name": "Shoggoth",
        }
    )
    cm.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_left_event() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_player_left_event({"room_id": "room-a", "player_id": "p1"})
    cm.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_game_tick_event() -> None:
    cm = MagicMock()
    cm.broadcast_global_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_game_tick_event({"tick_number": 42})
    cm.broadcast_global_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_combat_ended_event() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    cm.get_player = AsyncMock(return_value=None)
    handler = EventHandler(connection_manager=cm)
    await handler.handle_combat_ended_event({"room_id": "room-a", "participants": {}})
    cm.broadcast_room_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_entered_missing_room_id() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_player_entered_event({"player_id": "p1"})
    cm.broadcast_room_event.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_npc_attacked_event() -> None:
    cm = MagicMock()
    cm.broadcast_room_event = AsyncMock()
    handler = EventHandler(connection_manager=cm)
    await handler.handle_npc_attacked_event({"room_id": "room-a", "npc_id": "npc-1"})
    cm.broadcast_room_event.assert_awaited_once()
