"""
Unit tests for game tick processing functions.

Tests the game tick processing logic including status effects, combat, and maintenance tasks.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.game_tick_processing import (
    _log_cleanup_results,
    _process_all_status_effects,
    _process_damage_over_time_effect,
    _process_heal_over_time_effect,
    _process_single_effect,
    _update_player_status_effects,
    _validate_and_get_player,
    _validate_app_state_for_status_effects,
    _validate_mp_regeneration_services,
    cleanup_decayed_corpses,
    get_current_tick,
    get_tick_interval,
    process_casting_progress,
    process_combat_tick,
    process_npc_maintenance,
    process_status_effects,
    reset_current_tick,
)


def test_get_current_tick():
    """Test get_current_tick returns the current tick value."""
    # Reset to known state
    reset_current_tick()
    assert get_current_tick() == 0


def test_reset_current_tick():
    """Test reset_current_tick resets the tick counter."""
    # Set tick to non-zero (we can't directly set it, but we can test reset)
    reset_current_tick()
    initial = get_current_tick()
    assert initial == 0

    # Reset again should still be 0
    reset_current_tick()
    assert get_current_tick() == 0


def test_get_tick_interval():
    """Test get_tick_interval returns tick interval from config."""
    with patch("server.app.game_tick_processing.get_config") as mock_config:
        mock_config_instance = MagicMock()
        mock_config_instance.game.server_tick_rate = 0.5
        mock_config.return_value = mock_config_instance

        interval = get_tick_interval()
        assert interval == 0.5


def test_validate_app_state_for_status_effects_no_container():
    """Test _validate_app_state_for_status_effects returns False when no container."""
    app = FastAPI()
    app.state = MagicMock()
    del app.state.container  # Remove container attribute

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_no_async_persistence():
    """Test _validate_app_state_for_status_effects returns False when no async_persistence."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_no_connection_manager():
    """Test _validate_app_state_for_status_effects returns False when no connection_manager."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = None  # Set connection_manager to None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_valid():
    """Test _validate_app_state_for_status_effects returns True when all required components exist."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = MagicMock()
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is True
    assert container == mock_container


def test_validate_app_state_for_status_effects_container_is_none():
    """Test _validate_app_state_for_status_effects returns False when container is None."""
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = None

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_connection_manager_is_none():
    """Test _validate_app_state_for_status_effects returns False when connection_manager is None."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = None  # Set connection_manager to None in container
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_mp_regeneration_services() -> None:
    container = MagicMock()
    container.mp_regeneration_service = MagicMock()
    container.connection_manager = MagicMock()
    assert _validate_mp_regeneration_services(container) is True
    container.mp_regeneration_service = None
    assert _validate_mp_regeneration_services(container) is False


def test_log_cleanup_results() -> None:
    _log_cleanup_results(tick_count=60, cleaned_count=2, total_decayed=3)


@pytest.mark.asyncio
async def test_process_heal_over_time_effect() -> None:
    container = MagicMock()
    container.async_persistence = AsyncMock()
    player = MagicMock()
    effect = {"type": "heal_over_time", "healing": 5, "duration": 2, "remaining": 2}
    applied = await _process_heal_over_time_effect(container, player, effect, 1, "player-1")
    assert applied is True
    container.async_persistence.heal_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_damage_over_time_zero_remaining() -> None:
    app = FastAPI()
    container = MagicMock()
    player = MagicMock()
    effect = {"type": "damage_over_time", "damage": 3}
    applied = await _process_damage_over_time_effect(app, container, player, effect, 0, "player-1")
    assert applied is False


@pytest.mark.asyncio
async def test_process_single_effect_heal_expires() -> None:
    app = FastAPI()
    container = MagicMock()
    container.async_persistence = AsyncMock()
    player = MagicMock()
    effect = {"type": "heal_over_time", "healing": 2, "duration": 2, "remaining": 2}
    updated, applied = await _process_single_effect(app, container, player, effect, "p1")
    assert updated is not None
    assert updated["remaining"] == 1
    assert applied is True


@pytest.mark.asyncio
async def test_validate_and_get_player_invalid_id() -> None:
    container = MagicMock()
    container.async_persistence = MagicMock()
    player, player_uuid = await _validate_and_get_player(container, "not-a-uuid")
    assert player is None
    assert player_uuid is None


@pytest.mark.asyncio
async def test_validate_and_get_player_success() -> None:
    player_id = uuid.uuid4()
    container = MagicMock()
    mock_player = MagicMock()
    container.async_persistence = MagicMock()
    container.async_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    player, player_uuid = await _validate_and_get_player(container, str(player_id))
    assert player is mock_player
    assert player_uuid == player_id


@pytest.mark.asyncio
async def test_update_player_status_effects_saves() -> None:
    container = MagicMock()
    container.async_persistence = AsyncMock()
    player = MagicMock()
    updated = await _update_player_status_effects(container, player, [], 1, True)
    assert updated is True
    player.set_status_effects.assert_called_once()
    container.async_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_all_status_effects_empty() -> None:
    app = FastAPI()
    container = MagicMock()
    player = MagicMock()
    player.get_status_effects.return_value = []
    effects, applied, count = await _process_all_status_effects(app, container, player, "p1")
    assert effects == []
    assert applied is False
    assert count == 0


@pytest.mark.asyncio
async def test_process_status_effects_no_online_players() -> None:
    app = FastAPI()
    app.state = MagicMock()
    container = MagicMock()
    container.async_persistence = MagicMock()
    container.connection_manager = MagicMock()
    container.connection_manager.online_players = {}
    app.state.container = container
    await process_status_effects(app, tick_count=1)


@pytest.mark.asyncio
async def test_process_combat_tick_calls_service() -> None:
    app = FastAPI()
    app.state = MagicMock()
    combat = MagicMock()
    combat.process_game_tick = AsyncMock()
    container = MagicMock(combat_service=combat)
    app.state.container = container
    await process_combat_tick(app, tick_count=5)
    combat.process_game_tick.assert_awaited_once_with(5)


@pytest.mark.asyncio
async def test_process_casting_progress_calls_magic_service() -> None:
    app = FastAPI()
    app.state = MagicMock()
    magic = MagicMock()
    magic.check_casting_progress = AsyncMock()
    container = MagicMock(magic_service=magic)
    app.state.container = container
    await process_casting_progress(app, tick_count=3)
    magic.check_casting_progress.assert_awaited_once_with(3)


@pytest.mark.asyncio
async def test_process_npc_maintenance_runs_on_interval() -> None:
    app = FastAPI()
    app.state = MagicMock()
    manager = MagicMock()
    manager.respawn_queue = {}
    manager.periodic_maintenance.return_value = {"respawned_npcs": 1}
    container = MagicMock(npc_lifecycle_manager=manager)
    app.state.container = container
    with patch("server.app.game_tick_processing.NPCMaintenanceConfig.should_run_maintenance", return_value=True):
        await process_npc_maintenance(app, tick_count=60)
    manager.periodic_maintenance.assert_called_once()


@pytest.mark.asyncio
async def test_cleanup_decayed_corpses_no_persistence() -> None:
    app = FastAPI()
    app.state = MagicMock()
    container = MagicMock()
    container.persistence = None
    app.state.container = container
    with patch("server.app.game_tick_processing._create_corpse_lifecycle_service", return_value=None):
        await cleanup_decayed_corpses(app, tick_count=60)


@pytest.mark.asyncio
async def test_cleanup_single_decayed_corpse_success() -> None:
    from server.app.game_tick_processing import _cleanup_single_decayed_corpse

    corpse = MagicMock()
    corpse.container_id = uuid.uuid4()
    corpse.room_id = "room-1"
    service = MagicMock()
    service.cleanup_decayed_corpse = AsyncMock()
    cm = MagicMock()
    with patch("server.app.game_tick_processing.emit_container_decayed", new_callable=AsyncMock):
        ok = await _cleanup_single_decayed_corpse(service, cm, corpse, 60)
    assert ok is True


@pytest.mark.asyncio
async def test_process_dp_decay_and_death_no_service() -> None:
    from server.app.game_tick_processing import process_dp_decay_and_death

    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(player_death_service=None)
    await process_dp_decay_and_death(app, tick_count=1)


@pytest.mark.asyncio
async def test_process_player_effects_expiration_login_warded() -> None:
    from server.app.game_tick_processing import process_player_effects_expiration

    app = FastAPI()
    app.state = MagicMock()
    container = MagicMock()
    container.async_persistence = AsyncMock()
    container.connection_manager = MagicMock()
    player_id = str(uuid.uuid4())
    container.async_persistence.expire_player_effects_for_tick = AsyncMock(return_value=[(player_id, "login_warded")])
    app.state.container = container
    with patch(
        "server.app.game_tick_processing._grace_period_expiration_handler",
        new_callable=AsyncMock,
    ) as mock_handler:
        await process_player_effects_expiration(app, tick_count=1)
    mock_handler.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_status_effects_with_online_player() -> None:
    app = FastAPI()
    app.state = MagicMock()
    container = MagicMock()
    container.async_persistence = MagicMock()
    container.connection_manager = MagicMock()
    pid = uuid.uuid4()
    container.connection_manager.online_players = {pid: {}}
    app.state.container = container
    with patch(
        "server.app.game_tick_processing._process_player_status_effects",
        new_callable=AsyncMock,
        return_value=True,
    ):
        await process_status_effects(app, tick_count=2)


@pytest.mark.asyncio
async def test_process_single_player_mp_regeneration() -> None:
    from server.app.game_tick_processing import (
        _process_mp_regeneration,
        _process_single_player_mp_regeneration,
    )

    mp_service = MagicMock()
    mp_service.process_tick_regeneration = AsyncMock(return_value={"mp_restored": 2})
    player_id = str(uuid.uuid4())
    assert await _process_single_player_mp_regeneration(mp_service, player_id) is True

    container = MagicMock()
    container.mp_regeneration_service = mp_service
    container.connection_manager = MagicMock()
    container.connection_manager.online_players = {uuid.uuid4(): {}}
    await _process_mp_regeneration(container, MagicMock(), tick_count=1)


@pytest.mark.asyncio
async def test_process_mortally_wounded_skips_active_combat() -> None:
    from server.app.game_tick_processing import _process_mortally_wounded_player
    from server.models.combat import CombatStatus

    container = MagicMock()
    container.player_death_service = MagicMock()
    container.combat_service = MagicMock()
    combat = MagicMock()
    combat.status = CombatStatus.ACTIVE
    combat.combat_id = "c1"
    container.combat_service.get_combat_by_participant = AsyncMock(return_value=combat)
    player = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "Victim"
    session = AsyncMock()
    await _process_mortally_wounded_player(container, player, session)
    container.player_death_service.process_mortally_wounded_tick.assert_not_called()


@pytest.mark.asyncio
async def test_process_mortally_wounded_death_threshold() -> None:
    from server.app.game_tick_processing import _process_mortally_wounded_player

    container = MagicMock()
    container.player_death_service = MagicMock()
    container.player_death_service.process_mortally_wounded_tick = AsyncMock()
    container.player_death_service.handle_player_death = AsyncMock()
    container.player_death_service.handle_player_death = AsyncMock()
    container.combat_service = None
    container.player_respawn_service = MagicMock()
    container.player_respawn_service.move_player_to_limbo = AsyncMock()
    container.event_bus = MagicMock()
    player = MagicMock()
    player.player_id = str(uuid.uuid4())
    player.name = "Victim"
    player.current_room_id = "room-1"
    player.get_stats.return_value = {"current_dp": -10, "max_dp": 100}
    session = AsyncMock()
    with patch(
        "server.app.game_tick_processing.combat_messaging_integration.send_dp_decay_message",
        new_callable=AsyncMock,
    ):
        await _process_mortally_wounded_player(container, player, session)
    container.player_death_service.handle_player_death.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_dead_players_moves_to_limbo() -> None:
    from server.app.game_tick_processing import _process_dead_players

    container = MagicMock()
    container.player_death_service = MagicMock()
    container.player_respawn_service = MagicMock()
    player = MagicMock()
    player.player_id = "p1"
    player.name = "Dead"
    player.current_room_id = "room-1"
    container.player_death_service.get_dead_players = AsyncMock(return_value=[player])
    container.player_respawn_service.move_player_to_limbo = AsyncMock()
    session = AsyncMock()
    await _process_dead_players(container, session)
    container.player_respawn_service.move_player_to_limbo.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_dp_decay_and_death_with_session() -> None:
    from server.app.game_tick_processing import process_dp_decay_and_death

    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(player_death_service=MagicMock())

    async def _session_gen():
        yield AsyncMock()

    with patch("server.app.game_tick_processing.get_async_session", return_value=_session_gen()):
        with patch(
            "server.app.game_tick_processing._process_session_dp_decay_and_death",
            new_callable=AsyncMock,
        ) as mock_process:
            await process_dp_decay_and_death(app, tick_count=3)
    mock_process.assert_awaited_once()


@pytest.mark.asyncio
async def test_cleanup_decayed_corpses_on_interval() -> None:
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(connection_manager=MagicMock())
    corpse = MagicMock()
    corpse.container_id = uuid.uuid4()
    corpse.room_id = "room-1"
    service = MagicMock()
    service.get_all_decayed_corpses = AsyncMock(return_value=[corpse])
    service.cleanup_decayed_corpse = AsyncMock()
    with patch("server.app.game_tick_processing._create_corpse_lifecycle_service", return_value=service):
        with patch("server.app.game_tick_processing.emit_container_decayed", new_callable=AsyncMock):
            await cleanup_decayed_corpses(app, tick_count=60)


def test_create_corpse_lifecycle_service() -> None:
    from server.app.game_tick_processing import _create_corpse_lifecycle_service

    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(persistence=MagicMock(), connection_manager=MagicMock())
    with patch("server.app.game_tick_processing.get_mythos_chronicle", return_value=MagicMock()):
        service = _create_corpse_lifecycle_service(app)
    assert service is not None


@pytest.mark.asyncio
async def test_broadcast_tick_event() -> None:
    from server.app.game_tick_processing import broadcast_tick_event

    app = FastAPI()
    app.state = MagicMock()
    manager = MagicMock()
    player_id = uuid.uuid4()
    manager.player_websockets = {player_id: ["conn-1"]}
    manager.send_personal_message = AsyncMock()
    app.state.container = MagicMock(connection_manager=manager)
    chronicle = MagicMock()
    chronicle.get_current_mythos_datetime.return_value = MagicMock(isoformat=lambda: "2020-01-01T00:00:00")
    components = MagicMock(
        month_name="January",
        day_of_month=1,
        day_name="Monday",
        week_of_month=1,
        season="winter",
        daypart="morning",
        is_daytime=True,
        is_witching_hour=False,
    )
    chronicle.get_calendar_components.return_value = components
    chronicle.format_clock.return_value = "08:00"
    with patch("server.app.game_tick_processing.get_mythos_chronicle", return_value=chronicle):
        with patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock) as mock_broadcast:
            with patch(
                "server.app.game_tick_processing.is_player_in_login_grace_period",
                return_value=False,
            ):
                with patch(
                    "server.app.game_tick_processing.get_login_grace_period_remaining",
                    return_value=0.0,
                ):
                    await broadcast_tick_event(app, tick_count=10)
    mock_broadcast.assert_awaited_once()


@pytest.mark.asyncio
async def test_game_tick_loop_cancelled_on_sleep() -> None:
    import asyncio

    from server.app.game_tick_processing import game_tick_loop

    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(
        combat_service=None,
        magic_service=None,
        player_death_service=None,
        npc_lifecycle_manager=None,
    )
    with patch("server.app.game_tick_processing.get_tick_interval", return_value=0.01):
        with patch("server.app.game_tick_processing.sleep", side_effect=asyncio.CancelledError):
            with patch("server.app.game_tick_processing.process_player_effects_expiration", new_callable=AsyncMock):
                with patch("server.app.game_tick_processing.process_status_effects", new_callable=AsyncMock):
                    with patch("server.app.game_tick_processing.process_combat_tick", new_callable=AsyncMock):
                        with patch(
                            "server.app.game_tick_processing.process_casting_progress",
                            new_callable=AsyncMock,
                        ):
                            with patch(
                                "server.app.game_tick_processing.process_dp_decay_and_death",
                                new_callable=AsyncMock,
                            ):
                                with patch(
                                    "server.app.game_tick_processing.process_npc_maintenance",
                                    new_callable=AsyncMock,
                                ):
                                    with patch(
                                        "server.app.game_tick_processing.cleanup_decayed_corpses",
                                        new_callable=AsyncMock,
                                    ):
                                        await game_tick_loop(app)


@pytest.mark.asyncio
async def test_process_passive_lucidity_flux() -> None:
    from server.app.game_tick_processing import _process_passive_lucidity_flux

    container = MagicMock()
    container.passive_lucidity_flux_service = MagicMock()
    container.passive_lucidity_flux_service.process_tick = AsyncMock()
    await _process_passive_lucidity_flux(container, AsyncMock(), tick_count=1)
    container.passive_lucidity_flux_service.process_tick.assert_awaited_once()


def test_log_cleanup_results_warning_path() -> None:
    _log_cleanup_results(tick_count=60, cleaned_count=0, total_decayed=2)
