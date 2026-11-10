"""
Unit tests for PlayerEffectRepository (ADR-019, ADR-029 steps 3b-i and 6d).

The registry owns the rows now; what is left is the tick's candidate query. The procedure is exercised against a real
database by the integration tests; these tests pin the call the repository makes and how it maps and fails.
"""

from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Iterator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import DatabaseError
from server.persistence.repositories.player_effect_repository import PlayerEffectRepository

MODULE = "server.persistence.repositories.player_effect_repository"


class _Result:
    def __init__(self, ids: list[uuid.UUID]) -> None:
        self._ids: list[uuid.UUID] = ids

    def scalars(self) -> _Result:
        return self

    def all(self) -> list[uuid.UUID]:
        return self._ids


@dataclass
class FakeDb:
    """Records (sql, params) per execute; ``ids`` is what every execute returns."""

    ids: list[uuid.UUID] = field(default_factory=list)
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
        return _Result(self.ids)

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
async def test_candidates_are_asked_for_in_one_query_and_come_back_as_uuids(
    repo: PlayerEffectRepository, db: FakeDb
) -> None:
    online = [uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]
    db.ids = [online[1]]

    assert await repo.player_ids_with_active_effects(online) == [online[1]]

    [(sql, params)] = db.calls
    assert "FROM get_player_ids_with_active_effects(" in sql
    assert params == {"player_ids": online}
    assert db.commits == 1


@pytest.mark.asyncio
async def test_nobody_online_asks_nothing(repo: PlayerEffectRepository, db: FakeDb) -> None:
    assert await repo.player_ids_with_active_effects([]) == []

    assert db.calls == []


@pytest.mark.asyncio
async def test_a_database_failure_raises_database_error(repo: PlayerEffectRepository, db: FakeDb) -> None:
    db.fail = True

    with pytest.raises(DatabaseError):
        _ = await repo.player_ids_with_active_effects([uuid.uuid4()])
