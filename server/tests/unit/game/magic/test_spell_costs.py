"""Unit tests for SpellCostsService."""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.game.magic.spell_costs import SpellCostsService
from server.models.spell import Spell, SpellEffectType, SpellRangeType, SpellSchool, SpellTargetType


def _spell(**kwargs) -> Spell:
    base = {
        "spell_id": "test",
        "name": "Test",
        "description": "Test spell",
        "school": SpellSchool.ELEMENTAL,
        "mp_cost": 5,
        "target_type": SpellTargetType.SELF,
        "range_type": SpellRangeType.TOUCH,
        "effect_type": SpellEffectType.HEAL,
    }
    base.update(kwargs)
    return Spell(**base)


@pytest.fixture
def player_service():
    svc = MagicMock()
    svc.persistence = MagicMock()
    svc.persistence.get_player_by_id = AsyncMock(return_value=None)
    svc.persistence.save_player = AsyncMock()
    return svc


@pytest.fixture
def costs_service(player_service):
    return SpellCostsService(player_service)


@pytest.mark.asyncio
async def test_apply_costs_no_player(costs_service):
    await costs_service.apply_costs(uuid.uuid4(), _spell())
    costs_service.player_service.persistence.save_player.assert_not_called()


@pytest.mark.asyncio
async def test_apply_costs_spends_mp(costs_service, player_service):
    player = MagicMock()
    player.get_stats.return_value = {"magic_points": 10, "max_magic_points": 10, "current_dp": 5, "max_dp": 10}
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock):
        await costs_service.apply_costs(uuid.uuid4(), _spell(mp_cost=3))
    stats = player.get_stats()
    assert stats["magic_points"] == 7
    player_service.persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_apply_costs_mythos_lucidity_and_corruption(costs_service, player_service):
    player = MagicMock()
    player.get_stats.return_value = {
        "magic_points": 10,
        "lucidity": 50,
        "corruption": 1,
        "max_magic_points": 10,
        "current_dp": 5,
        "max_dp": 10,
    }
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    spell = _spell(
        school=SpellSchool.MYTHOS,
        lucidity_cost=10,
        corruption_on_cast=2,
    )
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock):
        await costs_service.apply_costs(uuid.uuid4(), spell)
    stats = player.get_stats()
    assert stats["lucidity"] == 40
    assert stats["corruption"] == 3


@pytest.mark.asyncio
async def test_apply_costs_send_event_failure_is_non_fatal(costs_service, player_service):
    player = MagicMock()
    player.get_stats.return_value = {"magic_points": 10, "max_magic_points": 10, "current_dp": 0, "max_dp": 10}
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    with patch(
        "server.realtime.connection_manager_api.send_game_event",
        new_callable=AsyncMock,
        side_effect=RuntimeError("no ws"),
    ):
        await costs_service.apply_costs(uuid.uuid4(), _spell(mp_cost=1))


@pytest.mark.asyncio
async def test_restore_mp_player_not_found(costs_service):
    result = await costs_service.restore_mp(uuid.uuid4(), 5)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_restore_mp_caps_at_max(player_service, costs_service):
    player = MagicMock()
    player.get_stats.return_value = {"magic_points": 8, "max_magic_points": 10}
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    result = await costs_service.restore_mp(uuid.uuid4(), 5)
    assert result["success"] is True
    assert result["current_mp"] == 10


@pytest.mark.asyncio
async def test_restore_mp_computes_max_from_power(player_service, costs_service):
    player = MagicMock()
    player.get_stats.return_value = {"magic_points": 0, "power": 50}
    player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    result = await costs_service.restore_mp(uuid.uuid4(), 100)
    assert result["success"] is True
    assert result["max_mp"] == 10
    assert result["current_mp"] == 10
