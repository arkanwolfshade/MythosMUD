"""Test doubles for the player registry: the shared in-memory database, and a loader over a dict of rows."""

from __future__ import annotations

import uuid
from collections.abc import Mapping

from server.game.player_registry import DbSession, PlayerAggregate, PlayerRowData
from server.tests.fixtures.shared.player_registry import FakeDatabase, aggregate, raw_row

__all__ = ["FakeDatabase", "FakeLoader", "aggregate", "raw_row", "row_data"]


def row_data(player_id: uuid.UUID | None = None, **overrides: object) -> PlayerRowData:
    """A valid PlayerRowData with full DP (the players-row part of ``raw_row``)."""
    return PlayerRowData.from_row(raw_row(player_id, **overrides))


class FakeLoader:
    """An AggregateLoader over raw ``get_player_by_id`` rows that counts loads per player."""

    def __init__(self, rows: dict[uuid.UUID, Mapping[str, object]]) -> None:
        self.rows: dict[uuid.UUID, Mapping[str, object]] = rows
        self.loads: dict[uuid.UUID, int] = {}

    async def __call__(self, _session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
        self.loads[player_id] = self.loads.get(player_id, 0) + 1
        row = self.rows.get(player_id)
        return aggregate(row) if row is not None else None
