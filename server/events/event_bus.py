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

import asyncio
from collections import defaultdict
from collections.abc import Callable
from typing import Any, TypeVar

from ..logging.enhanced_logging_config import get_logger
from .event_types import BaseEvent

# Type variable for generic event handling
T = TypeVar("T", bound=BaseEvent)

logger = get_logger(__name__)


class EventBus:
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
        self._event_queue: asyncio.Queue = asyncio.Queue()
        self._running: bool = False
        self._logger = get_logger("EventBus")
        # Task references for proper lifecycle management - Task 1.5
        self._active_tasks: set[asyncio.Task] = set()
        self._shutdown_event: asyncio.Event = asyncio.Event()
        self._main_loop: asyncio.AbstractEventLoop | None = None
        # Fix: Initialize on-demand rather than during __init__
        self._processing_task: asyncio.Task | None = None

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
                    self._processing_task.add_done_callback(lambda task: self._active_tasks.discard(task))
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
            except Exception as e:
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

    async def _stop_processing(self) -> None:
        """Stop pure async event processing gracefully."""
        if self._running:
            self._running = False
            # Signal shutdown to async processing loop - Task 1.3
            self._shutdown_event.set()

            # Put sentinel in queue to wake up processing task immediately
            # This ensures the task waiting on asyncio.wait_for() wakes up right away
            try:
                self._event_queue.put_nowait(None)  # Sentinel to wake up waiting task
            except asyncio.QueueFull:
                # Queue is full, but that's okay - task will wake up on timeout or cancellation
                pass

            # Cancel processing task explicitly if it exists
            if self._processing_task and not self._processing_task.done():
                self._processing_task.cancel()
                try:
                    await self._processing_task
                except asyncio.CancelledError:
                    pass

            # Cancel all active tasks and wait for graceful shutdown
            if self._active_tasks:
                for task in list(self._active_tasks):
                    if not task.done():
                        task.cancel()

                # Wait for tasks to complete with timeout - use a more robust approach
                try:
                    # Use asyncio.wait instead of gather to avoid hanging on unresponsive tasks
                    done, pending = await asyncio.wait(
                        self._active_tasks, timeout=1.0, return_when=asyncio.ALL_COMPLETED
                    )

                    # Force cancel any remaining pending tasks
                    if pending:
                        for task in pending:
                            if not task.done():
                                task.cancel()

                        # Give them a brief moment to cancel, then abandon
                        try:
                            await asyncio.wait_for(asyncio.gather(*pending, return_exceptions=True), timeout=0.5)
                        except (TimeoutError, Exception):
                            pass  # Abandon remaining tasks

                except (RuntimeError, asyncio.CancelledError) as e:
                    logger.error("Error during event bus shutdown", error=str(e), error_type=type(e).__name__)
                    # Any error in shutdown - just clear the tasks
                    pass

            self._logger.info("EventBus pure async processing stopped")

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
                except Exception as e:
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

        except Exception as e:
            # Use basic print to avoid Unicode encoding issues during cleanup
            try:
                self._logger.error("Fatal error in async event processing", error=str(e), exc_info=True)
            except (UnicodeEncodeError, AttributeError) as e2:
                logger.error("Error logging fatal event processing error", error=str(e2), error_type=type(e2).__name__)
                self._logger.critical("Fatal error in async event processing", error=str(e), exc_info=True)
        finally:
            self._logger.info("EventBus pure async processing stopped")

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

        import inspect

        # Separate async and sync subscribers
        async_subscribers: list[Callable[[BaseEvent], Any]] = []
        sync_subscribers: list[Callable[[BaseEvent], Any]] = []

        for subscriber in subscribers:
            if inspect.iscoroutinefunction(subscriber):
                async_subscribers.append(subscriber)
            else:
                sync_subscribers.append(subscriber)

        # Process sync subscribers first (they're blocking but quick)
        for subscriber in sync_subscribers:
            try:
                subscriber(event)
            except Exception as e:
                subscriber_name = getattr(subscriber, "__name__", "unknown")
                self._logger.error("Error in sync event subscriber", subscriber_name=subscriber_name, error=str(e))

        # Process async subscribers with structured concurrency
        # Use asyncio.gather with return_exceptions=True to ensure all subscribers run
        # even if individual ones fail (appropriate for event subscribers)
        if async_subscribers:
            # Create all subscriber tasks first
            tasks: list[asyncio.Task] = []
            subscriber_names: dict[asyncio.Task, str] = {}

            for subscriber in async_subscribers:
                subscriber_name = getattr(subscriber, "__name__", "unknown")
                try:
                    # Create task and track it
                    task = asyncio.create_task(subscriber(event))
                    tasks.append(task)
                    subscriber_names[task] = subscriber_name
                    self._active_tasks.add(task)

                    # Remove from active tasks when complete
                    def remove_task(t: asyncio.Task, sn: str = subscriber_name) -> None:
                        self._active_tasks.discard(t)

                    task.add_done_callback(remove_task)
                    self._logger.debug("Created tracked task for async subscriber", subscriber_name=subscriber_name)
                except Exception as e:
                    # If task creation fails, log but continue with other subscribers
                    self._logger.error(
                        "Failed to create task for subscriber", subscriber_name=subscriber_name, error=str(e)
                    )

            # Wait for all tasks with structured concurrency pattern
            # return_exceptions=True ensures all tasks complete even if some fail
            if tasks:
                try:
                    results = await asyncio.gather(*tasks, return_exceptions=True)
                    # Log any exceptions from subscribers
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
                except Exception as e:
                    # This should not happen with return_exceptions=True, but handle defensively
                    self._logger.error(
                        "Unexpected error in subscriber task group", error=str(e), error_type=type(e).__name__
                    )

    def _handle_task_result_async(self, task: asyncio.Task, subscriber_name: str) -> None:
        """Handle async task completion with proper exception extraction."""
        try:
            # Get the result to handle exceptions without threading/runtime scheduler crossing
            task.result()
        except Exception as e:
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

    def subscribe(self, event_type: type[T], handler: Callable[[T], Any]) -> None:
        """
        Subscribe to events of a specific type with pure async thread-safe patterns.

        Args:
            event_type: The type of event to subscribe to
            handler: The function to call when events of this type are published

        The handler function will be called with the event object as its
        argument when events of the specified type are published.
        """
        if not issubclass(event_type, BaseEvent):
            raise ValueError("Event type must inherit from BaseEvent")

        if not callable(handler):
            raise ValueError("Handler must be callable")

        # Remove threading dependency - Python dict operations are atomic at GIL
        # level for simple operations like this, sufficient for single-threaded async
        self._subscribers[event_type].append(handler)  # type: ignore[arg-type]
        self._logger.debug("Added subscriber for event type", event_type=event_type.__name__)

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
            subscribers.remove(handler)  # type: ignore[arg-type]
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

    async def shutdown(self) -> None:
        """Shutdown the pure asyncio event bus with proper grace s period coordination."""
        self._logger.info("Shutting down pure asyncio EventBus")
        await self._stop_processing()

    def __del__(self) -> None:
        """Cleanup when the EventBus is destroyed - replaced with async-aware graceful shutdown."""
        if self._running:
            # Use basic print instead of logger to avoid encoding issues during cleanup
            try:
                self._logger.warning("EventBus destroyed without graceful shutdown")
            except (AttributeError, RuntimeError) as e:
                logger.error("Error during event bus destruction warning", error=str(e), error_type=type(e).__name__)
                pass

            # Force immediate shutdown to prevent "no running event loop" errors
            self._running = False
            try:
                self._shutdown_event.set()
            except (AttributeError, RuntimeError) as e:
                logger.error("Error setting shutdown event", error=str(e), error_type=type(e).__name__)
                pass

            # Cancel all active tasks immediately, but only if event loop is still running
            if self._active_tasks:
                try:
                    loop = asyncio.get_running_loop()
                    if loop and not loop.is_closed():
                        # Cancel all tasks immediately
                        for task in list(self._active_tasks):
                            if not task.done():
                                task.cancel()
                except (RuntimeError, Exception):
                    # Event loop is closed or not running - just clear tasks
                    pass
                finally:
                    # Always clear the task set to prevent memory leaks
                    self._active_tasks.clear()
