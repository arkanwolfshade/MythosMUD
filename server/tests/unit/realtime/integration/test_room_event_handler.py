"""Unit tests for RoomEventHandler integration."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.integration.room_event_handler import RoomEventHandler


@pytest.fixture
def room_handler() -> RoomEventHandler:
    room_manager = MagicMock()
    room_manager.get_room_occupants = AsyncMock(return_value=[{"player_name": "Armitage"}])
    event_bus = MagicMock()
    event_publisher = MagicMock()
    event_publisher.publish_player_entered_event = AsyncMock()
    event_publisher.publish_player_left_event = AsyncMock()
    broadcast = AsyncMock(return_value={"success": True})
    player_id = uuid.uuid4()
    return RoomEventHandler(
        room_manager=room_manager,
        get_event_bus=lambda: event_bus,
        get_event_publisher=lambda: event_publisher,
        broadcast_to_room_callback=broadcast,
        get_online_players=lambda: {player_id: {"name": "Armitage"}},
    )


@pytest.mark.asyncio
async def test_subscribe_to_events(room_handler: RoomEventHandler) -> None:
    event_bus = room_handler.get_event_bus()
    await room_handler.subscribe_to_events()
    assert event_bus.subscribe.call_count == 2


@pytest.mark.asyncio
async def test_subscribe_to_events_no_bus() -> None:
    handler = RoomEventHandler(
        room_manager=MagicMock(),
        get_event_bus=lambda: None,
        get_event_publisher=lambda: None,
        broadcast_to_room_callback=AsyncMock(),
        get_online_players=lambda: {},
    )
    await handler.subscribe_to_events()


@pytest.mark.asyncio
async def test_unsubscribe_from_events(room_handler: RoomEventHandler) -> None:
    event_bus = room_handler.get_event_bus()
    await room_handler.unsubscribe_from_events()
    assert event_bus.unsubscribe.call_count == 2


@pytest.mark.asyncio
async def test_handle_player_entered_room_broadcasts(room_handler: RoomEventHandler) -> None:
    player_id = uuid.uuid4()
    await room_handler.handle_player_entered_room({"room_id": "room-001", "player_id": str(player_id)})
    room_handler.broadcast_to_room.assert_awaited_once()
    call_args = room_handler.broadcast_to_room.await_args
    assert call_args.args[0] == "room-001"
    assert call_args.args[1]["event_type"] == "room_occupants"


@pytest.mark.asyncio
async def test_handle_player_entered_room_missing_room_id(room_handler: RoomEventHandler) -> None:
    await room_handler.handle_player_entered_room({"player_id": "p1"})
    room_handler.broadcast_to_room.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_player_entered_skips_uuid_player_names(room_handler: RoomEventHandler) -> None:
    uuid_name = str(uuid.uuid4())
    room_handler.room_manager.get_room_occupants = AsyncMock(return_value=[{"player_name": uuid_name}])
    await room_handler.handle_player_entered_room({"room_id": "room-001", "player_id": uuid_name})
    event = room_handler.broadcast_to_room.await_args.args[1]
    assert event["data"]["occupants"] == []
    assert event["data"]["count"] == 0


@pytest.mark.asyncio
async def test_handle_player_left_room_broadcasts(room_handler: RoomEventHandler) -> None:
    player_id = uuid.uuid4()
    await room_handler.handle_player_left_room({"room_id": "room-002", "player_id": str(player_id)})
    room_handler.broadcast_to_room.assert_awaited_once()
    publisher = room_handler.get_event_publisher()
    publisher.publish_player_left_event.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_player_entered_nats_publish_failure(room_handler: RoomEventHandler) -> None:
    publisher = room_handler.get_event_publisher()
    publisher.publish_player_entered_event = AsyncMock(side_effect=RuntimeError("nats down"))
    await room_handler.handle_player_entered_room({"room_id": "room-001", "player_id": "p1"})
    room_handler.broadcast_to_room.assert_awaited_once()


@pytest.mark.asyncio
async def test_subscribe_handles_exception() -> None:
    event_bus = MagicMock()
    event_bus.subscribe.side_effect = RuntimeError("subscribe fail")
    handler = RoomEventHandler(
        room_manager=MagicMock(),
        get_event_bus=lambda: event_bus,
        get_event_publisher=lambda: None,
        broadcast_to_room_callback=AsyncMock(),
        get_online_players=lambda: {},
    )
    with patch("server.realtime.integration.room_event_handler.logger"):
        await handler.subscribe_to_events()
