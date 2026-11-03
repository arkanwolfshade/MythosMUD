"""
An append-only ledger part of a PlayerAggregate (ADR-029 §3.2): rows queued by a unit and inserted with its write.

The ledger is not player state the aggregate reads back; it records the changes other parts make. So a part only
queues rows, and the unit that changed the value writes them in the same transaction. A failed lazy flush puts its
rows back for the retry. Used for ``corruption_adjustment_log`` (step 5c); the statement says which table.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import TextClause, text

from .part import DbSession, Part, PartWrite

ADD_CORRUPTION_ADJUSTMENT_LOG_SQL = text(
    "CALL add_corruption_adjustment_log(:player_id, :delta, :reason_code, :metadata, :location_id, :created_at)"
)


class PlayerLedgerPart(Part):
    """Ledger rows waiting for the unit's write: ``{player_id, delta, reason_code, metadata, location_id, created_at}``."""

    __slots__: tuple[str, ...] = ("_in_flight", "_insert_sql", "_pending", "_player_id")

    _player_id: uuid.UUID
    _insert_sql: TextClause
    _pending: list[dict[str, object]]
    _in_flight: list[dict[str, object]]

    def __init__(self, player_id: uuid.UUID, insert_sql: TextClause = ADD_CORRUPTION_ADJUSTMENT_LOG_SQL) -> None:
        super().__init__()
        self._player_id = player_id
        self._insert_sql = insert_sql
        self._pending = []
        self._in_flight = []

    def log(self, delta: int, reason_code: str, metadata: str, location_id: str | None, *, sync: bool = False) -> None:
        """Queue one ledger row, written with the unit (``sync`` makes the unit commit before it returns)."""
        self._pending.append(
            {
                "player_id": str(self._player_id),
                "delta": delta,
                "reason_code": reason_code,
                "metadata": metadata,
                "location_id": location_id,
                "created_at": datetime.now(UTC),
            }
        )
        self.mark_dirty(sync=sync)

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return list(self._pending)  # queued rows are never changed, so a shallow copy is a snapshot

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, list):
            self._pending = cast(list[dict[str, object]], state)

    @override
    def capture_write(self) -> PartWrite:
        rows, self._in_flight, self._pending = self._pending, self._pending, []
        statement = self._insert_sql

        async def write(session: DbSession) -> None:
            for row in rows:
                _ = await session.execute(statement, row)

        return write

    @override
    def write_failed(self) -> None:
        """A lazy flush failed: put its rows back in front, so the retry writes them."""
        self._pending, self._in_flight = self._in_flight + self._pending, []
        super().write_failed()
