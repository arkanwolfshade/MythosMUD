"""Unit tests for lucidity_drain_over_time: a per-second, accelerating LCD drain that ends at the delirium floor."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator, Callable
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast

import pytest
from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from server.app import game_tick_lucidity_drain as drain
from server.app import game_tick_status_effects as tick
from server.app.game_tick_protocols import _TickContainer
from server.models.player import Player

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
    fail: bool = False


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

    monkeypatch.setattr(drain, "get_async_session", fake_sessions)
    monkeypatch.setattr(drain, "LucidityService", FakeLucidityService)
    # Authored drain narration is quest content: it goes out on the quest channel.
    monkeypatch.setattr("server.game.chat_npc_system.deliver_personal_quest", fake_deliver)
    return rig


def _player() -> Player:
    return Player(player_id=str(uuid.uuid4()), name="Tester")


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
