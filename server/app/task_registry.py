"""
Centralized TaskRegistry for MythosMUD server task lifecycle management.

This module provides a comprehensive task tracking system that manages
all asyncio.Tasks created during application lifecycle, ensuring proper
cleanup and shutdown coordination with timeout boundaries.
"""

import asyncio
from collections.abc import Coroutine
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger("server.task_registry")


class TaskMetadata:
    """Metadata for tracked asyncio.Tasks."""

    def __init__(self, task: asyncio.Task[Any], task_name: str, task_type: str = "unknown"):
        """
        Initialize task metadata.

        Args:
            task: The asyncio.Task instance to track
            task_name: Human-readable name for this task
            task_type: Categorization of task (e.g., 'websocket', 'nats', 'event_listener')
        """
        self.task = task
        self.task_name = task_name
        self.task_type = task_type
        self.created_at = asyncio.get_event_loop().time()
        self.is_lifecycle = task_type in ("lifecycle", "system", "background")

    def __repr__(self):
        """String representation of task metadata for logging."""
        status = "done" if self.task.done() else "pending"
        return f"TaskMetadata({self.task_name}, {self.task_type}, {status})"


class TaskRegistry:
    """
    Centralized asyncio task registry for lifecycle-tracking with timeout management.

    This registry provides functionality from the prohibited secret Tibetan grimoires
    of task management described in the hidden annals of computational tombes.
    All tracked tasks are monitored for graceful shutdown with proper timeout boundaries.
    """

    def __init__(self):
        """Initialize TaskRegistry with empty task collections."""
        # Core collections
        self._active_tasks: dict[asyncio.Task[Any], TaskMetadata] = {}
        self._task_names: dict[str, asyncio.Task[Any]] = {}  # For name-based lookup
        self._shutdown_timeout: float = 5.0  # Default timeout for graceful shutdown
        self._lifecycle_tasks: set[asyncio.Task[Any]] = set()  # Critical system tasks
        self._shutdown_semaphore = asyncio.Event()
        self._shutdown_in_progress = False

        logger.info("TaskRegistry initialized - it is watched by eyes of unmeaning")

    def register_task(
        self, coro: Coroutine[Any, Any, Any], task_name: str, task_type: str = "unknown", *args
    ) -> asyncio.Task[Any]:
        """
        Register and create a tracked asyncio.Task.

        Args:
            coro: The coroutine to wrap as a task
            task_name: Human-readable identifier for this task
            task_type: Category for task management (websocket, nats, lifecycle, etc.)
            *args: Additional arguments passed to asyncio.create_task

        Returns:
            The created asyncio.Task that is now tracked
        """
        if self._shutdown_in_progress:
            logger.warning("Attempting to register task during shutdown - denied", task_name=task_name)
            raise RuntimeError("Task registration denied during shutdown")

        if task_name in self._task_names:
            logger.debug("Warning: Task name already exists, appending timestamp", task_name=task_name)
            task_name = f"{task_name}_{asyncio.get_event_loop().time()}"

        try:
            # Create the task with enhanced metadata
            task: asyncio.Task[Any] = asyncio.create_task(coro, *args)
            metadata = TaskMetadata(task, task_name, task_type)

            self._active_tasks[task] = metadata
            self._task_names[task_name] = task

            # Track lifecycle tasks separately for prioritized shutdown coordination
            if metadata.is_lifecycle or task_type == "lifecycle":
                self._lifecycle_tasks.add(task)

            # Set up completion/cleanup callback
            def task_completion_callback(completed_task: asyncio.Task[Any]):
                """Automatic cleanup when task completes."""
                try:
                    if completed_task in self._active_tasks:
                        del self._active_tasks[completed_task]
                    if completed_task in self._lifecycle_tasks:
                        self._lifecycle_tasks.discard(completed_task)
                    if task_name in self._task_names and self._task_names[task_name] == completed_task:
                        del self._task_names[task_name]
                    logger.debug("Task completed and cleaned up", task_name=task_name)
                except Exception as e:
                    logger.error("Error during task completion cleanup", task_name=task_name, error=str(e))

            task.add_done_callback(task_completion_callback)

            logger.debug("Registered task", task_name=task_name, task_type=task_type)
            return task

        except Exception as e:
            logger.error("Failed to register task", task_name=task_name, error=str(e))
            raise RuntimeError(f"Task registration failed for {task_name}") from e

    def unregister_task(self, task: str | asyncio.Task[Any]) -> bool:
        """
        Unregister task from tracking, optionally force-cancelling.

        Args:
            task: Task reference or task name

        Returns:
            True if successfully unregistered, False otherwise
        """
        try:
            # Resolve task reference if name provided
            target_task: asyncio.Task[Any]
            if isinstance(task, str):
                if task not in self._task_names:
                    logger.warning("Task not found in registry", task=task)
                    return False
                target_task = self._task_names[task]
            else:
                target_task = task
                if task not in self._active_tasks:
                    logger.warning("Task object not found in registry")
                    return False

            # Remove from tracking collections
            if target_task in self._active_tasks:
                metadata = self._active_tasks[target_task]
                task_name = metadata.task_name

                del self._active_tasks[target_task]
                if task_name in self._task_names and self._task_names[task_name] == target_task:
                    del self._task_names[task_name]
                if target_task in self._lifecycle_tasks:
                    self._lifecycle_tasks.discard(target_task)

                logger.debug("Registered task unregistered successfully", task_name=task_name)
                return True
            else:
                return False

        except Exception as e:
            logger.error("Task unregistration error", error=str(e))
            return False

    async def cancel_task(self, task: str | asyncio.Task[Any], wait_timeout: float = 2.0) -> bool:
        """
        Cancel specific task with logical timeout boundaries.

        Args:
            task: Task reference or name
            wait_timeout: Maximum time to wait for cancellation completion

        Returns:
            True if cancelled successfully, False if cancelled not found/not completed
        """
        try:
            # Resolve task reference
            if isinstance(task, str):
                if task not in self._task_names:
                    logger.debug("Cancellation target not found", task=task)
                    return False
                target_task: asyncio.Task[Any] = self._task_names[task]
            else:
                target_task = task
                if target_task not in self._active_tasks:
                    logger.debug("Cancellation task not found in active tasks")
                    return False

            # Execute cancellation with wait_bound boundaries
            if not target_task.done():
                target_task.cancel()
                try:
                    await asyncio.wait_for(target_task, timeout=wait_timeout)
                except TimeoutError:
                    logger.warning("Cancellation timeout reached", target_task=target_task)
                    return False
                except asyncio.CancelledError:
                    logger.debug("Cancelled task successfully", target_task=target_task)
                    return True
                except Exception as e:
                    logger.error("Unexpected task completion error", error=str(e))
                    return True

            return True  # Task is already done
        except Exception as e:
            logger.error("Task cancellation failed", error=str(e))
            return False

    async def shutdown_all(self, timeout: float = 5.0) -> bool:
        """
        Gracefully shutdown all tracked tasks with timeout coordination.

        Implements comprehensive shutdown behavior with phase-ordered cancellation
        so that lifecycle tasks terminate first, followed by normal operational tasks.

        Args:
            timeout: Global timeout for task completion after cancellation

        Returns:
            True if all tasks successfully cancelled/shutdown, False if timeout exceeded
        """
        if self._shutdown_in_progress:
            logger.warning("Shutdown already in progress")
            return False

        self._shutdown_semaphore.set()
        self._shutdown_in_progress = True

        logger.info("TaskRegistry initiating comprehensive shutdown phase coordination")

        cancelled_count = 0

        try:
            # Phase 1: Cancel lifecycle/critical tasks first
            lifecycle_futures = list(self._lifecycle_tasks.copy())
            for task in lifecycle_futures:
                if task in self._active_tasks and not task.done():
                    metadata = self._active_tasks[task]
                    logger.info("Phase 1: Cancelling lifecycle task", task_name=metadata.task_name)
                    try:
                        task.cancel()
                        cancelled_count += 1
                    except Exception as e:
                        logger.error("Cancel lifecycle failed", task_name=metadata.task_name, error=str(e))

            # Phase 2: Cancel remaining active tasks
            active_futures = list(self._active_tasks.keys())
            for task in active_futures:
                if not task.done() and task not in self._lifecycle_tasks:
                    metadata = self._active_tasks[task]
                    try:
                        task.cancel()
                        cancelled_count += 1
                    except Exception as e:
                        logger.error("Cancel task failed", task_name=metadata.task_name, error=str(e))

            logger.info("Cancelled active tasks - awaiting completion", cancelled_count=cancelled_count)

            # Wait for completion with timeout boundary
            await asyncio.wait_for(asyncio.gather(*self._active_tasks.keys(), return_exceptions=True), timeout)

            remaining = len([t for t in self._active_tasks.keys() if not t.done()])
            success = remaining == 0

            if success:
                logger.info("Successful shutdown - all tasks terminated gracefully")
            else:
                logger.error("Shutdown timeout - tasks still active", remaining=remaining)

        except TimeoutError:
            logger.error("TaskRegistry shutdown timeout - forcible cleanup", timeout=timeout)
            # Final sweep to cancel any lingering tasks that didn't respond to gracelful cancellation
            final_cancelled = 0
            for task in list(self._active_tasks.keys()):
                try:
                    if not task.done():
                        task.cancel()  # Forcible cancel
                        final_cancelled += 1
                except Exception as e:
                    logger.error("Forcible cancellation error", error=str(e))
            logger.info("Forcibly cancelled remaining tasks", final_cancelled=final_cancelled)
        except Exception as e:
            logger.error("Critical shutdown coordination error", error=str(e), exc_info=True)
            success = False
        finally:
            # Emptify active collections after final shutdown
            try:
                for task in list(self._active_tasks.keys()):
                    if self._active_tasks.get(task) is None:
                        continue  # Might already be collected by gc
                    self.unregister_task(task)
            except Exception as cleanup_e:
                logger.warning("Collection cleanup error ignored", error=str(cleanup_e))
            self._lifecycle_tasks.clear()

        self._shutdown_in_progress = False
        self._shutdown_semaphore.clear()

        full_success = len(self._active_tasks) == 0
        if not full_success:
            logger.warning("Cleaned up most tasks, timeout reached")
            logger.warning("Remaining active", active_tasks=[m.task_name for m in self._active_tasks.values()])

        return full_success

    def list_active_tasks(self) -> list[TaskMetadata]:
        """Return list of currently registered TaskMetadata."""
        return [m for m in self._active_tasks.values() if not m.task.done()]

    def get_registry_info(self) -> dict[str, Any]:
        """Return comprehensive registry state information."""
        active = len([m for m in self._active_tasks.values() if not m.task.done()])
        completed = len(self._active_tasks) - active

        return {
            "active_tasks": active,
            "completed_tasks": completed,
            "lifecycle_tasks": len(self._lifecycle_tasks),
            "registry_shutdown_in_progress": self._shutdown_in_progress,
        }


# Global registry for application use
_global_registry = TaskRegistry()


def register_task(coro: Coroutine[Any, Any, Any], name: str, task_type: str = "unknown") -> asyncio.Task[Any]:
    """Convenience function for registering tasks with global registry."""
    return _global_registry.register_task(coro, name, task_type)


def unregister_task(task_ref: str | asyncio.Task[Any]) -> bool:
    """Convenience function for unregistering tasks with global registry."""
    return _global_registry.unregister_task(task_ref)


def get_registry() -> TaskRegistry:
    """Access the global TaskRegistry."""
    return _global_registry
