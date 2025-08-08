"""
Event bus for MythosMUD.

This module provides the EventBus class that implements an in-memory
pub/sub system for handling game events. The system is designed to be
asynchronous and non-blocking, with support for multiple subscribers
per event type.

As noted in the Pnakotic Manuscripts, proper event propagation is
essential for maintaining awareness of the dimensional shifts that
occur throughout our eldritch architecture.
"""

import asyncio
import queue
import threading
from collections import defaultdict
from collections.abc import Callable
from queue import Queue

from ..logging_config import get_logger
from .event_types import BaseEvent


class EventBus:
    """
    In-memory event bus for MythosMUD.

    This class provides a thread-safe pub/sub system for handling
    game events. Events are processed asynchronously to avoid
    blocking the main game loop.

    The EventBus maintains subscriptions by event type and processes
    events in a background thread to ensure non-blocking operation.
    """

    def __init__(self):
        """Initialize the event bus with empty subscriptions and processing queue."""
        self._subscribers: dict[type[BaseEvent], list[Callable]] = defaultdict(list)
        self._event_queue: Queue = Queue()
        self._processing_thread: threading.Thread | None = None
        self._running: bool = False
        self._lock = threading.RLock()
        self._logger = get_logger("EventBus")
        self._main_loop: asyncio.AbstractEventLoop | None = None

        # Start the event processing thread
        self._start_processing()

    def set_main_loop(self, loop: asyncio.AbstractEventLoop):
        """Set the main event loop for async event handling."""
        self._main_loop = loop
        self._logger.info("Main event loop set for EventBus")

    def _start_processing(self):
        """Start the background event processing thread."""
        with self._lock:
            if not self._running:
                self._running = True
                self._processing_thread = threading.Thread(
                    target=self._process_events, daemon=True, name="EventBus-Processor"
                )
                self._processing_thread.start()
                self._logger.info("EventBus processing thread started")

    def _stop_processing(self):
        """Stop the background event processing thread."""
        with self._lock:
            if self._running:
                self._running = False
                # Add a sentinel event to wake up the processing thread
                self._event_queue.put(None)
                if self._processing_thread:
                    self._processing_thread.join(timeout=5.0)
                self._logger.info("EventBus processing thread stopped")

    def _process_events(self):
        """Background thread that processes events from the queue."""
        self._logger.info("EventBus processing thread started")

        while self._running:
            try:
                # Get event from queue with timeout
                event = self._event_queue.get(timeout=1.0)

                # Check for sentinel value
                if event is None:
                    break

                # Process the event
                self._handle_event(event)

            except queue.Empty:
                # Timeout is expected when no events are available
                continue
            except Exception as e:
                self._logger.error(f"Error processing event: {e}", exc_info=True)
                continue

        self._logger.info("EventBus processing thread stopped")

    def _handle_event(self, event: BaseEvent):
        """Handle a single event by calling all registered subscribers."""
        event_type = type(event)
        subscribers = self._subscribers.get(event_type, [])

        if not subscribers:
            self._logger.debug(f"No subscribers for event type: {event_type.__name__}")
            return

        self._logger.debug(f"Processing {event_type.__name__} event for {len(subscribers)} subscribers")

        for subscriber in subscribers:
            try:
                import inspect

                # Check if subscriber is async
                if inspect.iscoroutinefunction(subscriber):
                    # Handle async subscriber
                    self._handle_async_subscriber(subscriber, event)
                else:
                    # Call sync subscriber directly
                    subscriber(event)
            except Exception as e:
                self._logger.error(f"Error in event subscriber {subscriber.__name__}: {e}")

    def _handle_async_subscriber(self, subscriber: Callable, event: BaseEvent):
        """Handle async event subscribers properly."""
        try:
            # Try to get the main event loop
            if self._main_loop and self._main_loop.is_running():
                # Use the main loop to schedule the coroutine
                asyncio.run_coroutine_threadsafe(subscriber(event), self._main_loop)
                # We don't wait for the result to avoid blocking
                self._logger.debug(f"Scheduled async subscriber {subscriber.__name__} in main loop")
            else:
                # Fallback: try to get the current running loop
                try:
                    asyncio.create_task(subscriber(event))
                    self._logger.debug(f"Created task for async subscriber {subscriber.__name__}")
                except RuntimeError:
                    # No running loop, log warning and skip
                    self._logger.warning(f"No event loop available for async subscriber {subscriber.__name__}")
        except Exception as e:
            self._logger.error(f"Error handling async subscriber {subscriber.__name__}: {e}")

    def publish(self, event: BaseEvent) -> None:
        """
        Publish an event to the event bus.

        Args:
            event: The event to publish

        The event will be processed asynchronously by the background
        processing thread to avoid blocking the caller.
        """
        if not isinstance(event, BaseEvent):
            raise ValueError("Event must inherit from BaseEvent")

        self._event_queue.put(event)
        self._logger.debug(f"Published {type(event).__name__} event")

    def subscribe(self, event_type: type[BaseEvent], handler: Callable[[BaseEvent], None]) -> None:
        """
        Subscribe to events of a specific type.

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

        with self._lock:
            self._subscribers[event_type].append(handler)
            self._logger.debug(f"Added subscriber for {event_type.__name__}")

    def unsubscribe(self, event_type: type[BaseEvent], handler: Callable[[BaseEvent], None]) -> bool:
        """
        Unsubscribe from events of a specific type.

        Args:
            event_type: The type of event to unsubscribe from
            handler: The function to remove from the subscription list

        Returns:
            True if the handler was found and removed, False otherwise
        """
        if not issubclass(event_type, BaseEvent):
            raise ValueError("Event type must inherit from BaseEvent")

        with self._lock:
            subscribers = self._subscribers.get(event_type, [])
            try:
                subscribers.remove(handler)
                self._logger.debug(f"Removed subscriber for {event_type.__name__}")
                return True
            except ValueError:
                self._logger.debug(f"Handler not found for {event_type.__name__}")
                return False

    def get_subscriber_count(self, event_type: type[BaseEvent]) -> int:
        """
        Get the number of subscribers for a specific event type.

        Args:
            event_type: The type of event to count subscribers for

        Returns:
            The number of subscribers for the event type
        """
        with self._lock:
            return len(self._subscribers.get(event_type, []))

    def get_all_subscriber_counts(self) -> dict[str, int]:
        """
        Get subscriber counts for all event types.

        Returns:
            Dictionary mapping event type names to subscriber counts
        """
        with self._lock:
            return {event_type.__name__: len(subscribers) for event_type, subscribers in self._subscribers.items()}

    def shutdown(self):
        """Shutdown the event bus and stop the processing thread."""
        self._logger.info("Shutting down EventBus")
        self._stop_processing()

    def __del__(self):
        """Cleanup when the EventBus is destroyed."""
        self.shutdown()
