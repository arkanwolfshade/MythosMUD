"""Monitoring package for MythosMUD server."""

from typing import Any

from server.monitoring.exception_tracker import ExceptionStats, get_exception_tracker

# pylint: disable=redefined-outer-name  # Reason: Test fixtures need to be redefined for each test

# Lazy imports to avoid numpy dependency during test imports
# These modules import numpy, so we defer their import until actually needed
# Stub definitions to satisfy linters - actual values provided by __getattr__
# pylint: disable=invalid-name  # Reason: Stub variable names must match lazy-imported names, not constants
PerformanceStats: type | None = None  # Reason: Lazy import via __getattr__
get_performance_monitor: Any | None = None  # Reason: Lazy import via __getattr__
MonitoringDashboard: type | None = None  # Reason: Lazy import via __getattr__
get_monitoring_dashboard: Any | None = None  # Reason: Lazy import via __getattr__


def __getattr__(name: str) -> Any:
    """Lazy import for modules that require numpy."""
    if name in ("MonitoringDashboard", "get_monitoring_dashboard"):
        from server.monitoring.monitoring_dashboard import (  # noqa: PLC0415
            MonitoringDashboard,
            get_monitoring_dashboard,
        )

        if name == "MonitoringDashboard":
            return MonitoringDashboard
        return get_monitoring_dashboard
    if name in ("PerformanceStats", "get_performance_monitor"):
        from server.monitoring.performance_monitor import PerformanceStats, get_performance_monitor  # noqa: PLC0415

        if name == "PerformanceStats":
            return PerformanceStats
        return get_performance_monitor
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "ExceptionStats",
    "get_exception_tracker",
    "PerformanceStats",
    "get_performance_monitor",
    "MonitoringDashboard",
    "get_monitoring_dashboard",
]
