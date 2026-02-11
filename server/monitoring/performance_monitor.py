"""
Performance monitoring and metrics collection for MythosMUD server.

This module provides comprehensive performance monitoring, metrics collection,
and alerting capabilities for the MythosMUD server.

As noted in the Pnakotic Manuscripts, understanding the flow and performance
of our systems is essential for maintaining their stability and efficiency.
"""

import time
from collections import defaultdict, deque
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from server.structured_logging.enhanced_logging_config import get_logger, log_with_context

logger = get_logger(__name__)


@dataclass
class PerformanceMetric:
    """Represents a single performance metric."""

    operation: str
    duration_ms: float
    timestamp: float
    success: bool
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class PerformanceStats:  # pylint: disable=too-many-instance-attributes  # Reason: Performance stats requires many fields to capture complete performance metrics
    """Aggregated performance statistics."""

    operation: str
    count: int
    total_duration_ms: float
    avg_duration_ms: float
    min_duration_ms: float
    max_duration_ms: float
    success_rate: float
    error_rate: float


class PerformanceMonitor:
    """
    Performance monitoring and metrics collection system.

    This class provides comprehensive performance monitoring capabilities including
    timing, metrics collection, alerting, and reporting.
    """

    def __init__(self, max_metrics: int = 10000, alert_threshold_ms: float = 1000.0) -> None:
        """
        Initialize the performance monitor.

        Args:
            max_metrics: Maximum number of metrics to keep in memory
            alert_threshold_ms: Threshold for performance alerts (milliseconds)
        """
        self.max_metrics = max_metrics
        self.alert_threshold_ms = alert_threshold_ms
        self.metrics: deque[PerformanceMetric] = deque(maxlen=max_metrics)
        self.operation_stats: dict[str, list[PerformanceMetric]] = defaultdict(list)
        self.alert_callbacks: list[Callable[[PerformanceMetric, dict[str, Any]], None]] = []

        logger.info("Performance monitor initialized", max_metrics=max_metrics, alert_threshold_ms=alert_threshold_ms)

    def record_metric(
        self, operation: str, duration_ms: float, success: bool = True, metadata: dict[str, Any] | None = None
    ) -> None:
        """
        Record a performance metric.

        Args:
            operation: Name of the operation
            duration_ms: Duration in milliseconds
            success: Whether the operation was successful
            metadata: Additional metadata about the operation
        """
        if metadata is None:
            metadata = {}

        metric = PerformanceMetric(
            operation=operation, duration_ms=duration_ms, timestamp=time.time(), success=success, metadata=metadata
        )

        # Store the metric
        self.metrics.append(metric)
        self.operation_stats[operation].append(metric)

        # Check for alerts
        if duration_ms > self.alert_threshold_ms:
            self._trigger_alert(metric)

        # Log the metric
        log_with_context(
            logger,
            "info",
            "Performance metric recorded",
            operation=operation,
            duration_ms=duration_ms,
            success=success,
            metadata=metadata,
            alert_triggered=duration_ms > self.alert_threshold_ms,
        )

    def get_operation_stats(self, operation: str) -> PerformanceStats | None:
        """
        Get performance statistics for a specific operation.

        Args:
            operation: Name of the operation

        Returns:
            Performance statistics or None if no metrics exist
        """
        if operation not in self.operation_stats or not self.operation_stats[operation]:
            return None

        metrics = self.operation_stats[operation]
        # Convert to NumPy arrays with explicit dtype for efficient statistical operations
        durations = np.array([m.duration_ms for m in metrics], dtype=np.float32)
        successes = np.array([m.success for m in metrics], dtype=np.bool_)

        return PerformanceStats(
            operation=operation,
            count=len(metrics),
            total_duration_ms=float(np.sum(durations)),
            avg_duration_ms=float(np.mean(durations)),
            min_duration_ms=float(np.min(durations)),
            max_duration_ms=float(np.max(durations)),
            success_rate=float(np.mean(successes) * 100),
            error_rate=float((1 - np.mean(successes)) * 100),
        )

    def get_all_stats(self) -> dict[str, PerformanceStats | None]:
        """
        Get performance statistics for all operations.

        Returns:
            Dictionary mapping operation names to their statistics (None if no stats available)
        """
        stats: dict[str, PerformanceStats | None] = {}
        for operation in self.operation_stats:
            stats[operation] = self.get_operation_stats(operation)
        return stats

    def get_recent_metrics(self, count: int = 100) -> list[PerformanceMetric]:
        """
        Get the most recent performance metrics.

        Args:
            count: Number of recent metrics to return

        Returns:
            List of recent performance metrics
        """
        return list(self.metrics)[-count:]

    def get_slow_operations(self, threshold_ms: float | None = None) -> list[PerformanceMetric]:
        """
        Get operations that exceeded the performance threshold.

        Args:
            threshold_ms: Performance threshold (uses default if None)

        Returns:
            List of slow operations
        """
        if threshold_ms is None:
            threshold_ms = self.alert_threshold_ms

        return [m for m in self.metrics if m.duration_ms > threshold_ms]

    def get_failed_operations(self) -> list[PerformanceMetric]:
        """
        Get operations that failed.

        Returns:
            List of failed operations
        """
        return [m for m in self.metrics if not m.success]

    def add_alert_callback(self, callback: Callable[[PerformanceMetric, dict[str, Any]], None]) -> None:
        """
        Add an alert callback function.

        Args:
            callback: Function to call when performance alerts are triggered (metric, alert_data)
        """
        self.alert_callbacks.append(callback)

    def _trigger_alert(self, metric: PerformanceMetric) -> None:
        """
        Trigger performance alerts for slow operations.

        Args:
            metric: The performance metric that triggered the alert
        """
        alert_data = {
            "operation": metric.operation,
            "duration_ms": metric.duration_ms,
            "threshold_ms": self.alert_threshold_ms,
            "timestamp": metric.timestamp,
            "metadata": metric.metadata,
        }

        # Log the alert
        log_with_context(
            logger,
            "warning",
            "Performance alert: operation exceeded threshold",
            **alert_data,
        )

        # Call alert callbacks
        for callback in self.alert_callbacks:
            try:
                callback(metric, alert_data)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Callback errors unpredictable, must not fail alert processing
                logger.error("Alert callback failed", callback=str(callback), error=str(e), exc_info=True)

    def reset_metrics(self) -> None:
        """Reset all performance metrics."""
        self.metrics.clear()
        self.operation_stats.clear()

        logger.info("Performance metrics reset")

    def export_metrics(self) -> dict[str, Any]:
        """
        Export metrics data for external monitoring systems.

        Returns:
            Dictionary containing all metrics data
        """
        return {
            "total_metrics": len(self.metrics),
            "operations": list(self.operation_stats.keys()),
            "stats": {op: self.get_operation_stats(op) for op in self.operation_stats},
            "recent_metrics": [
                {
                    "operation": m.operation,
                    "duration_ms": m.duration_ms,
                    "timestamp": m.timestamp,
                    "success": m.success,
                    "metadata": m.metadata,
                }
                for m in self.get_recent_metrics(100)
            ],
        }


# Global performance monitor instance
_performance_monitor: PerformanceMonitor | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_performance_monitor() -> PerformanceMonitor:
    """
    Get the global performance monitor instance.

    Returns:
        Global PerformanceMonitor instance
    """
    global _performance_monitor  # pylint: disable=global-statement  # Reason: Singleton pattern for performance monitoring
    if _performance_monitor is None:
        _performance_monitor = PerformanceMonitor()
    return _performance_monitor


@contextmanager
def measure_performance(
    operation: str, metadata: dict[str, Any] | None = None, monitor: PerformanceMonitor | None = None
) -> Iterator[None]:
    """
    Context manager for measuring operation performance.

    Args:
        operation: Name of the operation being measured
        metadata: Additional metadata about the operation
        monitor: Performance monitor instance (uses global if None)

    Yields:
        Context manager for performance measurement
    """
    if monitor is None:
        monitor = get_performance_monitor()

    if metadata is None:
        metadata = {}

    start_time = time.time()
    success = True
    error = None

    try:
        yield
    except Exception as e:
        success = False
        error = e
        raise
    finally:
        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000

        # Add error information to metadata if operation failed
        if not success and error:
            metadata["error_type"] = type(error).__name__
            metadata["error_message"] = str(error)

        # Record the metric
        monitor.record_metric(operation=operation, duration_ms=duration_ms, success=success, metadata=metadata)


def record_performance_metric(
    operation: str,
    duration_ms: float,
    success: bool = True,
    metadata: dict[str, Any] | None = None,
    monitor: PerformanceMonitor | None = None,
) -> None:
    """
    Record a performance metric.

    Args:
        operation: Name of the operation
        duration_ms: Duration in milliseconds
        success: Whether the operation was successful
        metadata: Additional metadata about the operation
        monitor: Performance monitor instance (uses global if None)
    """
    if monitor is None:
        monitor = get_performance_monitor()

    monitor.record_metric(operation, duration_ms, success, metadata)


def get_performance_stats(operation: str | None = None, monitor: PerformanceMonitor | None = None) -> Any:
    """
    Get performance statistics.

    Args:
        operation: Specific operation name (returns all if None)
        monitor: Performance monitor instance (uses global if None)

    Returns:
        Performance statistics
    """
    if monitor is None:
        monitor = get_performance_monitor()

    if operation:
        return monitor.get_operation_stats(operation)
    return monitor.get_all_stats()


def reset_performance_metrics(monitor: PerformanceMonitor | None = None) -> None:
    """
    Reset performance metrics.

    Args:
        monitor: Performance monitor instance (uses global if None)
    """
    if monitor is None:
        monitor = get_performance_monitor()

    monitor.reset_metrics()
