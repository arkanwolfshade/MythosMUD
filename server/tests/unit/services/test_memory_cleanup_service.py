"""
Tests for the MemoryThresholdMonitor and memory cleanup service.

This module tests the memory threshold monitoring and cleanup service that
detects memory threshold violations and coordinates cleanup of orphan tasks.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.memory_cleanup_service import (
    MemoryThresholdMonitor,
    create_memory_cleanup_monitor,
    get_managed_task_cleanup_implementation_for_task_four_spec_compliance,
)


class TestMemoryThresholdMonitorInitialization:
    """Test memory threshold monitor initialization."""

    def test_monitor_initialization_default_values(self) -> None:
        """Test monitor initializes with default values."""
        monitor = MemoryThresholdMonitor()

        assert monitor.memory_threshold_bytes == 512.0 * 1024 * 1024  # 512 MB in bytes
        assert monitor.task_count_threshold == 100
        assert monitor.cleanup_cooldown == 30.0
        assert monitor.last_cleanup_time == 0.0
        assert monitor.cleanup_total_count == 0
        assert monitor.monitoring_enabled is True

    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared state or initialization race conditions
    def test_monitor_initialization_custom_values(self) -> None:
        """Test monitor initializes with custom values."""
        monitor = MemoryThresholdMonitor(
            memory_threshold_mb=1024.0, task_count_threshold=200, cleanup_cooldown_seconds=60.0
        )

        assert monitor.memory_threshold_bytes == 1024.0 * 1024 * 1024
        assert monitor.task_count_threshold == 200
        assert monitor.cleanup_cooldown == 60.0

    def test_create_memory_cleanup_monitor_factory(self) -> None:
        """Test factory function creates monitor correctly."""
        monitor = create_memory_cleanup_monitor(
            memory_threshold_mb=256.0, task_count_threshold=50, cleanup_cooldown_seconds=15.0
        )

        assert isinstance(monitor, MemoryThresholdMonitor)
        assert monitor.memory_threshold_bytes == 256.0 * 1024 * 1024
        assert monitor.task_count_threshold == 50
        assert monitor.cleanup_cooldown == 15.0


class TestMemoryStatusMonitoring:
    """Test memory status monitoring functionality."""

    @pytest.mark.serial  # Worker crash in parallel execution - likely due to shared state or initialization race condition
    @patch("server.app.memory_cleanup_service.psutil.Process")
    def test_get_current_memory_usage_success(self, mock_process_class):
        """Test successful memory usage retrieval."""
        mock_process = MagicMock()
        mock_memory_info = MagicMock()
        mock_memory_info.rss = 256 * 1024 * 1024  # 256 MB
        mock_process.memory_info.return_value = mock_memory_info
        mock_process_class.return_value = mock_process

        monitor = MemoryThresholdMonitor()
        memory_usage = monitor._get_current_memory_usage()

        assert memory_usage == 256 * 1024 * 1024

    @patch("server.app.memory_cleanup_service.psutil.Process")
    def test_get_current_memory_usage_failure(self, mock_process_class):
        """Test memory usage retrieval handles exceptions."""
        mock_process_class.side_effect = OSError("Permission denied")

        monitor = MemoryThresholdMonitor()
        memory_usage = monitor._get_current_memory_usage()

        assert memory_usage == 0.0

    @pytest.mark.asyncio
    async def test_get_active_task_count_with_loop(self) -> None:
        """Test active task count retrieval with running loop."""
        monitor = MemoryThresholdMonitor()

        # Create some dummy tasks
        async def dummy_task():
            await asyncio.sleep(0.1)

        tasks = [asyncio.create_task(dummy_task()) for _ in range(3)]

        try:
            task_count = monitor._get_active_task_count()
            # Should include the 3 dummy tasks plus current test task
            assert task_count >= 3
        finally:
            # Cleanup tasks
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)

    def test_get_active_task_count_no_loop(self) -> None:
        """Test active task count handles no running loop."""
        monitor = MemoryThresholdMonitor()

        # This test runs outside async context, so no loop should be available
        # The method should handle this gracefully
        # Actually, pytest-asyncio provides a loop, so we need to mock the exception
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            task_count = monitor._get_active_task_count()
            assert task_count == 0

    @pytest.mark.asyncio
    @patch.object(MemoryThresholdMonitor, "_get_current_memory_usage")
    @patch.object(MemoryThresholdMonitor, "_get_active_task_count")
    async def test_get_memory_status_report(self, mock_task_count, mock_memory):
        """Test memory status report generation."""
        mock_memory.return_value = 600 * 1024 * 1024  # 600 MB
        mock_task_count.return_value = 150

        monitor = MemoryThresholdMonitor(memory_threshold_mb=512.0, task_count_threshold=100)
        status = await monitor.get_memory_status_report()

        assert status["current_memory_bytes"] == 600 * 1024 * 1024
        assert status["current_memory_mb"] == 600.0
        assert status["memory_threshold_mb"] == 512.0
        assert status["active_task_count"] == 150
        assert status["task_threshold"] == 100
        assert status["is_threshold_exceeded"] is True  # Both thresholds exceeded
        assert "timestamp" in status


class TestMemoryCleanup:
    """Test memory cleanup operations."""

    @pytest.mark.asyncio
    @patch("server.app.memory_cleanup_service.get_global_tracked_manager")
    async def test_managed_task_cleanup_success(self, mock_get_manager):
        """Test successful task cleanup."""
        mock_manager = AsyncMock()
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=5)
        mock_manager.audit_orphans = AsyncMock(return_value=2)
        mock_get_manager.return_value = mock_manager

        monitor = MemoryThresholdMonitor(cleanup_cooldown_seconds=0.0)
        cleaned_count = await monitor.managed_task_cleanup(force_cleanup=True)

        assert cleaned_count == 7  # 5 from cleanup + 2 from audit
        assert monitor.cleanup_total_count == 1
        mock_manager.cleanup_orphaned_tasks.assert_called_once_with(force_gc=True)

    @pytest.mark.asyncio
    @patch.object(MemoryThresholdMonitor, "get_memory_status_report")
    async def test_managed_task_cleanup_cooldown(self, mock_status):
        """Test cleanup respects cooldown period."""
        import time

        mock_status.return_value = {
            "current_memory_bytes": 1000 * 1024 * 1024,
            "active_task_count": 200,
            "is_threshold_exceeded": True,
        }

        monitor = MemoryThresholdMonitor(cleanup_cooldown_seconds=10.0)
        monitor.last_cleanup_time = time.time()  # Just did a cleanup

        cleaned_count = await monitor.managed_task_cleanup(force_cleanup=False)

        assert cleaned_count == 0  # Skipped due to cooldown

    @pytest.mark.asyncio
    @patch.object(MemoryThresholdMonitor, "get_memory_status_report")
    async def test_managed_task_cleanup_no_threshold_violation(self, mock_status):
        """Test cleanup skipped when no threshold violation."""
        mock_status.return_value = {
            "current_memory_bytes": 100 * 1024 * 1024,  # Well below threshold
            "active_task_count": 10,  # Well below threshold
            "is_threshold_exceeded": False,
        }

        monitor = MemoryThresholdMonitor(cleanup_cooldown_seconds=0.0)
        cleaned_count = await monitor.managed_task_cleanup(force_cleanup=False)

        assert cleaned_count == 0  # Skipped, no violation

    @pytest.mark.asyncio
    @patch("server.app.memory_cleanup_service.get_global_tracked_manager")
    async def test_managed_task_cleanup_timeout(self, mock_get_manager):
        """Test cleanup handles timeout."""
        mock_manager = AsyncMock()

        async def slow_cleanup(force_gc=False):  # pylint: disable=unused-argument
            await asyncio.sleep(10)  # Takes too long
            return 5

        mock_manager.cleanup_orphaned_tasks = slow_cleanup
        mock_get_manager.return_value = mock_manager

        monitor = MemoryThresholdMonitor(cleanup_cooldown_seconds=0.0)
        cleaned_count = await monitor.managed_task_cleanup(force_cleanup=True, timeout_seconds=0.1)

        assert cleaned_count == -1  # Timeout indicator

    @pytest.mark.asyncio
    @patch("server.app.memory_cleanup_service.get_global_tracked_manager")
    async def test_managed_task_cleanup_exception(self, mock_get_manager):
        """Test cleanup handles exceptions."""
        mock_get_manager.side_effect = Exception("Tracker unavailable")

        monitor = MemoryThresholdMonitor(cleanup_cooldown_seconds=0.0)
        cleaned_count = await monitor.managed_task_cleanup(force_cleanup=True)

        assert cleaned_count == -2  # Failure indicator

    @pytest.mark.asyncio
    @patch("server.app.memory_cleanup_service.get_global_tracked_manager")
    async def test_managed_task_cleanup_force_overrides_cooldown(self, mock_get_manager):
        """Test force cleanup overrides cooldown restrictions."""
        import time

        mock_manager = AsyncMock()
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=3)
        mock_manager.audit_orphans = AsyncMock(return_value=1)
        mock_get_manager.return_value = mock_manager

        monitor = MemoryThresholdMonitor(cleanup_cooldown_seconds=100.0)
        monitor.last_cleanup_time = time.time()  # Just did cleanup

        cleaned_count = await monitor.managed_task_cleanup(force_cleanup=True)

        assert cleaned_count == 4  # Cleanup executed despite cooldown


class TestFactoryFunctions:
    """Test factory functions and global accessors."""

    def test_task_four_spec_compliance_factory(self) -> None:
        """Test Task 4.3 specification compliance factory function."""
        cleanup_func = get_managed_task_cleanup_implementation_for_task_four_spec_compliance()

        assert callable(cleanup_func)

    @pytest.mark.asyncio
    @patch("server.app.memory_cleanup_service.get_global_tracked_manager")
    async def test_task_four_spec_compliance_execution(self, mock_get_manager):
        """Test Task 4.3 compliant cleanup function execution."""
        mock_manager = AsyncMock()
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=2)
        mock_manager.audit_orphans = AsyncMock(return_value=1)
        mock_get_manager.return_value = mock_manager

        cleanup_func = get_managed_task_cleanup_implementation_for_task_four_spec_compliance()

        # Function should accept force_cleanup parameter
        result = await cleanup_func(force_cleanup_ref=True)

        assert result >= 0  # Should return count or error indicator

    def test_task_four_spec_compliance_with_custom_monitor(self) -> None:
        """Test Task 4.3 factory with custom monitor."""
        custom_monitor = create_memory_cleanup_monitor(memory_threshold_mb=128.0)
        cleanup_func = get_managed_task_cleanup_implementation_for_task_four_spec_compliance(
            reference_monitor=custom_monitor
        )

        assert callable(cleanup_func)


class TestGarbageCollection:
    """Test garbage collection functionality."""

    @patch("gc.collect")
    @patch("gc.get_objects")
    def test_flush_memory_indexes_cache_success(self, mock_get_objects, mock_collect):
        """Test garbage collection flush succeeds."""
        mock_get_objects.return_value = list(range(1000))
        mock_collect.return_value = 50  # Collected 50 objects

        monitor = MemoryThresholdMonitor()

        # Explicitly call the flush method
        monitor._flush_memory_indexes_cache()

        mock_collect.assert_called()

    @patch("gc.collect")
    def test_flush_memory_indexes_cache_exception(self, mock_collect):
        """Test garbage collection handles exceptions."""
        mock_collect.side_effect = Exception("GC error")

        # Should not raise exception
        monitor = MemoryThresholdMonitor()
        monitor._flush_memory_indexes_cache()

        # Monitor should still be initialized
        assert monitor.monitoring_enabled is True
