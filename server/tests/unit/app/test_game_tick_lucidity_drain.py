"""Unit tests for lucidity_drain_over_time: a per-second, accelerating LCD drain that ends at the delirium floor."""

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import cast

import pytest
from pydantic import ValidationError

from server.app import game_tick_lucidity_drain as drain
from server.app import game_tick_status_effects as tick
from server.app.game_tick_protocols import EffectSecond, _TickContainer
from server.game.player_registry import LucidityData, PlayerAggregate
from server.services.lucidity_helpers import decode_liabilities
from server.services.lucidity_service import AppliedAdjustment, LucidityService
from server.tests.fixtures.shared.player_registry import LucidityHarness, lucidity_registry

EFFECT_TYPE = "lucidity_drain_over_time"
ROOM = "room-1"


@dataclass
class Rig:
    harness: LucidityHarness
    pid: uuid.UUID
    narrated: list[str] = field(default_factory=lambda: cast(list[str], []))
    announced: list[AppliedAdjustment] = field(default_factory=lambda: cast(list[AppliedAdjustment], []))
    hallucinated: list[tuple[str, str, str, int]] = field(
        default_factory=lambda: cast(list[tuple[str, str, str, int]], [])
    )
    fail_hallucination: bool = False

    @property
    def lcd(self) -> int:
        return self.harness.lucidity(self.pid).lcd

    async def second(self, effect: dict[str, object]) -> EffectSecond:
        """One second of the drain in its own registry unit, then what it left for after the commit."""
        async with self.harness.registry.mutate(self.pid) as player:
            outcome = drain.drain_second(self.harness.registry, None, player, effect)
        for action in outcome.after:
            await action()
        return outcome

    def deltas(self) -> list[int]:
        return [applied.result.delta for applied in self.announced]


def _make_rig(monkeypatch: pytest.MonkeyPatch, lcd: int) -> Rig:
    pid = uuid.uuid4()
    harness = lucidity_registry({pid: LucidityData(lcd=lcd)}, row={"current_room_id": ROOM})
    rig = Rig(harness, pid)

    async def announce(_self: LucidityService, applied: AppliedAdjustment) -> None:
        rig.announced.append(applied)

    async def fake_deliver(player_id: uuid.UUID | str, message: str) -> dict[str, object]:
        _ = player_id
        rig.narrated.append(message)
        return {}

    def fake_hallucination(kind: str) -> Callable[[uuid.UUID, str, str, int], Awaitable[None]]:
        async def handler(player_id: uuid.UUID, room_id: str, tier: str, current_lcd: int) -> None:
            _ = player_id
            if rig.fail_hallucination:
                raise RuntimeError("delivery failed")
            rig.hallucinated.append((kind, room_id, tier, current_lcd))

        return handler

    hallucinations = "server.services.passive_lucidity_flux.hallucinations"
    monkeypatch.setattr(
        f"{hallucinations}.handle_room_text_overlay_hallucination", fake_hallucination("room_text_overlay")
    )
    monkeypatch.setattr(f"{hallucinations}.handle_phantom_hostile_hallucination", fake_hallucination("phantom_hostile"))
    monkeypatch.setattr(LucidityService, "announce", announce)
    # Authored drain narration is quest content: it goes out on the quest channel.
    monkeypatch.setattr("server.game.chat_npc_system.deliver_personal_quest", fake_deliver)
    return rig


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    return _make_rig(monkeypatch, 100)


def _effect(**params: object) -> dict[str, object]:
    return {"type": EFFECT_TYPE, **params}


@pytest.mark.asyncio
async def test_each_second_drains_the_rate_and_counts_the_second(rig: Rig) -> None:
    outcome = await rig.second(_effect(rate=2))

    assert rig.deltas() == [-2] and rig.lcd == 98
    assert outcome.applied is True
    assert outcome.effect is not None
    assert outcome.effect["elapsed"] == 1


@pytest.mark.asyncio
@pytest.mark.parametrize(("elapsed", "expected_rate"), [(0, 1), (29, 1), (30, 2), (59, 2), (60, 3), (95, 4)])
async def test_the_rate_accelerates_on_schedule(rig: Rig, elapsed: int, expected_rate: int) -> None:
    effect = _effect(rate=1, accelerate_every=30, accelerate_by=1, elapsed=elapsed)

    _ = await rig.second(effect)

    assert rig.deltas() == [-expected_rate]


@pytest.mark.asyncio
async def test_the_last_step_lands_exactly_on_the_floor_and_removes_the_effect(monkeypatch: pytest.MonkeyPatch) -> None:
    rig = _make_rig(monkeypatch, 5)

    outcome = await rig.second(_effect(rate=3, elapsed=0))
    assert (rig.deltas(), outcome.effect, outcome.applied) == (
        [-3],
        {"type": EFFECT_TYPE, "rate": 3, "elapsed": 1},
        True,
    )

    outcome = await rig.second(cast(dict[str, object], outcome.effect))
    assert rig.deltas() == [-3, -3]  # 2 -> -1, not yet at the floor

    rig = _make_rig(monkeypatch, -8)
    outcome = await rig.second(_effect(rate=3, elapsed=9))

    assert rig.deltas() == [-2]  # clamped: -8 + -2 == -10
    assert rig.lcd == -10
    assert outcome.effect is None
    assert outcome.applied is True


@pytest.mark.asyncio
async def test_a_player_already_at_the_floor_just_loses_the_effect(monkeypatch: pytest.MonkeyPatch) -> None:
    rig = _make_rig(monkeypatch, -10)

    outcome = await rig.second(_effect(rate=3))

    assert (outcome.effect, outcome.applied, rig.deltas()) == (None, False, [])


@pytest.mark.asyncio
async def test_the_floor_is_configurable(monkeypatch: pytest.MonkeyPatch) -> None:
    rig = _make_rig(monkeypatch, 3)

    outcome = await rig.second(_effect(rate=9, floor=0))

    assert rig.lcd == 0
    assert outcome.effect is None


@pytest.mark.asyncio
async def test_the_lcd_loss_is_made_in_the_callers_unit_and_announced_only_after_it(rig: Rig) -> None:
    async with rig.harness.registry.mutate(rig.pid) as player:
        outcome = drain.drain_second(rig.harness.registry, None, player, _effect(rate=2))
        assert rig.announced == []  # nothing is sent for a second that may still roll back
        assert player.lucidity.lcd == 98
    for action in outcome.after:
        await action()

    assert len(rig.announced) == 1


@pytest.mark.asyncio
async def test_narration_is_sent_once_on_its_second(rig: Rig) -> None:
    narration = [{"at": 1, "text": "The baying starts."}, {"at": 5, "text": "Closer."}]

    _ = await rig.second(_effect(narration=narration, elapsed=0))
    assert rig.narrated == []
    _ = await rig.second(_effect(narration=narration, elapsed=1))
    assert rig.narrated == ["The baying starts."]
    _ = await rig.second(_effect(narration=narration, elapsed=2))

    assert rig.narrated == ["The baying starts."]


@pytest.mark.asyncio
async def test_liabilities_are_suppressed_only_when_the_effect_says_so(monkeypatch: pytest.MonkeyPatch) -> None:
    suppressing = _make_rig(monkeypatch, 100)
    _ = await suppressing.second(_effect(rate=20, grants_liabilities=False))
    granting = _make_rig(monkeypatch, 100)
    _ = await granting.second(_effect(rate=20))

    assert decode_liabilities(suppressing.harness.lucidity(suppressing.pid).liabilities) == []
    assert decode_liabilities(granting.harness.lucidity(granting.pid).liabilities) != []


@pytest.mark.asyncio
async def test_a_malformed_effect_is_dropped_rather_than_retried_forever(rig: Rig) -> None:
    outcome = await rig.second(_effect(rate=0))

    assert (outcome.effect, outcome.applied, rig.deltas()) == (None, False, [])


# --- wiring into the tick -----------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_the_tick_routes_a_drain_effect_to_the_drain(monkeypatch: pytest.MonkeyPatch) -> None:
    """process_status_effects only runs effects on game seconds (test_game_tick_status_effects.py)."""
    calls: list[dict[str, object]] = []

    def fake_drain(
        registry: object, observer: object, player: PlayerAggregate, effect: dict[str, object]
    ) -> EffectSecond:
        _ = registry, observer, player
        calls.append(effect)
        return EffectSecond({**effect, "elapsed": 1}, True)

    monkeypatch.setattr(tick, "drain_second", fake_drain)
    harness = lucidity_registry({(pid := uuid.uuid4()): None})
    effect = _effect(rate=1)

    async with harness.registry.mutate(pid) as player:
        outcome = tick._run_effect_second(cast(_TickContainer, object()), harness.registry, player, effect)

    assert outcome == EffectSecond({**effect, "elapsed": 1}, True)
    assert calls == [effect]


# --- scripted hallucination beats (#1096) -------------------------------------------------------------------------

BEATS = [{"at": 1, "kind": "room_text_overlay"}, {"at": 3, "kind": "phantom_hostile"}]


@pytest.mark.asyncio
async def test_each_hallucination_beat_fires_once_on_its_second(monkeypatch: pytest.MonkeyPatch) -> None:
    rig = _make_rig(monkeypatch, 30)

    for elapsed in range(6):
        _ = await rig.second(_effect(hallucinations=BEATS, elapsed=elapsed))

    # LCD after each step is 29, 28, 27, 26, ...: the overlay at second 1, the phantom at second 3, nothing else.
    assert rig.hallucinated == [
        ("room_text_overlay", ROOM, "fractured", 28),
        ("phantom_hostile", ROOM, "fractured", 26),
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("lcd_before", "tier"), [(100, "lucid"), (50, "uneasy"), (30, "fractured"), (10, "deranged"), (0, "catatonic")]
)
async def test_the_beat_uses_the_tier_of_the_players_lcd_right_now(
    monkeypatch: pytest.MonkeyPatch, lcd_before: int, tier: str
) -> None:
    rig = _make_rig(monkeypatch, lcd_before)

    _ = await rig.second(_effect(hallucinations=[{"at": 0, "kind": "phantom_hostile"}]))

    assert rig.hallucinated == [("phantom_hostile", ROOM, tier, lcd_before - 1)]


@pytest.mark.asyncio
async def test_no_beat_fires_once_the_player_is_at_the_floor(monkeypatch: pytest.MonkeyPatch) -> None:
    rig = _make_rig(monkeypatch, -10)

    outcome = await rig.second(_effect(hallucinations=[{"at": 0, "kind": "room_text_overlay"}]))

    assert (outcome.effect, outcome.applied, rig.hallucinated) == (None, False, [])


@pytest.mark.asyncio
async def test_a_beat_after_the_drain_ends_never_fires(monkeypatch: pytest.MonkeyPatch) -> None:
    rig = _make_rig(monkeypatch, 3)
    effect: dict[str, object] | None = _effect(hallucinations=[{"at": 99, "kind": "room_text_overlay"}])

    while effect is not None:
        effect = (await rig.second(effect)).effect

    assert rig.lcd == -10
    assert rig.hallucinated == []


@pytest.mark.asyncio
async def test_a_failing_hallucination_is_skipped_and_the_drain_still_advances(rig: Rig) -> None:
    rig.fail_hallucination = True

    outcome = await rig.second(_effect(hallucinations=[{"at": 0, "kind": "phantom_hostile"}]))

    assert rig.deltas() == [-1]  # applied exactly once: a retry would drain this second twice
    assert (outcome.applied, outcome.effect is not None and outcome.effect["elapsed"]) == (True, 1)


def test_unknown_hallucination_kinds_are_rejected_at_validation() -> None:
    with pytest.raises(ValidationError):
        _ = drain.LucidityDrainParams.model_validate({"hallucinations": [{"at": 5, "kind": "fake_npc_tell"}]})
    with pytest.raises(ValidationError):
        _ = drain.LucidityDrainParams.model_validate({"hallucinations": [{"at": -1, "kind": "room_text_overlay"}]})


@pytest.mark.asyncio
async def test_a_drain_with_an_unknown_kind_is_dropped_like_any_malformed_effect(rig: Rig) -> None:
    outcome = await rig.second(_effect(hallucinations=[{"at": 0, "kind": "fake_npc_tell"}]))

    assert (outcome.effect, outcome.applied, rig.deltas(), rig.hallucinated) == (None, False, [], [])
