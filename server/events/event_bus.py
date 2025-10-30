"""
Event bus for MythosMUD.

This module provides the EventBus class that implements an in-memory
pub/sub system for handling game events. The system is designed to be
asynchronous and non-blocking, with support for multiple subscribers
per event type.

Implemented using pure asyncio patterns to banish the hybrid threading
patterns that threatened the computational sanity of our eldritch
architecture. Based on warnings from the Pnakotic Manuscripts about
proper event propagation across dimensional boundaries.

As noted in the Pnakotic Manuscripts, proper event propagation is
essential for maintaining awareness of the dimensional shifts that
occur throughout our eldritch architecture.
"""

import asyncio
from collections import defaultdict
from collections.abc import Callable
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from .event_types import BaseEvent

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
                    self._logger.info("EventBus pure async processing started on-demand")
            except RuntimeError:
                # No running loop available - processing will start when first event published
                self._logger.debug("EventBus will start processing on first publish when event loop available")

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
                    # Pure asyncio await replaces threading/get(timeout) - Task 1.2
                    event = await asyncio.wait_for(self._event_queue.get(), timeout=1.0)

                    # Check for sentinel shutdown signal
                    if event is None:
                        break

                    # Process the event with proper async handling
                    await self._handle_event_async(event)

                except TimeoutError:
                    # Timeout is expected when no events are available
                    continue
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
        """Handle a single event by calling all registered subscribers with pure async coordination."""
        event_type = type(event)
        subscribers = self._subscribers.get(event_type, [])

        if not subscribers:
            self._logger.debug("No subscribers for event type", event_type=event_type.__name__)
            return

        self._logger.debug(
            "Processing event for subscribers", event_type=event_type.__name__, subscriber_count=len(subscribers)
        )

        import inspect

        # Process subscribers with proper async handling and task lifecycle management - Task 1.5
        for subscriber in subscribers:
            try:
                # Check if subscriber is async
                if inspect.iscoroutinefunction(subscriber):
                    # Create and track task properly for cancellation - Task 1.5: Task References
                    task = asyncio.create_task(subscriber(event))
                    self._active_tasks.add(task)

                    # Remove from active tasks when complete
                    def remove_task(t: asyncio.Task) -> None:
                        self._active_tasks.discard(t)

                    task.add_done_callback(remove_task)
                    # Handle task completion with proper exception handling
                    subscriber_name = subscriber.__name__
                    task.add_done_callback(lambda t, sn=subscriber_name: self._handle_task_result_async(t, sn))

                    self._logger.debug("Created tracked task for async subscriber", subscriber_name=subscriber.__name__)
                else:
                    # Call sync subscriber directly without threading hybrid antipattern
                    subscriber(event)
            except Exception as e:
                self._logger.error("Error in event subscriber", subscriber_name=subscriber.__name__, error=str(e))

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
            self._logger.debug("Published event", event_type=type(event).__name__)
        except asyncio.QueueFull as exc:
            # Rare case where queue is at capacity - indicates very high load
            self._logger.warning("Event queue at capacity - dropping event", event_type=type(event).__name__)
            raise RuntimeError("Event bus overloaded") from exc

    def subscribe(self, event_type: type[BaseEvent], handler: Callable[[BaseEvent], Any]) -> None:
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
        self._subscribers[event_type].append(handler)
        self._logger.debug("Added subscriber for event type", event_type=event_type.__name__)

    def unsubscribe(self, event_type: type[BaseEvent], handler: Callable[[BaseEvent], Any]) -> bool:
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
            subscribers.remove(handler)
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
