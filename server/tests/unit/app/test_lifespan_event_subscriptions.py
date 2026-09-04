"""Unit tests for lifespan event subscription producers."""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.lifespan_event_subscriptions import subscribe_quest_events, subscribe_room_occupants_refresh
from server.events.event_types import QuestCompleted, RoomOccupantsRefreshRequested
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
    await handlers[0](QuestCompleted(player_id=player_id, quest_id="quest-1"))

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

    await handlers[0](QuestCompleted(player_id="not-a-uuid", quest_id="quest-1"))
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
    await handlers[0](QuestCompleted(player_id=player_id, quest_id="quest-1"))
    container.connection_manager.send_personal_message.assert_not_called()
