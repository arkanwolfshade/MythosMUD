"""
Category tagging on room-movement and system events.

Each emitter here puts ``data.category`` on its payload; the client reads it to style and route the line.
These tests drive the real emitters and record what they hand to a connection manager.
"""

import asyncio
import uuid
from types import SimpleNamespace
from typing import cast

import pytest
from fastapi import WebSocket

from server.api.game import broadcast_message
from server.commands.admin_teleport_utils import broadcast_teleport_effects, notify_player_of_teleport
from server.events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from server.models.user import User
from server.realtime.connection_manager import ConnectionManager
from server.realtime.message_builders import MessageBuilder
from server.realtime.npc_event_handlers import NPCEventHandler
from server.realtime.posture_notify import emit_posture_change
from server.realtime.websocket_handler import send_system_message

PLAYER_ID = uuid.UUID("11111111-1111-1111-1111-111111111111")


class _RoomManager:
    """Room membership: everyone is in the room."""

    async def get_room_subscribers(self, _room_id: str) -> list[str]:
        return [str(PLAYER_ID)]


class _ConnectionRecorder:
    """Connection-manager surface used by the emitters under test; records every event it is asked to send."""

    def __init__(self) -> None:
        self.events: list[dict[str, object]] = []
        self.sequence_counter: int = 0
        self.room_manager: _RoomManager = _RoomManager()

    async def send_personal_message(self, _player_id: uuid.UUID, event: dict[str, object]) -> None:
        self.events.append(event)

    async def broadcast_to_room(self, _room_id: str, event: dict[str, object], exclude_player: object = None) -> None:
        _ = exclude_player  # the emitters pass it by keyword, so the name must stay
        self.events.append(event)

    async def broadcast_global_event(self, event_type: str, data: dict[str, object]) -> dict[str, object]:
        self.events.append({"event_type": event_type, "data": data})
        return {"successful_deliveries": 1}

    def get_online_player_by_display_name(self, _name: str) -> dict[str, object]:
        return {"player_id": PLAYER_ID}


class _TaskRegistry:
    """Runs registered coroutines on the current loop, as the real registry does."""

    def register_task(self, coro: object, _name: str, _task_type: str) -> None:
        _ = asyncio.ensure_future(cast("asyncio.Future[None]", coro))


class _SocketRecorder:
    """The slice of WebSocket that send_system_message uses."""

    def __init__(self) -> None:
        self.sent: list[dict[str, object]] = []

    async def send_json(self, payload: dict[str, object]) -> None:
        self.sent.append(payload)


def _as[T](_kind: type[T], fake: object) -> T:
    """View a test double as the production type the emitter is annotated with."""
    return cast(T, fake)


def _data(event: dict[str, object]) -> dict[str, object]:
    return cast(dict[str, object], event["data"])


@pytest.mark.asyncio
async def test_send_room_message_tags_every_npc_room_message_as_room_movement() -> None:
    recorder = _ConnectionRecorder()
    handler = NPCEventHandler(
        connection_manager=recorder,
        task_registry=_TaskRegistry(),
        message_builder=MessageBuilder(lambda: 1),
        send_occupants_update=None,
    )

    await handler._send_room_message(  # pyright: ignore[reportPrivateUsage]
        "room_001", "Rat left north.", message_type="system"
    )
    await handler._send_room_message("room_001", "A rat scurries in.")  # pyright: ignore[reportPrivateUsage]
    await asyncio.sleep(0)

    assert [e["event_type"] for e in recorder.events] == ["room_message", "room_message"]
    assert [_data(e)["category"] for e in recorder.events] == ["room.movement", "room.movement"]
    assert [_data(e)["message_type"] for e in recorder.events] == ["system", "npc_spawn"]


def test_player_enter_and_leave_messages_are_room_movement() -> None:
    builder = MessageBuilder(lambda: 1)
    entered = builder.create_player_entered_message(PlayerEnteredRoom(player_id="p1", room_id="room_a"), "Armitage")
    left = builder.create_player_left_message(PlayerLeftRoom(player_id="p1", room_id="room_a"), "Ward")
    assert entered["data"]["category"] == "room.movement"
    assert left["data"]["category"] == "room.movement"


@pytest.mark.asyncio
async def test_posture_change_room_event_is_room_movement() -> None:
    recorder = _ConnectionRecorder()
    _ = await emit_posture_change(
        recorder,
        player_id=uuid.uuid4(),
        display_name="Ada",
        room_id="room_a",
        previous_position="standing",
        new_position="sitting",
        send_personal_update=False,
    )
    [event] = recorder.events
    assert event["event_type"] == "player_posture_change"
    assert _data(event)["category"] == "room.movement"


@pytest.mark.asyncio
async def test_teleport_system_events_are_system_info() -> None:
    recorder = _ConnectionRecorder()
    await broadcast_teleport_effects(recorder, "Alice", "room-a", "room-b", "teleport")
    await notify_player_of_teleport(recorder, "Bob", "Admin", "teleported_to")
    assert len(recorder.events) == 3
    for event in recorder.events:
        assert event["event_type"] == "system"
        assert _data(event)["category"] == "system.info"


@pytest.mark.asyncio
async def test_admin_broadcast_event_is_system_info() -> None:
    recorder = _ConnectionRecorder()
    admin = _as(User, SimpleNamespace(id=uuid.uuid4(), username="admin"))
    _ = await broadcast_message("Hello all", admin, _as(ConnectionManager, recorder))
    [event] = recorder.events
    assert event["event_type"] == "system_broadcast"
    assert _data(event)["category"] == "system.info"


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("message_type", "category"),
    [
        ("info", "system.info"),
        ("warning", "system.warning"),
        ("error", "system.error"),
        ("unrecognised", "system.info"),
    ],
)
async def test_send_system_message_maps_message_type_to_category(message_type: str, category: str) -> None:
    socket = _SocketRecorder()
    await send_system_message(_as(WebSocket, socket), "Hello", message_type)
    [event] = socket.sent
    assert _data(event)["category"] == category
    assert _data(event)["message_type"] == message_type
