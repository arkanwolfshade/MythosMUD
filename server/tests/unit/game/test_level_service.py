"""
Unit tests for LevelService: grant_xp and the level-up hook.

Character creation revamp plan 4.1 (L3). #879: level is derived by
persistence.award_player_xp (SQL-side curve), never computed in Python here.
"""

# pyright: reportUnknownMemberType=false, reportUnknownParameterType=false
# pyright: reportMissingParameterType=false, reportUnusedParameter=false
# TEST_MOCK: mock_persistence/mock_level_service are untyped MagicMocks (award_player_xp
# has no real signature to check against); fixture params take the mock's inferred type.

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.level_service import LevelService

# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names must match fixture names


@pytest.fixture
def mock_persistence():
    """Mock async persistence with award_player_xp returning (new_xp, old_level, new_level)."""
    persistence = MagicMock()
    persistence.award_player_xp = AsyncMock()
    return persistence


@pytest.fixture
def level_service(mock_persistence):
    """LevelService with mocked persistence."""
    return LevelService(async_persistence=mock_persistence)


@pytest.mark.asyncio
async def test_grant_xp_zero_no_op(level_service, mock_persistence):
    """grant_xp(amount=0) does not call persistence."""
    await level_service.grant_xp(uuid.uuid4(), 0)
    mock_persistence.award_player_xp.assert_not_called()


@pytest.mark.asyncio
async def test_grant_xp_negative_raises(level_service):
    """grant_xp(amount < 0) raises ValueError."""
    with pytest.raises(ValueError, match="non-negative"):
        await level_service.grant_xp(uuid.uuid4(), -1)


@pytest.mark.asyncio
async def test_grant_xp_player_not_found_propagates(level_service, mock_persistence):
    """grant_xp propagates persistence's ValueError when player not found."""
    mock_persistence.award_player_xp.side_effect = ValueError("Player not found")
    player_id = uuid.uuid4()
    with pytest.raises(ValueError, match="not found"):
        await level_service.grant_xp(player_id, 50)
    mock_persistence.award_player_xp.assert_awaited_once_with(player_id, 50, "grant_xp")


@pytest.mark.asyncio
async def test_grant_xp_no_level_change_does_not_call_hook(level_service, mock_persistence):
    """When persistence reports old_level == new_level, the level-up hook is not invoked."""
    hook = AsyncMock()
    service_with_hook = LevelService(async_persistence=mock_persistence, level_up_hook=hook)
    mock_persistence.award_player_xp.return_value = (50, 1, 1)
    player_id = uuid.uuid4()
    await service_with_hook.grant_xp(player_id, 50)
    hook.assert_not_awaited()


@pytest.mark.asyncio
async def test_grant_xp_level_up_calls_hook(mock_persistence):
    """When persistence reports a level increase, the level-up hook is invoked with the new level."""
    hook = AsyncMock()
    service_with_hook = LevelService(async_persistence=mock_persistence, level_up_hook=hook)
    mock_persistence.award_player_xp.return_value = (100, 1, 2)
    player_id = uuid.uuid4()
    await service_with_hook.grant_xp(player_id, 100)
    hook.assert_awaited_once_with(player_id, 2)


@pytest.mark.asyncio
async def test_grant_xp_without_hook_does_not_raise_on_level_up(level_service, mock_persistence):
    """No level_up_hook configured: a level-up still completes without error."""
    mock_persistence.award_player_xp.return_value = (300, 2, 3)
    await level_service.grant_xp(uuid.uuid4(), 200)
