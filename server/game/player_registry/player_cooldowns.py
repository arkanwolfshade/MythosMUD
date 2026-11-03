"""
The cooldowns parts of a PlayerAggregate: the player's ``lucidity_cooldowns`` rows (ADR-029 §3.2, step 5b-ii) and
their ``corruption_cooldowns`` rows (step 5c), one part each, told apart by the statement that writes them.

A cooldown is an action code and the time it expires: recovery rites, consumables, involuntary flee, hallucination
timers, the debrief's long-lived ``DEBRIEF_PENDING`` flag, and corruption's cleanse. Every change is synchronous: a
cooldown gates the next command, so it must be in the database before the command that set it returns. A write
replaces the player's whole set, so a retried write never needs to know which cooldown changed.
"""

from __future__ import annotations

import json
import uuid
from collections.abc import Mapping, Sequence
from datetime import UTC, datetime
from typing import cast, override

from sqlalchemy import TextClause, text

from .part import DbSession, Part, PartWrite

REPLACE_COOLDOWNS_SQL = text("CALL replace_lucidity_cooldowns(:player_id, CAST(:cooldowns AS jsonb))")
REPLACE_CORRUPTION_COOLDOWNS_SQL = text("CALL replace_corruption_cooldowns(:player_id, CAST(:cooldowns AS jsonb))")
LOAD_CORRUPTION_COOLDOWNS_SQL = text("SELECT get_player_corruption_cooldowns(:id) AS cooldowns")


def parse_timestamp(raw: object) -> datetime:
    """A timestamp from the database (a datetime) or from its JSON (an ISO string), as an aware UTC datetime."""
    value = raw if isinstance(raw, datetime) else datetime.fromisoformat(str(raw))
    return value if value.tzinfo is not None else value.replace(tzinfo=UTC)


class PlayerCooldownsPart(Part):
    """One table's cooldowns by action code, with read access and synchronous mutators."""

    __slots__: tuple[str, ...] = ("_cooldowns", "_player_id", "_write_sql")

    _player_id: uuid.UUID
    _cooldowns: dict[str, datetime]
    _write_sql: TextClause

    def __init__(
        self,
        player_id: uuid.UUID,
        cooldowns: Mapping[str, datetime] | None = None,
        *,
        write_sql: TextClause = REPLACE_COOLDOWNS_SQL,
    ) -> None:
        super().__init__()
        self._player_id = player_id
        self._cooldowns = dict(cooldowns or {})
        self._write_sql = write_sql

    @classmethod
    def from_json(
        cls, player_id: uuid.UUID, rows: object, *, write_sql: TextClause = REPLACE_COOLDOWNS_SQL
    ) -> PlayerCooldownsPart:
        """Build from a JSON array of ``{action_code, expires_at}`` (or its text), as the load functions return it."""
        entries = cast(Sequence[Mapping[str, object]], json.loads(rows) if isinstance(rows, str) else rows or [])
        cooldowns = {str(row["action_code"]): parse_timestamp(row["expires_at"]) for row in entries}
        return cls(player_id, cooldowns, write_sql=write_sql)

    # ---- reads ----

    def expires_at(self, action_code: str) -> datetime | None:
        """When the cooldown on ``action_code`` expires, or None if there is none."""
        return self._cooldowns.get(action_code)

    def active(self, action_code: str, now: datetime) -> bool:
        """True while the cooldown on ``action_code`` has not expired."""
        expires = self._cooldowns.get(action_code)
        return expires is not None and expires > now

    # ---- mutators ----

    def set(self, action_code: str, expires_at: datetime) -> None:
        """Start (or move) the cooldown on ``action_code``."""
        expires = parse_timestamp(expires_at)
        if self._cooldowns.get(action_code) != expires:
            self._cooldowns[action_code] = expires
            self.mark_dirty(sync=True)

    def clear(self, action_code: str) -> bool:
        """Remove the cooldown on ``action_code``; True if there was one."""
        if self._cooldowns.pop(action_code, None) is None:
            return False
        self.mark_dirty(sync=True)
        return True

    def clear_prefix(self, prefix: str) -> int:
        """Remove every cooldown whose action code starts with ``prefix``; returns how many."""
        doomed = [code for code in self._cooldowns if code.startswith(prefix)]
        for code in doomed:
            del self._cooldowns[code]
        if doomed:
            self.mark_dirty(sync=True)
        return len(doomed)

    def write_params(self) -> dict[str, object]:
        """The replace procedure's parameters: the player and every cooldown they hold."""
        rows = [{"action_code": code, "expires_at": at.isoformat()} for code, at in sorted(self._cooldowns.items())]
        return {"player_id": str(self._player_id), "cooldowns": json.dumps(rows)}

    # ---- Part protocol ----

    @override
    def _copy_state(self) -> object:
        return dict(self._cooldowns)  # datetimes are immutable, so a shallow copy is a snapshot

    @override
    def _restore_state(self, state: object) -> None:
        if isinstance(state, dict):
            self._cooldowns = cast(dict[str, datetime], state)

    @override
    def capture_write(self) -> PartWrite:
        params = self.write_params()

        async def write(session: DbSession) -> None:
            _ = await session.execute(self._write_sql, params)

        return write
