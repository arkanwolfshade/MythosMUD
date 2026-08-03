"""Unit tests for periodic orphan auditing and lifespan memory coordination."""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.app.memory_lifespan_coordinator import PeriodicOrphanAuditor, create_lifespan_memory_service


@pytest.fixture
def auditor() -> PeriodicOrphanAuditor:
    """Auditor with short interval and auto cleanup enabled."""
    return PeriodicOrphanAuditor(
        check_interval_seconds=0.01,
        memory_threshold_mb=512.0,
        auto_cleanup_enabled=True,
    )


def test_create_lifespan_memory_service() -> None:
    """Factory returns a configured periodic auditor."""
    service = create_lifespan_memory_service()
    assert isinstance(service, PeriodicOrphanAuditor)
    assert service.auto_cleanup is True


@pytest.mark.asyncio
async def test_schedule_periodic_auditing_success(auditor: PeriodicOrphanAuditor) -> None:
    """Scheduler registers a tracked background task."""
    mock_manager = MagicMock()
    mock_task = asyncio.create_task(asyncio.sleep(60))

    def _tracked_task(coro: object, *_args: object, **_kwargs: object) -> asyncio.Task[None]:
        # Mock replaces the real background coro; close it to avoid RuntimeWarning.
        if asyncio.iscoroutine(coro):
            coro.close()
        return mock_task

    mock_manager.create_tracked_task.side_effect = _tracked_task

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        await auditor.schedule_periodic_auditing()

    assert auditor.audit_running is True
    assert auditor.coordinator_task is mock_task
    assert auditor.auditor_start_time is not None

    auditor.stop_audit_scheduler()
    await asyncio.sleep(0)


@pytest.mark.asyncio
async def test_schedule_periodic_auditing_already_running(auditor: PeriodicOrphanAuditor) -> None:
    """Second schedule attempt raises RuntimeError."""
    auditor.audit_running = True

    with pytest.raises(RuntimeError, match="already running"):
        await auditor.schedule_periodic_auditing()


@pytest.mark.asyncio
async def test_schedule_periodic_auditing_init_failure(auditor: PeriodicOrphanAuditor) -> None:
    """Tracked task creation failures surface as RuntimeError."""
    mock_manager = MagicMock()

    def _fail_tracked(coro: object, *_args: object, **_kwargs: object) -> None:
        if asyncio.iscoroutine(coro):
            coro.close()
        raise RuntimeError("no loop")

    mock_manager.create_tracked_task.side_effect = _fail_tracked

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        with pytest.raises(RuntimeError, match="not initialized"):
            await auditor.schedule_periodic_auditing()


@pytest.mark.asyncio
async def test_do_full_cleanup_audit_with_cleanup(auditor: PeriodicOrphanAuditor) -> None:
    """Orphans and threshold breaches trigger cleanup."""
    mock_manager = MagicMock()
    mock_manager.audit_orphans = AsyncMock(return_value=2)
    mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=2)

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        with patch.object(
            auditor.memory_monitor,
            "get_memory_status_report",
            AsyncMock(return_value={"is_threshold_exceeded": True, "active_task_count": 0, "current_memory_mb": 0.0}),
        ):
            await auditor._do_full_cleanup_audit()

    assert auditor.total_audit_cycles_completed == 1
    assert auditor.total_orphans_identified == 2
    mock_manager.cleanup_orphaned_tasks.assert_awaited_once_with(force_gc=True)


@pytest.mark.asyncio
async def test_do_full_cleanup_audit_no_cleanup(auditor: PeriodicOrphanAuditor) -> None:
    """No orphans and no threshold breach skips cleanup."""
    auditor.auto_cleanup = False
    mock_manager = MagicMock()
    mock_manager.audit_orphans = AsyncMock(return_value=0)

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        with patch.object(
            auditor.memory_monitor,
            "get_memory_status_report",
            AsyncMock(return_value={"is_threshold_exceeded": False, "active_task_count": 0, "current_memory_mb": 0.0}),
        ):
            await auditor._do_full_cleanup_audit()

    assert auditor.total_audit_cycles_completed == 1
    mock_manager.cleanup_orphaned_tasks.assert_not_called()


@pytest.mark.asyncio
async def test_do_full_cleanup_audit_handles_errors(auditor: PeriodicOrphanAuditor) -> None:
    """Audit cycle errors are logged without propagating."""
    mock_manager = MagicMock()
    mock_manager.audit_orphans = AsyncMock(side_effect=RuntimeError("audit failed"))

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        await auditor._do_full_cleanup_audit()

    assert auditor.total_audit_cycles_completed == 0


@pytest.mark.asyncio
async def test_force_single_audit_cycle_with_cleanup(auditor: PeriodicOrphanAuditor) -> None:
    """Manual audit returns summary and cleans detected orphans."""
    mock_manager = MagicMock()
    mock_manager.audit_orphans = AsyncMock(return_value=3)
    mock_manager.cleanup_orphaned_tasks = AsyncMock(return_value=3)

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        report = await auditor.force_single_audit_cycle()

    assert report["detected_unregistered_orphan_threats"] == 3
    assert report["reclaimed_lifespace_leaked"] == 3
    assert "manual_triggered_checkpoint" in report


@pytest.mark.asyncio
async def test_force_single_audit_cycle_no_orphans(auditor: PeriodicOrphanAuditor) -> None:
    """Manual audit skips cleanup when no orphans are found."""
    mock_manager = MagicMock()
    mock_manager.audit_orphans = AsyncMock(return_value=0)

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        report = await auditor.force_single_audit_cycle()

    assert report["reclaimed_lifespace_leaked"] == 0


def test_stop_audit_scheduler_not_running(auditor: PeriodicOrphanAuditor) -> None:
    """Stopping when idle is a no-op."""
    auditor.audit_running = False
    auditor.stop_audit_scheduler()
    assert auditor.audit_running is False


@pytest.mark.asyncio
async def test_stop_audit_scheduler_cancels_task(auditor: PeriodicOrphanAuditor) -> None:
    """Running scheduler cancels its coordinator task."""
    auditor.audit_running = True

    async def long_running() -> None:
        await asyncio.sleep(60)

    auditor.coordinator_task = asyncio.create_task(long_running())
    auditor.stop_audit_scheduler()
    await asyncio.sleep(0)

    assert auditor.audit_running is False
    assert auditor.coordinator_task.cancelled() or auditor.coordinator_task.done()


@pytest.mark.asyncio
async def test_background_audit_cycle_cancelled(auditor: PeriodicOrphanAuditor) -> None:
    """Background loop exits cleanly on cancellation."""
    mock_manager = MagicMock()
    mock_manager.audit_orphans = AsyncMock(return_value=0)

    with patch("server.app.memory_lifespan_coordinator.get_global_tracked_manager", return_value=mock_manager):
        with patch.object(
            auditor.memory_monitor,
            "get_memory_status_report",
            AsyncMock(return_value={"is_threshold_exceeded": False, "active_task_count": 0, "current_memory_mb": 0.0}),
        ):
            with patch("server.app.memory_lifespan_coordinator.sleep", AsyncMock(side_effect=asyncio.CancelledError)):
                auditor.audit_running = True
                await auditor._background_audit_cycle()

    assert auditor.audit_running is False
