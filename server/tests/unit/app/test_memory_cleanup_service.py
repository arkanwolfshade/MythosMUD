"""Unit tests for memory threshold monitoring and managed task cleanup."""

import asyncio
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.memory_cleanup_service import (
    MemoryThresholdMonitor,
    create_memory_cleanup_monitor,
    get_managed_task_cleanup_implementation_for_task_four_spec_compliance,
)


@pytest.fixture
def monitor() -> MemoryThresholdMonitor:
    """Monitor with tiny thresholds for easy triggering in tests."""
    return MemoryThresholdMonitor(
        memory_threshold_mb=0.001,
        task_count_threshold=1,
        cleanup_cooldown_seconds=3600.0,
    )


def test_create_memory_cleanup_monitor() -> None:
    """Factory returns a configured monitor."""
    created = create_memory_cleanup_monitor(
        memory_threshold_mb=256.0,
        task_count_threshold=50,
        cleanup_cooldown_seconds=15.0,
    )
    assert isinstance(created, MemoryThresholdMonitor)
    assert created.task_count_threshold == 50
    assert created.cleanup_cooldown == 15.0


def test_get_current_memory_usage_success(monitor: MemoryThresholdMonitor) -> None:
    """Process memory query returns a positive byte count."""
    usage = monitor._get_current_memory_usage()
    assert usage >= 0.0


def test_get_current_memory_usage_failure(monitor: MemoryThresholdMonitor) -> None:
    """Memory query failures return zero instead of raising."""
    with patch("server.app.memory_cleanup_service.psutil.Process", side_effect=OSError("denied")):
        assert monitor._get_current_memory_usage() == 0.0


def test_get_active_task_count_no_loop(monitor: MemoryThresholdMonitor) -> None:
    """Without a running loop, task count falls back to zero."""
    assert monitor._get_active_task_count() == 0


@pytest.mark.asyncio
async def test_get_active_task_count_with_loop(monitor: MemoryThresholdMonitor) -> None:
    """Running loop reports at least the current test task."""
    count = monitor._get_active_task_count()
    assert count >= 1


def test_flush_memory_indexes_cache_error(monitor: MemoryThresholdMonitor) -> None:
    """GC failures are swallowed after logging."""
    with patch("gc.collect", side_effect=RuntimeError("gc fail")):
        with patch("gc.get_objects", side_effect=RuntimeError("gc fail")):
            monitor._flush_memory_indexes_cache()


@pytest.mark.asyncio
async def test_get_memory_status_report(monitor: MemoryThresholdMonitor) -> None:
    """Status report includes threshold diagnostics."""
    report = await monitor.get_memory_status_report()

    assert "timestamp" in report
    assert report["memory_threshold_bytes"] == monitor.memory_threshold_bytes
    assert report["task_threshold"] == 1
    assert isinstance(report["is_threshold_exceeded"], bool)


@pytest.mark.asyncio
async def test_managed_task_cleanup_skips_on_cooldown(monitor: MemoryThresholdMonitor) -> None:
    """Recent cleanup is skipped unless forced."""
    monitor.last_cleanup_time = time.time()

    cleaned = await monitor.managed_task_cleanup(force_cleanup=False)
    assert cleaned == 0


@pytest.mark.asyncio
async def test_managed_task_cleanup_skips_when_below_threshold() -> None:
    """No cleanup when memory and task counts are within limits."""
    relaxed = MemoryThresholdMonitor(
        memory_threshold_mb=99999.0,
        task_count_threshold=99999,
        cleanup_cooldown_seconds=0.0,
    )

    cleaned = await relaxed.managed_task_cleanup(force_cleanup=False)
    assert cleaned == 0


@pytest.mark.asyncio
async def test_managed_task_cleanup_success(monitor: MemoryThresholdMonitor) -> None:
    """Threshold breach triggers orphan cleanup via tracked manager."""
    mock_manager = MagicMock()
    mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=2)
    mock_manager.audit_orphans = AsyncMock(return_value=1)

    with patch("server.app.memory_cleanup_service.get_global_tracked_manager", return_value=mock_manager):
        cleaned = await monitor.managed_task_cleanup(force_cleanup=True)

    assert cleaned == 3
    assert monitor.cleanup_total_count == 1
    assert monitor.last_cleanup_time > 0


@pytest.mark.asyncio
async def test_managed_task_cleanup_timeout(monitor: MemoryThresholdMonitor) -> None:
    """Cleanup timeout returns -1."""
    mock_manager = MagicMock()

    async def slow_cleanup(*_args: object, **_kwargs: object) -> int:
        await asyncio.sleep(10)
        return 0

    mock_manager.cleanup_orphaned_tasks = slow_cleanup
    mock_manager.audit_orphans = AsyncMock(return_value=0)

    with patch("server.app.memory_cleanup_service.get_global_tracked_manager", return_value=mock_manager):
        cleaned = await monitor.managed_task_cleanup(force_cleanup=True, timeout_seconds=0.01)

    assert cleaned == -1


@pytest.mark.asyncio
async def test_managed_task_cleanup_execution_failure(monitor: MemoryThresholdMonitor) -> None:
    """Unexpected cleanup errors return -2."""
    mock_manager = MagicMock()
    mock_manager.cleanup_orphaned_tasks = AsyncMock(side_effect=RuntimeError("boom"))

    with patch("server.app.memory_cleanup_service.get_global_tracked_manager", return_value=mock_manager):
        cleaned = await monitor.managed_task_cleanup(force_cleanup=True)

    assert cleaned == -2


@pytest.mark.asyncio
async def test_task_four_spec_factory(monitor: MemoryThresholdMonitor) -> None:
    """Legacy factory delegates to monitor.managed_task_cleanup."""
    mock_manager = MagicMock()
    mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=1)
    mock_manager.audit_orphans = AsyncMock(return_value=0)

    with patch("server.app.memory_cleanup_service.get_global_tracked_manager", return_value=mock_manager):
        cleanup_fn = get_managed_task_cleanup_implementation_for_task_four_spec_compliance(monitor)
        result = await cleanup_fn(force_cleanup_ref=True)

    assert result == 1
