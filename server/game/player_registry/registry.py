"""
PlayerRegistry: the one place player state is read, changed and written (ADR-029).

- ``peek(pid)`` returns the live aggregate as a read-only PlayerView, or None if it is not loaded. It takes no lock
  and never awaits. ``get(pid)`` loads it first if needed.
- ``mutate(pid)`` / ``mutate_many(pids)`` run a unit of work under each player's ``asyncio.Lock`` (taken in sorted id
  order). A nested ``mutate`` of a player the current task already holds joins the open unit; asking for a player it
  does not hold raises LockOrderError, since taking a second lock mid-unit could deadlock.
- On a successful exit, a unit that needs it (``sync=True``, or a sync part changed) commits every dirty part of its
  players in one transaction before returning; on failure everything rolls back and the error propagates. Otherwise
  the changes stay dirty for the lazy sweep. Queued events are published only after a successful unit.
- ``schedule_sweep()`` (driven by the tick loop) writes dirty players in the background, at most ``flush_concurrency``
  at a time, and then evicts idle unpinned players. ``close()`` writes everything at shutdown.
"""

from __future__ import annotations

import asyncio
import time
import uuid
from collections.abc import AsyncGenerator, Awaitable, Callable, Iterable, Sequence
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field

from ...events.event_types import BaseEvent
from ...monitoring.exception_tracker import track_exception
from ...structured_logging.enhanced_logging_config import get_logger
from .aggregate import PlayerAggregate, PlayerView
from .part import DbSession, Part, PartWrite
from .player_inventory import PlayerInventoryPart
from .player_row import PlayerRowData, PlayerRowPart, fetch_player_row

logger = get_logger(__name__)

SessionFactory = Callable[[], AbstractAsyncContextManager[DbSession]]
AggregateLoader = Callable[[DbSession, uuid.UUID], Awaitable[PlayerAggregate | None]]
EventPublisher = Callable[[BaseEvent], None]


class PlayerNotFoundError(LookupError):
    """There is no player with this id."""


class LockOrderError(RuntimeError):
    """A unit of work asked for a player it does not hold; open one unit with every player instead."""


async def load_player_aggregate(session: DbSession, player_id: uuid.UUID) -> PlayerAggregate | None:
    """The default loader: every part of one player, read in one session (both parts from one row today)."""
    row = await fetch_player_row(session, player_id)
    if row is None:
        return None
    return PlayerAggregate(PlayerRowPart(PlayerRowData.from_row(row)), PlayerInventoryPart.from_row(row))


@dataclass(slots=True)
class RegistrySettings:
    """Tuning, normally from GameConfig (ADR-029 §3.4)."""

    idle_ttl_seconds: float = 60.0
    flush_concurrency: int = 4
    failure_alert_after: int = 5
    retry_base_seconds: float = 2.0
    retry_max_seconds: float = 60.0


@dataclass(slots=True)
class _Entry:
    aggregate: PlayerAggregate
    last_used: float
    pinned: bool = False
    failures: int = 0
    retry_at: float = 0.0


@dataclass(slots=True)
class _Unit:
    """An open unit of work: the task that owns it and the players it holds."""

    owner: asyncio.Task[object] | None
    aggregates: dict[uuid.UUID, PlayerAggregate] = field(default_factory=dict)
    sync: bool = False


# The unit the current task holds. Child tasks inherit this, so the owner check in _held_unit matters.
_current_unit: ContextVar[_Unit | None] = ContextVar("player_registry_unit", default=None)


def _held_unit() -> _Unit | None:
    unit = _current_unit.get()
    return unit if unit is not None and unit.owner is asyncio.current_task() else None


class PlayerRegistry:  # pylint: disable=too-many-instance-attributes  # Reason: one coordinator owning entries, locks, settings and the sweep task
    """Owns one PlayerAggregate per player that is touched (ADR-029 §3.1)."""

    _session_factory: SessionFactory
    _loader: AggregateLoader
    _publish: EventPublisher | None
    _clock: Callable[[], float]
    _settings: RegistrySettings
    _entries: dict[uuid.UUID, _Entry]
    # shortcut: one Lock per player ever touched, never deleted (deleting one while a waiter holds it would let two
    # tasks hold "the" lock); upgrade to refcounted locks if the number of distinct players gets large.
    _locks: dict[uuid.UUID, asyncio.Lock]
    _sweep_task: asyncio.Task[int] | None

    def __init__(
        self,
        session_factory: SessionFactory,
        *,
        loader: AggregateLoader = load_player_aggregate,
        publish: EventPublisher | None = None,
        settings: RegistrySettings | None = None,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._session_factory = session_factory
        self._loader = loader
        self._publish = publish
        self._settings = settings or RegistrySettings()
        self._clock = clock
        self._entries = {}
        self._locks = {}
        self._sweep_task = None

    # ---- reads ----

    def peek(self, player_id: uuid.UUID) -> PlayerView | None:
        """The loaded player, read-only, or None if not loaded. Never awaits."""
        entry = self._entries.get(player_id)
        return entry.aggregate if entry is not None else None

    async def get(self, player_id: uuid.UUID) -> PlayerView | None:
        """The player, loaded first if needed, read-only; None if there is no such player."""
        if player_id in self._entries:
            return self._entries[player_id].aggregate
        if _held_unit() is not None:
            raise LockOrderError("get() of an unloaded player inside a unit of work")
        async with self._lock(player_id):
            view = await self._load_if_needed(player_id)
        if self._settings.idle_ttl_seconds <= 0:
            self._evict_now([player_id])
        return view

    def is_loaded(self, player_id: uuid.UUID) -> bool:
        """True if the player's aggregate is in memory."""
        return player_id in self._entries

    # ---- writes ----

    @asynccontextmanager
    async def mutate(self, player_id: uuid.UUID, *, sync: bool = False) -> AsyncGenerator[PlayerAggregate]:
        """A unit of work on one player. Raises PlayerNotFoundError if there is no such player."""
        async with self.mutate_many([player_id], sync=sync) as aggregates:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            yield aggregates[0]

    @asynccontextmanager
    async def mutate_many(
        self, player_ids: Sequence[uuid.UUID], *, sync: bool = False
    ) -> AsyncGenerator[list[PlayerAggregate]]:
        """A unit of work on several players at once, in one transaction if it commits synchronously.

        The aggregates are returned in the order the ids were given.
        """
        held = _held_unit()
        if held is not None:
            missing = [pid for pid in player_ids if pid not in held.aggregates]
            if missing:
                raise LockOrderError(f"unit of work does not hold players {missing}")
            held.sync = held.sync or sync
            yield [held.aggregates[pid] for pid in player_ids]
            return
        async with self._open_unit(player_ids, sync) as unit:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            yield [unit.aggregates[pid] for pid in player_ids]

    @asynccontextmanager
    async def _open_unit(self, player_ids: Sequence[uuid.UUID], sync: bool) -> AsyncGenerator[_Unit]:
        """Lock (sorted ids), load, checkpoint; after the caller's block, commit if needed or roll back."""
        unit = _Unit(owner=asyncio.current_task(), sync=sync)
        pids = sorted(set(player_ids))
        acquired: list[asyncio.Lock] = []
        events: list[BaseEvent] = []
        try:
            await self._lock_and_load(pids, unit, acquired)
            aggregates = list(unit.aggregates.values())
            for aggregate in aggregates:
                aggregate.begin()
            token = _current_unit.set(unit)
            try:
                try:
                    yield unit
                    await self._commit_if_needed(unit, aggregates)
                except BaseException:
                    for aggregate in aggregates:
                        aggregate.rollback()
                    raise
                for aggregate in aggregates:
                    events.extend(aggregate.end())
                now = self._clock()
                for pid in pids:
                    self._entries[pid].last_used = now
            finally:
                _current_unit.reset(token)
        finally:
            for lock in reversed(acquired):
                lock.release()
            if self._settings.idle_ttl_seconds <= 0:
                self._evict_now(pids)
        self._publish_all(events)

    def _evict_now(self, player_ids: Sequence[uuid.UUID]) -> None:
        """With no idle TTL, drop each unpinned, clean player as its unit ends, so the next unit reads it fresh."""
        cutoff = self._clock()
        for pid in player_ids:
            entry = self._entries.get(pid)
            if entry is not None and self._evictable(pid, entry, cutoff):
                del self._entries[pid]

    async def _lock_and_load(self, pids: Sequence[uuid.UUID], unit: _Unit, acquired: list[asyncio.Lock]) -> None:
        """Take each player's lock in the given (sorted) order, recording it in ``acquired``, then load them."""
        for pid in pids:
            lock = self._lock(pid)
            _ = await lock.acquire()
            acquired.append(lock)
        for pid in pids:
            aggregate = await self._load_if_needed(pid)
            if aggregate is None:
                raise PlayerNotFoundError(str(pid))
            unit.aggregates[pid] = aggregate

    async def _commit_if_needed(self, unit: _Unit, aggregates: Sequence[PlayerAggregate]) -> None:
        """Commit every dirty part of the unit's players in one transaction, if the unit is synchronous."""
        if not (unit.sync or any(aggregate.sync_required for aggregate in aggregates)):
            return
        writes = [write for aggregate in aggregates for write in aggregate.take_writes()]
        if writes:
            await self._write(writes)

    def _lock(self, player_id: uuid.UUID) -> asyncio.Lock:
        lock = self._locks.get(player_id)
        if lock is None:
            lock = self._locks[player_id] = asyncio.Lock()
        return lock

    async def _load_if_needed(self, player_id: uuid.UUID) -> PlayerAggregate | None:
        """Load the player (caller holds the player's lock)."""
        entry = self._entries.get(player_id)
        if entry is not None:
            entry.last_used = self._clock()
            return entry.aggregate
        async with self._session_factory() as session:
            aggregate = await self._loader(session, player_id)
        if aggregate is not None:
            self._entries[player_id] = _Entry(aggregate=aggregate, last_used=self._clock())
        return aggregate

    def _publish_all(self, events: Iterable[BaseEvent]) -> None:
        if self._publish is None:
            return
        for event in events:
            self._publish(event)

    async def _write(self, writes: Sequence[tuple[Part, PartWrite]]) -> None:
        """Apply captured writes in one transaction."""
        async with self._session_factory() as session:
            try:
                for _part, write in writes:
                    await write(session)
                await session.commit()
            except BaseException:
                await session.rollback()
                raise

    # ---- lifecycle ----

    def pin(self, player_id: uuid.UUID) -> None:
        """Keep a loaded player in memory (online or in disconnect grace)."""
        entry = self._entries.get(player_id)
        if entry is not None:
            entry.pinned = True

    def unpin(self, player_id: uuid.UUID) -> None:
        """Let a player be evicted once idle (grace has ended)."""
        entry = self._entries.get(player_id)
        if entry is not None:
            entry.pinned = False
            entry.last_used = self._clock()

    async def evict(self, player_id: uuid.UUID) -> None:
        """Write the player if dirty, then drop it from memory (character deleted). Unpins it."""
        if _held_unit() is not None:
            raise LockOrderError("evict() inside a unit of work")
        async with self._lock(player_id):
            entry = self._entries.get(player_id)
            if entry is None:
                return
            writes = entry.aggregate.take_writes()
            if writes:
                await self._write(writes)
            del self._entries[player_id]

    def schedule_sweep(self) -> None:
        """Start a background lazy flush, unless one is still running."""
        if self._sweep_task is not None and not self._sweep_task.done():
            return
        self._sweep_task = asyncio.create_task(self.flush_dirty(), name="player_registry_sweep")

    async def flush_dirty(self) -> int:
        """Write every dirty player that is due, then evict idle ones. Returns how many players were written."""
        now = self._clock()
        due = [pid for pid, entry in self._entries.items() if entry.aggregate.dirty and entry.retry_at <= now]
        written = await self._flush_players(due)
        self._evict_idle()
        return written

    async def close(self) -> int:
        """Shutdown: stop the sweep and write every dirty player, ignoring retry backoff."""
        if self._sweep_task is not None and not self._sweep_task.done():
            _ = await asyncio.gather(self._sweep_task, return_exceptions=True)
        dirty = [pid for pid, entry in self._entries.items() if entry.aggregate.dirty]
        return await self._flush_players(dirty)

    async def _flush_players(self, player_ids: Sequence[uuid.UUID]) -> int:
        limit = asyncio.Semaphore(max(1, self._settings.flush_concurrency))

        async def flush(pid: uuid.UUID) -> bool:
            async with limit:
                return await self._flush_one(pid)

        results = await asyncio.gather(*(flush(pid) for pid in player_ids))
        return sum(results)

    async def _flush_one(self, player_id: uuid.UUID) -> bool:
        """Write one player's dirty parts. The write happens under the player's lock: written after release, an
        older captured state could land after a newer sync commit and revert it (the lost update ADR-029 removes)."""
        async with self._lock(player_id):
            entry = self._entries.get(player_id)
            if entry is None:
                return False
            writes = entry.aggregate.take_writes()
            if not writes:
                return False
            try:
                await self._write(writes)
            except Exception as error:  # pylint: disable=broad-exception-caught  # Reason: a failed lazy flush must not kill the sweep; the player stays dirty and is retried
                for part, _write in writes:
                    part.mark_dirty()
                self._record_failure(entry, error)
                return False
            entry.failures = 0
            entry.retry_at = 0.0
            return True

    def _record_failure(self, entry: _Entry, error: Exception) -> None:
        entry.failures += 1
        delay = min(self._settings.retry_base_seconds * (1 << (entry.failures - 1)), self._settings.retry_max_seconds)
        entry.retry_at = self._clock() + delay
        logger.warning(
            "Player flush failed; will retry",
            player_id=str(entry.aggregate.player_id),
            failures=entry.failures,
            retry_in_seconds=delay,
            error=str(error),
        )
        if entry.failures == self._settings.failure_alert_after:
            _ = track_exception(
                error,
                {
                    "severity": "error",
                    "handled": True,
                    "context": {"player_id": str(entry.aggregate.player_id), "failures": entry.failures},
                    "metadata": {"component": "player_registry_flush"},
                },
            )

    def _evict_idle(self) -> None:
        cutoff = self._clock() - self._settings.idle_ttl_seconds
        for pid in [pid for pid, entry in self._entries.items() if self._evictable(pid, entry, cutoff)]:
            del self._entries[pid]

    def _evictable(self, player_id: uuid.UUID, entry: _Entry, cutoff: float) -> bool:
        lock = self._locks.get(player_id)
        return (
            not entry.pinned
            and not entry.aggregate.dirty
            and not (lock is not None and lock.locked())
            and entry.last_used <= cutoff
        )
