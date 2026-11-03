"""
The core part of a PlayerAggregate: the ``players`` row and its ``stats`` jsonb (ADR-029 §3.2).

It is read through ``get_player_by_id``, the same row the inventory part reads, and written through
``update_player_row``, which sets only the columns and ``stats`` keys a unit changed (steps 5c and 6a). Players are
still saved outside the registry (movement, logout), so a write must never put back this part's copy of anything it
did not change. Changes are lazy unless a mutator says otherwise (corruption and DP are sync).

Carried and equipped stacks are the inventory part (player_inventory.py), written on their own (step 4). Status
effects and lucidity are not here either: they live in ``player_effects`` (step 3b) and ``player_lucidity`` (step 3a).
"""

from __future__ import annotations

import copy
import json
import uuid
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import text

from .part import DbSession, Part, PartWrite

# Same columns PlayerRepository.get_player_by_id selects, so the aggregate starts from identical data.
LOAD_PLAYER_SQL = text(
    """
    SELECT
        player_id, user_id, name, inventory, current_room_id,
        respawn_room_id, experience_points, level, is_admin, profession_id,
        created_at, last_active, stats, is_deleted, deleted_at,
        tutorial_instance_id, inventory_json, equipped_json
    FROM get_player_by_id(:id)
    """
)

UPDATE_PLAYER_ROW_SQL = text(
    """
    CALL update_player_row(:player_id, CAST(:changes AS jsonb), CAST(:stats_changes AS jsonb))
    """
)

# PlayerSavePreparer's default for a row with no room.
DEFAULT_ROOM_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


def json_default(value: object) -> str:
    """Stacks and stats can hold UUIDs (item instance ids); everything else must already be JSON."""
    if isinstance(value, uuid.UUID):
        return str(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def as_json_object(raw: object) -> dict[str, object]:
    """A dict from a jsonb value that arrives as a dict or as JSON text."""
    loaded: object = cast(object, json.loads(raw)) if isinstance(raw, str) and raw else raw
    return dict(cast(dict[str, object], loaded)) if isinstance(loaded, dict) else {}


def _utc(value: object) -> datetime | None:
    return value.astimezone(UTC) if isinstance(value, datetime) and value.tzinfo else None


@dataclass(slots=True)
class PlayerRowData:  # pylint: disable=too-many-instance-attributes  # Reason: one field per players column
    """The values of one ``players`` row, as the aggregate holds them."""

    player_id: uuid.UUID
    user_id: str
    name: str
    current_room_id: str
    respawn_room_id: str | None
    experience_points: int
    level: int
    is_admin: int
    profession_id: int | None
    created_at: datetime | None
    last_active: datetime | None
    is_deleted: bool
    deleted_at: datetime | None
    tutorial_instance_id: str | None
    stats: dict[str, object] = field(default_factory=dict)

    @classmethod
    def from_row(cls, row: Mapping[str, object]) -> PlayerRowData:
        """Build from a ``get_player_by_id`` row."""
        profession = row.get("profession_id")
        return cls(
            player_id=uuid.UUID(str(row["player_id"])),
            user_id=str(row["user_id"]),
            name=str(row["name"]),
            current_room_id=str(row.get("current_room_id") or DEFAULT_ROOM_ID),
            respawn_room_id=cast(str | None, row.get("respawn_room_id")),
            experience_points=int(cast(int, row.get("experience_points") or 0)),
            level=int(cast(int, row.get("level") or 1)),
            is_admin=int(cast(int, row.get("is_admin") or 0)),
            profession_id=int(cast(int, profession)) if profession else None,
            created_at=cast(datetime | None, row.get("created_at")),
            last_active=cast(datetime | None, row.get("last_active")),
            is_deleted=bool(row.get("is_deleted")),
            deleted_at=cast(datetime | None, row.get("deleted_at")),
            tutorial_instance_id=cast(str | None, row.get("tutorial_instance_id")),
            stats=as_json_object(row.get("stats")),
        )

    def column_value(self, column: str) -> object:
        """A writable column's value as ``update_player_row`` takes it, with PlayerSavePreparer's defaults."""
        if column == "respawn_room_id":
            return self.respawn_room_id or DEFAULT_ROOM_ID
        if column == "last_active":
            return (_utc(self.last_active) or datetime.now(UTC)).isoformat()
        return cast(object, getattr(self, column))

    def update_params(
        self, changed_columns: Iterable[str] = (), changed_stats: Iterable[str] = ()
    ) -> dict[str, object]:
        """Parameters for ``update_player_row``: only the changed columns and stats keys are sent."""
        return {
            "player_id": str(self.player_id),
            "changes": json.dumps({column: self.column_value(column) for column in changed_columns}),
            "stats_changes": json.dumps({key: self.stats.get(key) for key in changed_stats}, default=json_default),
        }


async def fetch_player_row(session: DbSession, player_id: uuid.UUID) -> Mapping[str, object] | None:
    """One player's ``get_player_by_id`` row (every part is built from it), or None if there is no such player."""
    result = await session.execute(LOAD_PLAYER_SQL, {"id": str(player_id)})
    return result.mappings().first()


class PlayerRowPart(Part):
    """The ``players`` row, with typed read access and lazy mutators."""

    __slots__: tuple[str, ...] = ("_changed_columns", "_changed_stats", "_data", "_in_flight")

    _data: PlayerRowData
    _changed_columns: set[str]
    _changed_stats: set[str]
    _in_flight: tuple[set[str], set[str]]

    def __init__(self, data: PlayerRowData) -> None:
        super().__init__()
        self._data = data
        self._changed_columns = set()
        self._changed_stats = set()
        self._in_flight = (set(), set())

    # ---- reads (the read-only view exposes these) ----

    @property
    def player_id(self) -> uuid.UUID:
        """The player's id."""
        return self._data.player_id

    @property
    def user_id(self) -> str:
        """The owning account's id."""
        return self._data.user_id

    @property
    def name(self) -> str:
        """The character name."""
        return self._data.name

    @property
    def current_room_id(self) -> str:
        """The room the player is in."""
        return self._data.current_room_id

    @property
    def respawn_room_id(self) -> str | None:
        """Where the player respawns."""
        return self._data.respawn_room_id

    @property
    def experience_points(self) -> int:
        """Total XP."""
        return self._data.experience_points

    @property
    def level(self) -> int:
        """Character level."""
        return self._data.level

    @property
    def is_admin(self) -> bool:
        """True for an admin character."""
        return bool(self._data.is_admin)

    @property
    def profession_id(self) -> int | None:
        """The profession, if any."""
        return self._data.profession_id

    @property
    def tutorial_instance_id(self) -> str | None:
        """The tutorial instance the player is in (or the pending marker), else None."""
        return self._data.tutorial_instance_id

    @property
    def is_deleted(self) -> bool:
        """True for a soft-deleted character."""
        return self._data.is_deleted

    @property
    def stats(self) -> Mapping[str, object]:
        """The stats jsonb (DP, MP, corruption, ...). Read-only: change it with ``set_stat``."""
        return self._data.stats

    # ---- mutators ----

    def set_stat(self, key: str, value: object, *, sync: bool = False) -> None:
        """Set one stats entry (lazy, unless ``sync``)."""
        if key in self._data.stats and self._data.stats[key] == value:
            return
        self._data.stats[key] = value
        self._changed_stats.add(key)
        self.mark_dirty(sync=sync)

    def remove_stat(self, key: str, *, sync: bool = False) -> None:
        """Remove one stats entry (lazy, unless ``sync``); the write sends it as null, which removes it."""
        if key in self._data.stats:
            del self._data.stats[key]
            self._changed_stats.add(key)
            self.mark_dirty(sync=sync)

    def _set_column(self, column: str, value: object, *, sync: bool = False) -> None:
        if cast(object, getattr(self._data, column)) != value:
            setattr(self._data, column, value)
            self._changed_columns.add(column)
            self.mark_dirty(sync=sync)

    def set_current_room_id(self, room_id: str, *, sync: bool = False) -> None:
        """Move the player's saved room (lazy, unless ``sync``)."""
        self._set_column("current_room_id", room_id, sync=sync)

    def set_respawn_room_id(self, room_id: str | None) -> None:
        """Change the respawn room (lazy)."""
        self._set_column("respawn_room_id", room_id)

    def set_tutorial_instance_id(self, instance_id: str | None) -> None:
        """Enter or leave a tutorial instance (lazy)."""
        self._set_column("tutorial_instance_id", instance_id)

    def set_experience(self, experience_points: int, level: int) -> None:
        """Set XP and level (lazy)."""
        self._set_column("experience_points", experience_points)
        self._set_column("level", level)

    def touch_last_active(self, when: datetime) -> None:
        """Record activity (lazy)."""
        self._set_column("last_active", when)

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return copy.deepcopy(self._data), set(self._changed_columns), set(self._changed_stats)

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, tuple):
            self._data, self._changed_columns, self._changed_stats = cast(
                tuple[PlayerRowData, set[str], set[str]], state
            )

    @override
    def capture_write(self) -> PartWrite:
        params = self._data.update_params(self._changed_columns, self._changed_stats)
        self._in_flight = (self._changed_columns, self._changed_stats)
        self._changed_columns, self._changed_stats = set(), set()

        async def write(session: DbSession) -> None:
            _ = await session.execute(UPDATE_PLAYER_ROW_SQL, params)

        return write

    @override
    def write_failed(self) -> None:
        """A lazy flush failed: its columns and stats keys are still unwritten, so the retry sends them again."""
        columns, stats = self._in_flight
        self._changed_columns |= columns
        self._changed_stats |= stats
        self._in_flight = (set(), set())
        super().write_failed()
