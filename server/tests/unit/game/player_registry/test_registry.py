"""Unit tests for PlayerRegistry: units of work, locking, re-entrancy, sync and lazy writes, the sweep, eviction."""

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Mapping
from unittest.mock import patch

import pytest

from server.events.event_types import BaseEvent, PlayerEnteredRoom
from server.game.player_registry import (
    LockOrderError,
    PlayerNotFoundError,
    PlayerRegistry,
    PlayerRowData,
    RegistrySettings,
)
from server.schemas.shared import InventorySchemaValidationError

from .fakes import FakeDatabase, FakeLoader, row_data

AMULET = {"item_id": "jade_amulet", "item_name": "Jade Amulet", "slot_type": "backpack", "quantity": 1}


class _Clock:
    def __init__(self) -> None:
        self.now: float = 1000.0

    def __call__(self) -> float:
        return self.now


def _registry(
    rows: dict[uuid.UUID, PlayerRowData], db: FakeDatabase | None = None, settings: RegistrySettings | None = None
) -> tuple[PlayerRegistry, FakeDatabase, list[BaseEvent], _Clock]:
    database = db or FakeDatabase()
    published: list[BaseEvent] = []
    clock = _Clock()
    registry = PlayerRegistry(
        database.session, loader=FakeLoader(rows), publish=published.append, settings=settings, clock=clock
    )
    return registry, database, published, clock


def _last_write(db: FakeDatabase) -> Mapping[str, object]:
    params = db.executed[-1]
    assert params is not None
    return params


def _one() -> tuple[uuid.UUID, dict[uuid.UUID, PlayerRowData]]:
    pid = uuid.uuid4()
    return pid, {pid: row_data(pid)}


def _event(pid: uuid.UUID) -> PlayerEnteredRoom:
    return PlayerEnteredRoom(player_id=str(pid), room_id="room")


# ---- loading and reads ----


async def test_get_loads_once_and_peek_never_loads() -> None:
    pid, rows = _one()
    loader = FakeLoader(rows)
    db = FakeDatabase()
    registry = PlayerRegistry(db.session, loader=loader)

    assert registry.peek(pid) is None
    view = await registry.get(pid)
    again = await registry.get(pid)

    assert view is not None and view is again
    assert view.row.name == "Tester"
    assert loader.loads[pid] == 1
    assert registry.peek(pid) is view


async def test_unknown_player() -> None:
    registry, _db, _events, _clock = _registry({})
    assert await registry.get(uuid.uuid4()) is None
    with pytest.raises(PlayerNotFoundError):
        async with registry.mutate(uuid.uuid4()):
            pass


# ---- lazy and sync writes ----


async def test_lazy_change_is_written_by_the_sweep_not_the_unit() -> None:
    pid, rows = _one()
    registry, db, published, _clock = _registry(rows)

    async with registry.mutate(pid) as player:
        player.row.set_stat("current_dp", 5)
        player.emit(_event(pid))

    assert db.commits == 0
    assert published and published[0].event_type == "PlayerEnteredRoom"  # published once the unit succeeded
    assert await registry.flush_dirty() == 1
    assert db.commits == 1
    assert '"current_dp": 5' in str(_last_write(db)["stats"])
    assert await registry.flush_dirty() == 0  # nothing left to write


async def test_inventory_change_commits_before_the_unit_returns() -> None:
    pid, rows = _one()
    registry, db, _events, _clock = _registry(rows)

    async with registry.mutate(pid) as player:
        player.row.set_inventory([*player.row.inventory, AMULET])

    assert db.commits == 1
    assert "Jade Amulet" in str(_last_write(db)["inventory_json"])
    assert await registry.flush_dirty() == 0  # the sync commit cleared the dirty flags


async def test_sync_flag_forces_a_lazy_change_to_commit() -> None:
    pid, rows = _one()
    registry, db, _events, _clock = _registry(rows)

    async with registry.mutate(pid, sync=True) as player:
        player.row.set_stat("current_dp", 7)

    assert db.commits == 1


async def test_failed_sync_commit_rolls_back_memory_and_drops_events() -> None:
    pid, rows = _one()
    registry, db, published, _clock = _registry(rows, FakeDatabase(fail_commits=1))

    with pytest.raises(RuntimeError, match="database unavailable"):
        async with registry.mutate(pid) as player:
            player.row.set_stat("current_dp", 3)
            player.row.set_inventory([AMULET])
            player.emit(_event(pid))

    view = registry.peek(pid)
    assert view is not None
    assert [stack["item_id"] for stack in view.row.inventory] == ["sling"]
    assert view.row.stats["current_dp"] == 20
    assert db.rollbacks == 1
    assert published == []
    assert await registry.flush_dirty() == 0  # the rolled-back change is not pending either


async def test_exception_in_the_block_rolls_back_without_writing() -> None:
    pid, rows = _one()
    registry, db, published, _clock = _registry(rows)

    with pytest.raises(ValueError, match="boom"):
        async with registry.mutate(pid) as player:
            player.row.set_inventory([AMULET])
            player.emit(_event(pid))
            raise ValueError("boom")

    assert db.executed == []
    assert published == []
    view = registry.peek(pid)
    assert view is not None and view.row.inventory[0]["item_id"] == "sling"


async def test_invalid_inventory_is_rejected_inside_the_command() -> None:
    pid, rows = _one()
    registry, db, _events, _clock = _registry(rows)

    with pytest.raises(InventorySchemaValidationError):
        async with registry.mutate(pid) as player:
            player.row.set_inventory([{"item_id": "x"}])

    assert db.executed == []


# ---- locking and re-entrancy ----


async def test_units_on_one_player_are_serialized() -> None:
    pid, rows = _one()
    registry, _db, _events, _clock = _registry(rows)
    order: list[str] = []
    first_inside = asyncio.Event()
    release_first = asyncio.Event()

    async def first() -> None:
        async with registry.mutate(pid):
            order.append("first in")
            first_inside.set()
            _ = await release_first.wait()
            order.append("first out")

    async def second() -> None:
        _ = await first_inside.wait()
        async with registry.mutate(pid):
            order.append("second in")

    tasks = [asyncio.create_task(first()), asyncio.create_task(second())]
    _ = await first_inside.wait()
    await asyncio.sleep(0)
    release_first.set()
    _ = await asyncio.gather(*tasks)

    assert order == ["first in", "first out", "second in"]


async def test_nested_mutate_joins_the_open_unit_and_can_escalate_to_sync() -> None:
    pid, rows = _one()
    registry, db, published, _clock = _registry(rows)

    async with registry.mutate(pid) as outer:
        outer.row.set_stat("current_dp", 9)
        async with registry.mutate(pid, sync=True) as inner:
            assert inner is outer
            inner.emit(_event(pid))
        assert db.commits == 0  # only the outermost block commits

    assert db.commits == 1
    assert len(published) == 1


async def test_a_child_task_does_not_inherit_the_lock() -> None:
    """A task created inside a unit inherits the contextvar, but must wait for the lock, not join the unit."""
    pid, rows = _one()
    registry, _db, _events, _clock = _registry(rows)
    order: list[str] = []

    async def child() -> None:
        async with registry.mutate(pid):
            order.append("child")

    async with registry.mutate(pid):
        task = asyncio.create_task(child())
        await asyncio.sleep(0)
        order.append("parent")
    await task

    assert order == ["parent", "child"]


async def test_asking_for_another_player_mid_unit_is_refused() -> None:
    a, b = uuid.uuid4(), uuid.uuid4()
    registry, _db, _events, _clock = _registry({a: row_data(a), b: row_data(b)})

    async with registry.mutate(a):
        with pytest.raises(LockOrderError):
            async with registry.mutate(b):
                pass


async def test_mutate_many_commits_all_players_in_one_transaction() -> None:
    a, b = uuid.uuid4(), uuid.uuid4()
    registry, db, _events, _clock = _registry({a: row_data(a), b: row_data(b)})

    async with registry.mutate_many([b, a]) as (pb, pa):
        assert pb.player_id == b and pa.player_id == a
        pa.row.set_inventory([])
        pb.row.set_inventory([*pb.row.inventory, AMULET])

    assert db.commits == 1
    assert len(db.executed) == 2


async def test_opposite_order_mutate_many_does_not_deadlock() -> None:
    a, b = uuid.uuid4(), uuid.uuid4()
    registry, _db, _events, _clock = _registry({a: row_data(a), b: row_data(b)})

    async def touch(ids: list[uuid.UUID]) -> None:
        async with registry.mutate_many(ids):
            await asyncio.sleep(0)

    _ = await asyncio.wait_for(asyncio.gather(touch([a, b]), touch([b, a])), timeout=1)


# ---- the lost update ADR-029 removes ----


async def test_a_tick_and_a_pickup_interleaved_keep_both_changes() -> None:
    """The 2026-10-26 e2e failure: a heal tick saved a stale copy 2 ms after a pickup, wiping the amulet."""
    pid, rows = _one()
    registry, db, _events, _clock = _registry(rows)
    tick_has_read = asyncio.Event()

    async def heal_tick() -> None:
        async with registry.mutate(pid) as player:
            dp = int(str(player.row.stats["current_dp"]))
            tick_has_read.set()
            await asyncio.sleep(0)  # the heal's own await, where the pickup used to slip in
            player.row.set_stat("current_dp", dp + 5)

    async def pickup() -> None:
        _ = await tick_has_read.wait()
        async with registry.mutate(pid) as player:
            player.row.set_inventory([*player.row.inventory, AMULET])

    _ = await asyncio.gather(heal_tick(), pickup())
    _ = await registry.flush_dirty()

    last = _last_write(db)
    assert "Jade Amulet" in str(last["inventory_json"])
    assert '"current_dp": 25' in str(last["stats"])


# ---- the sweep ----


async def test_failed_lazy_flush_stays_dirty_backs_off_and_alerts() -> None:
    pid, rows = _one()
    registry, db, _events, clock = _registry(
        rows, FakeDatabase(fail_commits=2), RegistrySettings(failure_alert_after=2, retry_base_seconds=2.0)
    )
    async with registry.mutate(pid) as player:
        player.row.set_stat("current_dp", 4)

    with patch("server.game.player_registry.registry.track_exception") as alert:
        assert await registry.flush_dirty() == 0
        assert await registry.flush_dirty() == 0  # backing off: not due yet
        clock.now += 2.0
        assert await registry.flush_dirty() == 0  # second failure: alert
        alert.assert_called_once()
        clock.now += 4.0
        assert await registry.flush_dirty() == 1

    assert '"current_dp": 4' in str(_last_write(db)["stats"])


async def test_schedule_sweep_skips_while_one_is_running() -> None:
    pid, rows = _one()
    registry, _db, _events, _clock = _registry(rows)
    async with registry.mutate(pid) as player:
        player.row.set_stat("current_dp", 4)

    registry.schedule_sweep()
    first = registry._sweep_task  # pyright: ignore[reportPrivateUsage]  # Reason: TEST_DOUBLE - asserting the skip-if-running rule # Appropriate because: the running task is the only observable of a skipped sweep
    registry.schedule_sweep()
    assert registry._sweep_task is first  # pyright: ignore[reportPrivateUsage]  # Reason: TEST_DOUBLE - as above # Appropriate because: the running task is the only observable of a skipped sweep
    await asyncio.sleep(0.01)
    assert first is not None and first.done()


async def test_flush_concurrency_is_bounded() -> None:
    ids = [uuid.uuid4() for _ in range(5)]
    in_flight = 0
    peak = 0
    registry, _db, _events, _clock = _registry(
        {pid: row_data(pid) for pid in ids}, settings=RegistrySettings(flush_concurrency=2)
    )
    for pid in ids:
        async with registry.mutate(pid) as player:
            player.row.set_stat("current_dp", 1)

    async def slow_write(_self: PlayerRegistry, _writes: object) -> None:
        nonlocal in_flight, peak
        in_flight += 1
        peak = max(peak, in_flight)
        await asyncio.sleep(0.01)
        in_flight -= 1

    with patch.object(PlayerRegistry, "_write", new=slow_write):
        assert await registry.flush_dirty() == 5

    assert peak == 2


async def test_close_writes_everything_ignoring_backoff() -> None:
    pid, rows = _one()
    registry, db, _events, _clock = _registry(rows, FakeDatabase(fail_commits=1))
    async with registry.mutate(pid) as player:
        player.row.set_stat("current_dp", 2)
    _ = await registry.flush_dirty()  # fails, backs off

    assert await registry.close() == 1
    assert db.commits == 1


# ---- eviction ----


async def test_idle_unpinned_clean_players_are_evicted_after_the_ttl() -> None:
    pid, rows = _one()
    registry, _db, _events, clock = _registry(rows, settings=RegistrySettings(idle_ttl_seconds=60.0))
    _ = await registry.get(pid)

    clock.now += 59.0
    _ = await registry.flush_dirty()
    assert registry.is_loaded(pid)
    clock.now += 2.0
    _ = await registry.flush_dirty()
    assert not registry.is_loaded(pid)


async def test_pinned_and_dirty_players_are_never_evicted() -> None:
    pinned, dirty = uuid.uuid4(), uuid.uuid4()
    registry, _db, _events, clock = _registry(
        {pinned: row_data(pinned), dirty: row_data(dirty)},
        FakeDatabase(fail_commits=99),
        RegistrySettings(idle_ttl_seconds=1.0),
    )
    _ = await registry.get(pinned)
    registry.pin(pinned)
    async with registry.mutate(dirty) as player:
        player.row.set_stat("current_dp", 1)

    clock.now += 10_000.0
    _ = await registry.flush_dirty()  # the dirty player's flush fails, so it stays dirty

    assert registry.is_loaded(pinned)
    assert registry.is_loaded(dirty)

    registry.unpin(pinned)
    clock.now += 2.0
    _ = await registry.flush_dirty()
    assert not registry.is_loaded(pinned)


async def test_evict_writes_a_dirty_player_then_drops_it() -> None:
    pid, rows = _one()
    registry, db, _events, _clock = _registry(rows)
    async with registry.mutate(pid) as player:
        player.row.set_stat("current_dp", 1)

    await registry.evict(pid)

    assert db.commits == 1
    assert not registry.is_loaded(pid)
