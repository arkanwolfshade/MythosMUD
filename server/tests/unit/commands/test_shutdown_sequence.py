"""Unit tests for graceful shutdown sequence execution."""

import uuid
from dataclasses import dataclass
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.commands.shutdown_sequence import (
    _cancel_background_tasks,
    _cleanup_connection_manager,
    _despawn_all_npcs,
    _disconnect_all_players,
    _disconnect_nats_service,
    _persist_all_players,
    _stop_nats_message_handler,
    execute_shutdown_sequence,
)
from server.exceptions import DatabaseError


@dataclass
class _ShutdownAppState:
    connection_manager: MagicMock | None = None
    persistence: MagicMock | None = None
    container: MagicMock | None = None
    nats_message_handler: AsyncMock | None = None
    nats_service: AsyncMock | None = None
    task_registry: MagicMock | None = None
    shutdown_data: dict[str, object] | None = None
    npc_spawning_service: MagicMock | None = None
    npc_lifecycle_manager: MagicMock | None = None


@dataclass
class _ShutdownApp:
    state: _ShutdownAppState


@pytest.mark.asyncio
async def test_execute_shutdown_sequence_happy_path():
    """execute_shutdown_sequence runs all phases and schedules termination."""
    player_id = str(uuid4())
    conn_mgr = MagicMock()
    conn_mgr.get_online_players.return_value = [{"player_id": player_id}]
    conn_mgr.force_disconnect_player = AsyncMock()
    conn_mgr.force_cleanup = AsyncMock()

    get_player = AsyncMock(return_value=MagicMock())
    save_player = AsyncMock()
    persistence = MagicMock(spec=AsyncPersistenceLayer)
    persistence.get_player_by_id = get_player
    persistence.save_player = save_player

    lifecycle = MagicMock()
    lifecycle.active_npcs = {"npc-1": object()}
    lifecycle.despawn_npc = MagicMock()

    container = MagicMock()
    container.npc_spawning_service = MagicMock()
    container.npc_lifecycle_manager = lifecycle

    nats_handler = AsyncMock()
    nats_handler.stop = AsyncMock()
    nats_service = AsyncMock()
    nats_service.disconnect = AsyncMock()

    task_registry = MagicMock()
    task_registry.unregister_task.return_value = True
    task_registry.shutdown_all = AsyncMock(return_value=True)

    app = _ShutdownApp(
        _ShutdownAppState(
            connection_manager=conn_mgr,
            persistence=persistence,
            container=container,
            nats_message_handler=nats_handler,
            nats_service=nats_service,
            task_registry=task_registry,
            shutdown_data={"task": MagicMock()},
        )
    )

    with patch("server.commands.shutdown_sequence.schedule_process_termination") as mock_schedule:
        await execute_shutdown_sequence(app)

    get_player.assert_awaited_once_with(uuid.UUID(player_id))
    save_player.assert_awaited_once()
    lifecycle.despawn_npc.assert_called_once_with("npc-1", reason="server_shutdown")
    conn_mgr.force_disconnect_player.assert_awaited_once()
    nats_handler.stop.assert_awaited_once()
    nats_service.disconnect.assert_awaited_once()
    conn_mgr.force_cleanup.assert_awaited_once()
    task_registry.shutdown_all.assert_awaited_once()
    mock_schedule.assert_called_once_with(0.3)


@pytest.mark.asyncio
async def test_persist_all_players_no_connection_manager():
    """_persist_all_players skips when connection manager is missing."""
    app = _ShutdownApp(_ShutdownAppState(connection_manager=None))
    await _persist_all_players(app)


@pytest.mark.asyncio
async def test_persist_all_players_database_error_on_player():
    """_persist_all_players logs and continues when one player fails."""
    player_id = uuid4()
    conn_mgr = MagicMock()
    conn_mgr.get_online_players.return_value = [{"player_id": player_id}]
    persistence = MagicMock(spec=AsyncPersistenceLayer)
    persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
    persistence.save_player = AsyncMock(side_effect=DatabaseError("save failed"))

    app = _ShutdownApp(_ShutdownAppState(connection_manager=conn_mgr, persistence=persistence))
    await _persist_all_players(app)


@pytest.mark.asyncio
async def test_persist_all_players_player_not_found():
    """_persist_all_players skips when player object is missing."""
    conn_mgr = MagicMock()
    conn_mgr.get_online_players.return_value = [{"player_id": uuid4()}]
    persistence = MagicMock(spec=AsyncPersistenceLayer)
    persistence.get_player_by_id = AsyncMock(return_value=None)

    app = _ShutdownApp(_ShutdownAppState(connection_manager=conn_mgr, persistence=persistence))
    await _persist_all_players(app)


@pytest.mark.asyncio
async def test_despawn_all_npcs_via_app_state_fallback():
    """_despawn_all_npcs uses app.state fallback when container is absent."""
    lifecycle = MagicMock()
    lifecycle.active_npcs = {"npc-2": object()}
    lifecycle.despawn_npc = MagicMock()

    app = _ShutdownApp(
        _ShutdownAppState(
            container=None,
            npc_spawning_service=MagicMock(),
            npc_lifecycle_manager=lifecycle,
        )
    )
    await _despawn_all_npcs(app)
    lifecycle.despawn_npc.assert_called_once()


@pytest.mark.asyncio
async def test_despawn_all_npcs_no_services():
    """_despawn_all_npcs skips when spawning service is missing."""
    app = _ShutdownApp(_ShutdownAppState(container=None, npc_spawning_service=None))
    await _despawn_all_npcs(app)


@pytest.mark.asyncio
async def test_disconnect_all_players_string_uuid():
    """_disconnect_all_players converts string player_id to UUID."""
    player_id = str(uuid4())
    conn_mgr = MagicMock()
    conn_mgr.get_online_players.return_value = [{"player_id": player_id}]
    conn_mgr.force_disconnect_player = AsyncMock()

    app = _ShutdownApp(_ShutdownAppState(connection_manager=conn_mgr))
    await _disconnect_all_players(app)
    conn_mgr.force_disconnect_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_disconnect_all_players_skips_malformed_player_id():
    """A malformed online player ID is skipped; the valid players are still disconnected."""
    valid_id = uuid4()
    force_disconnect = AsyncMock()
    conn_mgr = MagicMock()
    conn_mgr.get_online_players = MagicMock(return_value=[{"player_id": "not-a-uuid"}, {"player_id": str(valid_id)}])
    conn_mgr.force_disconnect_player = force_disconnect

    app = _ShutdownApp(_ShutdownAppState(connection_manager=conn_mgr))
    await _disconnect_all_players(app)
    force_disconnect.assert_awaited_once_with(valid_id)


@pytest.mark.asyncio
async def test_stop_nats_message_handler_missing():
    """_stop_nats_message_handler skips when handler is absent."""
    app = _ShutdownApp(_ShutdownAppState(nats_message_handler=None))
    await _stop_nats_message_handler(app)


@pytest.mark.asyncio
async def test_disconnect_nats_service_os_error():
    """_disconnect_nats_service logs OSError without raising."""
    nats_service = AsyncMock()
    nats_service.disconnect = AsyncMock(side_effect=OSError("disconnect failed"))
    app = _ShutdownApp(_ShutdownAppState(nats_service=nats_service))
    await _disconnect_nats_service(app)


@pytest.mark.asyncio
async def test_cleanup_connection_manager_missing():
    """_cleanup_connection_manager skips when connection manager is absent."""
    app = _ShutdownApp(_ShutdownAppState(connection_manager=None))
    await _cleanup_connection_manager(app)


@pytest.mark.asyncio
async def test_cancel_background_tasks_timeout():
    """_cancel_background_tasks logs warning when shutdown_all times out."""
    task_registry = MagicMock()
    task_registry.shutdown_all = AsyncMock(return_value=False)
    app = _ShutdownApp(_ShutdownAppState(task_registry=task_registry, shutdown_data=None))
    await _cancel_background_tasks(app)


@pytest.mark.asyncio
async def test_cancel_background_tasks_unregisters_shutdown_task():
    """_cancel_background_tasks unregisters shutdown countdown when present."""
    task_registry = MagicMock()
    task_registry.unregister_task.return_value = False
    task_registry.shutdown_all = AsyncMock(return_value=True)
    app = _ShutdownApp(_ShutdownAppState(task_registry=task_registry, shutdown_data={"task": MagicMock()}))
    await _cancel_background_tasks(app)
    task_registry.unregister_task.assert_called_once_with("shutdown_countdown")


@pytest.mark.asyncio
async def test_execute_shutdown_sequence_non_os_error_still_terminates():
    """A phase raising a non-OSError (e.g. AttributeError) must not skip later phases or termination."""
    force_disconnect = AsyncMock()
    force_cleanup = AsyncMock()
    conn_mgr = MagicMock()
    conn_mgr.get_online_players = MagicMock(return_value=[{"player_id": str(uuid4())}])
    conn_mgr.force_disconnect_player = force_disconnect
    conn_mgr.force_cleanup = force_cleanup
    persistence = MagicMock(spec=AsyncPersistenceLayer)
    persistence.get_player_by_id = AsyncMock(side_effect=AttributeError("boom"))
    nats_disconnect = AsyncMock()
    nats_service = MagicMock()
    nats_service.disconnect = nats_disconnect

    app = _ShutdownApp(
        _ShutdownAppState(connection_manager=conn_mgr, persistence=persistence, nats_service=nats_service)
    )
    with patch("server.commands.shutdown_sequence.schedule_process_termination") as mock_schedule:
        await execute_shutdown_sequence(app)

    force_disconnect.assert_awaited_once()
    nats_disconnect.assert_awaited_once()
    force_cleanup.assert_awaited_once()
    mock_schedule.assert_called_once_with(0.3)
