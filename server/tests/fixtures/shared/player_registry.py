"""
A real PlayerRegistry over an in-memory database, for tests (ADR-029).

``FakeDatabase`` records every statement's parameters and can fail commits; ``raw_row`` and ``aggregate`` build a
player the way ``get_player_by_id`` and ``load_player_aggregate`` do. ``install_player_registry`` puts a registry in
front of a command test's player: the aggregate starts from that player's own inventory, so a command runs through the
real unit of work, validation and commit, and the test reads back what was written.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import AsyncGenerator, Callable, Mapping
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from typing import cast

import pytest

from server.game.player_registry import (
    DbSession,
    PlayerAggregate,
    PlayerInventoryPart,
    PlayerRegistry,
    PlayerRowData,
    PlayerRowPart,
)
from server.game.player_registry.player_row import json_default

ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"


def raw_row(player_id: uuid.UUID | None = None, **overrides: object) -> dict[str, object]:
    """A valid ``get_player_by_id`` row with full DP and one Sling."""
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
    return row


def aggregate(row: Mapping[str, object]) -> PlayerAggregate:
    """Both parts from one ``get_player_by_id`` row, as load_player_aggregate builds them."""
    return PlayerAggregate(PlayerRowPart(PlayerRowData.from_row(row)), PlayerInventoryPart.from_row(row))


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
    """Records every statement; ``fail_commits`` makes that many commits raise ``commit_error``."""

    executed: list[Mapping[str, object] | None] = field(default_factory=list)
    commits: int = 0
    rollbacks: int = 0
    fail_commits: int = 0
    commit_error: Exception = field(default_factory=lambda: RuntimeError("database unavailable"))
    row: Mapping[str, object] | None = None

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[DbSession]:
        yield _FakeSession(self)

    def last_inventory_write(self) -> Mapping[str, object] | None:
        """Parameters of the most recent ``update_player_inventory`` call, or None if there was none."""
        writes = [params for params in self.executed if params is not None and "inventory_json" in params]
        return writes[-1] if writes else None


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
            raise self._db.commit_error
        self._db.commits += 1

    async def rollback(self) -> None:
        self._db.rollbacks += 1


@dataclass
class RegistryHarness:
    """The installed registry and the database it writes to."""

    registry: PlayerRegistry
    db: FakeDatabase

    def saved_carried(self) -> list[dict[str, object]] | None:
        """The carried stacks of the last inventory write, or None if nothing was written."""
        write = self.db.last_inventory_write()
        if write is None:
            return None
        return cast(list[dict[str, object]], json.loads(str(write["inventory_json"])))

    def saved_equipped(self) -> dict[str, object] | None:
        """The equipped stacks of the last inventory write, or None if nothing was written."""
        write = self.db.last_inventory_write()
        if write is None:
            return None
        return cast(dict[str, object], json.loads(str(write["equipped_json"])))


def install_player_registry(monkeypatch: pytest.MonkeyPatch, player: object) -> RegistryHarness:
    """Give inventory commands a real registry whose aggregate starts from ``player``'s current inventory.

    ``player`` is whatever the test's command loads (a Player, a fake, a MagicMock): only its ``get_inventory`` and
    ``get_equipped_items`` are read, when the registry first loads the player.
    """
    db = FakeDatabase()
    get_inventory = cast(Callable[[], object], getattr(player, "get_inventory"))  # noqa: B009  # Reason: player is typed object (any test double), so plain access would not type-check
    get_equipped = cast(Callable[[], object], getattr(player, "get_equipped_items"))  # noqa: B009  # Reason: player is typed object (any test double), so plain access would not type-check

    async def load(_session: DbSession, player_id: uuid.UUID) -> PlayerAggregate:
        carried = get_inventory()
        equipped = get_equipped()
        row = raw_row(
            player_id,
            inventory=json.dumps(carried if isinstance(carried, list) else [], default=json_default),
            equipped_json=json.dumps(equipped if isinstance(equipped, dict) else {}, default=json_default),
        )
        return aggregate(row)

    registry = PlayerRegistry(db.session, loader=load)
    monkeypatch.setattr("server.commands.inventory_command_helpers._player_registry", lambda: registry)
    return RegistryHarness(registry, db)
