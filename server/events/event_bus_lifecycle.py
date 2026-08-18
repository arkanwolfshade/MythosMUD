"""Start/stop and destructor lifecycle for EventBus.

Extracted to keep event_bus.py under the Lizard file-nloc limit.
"""

# pyright: reportUninitializedInstanceVariable=false

from __future__ import annotations

import asyncio
from typing import override

from ..structured_logging.enhanced_logging_config import get_logger
from .event_bus_base import EventBusMixinBase

logger = get_logger("server.events.event_bus")


class EventBusLifecycleMixin(EventBusMixinBase):
    """Mixin: on-demand processing start, graceful stop, and destruction."""

    _running: bool
    _processing_task: asyncio.Task[object] | None

    @override
    def _ensure_async_processing(self) -> None:
        """Ensure async processing is started only when needed and within an event loop."""
        if not self._running and self._processing_task is None:
            try:
                loop = asyncio.get_running_loop()
                if loop.is_running():
                    self._running = True
                    self._processing_task = asyncio.create_task(self._process_events_async())
                    self._active_tasks.add(self._processing_task)
                    # Add callback to clean up task reference on completion
                    self._processing_task.add_done_callback(lambda task: self._active_tasks.discard(task))  # pylint: disable=unnecessary-lambda  # Reason: Lambda required for callback with discard method
                    self._logger.info(
                        "EventBus pure async processing started on-demand",
                        loop_running=loop.is_running(),
                        task_created=True,
                        task_name=self._processing_task.get_name()
                        if hasattr(self._processing_task, "get_name")
                        else "unknown",
                    )
                else:
                    self._logger.warning(
                        "EventBus: Loop exists but not running",
                        loop_running=loop.is_running(),
                    )
            except RuntimeError as e:
                # No running loop available - processing will start when first event published
                self._logger.warning(
                    "EventBus will start processing on first publish when event loop available",
                    error=str(e),
                    error_type=type(e).__name__,
                )
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event emission errors unpredictable, must handle gracefully
                # Unexpected error - log it
                self._logger.error(
                    "Unexpected error starting EventBus processing",
                    error=str(e),
                    error_type=type(e).__name__,
                    exc_info=True,
                )
        elif self._running:
            self._logger.debug(
                "EventBus already running",
                processing_task_exists=self._processing_task is not None,
                task_done=self._processing_task.done() if self._processing_task else None,
            )

    def _signal_shutdown(self) -> None:
        """Signal shutdown to async processing loop."""
        self._shutdown_event.set()
        try:
            self._event_queue.put_nowait(None)  # Sentinel to wake up waiting task
        except (asyncio.QueueFull, RuntimeError, AttributeError):
            # Queue is full, closed, or doesn't exist - task will wake up on timeout or cancellation
            pass

    async def _cancel_processing_task(self) -> None:
        """Cancel the main processing task if it exists."""
        if self._processing_task and not self._processing_task.done():
            try:
                if self._processing_task.cancel():
                    _ = await asyncio.wait_for(self._processing_task, timeout=0.5)
            except (TimeoutError, asyncio.CancelledError, RuntimeError):
                # Task was cancelled, timed out, or event loop is closing - expected
                pass

    def _cancel_task_quietly(self, task: asyncio.Task[object]) -> None:
        """Cancel a task, ignoring loop-closed and already-done races."""
        try:
            if not task.done() and not task.cancel():
                return
        except (RuntimeError, AttributeError):
            pass

    async def _abandon_pending_tasks(self, pending: set[asyncio.Task[object]]) -> None:
        """Cancel leftover tasks after the grace wait, then give them a short drain."""
        for task in pending:
            self._cancel_task_quietly(task)
        try:
            _ = await asyncio.wait_for(asyncio.gather(*pending, return_exceptions=True), timeout=0.2)
        except (TimeoutError, RuntimeError, asyncio.CancelledError):
            pass

    async def _cancel_and_wait_for_active_tasks(self) -> None:
        """Cancel all active tasks and wait for graceful shutdown."""
        if not self._active_tasks:
            return

        tasks_to_cancel = [task for task in list(self._active_tasks) if not task.done()]
        for task in tasks_to_cancel:
            self._cancel_task_quietly(task)
        if not tasks_to_cancel:
            return

        try:
            _done, pending = await asyncio.wait(  # pylint: disable=unused-variable  # noqa: F841  # Reason: done is part of asyncio.wait return tuple
                tasks_to_cancel, timeout=0.5, return_when=asyncio.ALL_COMPLETED
            )
            if pending:
                await self._abandon_pending_tasks(pending)
        except (RuntimeError, asyncio.CancelledError, AttributeError):
            pass

    def _finalize_shutdown(self) -> None:
        """Finalize shutdown by clearing tasks and logging."""
        self._active_tasks.clear()
        try:
            self._logger.info("EventBus pure async processing stopped")
        except Exception:  # pylint: disable=broad-exception-caught  # nosec B110  # noqa: B904  # Reason: Logging errors must not fail shutdown, if logging fails continue anyway
            pass

    async def _stop_processing(self) -> None:
        """Stop pure async event processing gracefully."""
        if not self._running:
            return

        self._running = False

        try:
            self._signal_shutdown()
            await self._cancel_processing_task()
            await self._cancel_and_wait_for_active_tasks()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Shutdown errors unpredictable, must prevent worker crashes
            try:
                logger.error(
                    "Error during event bus processing stop (non-fatal)",
                    error=str(e),
                    error_type=type(e).__name__,
                )
            except Exception:  # pylint: disable=broad-exception-caught  # nosec B110  # noqa: B904  # Reason: Logging errors must not fail shutdown, if logging fails continue anyway
                pass
        finally:
            self._finalize_shutdown()

    def _cleanup_tracked_subscriptions(self) -> None:
        """Unsubscribe every tracked service. No-op when none are registered."""
        if not self._subscriber_tracking:
            return
        service_ids = list(self._subscriber_tracking.keys())
        total_removed = sum(self.unsubscribe_all_for_service(service_id) for service_id in service_ids)
        self._logger.info(
            "Cleaned up service subscriptions during shutdown",
            services_cleaned=len(service_ids),
            total_subscriptions_removed=total_removed,
        )

    def _warn_shutdown_error(self, error: Exception) -> None:
        """Log a non-fatal shutdown error without letting logging fail the process."""
        try:
            self._logger.warning(
                "Error during EventBus shutdown (non-fatal)",
                error=str(error),
                error_type=type(error).__name__,
                exc_info=True,
            )
        except Exception:  # pylint: disable=broad-exception-caught  # nosec B110  # noqa: B904  # Reason: Logging errors must not crash workers, if logging fails just continue
            pass

    async def shutdown(self) -> None:
        """
        Shutdown the pure asyncio event bus with proper grace period coordination.

        This method is designed to be safe even when called multiple times or
        when the event loop is being torn down. All exceptions are caught to
        prevent worker crashes in pytest-xdist parallel execution.

        During shutdown, all service subscriptions are automatically cleaned up.
        """
        try:
            self._logger.info("Shutting down pure asyncio EventBus")
            self._cleanup_tracked_subscriptions()
            await self._stop_processing()
        except (RuntimeError, asyncio.CancelledError) as e:
            # Event loop is closing or task was cancelled - this is expected during test teardown
            self._logger.debug(
                "EventBus shutdown cancelled or event loop closing",
                error=str(e),
                error_type=type(e).__name__,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event processing errors unpredictable, must prevent worker crashes
            self._warn_shutdown_error(e)
        finally:
            self._running = False
            if self._processing_task is not None:
                self._cancel_task_quietly(self._processing_task)
            self._active_tasks.clear()

    def _cancel_active_tasks_best_effort(self) -> None:
        """Cancel subscriber tasks if a loop is still running; always clear the set."""
        if not self._active_tasks:
            return
        try:
            loop = asyncio.get_running_loop()
            if not loop.is_closed():
                for task in list(self._active_tasks):
                    self._cancel_task_quietly(task)
        except (RuntimeError, Exception):  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event loop cleanup errors unpredictable, must handle gracefully
            pass
        finally:
            self._active_tasks.clear()

    def __del__(self) -> None:
        """Cleanup when the EventBus is destroyed - replaced with async-aware graceful shutdown."""
        if not self._running:
            return
        try:
            self._logger.warning("EventBus destroyed without graceful shutdown")
        except (AttributeError, RuntimeError) as e:
            logger.error("Error during event bus destruction warning", error=str(e), error_type=type(e).__name__)

        self._running = False
        try:
            self._shutdown_event.set()
        except (AttributeError, RuntimeError) as e:
            logger.error("Error setting shutdown event", error=str(e), error_type=type(e).__name__)
        self._cancel_active_tasks_best_effort()
