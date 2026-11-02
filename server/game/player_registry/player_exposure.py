"""
The exposure part of a PlayerAggregate: the player's ``lucidity_exposure_state`` rows (ADR-029 §3.2, step 5b-ii).

How many times the player has met each kind of Mythos entity: the first sight costs most, repeats less, and enough
of them acclimate the player. Changes are synchronous, like the cooldowns they sit beside; a write upserts every
archetype the player has met (``upsert_lucidity_exposures``). Exposure is never forgotten, so nothing is deleted.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import text

from .part import DbSession, Part, PartWrite
from .player_cooldowns import parse_timestamp

UPSERT_EXPOSURES_SQL = text("CALL upsert_lucidity_exposures(:player_id, CAST(:exposures AS jsonb))")


@dataclass(frozen=True, slots=True)
class Exposure:
    """One archetype the player has met: how many times, and when last."""

    encounter_count: int
    last_encounter_at: datetime


class PlayerExposurePart(Part):
    """The player's encounter counts by entity archetype, with read access and a synchronous mutator."""

    __slots__: tuple[str, ...] = ("_exposures", "_player_id")

    _player_id: uuid.UUID
    _exposures: dict[str, Exposure]

    def __init__(self, player_id: uuid.UUID, exposures: Mapping[str, Exposure] | None = None) -> None:
        super().__init__()
        self._player_id = player_id
        self._exposures = dict(exposures or {})

    @classmethod
    def from_json(cls, player_id: uuid.UUID, rows: object) -> PlayerExposurePart:
        """Build from the ``exposures`` column of ``get_player_lucidity_state``."""
        entries = cast(Sequence[Mapping[str, object]], json.loads(rows) if isinstance(rows, str) else rows or [])
        return cls(
            player_id,
            {
                str(row["entity_archetype"]): Exposure(
                    int(cast(int, row["encounter_count"])), parse_timestamp(row["last_encounter_at"])
                )
                for row in entries
            },
        )

    # ---- reads ----

    def encounter_count(self, entity_archetype: str) -> int:
        """How many times the player has met ``entity_archetype`` (0 if never)."""
        exposure = self._exposures.get(entity_archetype)
        return exposure.encounter_count if exposure is not None else 0

    # ---- mutators ----

    def record_encounter(self, entity_archetype: str, now: datetime | None = None) -> int:
        """Count one more encounter with ``entity_archetype``; returns the new count."""
        count = self.encounter_count(entity_archetype) + 1
        self._exposures[entity_archetype] = Exposure(count, now or datetime.now(UTC))
        self.mark_dirty(sync=True)
        return count

    def write_params(self) -> dict[str, object]:
        """``upsert_lucidity_exposures`` parameters: the player and every archetype they have met."""
        rows = [
            {
                "entity_archetype": archetype,
                "encounter_count": exposure.encounter_count,
                "last_encounter_at": exposure.last_encounter_at.isoformat(),
            }
            for archetype, exposure in sorted(self._exposures.items())
        ]
        return {"player_id": str(self._player_id), "exposures": json.dumps(rows)}

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return dict(self._exposures)  # Exposure is frozen, so a shallow copy is a snapshot

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, dict):
            self._exposures = cast(dict[str, Exposure], state)

    @override
    def capture_write(self) -> PartWrite:
        params = self.write_params()

        async def write(session: DbSession) -> None:
            _ = await session.execute(UPSERT_EXPOSURES_SQL, params)

        return write
