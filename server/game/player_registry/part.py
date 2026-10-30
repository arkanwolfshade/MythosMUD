"""
One slice of a player's state inside a PlayerAggregate (ADR-029 §3.2).

A part owns its data, tracks whether it has changes the database does not have yet (``dirty``), and whether those
changes must reach the database before the command that made them returns (``sync_required``). It also knows how
to snapshot itself so a failed unit of work can be rolled back, and how to capture a write of its current state.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping, Sequence
from typing import Protocol


class DbResultRows(Protocol):
    """The row view of a query result that the part mappers read."""

    def first(self) -> Mapping[str, object] | None:
        """The first row, or None."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    def all(self) -> Sequence[Mapping[str, object]]:
        """Every row."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class DbResult(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """The slice of a SQLAlchemy result the part mappers read."""

    def mappings(self) -> DbResultRows:
        """Rows as mappings."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type


class DbSession(Protocol):
    """The slice of an AsyncSession the registry and part mappers use."""

    async def execute(self, statement: object, params: Mapping[str, object] | None = None) -> DbResult:
        """Run one statement (a stored procedure call)."""
        ...  # pylint: disable=unnecessary-ellipsis  # Reason: basedpyright requires an explicit stub body for a non-None Protocol return type

    async def commit(self) -> None:
        """Commit the transaction."""

    async def rollback(self) -> None:
        """Roll the transaction back."""


# A captured write: the part's state at capture time, applied to a session by the flusher.
PartWrite = Callable[[DbSession], Awaitable[None]]


class Part:
    """Base for aggregate parts: dirty and sync flags, plus the begin/rollback/end checkpoint protocol.

    Subclasses implement ``_copy_state`` / ``_restore_state`` (a deep copy of their data) and ``capture_write``.
    """

    __slots__: tuple[str, ...] = ("_checkpoint", "_dirty", "_sync_required")

    _dirty: bool
    _sync_required: bool
    _checkpoint: tuple[object, bool, bool] | None

    def __init__(self) -> None:
        self._dirty = False
        self._sync_required = False
        self._checkpoint = None

    @property
    def dirty(self) -> bool:
        """True if the part has changes the database does not have yet."""
        return self._dirty

    @property
    def sync_required(self) -> bool:
        """True if the pending changes must be committed before the current command returns."""
        return self._sync_required

    def mark_dirty(self, *, sync: bool = False) -> None:
        """Record a change; ``sync`` makes the enclosing unit of work commit before it returns."""
        self._dirty = True
        self._sync_required = self._sync_required or sync

    def begin(self) -> None:
        """Remember the current state, so a failed unit of work can put it back."""
        self._checkpoint = (self._copy_state(), self._dirty, self._sync_required)

    def rollback(self) -> None:
        """Put back the state remembered by ``begin``."""
        if self._checkpoint is None:
            return
        state, self._dirty, self._sync_required = self._checkpoint
        self._restore_state(state)
        self._checkpoint = None

    def end(self) -> None:
        """Forget the checkpoint: the unit of work succeeded."""
        self._checkpoint = None

    def take_write(self) -> PartWrite | None:
        """If dirty, capture a write of the current state and clear the flags; else None."""
        if not self._dirty:
            return None
        write = self.capture_write()
        self._dirty = False
        self._sync_required = False
        return write

    def _copy_state(self) -> object:
        raise NotImplementedError

    def _restore_state(self, state: object) -> None:
        _ = state
        raise NotImplementedError

    def capture_write(self) -> PartWrite:
        """A write of the part's current state (taken now; applied later by the flusher)."""
        raise NotImplementedError
