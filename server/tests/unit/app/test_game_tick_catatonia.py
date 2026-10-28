"""Unit tests for the catatonia clock: catatonic players lose LCD on an interval until delirium's floor (#1148)."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import cast, final
from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.app import game_tick_catatonia as clock
from server.app.game_tick_protocols import _TickContainer

PLAYER_A = uuid.uuid4()
PLAYER_B = uuid.uuid4()


@dataclass
class FakeResult:
    ids: list[uuid.UUID]

    def scalars(self) -> FakeResult:
        return self

    def all(self) -> list[uuid.UUID]:
        return self.ids


@dataclass
class Rig:
    lcds: dict[uuid.UUID, int]
    commits: int = 0
    rollbacks: int = 0
    queries: int = 0
    adjustments: list[tuple[uuid.UUID, int, str]] = field(
        default_factory=lambda: cast(list[tuple[uuid.UUID, int, str]], [])
    )
    fail_query: bool = False


@pytest.fixture(name="rig")
def _rig(monkeypatch: pytest.MonkeyPatch) -> Rig:
    rig = Rig(lcds={PLAYER_A: 0})

    class FakeLucidityService:
        def __init__(self, session: object, *, catatonia_observer: object | None = None) -> None:
            _ = session, catatonia_observer

        async def get_player_lucidity(self, player_id: uuid.UUID) -> SimpleNamespace:
            return SimpleNamespace(current_lcd=rig.lcds[player_id])

        async def apply_lucidity_adjustment(self, player_id: uuid.UUID, delta: int, *, reason_code: str) -> None:
            rig.adjustments.append((player_id, delta, reason_code))
            rig.lcds[player_id] += delta

    monkeypatch.setattr(clock, "LucidityService", FakeLucidityService)
    return rig


@final
class FakeSession:
    def __init__(self, rig: Rig) -> None:
        self.rig = rig

    async def execute(self, _statement: object) -> FakeResult:
        self.rig.queries += 1
        if self.rig.fail_query:
            raise SQLAlchemyError("boom")
        return FakeResult(list(self.rig.lcds))

    async def commit(self) -> None:
        self.rig.commits += 1

    async def rollback(self) -> None:
        self.rig.rollbacks += 1


async def _run(rig: Rig, tick_count: int = 0) -> None:
    container = cast(_TickContainer, cast(object, SimpleNamespace()))
    await clock.process_catatonia_decay(container, cast(AsyncSession, cast(object, FakeSession(rig))), tick_count)


def _config(interval: float, tick_rate: float) -> SimpleNamespace:
    return SimpleNamespace(game=SimpleNamespace(catatonia_decay_interval_seconds=interval, server_tick_rate=tick_rate))


@pytest.mark.parametrize(
    ("interval", "tick_rate", "tick_count", "due"),
    [
        (2.0, 0.1, 0, True),
        (2.0, 0.1, 10, False),  # one game second in: not yet
        (2.0, 0.1, 20, True),
        (2.0, 0.1, 21, False),
        (2.0, 0.5, 4, True),  # a slower tick rate still lands on the interval
        (2.0, 0.5, 2, False),
        (0.01, 0.1, 3, True),  # an interval below one tick runs every tick
    ],
)
def test_the_clock_is_due_on_the_configured_interval(interval: float, tick_rate: float, tick_count: int, due: bool):
    with patch.object(clock, "get_config", return_value=_config(interval, tick_rate)):
        assert clock.is_catatonia_decay_tick(tick_count) is due


@pytest.mark.asyncio
async def test_a_due_tick_takes_one_lcd_with_the_decay_reason(rig: Rig):
    rig.lcds = {PLAYER_A: 0, PLAYER_B: -4}
    with patch.object(clock, "is_catatonia_decay_tick", return_value=True):
        await _run(rig)

    assert rig.adjustments == [
        (PLAYER_A, -1, clock.CATATONIA_DECAY_REASON_CODE),
        (PLAYER_B, -1, clock.CATATONIA_DECAY_REASON_CODE),
    ]
    assert rig.lcds == {PLAYER_A: -1, PLAYER_B: -5}
    assert rig.commits == 1


@pytest.mark.asyncio
async def test_a_tick_that_is_not_due_does_nothing(rig: Rig):
    with patch.object(clock, "is_catatonia_decay_tick", return_value=False):
        await _run(rig)

    assert (rig.queries, rig.adjustments, rig.commits) == (0, [], 0)


@pytest.mark.asyncio
@pytest.mark.parametrize("lcd", [1, 40, clock.DELIRIUM_LCD, -15])
async def test_a_player_who_left_the_band_since_the_query_is_left_alone(rig: Rig, lcd: int):
    rig.lcds = {PLAYER_A: lcd}  # a tonic or /ground raised it, or a drain already reached the floor
    with patch.object(clock, "is_catatonia_decay_tick", return_value=True):
        await _run(rig)

    assert rig.adjustments == []
    assert rig.lcds == {PLAYER_A: lcd}


@pytest.mark.asyncio
async def test_the_last_step_lands_on_the_floor_and_the_next_tick_leaves_it(rig: Rig):
    rig.lcds = {PLAYER_A: clock.DELIRIUM_LCD + 1}
    with patch.object(clock, "is_catatonia_decay_tick", return_value=True):
        await _run(rig)
        await _run(rig)

    assert rig.lcds == {PLAYER_A: clock.DELIRIUM_LCD}
    assert len(rig.adjustments) == 1


@pytest.mark.asyncio
async def test_nobody_catatonic_commits_nothing(rig: Rig):
    rig.lcds = {}
    with patch.object(clock, "is_catatonia_decay_tick", return_value=True):
        await _run(rig)

    assert (rig.queries, rig.commits) == (1, 0)


@pytest.mark.asyncio
async def test_a_database_failure_rolls_the_shared_session_back_and_does_not_raise(rig: Rig):
    rig.fail_query = True
    with patch.object(clock, "is_catatonia_decay_tick", return_value=True):
        await _run(rig)

    assert (rig.rollbacks, rig.commits, rig.adjustments) == (1, 0, [])
