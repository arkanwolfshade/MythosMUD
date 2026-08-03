"""Unit tests for MemoryMonitor."""

import time
from unittest.mock import MagicMock, patch

from server.realtime.memory_monitor import MemoryMonitor, _max_connection_age_seconds


def test_max_connection_age_local() -> None:
    with patch.dict("os.environ", {"LOGGING_ENVIRONMENT": "local"}):
        assert _max_connection_age_seconds() == 1800


def test_max_connection_age_default() -> None:
    with patch.dict("os.environ", {"LOGGING_ENVIRONMENT": "prod"}, clear=False):
        assert _max_connection_age_seconds() == 300


def test_should_cleanup_time_based() -> None:
    monitor = MemoryMonitor()
    monitor.last_cleanup_time = 0.0
    monitor.cleanup_interval = 1
    with patch.object(monitor, "get_memory_usage", return_value=0.1):
        assert monitor.should_cleanup() is True


def test_should_cleanup_memory_threshold() -> None:
    monitor = MemoryMonitor()
    monitor.last_cleanup_time = time.time()
    with patch.object(monitor, "get_memory_usage", return_value=0.85):
        assert monitor.should_cleanup() is True


def test_get_memory_usage_success() -> None:
    monitor = MemoryMonitor()
    process = MagicMock()
    process.memory_percent.return_value = 42.0
    with patch("server.realtime.memory_monitor.psutil.Process", return_value=process):
        assert monitor.get_memory_usage() == 0.42


def test_get_memory_usage_error_returns_zero() -> None:
    monitor = MemoryMonitor()
    with patch("server.realtime.memory_monitor.psutil.Process", side_effect=OSError("fail")):
        assert monitor.get_memory_usage() == 0.0


def test_get_memory_stats() -> None:
    monitor = MemoryMonitor()
    process = MagicMock()
    process.memory_info.return_value = MagicMock(rss=1024 * 1024, vms=2048 * 1024)
    process.memory_percent.return_value = 10.0
    vm = MagicMock(available=512 * 1024 * 1024, total=1024 * 1024 * 1024)
    with (
        patch("server.realtime.memory_monitor.psutil.Process", return_value=process),
        patch("server.realtime.memory_monitor.psutil.virtual_memory", return_value=vm),
    ):
        stats = monitor.get_memory_stats()
    assert stats["rss_mb"] == 1.0
    assert stats["percent"] == 10.0


def test_get_memory_alerts() -> None:
    monitor = MemoryMonitor()
    with patch.object(monitor, "get_memory_usage", return_value=0.91):
        alerts = monitor.get_memory_alerts(
            {"connection_attempts": 2000, "pending_messages": 2000, "stale_connections": 2}
        )
    assert any("CRITICAL" in alert for alert in alerts)
    assert any("rate limit" in alert.lower() for alert in alerts)


def test_update_cleanup_time_and_gc() -> None:
    monitor = MemoryMonitor()
    monitor.update_cleanup_time()
    assert monitor.last_cleanup_time > 0
    monitor.force_garbage_collection()


def test_should_cleanup_returns_false() -> None:
    monitor = MemoryMonitor()
    monitor.last_cleanup_time = time.time()
    with patch.object(monitor, "get_memory_usage", return_value=0.1):
        assert monitor.should_cleanup() is False


def test_max_connection_age_e2e() -> None:
    with patch.dict("os.environ", {"LOGGING_ENVIRONMENT": "e2e_test"}):
        assert _max_connection_age_seconds() == 1800


def test_get_memory_stats_error_returns_empty() -> None:
    monitor = MemoryMonitor()
    with patch("server.realtime.memory_monitor.psutil.Process", side_effect=OSError("fail")):
        assert monitor.get_memory_stats() == {}


def test_get_memory_alerts_warning_and_info_levels() -> None:
    monitor = MemoryMonitor()
    with patch.object(monitor, "get_memory_usage", return_value=0.75):
        alerts = monitor.get_memory_alerts({})
    assert any("INFO" in a for a in alerts)
    with patch.object(monitor, "get_memory_usage", return_value=0.82):
        alerts = monitor.get_memory_alerts({})
    assert any("WARNING" in a for a in alerts)


def test_get_memory_alerts_error_path() -> None:
    monitor = MemoryMonitor()
    with patch.object(monitor, "get_memory_usage", side_effect=RuntimeError("boom")):
        alerts = monitor.get_memory_alerts({})
    assert any("ERROR" in a for a in alerts)


def test_force_garbage_collection_runtime_error() -> None:
    monitor = MemoryMonitor()
    with patch("server.realtime.memory_monitor.gc.collect", side_effect=RuntimeError("gc fail")):
        monitor.force_garbage_collection()


def test_get_memory_usage_invalid_type() -> None:
    monitor = MemoryMonitor()
    process = MagicMock()
    process.memory_percent.return_value = "bad"
    with patch("server.realtime.memory_monitor.psutil.Process", return_value=process):
        assert monitor.get_memory_usage() == 0.0
