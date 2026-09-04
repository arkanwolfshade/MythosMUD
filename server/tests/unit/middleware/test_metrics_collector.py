"""Unit tests for MetricsCollector."""

from __future__ import annotations

from server.middleware.metrics_collector import MetricsCollector


def test_record_and_get_metrics():
    collector = MetricsCollector()
    collector.record_message_processed("chat")
    collector.record_message_failed("chat", "timeout")
    collector.record_message_retried("chat", attempt=2)
    collector.record_message_dlq("chat")
    collector.record_circuit_state_change("closed", "open", reason="failures")
    collector.record_processing_time(12.5)

    metrics = collector.get_metrics()
    assert metrics["messages"]["total_processed"] >= 1
    assert metrics["messages"]["total_failed"] >= 1
    assert metrics["circuit_breaker"]["open_count"] == 1
    assert metrics["performance"]["avg_ms"] == 12.5


def test_get_summary():
    collector = MetricsCollector()
    collector.record_message_processed("system")
    summary = collector.get_summary()
    assert summary["messages_processed"] >= 1
    assert "uptime_seconds" in summary


def test_reset_metrics():
    collector = MetricsCollector()
    collector.record_message_processed("x")
    collector.reset_metrics()
    assert collector.get_summary()["messages_processed"] == 0


def test_circuit_state_change_trims_history():
    collector = MetricsCollector()
    for i in range(105):
        collector.record_circuit_state_change("closed", "open", reason=str(i))
    metrics = collector.get_metrics()
    assert len(metrics["circuit_breaker"]["recent_state_changes"]) <= 10
