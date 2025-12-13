"""
Performance metrics for NATS Subject Manager operations.

This module provides metrics collection and reporting for subject management
operations, tracking validation times, cache performance, and operation counts.

AI: Provides observability into subject management performance.
AI: Helps identify bottlenecks and optimize validation operations.
"""

from collections import deque
from collections.abc import Iterable
from typing import Any


class SubjectManagerMetrics:
    """
    Performance metrics for NATS Subject Manager operations.

    Tracks validation times, cache performance, and operation counts
    for monitoring and optimization purposes.

    AI: Provides observability into subject management performance.
    AI: Helps identify bottlenecks and optimize validation operations.
    """

    def __init__(self):
        """Initialize metrics collection."""
        # Validation metrics
        self.validation_count = 0
        self.validation_success_count = 0
        self.validation_failure_count = 0
        self.validation_times: deque[float] = deque(maxlen=1000)  # Rolling window of last 1000 times

        # Cache metrics
        self.cache_hits = 0
        self.cache_misses = 0

        # Build metrics
        self.build_count = 0
        self.build_success_count = 0
        self.build_failure_count = 0
        self.build_times: deque[float] = deque(maxlen=1000)  # Rolling window of last 1000 times

        # Error metrics
        self.pattern_not_found_errors = 0
        self.missing_parameter_errors = 0
        self.validation_errors = 0

    def record_validation(self, duration: float, success: bool, cache_hit: bool):
        """
        Record a validation operation.

        Args:
            duration: Time taken in seconds
            success: Whether validation succeeded
            cache_hit: Whether result was from cache
        """
        self.validation_count += 1
        if success:
            self.validation_success_count += 1
        else:
            self.validation_failure_count += 1

        if cache_hit:
            self.cache_hits += 1
        else:
            self.cache_misses += 1

        self.validation_times.append(duration)

    def record_build(self, duration: float, success: bool):
        """
        Record a build operation.

        Args:
            duration: Time taken in seconds
            success: Whether build succeeded
        """
        self.build_count += 1
        if success:
            self.build_success_count += 1
        else:
            self.build_failure_count += 1

        self.build_times.append(duration)

    def record_error(self, error_type: str):
        """
        Record an error occurrence.

        Args:
            error_type: Type of error (pattern_not_found, missing_parameter, validation_error)
        """
        if error_type == "pattern_not_found":
            self.pattern_not_found_errors += 1
        elif error_type == "missing_parameter":
            self.missing_parameter_errors += 1
        elif error_type == "validation_error":
            self.validation_errors += 1

    def get_metrics(self) -> dict[str, Any]:
        """
        Get current metrics summary.

        Returns:
            Dictionary containing all metrics
        """
        return {
            "validation": {
                "total_count": self.validation_count,
                "success_count": self.validation_success_count,
                "failure_count": self.validation_failure_count,
                "success_rate": self.validation_success_count / max(self.validation_count, 1),
                "avg_time_ms": sum(self.validation_times) / max(len(self.validation_times), 1) * 1000,
                "p95_time_ms": self._calculate_percentile(self.validation_times, 0.95) * 1000
                if self.validation_times
                else 0,
            },
            "cache": {
                "hits": self.cache_hits,
                "misses": self.cache_misses,
                "hit_rate": self.cache_hits / max(self.cache_hits + self.cache_misses, 1),
            },
            "build": {
                "total_count": self.build_count,
                "success_count": self.build_success_count,
                "failure_count": self.build_failure_count,
                "success_rate": self.build_success_count / max(self.build_count, 1),
                "avg_time_ms": sum(self.build_times) / max(len(self.build_times), 1) * 1000,
                "p95_time_ms": self._calculate_percentile(self.build_times, 0.95) * 1000 if self.build_times else 0,
            },
            "errors": {
                "pattern_not_found": self.pattern_not_found_errors,
                "missing_parameter": self.missing_parameter_errors,
                "validation_errors": self.validation_errors,
                "total_errors": self.pattern_not_found_errors + self.missing_parameter_errors + self.validation_errors,
            },
        }

    @staticmethod
    def _calculate_percentile(times: Iterable[float], percentile: float) -> float:
        """
        Calculate percentile from list of times.

        Args:
            times: List of time measurements
            percentile: Percentile to calculate (0.0-1.0)

        Returns:
            Percentile value
        """
        if not times:
            return 0.0
        sorted_times = sorted(times)
        index = int(len(sorted_times) * percentile)
        return sorted_times[min(index, len(sorted_times) - 1)]

    def reset(self) -> None:
        """Reset all metrics to zero."""
        # Reset all metrics manually instead of calling __init__ to avoid type safety issues
        self.validation_count = 0
        self.validation_success_count = 0
        self.validation_failure_count = 0
        self.validation_times.clear()
        self.cache_hits = 0
        self.cache_misses = 0
        self.build_count = 0
        self.build_success_count = 0
        self.build_failure_count = 0
        self.build_times.clear()
        self.pattern_not_found_errors = 0
        self.missing_parameter_errors = 0
        self.validation_errors = 0
