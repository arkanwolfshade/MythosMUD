"""NPC movement / appear / leave lines carry the NPC's name as a styled segment (#1025)."""

# pyright: reportAny=false, reportPrivateUsage=false
# The handler is exercised through MagicMock/AsyncMock doubles for the connection manager and its own private
# helpers; attribute access on those doubles is Any by construction.

from unittest.mock import AsyncMock, MagicMock, call, patch

import pytest

from server.constants.npc_disposition import NpcDisposition
from server.events.event_types import NPCEnteredRoom, NPCLeftRoom
from server.realtime.message_builders import MessageBuilder
from server.realtime.npc_event_handlers import NPCEventHandler

ROOM = "room_001"


@pytest.fixture
def handler() -> NPCEventHandler:
    cm = MagicMock()
    cm.async_persistence.get_room_by_id.return_value = MagicMock()
    h = NPCEventHandler(
        connection_manager=cm,
        task_registry=None,
        message_builder=MessageBuilder(lambda: 1),
        send_occupants_update=AsyncMock(),
    )
    return h


def _named(handler: NPCEventHandler, name: str, disposition: NpcDisposition):
    return (
        patch.object(handler, "_get_npc_name", return_value=name),
        patch(
            "server.realtime.npc_event_handlers.get_npc_disposition_from_instance",
            return_value=disposition,
        ),
        patch.object(handler, "_determine_direction_from_rooms", AsyncMock(return_value="north")),
        patch.object(handler, "_schedule_room_occupants_update"),
    )


@pytest.mark.asyncio
async def test_movement_into_the_room_styles_the_name_by_disposition(handler: NPCEventHandler) -> None:
    patches = _named(handler, "Rat", NpcDisposition.AGGRESSIVE_MOB)
    with patches[0], patches[1], patches[2], patches[3], patch.object(handler, "_send_room_message") as send:
        await handler.handle_npc_entered(NPCEnteredRoom(npc_id="npc_1", room_id=ROOM, from_room_id="room_000"))
    assert send.await_args == call(
        ROOM,
        "Rat entered from north.",
        "system",
        segments=[
            {"text": "Rat", "category": "npc.aggressive_mob"},
            {"text": " entered from north."},
        ],
    )


@pytest.mark.asyncio
async def test_movement_out_of_the_room_styles_the_name_by_disposition(handler: NPCEventHandler) -> None:
    patches = _named(handler, "Merchant", NpcDisposition.SHOPKEEPER)
    with patches[0], patches[1], patches[2], patches[3], patch.object(handler, "_send_room_message") as send:
        await handler.handle_npc_left(NPCLeftRoom(npc_id="npc_1", room_id=ROOM, to_room_id="room_002"))
    assert send.await_args == call(
        ROOM,
        "Merchant left north.",
        "system",
        segments=[
            {"text": "Merchant", "category": "npc.shopkeeper"},
            {"text": " left north."},
        ],
    )


@pytest.mark.asyncio
async def test_default_spawn_line_styles_the_name(handler: NPCEventHandler) -> None:
    patches = _named(handler, "Elder", NpcDisposition.QUEST_GIVER)
    with (
        patches[0],
        patches[1],
        patches[3],
        patch.object(handler, "_get_npc_spawn_message", return_value="Elder appears."),
        patch.object(handler, "_send_room_message") as send,
    ):
        await handler.handle_npc_entered(NPCEnteredRoom(npc_id="npc_1", room_id=ROOM))
    assert send.await_args == call(
        ROOM,
        "Elder appears.",
        "npc_spawn",
        segments=[{"text": "Elder", "category": "npc.quest_giver"}, {"text": " appears."}],
    )


@pytest.mark.asyncio
async def test_authored_spawn_text_stays_plain(handler: NPCEventHandler) -> None:
    """Authored behavior_config text has no name placeholder, so it is never guessed at and never styled."""
    patches = _named(handler, "Elder", NpcDisposition.QUEST_GIVER)
    with (
        patches[0],
        patches[1],
        patches[3],
        patch.object(handler, "_get_npc_spawn_message", return_value="A hooded figure shuffles in from the fog."),
        patch.object(handler, "_send_room_message") as send,
    ):
        await handler.handle_npc_entered(NPCEnteredRoom(npc_id="npc_1", room_id=ROOM))
    assert send.await_args == call(ROOM, "A hooded figure shuffles in from the fog.", "npc_spawn", segments=None)


@pytest.mark.asyncio
async def test_default_departure_line_styles_the_name_and_authored_text_does_not(handler: NPCEventHandler) -> None:
    patches = _named(handler, "Pigeon", NpcDisposition.PASSIVE_MOB)
    with (
        patches[0],
        patches[1],
        patches[3],
        patch.object(handler, "_get_npc_departure_message", return_value="Pigeon leaves."),
        patch.object(handler, "_send_room_message") as send,
    ):
        await handler.handle_npc_left(NPCLeftRoom(npc_id="npc_1", room_id=ROOM))
    assert send.await_args == call(
        ROOM,
        "Pigeon leaves.",
        "npc_spawn",
        segments=[{"text": "Pigeon", "category": "npc.passive_mob"}, {"text": " leaves."}],
    )

    patches = _named(handler, "Pigeon", NpcDisposition.PASSIVE_MOB)
    with (
        patches[0],
        patches[1],
        patches[3],
        patch.object(handler, "_get_npc_departure_message", return_value="The pigeon takes wing."),
        patch.object(handler, "_send_room_message") as send,
    ):
        await handler.handle_npc_left(NPCLeftRoom(npc_id="npc_1", room_id=ROOM))
    assert send.await_args == call(ROOM, "The pigeon takes wing.", "npc_spawn", segments=None)


def test_movement_message_text_is_unchanged_by_the_parts_refactor() -> None:
    """create_npc_movement_message still returns the plain line every existing caller expects."""
    builder = MessageBuilder(lambda: 1)
    assert builder.create_npc_movement_message("Rat", "north", "left") == "Rat left north."
    assert builder.create_npc_movement_message("Rat", None, "left") == "Rat left the room."
    assert builder.create_npc_movement_message("Rat", "south", "entered") == "Rat entered from south."
    assert builder.create_npc_movement_message("Rat", None, "entered") == "Rat entered the room."
    assert builder.create_npc_movement_message("Rat", None, "teleport") == "Rat moved."
