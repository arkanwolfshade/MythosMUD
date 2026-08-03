"""Unit tests for server.game.magic.spell_effects_support."""

from __future__ import annotations

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.magic import spell_effects_support as support
from server.schemas.shared import TargetMatch, TargetType


def _spell(**effect_data: object) -> MagicMock:
    spell = MagicMock()
    spell.spell_id = "buff_str"
    spell.effect_data = effect_data
    return spell


def _target(**kwargs: object) -> TargetMatch:
    defaults: dict[str, object] = {
        "target_id": str(uuid.uuid4()),
        "target_name": "Hero",
        "target_type": TargetType.PLAYER,
        "room_id": "room_001",
    }
    defaults.update(kwargs)
    return TargetMatch(**defaults)


def test_build_stat_modifications_shorthand() -> None:
    spell = _spell(stat="strength", delta=5)
    mods, err = support._build_stat_modifications(spell)
    assert err is None
    assert mods == {"strength": 5}


def test_build_stat_modifications_missing() -> None:
    spell = _spell()
    mods, err = support._build_stat_modifications(spell)
    assert mods is None
    assert err is not None
    assert err["success"] is False


@pytest.mark.asyncio
async def test_process_stat_modify_rejects_non_player() -> None:
    spell = _spell(stat_modifications={"strength": 1})
    target = _target(target_type=TargetType.NPC)
    result = await support.process_stat_modify_effect(MagicMock(), spell, target, 1.0)
    assert result["success"] is False


@pytest.mark.asyncio
async def test_process_stat_modify_success() -> None:
    spell = _spell(stat_modifications={"strength": 5}, duration=3)
    target = _target()
    player = MagicMock()
    player.get_stats.return_value = {"strength": 50}
    player.get_status_effects.return_value = []
    engine = MagicMock()
    engine.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    engine.player_service.persistence.save_player = AsyncMock()
    result = await support.process_stat_modify_effect(engine, spell, target, 1.0)
    assert result["success"] is True
    engine.player_service.persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_process_create_object_missing_prototype() -> None:
    spell = _spell()
    result = await support.process_create_object_effect(MagicMock(), spell, _target(), 1.0)
    assert "prototype" in result["message"].lower()


@pytest.mark.asyncio
async def test_process_create_object_for_player() -> None:
    spell = _spell(prototype_id="torch", quantity=2)
    target = _target()
    player = MagicMock()
    player.get_inventory.return_value = []
    engine = MagicMock()
    engine.player_service.persistence.get_player_by_id = AsyncMock(return_value=player)
    engine.player_service.persistence.save_player = AsyncMock()
    result = await support.process_create_object_effect(engine, spell, target, 1.0)
    assert result["success"] is True
    assert player.set_inventory.called


def test_create_object_for_room_placeholder() -> None:
    spell = _spell(prototype_id="rock")
    target = _target(target_type=TargetType.ROOM, room_id="room_1")
    result = support._create_object_for_room(spell, target)
    assert result["success"] is False
