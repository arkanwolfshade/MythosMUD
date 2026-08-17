"""
Unit tests for game tick processing functions.

Tests the game tick processing logic including status effects, combat, and maintenance tasks.
"""

# pyright: reportPrivateUsage=false
# Reason: this module unit-tests private tick helpers (_process_*, corpse cleanup internals).

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.game_tick_corpses import (
    _cleanup_single_decayed_corpse,
    _log_cleanup_results,
    cleanup_decayed_corpses,
)
from server.app.game_tick_processing import (
    _process_all_status_effects,
    _process_damage_over_time_effect,
    _process_heal_over_time_effect,
    _process_mp_regeneration,
    _process_single_effect,
    _process_single_player_mp_regeneration,
    _update_player_status_effects,
    _validate_and_get_player,
    _validate_app_state_for_status_effects,
    _validate_mp_regeneration_services,
    get_current_tick,
    get_tick_interval,
    process_casting_progress,
    process_combat_tick,
    process_dp_decay_and_death,
    process_npc_maintenance,
    process_player_effects_expiration,
    process_status_effects,
    reset_current_tick,
)

JsonMap = dict[str, object]


def test_get_current_tick() -> None:
    """Test get_current_tick returns the current tick value."""
    reset_current_tick()
    assert get_current_tick() == 0


def test_reset_current_tick() -> None:
    """Test reset_current_tick resets the tick counter."""
    reset_current_tick()
    initial = get_current_tick()
    assert initial == 0

    reset_current_tick()
    assert get_current_tick() == 0


def test_get_tick_interval() -> None:
    """Test get_tick_interval returns tick interval from config."""
    with patch("server.app.game_tick_processing.get_config") as mock_config:
        game: MagicMock = MagicMock()
        game.server_tick_rate = 0.5
        mock_config_instance: MagicMock = MagicMock()
        mock_config_instance.game = game
        mock_config.return_value = mock_config_instance

        interval = get_tick_interval()
        assert interval == 0.5


def test_validate_app_state_for_status_effects_no_container() -> None:
    """Test _validate_app_state_for_status_effects returns False when no container."""
    app = FastAPI()
    app.state = MagicMock()
    del app.state.container  # Remove container attribute

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_no_async_persistence() -> None:
    """Test _validate_app_state_for_status_effects returns False when no async_persistence."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.async_persistence = None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_no_connection_manager() -> None:
    """Test _validate_app_state_for_status_effects returns False when no connection_manager."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_valid() -> None:
    """Test _validate_app_state_for_status_effects returns True when all required components exist."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = MagicMock()
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is True
    assert container == mock_container


def test_validate_app_state_for_status_effects_container_is_none() -> None:
    """Test _validate_app_state_for_status_effects returns False when container is None."""
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = None

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_connection_manager_is_none() -> None:
    """Test _validate_app_state_for_status_effects returns False when connection_manager is None."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container: MagicMock = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_mp_regeneration_services() -> None:
    container: MagicMock = MagicMock()
    container.mp_regeneration_service = MagicMock()
    container.connection_manager = MagicMock()
    assert _validate_mp_regeneration_services(container) is True
    container.mp_regeneration_service = None
    assert _validate_mp_regeneration_services(container) is False


def test_log_cleanup_results() -> None:
    _log_cleanup_results(tick_count=60, cleaned_count=2, total_decayed=3)


@pytest.mark.asyncio
async def test_process_heal_over_time_effect() -> None:
    heal_player: AsyncMock = AsyncMock()
    async_persistence: AsyncMock = AsyncMock()
    async_persistence.heal_player = heal_player
    container: MagicMock = MagicMock()
    container.async_persistence = async_persistence
    player: MagicMock = MagicMock()
    effect: JsonMap = {"type": "heal_over_time", "healing": 5, "duration": 2, "remaining": 2}
    applied = await _process_heal_over_time_effect(container, player, effect, 1, "player-1")
    assert applied is True
    heal_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_damage_over_time_zero_remaining() -> None:
    app = FastAPI()
    container: MagicMock = MagicMock()
    player: MagicMock = MagicMock()
    effect: JsonMap = {"type": "damage_over_time", "damage": 3}
    applied = await _process_damage_over_time_effect(app, container, player, effect, 0, "player-1")
    assert applied is False


@pytest.mark.asyncio
async def test_process_single_effect_heal_expires() -> None:
    app = FastAPI()
    container: MagicMock = MagicMock()
    container.async_persistence = AsyncMock()
    player: MagicMock = MagicMock()
    effect: JsonMap = {"type": "heal_over_time", "healing": 2, "duration": 2, "remaining": 2}
    updated, applied = await _process_single_effect(app, container, player, effect, "p1")
    assert updated is not None
    assert updated["remaining"] == 1
    assert applied is True


@pytest.mark.asyncio
async def test_validate_and_get_player_invalid_id() -> None:
    container: MagicMock = MagicMock()
    container.async_persistence = MagicMock()
    player, player_uuid = await _validate_and_get_player(container, "not-a-uuid")
    assert player is None
    assert player_uuid is None


@pytest.mark.asyncio
async def test_validate_and_get_player_success() -> None:
    player_id = uuid.uuid4()
    container: MagicMock = MagicMock()
    mock_player: MagicMock = MagicMock()
    get_player_by_id: AsyncMock = AsyncMock(return_value=mock_player)
    async_persistence: MagicMock = MagicMock()
    async_persistence.get_player_by_id = get_player_by_id
    container.async_persistence = async_persistence
    player, player_uuid = await _validate_and_get_player(container, str(player_id))
    assert player is mock_player
    assert player_uuid == player_id


@pytest.mark.asyncio
async def test_update_player_status_effects_saves() -> None:
    save_player: AsyncMock = AsyncMock()
    async_persistence: AsyncMock = AsyncMock()
    async_persistence.save_player = save_player
    container: MagicMock = MagicMock()
    container.async_persistence = async_persistence
    set_status_effects: MagicMock = MagicMock()
    player: MagicMock = MagicMock()
    player.set_status_effects = set_status_effects
    updated = await _update_player_status_effects(container, player, [], 1, True)
    assert updated is True
    set_status_effects.assert_called_once()
    save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_all_status_effects_empty() -> None:
    app = FastAPI()
    container: MagicMock = MagicMock()
    get_status_effects: MagicMock = MagicMock(return_value=[])
    player: MagicMock = MagicMock()
    player.get_status_effects = get_status_effects
    effects, applied, count = await _process_all_status_effects(app, container, player, "p1")
    assert effects == []
    assert applied is False
    assert count == 0


@pytest.mark.asyncio
async def test_process_status_effects_no_online_players() -> None:
    app = FastAPI()
    app.state = MagicMock()
    connection_manager: MagicMock = MagicMock()
    connection_manager.online_players = {}
    container: MagicMock = MagicMock()
    container.async_persistence = MagicMock()
    container.connection_manager = connection_manager
    app.state.container = container
    await process_status_effects(app, tick_count=1)


@pytest.mark.asyncio
async def test_process_combat_tick_calls_service() -> None:
    app = FastAPI()
    app.state = MagicMock()
    process_game_tick: AsyncMock = AsyncMock()
    combat: MagicMock = MagicMock()
    combat.process_game_tick = process_game_tick
    container: MagicMock = MagicMock(combat_service=combat)
    app.state.container = container
    await process_combat_tick(app, tick_count=5)
    process_game_tick.assert_awaited_once_with(5)


@pytest.mark.asyncio
async def test_process_casting_progress_calls_magic_service() -> None:
    app = FastAPI()
    app.state = MagicMock()
    check_casting_progress: AsyncMock = AsyncMock()
    magic: MagicMock = MagicMock()
    magic.check_casting_progress = check_casting_progress
    container: MagicMock = MagicMock(magic_service=magic)
    app.state.container = container
    await process_casting_progress(app, tick_count=3)
    check_casting_progress.assert_awaited_once_with(3)


@pytest.mark.asyncio
async def test_process_npc_maintenance_runs_on_interval() -> None:
    app = FastAPI()
    app.state = MagicMock()
    periodic_maintenance: MagicMock = MagicMock(return_value={"respawned_npcs": 1})
    manager: MagicMock = MagicMock()
    manager.respawn_queue = {}
    manager.periodic_maintenance = periodic_maintenance
    container: MagicMock = MagicMock(npc_lifecycle_manager=manager)
    app.state.container = container
    with patch("server.app.game_tick_processing.NPCMaintenanceConfig.should_run_maintenance", return_value=True):
        await process_npc_maintenance(app, tick_count=60)
    periodic_maintenance.assert_called_once()


@pytest.mark.asyncio
async def test_cleanup_decayed_corpses_no_persistence() -> None:
    app = FastAPI()
    app.state = MagicMock()
    container: MagicMock = MagicMock()
    container.persistence = None
    app.state.container = container
    with patch("server.app.game_tick_corpses._create_corpse_lifecycle_service", return_value=None):
        await cleanup_decayed_corpses(app, tick_count=60)


@pytest.mark.asyncio
async def test_cleanup_single_decayed_corpse_success() -> None:
    corpse: MagicMock = MagicMock()
    corpse.container_id = uuid.uuid4()
    corpse.room_id = "room-1"
    cleanup_decayed_corpse: AsyncMock = AsyncMock()
    service: MagicMock = MagicMock()
    service.cleanup_decayed_corpse = cleanup_decayed_corpse
    cm: MagicMock = MagicMock()
    with patch("server.services.container_websocket_events.emit_container_decayed", new_callable=AsyncMock):
        ok = await _cleanup_single_decayed_corpse(service, cm, corpse, 60)
    assert ok is True


@pytest.mark.asyncio
async def test_process_dp_decay_and_death_no_service() -> None:
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = MagicMock(player_death_service=None)
    await process_dp_decay_and_death(app, tick_count=1)


@pytest.mark.asyncio
async def test_process_player_effects_expiration_login_warded() -> None:
    app = FastAPI()
    app.state = MagicMock()
    expire_player_effects_for_tick: AsyncMock = AsyncMock()
    async_persistence: AsyncMock = AsyncMock()
    async_persistence.expire_player_effects_for_tick = expire_player_effects_for_tick
    connection_manager: MagicMock = MagicMock()
    container: MagicMock = MagicMock()
    container.async_persistence = async_persistence
    container.connection_manager = connection_manager
    player_id = str(uuid.uuid4())
    expire_player_effects_for_tick.return_value = [(player_id, "login_warded")]
    app.state.container = container
    with patch(
        "server.app.game_tick_status_effects.handle_login_grace_period_expiration",
        new_callable=AsyncMock,
    ) as mock_handler:
        await process_player_effects_expiration(app, tick_count=1)
    mock_handler.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_status_effects_with_online_player() -> None:
    app = FastAPI()
    app.state = MagicMock()
    connection_manager: MagicMock = MagicMock()
    pid = uuid.uuid4()
    connection_manager.online_players = {pid: {}}
    container: MagicMock = MagicMock()
    container.async_persistence = MagicMock()
    container.connection_manager = connection_manager
    app.state.container = container
    with patch(
        "server.app.game_tick_status_effects._process_player_status_effects",
        new_callable=AsyncMock,
        return_value=True,
    ):
        await process_status_effects(app, tick_count=2)


@pytest.mark.asyncio
async def test_process_single_player_mp_regeneration() -> None:
    process_tick_regeneration: AsyncMock = AsyncMock(return_value={"mp_restored": 2})
    mp_service: MagicMock = MagicMock()
    mp_service.process_tick_regeneration = process_tick_regeneration
    player_id = str(uuid.uuid4())
    assert await _process_single_player_mp_regeneration(mp_service, player_id) is True

    connection_manager: MagicMock = MagicMock()
    connection_manager.online_players = {uuid.uuid4(): {}}
    container: MagicMock = MagicMock()
    container.mp_regeneration_service = mp_service
    container.connection_manager = connection_manager
    await _process_mp_regeneration(container, MagicMock(), tick_count=1)
