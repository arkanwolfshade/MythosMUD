"""Unit tests for asyncio TaskRegistry lifecycle management."""

import asyncio
from unittest.mock import patch

import pytest

from server.app.task_registry import TaskRegistry, get_registry, register_task, unregister_task


async def _sleep_briefly() -> None:
    await asyncio.sleep(0.01)


async def _hang_until_cancelled() -> None:
    try:
        await asyncio.Event().wait()
    except asyncio.CancelledError:
        raise


@pytest.fixture
def registry() -> TaskRegistry:
    return TaskRegistry()


@pytest.mark.asyncio
async def test_task_metadata_repr(registry: TaskRegistry) -> None:
    task = registry.register_task(_sleep_briefly(), "meta_task", "websocket")
    metadata = registry._active_tasks[task]
    assert "meta_task" in repr(metadata)
    assert "websocket" in repr(metadata)


@pytest.mark.asyncio
async def test_register_and_unregister_task(registry: TaskRegistry) -> None:
    task = registry.register_task(_sleep_briefly(), "worker", "websocket")
    assert registry.get_active_task_count() == 1
    assert registry.unregister_task(task) is True
    await asyncio.sleep(0.02)
    assert registry.get_active_task_count() == 0


@pytest.mark.asyncio
async def test_register_duplicate_name_gets_suffix(registry: TaskRegistry) -> None:
    first = registry.register_task(_sleep_briefly(), "dup", "unknown")
    second = registry.register_task(_sleep_briefly(), "dup", "unknown")
    assert first is not second
    second_name = next(name for name, task in registry._task_names.items() if task is second)
    assert second_name.startswith("dup")
    assert second_name != "dup"


@pytest.mark.asyncio
async def test_register_during_shutdown_raises(registry: TaskRegistry) -> None:
    registry._shutdown_in_progress = True
    coro = _sleep_briefly()
    with pytest.raises(RuntimeError, match="denied during shutdown"):
        registry.register_task(coro, "late", "unknown")
    coro.close()


@pytest.mark.asyncio
async def test_unregister_missing_task_returns_false(registry: TaskRegistry) -> None:
    assert registry.unregister_task("missing") is False


@pytest.mark.asyncio
async def test_cancel_task_by_name(registry: TaskRegistry) -> None:
    registry.register_task(_hang_until_cancelled(), "cancel_me", "background")
    cancelled = await registry.cancel_task("cancel_me", wait_timeout=1.0)
    assert cancelled is True


@pytest.mark.asyncio
async def test_cancel_missing_task_returns_false(registry: TaskRegistry) -> None:
    assert await registry.cancel_task("ghost") is False


@pytest.mark.asyncio
async def test_shutdown_all_clears_active_tasks(registry: TaskRegistry) -> None:
    registry.register_task(_hang_until_cancelled(), "lifecycle_one", "lifecycle")
    registry.register_task(_hang_until_cancelled(), "worker_two", "websocket")
    success = await registry.shutdown_all(timeout=2.0)
    assert success is True
    assert registry.get_active_task_count() == 0


@pytest.mark.asyncio
async def test_shutdown_all_idempotent_warning(registry: TaskRegistry) -> None:
    registry._shutdown_in_progress = True
    assert await registry.shutdown_all() is False


@pytest.mark.asyncio
async def test_get_registry_info_and_metrics(registry: TaskRegistry) -> None:
    registry.register_task(_sleep_briefly(), "svc:worker", "nats")
    info = registry.get_registry_info()
    assert info["active_tasks"] >= 1
    assert info["registry_shutdown_in_progress"] is False
    metrics = registry.get_task_lifecycle_metrics()
    assert metrics["task_creation_count"] >= 1
    assert "nats" in metrics["tasks_by_type"]
    assert "svc" in metrics["tasks_by_service"]


@pytest.mark.asyncio
async def test_list_active_tasks_and_stats_by_type(registry: TaskRegistry) -> None:
    registry.register_task(_sleep_briefly(), "typed", "websocket")
    active = registry.list_active_tasks()
    assert all(not m.task.done() for m in active)
    stats = registry.get_task_stats_by_type()
    assert stats.get("websocket", 0) >= 1


@pytest.mark.asyncio
async def test_module_level_helpers(registry: TaskRegistry) -> None:
    with patch("server.app.task_registry._global_registry", registry):
        task = register_task(_sleep_briefly(), "global", "system")
        assert task in registry._active_tasks
        assert unregister_task("global") is True


def test_get_registry_returns_global_instance() -> None:
    assert isinstance(get_registry(), TaskRegistry)
