"""
Performance tracking for connection management.

This module provides comprehensive performance metric collection and analysis
for connection lifecycle events, message delivery, and health monitoring.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Performance tracking is now a focused, independently testable component.
"""

import time
from typing import Any, TypedDict

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
        if len(self.performance_stats[metric_key]) > self.max_samples:  # type: ignore[literal-required]
            self.performance_stats[metric_key] = self.performance_stats[metric_key][-self.max_samples :]  # type: ignore[literal-required]

    def get_stats(self) -> dict[str, Any]:
        """
        Get comprehensive performance statistics with calculated averages.

        Returns:
            dict: Performance statistics including timing data and averages
        """
        try:
            # Calculate averages for connection establishment times
            websocket_times = [
                duration
                for conn_type, duration in self.performance_stats["connection_establishment_times"]
                if conn_type == "websocket"
            ]

            # Calculate averages for message delivery times
            message_times = [duration for msg_type, duration in self.performance_stats["message_delivery_times"]]

            # Calculate averages for disconnection times
            disconnection_times = [duration for conn_type, duration in self.performance_stats["disconnection_times"]]

            # Get session switch times
            session_switch_times = self.performance_stats["session_switch_times"]

            # Get health check times
            health_check_times = self.performance_stats["health_check_times"]

            return {
                "connection_establishment": {
                    "total_connections": self.performance_stats["total_connections_established"],
                    "websocket_connections": len(websocket_times),
                    "avg_websocket_establishment_ms": sum(websocket_times) / len(websocket_times)
                    if websocket_times
                    else 0,
                    "max_websocket_establishment_ms": max(websocket_times) if websocket_times else 0,
                    "min_websocket_establishment_ms": min(websocket_times) if websocket_times else 0,
                },
                "message_delivery": {
                    "total_messages": self.performance_stats["total_messages_delivered"],
                    "avg_delivery_time_ms": sum(message_times) / len(message_times) if message_times else 0,
                    "max_delivery_time_ms": max(message_times) if message_times else 0,
                    "min_delivery_time_ms": min(message_times) if message_times else 0,
                },
                "disconnections": {
                    "total_disconnections": self.performance_stats["total_disconnections"],
                    "avg_disconnection_time_ms": sum(disconnection_times) / len(disconnection_times)
                    if disconnection_times
                    else 0,
                    "max_disconnection_time_ms": max(disconnection_times) if disconnection_times else 0,
                    "min_disconnection_time_ms": min(disconnection_times) if disconnection_times else 0,
                },
                "session_management": {
                    "total_session_switches": self.performance_stats["total_session_switches"],
                    "avg_session_switch_time_ms": sum(session_switch_times) / len(session_switch_times)
                    if session_switch_times
                    else 0,
                    "max_session_switch_time_ms": max(session_switch_times) if session_switch_times else 0,
                    "min_session_switch_time_ms": min(session_switch_times) if session_switch_times else 0,
                },
                "health_monitoring": {
                    "total_health_checks": self.performance_stats["total_health_checks"],
                    "avg_health_check_time_ms": sum(health_check_times) / len(health_check_times)
                    if health_check_times
                    else 0,
                    "max_health_check_time_ms": max(health_check_times) if health_check_times else 0,
                    "min_health_check_time_ms": min(health_check_times) if health_check_times else 0,
                },
                "timestamp": time.time(),
            }
        except Exception as e:
            logger.error("Error getting performance stats", error=str(e), exc_info=True)
            return {"error": f"Failed to get performance stats: {e}", "timestamp": time.time()}
