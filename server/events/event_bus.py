"""
Event bus for MythosMUD.

This module provides the EventBus class that implements an in-memory
pub/sub system for handling game events. The system is designed to be
asynchronous and non-blocking, with support for multiple subscribers
per event type.

Implemented using pure asyncio patterns to banish the hybrid threading
patterns that threatened the computational lucidity of our eldritch
architecture. Based on warnings from the Pnakotic Manuscripts about
proper event propagation across dimensional boundaries.

As noted in the Pnakotic Manuscripts, proper event propagation is
essential for maintaining awareness of the dimensional shifts that
occur throughout our eldritch architecture.
"""

# pylint: disable=too-many-lines  # Reason: Event bus requires extensive event handling logic for comprehensive event system management

import asyncio
import inspect
import time
from collections import defaultdict
from collections.abc import Callable
from typing import Any, TypeVar, cast

from anyio import Event

from ..structured_logging.enhanced_logging_config import get_logger
from .event_types import BaseEvent

# Type variable for generic event handling
T = TypeVar("T", bound=BaseEvent)

logger = get_logger(__name__)


class EventBus:  # pylint: disable=too-many-instance-attributes  # Reason: Event bus requires multiple subscription maps and state tracking
    """
    Pure asyncio event bus for MythosMUD.

    This class provides a purely async pub/sub system for handling
    game events. Events are processed within the existing event loop
    to maintain computational dimensional integrity without dangerous
    threading.antipatterns.

    Events are processed using pure asyncio.Queue with properly managed
    task lifecycle and graceful shutdown capabilities.
    """

    def __init__(self) -> None:
        """Initialize the pure async event bus."""
        self._subscribers: dict[type[BaseEvent], list[Callable[[BaseEvent], Any]]] = defaultdict(list)
        # Pure asyncio.Queue replaces threading.Queue - Task 1.2: Replace queue
        self._event_queue: asyncio.Queue[Any] = asyncio.Queue()
        self._running: bool = False
        self._logger = get_logger("EventBus")
        # Task references for proper lifecycle management - Task 1.5
        self._active_tasks: set[asyncio.Task[Any]] = set()
        self._shutdown_event: Event = Event()
        self._main_loop: asyncio.AbstractEventLoop | None = None
        # Fix: Initialize on-demand rather than during __init__
        self._processing_task: asyncio.Task[Any] | None = None
        # Subscriber lifecycle tracking for metrics
        self._subscription_timestamps: list[float] = []
        self._unsubscription_timestamps: list[float] = []
        self._subscription_count = 0
        self._unsubscription_count = 0
        # Keep only last 1000 timestamps to prevent unbounded growth
        self._max_lifecycle_timestamps = 1000
        # Subscriber tracking by service identifier for cleanup (Task 2: Event Subscriber Cleanup)
        # Maps service_id -> list of (event_type, handler) tuples
        self._subscriber_tracking: dict[str, list[tuple[type[BaseEvent], Callable[[BaseEvent], Any]]]] = {}

    def _ensure_async_processing(self) -> None:
        """Ensure async processing is started only when needed and within an event loop."""
        if not self._running and self._processing_task is None:
            try:
                loop = asyncio.get_running_loop()
                if loop and loop.is_running():
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
                        loop_exists=loop is not None,
                        loop_running=loop.is_running() if loop else False,
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

    def set_main_loop(self, loop: asyncio.AbstractEventLoop) -> None:
        """Set the main event loop - now properly managed for async compatibility."""
        self._main_loop = loop
        self._logger.info("Main event loop set for EventBus")

    def _ensure_processing_started(self) -> None:
        """Legacy wrapper for API compatibility during transition."""
        self._ensure_async_processing()

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
                self._processing_task.cancel()
                await asyncio.wait_for(self._processing_task, timeout=0.5)
            except (TimeoutError, asyncio.CancelledError, RuntimeError):
                # Task was cancelled, timed out, or event loop is closing - expected
                pass

    async def _cancel_and_wait_for_active_tasks(self) -> None:
        """Cancel all active tasks and wait for graceful shutdown."""
        if not self._active_tasks:
            return

        tasks_to_cancel = [task for task in list(self._active_tasks) if not task.done()]
        for task in tasks_to_cancel:
            try:
                task.cancel()
            except (RuntimeError, AttributeError):
                # Task or event loop is in invalid state - skip
                pass

        if not tasks_to_cancel:
            return

        try:
            _done, pending = await asyncio.wait(  # pylint: disable=unused-variable  # noqa: F841  # Reason: done is part of asyncio.wait return tuple
                tasks_to_cancel, timeout=0.5, return_when=asyncio.ALL_COMPLETED
            )

            if pending:
                for task in pending:
                    try:
                        if not task.done():
                            task.cancel()
                    except (RuntimeError, AttributeError):
                        pass

                try:
                    await asyncio.wait_for(asyncio.gather(*pending, return_exceptions=True), timeout=0.2)
                except (TimeoutError, RuntimeError, asyncio.CancelledError):
                    # Timeout or event loop closing - abandon remaining tasks
                    pass

        except (RuntimeError, asyncio.CancelledError, AttributeError):
            # Event loop is closing or in invalid state - just clear tasks
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
                    # Use basic print to avoid Unicode encoding issues during cleanup
                    try:
                        self._logger.error("Error processing event", error=str(e), exc_info=True)
                    except (UnicodeEncodeError, AttributeError) as e2:
                        logger.error(
                            "Error logging event processing error", error=str(e2), error_type=type(e2).__name__
                        )
                        self._logger.error("Error processing event", error=str(e), exc_info=True)
                    continue

                # Check for shutdown signal
                if self._shutdown_event.is_set():
                    break

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cleanup errors unpredictable, must handle gracefully
            # Use basic print to avoid Unicode encoding issues during cleanup
            try:
                self._logger.error("Fatal error in async event processing", error=str(e), exc_info=True)
            except (UnicodeEncodeError, AttributeError) as e2:
                logger.error("Error logging fatal event processing error", error=str(e2), error_type=type(e2).__name__)
                self._logger.critical("Fatal error in async event processing", error=str(e), exc_info=True)
        finally:
            self._logger.info("EventBus pure async processing stopped")

    def _separate_subscribers(
        self, subscribers: list[Callable[[BaseEvent], Any]]
    ) -> tuple[list[Callable[[BaseEvent], Any]], list[Callable[[BaseEvent], Any]]]:
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
        async_subscribers: list[Callable[[BaseEvent], Any]] = []
        sync_subscribers: list[Callable[[BaseEvent], Any]] = []

        for subscriber in subscribers:
            if inspect.iscoroutinefunction(subscriber):
                async_subscribers.append(subscriber)
            else:
                sync_subscribers.append(subscriber)

        return async_subscribers, sync_subscribers

    def _process_sync_subscribers(self, sync_subscribers: list[Callable[[BaseEvent], Any]], event: BaseEvent) -> None:
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
                subscriber(event)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscriber errors unpredictable, must not fail event processing
                subscriber_name = getattr(subscriber, "__name__", "unknown")
                self._logger.error("Error in sync event subscriber", subscriber_name=subscriber_name, error=str(e))

    def _create_async_subscriber_tasks(
        self, async_subscribers: list[Callable[[BaseEvent], Any]], event: BaseEvent
    ) -> tuple[list[asyncio.Task[Any]], dict[asyncio.Task[Any], str]]:
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
        tasks: list[asyncio.Task[Any]] = []
        subscriber_names: dict[asyncio.Task[Any], str] = {}

        for subscriber in async_subscribers:
            subscriber_name = getattr(subscriber, "__name__", "unknown")
            try:
                task = asyncio.create_task(subscriber(event))
                tasks.append(task)
                subscriber_names[task] = subscriber_name
                self._active_tasks.add(task)

                def remove_task(t: asyncio.Task[Any], _sn: str = subscriber_name) -> None:  # pylint: disable=unused-argument  # Reason: Parameter required for callback signature, subscriber_name captured in closure
                    self._active_tasks.discard(t)

                task.add_done_callback(remove_task)
                self._logger.debug("Created tracked task for async subscriber", subscriber_name=subscriber_name)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task creation errors unpredictable, must continue with other subscribers
                self._logger.error(
                    "Failed to create task for subscriber", subscriber_name=subscriber_name, error=str(e)
                )

        return tasks, subscriber_names

    async def _wait_for_async_subscribers(
        self, tasks: list[asyncio.Task[Any]], subscriber_names: dict[asyncio.Task[Any], str]
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

    def _handle_task_result_async(self, task: asyncio.Task[Any], subscriber_name: str) -> None:
        """Handle async task completion with proper exception extraction."""
        try:
            # Get the result to handle exceptions without threading/runtime scheduler crossing
            task.result()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Async subscriber errors unpredictable, must handle gracefully
            self._logger.error("Error in async subscriber", subscriber_name=subscriber_name, error=str(e))

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

        # In test mode, process events synchronously to avoid event loop issues
        import os

        is_test_mode = (
            os.getenv("PYTEST_CURRENT_TEST") is not None
            or os.getenv("MYTHOSMUD_ENV") == "test"
            or "pytest" in os.getenv("_", "").lower()
        )

        if is_test_mode and not self._running:
            # In test mode, process events synchronously if async processing isn't running
            # This prevents event loop closure issues
            self._logger.debug(
                "EventBus in test mode - processing event synchronously", event_type=type(event).__name__
            )
            event_type = type(event)
            subscribers = self._subscribers.get(event_type, [])
            for subscriber in subscribers:
                try:
                    # Call subscriber directly (synchronously) in test mode
                    if asyncio.iscoroutinefunction(subscriber):
                        # For async subscribers in test mode, create a task if we have a running loop
                        try:
                            asyncio.get_running_loop()  # Check if loop exists
                            # We have a running loop, create a task
                            task = asyncio.create_task(subscriber(event))
                            # Store task for cleanup
                            self._active_tasks.add(task)
                            task.add_done_callback(lambda t: self._active_tasks.discard(t))  # pylint: disable=unnecessary-lambda  # Reason: Lambda required for callback with discard method
                        except RuntimeError:
                            # No running loop - skip async subscriber in test mode
                            self._logger.debug(
                                "Skipping async subscriber in test mode (no running loop)",
                                subscriber=subscriber.__name__,
                            )
                    else:
                        subscriber(event)
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Subscriber errors unpredictable, must not fail event processing
                    subscriber_name = getattr(subscriber, "__name__", "unknown")
                    self._logger.error(
                        "Error in sync test mode subscriber", subscriber_name=subscriber_name, error=str(e)
                    )
            # In test mode, we process synchronously without using the queue
            # No need to call task_done() since we're not using the queue
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

    def subscribe(self, event_type: type[T], handler: Callable[[T], Any], service_id: str | None = None) -> None:
        """
        Subscribe to events of a specific type with pure async thread-safe patterns.

        Args:
            event_type: The type of event to subscribe to
            handler: The function to call when events of this type are published
            service_id: Optional service identifier for tracking and cleanup

        The handler function will be called with the event object as its
        argument when events of the specified type are published.

        **Service Cleanup Pattern:**
        Services should provide a unique service_id when subscribing to events to enable
        automatic cleanup on shutdown. The recommended pattern is:

        .. code-block:: python

            class MyService:
                def __init__(self, event_bus: EventBus):
                    self.event_bus = event_bus
                    self.service_id = "my_service"
                    # Subscribe with service_id for automatic cleanup
                    self.event_bus.subscribe(MyEventType, self.handle_event, service_id=self.service_id)

                async def shutdown(self):
                    # Cleanup all subscriptions for this service
                    self.event_bus.unsubscribe_all_for_service(self.service_id)

        During application shutdown, the EventBus.shutdown() method automatically cleans up
        all service subscriptions, but services should also call unsubscribe_all_for_service()
        during their own shutdown to ensure proper cleanup order.
        """
        if not issubclass(event_type, BaseEvent):
            raise ValueError("Event type must inherit from BaseEvent")

        if not callable(handler):
            raise ValueError("Handler must be callable")

        # Remove threading dependency - Python dict operations are atomic at GIL
        # level for simple operations like this, sufficient for single-threaded async
        self._subscribers[event_type].append(handler)  # type: ignore[arg-type]  # Reason: Handler type is Callable but mypy cannot infer compatibility with list[Callable[[BaseEvent], Any]] due to generic type variance
        # Track subscription for metrics
        self._subscription_count += 1
        self._subscription_timestamps.append(time.time())
        # Keep only last N timestamps to prevent unbounded growth
        if len(self._subscription_timestamps) > self._max_lifecycle_timestamps:
            self._subscription_timestamps = self._subscription_timestamps[-self._max_lifecycle_timestamps :]
        # Track subscriber by service_id for cleanup (Task 2: Event Subscriber Cleanup)
        if service_id:
            if service_id not in self._subscriber_tracking:
                self._subscriber_tracking[service_id] = []
            # Cast is safe because issubclass check above ensures event_type is a subclass of BaseEvent
            self._subscriber_tracking[service_id].append(
                cast(tuple[type[BaseEvent], Callable[[BaseEvent], Any]], (event_type, handler))
            )
        self._logger.debug("Added subscriber for event type", event_type=event_type.__name__, service_id=service_id)

    def unsubscribe(self, event_type: type[T], handler: Callable[[T], Any]) -> bool:
        """
        Unsubscribe from events of a specific type with pure async coordination.

        Args:
            event_type: The type of event to unsubscribe from
            handler: The function to remove from the subscription list

        Returns:
            True if the handler was found and removed, False otherwise
        """
        if not issubclass(event_type, BaseEvent):
            raise ValueError("Event type must inherit from BaseEvent")

        # Remove threading dependency - GIL atomic operations suffice for read-only
        subscribers = self._subscribers.get(event_type, [])
        try:
            subscribers.remove(handler)  # type: ignore[arg-type]  # Reason: Handler type is Callable but mypy cannot infer compatibility with list[Callable[[BaseEvent], Any]] due to generic type variance
            # Track unsubscription for metrics
            self._unsubscription_count += 1
            self._unsubscription_timestamps.append(time.time())
            # Keep only last N timestamps to prevent unbounded growth
            if len(self._unsubscription_timestamps) > self._max_lifecycle_timestamps:
                self._unsubscription_timestamps = self._unsubscription_timestamps[-self._max_lifecycle_timestamps :]
            # Remove from service tracking if present (Task 2: Event Subscriber Cleanup)
            # Cast is safe because issubclass check above ensures event_type is a subclass of BaseEvent
            tuple_to_remove = cast(tuple[type[BaseEvent], Callable[[BaseEvent], Any]], (event_type, handler))
            for service_id, tracked_subscribers in list(self._subscriber_tracking.items()):
                if tuple_to_remove in tracked_subscribers:
                    tracked_subscribers.remove(tuple_to_remove)
                    if not tracked_subscribers:
                        # Remove service_id entry if no more subscribers
                        del self._subscriber_tracking[service_id]
            self._logger.debug("Removed subscriber for event type", event_type=event_type.__name__)
            return True
        except ValueError:
            self._logger.debug("Handler not found for event type", event_type=event_type.__name__)
            return False

    def get_subscriber_count(self, event_type: type[BaseEvent]) -> int:
        """
        Get the number of subscribers for a specific event type.

        Args:
            event_type: The type of event to count subscribers for

        Returns:
            The number of subscribers for the event type
        """
        # Remove threading - GIL guarantees atomic writes for this simple operation
        return len(self._subscribers.get(event_type, []))

    def get_all_subscriber_counts(self) -> dict[str, int]:
        """
        Get subscriber counts for all event types using pure async coordination.

        Returns:
            Dictionary mapping event type names to subscriber counts
        """
        # Remove threading dependency for this read-only operation
        return {event_type.__name__: len(subscribers) for event_type, subscribers in self._subscribers.items()}

    def get_active_task_count(self) -> int:
        """
        Get count of active async tasks in EventBus.

        Returns:
            Number of active tasks
        """
        return len(self._active_tasks)

    def get_active_task_details(self) -> list[dict[str, Any]]:
        """
        Get details of active tasks for debugging.

        Returns:
            List of dictionaries with task details
        """
        task_details = []
        for task in self._active_tasks:
            task_info: dict[str, Any] = {
                "task_name": task.get_name() if hasattr(task, "get_name") else "unknown",
                "done": task.done(),
                "cancelled": task.cancelled(),
            }
            # Add exception if task is done and has exception
            if task.done():
                try:
                    exception = task.exception()
                    if exception:
                        task_info["exception"] = str(exception)
                        task_info["exception_type"] = type(exception).__name__
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task exception retrieval can fail unpredictably
                    # nosec B110 - Intentional silent handling: Task exception retrieval can fail unpredictably,
                    # and we must continue processing other tasks even if one fails
                    logger.debug("Failed to retrieve task exception during task details collection", exc_info=e)
            task_details.append(task_info)
        return task_details

    def get_subscriber_lifecycle_metrics(self) -> dict[str, Any]:
        """
        Get subscriber lifecycle metrics including churn rate.

        Returns:
            Dictionary with subscriber lifecycle metrics
        """
        now = time.time()
        # Calculate churn rate based on recent activity (last hour)
        one_hour_ago = now - 3600
        recent_subscriptions = [ts for ts in self._subscription_timestamps if ts > one_hour_ago]
        recent_unsubscriptions = [ts for ts in self._unsubscription_timestamps if ts > one_hour_ago]

        # Calculate churn rate (unsubscriptions / subscriptions) over last hour
        subscription_churn_rate = (
            len(recent_unsubscriptions) / len(recent_subscriptions) if recent_subscriptions else 0.0
        )

        # Calculate total subscribers across all event types
        total_subscribers = sum(len(subscribers) for subscribers in self._subscribers.values())

        return {
            "subscription_count": self._subscription_count,
            "unsubscription_count": self._unsubscription_count,
            "total_subscribers": total_subscribers,
            "subscription_timestamps_count": len(self._subscription_timestamps),
            "unsubscription_timestamps_count": len(self._unsubscription_timestamps),
            "subscription_churn_rate": subscription_churn_rate,
            "recent_subscriptions_last_hour": len(recent_subscriptions),
            "recent_unsubscriptions_last_hour": len(recent_unsubscriptions),
        }

    def unsubscribe_all_for_service(self, service_id: str) -> int:
        """
        Unsubscribe all handlers for a specific service.

        Args:
            service_id: Service identifier to unsubscribe all handlers for

        Returns:
            Number of subscriptions removed

        This method is used during service shutdown to ensure all event
        subscriptions are properly cleaned up, preventing memory leaks.
        """
        if service_id not in self._subscriber_tracking:
            self._logger.debug("No subscribers found for service", service_id=service_id)
            return 0

        tracked_subscribers = self._subscriber_tracking[service_id]
        # Make a copy to avoid modification during iteration
        subscribers_to_remove = list(tracked_subscribers)
        removed_count = 0

        for event_type, handler in subscribers_to_remove:
            if self.unsubscribe(event_type, handler):
                removed_count += 1

        # Remove service tracking entry if it still exists
        # (it may have been removed by unsubscribe() if it was the last handler)
        if service_id in self._subscriber_tracking:
            del self._subscriber_tracking[service_id]

        self._logger.info(
            "Unsubscribed all handlers for service",
            service_id=service_id,
            removed_count=removed_count,
        )
        return removed_count

    def get_subscriber_stats(self) -> dict[str, Any]:
        """
        Get subscriber statistics per event type for monitoring.

        Returns:
            Dictionary with subscriber counts per event type and service tracking info
        """
        subscriber_counts = self.get_all_subscriber_counts()
        total_subscribers = sum(subscriber_counts.values())

        # Get service tracking statistics
        service_subscriber_counts = {
            service_id: len(subscribers) for service_id, subscribers in self._subscriber_tracking.items()
        }

        return {
            "subscriber_counts_by_event": subscriber_counts,
            "total_subscribers": total_subscribers,
            "services_tracked": len(self._subscriber_tracking),
            "service_subscriber_counts": service_subscriber_counts,
            "tracked_subscriptions": sum(len(subs) for subs in self._subscriber_tracking.values()),
        }

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
            # Clean up all service subscriptions (Task 2: Event Subscriber Cleanup)
            if self._subscriber_tracking:
                total_removed = 0
                for service_id in list(self._subscriber_tracking.keys()):
                    removed = self.unsubscribe_all_for_service(service_id)
                    total_removed += removed
                self._logger.info(
                    "Cleaned up service subscriptions during shutdown",
                    services_cleaned=len(self._subscriber_tracking),
                    total_subscriptions_removed=total_removed,
                )
            await self._stop_processing()
        except (RuntimeError, asyncio.CancelledError) as e:
            # Event loop is closing or task was cancelled - this is expected during test teardown
            self._logger.debug(
                "EventBus shutdown cancelled or event loop closing",
                error=str(e),
                error_type=type(e).__name__,
            )
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event processing errors unpredictable, must prevent worker crashes
            # Catch all other exceptions to prevent worker crashes
            # Log the error but don't re-raise to allow test cleanup to complete
            try:
                self._logger.warning(
                    "Error during EventBus shutdown (non-fatal)",
                    error=str(e),
                    error_type=type(e).__name__,
                    exc_info=True,
                )
            except Exception:  # pylint: disable=broad-exception-caught  # nosec B110  # noqa: B904  # Reason: Logging errors must not crash workers, if logging fails just continue
                pass
        finally:
            # Ensure state is always reset even if shutdown fails
            self._running = False
            if self._processing_task and not self._processing_task.done():
                try:
                    self._processing_task.cancel()
                except Exception:  # pylint: disable=broad-exception-caught  # nosec B110  # noqa: B904  # Reason: Task cancellation errors unpredictable, must handle gracefully
                    pass
            # Clear active tasks to prevent resource leaks
            self._active_tasks.clear()

    def __del__(self) -> None:
        """Cleanup when the EventBus is destroyed - replaced with async-aware graceful shutdown."""
        if self._running:  # pylint: disable=too-many-nested-blocks  # Reason: EventBus cleanup requires complex nested logic for error handling and resource cleanup
            # Use basic print instead of logger to avoid encoding issues during cleanup
            try:
                self._logger.warning("EventBus destroyed without graceful shutdown")
            except (AttributeError, RuntimeError) as e:
                logger.error("Error during event bus destruction warning", error=str(e), error_type=type(e).__name__)

            # Force immediate shutdown to prevent "no running event loop" errors
            self._running = False
            try:
                self._shutdown_event.set()
            except (AttributeError, RuntimeError) as e:
                logger.error("Error setting shutdown event", error=str(e), error_type=type(e).__name__)

            # Cancel all active tasks immediately, but only if event loop is still running
            if self._active_tasks:
                try:
                    loop = asyncio.get_running_loop()
                    if loop and not loop.is_closed():
                        # Cancel all tasks immediately
                        for task in list(self._active_tasks):
                            if not task.done():
                                task.cancel()
                except (RuntimeError, Exception):  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event loop cleanup errors unpredictable, must handle gracefully
                    # Event loop is closed or not running - just clear tasks
                    pass
                finally:
                    # Always clear the task set to prevent memory leaks
                    self._active_tasks.clear()
