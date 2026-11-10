"""
A real PlayerRegistry over an in-memory database, for tests (ADR-029).

``FakeDatabase`` records every statement's parameters and can fail commits; ``raw_row`` and ``aggregate`` build a
player the way ``get_player_by_id`` and ``load_player_aggregate`` do. ``install_player_registry`` puts a registry in
front of a command test's player: the aggregate starts from that player's own inventory, so a command runs through the
real unit of work, validation and commit, and the test reads back what was written. ``lucidity_registry`` seeds
players' lucidity for lucidity service tests (ADR-029 step 5b-i).
"""

from __future__ import annotations

import json
import uuid
from collections.abc import AsyncGenerator, Callable, Mapping, Sequence
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime
from typing import cast

import pytest

from server.events.event_types import BaseEvent
from server.game.player_registry import (
    DbSession,
    EffectData,
    Exposure,
    LucidityData,
    PlayerAggregate,
    PlayerCooldownsPart,
    PlayerCooldownsView,
    PlayerEffectsPart,
    PlayerEffectsView,
    PlayerExposurePart,
    PlayerInventoryPart,
    PlayerLucidityPart,
    PlayerQuestsPart,
    PlayerRegistry,
    PlayerRowData,
    PlayerRowPart,
    QuestInstanceData,
)
from server.game.player_registry.player_cooldowns import REPLACE_CORRUPTION_COOLDOWNS_SQL
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


def aggregate(
    row: Mapping[str, object],
    quests: Sequence[QuestInstanceData] = (),
    lucidity: LucidityData | None = None,
    *,
    cooldowns: PlayerCooldownsPart | None = None,
    exposure: PlayerExposurePart | None = None,
    corruption_cooldowns: PlayerCooldownsPart | None = None,
    effects: PlayerEffectsPart | None = None,
) -> PlayerAggregate:
    """The row and inventory parts from one ``get_player_by_id`` row, plus ``quests``, ``lucidity``, ``cooldowns``,
    ``exposure``, ``corruption_cooldowns`` and ``effects``, as load_player_aggregate builds them."""
    player_id = uuid.UUID(str(row["player_id"]))
    return PlayerAggregate(
        PlayerRowPart(PlayerRowData.from_row(row)),
        PlayerInventoryPart.from_row(row),
        PlayerQuestsPart(player_id, quests),
        PlayerLucidityPart(player_id, lucidity),
        cooldowns,
        exposure,
        corruption_cooldowns,
        effects,
    )


class _Rows:
    _row: Mapping[str, object] | None

    def __init__(self, row: Mapping[str, object] | None) -> None:
        self._row = row

    def first(self) -> Mapping[str, object] | None:
        return self._row

    def all(self) -> list[Mapping[str, object]]:
        return []  # no query this fake answers returns several rows (a loaded player has no quests)


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
    statements: list[object] = field(default_factory=list)
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
        self._db.statements.append(statement)
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
    monkeypatch.setattr("server.commands.inventory_command_helpers.player_registry", lambda: registry)
    return RegistryHarness(registry, db)


@dataclass
class LucidityHarness:
    """A real registry holding seeded players' lucidity, the database its flushes write to, and the events it published."""

    registry: PlayerRegistry
    db: FakeDatabase
    published: list[BaseEvent] = field(default_factory=list)

    def cooldowns(self, player_id: uuid.UUID) -> PlayerCooldownsView:
        """The player's live cooldowns."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.cooldowns

    def encounters(self, player_id: uuid.UUID, entity_archetype: str) -> int:
        """How many times the player has met ``entity_archetype``, live."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.exposure.encounter_count(entity_archetype)

    def stats(self, player_id: uuid.UUID) -> Mapping[str, object]:
        """The player's live ``stats`` (DP, posture, corruption, ...)."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.row.stats

    def room(self, player_id: uuid.UUID) -> str:
        """The player's live ``current_room_id``."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.row.current_room_id

    def corruption(self, player_id: uuid.UUID) -> object:
        """The player's live ``stats.corruption`` (None if it was never set)."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.row.stats.get("corruption")

    def effects(self, player_id: uuid.UUID) -> PlayerEffectsView:
        """The player's live effects."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.effects

    def corruption_cooldowns(self, player_id: uuid.UUID) -> PlayerCooldownsView:
        """The player's live corruption cooldowns."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.corruption_cooldowns

    def lucidity(self, player_id: uuid.UUID) -> LucidityData:
        """The player's live lucidity (what the registry holds, flushed or not)."""
        player = self.registry.peek(player_id)
        assert player is not None, f"player {player_id} is not loaded"
        return player.lucidity.data

    def ledger(self) -> list[Mapping[str, object]]:
        """Every ledger row written so far (lucidity's or corruption's; flush first for lucidity: it is lazy)."""
        return [params for params in self.db.executed if params is not None and "reason_code" in params]

    async def flush(self) -> int:
        """Run the lazy sweep once."""
        return await self.registry.flush_dirty()


def lucidity_registry(
    players: Mapping[uuid.UUID, LucidityData | None],
    *,
    stats: Mapping[str, object] | None = None,
    cooldowns: Mapping[str, datetime] | None = None,
    exposures: Mapping[str, Exposure] | None = None,
    corruption_cooldowns: Mapping[str, datetime] | None = None,
    effects: Sequence[EffectData] | None = None,
    row: Mapping[str, object] | None = None,
) -> LucidityHarness:
    """A registry with these players (lucidity None = the starting values); any other id is no such player.

    ``cooldowns`` and ``exposures`` seed every player's cooldowns and encounter counts (ADR-029 step 5b-ii), and
    ``corruption_cooldowns`` their corruption cooldowns (step 5c). Seed corruption and DP through ``stats``, and
    ``players`` columns (room, respawn room, tutorial instance, name) through ``row`` (step 6a). ``effects`` seeds
    every player's running effects (step 6d); ``published`` collects the events a committed unit published.
    """
    db = FakeDatabase()
    published: list[BaseEvent] = []

    async def load(_session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        if player_id not in players:
            return None
        columns = dict(row or {})
        seeded = raw_row(
            player_id, stats=dict(stats) if stats is not None else {"current_dp": 20, "max_dp": 20}, **columns
        )
        return aggregate(
            seeded,
            lucidity=players[player_id],
            cooldowns=PlayerCooldownsPart(player_id, cooldowns),
            exposure=PlayerExposurePart(player_id, exposures),
            corruption_cooldowns=PlayerCooldownsPart(
                player_id, corruption_cooldowns, write_sql=REPLACE_CORRUPTION_COOLDOWNS_SQL
            ),
            effects=PlayerEffectsPart(player_id, effects),
        )

    return LucidityHarness(PlayerRegistry(db.session, loader=load, publish=published.append), db, published)
