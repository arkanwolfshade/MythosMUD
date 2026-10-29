"""Unit tests for server.game.magic.spell_effects_support."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.items.item_factory import ItemFactoryError
from server.game.magic import spell_effects_support as support
from server.game.player_registry import PlayerNotFoundError
from server.schemas.shared import TargetMatch, TargetType
from server.services.inventory_service import InventoryCapacityError


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
    save = AsyncMock()
    add_effect = AsyncMock(return_value="effect-id")
    persistence = MagicMock(get_player_by_id=AsyncMock(return_value=player), save_player=save)
    persistence.add_player_effect = add_effect
    engine = MagicMock(player_service=MagicMock(persistence=persistence))
    result = await support.process_stat_modify_effect(engine, spell, target, 1.0)
    assert result["success"] is True
    save.assert_awaited_once()
    # The buff marker is a player_effects row (ADR-029 step 3b-i), lasting the spell's duration in game seconds.
    add_effect.assert_awaited_once_with(
        uuid.UUID(target.target_id), "buff", "spell", 3, {"intensity": 1, "source": "spell:buff_str"}
    )


@pytest.mark.asyncio
async def test_process_create_object_missing_prototype() -> None:
    spell = _spell()
    result = await support.process_create_object_effect(MagicMock(), spell, _target(), 1.0)
    assert "prototype" in result["message"].lower()


@dataclass
class _Granter:
    """ItemGranter.grant, recording what it was asked (or failing with ``error``)."""

    error: Exception | None = None
    calls: list[tuple[uuid.UUID, str, int, dict[str, object]]] = field(default_factory=list)

    async def grant(self, player_id: uuid.UUID, prototype_id: str, quantity: int = 1, *, origin: object) -> None:
        self.calls.append((player_id, prototype_id, quantity, dict(cast(dict[str, object], origin))))
        if self.error is not None:
            raise self.error


@pytest.mark.asyncio
async def test_create_object_grants_a_real_item_through_the_registry() -> None:
    """ADR-029 step 4c-i: no hand-built stack and no full-row save; the ItemGranter commits the item."""
    granter = _Granter()
    target = _target()

    result = await support.process_create_object_effect(
        SimpleNamespace(item_granter=granter), _spell(prototype_id="torch", quantity=2), target, 1.0
    )

    assert result["success"] is True and result["quantity"] == 2
    assert granter.calls == [(uuid.UUID(target.target_id), "torch", 2, {"source": "spell_create_object"})]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("error", "message"),
    [
        (PlayerNotFoundError("gone"), "Target player not found"),
        (InventoryCapacityError("full"), "Hero's inventory is full"),
        (ItemFactoryError("Prototype 'torch' not found."), "Failed to create object: Prototype 'torch' not found."),
    ],
)
async def test_create_object_reports_why_nothing_was_created(error: Exception, message: str) -> None:
    result = await support.process_create_object_effect(
        SimpleNamespace(item_granter=_Granter(error)), _spell(prototype_id="torch"), _target(), 1.0
    )

    assert result == {"success": False, "message": message, "effect_applied": False}


@pytest.mark.asyncio
async def test_create_object_without_an_item_system_creates_nothing() -> None:
    result = await support.process_create_object_effect(
        SimpleNamespace(item_granter=None), _spell(prototype_id="torch"), _target(), 1.0
    )

    assert result["success"] is False


def test_create_object_for_room_placeholder() -> None:
    spell = _spell(prototype_id="rock")
    target = _target(target_type=TargetType.ROOM, room_id="room_1")
    result = support._create_object_for_room(spell, target)
    assert result["success"] is False
