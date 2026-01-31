"""
Memory monitoring and cleanup management for MythosMUD.

This module provides memory usage monitoring, cleanup scheduling,
and memory-related statistics for the real-time connection system.
"""

import gc
import os
import time
from typing import Any

import psutil

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _max_connection_age_seconds() -> int:
    """Connection age threshold (seconds). Higher in e2e/local to avoid mid-run drops."""
    env = os.environ.get("LOGGING_ENVIRONMENT") or ""
    return 1800 if env in ("e2e_test", "local") else 300


class MemoryMonitor:
    """
    Monitor memory usage and trigger cleanup when needed.

    This class provides memory monitoring, cleanup scheduling, and
    memory-related statistics for the connection management system.
    """

    def __init__(self) -> None:
        """Initialize the memory monitor with default settings."""
        self.last_cleanup_time = time.time()
        self.cleanup_interval = 300  # 5 minutes
        self.memory_threshold = 0.8  # 80% memory usage triggers cleanup
        self.max_connection_age = _max_connection_age_seconds()
        self.max_pending_messages = 1000  # Max pending messages per player
        self.max_rate_limit_entries = 1000  # Max rate limit entries per player

    def should_cleanup(self) -> bool:
        """
        Check if cleanup should be triggered.

        Returns:
            bool: True if cleanup should be triggered, False otherwise
        """
        current_time = time.time()
        memory_usage = self.get_memory_usage()

        # Time-based cleanup
        if current_time - self.last_cleanup_time > self.cleanup_interval:
            return True

        # Memory-based cleanup
        if memory_usage > self.memory_threshold:
            logger.warning("Memory usage high, triggering cleanup", memory_usage=memory_usage)
            return True

        return False

    def get_memory_usage(self) -> float:
        """
        Get current memory usage as percentage.

        Returns:
            float: Memory usage as a decimal (0.0 to 1.0)
        """
        try:
            process = psutil.Process()
            memory_percent = process.memory_percent()
            if not isinstance(memory_percent, (int, float)):
                raise TypeError("memory_percent must be int or float")
            return float(memory_percent) / 100.0
        except (OSError, ValueError, TypeError, RuntimeError) as e:
            logger.error("Error getting memory usage", error=str(e), error_type=type(e).__name__, exc_info=True)
            return 0.0

    def get_memory_stats(self) -> dict[str, Any]:
        """
        Get detailed memory statistics.

        Returns:
            dict: Memory statistics including RSS, VMS, percentage, and system memory
        """
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            return {
                "rss_mb": memory_info.rss / 1024 / 1024,
                "vms_mb": memory_info.vms / 1024 / 1024,
                "percent": process.memory_percent(),
                "available_mb": psutil.virtual_memory().available / 1024 / 1024,
                "total_mb": psutil.virtual_memory().total / 1024 / 1024,
            }
        except (OSError, ValueError, TypeError, RuntimeError) as e:
            logger.error("Error getting memory stats", error=str(e), error_type=type(e).__name__, exc_info=True)
            return {}

    def get_memory_alerts(self, connection_stats: dict[str, Any]) -> list[str]:
        """
        Get memory-related alerts based on current usage and connection statistics.

        Args:
            connection_stats: Current connection and data structure statistics

        Returns:
            list[str]: List of memory-related alerts
        """
        alerts = []

        try:
            memory_usage = self.get_memory_usage()

            if memory_usage > 0.9:  # 90%
                alerts.append(f"CRITICAL: Memory usage at {memory_usage:.1%}")
            elif memory_usage > 0.8:  # 80%
                alerts.append(f"WARNING: Memory usage at {memory_usage:.1%}")
            elif memory_usage > 0.7:  # 70%
                alerts.append(f"INFO: Memory usage at {memory_usage:.1%}")

            # Check for large data structures
            if connection_stats.get("connection_attempts", 0) > 1000:
                alerts.append(
                    f"WARNING: Large number of rate limit entries: {connection_stats.get('connection_attempts')}"
                )

            if connection_stats.get("pending_messages", 0) > 1000:
                alerts.append(
                    f"WARNING: Large number of pending message queues: {connection_stats.get('pending_messages')}"
                )

            # Check for stale connections
            stale_count = connection_stats.get("stale_connections", 0)
            if stale_count > 0:
                alerts.append(f"WARNING: {stale_count} stale connections detected")

        except (OSError, ValueError, TypeError, RuntimeError) as e:
            logger.error("Error getting memory alerts", error=str(e), error_type=type(e).__name__, exc_info=True)
            alerts.append(f"ERROR: Failed to get memory alerts: {e}")

        return alerts

    def update_cleanup_time(self) -> None:
        """Update the last cleanup time to the current time."""
        self.last_cleanup_time = time.time()

    def force_garbage_collection(self) -> None:
        """Force garbage collection to free memory."""
        try:
            gc.collect()
            logger.debug("Forced garbage collection completed")
        except RuntimeError as e:
            logger.error(
                "Error during forced garbage collection", error=str(e), error_type=type(e).__name__, exc_info=True
            )
