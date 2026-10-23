"""Unit tests for lucidity_drain_over_time: a per-second, accelerating LCD drain that ends at the delirium floor."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator, Awaitable, Callable
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest
from fastapi import FastAPI
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from server.app import game_tick_lucidity_drain as drain
from server.app import game_tick_status_effects as tick
from server.app.game_tick_protocols import _TickContainer
from server.models.player import Player
from server.services.lucidity_repository import PlayerGoneError

EFFECT_TYPE = "lucidity_drain_over_time"


@dataclass
class FakeSession:
    commits: int = 0

    async def commit(self) -> None:
        self.commits += 1


@dataclass
class Rig:
    lcd: int
    session: FakeSession = field(default_factory=FakeSession)
    deltas: list[int] = field(default_factory=lambda: cast(list[int], []))
    narrated: list[str] = field(default_factory=lambda: cast(list[str], []))
    picker_kwargs: list[object] = field(default_factory=lambda: cast(list[object], []))
    hallucinated: list[tuple[str, str, str, int]] = field(
        default_factory=lambda: cast(list[tuple[str, str, str, int]], [])
    )
    fail: bool = False
    gone: bool = False
    fail_hallucination: bool = False


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    rig = Rig(lcd=100)

    async def fake_sessions() -> AsyncIterator[FakeSession]:
        yield rig.session

    class FakeLucidityService:
        def __init__(
            self,
            session: FakeSession,
            liability_picker: Callable[..., str | None] | None = None,
            *,
            catatonia_observer: object | None = None,
        ) -> None:
            _ = session, catatonia_observer
            rig.picker_kwargs.append(liability_picker)

        async def get_player_lucidity(self, player_id: uuid.UUID) -> SimpleNamespace:
            _ = player_id
            if rig.fail:
                raise SQLAlchemyError("database unavailable")
            if rig.gone:
                raise PlayerGoneError(str(player_id))
            return SimpleNamespace(current_lcd=rig.lcd)

        async def apply_lucidity_adjustment(
            self, player_id: uuid.UUID, delta: int, *, reason_code: str, location_id: str | None = None
        ) -> SimpleNamespace:
            _ = player_id, reason_code, location_id
            rig.deltas.append(delta)
            rig.lcd += delta
            return SimpleNamespace(new_lcd=rig.lcd)

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
    monkeypatch.setattr(drain, "get_async_session", fake_sessions)
    monkeypatch.setattr(drain, "LucidityService", FakeLucidityService)
    # Authored drain narration is quest content: it goes out on the quest channel.
    monkeypatch.setattr("server.game.chat_npc_system.deliver_personal_quest", fake_deliver)
    return rig


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


def _player_in_room() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester", current_room_id="room-1")


def _container() -> _TickContainer:
    return cast(_TickContainer, cast(object, SimpleNamespace()))


def _effect(**params: object) -> dict[str, object]:
    return {"type": EFFECT_TYPE, **params}


@pytest.mark.asyncio
async def test_each_second_drains_the_rate_and_counts_the_second(rig: Rig) -> None:
    updated, applied = await drain.process_lucidity_drain(_container(), _player(), _effect(rate=2))

    assert rig.deltas == [-2]
    assert applied is True
    assert updated is not None
    assert updated["elapsed"] == 1
    assert rig.session.commits == 1


@pytest.mark.asyncio
@pytest.mark.parametrize(("elapsed", "expected_rate"), [(0, 1), (29, 1), (30, 2), (59, 2), (60, 3), (95, 4)])
async def test_the_rate_accelerates_on_schedule(rig: Rig, elapsed: int, expected_rate: int) -> None:
    effect = _effect(rate=1, accelerate_every=30, accelerate_by=1, elapsed=elapsed)

    _ = await drain.process_lucidity_drain(_container(), _player(), effect)

    assert rig.deltas == [-expected_rate]


@pytest.mark.asyncio
async def test_the_last_step_lands_exactly_on_the_floor_and_removes_the_effect(rig: Rig) -> None:
    rig.lcd = 5

    updated, applied = await drain.process_lucidity_drain(_container(), _player(), _effect(rate=3, elapsed=0))
    assert (rig.deltas, updated, applied) == ([-3], {"type": EFFECT_TYPE, "rate": 3, "elapsed": 1}, True)

    updated, applied = await drain.process_lucidity_drain(_container(), _player(), cast(dict[str, object], updated))
    assert rig.deltas == [-3, -3]  # 2 -> -1, not yet at the floor

    rig.lcd = -8
    updated, applied = await drain.process_lucidity_drain(_container(), _player(), _effect(rate=3, elapsed=9))

    assert rig.deltas[-1] == -2  # clamped: -8 + -2 == -10
    assert rig.lcd == -10
    assert updated is None
    assert applied is True


@pytest.mark.asyncio
async def test_a_player_already_at_the_floor_just_loses_the_effect(rig: Rig) -> None:
    rig.lcd = -10

    updated, applied = await drain.process_lucidity_drain(_container(), _player(), _effect(rate=3))

    assert (updated, applied, rig.deltas) == (None, False, [])


@pytest.mark.asyncio
async def test_a_deleted_player_is_a_quiet_no_op(rig: Rig) -> None:
    """#1147: the player vanished mid-drain; no write, no commit, and the effect is left for the tick to discard."""
    rig.gone = True
    effect = _effect(rate=3)

    updated, applied = await drain.process_lucidity_drain(_container(), _player(), effect)

    assert (updated, applied) == (effect, False)
    assert rig.deltas == []
    assert rig.session.commits == 0


@pytest.mark.asyncio
async def test_the_floor_is_configurable(rig: Rig) -> None:
    rig.lcd = 3

    updated, _ = await drain.process_lucidity_drain(_container(), _player(), _effect(rate=9, floor=0))

    assert rig.lcd == 0
    assert updated is None


@pytest.mark.asyncio
async def test_narration_is_sent_once_on_its_second(rig: Rig) -> None:
    narration = [{"at": 1, "text": "The baying starts."}, {"at": 5, "text": "Closer."}]

    _ = await drain.process_lucidity_drain(_container(), _player(), _effect(narration=narration, elapsed=0))
    assert rig.narrated == []
    _ = await drain.process_lucidity_drain(_container(), _player(), _effect(narration=narration, elapsed=1))
    assert rig.narrated == ["The baying starts."]
    _ = await drain.process_lucidity_drain(_container(), _player(), _effect(narration=narration, elapsed=2))

    assert rig.narrated == ["The baying starts."]


@pytest.mark.asyncio
async def test_liabilities_are_suppressed_only_when_the_effect_says_so(rig: Rig) -> None:
    _ = await drain.process_lucidity_drain(_container(), _player(), _effect(grants_liabilities=False))
    _ = await drain.process_lucidity_drain(_container(), _player(), _effect())

    suppressing, default = rig.picker_kwargs
    assert callable(suppressing)
    assert suppressing("player", 50, 40, "reason") is None
    assert default is None


@pytest.mark.asyncio
async def test_a_database_failure_keeps_the_effect_for_the_next_second(rig: Rig) -> None:
    rig.fail = True
    effect = _effect(rate=2, elapsed=7)

    updated, applied = await drain.process_lucidity_drain(_container(), _player(), effect)

    assert (updated, applied, rig.deltas) == (effect, False, [])


@pytest.mark.asyncio
async def test_a_malformed_effect_is_dropped_rather_than_retried_forever(rig: Rig) -> None:
    updated, applied = await drain.process_lucidity_drain(_container(), _player(), _effect(rate=0))

    assert (updated, applied, rig.deltas) == (None, False, [])


# --- wiring into the tick -----------------------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_the_tick_runs_the_drain_only_on_game_seconds(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[dict[str, object]] = []

    async def fake_process(
        container: _TickContainer, player: Player, effect: dict[str, object]
    ) -> tuple[dict[str, object] | None, bool]:
        _ = container, player
        calls.append(effect)
        return {**effect, "elapsed": 1}, True

    monkeypatch.setattr(tick, "process_lucidity_drain", fake_process)
    app = cast(FastAPI, object())
    effect = _effect(rate=1)

    between = await tick._process_single_effect(app, _container(), _player(), effect, "p", second_tick=False)
    on_second = await tick._process_single_effect(app, _container(), _player(), effect, "p", second_tick=True)

    assert between == (effect, False)
    assert on_second == ({**effect, "elapsed": 1}, True)
    assert calls == [effect]


# --- scripted hallucination beats (#1096) -------------------------------------------------------------------------

BEATS = [{"at": 1, "kind": "room_text_overlay"}, {"at": 3, "kind": "phantom_hostile"}]


@pytest.mark.asyncio
async def test_each_hallucination_beat_fires_once_on_its_second(rig: Rig) -> None:
    rig.lcd = 30
    player = _player_in_room()

    for elapsed in range(6):
        _ = await drain.process_lucidity_drain(_container(), player, _effect(hallucinations=BEATS, elapsed=elapsed))

    # LCD after each step is 29, 28, 27, 26, ...: the overlay at second 1, the phantom at second 3, nothing else.
    assert rig.hallucinated == [
        ("room_text_overlay", "room-1", "fractured", 28),
        ("phantom_hostile", "room-1", "fractured", 26),
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("lcd_before", "tier"), [(100, "lucid"), (50, "uneasy"), (30, "fractured"), (10, "deranged"), (0, "catatonic")]
)
async def test_the_beat_uses_the_tier_of_the_players_lcd_right_now(rig: Rig, lcd_before: int, tier: str) -> None:
    rig.lcd = lcd_before

    _ = await drain.process_lucidity_drain(
        _container(), _player_in_room(), _effect(hallucinations=[{"at": 0, "kind": "phantom_hostile"}])
    )

    assert rig.hallucinated == [("phantom_hostile", "room-1", tier, lcd_before - 1)]


@pytest.mark.asyncio
async def test_no_beat_fires_once_the_player_is_at_the_floor(rig: Rig) -> None:
    rig.lcd = -10

    updated, applied = await drain.process_lucidity_drain(
        _container(), _player_in_room(), _effect(hallucinations=[{"at": 0, "kind": "room_text_overlay"}])
    )

    assert (updated, applied, rig.hallucinated) == (None, False, [])


@pytest.mark.asyncio
async def test_a_beat_after_the_drain_ends_never_fires(rig: Rig) -> None:
    rig.lcd = 3
    effect: dict[str, object] | None = _effect(hallucinations=[{"at": 99, "kind": "room_text_overlay"}])

    while effect is not None:
        effect, _applied = await drain.process_lucidity_drain(_container(), _player_in_room(), effect)

    assert rig.lcd == -10
    assert rig.hallucinated == []


@pytest.mark.asyncio
async def test_a_failed_database_step_fires_no_beat_and_retries_the_same_second(rig: Rig) -> None:
    rig.fail = True
    effect = _effect(hallucinations=[{"at": 0, "kind": "room_text_overlay"}])

    updated, applied = await drain.process_lucidity_drain(_container(), _player_in_room(), effect)

    assert (updated, applied, rig.hallucinated) == (effect, False, [])


@pytest.mark.asyncio
async def test_a_player_without_a_room_skips_the_beat_but_the_drain_advances(rig: Rig) -> None:
    updated, applied = await drain.process_lucidity_drain(
        _container(), _player(), _effect(hallucinations=[{"at": 0, "kind": "room_text_overlay"}])
    )

    assert rig.hallucinated == []
    assert (applied, updated is not None and updated["elapsed"]) == (True, 1)


@pytest.mark.asyncio
async def test_a_failing_hallucination_is_skipped_and_the_drain_still_advances(rig: Rig) -> None:
    rig.fail_hallucination = True

    updated, applied = await drain.process_lucidity_drain(
        _container(), _player_in_room(), _effect(hallucinations=[{"at": 0, "kind": "phantom_hostile"}])
    )

    assert rig.deltas == [-1]  # applied exactly once: a retry would drain this second twice
    assert (applied, updated is not None and updated["elapsed"]) == (True, 1)


def test_unknown_hallucination_kinds_are_rejected_at_validation() -> None:
    with pytest.raises(ValidationError):
        _ = drain.LucidityDrainParams.model_validate({"hallucinations": [{"at": 5, "kind": "fake_npc_tell"}]})
    with pytest.raises(ValidationError):
        _ = drain.LucidityDrainParams.model_validate({"hallucinations": [{"at": -1, "kind": "room_text_overlay"}]})


@pytest.mark.asyncio
async def test_a_drain_with_an_unknown_kind_is_dropped_like_any_malformed_effect(rig: Rig) -> None:
    updated, applied = await drain.process_lucidity_drain(
        _container(), _player_in_room(), _effect(hallucinations=[{"at": 0, "kind": "fake_npc_tell"}])
    )

    assert (updated, applied, rig.deltas, rig.hallucinated) == (None, False, [], [])
