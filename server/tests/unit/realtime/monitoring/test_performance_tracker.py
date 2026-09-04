"""Unit tests for PerformanceTracker."""

from unittest.mock import patch

from server.realtime.monitoring.performance_tracker import PerformanceTracker


def test_record_events_increase_counters():
    """Recording events updates totals and sample lists."""
    tracker = PerformanceTracker(max_samples=5)
    tracker.record_connection_establishment("websocket", 10.0)
    tracker.record_connection_establishment("sse", 20.0)
    tracker.record_message_delivery("chat", 5.0)
    tracker.record_disconnection("websocket", 3.0)
    tracker.record_session_switch(2.0)
    tracker.record_health_check(1.0)

    stats = tracker.performance_stats
    assert stats["total_connections_established"] == 2
    assert stats["total_messages_delivered"] == 1
    assert stats["total_disconnections"] == 1
    assert stats["total_session_switches"] == 1
    assert stats["total_health_checks"] == 1


def test_trim_samples_keeps_max_samples():
    """Samples beyond max_samples are trimmed from the front."""
    tracker = PerformanceTracker(max_samples=3)
    for i in range(5):
        tracker.record_message_delivery("chat", float(i))
    assert len(tracker.performance_stats["message_delivery_times"]) == 3
    assert tracker.performance_stats["message_delivery_times"][0][1] == 2.0


def test_get_stats_empty_returns_zeros():
    """Empty tracker returns zero averages."""
    tracker = PerformanceTracker()
    result = tracker.get_stats()
    assert result["connection_establishment"]["total_connections"] == 0
    assert result["connection_establishment"]["avg_websocket_establishment_ms"] == 0.0
    assert result["message_delivery"]["avg_delivery_time_ms"] == 0.0
    assert "timestamp" in result


def test_get_stats_calculates_averages():
    """get_stats computes min/max/avg for recorded metrics."""
    tracker = PerformanceTracker()
    tracker.record_connection_establishment("websocket", 10.0)
    tracker.record_connection_establishment("websocket", 30.0)
    tracker.record_message_delivery("chat", 5.0)
    tracker.record_message_delivery("chat", 15.0)
    tracker.record_disconnection("websocket", 4.0)
    tracker.record_session_switch(2.0)
    tracker.record_session_switch(8.0)
    tracker.record_health_check(1.0)

    result = tracker.get_stats()
    assert result["connection_establishment"]["websocket_connections"] == 2
    assert result["connection_establishment"]["avg_websocket_establishment_ms"] == 20.0
    assert result["message_delivery"]["max_delivery_time_ms"] == 15.0
    assert result["disconnections"]["avg_disconnection_time_ms"] == 4.0
    assert result["session_management"]["min_session_switch_time_ms"] == 2.0
    assert result["health_monitoring"]["avg_health_check_time_ms"] == 1.0


def test_get_stats_non_websocket_connections_excluded_from_websocket_stats():
    """Only websocket connection types count toward websocket stats."""
    tracker = PerformanceTracker()
    tracker.record_connection_establishment("sse", 100.0)
    result = tracker.get_stats()
    assert result["connection_establishment"]["websocket_connections"] == 0
    assert result["connection_establishment"]["total_connections"] == 1


def test_get_stats_error_path_returns_error_dict():
    """Exception during stats calculation returns error payload."""
    tracker = PerformanceTracker()
    tracker.record_connection_establishment("websocket", 1.0)
    with patch("server.realtime.monitoring.performance_tracker.np.array", side_effect=RuntimeError("boom")):
        result = tracker.get_stats()
    assert "error" in result
    assert "timestamp" in result
