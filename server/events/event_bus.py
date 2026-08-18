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

# pyright: reportUnnecessaryIsInstance=false, reportUnreachable=false
# Reason: subscribe retains runtime guards for invalid dynamic/cast inputs (see unit tests).

import asyncio
import time
from collections import defaultdict
from collections.abc import Callable
from typing import TypedDict, TypeVar, cast, override

from anyio import Event
from structlog.stdlib import BoundLogger

from ..structured_logging.enhanced_logging_config import get_logger
from .event_bus_lifecycle import EventBusLifecycleMixin
from .event_bus_processing import EventBusProcessingMixin
from .event_types import BaseEvent

T = TypeVar("T", bound=BaseEvent)

logger = get_logger(__name__)


class SubscriberStats(TypedDict):
    """Subscriber counts returned by get_subscriber_stats()."""

    subscriber_counts_by_event: dict[str, int]
    total_subscribers: int
    services_tracked: int
    service_subscriber_counts: dict[str, int]
    tracked_subscriptions: int


class SubscriberLifecycleMetrics(TypedDict):
    """Lifecycle metrics returned by get_subscriber_lifecycle_metrics()."""

    subscription_count: int
    unsubscription_count: int
    total_subscribers: int
    subscription_timestamps_count: int
    unsubscription_timestamps_count: int
    subscription_churn_rate: float
    recent_subscriptions_last_hour: int
    recent_unsubscriptions_last_hour: int


class EventBus(EventBusProcessingMixin, EventBusLifecycleMixin):  # pylint: disable=too-many-instance-attributes  # Reason: Event bus requires multiple subscription maps and state tracking
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
        self._subscribers: dict[type[BaseEvent], list[Callable[[BaseEvent], object]]] = defaultdict(list)
        # Pure asyncio.Queue replaces threading.Queue - Task 1.2: Replace queue
        self._event_queue: asyncio.Queue[BaseEvent | None] = asyncio.Queue()
        self._running: bool = False
        self._logger: BoundLogger = get_logger("EventBus")
        # Task references for proper lifecycle management - Task 1.5
        self._active_tasks: set[asyncio.Task[object]] = set()
        self._shutdown_event: Event = Event()
        self._main_loop: asyncio.AbstractEventLoop | None = None
        # Fix: Initialize on-demand rather than during __init__
        self._processing_task: asyncio.Task[object] | None = None
        # Subscriber lifecycle tracking for metrics
        self._subscription_timestamps: list[float] = []
        self._unsubscription_timestamps: list[float] = []
        self._subscription_count: int = 0
        self._unsubscription_count: int = 0
        # Keep only last 1000 timestamps to prevent unbounded growth
        self._max_lifecycle_timestamps: int = 1000
        # Subscriber tracking by service identifier for cleanup (Task 2: Event Subscriber Cleanup)
        # Maps service_id -> list of (event_type, handler) tuples
        self._subscriber_tracking: dict[str, list[tuple[type[BaseEvent], Callable[[BaseEvent], object]]]] = {}

    def set_main_loop(self, loop: asyncio.AbstractEventLoop) -> None:
        """Set the main event loop - now properly managed for async compatibility."""
        self._main_loop = loop
        self._logger.info("Main event loop set for EventBus")

    def _ensure_processing_started(self) -> None:
        """Legacy wrapper for API compatibility during transition."""
        self._ensure_async_processing()

    def subscribe(  # noqa: UP047
        self,
        event_type: type[T],
        handler: Callable[[T], object],
        service_id: str | None = None,
    ) -> None:
        """
        Subscribe ``handler`` to ``event_type``. Pass ``service_id`` for shutdown cleanup.

        Args:
            event_type: Event class to subscribe to (must subclass BaseEvent)
            handler: Called with each published event of that type
            service_id: Optional id for ``unsubscribe_all_for_service``
        """
        if not issubclass(event_type, BaseEvent):
            raise ValueError("Event type must inherit from BaseEvent")

        if not callable(handler):
            raise ValueError("Handler must be callable")

        # Remove threading dependency - Python dict operations are atomic at GIL
        # level for simple operations like this, sufficient for single-threaded async
        stored = cast(Callable[[BaseEvent], object], handler)
        self._subscribers[event_type].append(stored)
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
            self._subscriber_tracking[service_id].append((event_type, stored))
        self._logger.debug("Added subscriber for event type", event_type=event_type.__name__, service_id=service_id)

    def unsubscribe(self, event_type: type[T], handler: Callable[[T], object]) -> bool:  # noqa: UP047
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
        stored = cast(Callable[[BaseEvent], object], handler)
        try:
            subscribers.remove(stored)
            # Track unsubscription for metrics
            self._unsubscription_count += 1
            self._unsubscription_timestamps.append(time.time())
            # Keep only last N timestamps to prevent unbounded growth
            if len(self._unsubscription_timestamps) > self._max_lifecycle_timestamps:
                self._unsubscription_timestamps = self._unsubscription_timestamps[-self._max_lifecycle_timestamps :]
            # Remove from service tracking if present (Task 2: Event Subscriber Cleanup)
            tuple_to_remove = (event_type, stored)
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

    def get_queue_depth(self) -> int:
        """Return the number of events waiting for the sole async consumer."""
        return self._event_queue.qsize()

    def get_active_task_details(self) -> list[dict[str, object]]:
        """
        Get details of active tasks for debugging.

        Returns:
            List of dictionaries with task details
        """
        task_details: list[dict[str, object]] = []
        for task in self._active_tasks:
            task_info: dict[str, object] = {
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

    def get_subscriber_lifecycle_metrics(self) -> SubscriberLifecycleMetrics:
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

    @override
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

    def get_subscriber_stats(self) -> SubscriberStats:
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
