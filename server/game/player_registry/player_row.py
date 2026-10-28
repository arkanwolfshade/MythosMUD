"""
The core part of a PlayerAggregate: the ``players`` row and its ``stats`` jsonb (ADR-029 §3.2).

It is read through ``get_player_by_id``, the same row the inventory part reads, and written through
``update_player_row``, which sets this part's columns and nothing else. Every change here is lazy.

Carried and equipped stacks are the inventory part (player_inventory.py), written on their own (step 4). Status
effects and lucidity are not here either: they live in ``player_effects`` (step 3b) and ``player_lucidity`` (step 3a).
"""

from __future__ import annotations

import copy
import json
import uuid
from collections.abc import Mapping
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
    CALL update_player_row(
        :player_id, :name, :current_room_id, :respawn_room_id, :experience_points, :level, :is_admin,
        :profession_id, :last_active, :stats, :is_deleted, :deleted_at, :tutorial_instance_id
    )
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

    def update_params(self) -> dict[str, object]:
        """Parameters for ``update_player_row``, with PlayerSavePreparer's defaults."""
        return {
            "player_id": str(self.player_id),
            "name": self.name,
            "current_room_id": self.current_room_id,
            "respawn_room_id": self.respawn_room_id or DEFAULT_ROOM_ID,
            "experience_points": self.experience_points,
            "level": self.level,
            "is_admin": self.is_admin,
            "profession_id": self.profession_id,
            "last_active": _utc(self.last_active) or datetime.now(UTC),
            "stats": json.dumps(self.stats, default=json_default),
            "is_deleted": self.is_deleted,
            "deleted_at": _utc(self.deleted_at),
            "tutorial_instance_id": self.tutorial_instance_id,
        }


async def fetch_player_row(session: DbSession, player_id: uuid.UUID) -> Mapping[str, object] | None:
    """One player's ``get_player_by_id`` row (every part is built from it), or None if there is no such player."""
    result = await session.execute(LOAD_PLAYER_SQL, {"id": str(player_id)})
    return result.mappings().first()


class PlayerRowPart(Part):
    """The ``players`` row, with typed read access and lazy mutators."""

    __slots__: tuple[str, ...] = ("_data",)

    _data: PlayerRowData

    def __init__(self, data: PlayerRowData) -> None:
        super().__init__()
        self._data = data

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

    def set_stat(self, key: str, value: object) -> None:
        """Set one stats entry (lazy)."""
        if key in self._data.stats and self._data.stats[key] == value:
            return
        self._data.stats[key] = value
        self.mark_dirty()

    def set_current_room_id(self, room_id: str) -> None:
        """Move the player's saved room (lazy)."""
        if room_id != self._data.current_room_id:
            self._data.current_room_id = room_id
            self.mark_dirty()

    def set_respawn_room_id(self, room_id: str | None) -> None:
        """Change the respawn room (lazy)."""
        if room_id != self._data.respawn_room_id:
            self._data.respawn_room_id = room_id
            self.mark_dirty()

    def set_tutorial_instance_id(self, instance_id: str | None) -> None:
        """Enter or leave a tutorial instance (lazy)."""
        if instance_id != self._data.tutorial_instance_id:
            self._data.tutorial_instance_id = instance_id
            self.mark_dirty()

    def set_experience(self, experience_points: int, level: int) -> None:
        """Set XP and level (lazy)."""
        if (experience_points, level) != (self._data.experience_points, self._data.level):
            self._data.experience_points = experience_points
            self._data.level = level
            self.mark_dirty()

    def touch_last_active(self, when: datetime) -> None:
        """Record activity (lazy)."""
        self._data.last_active = when
        self.mark_dirty()

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return copy.deepcopy(self._data)

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, PlayerRowData):
            self._data = state

    @override
    def capture_write(self) -> PartWrite:
        params = self._data.update_params()

        async def write(session: DbSession) -> None:
            _ = await session.execute(UPDATE_PLAYER_ROW_SQL, params)

        return write
