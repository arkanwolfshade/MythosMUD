"""Unit tests for server.monitoring lazy __getattr__ re-exports."""

from __future__ import annotations

import importlib

import pytest

import server.monitoring as monitoring_pkg


def test_monitoring_eager_imports() -> None:
    """Exception tracker symbols import without triggering numpy lazy paths."""
    assert monitoring_pkg.get_exception_tracker is not None
    assert monitoring_pkg.ExceptionStats is not None


def test_monitoring_getattr_lazy_dashboard_symbols() -> None:
    """__getattr__ resolves MonitoringDashboard and get_monitoring_dashboard."""
    mod = importlib.import_module("server.monitoring")
    dashboard_cls = mod.__getattr__("MonitoringDashboard")
    get_dashboard = mod.__getattr__("get_monitoring_dashboard")
    assert dashboard_cls.__name__ == "MonitoringDashboard"
    assert callable(get_dashboard)


def test_monitoring_getattr_lazy_performance_symbols() -> None:
    """__getattr__ resolves PerformanceStats and get_performance_monitor."""
    mod = importlib.import_module("server.monitoring")
    stats_cls = mod.__getattr__("PerformanceStats")
    get_monitor = mod.__getattr__("get_performance_monitor")
    assert stats_cls.__name__ == "PerformanceStats"
    assert callable(get_monitor)


def test_monitoring_getattr_unknown_raises() -> None:
    """Unknown attribute names raise AttributeError."""
    with pytest.raises(AttributeError, match="has no attribute 'not_a_symbol'"):
        _ = monitoring_pkg.not_a_symbol  # type: ignore[attr-defined]


def test_monitoring_getattr_direct_call() -> None:
    """Direct __getattr__ covers both branch returns for dashboard imports."""
    mod = importlib.import_module("server.monitoring")
    assert mod.__getattr__("MonitoringDashboard").__name__ == "MonitoringDashboard"
    assert callable(mod.__getattr__("get_monitoring_dashboard"))
    assert mod.__getattr__("PerformanceStats").__name__ == "PerformanceStats"
    assert callable(mod.__getattr__("get_performance_monitor"))
