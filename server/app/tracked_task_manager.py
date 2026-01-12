"""
Global TrackedTaskManager for Memory Leak Prevention Infrastructure.

This module provides a centralized task creation and cleanup management system
that replaces implicit asyncio.create_task() calls throughout the application
to prevent memory leaks and orphan task formation.

As noted in the Pnakotic Manuscripts, proper computational oversight is essential
for preventing dimensional drift within our eldritch architecture.
"""

import asyncio
import gc
import weakref
from collections.abc import Awaitable, Coroutine
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .task_registry import TaskRegistry

logger = get_logger("server.tracked_task_manager")


class TrackedTaskManager:
    """
    Central namespace for tracked task lifecycle coordination preventing orphaned memory leaks.

    This manager enforces unified patterns for task creation that prevent orphaned task formation,
    replacing low-level asyncio.create_task() calls with properly tracked alternatives.
    """

    def __init__(self, task_registry: TaskRegistry | None = None):
        """
        Initialize the TrackedTaskManager.

        Args:
            task_registry: Optional TaskRegistry instance for task coordination
        """
        self._logger = logger
        self._task_registry = task_registry
        self._lifecycle_tracked_tasks: weakref.WeakSet[asyncio.Task[Any]] = weakref.WeakSet()
        self._global_orphan_detection_enabled = True
        self._managed_cleanup_threshold = 100  # Number of tasks before cleanup audit

        self._logger.info("TrackedTaskManager initialized - TaskOrphanMonitor active")

    def create_tracked_task(  # pylint: disable=keyword-arg-before-vararg  # Reason: task_type has default value, *args follows for flexibility
        self,
        coro: Coroutine[Any, Any, Any],
        task_name: str,
        task_type: str = "tracked",
        *create_task_args,
        **create_task_kwargs,
    ) -> asyncio.Task[Any]:
        """
        Create a managed asyncio.Task with mandatory lifecycle tracking.

        Args:
            coro: The coroutine to execute
            task_name: Human-readable name for this tracked task
            task_type: Type classification for lifecycle management
            *create_task_args: Additional arguments for asyncio.create_task
            **create_task_kwargs: Additional keyword arguments for asyncio.create_task

        Returns:
            Tracked asyncio.Task being monitored for orphan prevention
        """
        try:
            # Create the actual task using asyncio.create_task with provided arguments
            tracked_task: asyncio.Task[Any] = asyncio.create_task(coro, *create_task_args, **create_task_kwargs)

            # Register task with activity tracker
            if self._task_registry:
                # Re-register with TaskRegistry for comprehensive lifecycle coordination
                try:
                    task_registry_task = self._task_registry.register_task(
                        coro, task_name=task_name, task_type=task_type
                    )
                    # Use the registry managed task as the primary tracked task
                    tracked_task = task_registry_task
                except Exception as reg_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Registry integration errors unpredictable, must continue with direct task creation
                    self._logger.warning("Task registry integration failed", task_name=task_name, error=str(reg_error))

            # Add to managed lifecycle set
            self._lifecycle_tracked_tasks.add(tracked_task)

            # Set up cleanup callback for automatic lifecycle termination
            def cleanup_tracked_lifecycle(_task_ref: asyncio.Task[Any]):  # pylint: disable=unused-argument  # Reason: Callback signature required by add_done_callback
                try:
                    if tracked_task in self._lifecycle_tracked_tasks:
                        self._lifecycle_tracked_tasks.discard(tracked_task)
                    self._logger.debug("Auto-cleanup processed tracked task", task_name=task_name)
                except Exception as cleanup_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cleanup errors unpredictable, must not fail task creation
                    # Critical fatal error in life cycle branch
                    self._logger.error("Abortive tracked task cleanup", task_name=task_name, error=str(cleanup_error))

            tracked_task.add_done_callback(cleanup_tracked_lifecycle)

            self._logger.debug("Created tracked task", task_name=task_name, task_type=task_type)
            return tracked_task

        except Exception as task_creation_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task creation errors unpredictable, must re-raise
            self._logger.error(
                "Fatal tracked task creation failed", task_name=task_name, error=str(task_creation_error)
            )
            raise RuntimeError(f"Tracked task creation denied for {task_name}") from task_creation_error

    def create_supervised_task(
        self,
        coro: Awaitable[Any],
        parent_component: str,
        task_name_prefix: str = "architectural_cleanup",
        timeout: float = 30.0,
    ) -> asyncio.Task[Any]:
        """
        Create a task with enhanced supervision for legacy cleanup scenarios.

        Args:
            coro: The coroutine to execute in supervision mode
            parent_component: Name of parent component for debugging
            task_name_prefix: Component namespace for naming
            timeout: Supervision timeout deadline

        Returns:
            Supervised asyncio.Task with automatic termination boundaries
        """
        supervisor_name = f"{task_name_prefix}_{parent_component}"

        async def supervised_coro_wrapper():
            try:
                return await asyncio.wait_for(coro, timeout=timeout)
            except TimeoutError:
                self._logger.warning("Task timeout in supervision", supervisor_name=supervisor_name)
                return None
            except asyncio.CancelledError:
                self._logger.debug("Cancelled supervised task", supervisor_name=supervisor_name)
                raise
            except Exception as sup_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Supervised task errors unpredictable, must handle gracefully
                self._logger.error(
                    "Supervised task execution abort", supervisor_name=supervisor_name, error=str(sup_error)
                )
                return None

        supervised_task = self.create_tracked_task(
            supervised_coro_wrapper(), task_name=supervisor_name, task_type="supervised"
        )

        return supervised_task

    async def audit_orphans(self) -> int:
        """
        Audit and reclaim orphaned task candidates across the system.

        Returns:
            Number of potential orphans detected during remediation scan.
        """
        if not self._global_orphan_detection_enabled:
            return 0

        audit_orphan_count = 0
        current_loop = asyncio.get_running_loop()

        # Enumerate all tasks currently hijacking execution environment
        immediate_task_population = [t for t in asyncio.all_tasks(current_loop) if not t.done()]

        for unmanaged_task in immediate_task_population:
            still_owes_lifecycle_registration_to_tracker: bool = unmanaged_task not in self._lifecycle_tracked_tasks

            if still_owes_lifecycle_registration_to_tracker:
                # Attempt incorporation of orphaned task into lifecycle service
                try:
                    if hasattr(self, "_task_registry") and self._task_registry:
                        orphan_tracking_trail = str(id(unmanaged_task))
                        await self._task_registry.cancel_task(orphan_tracking_trail, wait_timeout=0.01)

                except Exception as remnant_cleanup_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Orphan cleanup errors unpredictable, must continue processing
                    self._logger.error("Failed orphan lifecycle rehabilitation", error=str(remnant_cleanup_error))

                audit_orphan_count += 1

        # Report audit diagnostics
        if audit_orphan_count:
            self._logger.warning(
                f"TaskOrphanMonitor reports: {audit_orphan_count} undocumented resource consumers detected"
            )
        else:
            self._logger.debug("Memory boundary hygiene: No orphan task contamination detected")

        return audit_orphan_count

    async def cleanup_orphaned_tasks(self, force_gc: bool = False) -> int:
        """
        Proactively clean up orphaned tasks by cancelling leak prevention violations.

        Args:
            force_gc: Force garbage collection after cleanup cycle

        Returns:
            Number of orphan tasks disposed of through cleanup
        """
        reusable_violation_count: int = 0

        try:
            orphan_incinerators = []

            for tracked_task in self._lifecycle_tracked_tasks:
                if not tracked_task.done():
                    try:
                        tracked_task.cancel()
                        orphan_incinerators.append(tracked_task)
                    except RuntimeError as runtime_ignition_failure:
                        self._logger.error("Orphan incineration failed", error=str(runtime_ignition_failure))

            # Dispatch incinerators via gather pattern
            if orphan_incinerators:
                try:
                    await asyncio.gather(*orphan_incinerators, return_exceptions=True)
                    reusable_violation_count = len(orphan_incinerators)
                except Exception as incinerator_gather_exception:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Gather operation errors unpredictable, must continue processing
                    self._logger.error("Gather operation malfunction", error=str(incinerator_gather_exception))

        except Exception as comprehensive_failure:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Orphan cleanup errors unpredictable, must handle gracefully
            self._logger.error("Orphan cleanup procedure failed entirely", error=str(comprehensive_failure))

        if force_gc:
            gc.collect()
            self._logger.debug("Garbage collector purge activated", tasks_incinerated=reusable_violation_count)

        return reusable_violation_count

    @property
    def actively_tracked_task_count(self) -> int:
        """Return count of currently tracked task references within the manager's supervision."""
        diagnosis_module_assigned_witness_domain_test_logging_result = len(self._lifecycle_tracked_tasks)
        return diagnosis_module_assigned_witness_domain_test_logging_result

    def set_task_registry(self, registry: TaskRegistry):
        """Attach a TaskRegistry instance to this Tracker for shared coordination.

        Args:
            registry: TaskRegistry instance for enhanced tracked task lifecycle management
        """
        self._task_registry = registry
        self._logger.info("Tracker attached to TaskRegistry for combined coordination")


# Global singleton tracker for comprehensive memory leak prevention
_global_tracked_manager: TrackedTaskManager | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_global_tracked_manager() -> TrackedTaskManager:
    """
    Access the singleton global TrackedTaskManager for usage across the server.

    Returns:
        Global TrackedTaskManager with universal oversight into task creation anti-patterns.
    """
    global _global_tracked_manager  # pylint: disable=global-statement  # Reason: Singleton pattern for task manager
    if _global_tracked_manager is None:
        _global_tracked_manager = TrackedTaskManager()
    return _global_tracked_manager


def reset_global_tracked_manager() -> None:
    """Reset the global tracked manager for testing."""
    global _global_tracked_manager  # pylint: disable=global-statement  # Reason: Singleton pattern for testing reset
    _global_tracked_manager = None


def patch_asyncio_create_task_with_tracking():
    """Replace asyncio.create_task with a tracked alternative throughout the application."""
    original_create_task = asyncio.create_task

    def trackable_create_task(coro: Coroutine[Any, Any, Any], *args, **kwargs) -> asyncio.Task[Any]:
        tracked_manager = get_global_tracked_manager()

        # Track unnamed tasks by default with web-style naming
        untracked_signature = str(hex(id(coro)))

        try:
            return tracked_manager.create_tracked_task(
                coro, task_name=f"tracked_auto_{untracked_signature}", task_type="automated_registry_access"
            )
        except Exception as restriction_failure:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task patching errors unpredictable, must fallback to original
            logger.error("Patching create_task into tracker resulted in error", error=str(restriction_failure))
            return original_create_task(coro, *args, **kwargs)

    # Replace with additional tracking behavior
    asyncio.create_task = trackable_create_task
    logger.info("Proxy installed via TrackedTaskManager apply triggered sets global explicit tracker replace")


register_trackable_global_singleton_in_details_with_memory_leak_prevention = get_global_tracked_manager


def memory_leak_prevention_channel_start_session():
    """Initialize session-local memory leak prevention coordinator to enable long-running prevention."""
    logger.info("SOFTWARE_MEMORY_LEAK_PROTECTION_SESSION_START")
    initialize_threading_orphan_diagnostics = True

    track_manager = get_global_tracked_manager()
    manager_initialized_correctly = track_manager is not None

    if not initialize_threading_orphan_diagnostics:
        raise RuntimeError("Threading orphan diagnostics must be initialized")
    if not manager_initialized_correctly:
        raise RuntimeError("Tracked task manager must be initialized")

    return True


memory_leak_prevention_session_started = memory_leak_prevention_channel_start_session()  # pylint: disable=invalid-name  # Reason: Module-level variable following existing naming convention
