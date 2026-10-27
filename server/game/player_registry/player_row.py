"""
The core part of a PlayerAggregate: the ``players`` row, its ``stats`` jsonb, and the inventory (ADR-029 §3.2).

It is read through ``get_player_by_id`` and written through ``upsert_player``, the same stored procedures
PlayerRepository uses, which also write ``player_inventories``. Inventory and equipped changes are synchronous
(they must be committed before the command returns); every other change here is lazy.

Status effects and lucidity are not here: they live in ``player_effects`` (ADR-029 step 3b) and
``player_lucidity`` (step 3a).
"""

from __future__ import annotations

import copy
import json
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import text

from ...persistence.repositories.player_repository_save import UPSERT_PLAYER_SQL
from ...schemas.shared import validate_inventory_payload
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

# PlayerSavePreparer's default for a row with no room.
DEFAULT_ROOM_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


def _json_default(value: object) -> str:
    """Inventory stacks can hold UUIDs (item instance ids); everything else must already be JSON."""
    if isinstance(value, uuid.UUID):
        return str(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def _as_dict(raw: object) -> dict[str, object]:
    """A dict from a jsonb value that arrives as a dict or as JSON text."""
    loaded: object = cast(object, json.loads(raw)) if isinstance(raw, str) and raw else raw
    return dict(cast(dict[str, object], loaded)) if isinstance(loaded, dict) else {}


def _as_stacks(raw: object) -> list[dict[str, object]]:
    """A list of stack dicts from JSON text (anything else is empty)."""
    loaded: object = cast(object, json.loads(raw)) if isinstance(raw, str) and raw else raw
    if not isinstance(loaded, list):
        return []
    return [dict(cast(dict[str, object], item)) for item in cast(list[object], loaded) if isinstance(item, dict)]


def _utc(value: object) -> datetime | None:
    return value.astimezone(UTC) if isinstance(value, datetime) and value.tzinfo else None


def _validate(inventory: Sequence[Mapping[str, object]], equipped: Mapping[str, object]) -> None:
    """Raise InventorySchemaValidationError if the payload is not a valid inventory."""
    validate_inventory_payload({"inventory": list(inventory), "equipped": dict(equipped), "version": 1})


@dataclass(slots=True)
class PlayerRowData:  # pylint: disable=too-many-instance-attributes  # Reason: one field per players column
    """The values of one ``players`` row plus its inventory, as the aggregate holds them."""

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
    inventory: list[dict[str, object]] = field(default_factory=list)
    equipped: dict[str, object] = field(default_factory=dict)

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
            stats=_as_dict(row.get("stats")),
            inventory=_as_stacks(row.get("inventory")),
            equipped=_as_dict(row.get("equipped_json")),
        )

    def upsert_params(self) -> dict[str, object]:
        """Parameters for ``upsert_player``, built the way PlayerSavePreparer builds them."""
        inventory_json = json.dumps(self.inventory, default=_json_default)
        equipped_json = json.dumps(self.equipped, default=_json_default)
        now = datetime.now(UTC)
        return {
            "player_id": str(self.player_id),
            "user_id": self.user_id,
            "name": self.name,
            "inventory": inventory_json,
            "current_room_id": self.current_room_id,
            "respawn_room_id": self.respawn_room_id or DEFAULT_ROOM_ID,
            "experience_points": self.experience_points,
            "level": self.level,
            "is_admin": self.is_admin,
            "profession_id": self.profession_id,
            "created_at": _utc(self.created_at) or now,
            "last_active": _utc(self.last_active) or now,
            "stats": json.dumps(self.stats, default=_json_default),
            "is_deleted": self.is_deleted,
            "deleted_at": _utc(self.deleted_at),
            "tutorial_instance_id": self.tutorial_instance_id,
            "inventory_json": inventory_json,
            "equipped_json": equipped_json,
        }


async def load_player_row(session: DbSession, player_id: uuid.UUID) -> PlayerRowPart | None:
    """Load one player's row and inventory, or None if there is no such player."""
    result = await session.execute(LOAD_PLAYER_SQL, {"id": str(player_id)})
    row = result.mappings().first()
    return PlayerRowPart(PlayerRowData.from_row(row)) if row is not None else None


class PlayerRowPart(Part):
    """The ``players`` row and inventory, with typed read access and validated mutators."""

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

    @property
    def inventory(self) -> Sequence[Mapping[str, object]]:
        """Carried stacks. Read-only: change them with ``set_inventory``."""
        return self._data.inventory

    @property
    def equipped(self) -> Mapping[str, object]:
        """Equipped stacks by slot. Read-only: change them with ``set_equipped``."""
        return self._data.equipped

    # ---- mutators ----

    def set_stat(self, key: str, value: object) -> None:
        """Set one stats entry (lazy)."""
        if key in self._data.stats and self._data.stats[key] == value:
            return
        self._data.stats[key] = value
        self.mark_dirty()

    def set_inventory(self, stacks: Sequence[Mapping[str, object]]) -> None:
        """Replace the carried stacks (synchronous). Raises InventorySchemaValidationError if invalid."""
        inventory = [dict(stack) for stack in stacks]
        _validate(inventory, self._data.equipped)
        self._data.inventory = inventory
        self.mark_dirty(sync=True)

    def set_equipped(self, equipped: Mapping[str, object]) -> None:
        """Replace the equipped stacks (synchronous). Raises InventorySchemaValidationError if invalid."""
        slots = dict(equipped)
        _validate(self._data.inventory, slots)
        self._data.equipped = slots
        self.mark_dirty(sync=True)

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
        params = self._data.upsert_params()

        async def write(session: DbSession) -> None:
            _ = await session.execute(UPSERT_PLAYER_SQL, params)

        return write
