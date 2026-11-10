"""
The lucidity part of a PlayerAggregate: the player's ``player_lucidity`` row (ADR-029 §3.2, step 5b-i).

Changes are lazy: the sweep writes them, or an enclosing sync unit commits them along with its own parts. Each change
also queues a ``lucidity_adjustment_log`` row; the ledger is outside the aggregate, but its rows are written in the
same transaction as the lucidity they record. A player with no row yet has the starting values, and their first
change creates the row (``upsert_player_lucidity``).
"""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import text

from ...constants.lucidity import STARTING_LCD
from .part import DbSession, Part, PartWrite

# One row per player: the lucidity columns (NULL with no row yet) plus the cooldowns, exposures (5b-ii) and
# effects (6d) as JSON.
LOAD_LUCIDITY_SQL = text(
    """
    SELECT
        current_lcd, current_tier, liabilities, last_updated_at, catatonia_entered_at, cooldowns, exposures, effects
    FROM get_player_lucidity_state(:id)
    """
)

UPSERT_LUCIDITY_SQL = text(
    """
    CALL upsert_player_lucidity(
        :player_id, :current_lcd, :current_tier, :liabilities, :last_updated_at, :catatonia_entered_at
    )
    """
)

ADD_ADJUSTMENT_LOG_SQL = text(
    "CALL add_lucidity_adjustment_log(:player_id, :delta, :reason_code, :metadata, :location_id, :created_at)"
)


@dataclass(frozen=True, slots=True)
class LucidityData:
    """A player's lucidity, as the aggregate holds it. ``liabilities`` is the stored JSON list of stacks."""

    lcd: int = STARTING_LCD
    tier: str = "lucid"
    liabilities: str = "[]"
    catatonia_entered_at: datetime | None = None
    last_updated_at: datetime | None = None

    @classmethod
    def from_row(cls, row: Mapping[str, object] | None) -> LucidityData:
        """Build from a ``get_player_lucidity_state`` row; the starting values if the player has no lucidity yet."""
        if row is None or row.get("current_lcd") is None:
            return cls()
        return cls(
            lcd=int(cast(int, row["current_lcd"])),
            tier=str(row["current_tier"]),
            liabilities=str(row.get("liabilities") or "[]"),
            catatonia_entered_at=cast(datetime | None, row.get("catatonia_entered_at")),
            last_updated_at=cast(datetime | None, row.get("last_updated_at")),
        )


class PlayerLucidityPart(Part):
    """The player's lucidity, with read access, a lazy mutator, and the ledger rows waiting to be written."""

    __slots__: tuple[str, ...] = ("_data", "_in_flight", "_ledger", "_player_id")

    _player_id: uuid.UUID
    _data: LucidityData
    _ledger: list[dict[str, object]]
    _in_flight: list[dict[str, object]]

    def __init__(self, player_id: uuid.UUID, data: LucidityData | None = None) -> None:
        super().__init__()
        self._player_id = player_id
        self._data = data if data is not None else LucidityData()
        self._ledger = []
        self._in_flight = []

    # ---- reads ----

    @property
    def data(self) -> LucidityData:
        """The current lucidity. Change it with ``set``."""
        return self._data

    @property
    def lcd(self) -> int:
        """Current lucidity (LCD)."""
        return self._data.lcd

    @property
    def tier(self) -> str:
        """Current tier (lucid, uneasy, fractured, deranged, catatonic)."""
        return self._data.tier

    # ---- mutators ----

    def set(
        self,
        *,
        lcd: int | None = None,
        tier: str | None = None,
        liabilities: str | None = None,
        catatonia_entered_at: datetime | None = None,
        clear_catatonia: bool = False,
    ) -> LucidityData:
        """Change the fields given (lazy); ``clear_catatonia`` sets ``catatonia_entered_at`` back to None."""
        updated = replace(
            self._data,
            lcd=lcd if lcd is not None else self._data.lcd,
            tier=tier if tier is not None else self._data.tier,
            liabilities=liabilities if liabilities is not None else self._data.liabilities,
            catatonia_entered_at=None
            if clear_catatonia
            else (catatonia_entered_at if catatonia_entered_at is not None else self._data.catatonia_entered_at),
        )
        if updated != self._data:
            self._data = replace(updated, last_updated_at=datetime.now(UTC))
            self.mark_dirty()
        return self._data

    def log(self, delta: int, reason_code: str, metadata: str, location_id: str | None) -> None:
        """Queue a ``lucidity_adjustment_log`` row, written with the part's next write."""
        self._ledger.append(
            {
                "player_id": str(self._player_id),
                "delta": delta,
                "reason_code": reason_code,
                "metadata": metadata,
                "location_id": location_id,
                "created_at": datetime.now(UTC),
            }
        )
        self.mark_dirty()

    def upsert_params(self) -> dict[str, object]:
        """``upsert_player_lucidity`` parameters."""
        return {
            "player_id": str(self._player_id),
            "current_lcd": self._data.lcd,
            "current_tier": self._data.tier,
            "liabilities": self._data.liabilities,
            "last_updated_at": self._data.last_updated_at or datetime.now(UTC),
            "catatonia_entered_at": self._data.catatonia_entered_at,
        }

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return self._data, list(self._ledger)  # LucidityData is frozen and ledger rows are never changed

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, tuple):
            data, ledger = cast(tuple[LucidityData, list[dict[str, object]]], state)
            self._data, self._ledger = data, ledger

    @override
    def capture_write(self) -> PartWrite:
        params = self.upsert_params()
        rows, self._in_flight, self._ledger = self._ledger, self._ledger, []

        async def write(session: DbSession) -> None:
            _ = await session.execute(UPSERT_LUCIDITY_SQL, params)
            for row in rows:
                _ = await session.execute(ADD_ADJUSTMENT_LOG_SQL, row)

        return write

    @override
    def write_failed(self) -> None:
        """A lazy flush failed: put its ledger rows back in front, so the retry writes them."""
        self._ledger, self._in_flight = self._in_flight + self._ledger, []
        super().write_failed()
