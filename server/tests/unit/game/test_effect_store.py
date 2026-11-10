"""Unit tests for content effect dicts and the PlayerEffects write path (ADR-029 steps 3b-i and 6d)."""

from __future__ import annotations

import json
import uuid

import pytest

from server.game import effect_store
from server.game.effect_store import PlayerEffects
from server.game.player_registry import EffectData, PlayerNotFoundError
from server.game.player_registry.player_effects import (
    ADD_EFFECT_SQL,
    DELETE_EFFECTS_BY_TYPE_SQL,
    DELETE_INSTANCE_SCOPED_SQL,
)
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

PLAYER = uuid.UUID("22222222-2222-2222-2222-222222222222")


def _rig(*effects: EffectData) -> tuple[PlayerEffects, LucidityHarness]:
    harness = lucidity_registry({PLAYER: None}, effects=effects)
    return PlayerEffects(harness.registry), harness


def _executed(harness: LucidityHarness, statement: object) -> int:
    """How many times the commit ran this exact statement (by identity: clauses define their own ==)."""
    return sum(1 for executed in harness.db.statements if executed is statement)


def _added(harness: LucidityHarness) -> dict[str, object]:
    [params] = [
        dict(params)
        for statement, params in zip(harness.db.statements, harness.db.executed, strict=True)
        if statement is ADD_EFFECT_SQL and params is not None
    ]
    return params


async def test_a_timed_content_effect_stores_its_duration_as_remaining_seconds() -> None:
    effects, harness = _rig()
    effect: dict[str, object] = {"type": "heal_over_time", "healing": 5, "duration": 15}

    effect_id = await effects.add_content(PLAYER, effect)

    stored = _added(harness)
    assert stored["effect_id"] == effect_id
    assert (stored["effect_type"], stored["category"], stored["remaining_seconds"]) == (
        "heal_over_time",
        "scripted",
        15,
    )
    assert json.loads(str(stored["payload"])) == {"healing": 5, "duration": 15}
    assert stored["instance_scoped"] is False
    assert harness.db.commits == 1  # an effect is sync: committed before the call returns


async def test_an_untimed_instance_scoped_content_effect_lasts_until_removed() -> None:
    effects, harness = _rig()

    _ = await effects.add_content(PLAYER, {"type": "lucidity_drain_over_time", "rate": 1, "instance_scoped": True})

    stored = _added(harness)
    assert stored["remaining_seconds"] is None and stored["instance_scoped"] is True
    assert json.loads(str(stored["payload"])) == {"rate": 1}


async def test_add_passes_the_options_a_spell_or_the_ward_gives() -> None:
    effects, harness = _rig()

    _ = await effects.add(
        PLAYER, "login_warded", "entry_ward", 30, {"intensity": 2, "source": "game_entry", "visibility_level": "hidden"}
    )

    stored = _added(harness)
    assert (stored["intensity"], stored["source"], stored["visibility_level"]) == (2, "game_entry", "hidden")


async def test_an_unknown_player_gets_no_effect() -> None:
    effects, harness = _rig()

    with pytest.raises(PlayerNotFoundError):
        _ = await effects.add(uuid.UUID(int=0), "blinded", "spell", 5)
    assert harness.db.statements == []


async def test_removing_by_type_returns_the_count_and_writes_one_delete() -> None:
    blinded = [EffectData(uuid.uuid4(), "blinded", "spell", 9, {}) for _ in range(2)]
    effects, harness = _rig(*blinded)

    assert await effects.remove_by_type(PLAYER, "blinded") == 2

    assert _executed(harness, DELETE_EFFECTS_BY_TYPE_SQL) == 1


async def test_clearing_instance_scoped_effects_returns_the_count() -> None:
    scoped = EffectData(uuid.uuid4(), "lucidity_drain_over_time", "scripted", None, {}, instance_scoped=True)
    effects, harness = _rig(scoped, EffectData(uuid.uuid4(), "blinded", "spell", 9, {}))

    assert await effects.clear_instance_scoped(PLAYER) == 1
    assert await effects.clear_instance_scoped(PLAYER) == 0  # nothing left: no second write

    assert _executed(harness, DELETE_INSTANCE_SCOPED_SQL) == 1


async def test_clearing_without_a_registry_changes_nothing_and_says_so() -> None:
    assert await effect_store.clear_instance_scoped_effects(None, PLAYER) == 0


async def test_clearing_with_a_registry_ends_the_scoped_effects() -> None:
    scoped = EffectData(uuid.uuid4(), "lucidity_drain_over_time", "scripted", None, {}, instance_scoped=True)
    _effects, harness = _rig(scoped)

    assert await effect_store.clear_instance_scoped_effects(harness.registry, PLAYER) == 1
    assert _executed(harness, DELETE_INSTANCE_SCOPED_SQL) == 1


def test_a_running_effect_reads_back_as_the_dict_content_wrote() -> None:
    effect: dict[str, object] = {"type": "lucidity_drain_over_time", "rate": 1, "instance_scoped": True}
    running = EffectData(
        id=uuid.uuid4(),
        effect_type="lucidity_drain_over_time",
        category="scripted",
        remaining_seconds=None,
        payload=effect_store.effect_payload(effect),
        instance_scoped=True,
    )

    assert effect_store.effect_dict(running) == effect
