"""
NATS metrics collection for MythosMUD.

This module provides metrics collection for NATS service operations,
enabling monitoring and alerting for the real-time messaging system.
"""

from collections import deque
from typing import Any


class NATSMetrics:  # pylint: disable=too-many-instance-attributes  # Reason: Metrics class requires many fields to capture complete NATS metrics
    """NATS-specific metrics collection for monitoring and alerting."""

    def __init__(self) -> None:
        self.publish_count = 0
        self.publish_errors = 0
        self.subscribe_count = 0
        self.subscribe_errors = 0
        # Use deque with maxlen for automatic rotation - more memory efficient than list slicing
        self.message_processing_times: deque[float] = deque(maxlen=1000)
        self.connection_health_score = 100.0
        self.batch_flush_count = 0
        self.batch_flush_errors = 0
        self.pool_utilization = 0.0
        # Acknowledgment metrics (for manual ack mode)
        self.ack_success_count = 0
        self.ack_failure_count = 0
        self.nak_count = 0

    def record_publish(self, success: bool, processing_time: float) -> None:
        """Record publish operation metrics."""
        self.publish_count += 1
        if not success:
            self.publish_errors += 1
        # Deque automatically rotates when maxlen is reached - no manual slicing needed
        self.message_processing_times.append(processing_time)

    def record_subscribe(self, success: bool) -> None:
        """Record subscribe operation metrics."""
        self.subscribe_count += 1
        if not success:
            self.subscribe_errors += 1

    def record_batch_flush(self, success: bool, _message_count: int) -> None:
        """Record batch flush operation metrics."""
        self.batch_flush_count += 1
        if not success:
            self.batch_flush_errors += 1

    def update_connection_health(self, health_score: float) -> None:
        """Update connection health score (0-100)."""
        self.connection_health_score = max(0.0, min(100.0, health_score))

    def update_pool_utilization(self, utilization: float) -> None:
        """Update connection pool utilization (0-1)."""
        self.pool_utilization = max(0.0, min(1.0, utilization))

    def record_ack_success(self) -> None:
        """Record successful message acknowledgment."""
        self.ack_success_count += 1

    def record_ack_failure(self) -> None:
        """Record failed message acknowledgment."""
        self.ack_failure_count += 1

    def record_nak(self) -> None:
        """Record negative acknowledgment (message requeued)."""
        self.nak_count += 1

    def get_metrics(self) -> dict[str, Any]:
        """Get comprehensive NATS metrics."""
        # Deque supports len() and iteration like a list
        avg_processing_time = (
            sum(self.message_processing_times) / len(self.message_processing_times)
            if self.message_processing_times
            else 0
        )

        return {
            "publish_count": self.publish_count,
            "publish_error_rate": self.publish_errors / max(self.publish_count, 1),
            "subscribe_count": self.subscribe_count,
            "subscribe_error_rate": self.subscribe_errors / max(self.subscribe_count, 1),
            "avg_processing_time_ms": avg_processing_time * 1000,
            "connection_health": self.connection_health_score,
            "pool_utilization": self.pool_utilization,
            "batch_flush_count": self.batch_flush_count,
            "batch_flush_error_rate": self.batch_flush_errors / max(self.batch_flush_count, 1),
            "processing_time_samples": len(self.message_processing_times),
            # Acknowledgment metrics
            "ack_success_count": self.ack_success_count,
            "ack_failure_count": self.ack_failure_count,
            "ack_failure_rate": self.ack_failure_count / max(self.ack_success_count + self.ack_failure_count, 1),
            "nak_count": self.nak_count,
        }
