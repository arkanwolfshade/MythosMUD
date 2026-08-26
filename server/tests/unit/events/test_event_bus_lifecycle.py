"""
Unit tests for EventBusLifecycleMixin's edge-case and exception-handling branches.

test_event_bus.py already covers the happy paths (start, stop, shutdown, idempotency).
This file targets the defensive branches in server/events/event_bus_lifecycle.py that
those happy-path tests never exercise: loop-not-running, unexpected exceptions during
start/stop/shutdown, and the best-effort cleanup in __del__.
"""

# pylint: disable=protected-access  # Reason: Testing internal lifecycle state requires accessing protected members
# pyright: reportPrivateUsage=false
# Reason: unit tests exercise EventBusLifecycleMixin protected members and private helpers.

from __future__ import annotations

import asyncio
from unittest.mock import MagicMock, patch

import pytest

from server.events.event_bus import EventBus


@pytest.fixture
def event_bus() -> EventBus:
    """Create an EventBus instance."""
    return EventBus()


def test_ensure_async_processing_loop_not_running_logs_warning(event_bus: EventBus) -> None:
    """When get_running_loop() succeeds but the loop reports not-running, warn and don't start."""
    fake_loop = MagicMock()
    fake_loop.is_running.return_value = False
    with patch("asyncio.get_running_loop", return_value=fake_loop):
        event_bus._ensure_async_processing()
    assert event_bus._running is False
    assert event_bus._processing_task is None


def test_ensure_async_processing_unexpected_exception_logged(event_bus: EventBus) -> None:
    """An unexpected (non-RuntimeError) exception while starting is caught and logged, not raised."""
    with patch("asyncio.get_running_loop", side_effect=ValueError("boom")):
        event_bus._ensure_async_processing()  # must not raise
    assert event_bus._running is False


def test_signal_shutdown_swallows_queue_full(event_bus: EventBus) -> None:
    """_signal_shutdown() tolerates a full/closed/missing queue."""
    with patch.object(event_bus._event_queue, "put_nowait", side_effect=asyncio.QueueFull):
        event_bus._signal_shutdown()  # must not raise
    assert event_bus._shutdown_event.is_set()


@pytest.mark.asyncio
async def test_cancel_processing_task_swallows_timeout(event_bus: EventBus) -> None:
    """_cancel_processing_task() tolerates asyncio.wait_for timing out."""

    async def _never_finishes() -> None:
        await asyncio.sleep(10)

    task = asyncio.create_task(_never_finishes())
    event_bus._processing_task = task
    with patch("asyncio.wait_for", side_effect=TimeoutError):
        await event_bus._cancel_processing_task()  # must not raise
    _ = task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task


def test_cancel_task_quietly_swallows_runtime_error(event_bus: EventBus) -> None:
    """_cancel_task_quietly() tolerates a task whose .done()/.cancel() raise."""
    bad_task = MagicMock()
    bad_task.done.side_effect = RuntimeError("loop closed")
    event_bus._cancel_task_quietly(bad_task)  # must not raise


@pytest.mark.asyncio
async def test_abandon_pending_tasks_cancels_and_drains(event_bus: EventBus) -> None:
    """_abandon_pending_tasks() cancels leftover tasks and tolerates gather timing out."""

    async def _never_finishes() -> None:
        await asyncio.sleep(10)

    task = asyncio.create_task(_never_finishes())
    await event_bus._abandon_pending_tasks({task})
    assert task.cancelled() or task.cancelling() > 0


@pytest.mark.asyncio
async def test_cancel_and_wait_for_active_tasks_all_already_done(event_bus: EventBus) -> None:
    """_cancel_and_wait_for_active_tasks() returns early when every active task is already done."""

    async def _noop() -> None:
        return None

    done_task = asyncio.create_task(_noop())
    await done_task
    event_bus._active_tasks.add(done_task)
    await event_bus._cancel_and_wait_for_active_tasks()  # must not raise


@pytest.mark.asyncio
async def test_cancel_and_wait_for_active_tasks_abandons_pending(event_bus: EventBus) -> None:
    """_cancel_and_wait_for_active_tasks() falls through to _abandon_pending_tasks when wait() times out."""

    async def _never_finishes() -> None:
        await asyncio.sleep(10)

    task = asyncio.create_task(_never_finishes())
    event_bus._active_tasks.add(task)
    with patch("asyncio.wait", return_value=(set(), {task})):
        await event_bus._cancel_and_wait_for_active_tasks()  # must not raise


@pytest.mark.asyncio
async def test_finalize_shutdown_swallows_logging_error(event_bus: EventBus) -> None:
    """_finalize_shutdown() tolerates the logger itself failing."""
    with patch.object(event_bus._logger, "info", side_effect=RuntimeError("logger down")):
        event_bus._finalize_shutdown()  # must not raise
    assert len(event_bus._active_tasks) == 0


@pytest.mark.asyncio
async def test_stop_processing_swallows_unexpected_exception(event_bus: EventBus) -> None:
    """_stop_processing() logs and swallows an unexpected exception from any of its steps."""
    event_bus._running = True
    with patch.object(event_bus, "_signal_shutdown", side_effect=RuntimeError("boom")):
        await event_bus._stop_processing()  # must not raise
    assert event_bus._running is False


def test_warn_shutdown_error_swallows_logging_error(event_bus: EventBus) -> None:
    """_warn_shutdown_error() tolerates the logger itself failing while reporting a shutdown error."""
    with patch.object(event_bus._logger, "warning", side_effect=RuntimeError("logger down")):
        event_bus._warn_shutdown_error(ValueError("original error"))  # must not raise


@pytest.mark.asyncio
async def test_shutdown_swallows_cancelled_error(event_bus: EventBus) -> None:
    """shutdown() treats CancelledError from _stop_processing as expected teardown noise."""
    with patch.object(event_bus, "_stop_processing", side_effect=asyncio.CancelledError):
        await event_bus.shutdown()  # must not raise
    assert event_bus._running is False


@pytest.mark.asyncio
async def test_shutdown_swallows_unexpected_exception(event_bus: EventBus) -> None:
    """shutdown() logs and swallows an unexpected exception from _stop_processing."""
    with patch.object(event_bus, "_stop_processing", side_effect=ValueError("boom")):
        await event_bus.shutdown()  # must not raise
    assert event_bus._running is False


@pytest.mark.asyncio
async def test_shutdown_finally_cancels_leftover_processing_task(event_bus: EventBus) -> None:
    """shutdown()'s finally block cancels a still-set _processing_task even after an exception."""

    async def _never_finishes() -> None:
        await asyncio.sleep(10)

    task = asyncio.create_task(_never_finishes())
    event_bus._processing_task = task
    with patch.object(event_bus, "_stop_processing", side_effect=ValueError("boom")):
        await event_bus.shutdown()
    assert task.cancelled() or task.cancelling() > 0


def test_cancel_active_tasks_best_effort_no_active_tasks(event_bus: EventBus) -> None:
    """_cancel_active_tasks_best_effort() is a no-op when there are no active tasks."""
    event_bus._cancel_active_tasks_best_effort()  # must not raise


@pytest.mark.asyncio
async def test_cancel_active_tasks_best_effort_cancels_running_tasks(event_bus: EventBus) -> None:
    """_cancel_active_tasks_best_effort() cancels active tasks when the loop is open, then clears the set."""

    async def _never_finishes() -> None:
        await asyncio.sleep(10)

    task = asyncio.create_task(_never_finishes())
    event_bus._active_tasks.add(task)
    event_bus._cancel_active_tasks_best_effort()
    assert len(event_bus._active_tasks) == 0
    _ = task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task


def test_del_no_op_when_not_running(event_bus: EventBus) -> None:
    """__del__() is a no-op when the bus was never started."""
    event_bus._running = False
    event_bus.__del__()  # must not raise


def test_del_running_swallows_logger_warning_error(event_bus: EventBus) -> None:
    """__del__() tolerates the logger itself failing while warning about ungraceful destruction."""
    event_bus._running = True
    with patch.object(event_bus._logger, "warning", side_effect=AttributeError("no logger")):
        event_bus.__del__()  # must not raise
    assert event_bus._running is False


def test_del_running_swallows_shutdown_event_set_error(event_bus: EventBus) -> None:
    """__del__() tolerates _shutdown_event.set() itself failing."""
    event_bus._running = True
    fake_shutdown_event = MagicMock()
    fake_shutdown_event.set.side_effect = RuntimeError("no loop")
    event_bus._shutdown_event = fake_shutdown_event
    event_bus.__del__()  # must not raise
    assert event_bus._running is False
