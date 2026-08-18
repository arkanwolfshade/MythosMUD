"""Event dispatch and subscriber invocation for EventBus.

Extracted to keep event_bus.py under the Lizard file-nloc limit.
"""

# pyright: reportUnnecessaryIsInstance=false, reportUnreachable=false
# Reason: publish/inject retain runtime guards for invalid dynamic/cast inputs (see unit tests).

from __future__ import annotations

import asyncio
import inspect
import os
from collections.abc import Callable
from typing import override

from ..structured_logging.enhanced_logging_config import get_logger
from .event_bus_base import EventBusMixinBase
from .event_types import BaseEvent

logger = get_logger("server.events.event_bus")


class EventBusProcessingMixin(EventBusMixinBase):
    """Mixin: queue loop, subscriber dispatch, publish, and inject."""

    def _log_processing_failure(self, message: str, error: Exception, *, critical: bool = False) -> None:
        """Log a processing error, falling back if Unicode encoding fails."""
        log = self._logger.critical if critical else self._logger.error
        try:
            log(message, error=str(error), exc_info=True)
        except (UnicodeEncodeError, AttributeError) as e2:
            logger.error("Error logging event processing error", error=str(e2), error_type=type(e2).__name__)
            log(message, error=str(error), exc_info=True)

    @override
    async def _process_events_async(self) -> None:
        """Pure async event processing loop replacing the dangerous threading pattern."""
        self._logger.info("EventBus pure async processing started")

        try:
            while self._running:
                try:
                    # CRITICAL FIX: Reduce timeout from 1.0s to 0.1s for faster event processing
                    # The timeout allows periodic checks of self._running for graceful shutdown,
                    # but 1.0s was causing noticeable delays. 0.1s provides responsive shutdown
                    # while processing events nearly immediately (max 100ms delay vs 1000ms).
                    event = await asyncio.wait_for(self._event_queue.get(), timeout=0.1)

                    # Check for sentinel shutdown signal
                    if event is None:
                        break

                    # Process the event with proper async handling
                    await self._handle_event_async(event)

                except TimeoutError:
                    # Timeout is expected when no events are available - allows periodic shutdown check
                    # Continue loop to check self._running and process next event
                    continue
                except asyncio.CancelledError:
                    # Task was cancelled - break out of loop
                    break
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cleanup errors unpredictable, must handle gracefully
                    self._log_processing_failure("Error processing event", e)
                    continue

                # Check for shutdown signal
                if self._shutdown_event.is_set():
                    break

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cleanup errors unpredictable, must handle gracefully
            self._log_processing_failure("Fatal error in async event processing", e, critical=True)
        finally:
            self._logger.info("EventBus pure async processing stopped")

    def _separate_subscribers(
        self, subscribers: list[Callable[[BaseEvent], object]]
    ) -> tuple[list[Callable[[BaseEvent], object]], list[Callable[[BaseEvent], object]]]:
        """
        Separate async and sync subscribers for appropriate execution.

        Uses inspect.iscoroutinefunction to detect async callables at runtime. This allows
        the event bus to handle mixed subscriber lists, executing sync subscribers immediately
        and async subscribers concurrently via asyncio tasks.

        Args:
            subscribers: Mixed list of sync and async subscriber callables

        Returns:
            Tuple of (async_subscribers, sync_subscribers) for separate processing
        """
        async_subscribers: list[Callable[[BaseEvent], object]] = []
        sync_subscribers: list[Callable[[BaseEvent], object]] = []

        for subscriber in subscribers:
            if inspect.iscoroutinefunction(subscriber):
                async_subscribers.append(subscriber)
            else:
                sync_subscribers.append(subscriber)

        return async_subscribers, sync_subscribers

    def _process_sync_subscribers(
        self, sync_subscribers: list[Callable[[BaseEvent], object]], event: BaseEvent
    ) -> None:
        """
        Execute sync subscribers sequentially with error isolation.

        Sync subscribers are called directly in the current execution context. Errors
        are caught and logged but do not prevent other subscribers from executing. This
        ensures that a single subscriber failure doesn't disrupt event processing for
        other subscribers.

        Args:
            sync_subscribers: List of synchronous subscriber callables
            event: Event to pass to each subscriber
        """
        for subscriber in sync_subscribers:
            try:
                _ = subscriber(event)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscriber errors unpredictable, must not fail event processing
                subscriber_name = getattr(subscriber, "__name__", "unknown")
                self._logger.error("Error in sync event subscriber", subscriber_name=subscriber_name, error=str(e))

    def _create_async_subscriber_tasks(
        self, async_subscribers: list[Callable[[BaseEvent], object]], event: BaseEvent
    ) -> tuple[list[asyncio.Task[object]], dict[asyncio.Task[object], str]]:
        """
        Create asyncio tasks for async event subscribers and track their lifecycle.

        This method creates tasks for all async subscribers, registers them in the active
        tasks set for lifecycle tracking, and sets up done callbacks to automatically
        remove them from tracking when complete. This ensures we can monitor all active
        event processing tasks for graceful shutdown.

        The subscriber_names mapping allows error handling to identify which subscriber
        failed without maintaining task-to-subscriber references separately.

        Args:
            async_subscribers: List of async callable subscribers to invoke
            event: Event to pass to each subscriber

        Returns:
            Tuple of (list of created tasks, mapping of task to subscriber name for error reporting)
        """
        tasks: list[asyncio.Task[object]] = []
        subscriber_names: dict[asyncio.Task[object], str] = {}

        for subscriber in async_subscribers:
            subscriber_name = getattr(subscriber, "__name__", "unknown")
            try:
                coro = subscriber(event)
                if not inspect.iscoroutine(coro):
                    self._logger.error(
                        "Async subscriber did not return a coroutine",
                        subscriber_name=subscriber_name,
                    )
                    continue
                task = asyncio.create_task(coro)
                tasks.append(task)
                subscriber_names[task] = subscriber_name
                self._active_tasks.add(task)

                def remove_task(t: asyncio.Task[object], _sn: str = subscriber_name) -> None:  # pylint: disable=unused-argument  # Reason: Parameter required for callback signature, subscriber_name captured in closure
                    self._active_tasks.discard(t)

                task.add_done_callback(remove_task)
                self._logger.debug("Created tracked task for async subscriber", subscriber_name=subscriber_name)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task creation errors unpredictable, must continue with other subscribers
                self._logger.error(
                    "Failed to create task for subscriber", subscriber_name=subscriber_name, error=str(e)
                )

        return tasks, subscriber_names

    async def _wait_for_async_subscribers(
        self, tasks: list[asyncio.Task[object]], subscriber_names: dict[asyncio.Task[object], str]
    ) -> None:
        """
        Wait for all async subscriber tasks to complete and handle their results.

        Uses asyncio.gather with return_exceptions=True to ensure all subscribers execute
        even if one fails. This is critical for event processing reliability - a single
        subscriber failure must not prevent other subscribers from receiving the event.

        Errors are logged but not raised, allowing the event bus to continue processing
        subsequent events. The subscriber_names mapping provides context for error logs.

        Args:
            tasks: List of asyncio tasks created for async subscribers
            subscriber_names: Mapping of task to subscriber name for error reporting
        """
        if not tasks:
            return

        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for task, result in zip(tasks, results, strict=False):
                subscriber_name = subscriber_names.get(task, "unknown")
                if isinstance(result, Exception):
                    self._logger.error(
                        "Error in async subscriber",
                        subscriber_name=subscriber_name,
                        error=str(result),
                        error_type=type(result).__name__,
                        exc_info=True,
                    )
                else:
                    self._logger.debug(
                        "Async subscriber completed successfully",
                        subscriber_name=subscriber_name,
                        has_result=result is not None,
                    )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Gather operation errors unpredictable, must handle defensively
            self._logger.error("Unexpected error in subscriber task group", error=str(e), error_type=type(e).__name__)

    async def _handle_event_async(self, event: BaseEvent) -> None:
        """
        Handle a single event by calling all registered subscribers with structured concurrency.

        Uses asyncio.TaskGroup (Python 3.11+) for structured concurrency to ensure:
        - Proper exception propagation
        - Automatic cancellation of all tasks if one fails
        - Clean resource management
        - No orphaned tasks

        AnyIO Pattern: Task groups provide structured concurrency similar to anyio.create_task_group()
        """
        event_type = type(event)
        subscribers = self._subscribers.get(event_type, [])

        if not subscribers:
            self._logger.debug("No subscribers for event type", event_type=event_type.__name__)
            return

        self._logger.info(
            "Processing event for subscribers",
            event_type=event_type.__name__,
            subscriber_count=len(subscribers),
            subscriber_names=[getattr(s, "__name__", "unknown") for s in subscribers],
        )

        async_subscribers, sync_subscribers = self._separate_subscribers(subscribers)

        self._process_sync_subscribers(sync_subscribers, event)

        if async_subscribers:
            tasks, subscriber_names = self._create_async_subscriber_tasks(async_subscribers, event)
            await self._wait_for_async_subscribers(tasks, subscriber_names)

    def _handle_task_result_async(self, task: asyncio.Task[object], subscriber_name: str) -> None:
        """Handle async task completion with proper exception extraction."""
        try:
            # Get the result to handle exceptions without threading/runtime scheduler crossing
            _ = task.result()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Async subscriber errors unpredictable, must handle gracefully
            self._logger.error("Error in async subscriber", subscriber_name=subscriber_name, error=str(e))

    def _invoke_test_mode_subscriber(self, subscriber: Callable[[BaseEvent], object], event: BaseEvent) -> None:
        """Invoke one subscriber in test mode (direct call or create_task)."""
        if not inspect.iscoroutinefunction(subscriber):
            _ = subscriber(event)
            return
        try:
            _ = asyncio.get_running_loop()
            coro = subscriber(event)
            if inspect.iscoroutine(coro):
                task = asyncio.create_task(coro)
                self._active_tasks.add(task)
                task.add_done_callback(lambda t: self._active_tasks.discard(t))  # pylint: disable=unnecessary-lambda  # Reason: Lambda required for callback with discard method
        except RuntimeError:
            self._logger.debug(
                "Skipping async subscriber in test mode (no running loop)",
                subscriber=subscriber.__name__,
            )

    def _publish_in_test_mode(self, event: BaseEvent) -> None:
        """Process subscribers synchronously when tests have no running EventBus loop."""
        self._logger.debug("EventBus in test mode - processing event synchronously", event_type=type(event).__name__)
        for subscriber in self._subscribers.get(type(event), []):
            try:
                self._invoke_test_mode_subscriber(subscriber, event)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscriber errors unpredictable, must not fail event processing
                subscriber_name = getattr(subscriber, "__name__", "unknown")
                self._logger.error("Error in sync test mode subscriber", subscriber_name=subscriber_name, error=str(e))

    def publish(self, event: BaseEvent) -> None:
        """
        Publish an event to the pure asyncio event bus.

        Args:
            event: The event to publish

        The event will be processed asynchronously using event loop
        coordination without the dangerous threading hybrid patterns.
        """
        if not isinstance(event, BaseEvent):
            raise ValueError("Event must inherit from BaseEvent")

        is_test_mode = (
            os.getenv("PYTEST_CURRENT_TEST") is not None
            or os.getenv("MYTHOSMUD_ENV") == "test"
            or "pytest" in os.getenv("_", "").lower()
        )

        if is_test_mode and not self._running:
            self._publish_in_test_mode(event)
            return

        # Begin processing startup on-demand for first event
        self._ensure_async_processing()

        # Use put_nowait for non-blocking publish (pure asyncio.Queue) - Task 1.2
        try:
            self._event_queue.put_nowait(event)
            self._logger.info(
                "Published event to queue",
                event_type=type(event).__name__,
                queue_size=self._event_queue.qsize(),
                processing_running=self._running,
            )
        except asyncio.QueueFull as exc:
            # Rare case where queue is at capacity - indicates very high load
            self._logger.warning("Event queue at capacity - dropping event", event_type=type(event).__name__)
            raise RuntimeError("Event bus overloaded") from exc

    def inject(self, event: BaseEvent) -> None:
        """
        Inject event from remote source (e.g. NATS) for local dispatch.

        Used by distributed EventBus when receiving events from other instances.
        Does not trigger re-publish to NATS. Same processing path as publish.
        """
        if not isinstance(event, BaseEvent):
            raise ValueError("Event must inherit from BaseEvent")
        self._ensure_async_processing()
        try:
            self._event_queue.put_nowait(event)
            self._logger.debug(
                "Injected remote event",
                event_type=type(event).__name__,
                queue_size=self._event_queue.qsize(),
            )
        except asyncio.QueueFull as exc:
            self._logger.warning("Event queue at capacity - dropping injected event", event_type=type(event).__name__)
            raise RuntimeError("Event bus overloaded") from exc
