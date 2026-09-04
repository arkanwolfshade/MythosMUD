"""Unit tests for server.monitoring.performance_monitor."""

# pyright: reportPrivateUsage=false, reportUnusedFunction=false
# Reason: autouse fixture resets perf_mod._performance_monitor; tests touch module private state.

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

import server.monitoring.performance_monitor as perf_mod
from server.monitoring.performance_monitor import (
    PerformanceMonitor,
    get_performance_monitor,
    measure_performance,
    record_performance_metric,
    reset_performance_metrics,
)


@pytest.fixture(autouse=True)
def _reset_global_monitor() -> None:
    perf_mod._performance_monitor = None  # pylint: disable=protected-access


def test_record_metric_and_stats() -> None:
    monitor = PerformanceMonitor(max_metrics=100, alert_threshold_ms=50.0)
    monitor.record_metric("op_a", 10.0, success=True, metadata={"k": "v"})
    monitor.record_metric("op_a", 30.0, success=False)

    stats = monitor.get_operation_stats("op_a")
    assert stats is not None
    assert stats.count == 2
    assert stats.operation == "op_a"
    assert stats.min_duration_ms == 10.0
    assert stats.max_duration_ms == 30.0
    assert stats.error_rate == 50.0


def test_get_operation_stats_missing_returns_none() -> None:
    monitor = PerformanceMonitor()
    assert monitor.get_operation_stats("missing") is None


def test_get_all_stats_and_recent_metrics() -> None:
    monitor = PerformanceMonitor()
    monitor.record_metric("a", 1.0)
    monitor.record_metric("b", 2.0)
    all_stats = monitor.get_all_stats()
    assert set(all_stats.keys()) == {"a", "b"}
    recent = monitor.get_recent_metrics(count=1)
    assert len(recent) == 1
    assert recent[0].operation == "b"


def test_slow_and_failed_operations() -> None:
    monitor = PerformanceMonitor(alert_threshold_ms=5.0)
    monitor.record_metric("slow", 10.0, success=True)
    monitor.record_metric("fail", 1.0, success=False)
    assert len(monitor.get_slow_operations()) == 1
    assert monitor.get_slow_operations(threshold_ms=20.0) == []
    assert len(monitor.get_failed_operations()) == 1


def test_alert_callback_and_callback_error_is_swallowed() -> None:
    monitor = PerformanceMonitor(alert_threshold_ms=1.0)
    callback: MagicMock = MagicMock(side_effect=RuntimeError("boom"))
    monitor.add_alert_callback(callback)
    monitor.record_metric("slow_op", 5.0)
    callback.assert_called_once()


def test_reset_and_export_metrics() -> None:
    monitor = PerformanceMonitor()
    monitor.record_metric("x", 3.0, metadata={"tag": "t"})
    exported = monitor.export_metrics()
    assert exported["total_metrics"] == 1
    assert exported["operations"] == ["x"]
    assert exported["recent_metrics"][0]["operation"] == "x"
    monitor.reset_metrics()
    assert monitor.export_metrics()["total_metrics"] == 0


def test_get_performance_monitor_singleton() -> None:
    first = get_performance_monitor()
    second = get_performance_monitor()
    assert first is second


def test_measure_performance_success_and_failure() -> None:
    monitor = PerformanceMonitor()
    with measure_performance("ok_op", metadata={"m": 1}, monitor=monitor):
        pass
    with pytest.raises(ValueError):
        with measure_performance("bad_op", monitor=monitor):
            raise ValueError("fail")
    assert monitor.get_operation_stats("ok_op") is not None
    failed = monitor.get_failed_operations()
    assert any(m.operation == "bad_op" for m in failed)


def test_operation_stats_drop_metrics_evicted_from_primary_history() -> None:
    monitor = PerformanceMonitor(max_metrics=3, alert_threshold_ms=10_000.0)
    monitor.record_metric("old", 1.0)
    monitor.record_metric("keep", 1.0)
    monitor.record_metric("keep", 1.0)
    monitor.record_metric("keep", 1.0)
    assert len(monitor.metrics) == 3
    assert all(metric.operation == "keep" for metric in monitor.metrics)
    assert "old" not in monitor.operation_stats
    assert sum(len(values) for values in monitor.operation_stats.values()) == 3


def test_module_level_helpers_use_global_monitor() -> None:
    monitor = get_performance_monitor()
    record_performance_metric("helper_op", 12.0, success=True)
    stats = monitor.get_operation_stats("helper_op")
    assert stats is not None
    assert stats.count == 1
    all_stats = monitor.get_all_stats()
    assert "helper_op" in all_stats
    reset_performance_metrics()
    assert monitor.get_operation_stats("helper_op") is None
