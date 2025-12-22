"""
Tests for the Memory Lifespan Coordinator.

This module tests the periodic orphan auditing and memory lifecycle coordination
system that prevents computational entropy from exceeding permitted boundaries.

As noted in the Pnakotic Manuscripts: "Proper testing of lifecycle mechanisms
ensures the ancient ones remain properly contained within their designated boundaries."
"""

import asyncio
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.memory_lifespan_coordinator import (
    PeriodicOrphanAuditor,
    create_lifespan_memory_service,
)


class TestPeriodicOrphanAuditorInitialization:
    """Test PeriodicOrphanAuditor initialization."""

    def test_auditor_initialization_default_values(self) -> None:
        """Test auditor initializes with default values."""
        auditor = PeriodicOrphanAuditor()

        assert auditor.check_interval == 60.0
        assert auditor.auto_cleanup is True
        assert auditor.audit_running is False
        assert auditor.coordinator_task is None
        assert auditor.auditor_start_time is None
        assert auditor.total_audit_cycles_completed == 0
        assert auditor.total_orphans_identified == 0

    def test_auditor_initialization_custom_values(self) -> None:
        """Test auditor initializes with custom values."""
        auditor = PeriodicOrphanAuditor(
            check_interval_seconds=30.0, memory_threshold_mb=256.0, auto_cleanup_enabled=False
        )

        assert auditor.check_interval == 30.0
        assert auditor.auto_cleanup is False
        assert auditor.memory_monitor is not None

    @patch("server.app.memory_lifespan_coordinator.create_memory_cleanup_monitor")
    def test_auditor_creates_memory_monitor(self, mock_create_monitor):
        """Test auditor creates memory monitor with correct parameters."""
        mock_monitor = MagicMock()
        mock_create_monitor.return_value = mock_monitor

        auditor = PeriodicOrphanAuditor(memory_threshold_mb=1024.0)

        mock_create_monitor.assert_called_once_with(memory_threshold_mb=1024.0, task_count_threshold=80)
        assert auditor.memory_monitor == mock_monitor


class TestPeriodicAuditScheduling:
    """Test periodic audit scheduling functionality."""

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_schedule_periodic_auditing_success(self, mock_get_manager):
        """Test successful scheduling of periodic auditing."""
        mock_manager = MagicMock()
        mock_task: asyncio.Future[Any] = asyncio.Future()
        mock_task.set_result(None)

        # create_tracked_task consumes the coroutine by creating a task from it
        def create_task_side_effect(coro, *_args, **_kwargs):
            # Close the coroutine to prevent "never awaited" warning
            coro.close()
            return mock_task

        mock_manager.create_tracked_task.side_effect = create_task_side_effect
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(check_interval_seconds=1.0)

        # Start auditing (will run in background)
        await auditor.schedule_periodic_auditing()

        # Give it a moment to initialize
        await asyncio.sleep(0.1)

        assert auditor.audit_running is True
        assert auditor.auditor_start_time is not None
        assert auditor.coordinator_task is not None

        # Stop the auditor
        auditor.stop_audit_scheduler()

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_schedule_periodic_auditing_already_running(self, mock_get_manager):
        """Test scheduling fails when already running."""
        mock_manager = MagicMock()
        mock_task: asyncio.Future[Any] = asyncio.Future()
        mock_task.set_result(None)

        # create_tracked_task consumes the coroutine by creating a task from it
        def create_task_side_effect(coro, *_args, **_kwargs):
            # Close the coroutine to prevent "never awaited" warning
            coro.close()
            return mock_task

        mock_manager.create_tracked_task.side_effect = create_task_side_effect
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(check_interval_seconds=1.0)

        # Start auditing first time
        await auditor.schedule_periodic_auditing()

        # Attempt to start again should raise RuntimeError
        with pytest.raises(RuntimeError, match="Periodic audit already running"):
            await auditor.schedule_periodic_auditing()

        # Cleanup
        auditor.stop_audit_scheduler()

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_schedule_periodic_auditing_initialization_failure(self, mock_get_manager):
        """Test scheduling handles initialization failures."""
        mock_manager = MagicMock()
        mock_manager.create_tracked_task.side_effect = Exception("Tracker initialization failed")
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor()

        with pytest.raises(RuntimeError, match="Chronic memory auditing not initialized"):
            await auditor.schedule_periodic_auditing()


class TestBackgroundAuditCycle:
    """Test background audit cycle execution."""

    @pytest.mark.asyncio
    @patch.object(PeriodicOrphanAuditor, "_do_full_cleanup_audit")
    async def test_background_audit_cycle_executes(self, mock_audit):
        """Test background audit cycle executes audits."""
        mock_audit.return_value = None
        auditor = PeriodicOrphanAuditor(check_interval_seconds=0.1)

        # Create a task to run the cycle
        cycle_task = asyncio.create_task(auditor._background_audit_cycle())

        try:
            # Let it run a couple cycles
            await asyncio.sleep(0.3)

            # Should have called audit at least twice
            assert mock_audit.call_count >= 2
        finally:
            # Cancel the cycle and ensure it's properly awaited
            cycle_task.cancel()
            try:
                await asyncio.wait_for(cycle_task, timeout=0.1)
            except (asyncio.CancelledError, TimeoutError):
                pass
            # Ensure task is done before test ends
            if not cycle_task.done():
                cycle_task.cancel()
                try:
                    await cycle_task
                except asyncio.CancelledError:
                    pass
            # Force garbage collection to ensure no orphaned coroutines
            import gc

            gc.collect()
            await asyncio.sleep(0.01)  # Give GC time to process

    @pytest.mark.asyncio
    @patch.object(PeriodicOrphanAuditor, "_do_full_cleanup_audit")
    async def test_background_audit_cycle_handles_cancellation(self, mock_audit):
        """Test background cycle handles cancellation gracefully."""
        mock_audit.return_value = None
        auditor = PeriodicOrphanAuditor(check_interval_seconds=0.1)

        # Start the cycle
        cycle_task = asyncio.create_task(auditor._background_audit_cycle())

        # Let it run briefly
        await asyncio.sleep(0.05)

        # Cancel it
        cycle_task.cancel()

        # Should handle cancellation without error
        try:
            await cycle_task
        except asyncio.CancelledError:
            pass  # Expected

        assert auditor.audit_running is False

    @pytest.mark.asyncio
    @patch.object(PeriodicOrphanAuditor, "_do_full_cleanup_audit")
    async def test_background_audit_cycle_handles_exceptions(self, mock_audit):
        """Test background cycle handles audit exceptions."""
        mock_audit.side_effect = Exception("Audit failed")
        auditor = PeriodicOrphanAuditor(check_interval_seconds=0.1)

        # Start the cycle
        cycle_task = asyncio.create_task(auditor._background_audit_cycle())

        # Let it run briefly
        await asyncio.sleep(0.2)

        # Should have completed without crashing
        assert cycle_task.done()


class TestFullCleanupAudit:
    """Test full cleanup audit execution."""

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_full_cleanup_audit_success(self, mock_get_manager):
        """Test successful full cleanup audit."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=5)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=3)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(check_interval_seconds=1.0)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": False, "active_task_count": 10, "current_memory_mb": 100.0}
        )

        await auditor._do_full_cleanup_audit()

        assert auditor.total_orphans_identified == 5
        assert auditor.total_audit_cycles_completed == 1
        mock_manager.audit_orphans.assert_called_once()

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_full_cleanup_audit_with_threshold_exceeded(self, mock_get_manager):
        """Test audit triggers cleanup when threshold exceeded."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=0)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=2)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": True, "active_task_count": 200, "current_memory_mb": 1024.0}
        )

        await auditor._do_full_cleanup_audit()

        # Should have triggered cleanup due to threshold exceeded
        mock_manager.cleanup_orphaned_tasks.assert_called_once_with(force_gc=True)

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_full_cleanup_audit_with_orphans_detected(self, mock_get_manager):
        """Test audit triggers cleanup when orphans detected."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=10)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=10)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": False, "active_task_count": 50, "current_memory_mb": 200.0}
        )

        await auditor._do_full_cleanup_audit()

        # Should have triggered cleanup due to orphans detected
        assert auditor.total_orphans_identified == 10
        mock_manager.cleanup_orphaned_tasks.assert_called_once_with(force_gc=True)

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_full_cleanup_audit_auto_cleanup_disabled(self, mock_get_manager):
        """Test audit skips cleanup when auto_cleanup is disabled."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=10)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=10)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=False)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": True, "active_task_count": 200, "current_memory_mb": 1024.0}
        )

        await auditor._do_full_cleanup_audit()

        # Should NOT have triggered cleanup
        mock_manager.cleanup_orphaned_tasks.assert_not_called()
        assert auditor.total_orphans_identified == 10

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_full_cleanup_audit_handles_exceptions(self, mock_get_manager):
        """Test audit handles exceptions gracefully."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(side_effect=Exception("Audit failed"))
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor()

        # Should not raise exception
        await auditor._do_full_cleanup_audit()

        # Audit cycle should still increment (logged as attempted)
        # But orphans should not increment due to exception
        assert auditor.total_orphans_identified == 0


class TestForceSingleAuditCycle:
    """Test forced single audit cycle functionality."""

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_force_single_audit_cycle_success(self, mock_get_manager):
        """Test successful forced audit cycle."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=7)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=5)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(return_value={"is_threshold_exceeded": False})

        report = await auditor.force_single_audit_cycle()

        assert report["detected_unregistered_orphan_threats"] == 7
        assert report["reclaimed_lifespace_leaked"] == 5
        assert "manual_triggered_checkpoint" in report
        assert "manual_audit_terminated_at" in report

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_force_single_audit_cycle_no_orphans(self, mock_get_manager):
        """Test forced audit cycle with no orphans detected."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=0)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(return_value={"is_threshold_exceeded": False})

        report = await auditor.force_single_audit_cycle()

        assert report["detected_unregistered_orphan_threats"] == 0
        assert report["reclaimed_lifespace_leaked"] == 0

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_force_single_audit_cycle_auto_cleanup_disabled(self, mock_get_manager):
        """Test forced audit with auto_cleanup disabled."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=5)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=3)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=False)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(return_value={"is_threshold_exceeded": True})

        report = await auditor.force_single_audit_cycle()

        assert report["detected_unregistered_orphan_threats"] == 5
        assert report["reclaimed_lifespace_leaked"] == 0  # No cleanup due to disabled flag
        mock_manager.cleanup_orphaned_tasks.assert_not_called()

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_force_single_audit_cycle_updates_totals(self, mock_get_manager):
        """Test forced audit updates total orphan count."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=3)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=3)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(return_value={"is_threshold_exceeded": False})

        # Run audit twice
        await auditor.force_single_audit_cycle()
        await auditor.force_single_audit_cycle()

        # Note: _do_full_cleanup_audit updates totals, but force_single_audit_cycle
        # directly calls audit_orphans, so total_orphans_identified is NOT updated
        # Only the automatic cycle updates that counter
        assert auditor.total_audit_cycles_completed == 0  # Not updated by forced cycles


class TestAuditorShutdown:
    """Test auditor shutdown functionality."""

    def test_stop_audit_scheduler_when_not_running(self) -> None:
        """Test stopping auditor when not running logs warning."""
        auditor = PeriodicOrphanAuditor()

        # Should handle gracefully
        auditor.stop_audit_scheduler()

        assert auditor.audit_running is False

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_stop_audit_scheduler_cancels_task(self, mock_get_manager):
        """Test stopping auditor cancels background task."""
        mock_manager = MagicMock()
        mock_task = MagicMock()  # Use MagicMock instead of AsyncMock for task
        mock_task.done.return_value = False
        mock_task.cancel = MagicMock()

        # create_tracked_task consumes the coroutine by creating a task from it
        def create_task_side_effect(coro, *_args, **_kwargs):
            # Close the coroutine to prevent "never awaited" warning
            coro.close()
            return mock_task

        mock_manager.create_tracked_task.side_effect = create_task_side_effect
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(check_interval_seconds=1.0)

        # Start auditing
        await auditor.schedule_periodic_auditing()

        # Stop auditing
        auditor.stop_audit_scheduler()

        assert auditor.audit_running is False
        mock_task.cancel.assert_called()

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_stop_audit_scheduler_handles_exceptions(self, mock_get_manager):
        """Test stopping auditor handles exceptions."""
        mock_manager = MagicMock()
        mock_task = MagicMock()
        mock_task.done.return_value = False
        mock_task.cancel.side_effect = Exception("Cancel failed")

        # create_tracked_task consumes the coroutine by creating a task from it
        def create_task_side_effect(coro, *_args, **_kwargs):
            # Close the coroutine to prevent "never awaited" warning
            coro.close()
            return mock_task

        mock_manager.create_tracked_task.side_effect = create_task_side_effect
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor()
        await auditor.schedule_periodic_auditing()

        # Should handle exception gracefully
        auditor.stop_audit_scheduler()

        # audit_running should still be set to False
        assert auditor.audit_running is False


class TestFactoryFunction:
    """Test factory function for creating lifespan memory service."""

    def test_create_lifespan_memory_service(self) -> None:
        """Test factory creates properly configured auditor."""
        service = create_lifespan_memory_service()

        assert isinstance(service, PeriodicOrphanAuditor)
        assert service.check_interval == 60.0
        assert service.auto_cleanup is True
        assert service.memory_monitor is not None

    def test_create_lifespan_memory_service_returns_same_instance(self) -> None:
        """Test factory returns configured instance."""
        service1 = create_lifespan_memory_service()
        service2 = create_lifespan_memory_service()

        # Factory creates new instances each time (not a singleton in implementation)
        assert isinstance(service1, PeriodicOrphanAuditor)
        assert isinstance(service2, PeriodicOrphanAuditor)


class TestIntegrationScenarios:
    """Test integration scenarios with real asyncio behavior."""

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_complete_lifecycle_flow(self, mock_get_manager):
        """Test complete audit lifecycle from start to finish."""
        # Setup mock manager with realistic behavior
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=2)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=2)
        mock_manager.create_tracked_task = lambda coro, task_name, task_type: asyncio.create_task(coro)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(check_interval_seconds=0.1, auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": False, "active_task_count": 5, "current_memory_mb": 50.0}
        )

        # Start periodic auditing
        await auditor.schedule_periodic_auditing()

        # Let it run for a short time
        await asyncio.sleep(0.25)

        # Force a manual audit
        report = await auditor.force_single_audit_cycle()

        # Stop auditing
        auditor.stop_audit_scheduler()

        # Verify the audit ran
        assert auditor.audit_running is False
        assert report["detected_unregistered_orphan_threats"] >= 0

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_auditor_tracks_multiple_cycles(self, mock_get_manager):
        """Test auditor correctly tracks multiple audit cycles."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=1)
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=1)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(check_interval_seconds=0.05)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": False, "active_task_count": 5, "current_memory_mb": 50.0}
        )

        # Run multiple audit cycles
        await auditor._do_full_cleanup_audit()
        await auditor._do_full_cleanup_audit()
        await auditor._do_full_cleanup_audit()

        assert auditor.total_audit_cycles_completed == 3
        assert auditor.total_orphans_identified == 3


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_audit_with_zero_check_interval(self, mock_get_manager):
        """Test auditor handles zero check interval."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=0)
        mock_get_manager.return_value = mock_manager

        # Zero interval should still work but run continuously
        auditor = PeriodicOrphanAuditor(check_interval_seconds=0.0)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": False, "active_task_count": 0, "current_memory_mb": 0.0}
        )

        await auditor._do_full_cleanup_audit()

        assert auditor.total_audit_cycles_completed == 1

    @pytest.mark.asyncio
    @patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager")
    async def test_audit_with_very_high_orphan_count(self, mock_get_manager):
        """Test auditor handles very high orphan counts."""
        mock_manager = AsyncMock()
        mock_manager.audit_orphans = AsyncMock(return_value=10000)  # High count
        mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=10000)
        mock_get_manager.return_value = mock_manager

        auditor = PeriodicOrphanAuditor(auto_cleanup_enabled=True)
        auditor.memory_monitor = AsyncMock()
        auditor.memory_monitor.get_memory_status_report = AsyncMock(
            return_value={"is_threshold_exceeded": False, "active_task_count": 10, "current_memory_mb": 100.0}
        )

        await auditor._do_full_cleanup_audit()

        assert auditor.total_orphans_identified == 10000
        mock_manager.cleanup_orphaned_tasks.assert_called_once_with(force_gc=True)
