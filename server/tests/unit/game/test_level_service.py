"""
Unit tests for LevelService: grant_xp, check_level_up, level-up hook.

Character creation revamp plan 4.1 (L3).
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.level_service import LevelService

# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names


@pytest.fixture
def mock_persistence():
    """Mock async persistence with get_player_by_id and save_player."""
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock()
    persistence.save_player = AsyncMock()
    return persistence


@pytest.fixture
def level_service(mock_persistence):
    """LevelService with mocked persistence."""
    return LevelService(async_persistence=mock_persistence)


@pytest.fixture
def sample_player():
    """Player-like object with experience_points and level."""
    p = MagicMock()
    p.player_id = uuid.uuid4()
    p.experience_points = 0
    p.level = 1
    return p


@pytest.mark.asyncio
async def test_grant_xp_zero_no_op(level_service, mock_persistence, sample_player):
    """grant_xp(amount=0) does not load or save."""
    await level_service.grant_xp(sample_player.player_id, 0)
    mock_persistence.get_player_by_id.assert_not_called()
    mock_persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_grant_xp_negative_raises(level_service, sample_player):
    """grant_xp(amount < 0) raises ValueError."""
    with pytest.raises(ValueError, match="non-negative"):
        await level_service.grant_xp(sample_player.player_id, -1)


@pytest.mark.asyncio
async def test_grant_xp_player_not_found_raises(level_service, mock_persistence):
    """grant_xp when player not found raises ValueError."""
    mock_persistence.get_player_by_id.return_value = None
    player_id = uuid.uuid4()
    with pytest.raises(ValueError, match="not found"):
        await level_service.grant_xp(player_id, 50)
    mock_persistence.get_player_by_id.assert_awaited_once_with(player_id)


@pytest.mark.asyncio
async def test_grant_xp_increases_xp_and_persists(level_service, mock_persistence, sample_player):
    """grant_xp adds amount to experience_points and saves (level unchanged)."""
    mock_persistence.get_player_by_id.return_value = sample_player
    # Keep level 1: total XP for level 2 is > 100 with our curve; 50 XP stays level 1
    await level_service.grant_xp(sample_player.player_id, 50)
    assert sample_player.experience_points == 50
    mock_persistence.save_player.assert_awaited_once_with(sample_player)


@pytest.mark.asyncio
async def test_grant_xp_level_up_calls_hook(mock_persistence, sample_player):
    """When level increases, save is called and level_up_hook is invoked."""
    hook = AsyncMock()
    service_with_hook = LevelService(async_persistence=mock_persistence, level_up_hook=hook)
    mock_persistence.get_player_by_id.return_value = sample_player
    # Grant enough XP to reach level 2 (total_xp_for_level(2) from level_curve)
    from server.game.level_curve import total_xp_for_level

    xp_for_two = total_xp_for_level(2)
    sample_player.experience_points = 0
    sample_player.level = 1
    await service_with_hook.grant_xp(sample_player.player_id, xp_for_two)
    assert sample_player.level == 2
    assert sample_player.experience_points == xp_for_two
    mock_persistence.save_player.assert_awaited()
    hook.assert_awaited_once_with(sample_player.player_id, 2)


@pytest.mark.asyncio
async def test_check_level_up_no_change_returns_false(level_service, mock_persistence, sample_player):
    """check_level_up when level already matches curve returns False."""
    from server.game.level_curve import level_from_total_xp

    sample_player.experience_points = 50
    sample_player.level = level_from_total_xp(50)
    mock_persistence.get_player_by_id.return_value = sample_player
    result = await level_service.check_level_up(sample_player.player_id)
    assert result is False
    mock_persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_check_level_up_player_not_found_raises(level_service, mock_persistence):
    """check_level_up when player not found raises ValueError."""
    mock_persistence.get_player_by_id.return_value = None
    with pytest.raises(ValueError, match="not found"):
        await level_service.check_level_up(uuid.uuid4())


@pytest.mark.asyncio
async def test_check_level_up_increase_persists_and_returns_true(level_service, mock_persistence, sample_player):
    """check_level_up when curve gives higher level updates player and returns True."""
    from server.game.level_curve import total_xp_for_level

    sample_player.experience_points = total_xp_for_level(3)
    sample_player.level = 1  # Out of sync: curve says 3
    mock_persistence.get_player_by_id.return_value = sample_player
    result = await level_service.check_level_up(sample_player.player_id)
    assert result is True
    assert sample_player.level == 3
    mock_persistence.save_player.assert_awaited_once_with(sample_player)
