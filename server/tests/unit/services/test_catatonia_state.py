"""Unit tests for player_is_catatonic: the registry first, the stored lucidity as the fallback (#1148)."""

from __future__ import annotations

import uuid
from collections.abc import AsyncIterator
from types import SimpleNamespace
from typing import final

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.services import catatonia_state as state

PLAYER = uuid.uuid4()


@final
class FakeRegistry:
    def __init__(self, catatonic: bool) -> None:
        self.catatonic = catatonic

    def is_catatonic(self, player_id: uuid.UUID | str) -> bool:
        _ = player_id
        return self.catatonic


@final
class FakeSession:
    def __init__(self, record: SimpleNamespace | None, *, fail: bool = False) -> None:
        self.record = record
        self.fail = fail

    async def get(self, model: object, player_id: uuid.UUID) -> SimpleNamespace | None:
        _ = model, player_id
        if self.fail:
            raise SQLAlchemyError("boom")
        return self.record


def _sessions(monkeypatch: pytest.MonkeyPatch, session: FakeSession) -> None:
    async def fake_sessions() -> AsyncIterator[FakeSession]:
        yield session

    monkeypatch.setattr(state, "get_async_session", fake_sessions)


def _record(lcd: int, tier: str) -> SimpleNamespace:
    return SimpleNamespace(current_lcd=lcd, current_tier=tier)


@pytest.mark.asyncio
async def test_the_registry_alone_says_catatonic(monkeypatch: pytest.MonkeyPatch) -> None:
    _sessions(monkeypatch, FakeSession(None, fail=True))  # never reached

    assert await state.player_is_catatonic(SimpleNamespace(catatonia_registry=FakeRegistry(True)), PLAYER) is True


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("record", "expected"),
    [
        (_record(0, "catatonic"), True),
        (_record(-4, "catatonic"), True),
        (_record(0, "deranged"), True),  # LCD <= 0 counts even if the tier column lags
        (_record(5, "catatonic"), True),  # and so does the tier
        (_record(5, "deranged"), False),
        (None, False),
    ],
)
async def test_the_stored_lucidity_is_the_fallback_when_the_registry_is_empty(
    monkeypatch: pytest.MonkeyPatch, record: SimpleNamespace | None, expected: bool
) -> None:
    _sessions(monkeypatch, FakeSession(record))

    assert await state.player_is_catatonic(SimpleNamespace(catatonia_registry=FakeRegistry(False)), PLAYER) is expected


@pytest.mark.asyncio
async def test_a_missing_registry_falls_back_to_the_database(monkeypatch: pytest.MonkeyPatch) -> None:
    _sessions(monkeypatch, FakeSession(_record(-2, "catatonic")))

    assert await state.player_is_catatonic(SimpleNamespace(), PLAYER) is True


@pytest.mark.asyncio
async def test_a_failed_lookup_answers_false_rather_than_locking_the_player_out(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _sessions(monkeypatch, FakeSession(None, fail=True))

    assert await state.player_is_catatonic(SimpleNamespace(), PLAYER) is False
