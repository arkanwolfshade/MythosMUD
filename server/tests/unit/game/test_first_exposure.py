"""The First Exposure ending: what a tutorial delirium respawn leaves the player with (ADR-028, #1080)."""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast
from unittest.mock import patch

import pytest

from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.game import first_exposure as module
from server.game.first_exposure import (
    EPILOGUE_QUEST_ID,
    FINISH_ACTIONS,
    RESTORED_LCD,
    FirstExposureFinisher,
    apply_first_exposure_end_state,
    restore_first_exposure_lucidity,
)
from server.game.instance_state import StrippedInventory
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.game.player_registry import LucidityData, PlayerAggregate, PlayerRegistry
from server.game.scripted_actions import QuestActionService, ScriptedActionContext
from server.models.corruption import CorruptionUpdateResult, compute_tier
from server.models.player import Player
from server.schemas.scripted_actions import CorruptionAtLeastAction, StartQuestAction, parse_scripted_actions
from server.services.lucidity_service import resolve_tier
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, lucidity_registry, raw_row


def _stack(item_id: str, *flags: str) -> dict[str, object]:
    stack: dict[str, object] = {"item_id": item_id, "prototype_id": item_id, "quantity": 1}
    if flags:
        stack["flags"] = list(flags)
    return stack


def _tutorial_player(instance_id: str | None = "instance-abc") -> Player:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = f"instance_{uuid.uuid4()}_vault"
    player.tutorial_instance_id = instance_id
    player.set_stats({"current_dp": 1, "max_dp": 100})
    player.set_inventory([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG)])
    return player


# --- the in-session end state -----------------------------------------------------------------------------------


def _tutorial_aggregate(instance_id: str | None = "instance-abc") -> PlayerAggregate:
    """The tutorial player as the delirium respawn's registry unit holds them (ADR-029 step 6a)."""
    return aggregate(
        raw_row(
            uuid.uuid4(),
            current_room_id=f"instance_{uuid.uuid4()}_vault",
            tutorial_instance_id=instance_id,
            stats={"current_dp": 1, "max_dp": 100},
            inventory=json.dumps([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG)]),
        )
    )


def test_the_end_state_leaves_a_tutorial_player_whole_and_in_the_ward() -> None:
    player = _tutorial_aggregate()

    applied = apply_first_exposure_end_state(player)

    assert applied is True
    assert player.row.current_room_id == RECOVERY_WARD_ROOM_ID
    assert player.row.tutorial_instance_id is None
    assert player.row.stats["current_dp"] == player.row.stats["max_dp"]
    assert player.row.sync_required  # it commits with the respawn


def test_the_end_state_leaves_the_inventory_to_the_finisher() -> None:
    """The amulet is stripped by FirstExposureFinisher, after the respawn's unit has committed."""
    player = _tutorial_aggregate()

    _ = apply_first_exposure_end_state(player)

    assert [stack["item_id"] for stack in player.inventory.carried] == ["lantern", "jade_amulet"]
    assert not player.inventory.dirty


def test_the_end_state_does_nothing_for_a_player_who_is_not_in_the_tutorial() -> None:
    player = _tutorial_aggregate(instance_id=None)
    room_before = player.row.current_room_id

    applied = apply_first_exposure_end_state(player)

    assert applied is False
    assert player.row.current_room_id == room_before
    assert not player.row.dirty


def test_the_end_state_is_idempotent() -> None:
    player = _tutorial_aggregate()

    _ = apply_first_exposure_end_state(player)
    second = apply_first_exposure_end_state(player)

    assert second is False  # tutorial_instance_id is cleared, so a replay finds nothing to do


# --- what runs after the commit ---------------------------------------------------------------------------------


def test_the_finish_actions_are_data_that_parses_and_raise_corruption_to_the_floor_then_start_the_epilogue() -> None:
    assert [type(action) for action in FINISH_ACTIONS] == [CorruptionAtLeastAction, StartQuestAction]
    corruption, quest = FINISH_ACTIONS
    assert isinstance(corruption, CorruptionAtLeastAction)
    assert corruption.value == 1  # a floor, never "+1": replay, restart and skip are idempotent
    assert isinstance(quest, StartQuestAction)
    assert quest.quest_id == EPILOGUE_QUEST_ID
    assert parse_scripted_actions([a.model_dump() for a in FINISH_ACTIONS]) == list(FINISH_ACTIONS)


@dataclass
class Rig:
    player: Player | None
    ran: list[tuple[tuple[object, ...], object]] = field(
        default_factory=lambda: cast(list[tuple[tuple[object, ...], object]], [])
    )
    flushed: list[str] = field(default_factory=lambda: cast(list[str], []))
    order: list[str] = field(default_factory=lambda: cast(list[str], []))
    actions_fail: bool = False
    clear_fails: bool = False
    strip_fails: bool = False
    stripped: list[uuid.UUID] = field(default_factory=lambda: cast(list[uuid.UUID], []))
    cleared: list[uuid.UUID] = field(default_factory=lambda: cast(list[uuid.UUID], []))


class FakePersistence:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        _ = player_id
        return self._rig.player

    async def adjust_corruption(  # pragma: no cover - the runner (the corruption floor's caller) is faked
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
        bypass_permanence_floor: bool = False,
    ) -> CorruptionUpdateResult:
        _ = reason_code, metadata, location_id, bypass_permanence_floor
        return CorruptionUpdateResult(player_id, 0, delta, compute_tier(0), compute_tier(delta), delta)


class FakeFlush:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def flush(self, instance_id: str) -> int:
        self._rig.order.append("flush")
        self._rig.flushed.append(instance_id)
        return 0


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    rig = Rig(_tutorial_player())

    async def fake_run(actions: tuple[object, ...], ctx: object) -> None:
        rig.order.append("actions")
        if rig.actions_fail:
            raise RuntimeError("quest store down")
        rig.ran.append((tuple(actions), ctx))

    async def fake_clear(_registry: PlayerRegistry | None, player_id: uuid.UUID) -> int:
        rig.order.append("clear")
        if rig.clear_fails:
            raise RuntimeError("database down")
        rig.cleared.append(player_id)
        return 1

    async def fake_strip(_registry: PlayerRegistry, player_id: uuid.UUID) -> StrippedInventory:
        rig.order.append("strip")
        if rig.strip_fails:
            raise RuntimeError("database down")
        rig.stripped.append(player_id)
        return StrippedInventory(1, [], {})

    monkeypatch.setattr(module, "run_scripted_actions", fake_run)
    monkeypatch.setattr(module, "clear_instance_scoped_effects", fake_clear)
    monkeypatch.setattr(module, "strip_instance_bound_items", fake_strip)
    return rig


def _finisher(rig: Rig, *, with_registry: bool = True) -> FirstExposureFinisher:
    return FirstExposureFinisher(
        persistence=cast(module.FinishPersistence, FakePersistence(rig)),
        quest_service=cast(QuestActionService, cast(object, SimpleNamespace())),
        flush=cast(module.InstanceFlush, FakeFlush(rig)),
        registry=PlayerRegistry(FakeDatabase().session) if with_registry else None,
    )


@pytest.mark.asyncio
async def test_finishing_runs_the_finish_actions_clears_the_drain_then_flushes_the_instance(rig: Rig) -> None:
    player_id = uuid.uuid4()
    await _finisher(rig).finish(player_id, "instance-abc")

    [(actions, ctx)] = rig.ran
    assert actions == tuple(FINISH_ACTIONS)
    assert isinstance(ctx, ScriptedActionContext)
    assert ctx.player is rig.player
    assert rig.order == ["strip", "actions", "clear", "flush"]
    assert rig.stripped == [player_id]  # the amulet does not leave the tutorial with them
    assert rig.cleared == [player_id]  # the instance-scoped drain row does not follow them out
    assert rig.flushed == ["instance-abc"]


@pytest.mark.asyncio
async def test_a_failing_strip_never_stops_the_rest_of_the_finish(rig: Rig) -> None:
    rig.strip_fails = True

    await _finisher(rig).finish(uuid.uuid4(), "instance-abc")

    assert rig.order == ["strip", "actions", "clear", "flush"]


@pytest.mark.asyncio
async def test_without_a_registry_the_strip_is_skipped_and_the_finish_goes_on(rig: Rig) -> None:
    await _finisher(rig, with_registry=False).finish(uuid.uuid4(), "instance-abc")

    assert rig.order == ["actions", "clear", "flush"]


@pytest.mark.asyncio
async def test_a_failing_effect_clear_never_stops_the_instance_being_flushed(rig: Rig) -> None:
    rig.clear_fails = True

    await _finisher(rig).finish(uuid.uuid4(), "instance-abc")

    assert rig.flushed == ["instance-abc"]


@pytest.mark.asyncio
async def test_a_failing_action_never_stops_the_instance_being_flushed(rig: Rig) -> None:
    rig.actions_fail = True

    await _finisher(rig).finish(uuid.uuid4(), "instance-abc")

    assert rig.flushed == ["instance-abc"]


@pytest.mark.asyncio
async def test_a_missing_player_still_flushes_the_instance(rig: Rig) -> None:
    rig.player = None

    await _finisher(rig).finish(uuid.uuid4(), "instance-abc")

    assert rig.ran == []
    assert rig.flushed == ["instance-abc"]


# --- the lazily-resolved finish callable --------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_the_lazy_finish_resolves_its_services_from_the_container_when_called(rig: Rig) -> None:
    container = SimpleNamespace(async_persistence=None, instance_flush_service=None, quest_service=None)
    finish = module.make_first_exposure_finish(container)

    await finish(uuid.uuid4(), "instance-abc")  # services not built yet: skipped quietly
    assert rig.flushed == []

    container.async_persistence = FakePersistence(rig)
    container.instance_flush_service = FakeFlush(rig)
    await finish(uuid.uuid4(), "instance-abc")  # the same callable now finds them
    assert rig.flushed == ["instance-abc"]
    assert rig.stripped == []  # no player registry on the container yet: the strip step is skipped


@pytest.mark.asyncio
async def test_the_lazy_finish_hands_the_containers_player_registry_to_the_finisher(rig: Rig) -> None:
    container = SimpleNamespace(
        async_persistence=FakePersistence(rig),
        instance_flush_service=FakeFlush(rig),
        quest_service=None,
        player_registry=PlayerRegistry(FakeDatabase().session),
    )
    player_id = uuid.uuid4()

    await module.make_first_exposure_finish(container)(player_id, "instance-abc")

    assert rig.stripped == [player_id]
    assert rig.order[0] == "strip"


@pytest.mark.asyncio
async def test_the_restored_lucidity_is_set_in_the_registry_and_the_tier_cache() -> None:
    """The respawn sets lucidity after its commit: 70 and its tier, in the registry and the tier cache."""
    player_id = uuid.uuid4()
    harness = lucidity_registry({player_id: LucidityData(-10, "catatonic")})

    with patch("server.services.lucidity_tier_cache.lucidity_tier_cache.set_tier") as set_tier:
        await restore_first_exposure_lucidity(harness.registry, player_id)

    assert (harness.lucidity(player_id).lcd, harness.lucidity(player_id).tier) == (RESTORED_LCD, resolve_tier(70))
    set_tier.assert_called_once_with(player_id, resolve_tier(70))
