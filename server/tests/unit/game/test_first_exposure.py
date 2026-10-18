"""The First Exposure ending: what a tutorial delirium respawn leaves the player with (ADR-028, #1080)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest

from server.constants.spawn_defaults import RECOVERY_WARD_ROOM_ID
from server.game import first_exposure as module
from server.game.first_exposure import (
    EPILOGUE_QUEST_ID,
    FINISH_ACTIONS,
    RESTORED_LCD,
    FirstExposureFinisher,
    apply_first_exposure_end_state,
)
from server.game.instance_state import INSTANCE_SCOPED_EFFECT_KEY
from server.game.items.constants import INSTANCE_BOUND_FLAG
from server.game.scripted_actions import QuestActionService, ScriptedActionContext
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.schemas.scripted_actions import CorruptionAtLeastAction, StartQuestAction, parse_scripted_actions
from server.services.lucidity_service import resolve_tier


def _stack(item_id: str, *flags: str) -> dict[str, object]:
    stack: dict[str, object] = {"item_id": item_id, "prototype_id": item_id, "quantity": 1}
    if flags:
        stack["flags"] = list(flags)
    return stack


def _tutorial_player(instance_id: str | None = "instance-abc") -> tuple[Player, PlayerLucidity]:
    player = Player(player_id=str(uuid.uuid4()), name="Tester")
    player.current_room_id = f"instance_{uuid.uuid4()}_vault"
    player.tutorial_instance_id = instance_id
    player.set_stats({"current_dp": 1, "max_dp": 100})
    player.set_inventory([_stack("lantern"), _stack("jade_amulet", INSTANCE_BOUND_FLAG)])
    player.set_status_effects(
        [
            {"type": "lucidity_drain_over_time", INSTANCE_SCOPED_EFFECT_KEY: True},
            {"type": "heal_over_time", "healing": 1},
        ]
    )
    lucidity = PlayerLucidity(player_id=player.player_id, current_lcd=-10, current_tier="delirious", liabilities="[]")
    return player, lucidity


# --- the in-session end state -----------------------------------------------------------------------------------


def test_the_end_state_leaves_a_tutorial_player_whole_and_in_the_ward() -> None:
    player, lucidity = _tutorial_player()

    applied = apply_first_exposure_end_state(player, lucidity)

    assert applied is True
    assert player.current_room_id == RECOVERY_WARD_ROOM_ID
    assert player.tutorial_instance_id is None
    assert lucidity.current_lcd == RESTORED_LCD == 70
    assert lucidity.current_tier == resolve_tier(70)
    assert player.get_stats()["current_dp"] == player.get_stats()["max_dp"]


def test_the_end_state_takes_the_amulet_and_the_drain_but_keeps_everything_else() -> None:
    player, lucidity = _tutorial_player()

    _ = apply_first_exposure_end_state(player, lucidity)

    assert [stack["item_id"] for stack in player.get_inventory()] == ["lantern"]
    assert [effect["type"] for effect in player.get_status_effects()] == ["heal_over_time"]


def test_the_end_state_does_nothing_for_a_player_who_is_not_in_the_tutorial() -> None:
    player, lucidity = _tutorial_player(instance_id=None)
    room_before = player.current_room_id

    applied = apply_first_exposure_end_state(player, lucidity)

    assert applied is False
    assert lucidity.current_lcd == -10
    assert player.current_room_id == room_before
    assert len(player.get_inventory()) == 2


def test_the_end_state_is_idempotent() -> None:
    player, lucidity = _tutorial_player()

    _ = apply_first_exposure_end_state(player, lucidity)
    second = apply_first_exposure_end_state(player, lucidity)

    assert second is False  # tutorial_instance_id is cleared, so a replay finds nothing to do
    assert lucidity.current_lcd == 70


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


class FakePersistence:
    _rig: Rig

    def __init__(self, rig: Rig) -> None:
        self._rig = rig

    async def get_player_by_id(self, player_id: uuid.UUID) -> Player | None:
        _ = player_id
        return self._rig.player

    async def save_player(self, player: object) -> None:  # pragma: no cover - the runner is faked
        _ = player


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
    rig = Rig(_tutorial_player()[0])

    async def fake_run(actions: tuple[object, ...], ctx: object) -> None:
        rig.order.append("actions")
        if rig.actions_fail:
            raise RuntimeError("quest store down")
        rig.ran.append((tuple(actions), ctx))

    monkeypatch.setattr(module, "run_scripted_actions", fake_run)
    return rig


def _finisher(rig: Rig) -> FirstExposureFinisher:
    return FirstExposureFinisher(
        persistence=cast(module.FinishPersistence, FakePersistence(rig)),
        quest_service=cast(QuestActionService, cast(object, SimpleNamespace())),
        flush=cast(module.InstanceFlush, FakeFlush(rig)),
    )


@pytest.mark.asyncio
async def test_finishing_runs_the_finish_actions_for_the_player_then_flushes_the_instance(rig: Rig) -> None:
    await _finisher(rig).finish(uuid.uuid4(), "instance-abc")

    [(actions, ctx)] = rig.ran
    assert actions == tuple(FINISH_ACTIONS)
    assert isinstance(ctx, ScriptedActionContext)
    assert ctx.player is rig.player
    assert rig.order == ["actions", "flush"]
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
