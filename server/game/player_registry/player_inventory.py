"""
The inventory part of a PlayerAggregate: carried and equipped stacks (ADR-029 §3.2, step 4).

It is read from the same ``get_player_by_id`` row as the players-row part and written through
``update_player_inventory``, which sets both copies of the carried stacks and the equipped stacks and nothing else,
so an inventory write never touches stats. Every change is synchronous (committed before the command returns), and
each one is validated as a whole inventory, so a bad change is refused in memory before anything is written.
"""

from __future__ import annotations

import copy
import json
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import cast, override

from sqlalchemy import text

from ...schemas.shared import validate_inventory_payload
from .part import DbSession, Part, PartWrite
from .player_row import as_json_object, json_default

UPDATE_PLAYER_INVENTORY_SQL = text(
    "CALL update_player_inventory(:player_id, :inventory, :inventory_json, :equipped_json)"
)


def _as_stacks(raw: object) -> list[dict[str, object]]:
    """A list of stack dicts from JSON text (anything else is empty)."""
    loaded: object = cast(object, json.loads(raw)) if isinstance(raw, str) and raw else raw
    if not isinstance(loaded, list):
        return []
    return [dict(cast(dict[str, object], item)) for item in cast(list[object], loaded) if isinstance(item, dict)]


@dataclass(slots=True)
class InventoryData:
    """Carried stacks, and equipped stacks by slot."""

    carried: list[dict[str, object]] = field(default_factory=list)
    equipped: dict[str, object] = field(default_factory=dict)


class PlayerInventoryPart(Part):
    """Carried and equipped stacks, with read-only access and validated, synchronous mutators."""

    __slots__: tuple[str, ...] = ("_data", "_player_id")

    _player_id: uuid.UUID
    _data: InventoryData

    def __init__(self, player_id: uuid.UUID, data: InventoryData) -> None:
        super().__init__()
        self._player_id = player_id
        self._data = data

    @classmethod
    def from_row(cls, row: Mapping[str, object]) -> PlayerInventoryPart:
        """Build from a ``get_player_by_id`` row: carried from ``inventory``, equipped from ``equipped_json``."""
        data = InventoryData(_as_stacks(row.get("inventory")), as_json_object(row.get("equipped_json")))
        return cls(uuid.UUID(str(row["player_id"])), data)

    # ---- reads (the read-only view exposes these) ----

    @property
    def carried(self) -> Sequence[Mapping[str, object]]:
        """Carried stacks. Read-only: change them with ``set_carried`` or ``replace``."""
        return self._data.carried

    @property
    def equipped(self) -> Mapping[str, object]:
        """Equipped stacks by slot. Read-only: change them with ``set_equipped`` or ``replace``."""
        return self._data.equipped

    # ---- mutators ----

    def set_carried(self, stacks: Sequence[Mapping[str, object]]) -> None:
        """Replace the carried stacks. Raises InventorySchemaValidationError if the result is invalid."""
        self.replace(stacks, self._data.equipped)

    def set_equipped(self, equipped: Mapping[str, object]) -> None:
        """Replace the equipped stacks. Raises InventorySchemaValidationError if the result is invalid."""
        self.replace(self._data.carried, equipped)

    def replace(self, carried: Sequence[Mapping[str, object]], equipped: Mapping[str, object]) -> None:
        """Replace both at once (equip and unequip move a stack between them), validated as one inventory."""
        stacks = [dict(stack) for stack in carried]
        slots = dict(equipped)
        if stacks == self._data.carried and slots == self._data.equipped:
            return
        validate_inventory_payload({"inventory": stacks, "equipped": slots, "version": 1})
        self._data = InventoryData(stacks, slots)
        self.mark_dirty(sync=True)

    def write_params(self) -> dict[str, object]:
        """Parameters for ``update_player_inventory``: both carried copies get the same payload."""
        carried_json = json.dumps(self._data.carried, default=json_default)
        return {
            "player_id": str(self._player_id),
            "inventory": carried_json,
            "inventory_json": carried_json,
            "equipped_json": json.dumps(self._data.equipped, default=json_default),
        }

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return copy.deepcopy(self._data)

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, InventoryData):
            self._data = state

    @override
    def capture_write(self) -> PartWrite:
        params = self.write_params()

        async def write(session: DbSession) -> None:
            _ = await session.execute(UPDATE_PLAYER_INVENTORY_SQL, params)

        return write
