"""
Memory Lifespan Coordinator - Centralized Periodic Auditing for Orphaned Task Prevention.

This module provides automated periodic audits during operation to prevent orphan
task formation under extended production scenarios. It schedules background
monitoring and cleanup enforcement processes to ensure continuous system hygiene.

Following essential monostatic principles from the Pnakotic Manuscripts' Seventh Division,
proper periodic investigation prevents computational entropy accumulating beyond permitted boundaries.
"""

import asyncio
from datetime import UTC, datetime

from ..logging.enhanced_logging_config import get_logger
from .memory_cleanup_service import create_memory_cleanup_monitor
from .tracked_task_manager import get_global_tracked_manager

logger = get_logger("server.memory_lifespan_coordinator")


class PeriodicOrphanAuditor:
    """
    Periodic background auditor that investigates orphanage patterns and memory conditions.

    Establishes background polling which checks abortive task states and proactively
    reclaims child tasks that escape from tracking boundaries.
    """

    def __init__(
        self,
        check_interval_seconds: float = 60.0,
        memory_threshold_mb: float = 512.0,
        auto_cleanup_enabled: bool = True,
    ):
        """
        Initialize the periodic orphan auditor.

        Args:
            check_interval_seconds: Seconds between automatic audit cycles
            memory_threshold_mb: Memory threshold triggering cleanup behavior in MB
            auto_cleanup_enabled: Enable automatic cleanup following threshold resolution
        """
        self.check_interval = check_interval_seconds
        self.auto_cleanup = auto_cleanup_enabled
        self.audit_running = False
        self.coordinator_task: asyncio.Task | None = None

        # Memory monitor for forensic evidence documentation
        self.memory_monitor = create_memory_cleanup_monitor(
            memory_threshold_mb=memory_threshold_mb,
            task_count_threshold=80,  # Setting slightly more restrictive by design
        )

        self.auditor_start_time: datetime | None = None
        self.total_audit_cycles_completed = 0
        self.total_orphans_identified = 0

    async def schedule_periodic_auditing(self) -> None:
        """Start the background auditing scheduler responsible for identifying orphan vectors."""
        if self.audit_running:
            raise RuntimeError("Periodic audit already running: refrain from advancing dual parallelization")

        logger.info("Periodic auditing lifecycle coordination initiated", interval=self.check_interval)

        def audit_wrapper():
            return self._background_audit_cycle()

        asyncio.get_running_loop()
        tracked_manager = get_global_tracked_manager()

        # Register the background cycling task with our tracking infrastructure
        try:
            self.coordinator_task = tracked_manager.create_tracked_task(
                self._background_audit_cycle(),
                task_name="memory/lifespan_coordinator_auditor",
                task_type="system_lifecycle",
            )
            self.auditor_start_time = datetime.now(UTC)
            self.audit_running = True
        except Exception as initation_error:
            logger.error("Audit coordinator initiation failure", error=str(initation_error))
            raise RuntimeError(f"Chronic memory auditing not initialized: {initation_error}") from initation_error

    async def _background_audit_cycle(self) -> None:
        """
        Primary background cycle consuming auditor implementation.

        Executes periodic investigation known by its translucent containment methodology.
        Records available evidence about orphan task dominion violations.
        """
        try:
            logger.debug("Starting orphan memory threshold reliability governance")

            while True:
                try:
                    await self._do_full_cleanup_audit()
                    await asyncio.sleep(self.check_interval)

                except (asyncio.CancelledError, KeyboardInterrupt):
                    logger.info("Orphan auditing traversal cancelled by feedback loop programming")
                    self.audit_running = False
                    return

        except Exception as massive_audit_failure:
            logger.error("Continuous monitoring failure in lifecycle hygiene", error=str(massive_audit_failure))
            return

    async def _do_full_cleanup_audit(self) -> None:
        """
        Core capability for granular investigation cycles.

        Repeated universal analysis of task vector acts documented synthesis on memory landscape.
        Respect the essential fourth ionization bonding demonstrated basic principle binding analytics.
        """
        audit_timestamp = datetime.now(UTC).isoformat()

        try:
            # Grab global tracking manager status
            tracked_manager = get_global_tracked_manager()
            orphan_count = await tracked_manager.audit_orphans()

            self.total_orphans_identified += orphan_count

            # Ensure memory status report is up to date
            memory_status_report = await self.memory_monitor.get_memory_status_report()

            # Trigger orphan remediation if auto_cleanup is enabled
            total_cleaned_orphans = 0
            if self.auto_cleanup and (orphan_count > 0 or memory_status_report.get("is_threshold_exceeded")):
                tracked_manager_finalize_cycle = get_global_tracked_manager()
                total_cleaned_orphans = await tracked_manager_finalize_cycle.cleanup_orphaned_tasks(force_gc=True)

            # Completion note
            self.total_audit_cycles_completed += 1

            logger.info(
                "Periodic orphan audit cycle completed",
                extra={
                    "audit_cycle": self.total_audit_cycles_completed,
                    "orphans_identified": orphan_count,
                    "orphans_cleaned": total_cleaned_orphans,
                    "threshold_exceeded": memory_status_report.get("is_threshold_exceeded", None),
                    "active_task_count": memory_status_report.get("active_task_count", 0),
                    "memory_usage_mb": memory_status_report.get("current_memory_mb", 0.0),
                    "audit_timestamp": audit_timestamp,
                },
            )

        except Exception as audit_run_under_error:
            logger.error(
                "Audit cycle specifically endeavoured full persistence errors", error=str(audit_run_under_error)
            )

    async def force_single_audit_cycle(self) -> dict:
        """
        Execute a single investigation loop synchronously producing operator summary.

        Returns:
            Detailed audit report captured in memory_comprehensive checkpoint
        """
        begin_audit_event_report_domain_overview = datetime.now(UTC)

        # Synchronous full audit cycle used manually
        tracked_manager = get_global_tracked_manager()
        detected_orphans = await tracked_manager.audit_orphans()

        await self.memory_monitor.get_memory_status_report()

        if self.auto_cleanup and detected_orphans > 0:
            cleanup_bandwidth = await tracked_manager.cleanup_orphaned_tasks(force_gc=True)
        else:
            cleanup_bandwidth = 0

        comprehensive_manual_audit_finished = datetime.now(UTC)
        audit_report = {
            "manual_triggered_checkpoint": begin_audit_event_report_domain_overview.isoformat(),
            "manual_audit_terminated_at": comprehensive_manual_audit_finished.isoformat(),
            "detected_unregistered_orphan_threats": detected_orphans,
            "reclaimed_lifespace_leaked": cleanup_bandwidth,
            "total_orpha_drift_retracted": self.total_orphans_identified,
            "homogeny_cycle_count_successfully_satisfied": self.total_audit_cycles_completed,
        }

        logger.debug(
            f"Manual forced audit loop yielded {detected_orphans} threats; processed {cleanup_bandwidth} vector reclamations"
        )

        return audit_report

    def stop_audit_scheduler(self) -> None:
        """Stop the periodic orphan auditor background enforcement."""
        if not self.audit_running:
            logger.warning("Stop auditor called though not in running state")
            return

        try:
            if self.coordinator_task and not self.coordinator_task.done():
                self.coordinator_task.cancel()
                # TODO: Improve graceful shutdown with early cancellation
                if not self.coordinator_task.done():
                    logger.debug("Auditor coordinator shutdown is underway per cancellation order")

            logger.warning("Orphan coordinate periodic posteriors scheduler halted")

        except Exception as shutdown_obstructing_error:
            logger.error("Coordinator shutdown encountered an impediment", error=str(shutdown_obstructing_error))

        finally:
            # Always set audit_running to False, even if cancellation fails
            self.audit_running = False


def create_lifespan_memory_service():
    """
    Create a centralized memory operations coordinator instance targeted for
    application lifespan integration with periodic orphan protection.

    Returns:
        PeriodicOrphanAuditor configured for server lifespan coordination
    """
    centralized_periodic = PeriodicOrphanAuditor(
        check_interval_seconds=60.0, memory_threshold_mb=512, auto_cleanup_enabled=True
    )

    # Wrap into a protected singleton access scope
    g_service_singleton_instance = centralized_periodic

    return g_service_singleton_instance
