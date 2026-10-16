"""
Unit tests for game tick processing async functions.

Tests the async game tick processing functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import FastAPI

from server.app.game_tick_processing import (
    _process_damage_over_time_effect,
    _process_heal_over_time_effect,
    _process_single_effect,
    _update_player_status_effects,
    process_combat_tick,
    process_status_effects,
)
from server.events.event_types import PlayerDPUpdated


@pytest.fixture
def mock_app():
    """Create a mock FastAPI app."""
    app = MagicMock(spec=FastAPI)
    app.state = MagicMock()
    return app


@pytest.fixture
def mock_container():
    """Create a mock ApplicationContainer."""
    container = MagicMock()
    container.async_persistence = AsyncMock()
    return container


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = "player_001"
    player.get_status_effects = MagicMock(return_value=[])
    return player


@pytest.mark.asyncio
async def test_process_damage_over_time_effect_no_damage(mock_app, mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_damage_over_time_effect() with no damage."""
    # Parameter names must match fixture names for pytest automatic injection
    effect = {"type": "damage_over_time", "damage": 0, "remaining": 5}
    result = await _process_damage_over_time_effect(mock_app, mock_container, mock_player, effect, 5, "player_001")
    assert result is False


@pytest.mark.asyncio
async def test_process_damage_over_time_effect_no_remaining(mock_app, mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_damage_over_time_effect() with no remaining duration."""
    # Parameter names must match fixture names for pytest automatic injection
    effect = {"type": "damage_over_time", "damage": 10, "remaining": 0}
    result = await _process_damage_over_time_effect(mock_app, mock_container, mock_player, effect, 0, "player_001")
    assert result is False


@pytest.mark.asyncio
async def test_process_damage_over_time_effect_success(mock_app, mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_damage_over_time_effect() successful application."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_app.state.player_death_service = MagicMock()
    mock_container.async_persistence.damage_player = AsyncMock()
    effect = {"type": "damage_over_time", "damage": 10, "remaining": 5}
    result = await _process_damage_over_time_effect(mock_app, mock_container, mock_player, effect, 5, "player_001")
    assert result is True
    mock_container.async_persistence.damage_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_heal_over_time_effect_no_healing(mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_heal_over_time_effect() with no healing."""
    # Parameter names must match fixture names for pytest automatic injection
    effect = {"type": "heal_over_time", "healing": 0, "remaining": 5}
    result = await _process_heal_over_time_effect(mock_container, mock_player, effect, 5, "player_001")
    assert result is False


@pytest.mark.asyncio
async def test_process_heal_over_time_effect_no_remaining(mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_heal_over_time_effect() with no remaining duration."""
    # Parameter names must match fixture names for pytest automatic injection
    effect = {"type": "heal_over_time", "healing": 10, "remaining": 0}
    result = await _process_heal_over_time_effect(mock_container, mock_player, effect, 0, "player_001")
    assert result is False


@pytest.mark.asyncio
async def test_process_heal_over_time_effect_success(mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_heal_over_time_effect() successful application."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.async_persistence.heal_player = AsyncMock()
    effect = {"type": "heal_over_time", "healing": 10, "remaining": 5}
    result = await _process_heal_over_time_effect(mock_container, mock_player, effect, 5, "player_001")
    assert result is True
    mock_container.async_persistence.heal_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_single_effect_damage_over_time(mock_app, mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_single_effect() with damage_over_time effect."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_app.state.player_death_service = MagicMock()
    mock_container.async_persistence.damage_player = AsyncMock()
    effect = {"type": "damage_over_time", "damage": 10, "duration": 5, "remaining": 5}
    updated_effect, effect_applied = await _process_single_effect(
        mock_app, mock_container, mock_player, effect, "player_001"
    )
    assert updated_effect is not None
    assert updated_effect["remaining"] == 4
    assert effect_applied is True


@pytest.mark.asyncio
async def test_process_single_effect_heal_over_time(mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_single_effect() with heal_over_time effect."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.async_persistence.heal_player = AsyncMock()
    effect = {"type": "heal_over_time", "healing": 10, "duration": 5, "remaining": 5}
    updated_effect, effect_applied = await _process_single_effect(
        MagicMock(), mock_container, mock_player, effect, "player_001"
    )
    assert updated_effect is not None
    assert updated_effect["remaining"] == 4
    assert effect_applied is True


@pytest.mark.asyncio
async def test_process_single_effect_heal_over_time_waits_for_game_second() -> None:
    """heal_over_time heals once per game second: between seconds it neither heals nor burns duration."""
    heal_player: AsyncMock = AsyncMock()
    async_persistence: AsyncMock = AsyncMock()
    async_persistence.heal_player = heal_player
    container: MagicMock = MagicMock()
    container.async_persistence = async_persistence
    player: MagicMock = MagicMock()
    effect: dict[str, object] = {"type": "heal_over_time", "healing": 10, "duration": 5, "remaining": 5}

    updated_effect, effect_applied = await _process_single_effect(
        MagicMock(), container, player, effect, "player_001", second_tick=False
    )

    assert updated_effect == effect
    assert effect_applied is False
    heal_player.assert_not_awaited()


@pytest.mark.asyncio
@pytest.mark.parametrize("is_second", [False, True])
async def test_process_status_effects_tells_each_player_whether_this_is_a_game_second(is_second: bool) -> None:
    """process_status_effects must pass the once-per-second flag down to per-player processing."""
    player_id = uuid.uuid4()
    app = FastAPI()
    app.state = MagicMock()
    connection_manager: MagicMock = MagicMock()
    connection_manager.online_players = {player_id: {}}
    container: MagicMock = MagicMock()
    container.async_persistence = MagicMock()
    container.connection_manager = connection_manager
    app.state.container = container
    process_player: AsyncMock = AsyncMock(return_value=False)

    with (
        patch("server.app.game_tick_status_effects.is_game_second_tick", return_value=is_second),
        patch("server.app.game_tick_status_effects._process_player_status_effects", new=process_player),
    ):
        await process_status_effects(app, 7)

    process_player.assert_awaited_once_with(app, container, str(player_id), second_tick=is_second)


@pytest.mark.asyncio
async def test_process_heal_over_time_effect_publishes_dp_update() -> None:
    """heal_player only writes the database, so healing must publish PlayerDPUpdated for the client."""
    player_id = uuid.uuid4()
    stats: dict[str, object] = {"current_dp": 5, "max_dp": 20}
    player: MagicMock = MagicMock()
    player.player_id = player_id
    player.current_room_id = "room_001"
    player.get_stats = MagicMock(side_effect=lambda: stats)

    async def heal(_player: object, amount: int) -> None:
        stats["current_dp"] = 5 + amount

    published: list[object] = []
    event_bus: MagicMock = MagicMock()
    event_bus.publish = MagicMock(side_effect=published.append)
    async_persistence: AsyncMock = AsyncMock()
    async_persistence.heal_player = AsyncMock(side_effect=heal)
    container: MagicMock = MagicMock()
    container.async_persistence = async_persistence
    container.event_bus = event_bus
    effect: dict[str, object] = {"type": "heal_over_time", "healing": 4, "remaining": 3}

    applied = await _process_heal_over_time_effect(container, player, effect, 3, str(player_id))

    assert applied is True
    assert len(published) == 1
    event = published[0]
    assert isinstance(event, PlayerDPUpdated)
    assert (event.player_id, event.old_dp, event.new_dp, event.max_dp) == (player_id, 5, 9, 20)
    assert event.damage_taken == -4


@pytest.mark.asyncio
async def test_process_single_effect_expired(mock_app, mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _process_single_effect() with expired effect."""
    # Parameter names must match fixture names for pytest automatic injection
    effect = {"type": "generic", "duration": 5, "remaining": 1}
    updated_effect, effect_applied = await _process_single_effect(
        mock_app, mock_container, mock_player, effect, "player_001"
    )
    assert updated_effect is None
    assert effect_applied is False


@pytest.mark.asyncio
async def test_update_player_status_effects_no_changes(mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _update_player_status_effects() when no changes occurred."""
    # Parameter names must match fixture names for pytest automatic injection
    result = await _update_player_status_effects(mock_container, mock_player, [{"type": "test"}], 1, False)
    assert result is False


@pytest.mark.asyncio
async def test_update_player_status_effects_changes(mock_container, mock_player):  # pylint: disable=redefined-outer-name
    """Test _update_player_status_effects() when changes occurred."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_container.async_persistence.save_player = AsyncMock()
    mock_player.set_status_effects = MagicMock()
    result = await _update_player_status_effects(mock_container, mock_player, [{"type": "test"}], 2, False)
    assert result is True
    mock_container.async_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_status_effects_no_container(mock_app):  # pylint: disable=redefined-outer-name
    """Test process_status_effects() when container is invalid."""
    # Parameter name must match fixture name for pytest automatic injection
    mock_app.state.container = None
    await process_status_effects(mock_app, 1)
    # Should not raise


@pytest.mark.asyncio
async def test_process_status_effects_no_online_players(mock_app, mock_container):  # pylint: disable=redefined-outer-name
    """Test process_status_effects() when no online players."""
    # Parameter names must match fixture names for pytest automatic injection
    mock_app.state.container = mock_container
    mock_app.state.connection_manager = MagicMock()
    mock_app.state.connection_manager.online_players = {}
    await process_status_effects(mock_app, 1)
    # Should not raise


@pytest.mark.asyncio
async def test_process_combat_tick_no_service(mock_app):  # pylint: disable=redefined-outer-name
    """Test process_combat_tick() when combat service is not available."""
    # Parameter name must match fixture name for pytest automatic injection
    mock_app.state.combat_service = None
    await process_combat_tick(mock_app, 1)
    # Should not raise


@pytest.mark.asyncio
async def test_process_combat_tick_success(mock_app):  # pylint: disable=redefined-outer-name
    """Test process_combat_tick() successful execution."""
    # Parameter name must match fixture name for pytest automatic injection
    mock_combat_service = AsyncMock()
    mock_combat_service.process_game_tick = AsyncMock()
    mock_app.state.container = MagicMock()
    mock_app.state.container.combat_service = mock_combat_service
    await process_combat_tick(mock_app, 1)
    mock_combat_service.process_game_tick.assert_awaited_once_with(1)
