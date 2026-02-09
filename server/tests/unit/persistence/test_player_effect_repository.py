"""
Unit tests for PlayerEffectRepository (ADR-009 effects system).

Tests add_effect, delete_effect, get_active_effects_for_player, has_effect,
get_effect_remaining_ticks, and expire_effects_for_tick.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.player_effect import PlayerEffect
from server.persistence.repositories.player_effect_repository import PlayerEffectRepository


@pytest.fixture
def repo():
    """Create PlayerEffectRepository instance."""
    return PlayerEffectRepository()


@pytest.fixture
def player_id():
    """Sample player UUID."""
    return uuid.uuid4()


def _make_effect(
    player_id_str: str,
    effect_type: str = "login_warded",
    duration: int = 100,
    applied_at_tick: int = 0,
) -> MagicMock:
    """Build a mock PlayerEffect with given fields."""
    e = MagicMock(spec=PlayerEffect)
    e.player_id = player_id_str
    e.effect_type = effect_type
    e.duration = duration
    e.applied_at_tick = applied_at_tick
    e.id = str(uuid.uuid4())
    return e


@pytest.mark.asyncio
async def test_add_effect_returns_id(repo, player_id):
    """add_effect persists effect and returns effect id."""
    mock_session = AsyncMock()
    mock_session.commit = AsyncMock()
    effect_id = str(uuid.uuid4())

    def set_id_on_refresh(obj):
        obj.id = effect_id

    mock_session.refresh = AsyncMock(side_effect=set_id_on_refresh)
    mock_session.add = MagicMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        result = await repo.add_effect(
            player_id,
            "login_warded",
            "entry_ward",
            duration=100,
            applied_at_tick=50,
        )

        assert result == effect_id
        mock_session.add.assert_called_once()
        mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_delete_effect(repo):
    """delete_effect removes effect by id."""
    effect_id = str(uuid.uuid4())
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock()
    mock_session.commit = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        await repo.delete_effect(effect_id)

        mock_session.execute.assert_called_once()
        mock_session.commit.assert_called_once()


@pytest.mark.asyncio
async def test_get_active_effects_for_player_filters_by_remaining(repo, player_id):
    """get_active_effects_for_player returns only effects with remaining_ticks > 0."""
    pid_str = str(player_id)
    effect_active = _make_effect(pid_str, "login_warded", duration=100, applied_at_tick=10)
    effect_expired = _make_effect(pid_str, "poisoned", duration=5, applied_at_tick=0)
    current_tick = 50
    # remaining for effect_active: 100 - (50 - 10) = 60 > 0
    # remaining for effect_expired: 5 - (50 - 0) = -45 <= 0

    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [effect_active, effect_expired]
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        active = await repo.get_active_effects_for_player(player_id, current_tick)

        assert len(active) == 1
        assert active[0].effect_type == "login_warded"


@pytest.mark.asyncio
async def test_has_effect_true(repo, player_id):
    """has_effect returns True when player has active effect of type."""
    pid_str = str(player_id)
    effect = _make_effect(pid_str, "login_warded", duration=100, applied_at_tick=0)
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [effect]
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        assert await repo.has_effect(player_id, "login_warded", current_tick=10) is True


@pytest.mark.asyncio
async def test_has_effect_false(repo, player_id):
    """has_effect returns False when no active effect of type."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        assert await repo.has_effect(player_id, "login_warded", current_tick=1000) is False


@pytest.mark.asyncio
async def test_get_effect_remaining_ticks(repo, player_id):
    """get_effect_remaining_ticks returns duration - (current_tick - applied_at_tick)."""
    pid_str = str(player_id)
    effect = _make_effect(pid_str, "login_warded", duration=100, applied_at_tick=20)
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = [effect]
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        remaining = await repo.get_effect_remaining_ticks(player_id, "login_warded", current_tick=50)
        assert remaining == 70  # 100 - (50 - 20)


@pytest.mark.asyncio
async def test_get_effect_remaining_ticks_none(repo, player_id):
    """get_effect_remaining_ticks returns None when no matching effect."""
    mock_session = AsyncMock()
    mock_result = MagicMock()
    mock_result.scalars.return_value.all.return_value = []
    mock_session.execute = AsyncMock(return_value=mock_result)
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = MagicMock()
        m.return_value.return_value = mock_session

        assert await repo.get_effect_remaining_ticks(player_id, "login_warded", current_tick=0) is None


@pytest.mark.asyncio
async def test_expire_effects_for_tick_returns_expired_and_deletes(repo):
    """expire_effects_for_tick returns (player_id, effect_type) and deletes rows."""
    effect1 = _make_effect("p1", "login_warded", duration=10, applied_at_tick=0)
    effect2 = _make_effect("p2", "poisoned", duration=5, applied_at_tick=0)
    current_tick = 20
    get_result = MagicMock()
    get_result.scalars.return_value.all.return_value = [effect1, effect2]
    mock_session = AsyncMock()
    mock_session.execute = AsyncMock(side_effect=[get_result, None])
    mock_session.commit = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    ctx = MagicMock()
    ctx.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    ctx.return_value.__aexit__ = AsyncMock(return_value=None)

    with patch("server.persistence.repositories.player_effect_repository.get_session_maker") as m:
        m.return_value = ctx

        expired = await repo.expire_effects_for_tick(current_tick)

        assert set(expired) == {("p1", "login_warded"), ("p2", "poisoned")}
        assert mock_session.commit.called
