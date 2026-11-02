"""Unit tests for player_is_catatonic: the catatonia registry first, the player's lucidity as the fallback (#1148)."""

from __future__ import annotations

import uuid
from types import SimpleNamespace
from typing import final

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.game.player_registry import LucidityData
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
class FakePlayers:
    """The player registry's ``get``: the player's lucidity, no such player (None), or a failed lookup."""

    def __init__(self, lucidity: LucidityData | None, *, fail: bool = False) -> None:
        self.lucidity = lucidity
        self.fail = fail

    async def get(self, player_id: uuid.UUID) -> SimpleNamespace | None:
        _ = player_id
        if self.fail:
            raise SQLAlchemyError("boom")
        return None if self.lucidity is None else SimpleNamespace(lucidity=SimpleNamespace(data=self.lucidity))


def _state(players: FakePlayers | None, catatonia: FakeRegistry | None = None) -> SimpleNamespace:
    return SimpleNamespace(catatonia_registry=catatonia, container=SimpleNamespace(player_registry=players))


def _record(lcd: int, tier: str) -> LucidityData:
    return LucidityData(lcd, tier)


@pytest.mark.asyncio
async def test_the_registry_alone_says_catatonic() -> None:
    assert await state.player_is_catatonic(_state(FakePlayers(None, fail=True), FakeRegistry(True)), PLAYER) is True


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
async def test_the_players_lucidity_is_the_fallback_when_the_catatonia_registry_is_empty(
    record: LucidityData | None, expected: bool
) -> None:
    assert await state.player_is_catatonic(_state(FakePlayers(record), FakeRegistry(False)), PLAYER) is expected


@pytest.mark.asyncio
async def test_a_missing_catatonia_registry_falls_back_to_the_players_lucidity() -> None:
    assert await state.player_is_catatonic(_state(FakePlayers(_record(-2, "catatonic"))), PLAYER) is True


@pytest.mark.asyncio
async def test_no_player_registry_answers_false() -> None:
    assert await state.player_is_catatonic(SimpleNamespace(), PLAYER) is False


@pytest.mark.asyncio
async def test_a_failed_lookup_answers_false_rather_than_locking_the_player_out() -> None:
    assert await state.player_is_catatonic(_state(FakePlayers(None, fail=True)), PLAYER) is False
