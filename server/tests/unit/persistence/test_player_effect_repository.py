"""
Unit tests for PlayerEffectRepository (ADR-019, ADR-029 step 3b-i).

The procedures are exercised against a real database by the dry runs recorded in the PR; these tests pin the calls the
repository makes and how it maps rows.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import AsyncGenerator, Iterator, Mapping
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime
from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.player_effect_repository import PlayerEffectRepository

MODULE = "server.persistence.repositories.player_effect_repository"


class _Rows:
    def __init__(self, rows: list[Mapping[str, object]]) -> None:
        self._rows: list[Mapping[str, object]] = rows

    def all(self) -> list[Mapping[str, object]]:
        return self._rows


class _Result:
    def __init__(self, scalar: object, rows: list[Mapping[str, object]]) -> None:
        self._scalar: object = scalar
        self._rows: list[Mapping[str, object]] = rows

    def scalar(self) -> object:
        return self._scalar

    def mappings(self) -> _Rows:
        return _Rows(self._rows)


@dataclass
class FakeDb:
    """Records (sql, params) per execute; ``scalar`` / ``rows`` are what every execute returns."""

    scalar: object = None
    rows: list[Mapping[str, object]] = field(default_factory=list)
    fail: bool = False
    calls: list[tuple[str, dict[str, object]]] = field(default_factory=list)
    commits: int = 0

    @asynccontextmanager
    async def __call__(self) -> AsyncGenerator[FakeDb]:
        yield self

    async def execute(self, statement: object, params: dict[str, object]) -> _Result:
        if self.fail:
            raise SQLAlchemyError("database down")
        self.calls.append((" ".join(str(statement).split()), params))
        return _Result(self.scalar, self.rows)

    async def commit(self) -> None:
        self.commits += 1


@pytest.fixture(name="db")
def _db() -> FakeDb:
    return FakeDb()


@pytest.fixture(name="repo")
def _repo(db: FakeDb) -> Iterator[PlayerEffectRepository]:
    with patch(f"{MODULE}.get_session_maker", return_value=db):
        yield PlayerEffectRepository()


@pytest.mark.asyncio
async def test_add_effect_sends_the_payload_as_json_and_returns_the_id(
    repo: PlayerEffectRepository, db: FakeDb
) -> None:
    effect_id = uuid.uuid4()
    db.scalar = effect_id
    player_id = uuid.uuid4()

    result = await repo.add_effect(
        player_id,
        {
            "effect_type": "lucidity_drain_over_time",
            "category": "scripted",
            "remaining_seconds": None,
            "payload": {"rate": 1, "floor": -10},
            "instance_scoped": True,
        },
    )

    assert result == str(effect_id)
    [(sql, params)] = db.calls
    assert "add_player_effect(" in sql
    assert params["player_id"] == str(player_id)
    assert params["remaining_seconds"] is None  # until removed
    assert json.loads(str(params["payload"])) == {"rate": 1, "floor": -10}
    assert (params["instance_scoped"], params["intensity"], params["visibility_level"]) == (True, 1, "visible")
    assert db.commits == 1


@pytest.mark.asyncio
async def test_deletes_by_id_type_and_instance_scope(repo: PlayerEffectRepository, db: FakeDb) -> None:
    db.scalar = 2
    player_id = uuid.uuid4()

    await repo.delete_effect("e1")
    by_type = await repo.delete_effects_by_type(player_id, "blinded")
    scoped = await repo.delete_instance_scoped_effects(player_id)

    assert (by_type, scoped) == (2, 2)
    assert [sql.split("(")[0] for sql, _params in db.calls] == [
        "SELECT delete_player_effect",
        "SELECT delete_player_effects_by_type",
        "SELECT delete_instance_scoped_effects",
    ]


@pytest.mark.asyncio
async def test_get_active_effects_maps_rows(repo: PlayerEffectRepository, db: FakeDb) -> None:
    player_id = uuid.uuid4()
    created = datetime(2026, 10, 27, 12, 0)
    db.rows = [
        {
            "id": uuid.uuid4(),
            "player_id": player_id,
            "effect_type": "heal_over_time",
            "category": "scripted",
            "remaining_seconds": 7,
            "payload": {"healing": 5},
            "instance_scoped": False,
            "intensity": 1,
            "source": None,
            "visibility_level": "visible",
            "created_at": created,
        },
        {
            "id": uuid.uuid4(),
            "player_id": player_id,
            "effect_type": "lucidity_drain_over_time",
            "category": "scripted",
            "remaining_seconds": None,
            "payload": None,
            "instance_scoped": True,
            "intensity": None,
            "source": None,
            "visibility_level": None,
            "created_at": created,
        },
    ]

    heal, drain = await repo.get_active_effects_for_player(player_id)

    assert (heal.effect_type, heal.remaining_seconds, heal.payload) == ("heal_over_time", 7, {"healing": 5})
    assert (drain.remaining_seconds, drain.payload, drain.instance_scoped) == (None, {}, True)
    assert (drain.intensity, drain.visibility_level) == (1, "visible")
    assert "FROM get_active_effects_for_player(" in db.calls[0][0]


@pytest.mark.asyncio
async def test_update_payload_sends_json(repo: PlayerEffectRepository, db: FakeDb) -> None:
    await repo.update_effect_payload("e1", {"elapsed": 4})

    [(sql, params)] = db.calls
    assert "update_player_effect_payload(" in sql
    assert json.loads(str(params["payload"])) == {"elapsed": 4}


@pytest.mark.asyncio
async def test_advance_returns_what_ran_out_and_skips_an_empty_set(repo: PlayerEffectRepository, db: FakeDb) -> None:
    player_id = uuid.uuid4()
    db.rows = [{"player_id": player_id, "effect_type": "login_warded"}]

    assert await repo.advance_effects([]) == []
    assert db.calls == []  # nobody online: no round trip

    assert await repo.advance_effects([player_id]) == [(str(player_id), "login_warded")]
    [(sql, params)] = db.calls
    assert "FROM advance_player_effects(" in sql
    assert params["player_ids"] == [player_id]


@pytest.mark.asyncio
async def test_a_database_failure_raises_database_error(repo: PlayerEffectRepository, db: FakeDb) -> None:
    db.fail = True

    with pytest.raises(DatabaseError):
        _ = await repo.get_active_effects_for_player(uuid.uuid4())
    with pytest.raises(DatabaseError):
        await repo.delete_effect("e1")
