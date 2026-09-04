"""
Unit tests for game tick processing async functions.

Tests the async game tick processing functions.
"""

from unittest.mock import AsyncMock, MagicMock

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
