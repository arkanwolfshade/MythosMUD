"""Unit tests for lifespan event subscription producers."""

# pyright: reportAny=false
# Reason: unittest.mock.MagicMock/AsyncMock inherit Any in typeshed (NonCallableMock(Base, Any)); these tests
# drive the code through mocked sessions, services and connection managers, so mock attribute access is Any.

import asyncio
import uuid
from collections.abc import Awaitable, Callable
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.lifespan_event_subscriptions import subscribe_quest_events, subscribe_room_occupants_refresh
from server.events.event_types import NPCOpensDialogue, QuestLogChanged, RoomOccupantsRefreshRequested
from server.tests.unit.realtime.envelope_assertions import assert_event_envelope


@pytest.mark.asyncio
async def test_quest_log_updated_event_envelope_shape():
    """quest_log_updated producer emits a build_event-shaped envelope with player_id."""
    handlers: list = []
    event_bus = MagicMock()
    event_bus.subscribe = lambda event_type, handler, service_id=None: handlers.append(handler)

    conn_mgr = MagicMock()
    conn_mgr.send_personal_message = AsyncMock()
    quest_service = MagicMock()
    quest_service.get_quest_log = AsyncMock(return_value=[])

    container = MagicMock()
    container.event_bus = event_bus
    container.quest_service = quest_service
    container.connection_manager = conn_mgr

    with patch("server.game.quest.quest_events.subscribe_quest_events"):
        subscribe_quest_events(container)

    assert len(handlers) == 1
    player_id = str(uuid.uuid4())
    await handlers[0](QuestLogChanged(player_id=player_id))

    conn_mgr.send_personal_message.assert_awaited_once()
    event = conn_mgr.send_personal_message.await_args.args[1]
    assert_event_envelope(event, event_type="quest_log_updated", require_player_id=True)


def test_subscribe_room_occupants_refresh_skips_without_event_bus() -> None:
    container = MagicMock()
    container.event_bus = None
    container.connection_manager = MagicMock()
    subscribe_room_occupants_refresh(container)


@pytest.mark.asyncio
async def test_subscribe_room_occupants_refresh_broadcasts_on_event() -> None:
    handlers: list = []
    event_bus = MagicMock()
    event_bus.subscribe = lambda event_type, handler, service_id=None: handlers.append(handler)
    conn_mgr = MagicMock()
    container = MagicMock()
    container.event_bus = event_bus
    container.connection_manager = conn_mgr

    with patch(
        "server.realtime.websocket_room_updates.broadcast_room_update",
        new_callable=AsyncMock,
    ) as broadcast:
        subscribe_room_occupants_refresh(container)
        assert len(handlers) == 1
        handlers[0](RoomOccupantsRefreshRequested(room_id="room-1"))
        await asyncio.sleep(0)
        broadcast.assert_awaited_once_with("room-1", "room-1", connection_manager=conn_mgr)


def test_room_occupants_refresh_no_running_loop_returns_silently() -> None:
    handlers: list = []
    event_bus = MagicMock()
    event_bus.subscribe = lambda event_type, handler, service_id=None: handlers.append(handler)
    container = MagicMock()
    container.event_bus = event_bus
    container.connection_manager = MagicMock()
    subscribe_room_occupants_refresh(container)
    handlers[0](RoomOccupantsRefreshRequested(room_id="room-1"))


@pytest.mark.asyncio
async def test_quest_completed_invalid_player_id_logs_warning() -> None:
    handlers: list = []
    event_bus = MagicMock()
    event_bus.subscribe = lambda event_type, handler, service_id=None: handlers.append(handler)
    container = MagicMock()
    container.event_bus = event_bus
    container.quest_service = MagicMock()
    container.connection_manager = MagicMock()

    with patch("server.game.quest.quest_events.subscribe_quest_events"):
        subscribe_quest_events(container)

    await handlers[0](QuestLogChanged(player_id="not-a-uuid"))
    container.connection_manager.send_personal_message.assert_not_called()


@pytest.mark.asyncio
async def test_quest_completed_missing_services_skips_push() -> None:
    handlers: list = []
    event_bus = MagicMock()
    event_bus.subscribe = lambda event_type, handler, service_id=None: handlers.append(handler)
    container = MagicMock()
    container.event_bus = event_bus
    container.quest_service = None
    container.connection_manager = MagicMock()

    with patch("server.game.quest.quest_events.subscribe_quest_events"):
        subscribe_quest_events(container)

    player_id = str(uuid.uuid4())
    await handlers[0](QuestLogChanged(player_id=player_id))
    container.connection_manager.send_personal_message.assert_not_called()


_DialogueHandler = Callable[[NPCOpensDialogue], Awaitable[None]]


def _npc_dialogue_handler(container: MagicMock) -> _DialogueHandler:
    """Subscribe the NPC-dialogue opener on ``container`` and return its handler."""
    from server.app.lifespan_event_subscriptions import subscribe_npc_dialogue_events

    handlers: list[_DialogueHandler] = []

    def _subscribe(_event_type: object, handler: _DialogueHandler, service_id: str | None = None) -> None:
        _ = service_id
        handlers.append(handler)

    container.event_bus.subscribe = _subscribe
    subscribe_npc_dialogue_events(container)
    [handler] = handlers
    return handler


def _opens(player_id: uuid.UUID) -> NPCOpensDialogue:
    return NPCOpensDialogue(npc_id="ghoul-1", npc_name="Pale Ghoul", room_id="yew", player_id=str(player_id))


@pytest.mark.asyncio
async def test_an_npc_that_speaks_first_opens_its_dialogue_with_the_entering_player() -> None:
    player_id = uuid.uuid4()
    container = MagicMock()
    container.async_persistence.get_player_by_id = AsyncMock(return_value=MagicMock(current_room_id="yew"))
    handler = _npc_dialogue_handler(container)
    npc = MagicMock()
    npc.definition.id = 7

    with (
        patch("server.commands.quest_commands.npc_instance_in_room", return_value=npc),
        patch("server.game.dialogue.get_dialogue_service") as service,
        patch("server.commands.talk_command.open_dialogue", new_callable=AsyncMock) as open_dialogue,
    ):
        service.return_value.get_cursor.return_value = None
        await handler(_opens(player_id))

    open_dialogue.assert_awaited_once()
    call = open_dialogue.await_args
    assert call is not None
    assert call.args == (player_id,)
    assert call.kwargs["definition_id"] == 7
    assert call.kwargs["npc_name"] == "Pale Ghoul"


@pytest.mark.asyncio
async def test_re_entering_mid_conversation_does_not_restart_it() -> None:
    container = MagicMock()
    handler = _npc_dialogue_handler(container)
    npc = MagicMock()
    npc.definition.id = 7

    with (
        patch("server.commands.quest_commands.npc_instance_in_room", return_value=npc),
        patch("server.game.dialogue.get_dialogue_service") as service,
        patch("server.commands.talk_command.open_dialogue", new_callable=AsyncMock) as open_dialogue,
    ):
        service.return_value.get_cursor.return_value = MagicMock(npc_id="ghoul-1")
        await handler(_opens(uuid.uuid4()))

    open_dialogue.assert_not_awaited()


@pytest.mark.asyncio
async def test_a_player_who_already_moved_on_is_not_spoken_to() -> None:
    container = MagicMock()
    container.async_persistence.get_player_by_id = AsyncMock(return_value=MagicMock(current_room_id="elsewhere"))
    handler = _npc_dialogue_handler(container)
    npc = MagicMock()
    npc.definition.id = 7

    with (
        patch("server.commands.quest_commands.npc_instance_in_room", return_value=npc),
        patch("server.game.dialogue.get_dialogue_service") as service,
        patch("server.commands.talk_command.open_dialogue", new_callable=AsyncMock) as open_dialogue,
    ):
        service.return_value.get_cursor.return_value = None
        await handler(_opens(uuid.uuid4()))

    open_dialogue.assert_not_awaited()
