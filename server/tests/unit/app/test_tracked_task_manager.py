"""Unit tests for TrackedTaskManager."""

from __future__ import annotations

import asyncio
from unittest.mock import MagicMock

import pytest

from server.app.tracked_task_manager import (
    TrackedTaskManager,
    get_global_tracked_manager,
    memory_leak_prevention_channel_start_session,
    patch_asyncio_create_task_with_tracking,
    reset_global_tracked_manager,
)


@pytest.fixture(autouse=True)
def reset_global():
    reset_global_tracked_manager()
    yield
    reset_global_tracked_manager()


@pytest.mark.asyncio
async def test_create_tracked_task_runs_coro():
    manager = TrackedTaskManager()
    seen = []

    async def work():
        seen.append(True)

    task = manager.create_tracked_task(work(), task_name="test_work")
    await task
    assert seen == [True]
    assert manager.actively_tracked_task_count >= 0


@pytest.mark.asyncio
async def test_create_tracked_task_with_registry():
    registry = MagicMock()
    replacement = asyncio.create_task(asyncio.sleep(0))
    registry.register_task = MagicMock(return_value=replacement)
    manager = TrackedTaskManager(task_registry=registry)

    async def work():
        return 42

    task = manager.create_tracked_task(work(), task_name="reg_work")
    assert task is replacement
    registry.register_task.assert_called_once()


@pytest.mark.asyncio
async def test_create_tracked_task_registry_failure_falls_back():
    registry = MagicMock()
    registry.register_task = MagicMock(side_effect=RuntimeError("registry fail"))
    manager = TrackedTaskManager(task_registry=registry)

    async def work():
        return 7

    task = manager.create_tracked_task(work(), task_name="fallback")
    assert await task == 7


@pytest.mark.asyncio
async def test_create_supervised_task_completes():
    manager = TrackedTaskManager()

    async def work():
        return "done"

    task = manager.create_supervised_task(work(), parent_component="test")
    assert await task == "done"


@pytest.mark.asyncio
async def test_audit_orphans_counts_untracked():
    manager = TrackedTaskManager()

    async def sleeper():
        await asyncio.sleep(0.05)

    _ = asyncio.create_task(sleeper())
    count = await manager.audit_orphans()
    assert count >= 1


@pytest.mark.asyncio
async def test_cleanup_orphaned_tasks_cancels_running():
    manager = TrackedTaskManager()
    started = asyncio.Event()

    async def block():
        started.set()
        await asyncio.sleep(10)

    task = manager.create_tracked_task(block(), task_name="to_cancel")
    await started.wait()
    cleaned = await manager.cleanup_orphaned_tasks()
    assert cleaned >= 1
    assert task.cancelled() or task.done()


def test_global_manager_singleton():
    a = get_global_tracked_manager()
    b = get_global_tracked_manager()
    assert a is b


def test_set_task_registry():
    manager = TrackedTaskManager()
    registry = MagicMock()
    manager.set_task_registry(registry)
    assert manager._task_registry is registry


def test_memory_leak_prevention_session_start():
    assert memory_leak_prevention_channel_start_session() is True


@pytest.mark.asyncio
async def test_patch_asyncio_create_task_with_tracking():
    original = asyncio.create_task
    try:
        patch_asyncio_create_task_with_tracking()

        async def tiny():
            return 1

        task = asyncio.create_task(tiny())
        assert await task == 1
    finally:
        asyncio.create_task = original
