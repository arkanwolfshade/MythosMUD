"""
Metrics collection for NATS message delivery.

Collects and exposes metrics for monitoring message delivery,
failures, retries, and circuit breaker state.

AI: Metrics are critical for observability and incident response.
"""

from collections import Counter
from datetime import UTC, datetime
from threading import Lock
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MetricsCollector:
    """
    Simple metrics collector for NATS message delivery.

    Thread-safe metrics collection using Counters and locks.
    Designed to be lightweight and not impact message processing performance.

    AI: In-memory metrics with atomic updates for low overhead.
    """

    def __init__(self):
        """
        Initialize metrics collector.

        AI: Uses Lock for thread-safety in async context.
        """
        self._lock = Lock()

        # Message counters
        self.messages_processed: Counter[str] = Counter()
        self.messages_failed: Counter[str] = Counter()
        self.messages_retried: Counter[str] = Counter()
        self.messages_dlq: Counter[str] = Counter()

        # Circuit breaker state tracking
        self.circuit_state_changes: list[dict[str, Any]] = []
        self.circuit_open_count = 0

        # Performance metrics
        self.processing_times: list[float] = []
        self.max_processing_times = 1000  # Keep last N measurements

        # Timestamps
        self.start_time = datetime.now(UTC)
        self.last_reset_time = datetime.now(UTC)

        logger.info("MetricsCollector initialized")

    def record_message_processed(self, channel: str = "unknown") -> None:
        """
        Record a successfully processed message.

        Args:
            channel: Message channel for categorization

        AI: Track per-channel for detailed monitoring.
        """
        with self._lock:
            self.messages_processed[channel] += 1

    def record_message_failed(self, channel: str = "unknown", error_type: str = "unknown") -> None:
        """
        Record a failed message.

        Args:
            channel: Message channel
            error_type: Type of error that occurred

        AI: Track error types for pattern detection.
        """
        with self._lock:
            self.messages_failed[channel] += 1
            self.messages_failed[f"{channel}:{error_type}"] += 1

    def record_message_retried(self, channel: str = "unknown", attempt: int = 1) -> None:
        """
        Record a message retry attempt.

        Args:
            channel: Message channel
            attempt: Retry attempt number

        AI: High retry counts indicate systematic issues.
        """
        with self._lock:
            self.messages_retried[channel] += 1
            self.messages_retried[f"attempt_{attempt}"] += 1

    def record_message_dlq(self, channel: str = "unknown") -> None:
        """
        Record a message added to dead letter queue.

        Args:
            channel: Message channel

        AI: DLQ growth indicates serious delivery problems.
        """
        with self._lock:
            self.messages_dlq[channel] += 1

    def record_circuit_state_change(self, old_state: str, new_state: str, reason: str = "") -> None:
        """
        Record a circuit breaker state change.

        Args:
            old_state: Previous circuit state
            new_state: New circuit state
            reason: Reason for state change

        AI: State changes indicate service health transitions.
        """
        with self._lock:
            change = {
                "timestamp": datetime.now(UTC).isoformat(),
                "old_state": old_state,
                "new_state": new_state,
                "reason": reason,
            }

            self.circuit_state_changes.append(change)

            # Keep only last 100 state changes
            if len(self.circuit_state_changes) > 100:
                self.circuit_state_changes = self.circuit_state_changes[-100:]

            if new_state == "open":
                self.circuit_open_count += 1

    def record_processing_time(self, duration_ms: float) -> None:
        """
        Record message processing time.

        Args:
            duration_ms: Processing duration in milliseconds

        AI: Track performance and detect degradation.
        """
        with self._lock:
            self.processing_times.append(duration_ms)

            # Keep only recent measurements
            if len(self.processing_times) > self.max_processing_times:
                self.processing_times = self.processing_times[-self.max_processing_times :]

    def get_metrics(self) -> dict[str, Any]:
        """
        Get current metrics snapshot.

        Returns:
            Dictionary containing all metrics

        AI: For /api/metrics endpoint and monitoring.
        """
        with self._lock:
            uptime = (datetime.now(UTC) - self.start_time).total_seconds()

            # Calculate processing time statistics
            processing_stats = {}
            if self.processing_times:
                processing_stats = {
                    "avg_ms": sum(self.processing_times) / len(self.processing_times),
                    "min_ms": min(self.processing_times),
                    "max_ms": max(self.processing_times),
                    "count": len(self.processing_times),
                }

            # Calculate success rate
            total_processed = sum(self.messages_processed.values())
            total_failed = sum(self.messages_failed.values())
            total_attempts = total_processed + total_failed

            success_rate = (total_processed / total_attempts * 100) if total_attempts > 0 else 100.0

            return {
                "uptime_seconds": uptime,
                "messages": {
                    "processed": dict(self.messages_processed),
                    "failed": dict(self.messages_failed),
                    "retried": dict(self.messages_retried),
                    "dlq": dict(self.messages_dlq),
                    "total_processed": total_processed,
                    "total_failed": total_failed,
                    "success_rate_percent": round(success_rate, 2),
                },
                "circuit_breaker": {
                    "open_count": self.circuit_open_count,
                    "recent_state_changes": self.circuit_state_changes[-10:],  # Last 10
                },
                "performance": processing_stats,
                "collection_period": {
                    "start": self.last_reset_time.isoformat(),
                    "end": datetime.now(UTC).isoformat(),
                },
            }

    def reset_metrics(self) -> None:
        """
        Reset all metrics counters.

        Useful for clearing metrics after a deployment or maintenance window.

        AI: Use sparingly - metrics history is valuable for trend analysis.
        """
        with self._lock:
            self.messages_processed.clear()
            self.messages_failed.clear()
            self.messages_retried.clear()
            self.messages_dlq.clear()
            self.circuit_state_changes.clear()
            self.circuit_open_count = 0
            self.processing_times.clear()
            self.last_reset_time = datetime.now(UTC)

            logger.warning("Metrics reset", reset_time=self.last_reset_time.isoformat())

    def get_summary(self) -> dict[str, Any]:
        """
        Get concise metrics summary.

        Returns:
            High-level metrics summary

        AI: For quick health checks and alerting.
        """
        with self._lock:
            total_processed = sum(self.messages_processed.values())
            total_failed = sum(self.messages_failed.values())
            total_dlq = sum(self.messages_dlq.values())
            total_retries = sum(self.messages_retried.values())

            return {
                "messages_processed": total_processed,
                "messages_failed": total_failed,
                "messages_in_dlq": total_dlq,
                "total_retries": total_retries,
                "circuit_opens": self.circuit_open_count,
                "uptime_seconds": (datetime.now(UTC) - self.start_time).total_seconds(),
            }


# Global metrics collector instance
# AI: Singleton pattern for consistent metrics across the application
metrics_collector = MetricsCollector()
