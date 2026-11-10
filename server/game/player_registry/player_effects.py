"""
The effects part of a PlayerAggregate: the player's ``player_effects`` rows that are still running (ADR-029 §3.2,
step 6d).

An effect is the login ward, a spell's status, or a scripted effect that acts every game second (heal or damage over
time, the lucidity drain). The part holds the rows as they were when the aggregate loaded, and every change is
synchronous: it is queued as one row-level write (add, delete, set the payload, count one second) and committed with
the unit that made it, so a second's effects, the DP and lucidity they moved and the countdown land together.

A write never replaces the whole set. ``remaining_seconds`` is written only when a row is added and by the
countdown, which the part runs on its own copy exactly as ``advance_player_effects`` runs it in the database: the
counters used to be a separate batched statement, and a resident copy would have gone stale against it. The row ids
are named here (not by the database) so a row added in one unit can be changed in a later one.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, replace
from typing import cast, override

from sqlalchemy import TextClause, text

from .part import DbSession, Part, PartWrite

ADD_EFFECT_SQL = text(
    """
    SELECT add_player_effect(
        :player_id, :effect_type, :category, :remaining_seconds, CAST(:payload AS jsonb), :instance_scoped,
        :intensity, :source, :visibility_level, :effect_id
    )
    """
)
DELETE_EFFECT_SQL = text("SELECT delete_player_effect(:effect_id)")
DELETE_EFFECTS_BY_TYPE_SQL = text("SELECT delete_player_effects_by_type(:player_id, :effect_type)")
DELETE_INSTANCE_SCOPED_SQL = text("SELECT delete_instance_scoped_effects(:player_id)")
UPDATE_PAYLOAD_SQL = text("SELECT update_player_effect_payload(:effect_id, CAST(:payload AS jsonb))")
ADVANCE_EFFECTS_SQL = text("SELECT player_id, effect_type FROM advance_player_effects(CAST(:player_ids AS uuid[]))")

type _Write = tuple[TextClause, Mapping[str, object]]


@dataclass(frozen=True, slots=True)
class EffectData:
    """One running effect. ``remaining_seconds`` counts online game seconds; None means until removed.

    ``payload`` holds the effect's parameters and mutable state (healing, a drain's elapsed). It is never changed in
    place: ``PlayerEffectsPart.set_payload`` swaps in a new one.
    """

    id: uuid.UUID
    effect_type: str
    category: str
    remaining_seconds: int | None
    payload: Mapping[str, object]
    instance_scoped: bool = False
    intensity: int = 1
    source: str | None = None
    visibility_level: str = "visible"

    @classmethod
    def from_row(cls, row: Mapping[str, object]) -> EffectData:
        """Build from one element of the ``effects`` column of ``get_player_lucidity_state``."""
        remaining = row.get("remaining_seconds")
        payload = row.get("payload")
        return cls(
            id=uuid.UUID(str(row["id"])),
            effect_type=str(row["effect_type"]),
            category=str(row["category"]),
            remaining_seconds=int(cast(int, remaining)) if remaining is not None else None,
            payload=dict(cast(Mapping[str, object], payload)) if isinstance(payload, Mapping) else {},
            instance_scoped=bool(row.get("instance_scoped")),
            intensity=int(cast(int, row.get("intensity") or 1)),
            source=cast(str | None, row.get("source")),
            visibility_level=str(row.get("visibility_level") or "visible"),
        )


class PlayerEffectsPart(Part):
    """The player's running effects, oldest first, with synchronous row-level mutators."""

    __slots__: tuple[str, ...] = ("_effects", "_in_flight", "_pending", "_player_id")

    _player_id: uuid.UUID
    _effects: list[EffectData]
    _pending: list[_Write]
    _in_flight: list[_Write]

    def __init__(self, player_id: uuid.UUID, effects: Sequence[EffectData] | None = None) -> None:
        super().__init__()
        self._player_id = player_id
        self._effects = list(effects or [])
        self._pending = []
        self._in_flight = []

    @classmethod
    def from_json(cls, player_id: uuid.UUID, rows: object) -> PlayerEffectsPart:
        """Build from the ``effects`` column of ``get_player_lucidity_state`` (a JSON array, or its text)."""
        entries = cast(Sequence[Mapping[str, object]], json.loads(rows) if isinstance(rows, str) else rows or [])
        return cls(player_id, [EffectData.from_row(row) for row in entries])

    # ---- reads ----

    @property
    def effects(self) -> tuple[EffectData, ...]:
        """The running effects, oldest first. A copy: changing the part while looping over it is safe."""
        return tuple(self._effects)

    # ---- mutators ----

    def add(  # pylint: disable=too-many-arguments  # Reason: one effect's columns; the keyword-only ones all have defaults
        self,
        effect_type: str,
        category: str,
        *,
        remaining_seconds: int | None = None,
        payload: Mapping[str, object] | None = None,
        instance_scoped: bool = False,
        intensity: int = 1,
        source: str | None = None,
        visibility_level: str = "visible",
    ) -> uuid.UUID:
        """Start an effect and return its id. One with no time left (0 or less) is never stored: it would not run."""
        effect = EffectData(
            id=uuid.uuid4(),
            effect_type=effect_type,
            category=category,
            remaining_seconds=remaining_seconds,
            payload=dict(payload or {}),
            instance_scoped=instance_scoped,
            intensity=intensity,
            source=source,
            visibility_level=visibility_level,
        )
        if remaining_seconds is not None and remaining_seconds <= 0:
            return effect.id
        self._effects.append(effect)
        self._queue(
            ADD_EFFECT_SQL,
            {
                "player_id": str(self._player_id),
                "effect_type": effect.effect_type,
                "category": effect.category,
                "remaining_seconds": effect.remaining_seconds,
                "payload": json.dumps(dict(effect.payload)),
                "instance_scoped": effect.instance_scoped,
                "intensity": effect.intensity,
                "source": effect.source,
                "visibility_level": effect.visibility_level,
                "effect_id": str(effect.id),
            },
        )
        return effect.id

    def remove(self, effect_id: uuid.UUID) -> bool:
        """End one effect; True if the player had it."""
        if not self._drop(lambda effect: effect.id == effect_id):
            return False
        self._queue(DELETE_EFFECT_SQL, {"effect_id": str(effect_id)})
        return True

    def remove_by_type(self, effect_type: str) -> int:
        """End every effect of one type; returns how many."""
        removed = self._drop(lambda effect: effect.effect_type == effect_type)
        if removed:
            self._queue(DELETE_EFFECTS_BY_TYPE_SQL, {"player_id": str(self._player_id), "effect_type": effect_type})
        return removed

    def clear_instance_scoped(self) -> int:
        """End the effects tied to an instance the player has lost; returns how many."""
        removed = self._drop(lambda effect: effect.instance_scoped)
        if removed:
            self._queue(DELETE_INSTANCE_SCOPED_SQL, {"player_id": str(self._player_id)})
        return removed

    def set_payload(self, effect_id: uuid.UUID, payload: Mapping[str, object]) -> bool:
        """Replace one effect's payload (its mutable state); False if the player does not have it or it is unchanged."""
        for index, effect in enumerate(self._effects):
            if effect.id != effect_id:
                continue
            if effect.payload == payload:
                return False
            self._effects[index] = replace(effect, payload=dict(payload))
            self._queue(UPDATE_PAYLOAD_SQL, {"effect_id": str(effect_id), "payload": json.dumps(dict(payload))})
            return True
        return False

    def advance_second(self) -> list[EffectData]:
        """One online game second passes: timed effects lose a second, and the ones that run out end.

        Returns the effects that ended (as they were), so the caller can react, for example to a login ward.
        """
        if all(effect.remaining_seconds is None for effect in self._effects):
            return []
        ended: list[EffectData] = []
        running: list[EffectData] = []
        for effect in self._effects:
            if effect.remaining_seconds is None:
                running.append(effect)
            elif effect.remaining_seconds <= 1:
                ended.append(effect)
            else:
                running.append(replace(effect, remaining_seconds=effect.remaining_seconds - 1))
        self._effects = running
        self._queue(ADVANCE_EFFECTS_SQL, {"player_ids": [self._player_id]})
        return ended

    def _drop(self, matches: Callable[[EffectData], bool]) -> int:
        kept = [effect for effect in self._effects if not matches(effect)]
        dropped = len(self._effects) - len(kept)
        self._effects = kept
        return dropped

    def _queue(self, statement: TextClause, params: Mapping[str, object]) -> None:
        self._pending.append((statement, params))
        self.mark_dirty(sync=True)

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return list(self._effects), list(self._pending)  # EffectData is frozen and queued writes are never changed

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, tuple):
            effects, pending = cast(tuple[list[EffectData], list[_Write]], state)
            self._effects, self._pending = effects, pending

    @override
    def capture_write(self) -> PartWrite:
        writes, self._in_flight, self._pending = self._pending, self._pending, []

        async def write(session: DbSession) -> None:
            for statement, params in writes:
                _ = await session.execute(statement, params)

        return write

    @override
    def write_failed(self) -> None:
        """A flush failed: put its writes back in front, so the retry applies them in their original order."""
        self._pending, self._in_flight = self._in_flight + self._pending, []
        super().write_failed()
