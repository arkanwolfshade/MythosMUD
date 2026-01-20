"""
Memory leak metrics collector for MythosMUD.

This module provides comprehensive metrics collection for memory leak detection,
aggregating metrics from all sources including connections, events, caches, tasks, and NATS.

As noted in the Pnakotic Manuscripts, proper monitoring of our eldritch architecture
is essential for detecting dimensional drift and preventing resource leaks.
"""

import time
from collections import deque
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MemoryLeakMetricsCollector:
    """
    Unified metrics collector for memory leak detection.

    Aggregates metrics from all sources and provides trend tracking,
    growth rate calculation, and alerting threshold checking.
    """

    def __init__(self) -> None:
        """Initialize the memory leak metrics collector."""
        # Track metrics history (last 100 measurements)
        self._history: deque[dict[str, Any]] = deque(maxlen=100)

        # Alert thresholds
        self._alert_thresholds = {
            "closed_websockets_max": 5000,
            "subscriber_growth_rate": 0.1,  # 10% growth per period
            "cache_size_limit_factor": 1.1,  # 110% of max_size
            "task_growth_rate": 0.2,  # 20% growth per period
        }

        logger.info("MemoryLeakMetricsCollector initialized")

    def collect_all_metrics(self) -> dict[str, Any]:
        """
        Collect all metrics from all sources.

        Returns:
            Dictionary containing aggregated metrics from all sources
        """
        try:
            metrics: dict[str, Any] = {
                "connection": self.collect_connection_metrics(),
                "event": self.collect_event_metrics(),
                "cache": self.collect_cache_metrics(),
                "task": self.collect_task_metrics(),
                "nats": self.collect_nats_metrics(),
            }

            # Add timestamp
            metrics["timestamp"] = time.time()

            # Store in history
            self._history.append(metrics)

            return metrics
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Metrics collection errors unpredictable, must return partial metrics
            logger.error("Error collecting all metrics", error=str(e), exc_info=True)
            return {"error": str(e), "timestamp": time.time()}

    def collect_connection_metrics(self) -> dict[str, Any]:
        """
        Collect connection metrics from ConnectionManager.

        Returns:
            Dictionary with connection metrics
        """
        try:
            from ..realtime.connection_manager import resolve_connection_manager

            connection_manager = resolve_connection_manager(None)
            if not connection_manager:
                return {"error": "ConnectionManager not available"}

            memory_stats = connection_manager.get_memory_stats()
            connections = memory_stats.get("connections", {})

            return {
                "active_websockets_count": connections.get("active_websockets_count", 0),
                "connection_metadata_count": connections.get("connection_metadata_count", 0),
                "player_websockets_count": connections.get("player_websockets_count", 0),
                "closed_websockets_count": connections.get("closed_websockets_count", 0),
                "active_to_player_ratio": connections.get("active_to_player_ratio", 0.0),
                "orphaned_connections": connections.get("orphaned_connections", 0),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Connection metrics errors unpredictable, must return error
            logger.error("Error collecting connection metrics", error=str(e))
            return {"error": str(e)}

    def collect_event_metrics(self) -> dict[str, Any]:
        """
        Collect event metrics from EventBus.

        Returns:
            Dictionary with event metrics
        """
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            if not container or not hasattr(container, "event_bus") or not container.event_bus:
                return {"error": "EventBus not available"}

            event_bus = container.event_bus
            subscriber_counts = event_bus.get_all_subscriber_counts()
            lifecycle_metrics = event_bus.get_subscriber_lifecycle_metrics()
            subscriber_stats = event_bus.get_subscriber_stats()  # Task 2: Event Subscriber Cleanup

            return {
                "subscriber_counts_by_type": subscriber_counts,
                "total_subscribers": lifecycle_metrics["total_subscribers"],
                "active_task_count": event_bus.get_active_task_count(),
                "subscription_churn_rate": lifecycle_metrics["subscription_churn_rate"],
                "services_tracked": subscriber_stats.get("services_tracked", 0),
                "tracked_subscriptions": subscriber_stats.get("tracked_subscriptions", 0),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event metrics errors unpredictable, must return error
            logger.error("Error collecting event metrics", error=str(e))
            return {"error": str(e)}

    def collect_cache_metrics(self) -> dict[str, Any]:
        """
        Collect cache metrics from CacheManager.

        Returns:
            Dictionary with cache metrics
        """
        try:
            from ..caching.lru_cache import get_cache_manager

            cache_manager = get_cache_manager()
            all_stats = cache_manager.get_all_stats()

            # Aggregate metrics
            cache_sizes = {name: stats.get("size", 0) for name, stats in all_stats.items()}
            capacity_utilization = {name: stats.get("capacity_utilization", 0.0) for name, stats in all_stats.items()}
            expired_counts = {name: stats.get("expired_count", 0) for name, stats in all_stats.items()}

            return {
                "cache_sizes": cache_sizes,
                "capacity_utilization": capacity_utilization,
                "expired_entry_counts": expired_counts,
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cache metrics errors unpredictable, must return error
            logger.error("Error collecting cache metrics", error=str(e))
            return {"error": str(e)}

    def collect_task_metrics(self) -> dict[str, Any]:
        """
        Collect task metrics from TaskRegistry.

        Returns:
            Dictionary with task metrics
        """
        try:
            from ..app.task_registry import get_registry

            task_registry = get_registry()
            lifecycle_metrics = task_registry.get_task_lifecycle_metrics()

            return {
                "active_task_count": lifecycle_metrics["active_task_count"],
                "tasks_by_type": lifecycle_metrics["tasks_by_type"],
                "task_creation_rate": lifecycle_metrics["task_creation_rate"],
                "task_completion_rate": lifecycle_metrics["task_completion_rate"],
                "orphaned_task_count": lifecycle_metrics["orphaned_task_count"],
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task metrics errors unpredictable, must return error
            logger.error("Error collecting task metrics", error=str(e))
            return {"error": str(e)}

    def collect_nats_metrics(self) -> dict[str, Any]:
        """
        Collect NATS subscription metrics from NATSService.

        Returns:
            Dictionary with NATS metrics
        """
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            if not container or not hasattr(container, "nats_service") or not container.nats_service:
                return {"error": "NATSService not available"}

            nats_service = container.nats_service
            active_subscriptions = nats_service.get_active_subscriptions()

            return {
                "active_subscriptions": active_subscriptions,
                "subscription_count": len(active_subscriptions),
                "last_cleanup_time": getattr(nats_service, "_last_cleanup_time", None),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NATS metrics errors unpredictable, must return error
            logger.error("Error collecting NATS metrics", error=str(e))
            return {"error": str(e)}

    def _calculate_single_growth_rate(
        self, current: dict[str, Any], previous: dict[str, Any], category: str, metric_key: str
    ) -> float | None:
        """
        Calculate growth rate for a single metric.

        Args:
            current: Current metrics dictionary
            previous: Previous metrics dictionary
            category: Category key (e.g., "connection", "event", "task")
            metric_key: Metric key within the category

        Returns:
            Growth rate as float, or None if calculation not possible
        """
        if category not in current or category not in previous:
            return None

        category_current = current[category]
        category_previous = previous[category]

        if metric_key not in category_current or metric_key not in category_previous:
            return None

        prev_count = category_previous.get(metric_key, 0)
        curr_count = category_current.get(metric_key, 0)

        if prev_count > 0:
            return (curr_count - prev_count) / prev_count
        return float("inf") if curr_count > 0 else 0.0

    def calculate_growth_rates(self) -> dict[str, float]:
        """
        Calculate growth rates for metrics over time.

        Returns:
            Dictionary mapping metric names to growth rates
        """
        if len(self._history) < 2:
            return {}

        try:
            current = self._history[-1]
            previous = self._history[-2]

            growth_rates: dict[str, float] = {}

            # Calculate connection growth rates
            closed_ws_rate = self._calculate_single_growth_rate(
                current, previous, "connection", "closed_websockets_count"
            )
            if closed_ws_rate is not None:
                growth_rates["closed_websockets"] = closed_ws_rate

            # Calculate subscriber growth rates
            subscriber_rate = self._calculate_single_growth_rate(current, previous, "event", "total_subscribers")
            if subscriber_rate is not None:
                growth_rates["subscribers"] = subscriber_rate

            # Calculate task growth rates
            task_rate = self._calculate_single_growth_rate(current, previous, "task", "active_task_count")
            if task_rate is not None:
                growth_rates["tasks"] = task_rate

            return growth_rates
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Growth rate calculation errors unpredictable, must return empty dict
            logger.error("Error calculating growth rates", error=str(e))
            return {}

    def _check_connection_alerts(self, metrics: dict[str, Any], alerts: list[str]) -> None:
        """Check connection-related alerts and append to alerts list."""
        if "connection" not in metrics:
            return

        conn_metrics = metrics["connection"]
        closed_count = conn_metrics.get("closed_websockets_count", 0)
        if closed_count > self._alert_thresholds["closed_websockets_max"]:
            alerts.append(
                f"WARNING: Closed websockets count ({closed_count}) exceeds threshold "
                f"({self._alert_thresholds['closed_websockets_max']})"
            )

    def _check_subscriber_alerts(self, growth_rates: dict[str, float], alerts: list[str]) -> None:
        """Check subscriber growth rate alerts and append to alerts list."""
        if "subscribers" not in growth_rates:
            return

        growth_rate = growth_rates["subscribers"]
        if growth_rate > self._alert_thresholds["subscriber_growth_rate"]:
            alerts.append(
                f"WARNING: Subscriber growth rate ({growth_rate:.2%}) exceeds threshold "
                f"({self._alert_thresholds['subscriber_growth_rate']:.2%})"
            )

    def _check_cache_alerts(self, metrics: dict[str, Any], alerts: list[str]) -> None:
        """Check cache-related alerts and append to alerts list."""
        if "cache" not in metrics:
            return

        cache_metrics = metrics["cache"]
        capacity_utilization = cache_metrics.get("capacity_utilization", {})
        for cache_name, utilization in capacity_utilization.items():
            if utilization > self._alert_thresholds["cache_size_limit_factor"]:
                alerts.append(
                    f"WARNING: Cache '{cache_name}' capacity utilization ({utilization:.2%}) exceeds threshold "
                    f"({self._alert_thresholds['cache_size_limit_factor']:.2%})"
                )

    def _check_task_alerts(self, growth_rates: dict[str, float], alerts: list[str]) -> None:
        """Check task growth rate alerts and append to alerts list."""
        if "tasks" not in growth_rates:
            return

        growth_rate = growth_rates["tasks"]
        if growth_rate > self._alert_thresholds["task_growth_rate"]:
            alerts.append(
                f"WARNING: Task growth rate ({growth_rate:.2%}) exceeds threshold "
                f"({self._alert_thresholds['task_growth_rate']:.2%})"
            )

    def check_alerts(self, metrics: dict[str, Any] | None = None) -> list[str]:
        """
        Check metrics against alert thresholds and return list of alerts.

        Args:
            metrics: Optional metrics dictionary (if None, uses current metrics)

        Returns:
            List of alert messages
        """
        if metrics is None:
            metrics = self.collect_all_metrics()

        alerts: list[str] = []

        try:
            self._check_connection_alerts(metrics, alerts)

            growth_rates = self.calculate_growth_rates()
            self._check_subscriber_alerts(growth_rates, alerts)
            self._check_task_alerts(growth_rates, alerts)

            self._check_cache_alerts(metrics, alerts)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alert checking errors unpredictable, must return partial alerts
            logger.error("Error checking alerts", error=str(e))
            alerts.append(f"ERROR: Failed to check some alerts: {e}")

        return alerts
