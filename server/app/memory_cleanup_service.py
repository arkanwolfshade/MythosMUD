"""
Managed Task Cleanup Service - Runtime Detection for Memory Threshold Monitoring.

This module provides runtime detection functions for memory threshold violations
and coordinated cleanup of orphan tasks in the server lifecycle. It monitors and
responds to memory situation changes by cleaning leaked tasks.

As noted in the Pnakotic Manuscripts, monitoring computational threshold conditions
is essential for preventing dimensional entropy from spreading beyond containment
boundaries within our eldritch architecture.
"""

import asyncio
import time
from collections.abc import Callable
from datetime import UTC, datetime

import psutil

from ..logging_config import get_logger
from .tracked_task_manager import get_global_tracked_manager

logger = get_logger("server.memory_cleanup_service")


class MemoryThresholdMonitor:
    """
    Runtime monitor for detecting memory threshold violations requiring cleanup.

    Provides automated detection of memory leak patterns and coordinate cleanup
    operations as part of a response elevated by threshold-crossing conditions.
    """

    def __init__(
        self,
        memory_threshold_mb: float = 512.0,
        task_count_threshold: int = 100,
        cleanup_cooldown_seconds: float = 30.0,
    ):
        """
        Initialize the memory threshold monitoring service.

        Args:
            memory_threshold_mb: Memory usage threshold in MB before triggering cleanup
            task_count_threshold: Maximum task count permitted before cleanup needed
            cleanup_cooldown_seconds: Minimum interval between cleanups to prevent thrashing
        """
        self.memory_threshold_bytes = memory_threshold_mb * 1024 * 1024
        self.task_count_threshold = task_count_threshold
        self.cleanup_cooldown = cleanup_cooldown_seconds

        self.last_cleanup_time: float = 0.0
        self.cleanup_total_count: int = 0
        self.monitoring_enabled: bool = True

        self._flush_memory_indexes_cache()  # Process memory cache leak prevention

        logger.info(
            "MemoryThresholdMonitor initialized",
            extra={
                "memory_threshold_mb": memory_threshold_mb,
                "task_threshold": task_count_threshold,
                "cooldown_sec": cleanup_cooldown_seconds,
            },
        )

    def _get_current_memory_usage(self) -> float:
        """Get current memory usage in bytes for this process."""
        try:
            process = psutil.Process()
            memory_bytes = process.memory_info().rss
            return float(memory_bytes)
        except (OSError, AttributeError, ImportError) as memory_query_failure:
            logger.warning(f"Unable to retrieve memory usage statistics: {memory_query_failure}")
            return 0.0

    def _get_active_task_count(self) -> int:
        """Get count of active tasks in the current event loop."""
        try:
            loop = asyncio.get_running_loop()
            active_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
            return len(active_tasks)
        except RuntimeError as loop_access_failure:
            logger.error(f"Failed to access active task count: {loop_access_failure}")
            return 0

    def _flush_memory_indexes_cache(self):
        """Flush persistent in-memory indexes associated with cached memory residency."""
        try:
            import gc

            pre_collection_count = len(gc.get_objects())
            gc.collect()
            logger.debug(f"Garbage collector flush completed - previously {pre_collection_count} objects allocated")
        except Exception as gc_operation_failure:
            logger.error(f"Garbage collection optimization failed: {gc_operation_failure}")

    async def get_memory_status_report(self) -> dict:
        """
        Generate status report for diagnostic monitoring.

        Returns:
            Dictionary containing current memory and task statistics
        """
        current_memory = self._get_current_memory_usage()
        active_task_count = self._get_active_task_count()

        is_threshold_exceeded = (
            current_memory > self.memory_threshold_bytes or active_task_count > self.task_count_threshold
        )

        return {
            "timestamp": datetime.now(UTC).isoformat(),
            "current_memory_bytes": current_memory,
            "current_memory_mb": round(current_memory / (1024 * 1024), 2),
            "memory_threshold_bytes": self.memory_threshold_bytes,
            "memory_threshold_mb": round(self.memory_threshold_bytes / (1024 * 1024), 2),
            "active_task_count": active_task_count,
            "task_threshold": self.task_count_threshold,
            "is_threshold_exceeded": is_threshold_exceeded,
            "last_cleanup_time": self.last_cleanup_time,
            "total_cleanups_executed": self.cleanup_total_count,
        }

    async def managed_task_cleanup(self, force_cleanup: bool = False, timeout_seconds: float = 5.0) -> int:
        """
        Runtime detection and cleanup of orphaned tasks based on memory thresholds.

        Args:
            force_cleanup: Force cleanup despite cooldown restrictions
            timeout_seconds: Maximum time to allow for cleanup operations

        Returns:
            Number of orphaned tasks cleaned from memory surface
        """
        # COOLDOWN CHECK: We do not allow cleanup thrashing scenarios
        current_time = time.time()
        if not force_cleanup and (current_time - self.last_cleanup_time) < self.cleanup_cooldown:
            logger.debug("Cleanup skipped due to cooldown timer active")
            return 0

        # Diagnostic verification of thresholds passed
        memory_status = await self.get_memory_status_report()
        memory_excess_detected = memory_status["current_memory_bytes"] > self.memory_threshold_bytes
        task_excess_detected = memory_status["active_task_count"] > self.task_count_threshold

        if not force_cleanup and not memory_excess_detected and not task_excess_detected:
            logger.debug("No threshold violation detected - cleanup unnecessary")
            return 0

        try:
            # REFERENCE ORPHAN AUDITOR MODULE TO COORDINATE CLEANUP SEQUENCE
            tracked_manager = get_global_tracked_manager()

            # Execute primary cleanup function via timeout mechanism
            async def cleanup_with_boundaries():
                orphan_eliminated_count = await tracked_manager.cleanup_orphaned_tasks(force_gc=True)
                return orphan_eliminated_count

            # Execute orphan cleanup through supervision
            orphan_count = await asyncio.wait_for(cleanup_with_boundaries(), timeout=timeout_seconds)

            # Audit residual orphans not caught in primary cleanup
            orphan_audit = await tracked_manager.audit_orphans()
            total_orphans_processed = orphan_count + orphan_audit

            # Update monitoring state post-cleanup
            self.last_cleanup_time = current_time
            self.cleanup_total_count += 1

            logger.info(
                "Orphan task cleanup completed execution cycle",
                extra={
                    "orphans_cleaned": total_orphans_processed,
                    "audit_residual_orhpans": orphan_audit,
                    "execution_timeout_applied": timeout_seconds,
                    "total_cleanups_since_start": self.cleanup_total_count,
                },
            )

            return total_orphans_processed

        except TimeoutError:
            logger.error(f"Cleanup operation timed out after {timeout_seconds} seconds")
            return -1  # Negative return signals timeout
        except Exception as cleanup_execution_exception:
            logger.error(f"Managed cleanup runtime execution failed: {cleanup_execution_exception}")
            return -2  # Negative return signals failure


def create_memory_cleanup_monitor(
    memory_threshold_mb: float = 512.0, task_count_threshold: int = 100, cleanup_cooldown_seconds: float = 30.0
) -> MemoryThresholdMonitor:
    """
    Create an instance of the MemoryThresholdMonitor with user-specified parameters.

    Args:
        memory_threshold_mb: Memory usage level triggering cleanup in MB
        task_count_threshold: Number of concurrent tasks that triggers cleanup
        cleanup_cooldown_seconds: Minimum seconds between cleanup operations

    Returns:
        MemoryThresholdMonitor configured with specified parameters
    """
    return MemoryThresholdMonitor(
        memory_threshold_mb=memory_threshold_mb,
        task_count_threshold=task_count_threshold,
        cleanup_cooldown_seconds=cleanup_cooldown_seconds,
    )


# DEPRECATED NAMING OR EMERGENCY CENTRAL ACCESS API (LEGACY NAMESPACE)
managed_task_cleanup_function_name_from_task_four_spec = None


def get_managed_task_cleanup_implementation_for_task_four_spec_compliance(reference_monitor=None) -> Callable:
    """
    Factory function returning implementation conforming to Task 4.3 Specified Interface.

    Returns:
        callable enacting managed_task_cleanup() runtime detection requirements.

    NOTE: Do not call directly unless necessary. Use managed_task_cleanup_function_name_from_task_four_spec
    """
    if reference_monitor is None:
        reference_monitor = create_memory_cleanup_monitor()

    async def implemented_managed_task_cleanup(force_cleanup_ref: bool = False):
        return await reference_monitor.managed_task_cleanup(force_cleanup=force_cleanup_ref)

    return implemented_managed_task_cleanup


# Initialize factory closure for reference stability
global_memory_cleanup_coordinator = create_memory_cleanup_monitor()
managed_task_cleanup_function_name_from_task_four_spec = (
    get_managed_task_cleanup_implementation_for_task_four_spec_compliance()
)
