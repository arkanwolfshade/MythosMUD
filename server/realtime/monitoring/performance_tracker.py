"""
Performance tracking for connection management.

This module provides comprehensive performance metric collection and analysis
for connection lifecycle events, message delivery, and health monitoring.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Performance tracking is now a focused, independently testable component.
"""

import time
from typing import Any, TypedDict

import numpy as np

from ...structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PerformanceStats(TypedDict):
    """Type definition for performance statistics tracking."""

    connection_establishment_times: list[tuple[str, float]]
    message_delivery_times: list[tuple[str, float]]
    disconnection_times: list[tuple[str, float]]
    session_switch_times: list[float]
    health_check_times: list[float]
    total_connections_established: int
    total_messages_delivered: int
    total_disconnections: int
    total_session_switches: int
    total_health_checks: int


class PerformanceTracker:
    """
    Tracks performance metrics for connection management operations.

    This class provides:
    - Connection establishment timing
    - Message delivery timing
    - Disconnection timing
    - Session switch timing
    - Health check timing
    - Statistical analysis of performance data

    AI Agent: Single Responsibility - Performance metric collection and analysis only.
    """

    def __init__(self, max_samples: int = 1000) -> None:
        """
        Initialize the performance tracker.

        Args:
            max_samples: Maximum number of samples to keep for each metric (prevents unbounded growth)
        """
        self.max_samples = max_samples
        self.performance_stats: PerformanceStats = {
            "connection_establishment_times": [],
            "message_delivery_times": [],
            "disconnection_times": [],
            "session_switch_times": [],
            "health_check_times": [],
            "total_connections_established": 0,
            "total_messages_delivered": 0,
            "total_disconnections": 0,
            "total_session_switches": 0,
            "total_health_checks": 0,
        }

    def record_connection_establishment(self, connection_type: str, duration_ms: float) -> None:
        """
        Record a connection establishment event.

        Args:
            connection_type: Type of connection (e.g., "websocket")
            duration_ms: Duration in milliseconds
        """
        self.performance_stats["connection_establishment_times"].append((connection_type, duration_ms))
        self.performance_stats["total_connections_established"] += 1
        self._trim_samples("connection_establishment_times")

    def record_message_delivery(self, message_type: str, duration_ms: float) -> None:
        """
        Record a message delivery event.

        Args:
            message_type: Type of message
            duration_ms: Duration in milliseconds
        """
        self.performance_stats["message_delivery_times"].append((message_type, duration_ms))
        self.performance_stats["total_messages_delivered"] += 1
        self._trim_samples("message_delivery_times")

    def record_disconnection(self, connection_type: str, duration_ms: float) -> None:
        """
        Record a disconnection event.

        Args:
            connection_type: Type of connection
            duration_ms: Duration in milliseconds
        """
        self.performance_stats["disconnection_times"].append((connection_type, duration_ms))
        self.performance_stats["total_disconnections"] += 1
        self._trim_samples("disconnection_times")

    def record_session_switch(self, duration_ms: float) -> None:
        """
        Record a session switch event.

        Args:
            duration_ms: Duration in milliseconds
        """
        self.performance_stats["session_switch_times"].append(duration_ms)
        self.performance_stats["total_session_switches"] += 1
        self._trim_samples("session_switch_times")

    def record_health_check(self, duration_ms: float) -> None:
        """
        Record a health check event.

        Args:
            duration_ms: Duration in milliseconds
        """
        self.performance_stats["health_check_times"].append(duration_ms)
        self.performance_stats["total_health_checks"] += 1
        self._trim_samples("health_check_times")

    def _trim_samples(self, metric_key: str) -> None:
        """
        Trim samples to prevent unbounded memory growth.

        Args:
            metric_key: Key in performance_stats to trim
        """
        if len(self.performance_stats[metric_key]) > self.max_samples:  # type: ignore[literal-required]  # Reason: TypedDict access with variable key, mypy cannot verify key exists or value type, but _trim_samples is only called with known list keys
            self.performance_stats[metric_key] = self.performance_stats[metric_key][-self.max_samples :]  # type: ignore[literal-required]  # Reason: TypedDict access with variable key, mypy cannot verify key exists or value type, but _trim_samples is only called with known list keys

    def get_stats(self) -> dict[str, Any]:
        """
        Get comprehensive performance statistics with calculated averages.

        Returns:
            dict: Performance statistics including timing data and averages
        """
        try:
            # Filter and convert to NumPy arrays with explicit dtype for efficient statistical operations
            websocket_times = np.array(
                [
                    duration
                    for conn_type, duration in self.performance_stats["connection_establishment_times"]
                    if conn_type == "websocket"
                ],
                dtype=np.float32,
            )

            # Calculate averages for message delivery times
            message_times = np.array(
                [duration for msg_type, duration in self.performance_stats["message_delivery_times"]], dtype=np.float32
            )

            # Calculate averages for disconnection times
            disconnection_times = np.array(
                [duration for conn_type, duration in self.performance_stats["disconnection_times"]], dtype=np.float32
            )

            # Get session switch times
            session_switch_times = np.array(self.performance_stats["session_switch_times"], dtype=np.float32)

            # Get health check times
            health_check_times = np.array(self.performance_stats["health_check_times"], dtype=np.float32)

            # Helper function to safely calculate stats from NumPy array
            def _calculate_stats(times: np.ndarray) -> dict[str, float]:
                """Calculate statistical measures from a NumPy array of times."""
                if times.size > 0:
                    return {
                        "avg": float(np.mean(times)),
                        "max": float(np.max(times)),
                        "min": float(np.min(times)),
                    }
                return {"avg": 0.0, "max": 0.0, "min": 0.0}

            websocket_stats = _calculate_stats(websocket_times)
            message_stats = _calculate_stats(message_times)
            disconnection_stats = _calculate_stats(disconnection_times)
            session_switch_stats = _calculate_stats(session_switch_times)
            health_check_stats = _calculate_stats(health_check_times)

            return {
                "connection_establishment": {
                    "total_connections": self.performance_stats["total_connections_established"],
                    "websocket_connections": websocket_times.size,
                    "avg_websocket_establishment_ms": websocket_stats["avg"],
                    "max_websocket_establishment_ms": websocket_stats["max"],
                    "min_websocket_establishment_ms": websocket_stats["min"],
                },
                "message_delivery": {
                    "total_messages": self.performance_stats["total_messages_delivered"],
                    "avg_delivery_time_ms": message_stats["avg"],
                    "max_delivery_time_ms": message_stats["max"],
                    "min_delivery_time_ms": message_stats["min"],
                },
                "disconnections": {
                    "total_disconnections": self.performance_stats["total_disconnections"],
                    "avg_disconnection_time_ms": disconnection_stats["avg"],
                    "max_disconnection_time_ms": disconnection_stats["max"],
                    "min_disconnection_time_ms": disconnection_stats["min"],
                },
                "session_management": {
                    "total_session_switches": self.performance_stats["total_session_switches"],
                    "avg_session_switch_time_ms": session_switch_stats["avg"],
                    "max_session_switch_time_ms": session_switch_stats["max"],
                    "min_session_switch_time_ms": session_switch_stats["min"],
                },
                "health_monitoring": {
                    "total_health_checks": self.performance_stats["total_health_checks"],
                    "avg_health_check_time_ms": health_check_stats["avg"],
                    "max_health_check_time_ms": health_check_stats["max"],
                    "min_health_check_time_ms": health_check_stats["min"],
                },
                "timestamp": time.time(),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Performance stats retrieval errors unpredictable, must return error response
            logger.error("Error getting performance stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get performance stats: {e}", "timestamp": time.time()}
