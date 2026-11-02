"""Unit tests for the lucidity part: defaults, lazy changes, ledger rows written with the row, rollback, retry."""

from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Mapping, Sequence
from contextlib import asynccontextmanager
from datetime import UTC, datetime

from server.constants.lucidity import STARTING_LCD
from server.game.player_registry import (
    DbSession,
    LucidityData,
    PlayerAggregate,
    PlayerLucidityPart,
    PlayerRegistry,
    load_player_aggregate,
)
from server.game.player_registry.player_lucidity import (
    ADD_ADJUSTMENT_LOG_SQL,
    LOAD_LUCIDITY_SQL,
    UPSERT_LUCIDITY_SQL,
)
from server.game.player_registry.player_quests import LIST_QUEST_INSTANCES_SQL

from .fakes import aggregate, raw_row

T0 = datetime(2026, 10, 30, 12, 0, tzinfo=UTC)


class _RecordingSession:
    """Records (statement, params) pairs; ``fail_commits`` makes that many commits raise."""

    def __init__(self, log: list[tuple[object, Mapping[str, object] | None]], fail: list[bool]) -> None:
        self._log: list[tuple[object, Mapping[str, object] | None]] = log
        self._fail: list[bool] = fail

    async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> _RecordingSession:
        self._log.append((statement, params))
        return self

    def mappings(self) -> _RecordingSession:
        return self

    def first(self) -> Mapping[str, object] | None:
        return None

    def all(self) -> Sequence[Mapping[str, object]]:
        return []

    async def commit(self) -> None:
        if self._fail and self._fail.pop(0):
            raise RuntimeError("database unavailable")

    async def rollback(self) -> None:
        return None


def test_a_player_without_a_row_has_the_starting_values() -> None:
    assert LucidityData.from_row(None) == LucidityData(STARTING_LCD, "lucid", "[]", None, None)
    assert PlayerLucidityPart(uuid.uuid4()).lcd == STARTING_LCD


def test_from_row_reads_every_column() -> None:
    stacks = '[{"code": "ethereal_chill", "stacks": 2}]'
    row = {
        "current_lcd": 12,
        "current_tier": "deranged",
        "liabilities": stacks,
        "catatonia_entered_at": None,
        "last_updated_at": T0,
    }
    assert LucidityData.from_row(row) == LucidityData(12, "deranged", stacks, None, T0)


def test_set_is_lazy_and_stamps_the_change() -> None:
    part = PlayerLucidityPart(uuid.uuid4())

    data = part.set(lcd=40, tier="uneasy")

    assert (data.lcd, data.tier) == (40, "uneasy") and data.last_updated_at is not None
    assert part.dirty and not part.sync_required


def test_an_unchanged_set_is_not_dirty() -> None:
    part = PlayerLucidityPart(uuid.uuid4())

    _ = part.set(lcd=STARTING_LCD, tier="lucid")

    assert not part.dirty


def test_set_keeps_catatonia_unless_cleared() -> None:
    part = PlayerLucidityPart(uuid.uuid4(), LucidityData(0, "catatonic", catatonia_entered_at=T0))

    assert part.set(lcd=-1).catatonia_entered_at == T0
    assert part.set(lcd=5, tier="deranged", clear_catatonia=True).catatonia_entered_at is None


def test_rollback_drops_the_change_and_its_ledger_row() -> None:
    part = PlayerLucidityPart(uuid.uuid4())
    part.begin()
    _ = part.set(lcd=10, tier="deranged")
    part.log(-90, "test", "{}", None)
    part.rollback()

    assert part.lcd == STARTING_LCD and not part.dirty
    assert part.take_write() is None


async def test_a_write_upserts_the_row_and_appends_every_ledger_row_in_one_transaction() -> None:
    player_id = uuid.uuid4()
    part = PlayerLucidityPart(player_id)
    _ = part.set(lcd=90, tier="lucid")
    part.log(-6, "encounter_disturbing", '{"a": 1}', "room_1")
    part.log(-4, "passive_flux", "{}", None)
    write = part.take_write()
    assert write is not None and not part.dirty

    log: list[tuple[object, Mapping[str, object] | None]] = []
    await write(_RecordingSession(log, []))

    assert [statement for statement, _params in log] == [
        UPSERT_LUCIDITY_SQL,
        ADD_ADJUSTMENT_LOG_SQL,
        ADD_ADJUSTMENT_LOG_SQL,
    ]
    upsert = log[0][1]
    assert upsert is not None and (upsert["player_id"], upsert["current_lcd"]) == (str(player_id), 90)
    assert [params["reason_code"] for _s, params in log[1:] if params is not None] == [
        "encounter_disturbing",
        "passive_flux",
    ]


async def test_a_failed_lazy_flush_keeps_its_ledger_rows_for_the_retry() -> None:
    player_id = uuid.uuid4()
    log: list[tuple[object, Mapping[str, object] | None]] = []
    fail = [True]

    @asynccontextmanager
    async def session() -> AsyncGenerator[DbSession]:
        yield _RecordingSession(log, fail)

    async def load(_session: DbSession, pid: uuid.UUID) -> PlayerAggregate:
        return aggregate(raw_row(pid))

    now = [0.0]
    registry = PlayerRegistry(session, loader=load, clock=lambda: now[0])
    async with registry.mutate(player_id) as player:
        _ = player.lucidity.set(lcd=50, tier="uneasy")
        player.lucidity.log(-50, "test", "{}", None)

    assert await registry.flush_dirty() == 0  # the commit fails; the player stays dirty
    log.clear()
    now[0] = 60.0  # past the retry backoff
    assert await registry.flush_dirty() == 1

    assert [statement for statement, _params in log] == [UPSERT_LUCIDITY_SQL, ADD_ADJUSTMENT_LOG_SQL]


async def test_the_default_loader_reads_the_players_lucidity() -> None:
    player_id = uuid.uuid4()
    lucidity_row = {"current_lcd": 33, "current_tier": "fractured", "liabilities": "[]", "last_updated_at": T0}

    class _Session:
        def __init__(self) -> None:
            self.answer: Sequence[Mapping[str, object]] = []

        async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> _Session:
            _ = params
            if statement is LOAD_LUCIDITY_SQL:
                self.answer = [lucidity_row]
            elif statement is LIST_QUEST_INSTANCES_SQL:
                self.answer = []
            else:
                self.answer = [raw_row(player_id)]
            return self

        def mappings(self) -> _Session:
            return self

        def first(self) -> Mapping[str, object] | None:
            return self.answer[0] if self.answer else None

        def all(self) -> Sequence[Mapping[str, object]]:
            return self.answer

        async def commit(self) -> None:
            return None

        async def rollback(self) -> None:
            return None

    loaded = await load_player_aggregate(_Session(), player_id)

    assert loaded is not None and (loaded.lucidity.lcd, loaded.lucidity.tier) == (33, "fractured")
