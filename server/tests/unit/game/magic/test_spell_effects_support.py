"""Unit tests for server.game.magic.spell_effects_support."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.game.items.item_factory import ItemFactoryError
from server.game.magic import spell_effects_support as support
from server.game.player_registry import PlayerNotFoundError
from server.schemas.shared import TargetMatch, TargetType
from server.services.inventory_service import InventoryCapacityError
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry


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


def _power_drain() -> MagicMock:
    """The seeded effect data of Power Drain."""
    return _spell(stat="mp", delta=-10, transfer_to_caster=True)


async def _cast_at(
    spell: MagicMock,
    stats: dict[str, object],
    *,
    mastery: float = 1.0,
    target_id: uuid.UUID | None = None,
) -> tuple[Mapping[str, object], LucidityHarness, uuid.UUID, uuid.UUID]:
    """Cast ``spell`` from one registry player at another; returns (result, harness, target id, caster id)."""
    target, caster = target_id or uuid.uuid4(), uuid.uuid4()
    harness = lucidity_registry({target: None, caster: None}, stats=stats)
    engine = SimpleNamespace(player_registry=harness.registry)
    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock):
        result = await support.process_stat_modify_effect(
            engine, spell, _target(target_id=str(target)), mastery, caster_id=caster
        )
    return result, harness, target, caster


@pytest.mark.asyncio
async def test_power_drain_moves_mp_to_the_caster_in_one_commit() -> None:
    result, harness, target, caster = await _cast_at(_power_drain(), {"magic_points": 12, "max_magic_points": 30})

    assert result["success"] is True and result["effect_applied"] is True
    assert result["stat_changes"] == {"magic_points": -10}
    assert result["mp_transferred"] == 10
    assert harness.stats(target)["magic_points"] == 2
    assert harness.stats(caster)["magic_points"] == 22
    assert harness.db.commits == 1


@pytest.mark.asyncio
async def test_power_drain_tells_both_players() -> None:
    target, caster = uuid.uuid4(), uuid.uuid4()
    harness = lucidity_registry({target: None, caster: None}, stats={"magic_points": 12, "max_magic_points": 30})
    engine = SimpleNamespace(player_registry=harness.registry)

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock) as send:
        _ = await support.process_stat_modify_effect(
            engine, _power_drain(), _target(target_id=str(target)), 1.0, caster_id=caster
        )

    assert [call.args[0] for call in send.await_args_list] == [target, caster]


@pytest.mark.asyncio
async def test_power_drain_scales_with_mastery() -> None:
    result, _, _, _ = await _cast_at(_power_drain(), {"magic_points": 12, "max_magic_points": 30}, mastery=0.5)

    assert result["stat_changes"] == {"magic_points": -5}


@pytest.mark.asyncio
async def test_power_drain_takes_only_what_the_target_has() -> None:
    result, harness, target, caster = await _cast_at(_power_drain(), {"magic_points": 3, "max_magic_points": 30})

    assert result["mp_transferred"] == 3
    assert harness.stats(target)["magic_points"] == 0
    assert harness.stats(caster)["magic_points"] == 6


@pytest.mark.asyncio
async def test_power_drain_on_a_drained_target_does_nothing() -> None:
    result, harness, _, _ = await _cast_at(_power_drain(), {"magic_points": 0, "max_magic_points": 30})

    assert result["success"] is True and result["effect_applied"] is False
    assert harness.db.commits == 0


@pytest.mark.asyncio
async def test_a_full_caster_still_drains_but_gains_nothing() -> None:
    result, harness, target, caster = await _cast_at(_power_drain(), {"magic_points": 30, "max_magic_points": 30})

    assert result["stat_changes"] == {"magic_points": -10}
    assert result["mp_transferred"] == 0
    assert harness.stats(target)["magic_points"] == 20
    assert harness.stats(caster)["magic_points"] == 30


@pytest.mark.asyncio
async def test_power_drain_on_yourself_only_costs_you() -> None:
    caster = uuid.uuid4()
    harness = lucidity_registry({caster: None}, stats={"magic_points": 12, "max_magic_points": 30})
    engine = SimpleNamespace(player_registry=harness.registry)

    with patch("server.realtime.connection_manager_api.send_game_event", new_callable=AsyncMock):
        result = await support.process_stat_modify_effect(
            engine, _power_drain(), _target(target_id=str(caster)), 1.0, caster_id=caster
        )

    assert result["mp_transferred"] == 0
    assert harness.stats(caster)["magic_points"] == 2


@pytest.mark.asyncio
async def test_an_mp_effect_without_a_transfer_only_changes_the_target() -> None:
    result, harness, target, caster = await _cast_at(
        _spell(stat="mp", delta=-4), {"magic_points": 12, "max_magic_points": 30}
    )

    assert result["mp_transferred"] == 0
    assert harness.stats(target)["magic_points"] == 8
    assert harness.registry.peek(caster) is None  # the caster was never touched


@pytest.mark.asyncio
async def test_a_positive_mp_effect_restores_the_target() -> None:
    result, harness, target, _ = await _cast_at(
        _spell(stat="magic_points", delta=4), {"magic_points": 2, "max_magic_points": 30}
    )

    assert result["stat_changes"] == {"magic_points": 4}
    assert "Restored 4 magic points" in str(result["message"])
    assert harness.stats(target)["magic_points"] == 6


@pytest.mark.asyncio
async def test_power_drain_on_an_unknown_player_fails() -> None:
    engine = SimpleNamespace(player_registry=lucidity_registry({}).registry)

    result = await support.process_stat_modify_effect(engine, _power_drain(), _target(), 1.0, caster_id=uuid.uuid4())

    assert result == {"success": False, "message": "Target player not found", "effect_applied": False}


@pytest.mark.asyncio
async def test_power_drain_without_a_registry_fails() -> None:
    engine = SimpleNamespace(player_registry=None)

    result = await support.process_stat_modify_effect(engine, _power_drain(), _target(), 1.0, caster_id=uuid.uuid4())

    assert result["success"] is False


@pytest.mark.asyncio
async def test_a_failed_power_drain_commit_changes_neither_player() -> None:
    target, caster = uuid.uuid4(), uuid.uuid4()
    harness = lucidity_registry({target: None, caster: None}, stats={"magic_points": 12, "max_magic_points": 30})
    harness.db.fail_commits, harness.db.commit_error = 1, SQLAlchemyError("db down")
    engine = SimpleNamespace(player_registry=harness.registry)

    result = await support.process_stat_modify_effect(
        engine, _power_drain(), _target(target_id=str(target)), 1.0, caster_id=caster
    )

    assert result["success"] is False
    for player_id in (target, caster):
        view = harness.registry.peek(player_id)
        assert view is None or view.row.stats["magic_points"] == 12


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
