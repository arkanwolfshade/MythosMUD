"""Test doubles for the player registry: an in-memory session and a loader over a dict of rows."""

from __future__ import annotations

import uuid
from collections.abc import AsyncGenerator, Mapping
from contextlib import asynccontextmanager
from dataclasses import dataclass, field

from server.game.player_registry import DbSession, PlayerAggregate, PlayerRowData, PlayerRowPart

ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"


def row_data(player_id: uuid.UUID | None = None, **overrides: object) -> PlayerRowData:
    """A valid PlayerRowData with full DP and one Sling."""
    pid = player_id or uuid.uuid4()
    row: dict[str, object] = {
        "player_id": str(pid),
        "user_id": str(uuid.uuid4()),
        "name": "Tester",
        "current_room_id": ROOM,
        "respawn_room_id": ROOM,
        "experience_points": 0,
        "level": 1,
        "is_admin": 0,
        "profession_id": 0,
        "created_at": None,
        "last_active": None,
        "is_deleted": False,
        "deleted_at": None,
        "tutorial_instance_id": None,
        "stats": {"current_dp": 20, "max_dp": 20},
        "inventory": '[{"item_id": "sling", "item_name": "Sling", "slot_type": "backpack", "quantity": 1}]',
        "equipped_json": "{}",
    }
    row.update(overrides)
    return PlayerRowData.from_row(row)


class _Rows:
    _row: Mapping[str, object] | None

    def __init__(self, row: Mapping[str, object] | None) -> None:
        self._row = row

    def first(self) -> Mapping[str, object] | None:
        return self._row


class _Result:
    _row: Mapping[str, object] | None

    def __init__(self, row: Mapping[str, object] | None = None) -> None:
        self._row = row

    def mappings(self) -> _Rows:
        return _Rows(self._row)


@dataclass
class FakeDatabase:
    """Records every statement; ``fail_next`` makes the next commit raise."""

    executed: list[Mapping[str, object] | None] = field(default_factory=list)
    commits: int = 0
    rollbacks: int = 0
    fail_commits: int = 0
    row: Mapping[str, object] | None = None

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[DbSession]:
        yield _FakeSession(self)


class _FakeSession:
    _db: FakeDatabase

    def __init__(self, db: FakeDatabase) -> None:
        self._db = db

    async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> _Result:
        _ = statement
        self._db.executed.append(params)
        return _Result(self._db.row)

    async def commit(self) -> None:
        if self._db.fail_commits > 0:
            self._db.fail_commits -= 1
            raise RuntimeError("database unavailable")
        self._db.commits += 1

    async def rollback(self) -> None:
        self._db.rollbacks += 1


class FakeLoader:
    """An AggregateLoader over ``rows`` that counts loads per player."""

    def __init__(self, rows: dict[uuid.UUID, PlayerRowData]) -> None:
        self.rows: dict[uuid.UUID, PlayerRowData] = rows
        self.loads: dict[uuid.UUID, int] = {}

    async def __call__(self, _session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        self.loads[player_id] = self.loads.get(player_id, 0) + 1
        data = self.rows.get(player_id)
        return PlayerAggregate(PlayerRowPart(data)) if data is not None else None
