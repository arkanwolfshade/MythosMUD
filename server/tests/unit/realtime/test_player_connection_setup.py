"""Gap coverage for player_connection_setup helpers and setup paths."""

import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.exceptions import DatabaseError
from server.realtime import player_connection_setup as pcs


def _manager(**kwargs: object) -> MagicMock:
    manager = MagicMock()
    manager.async_persistence = kwargs.get("async_persistence", None)
    manager.app = kwargs.get("app", None)
    manager.broadcast_to_room = AsyncMock()
    manager.message_queue = MagicMock()
    manager.processed_disconnects = set()
    manager.processed_disconnect_lock = asyncio.Lock()
    manager.grace_period_players = {}
    manager.room_manager = MagicMock()
    manager.online_players = {}
    manager._send_initial_game_state = AsyncMock()
    for key, value in kwargs.items():
        setattr(manager, key, value)
    return manager


@pytest.mark.asyncio
async def test_update_player_last_active_no_persistence() -> None:
    await pcs._update_player_last_active(uuid.uuid4(), _manager(async_persistence=None))


@pytest.mark.asyncio
async def test_update_player_last_active_success() -> None:
    persistence = MagicMock()
    persistence.update_player_last_active = AsyncMock()
    await pcs._update_player_last_active(uuid.uuid4(), _manager(async_persistence=persistence))
    persistence.update_player_last_active.assert_awaited_once()


@pytest.mark.asyncio
async def test_update_player_last_active_database_error() -> None:
    persistence = MagicMock()
    persistence.update_player_last_active = AsyncMock(side_effect=DatabaseError("db down"))
    await pcs._update_player_last_active(uuid.uuid4(), _manager(async_persistence=persistence))


def test_stable_room_id_strips_instance_prefix() -> None:
    room_uuid = uuid.uuid4()
    assert pcs._stable_room_id_for_quest(f"instance_{room_uuid}_earth_arkham_1") == "earth_arkham_1"
    assert pcs._stable_room_id_for_quest("earth_arkham_1") == "earth_arkham_1"


@pytest.mark.asyncio
async def test_trigger_quests_no_service() -> None:
    await pcs._trigger_quests_for_room_on_spawn(uuid.uuid4(), "room_1", _manager(app=None))


@pytest.mark.asyncio
async def test_trigger_quests_success_and_failure() -> None:
    quest = MagicMock()
    quest.start_quest_by_trigger = AsyncMock()
    container = MagicMock()
    container.quest_service = quest
    app = MagicMock()
    app.state.container = container
    player_id = uuid.uuid4()
    await pcs._trigger_quests_for_room_on_spawn(player_id, "room_1", _manager(app=app))
    quest.start_quest_by_trigger.assert_awaited_once_with(player_id, "room", "room_1")

    quest.start_quest_by_trigger = AsyncMock(side_effect=RuntimeError("quest boom"))
    await pcs._trigger_quests_for_room_on_spawn(player_id, "room_1", _manager(app=app))


@pytest.mark.asyncio
async def test_add_player_to_room_silently_paths() -> None:
    await pcs._add_player_to_room_silently(uuid.uuid4(), "room_1", _manager(async_persistence=None))

    persistence = MagicMock()
    persistence.get_room_by_id.return_value = None
    await pcs._add_player_to_room_silently(uuid.uuid4(), "room_1", _manager(async_persistence=persistence))

    room = MagicMock()
    room.has_player.return_value = False
    persistence.get_room_by_id.return_value = room
    player_id = uuid.uuid4()
    await pcs._add_player_to_room_silently(player_id, "room_1", _manager(async_persistence=persistence))
    room.add_player_silently.assert_called_once_with(player_id)


@pytest.mark.asyncio
async def test_broadcast_player_entered_game_success_and_error() -> None:
    manager = _manager()
    player = MagicMock()
    player_id = uuid.uuid4()
    with patch("server.realtime.player_connection_setup.extract_player_name", return_value="Ada"):
        await pcs._broadcast_player_entered_game(player_id, player, "room_1", manager)
    manager.broadcast_to_room.assert_awaited_once()

    manager.broadcast_to_room = AsyncMock(side_effect=DatabaseError("broadcast fail"))
    with patch("server.realtime.player_connection_setup.extract_player_name", return_value="Ada"):
        await pcs._broadcast_player_entered_game(player_id, player, "room_1", manager)


@pytest.mark.asyncio
async def test_send_room_occupants_update_paths() -> None:
    await pcs._send_room_occupants_update_after_connection(uuid.uuid4(), "room_1", _manager(app=None))

    handler = MagicMock()
    handler.send_room_occupants_update = AsyncMock()
    container = MagicMock()
    container.real_time_event_handler = handler
    app = MagicMock()
    app.state.container = container
    player_id = uuid.uuid4()
    await pcs._send_room_occupants_update_after_connection(player_id, "room_1", _manager(app=app))
    handler.send_room_occupants_update.assert_awaited_once()

    handler.send_room_occupants_update = AsyncMock(side_effect=DatabaseError("occupants fail"))
    await pcs._send_room_occupants_update_after_connection(player_id, "room_1", _manager(app=app))


@pytest.mark.asyncio
async def test_handle_new_connection_setup_room_none_early_return() -> None:
    manager = _manager()
    with patch("server.services.combat_service.get_combat_service", return_value=None):
        await pcs.handle_new_connection_setup(uuid.uuid4(), MagicMock(), None, manager)
    manager._send_initial_game_state.assert_not_awaited()


@pytest.mark.asyncio
async def test_handle_new_connection_setup_ends_combat_on_login() -> None:
    manager = _manager(async_persistence=None)
    player_id = uuid.uuid4()
    combat = MagicMock()
    combat.combat_id = uuid.uuid4()
    combat_service = MagicMock()
    combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    combat_service.end_combat = AsyncMock()

    with (
        patch("server.services.combat_service.get_combat_service", return_value=combat_service),
        patch("server.realtime.player_connection_setup.start_login_grace_period", new_callable=AsyncMock),
        patch("server.realtime.player_connection_setup._broadcast_player_entered_game", new_callable=AsyncMock),
        patch(
            "server.realtime.player_connection_setup._send_room_occupants_update_after_connection",
            new_callable=AsyncMock,
        ),
        patch("server.realtime.player_connection_setup._add_player_to_room_silently", new_callable=AsyncMock),
        patch("server.realtime.player_connection_setup._trigger_quests_for_room_on_spawn", new_callable=AsyncMock),
        patch("server.realtime.player_connection_setup._update_player_last_active", new_callable=AsyncMock),
    ):
        await pcs.handle_new_connection_setup(player_id, MagicMock(), "room_1", manager)

    combat_service.end_combat.assert_awaited_once()
    manager.room_manager.add_room_occupant.assert_called_once()
    manager._send_initial_game_state.assert_awaited_once()
