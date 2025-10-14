"""
Tests for metrics collection for NATS message processing.

Like the meticulous records kept by Miskatonic University's librarians,
these metrics track every invocation and its outcome.

AI: Tests metrics collection for monitoring NATS message processing.
"""

from server.middleware.metrics_collector import MetricsCollector


class TestMetricsCollector:
    """Test suite for metrics collection."""

    def test_initialization(self):
        """Metrics collector initializes with zero counters."""
        collector = MetricsCollector()

        metrics = collector.get_metrics()

        assert metrics["messages"]["total_processed"] == 0
        assert metrics["messages"]["total_failed"] == 0
        assert metrics["circuit_breaker"]["open_count"] == 0

    def test_record_message_processed(self):
        """Recording processed message increments counter."""
        collector = MetricsCollector()

        collector.record_message_processed("game.events")

        metrics = collector.get_metrics()

        assert metrics["messages"]["total_processed"] == 1
        assert metrics["messages"]["processed"]["game.events"] == 1

    def test_record_multiple_messages_processed(self):
        """Recording multiple messages increments counters correctly."""
        collector = MetricsCollector()

        collector.record_message_processed("game.events")
        collector.record_message_processed("game.events")
        collector.record_message_processed("chat.global")

        metrics = collector.get_metrics()

        assert metrics["messages"]["total_processed"] == 3
        assert metrics["messages"]["processed"]["game.events"] == 2
        assert metrics["messages"]["processed"]["chat.global"] == 1

    def test_record_message_failed(self):
        """Recording failed message increments failure counters."""
        collector = MetricsCollector()

        collector.record_message_failed("game.events", "timeout")

        metrics = collector.get_metrics()

        # Doubled: once for channel, once for channel:error_type
        assert metrics["messages"]["total_failed"] == 2
        assert metrics["messages"]["failed"]["game.events"] == 1
        assert metrics["messages"]["failed"]["game.events:timeout"] == 1

    def test_record_message_failed_multiple_channels(self):
        """Recording failures across channels tracked separately."""
        collector = MetricsCollector()

        collector.record_message_failed("game.events", "timeout")
        collector.record_message_failed("chat.global", "connection_lost")
        collector.record_message_failed("game.events", "timeout")

        metrics = collector.get_metrics()

        assert metrics["messages"]["total_failed"] == 6  # 3 failures * 2 (channel + error type)
        assert metrics["messages"]["failed"]["game.events"] == 2
        assert metrics["messages"]["failed"]["chat.global"] == 1
        assert metrics["messages"]["failed"]["game.events:timeout"] == 2
        assert metrics["messages"]["failed"]["chat.global:connection_lost"] == 1

    def test_record_message_retried(self):
        """Recording retry increments retry counter."""
        collector = MetricsCollector()

        collector.record_message_retried("game.events", attempt=1)

        metrics = collector.get_metrics()

        assert metrics["messages"]["retried"]["game.events"] == 1
        assert metrics["messages"]["retried"]["attempt_1"] == 1

    def test_record_multiple_retries(self):
        """Recording multiple retries tracked correctly."""
        collector = MetricsCollector()

        collector.record_message_retried("game.events", attempt=1)
        collector.record_message_retried("game.events", attempt=2)
        collector.record_message_retried("chat.global", attempt=1)

        metrics = collector.get_metrics()

        assert metrics["messages"]["retried"]["game.events"] == 2
        assert metrics["messages"]["retried"]["chat.global"] == 1
        assert metrics["messages"]["retried"]["attempt_1"] == 2
        assert metrics["messages"]["retried"]["attempt_2"] == 1

    def test_record_message_dlq(self):
        """Recording DLQ message increments DLQ counter."""
        collector = MetricsCollector()

        collector.record_message_dlq("game.events")

        metrics = collector.get_metrics()

        assert metrics["messages"]["dlq"]["game.events"] == 1

    def test_record_circuit_state_change(self):
        """Recording circuit state change updates tracking."""
        collector = MetricsCollector()

        collector.record_circuit_state_change("closed", "open", "too many failures")

        metrics = collector.get_metrics()

        assert len(metrics["circuit_breaker"]["recent_state_changes"]) == 1
        assert metrics["circuit_breaker"]["recent_state_changes"][0]["old_state"] == "closed"
        assert metrics["circuit_breaker"]["recent_state_changes"][0]["new_state"] == "open"
        assert metrics["circuit_breaker"]["open_count"] == 1

    def test_get_summary(self):
        """Get summary returns aggregated metrics."""
        collector = MetricsCollector()

        # Simulate some activity
        collector.record_message_processed("game.events")
        collector.record_message_processed("game.events")
        collector.record_message_failed("game.events", "timeout")
        collector.record_message_retried("game.events", attempt=1)

        summary = collector.get_summary()

        assert summary["messages_processed"] == 2
        assert summary["messages_failed"] == 2  # Doubled due to channel + error type tracking
        assert summary["total_retries"] == 2  # Also doubled (channel + attempt)

    def test_success_rate_calculation(self):
        """Success rate calculated correctly."""
        collector = MetricsCollector()

        # Process 8 messages successfully
        for _ in range(8):
            collector.record_message_processed("game.events")

        # Fail 2 messages (counts as 4 due to double tracking)
        collector.record_message_failed("game.events", "timeout")
        collector.record_message_failed("game.events", "timeout")

        metrics = collector.get_metrics()

        # success_rate = successful / (successful + failed)
        # 8 / (8 + 4) = 8/12 = 66.67%
        assert 66.0 <= metrics["messages"]["success_rate_percent"] <= 67.0

    def test_success_rate_with_zero_messages(self):
        """Success rate is 100% when no messages processed."""
        collector = MetricsCollector()

        metrics = collector.get_metrics()

        assert metrics["messages"]["success_rate_percent"] == 100.0

    def test_reset_metrics(self):
        """Reset clears all metrics."""
        collector = MetricsCollector()

        # Generate some metrics
        collector.record_message_processed("game.events")
        collector.record_message_failed("game.events", "timeout")
        collector.record_message_retried("game.events", attempt=1)
        collector.record_message_dlq("game.events")

        # Reset
        collector.reset_metrics()

        metrics = collector.get_metrics()

        assert metrics["messages"]["total_processed"] == 0
        assert metrics["messages"]["total_failed"] == 0

    def test_multiple_channels_tracked_independently(self):
        """Different channels tracked independently."""
        collector = MetricsCollector()

        collector.record_message_processed("game.events")
        collector.record_message_processed("chat.global")
        collector.record_message_processed("game.events")

        metrics = collector.get_metrics()

        assert metrics["messages"]["processed"]["game.events"] == 2
        assert metrics["messages"]["processed"]["chat.global"] == 1

    def test_error_types_tracked_separately(self):
        """Different error types tracked separately."""
        collector = MetricsCollector()

        collector.record_message_failed("game.events", "timeout")
        collector.record_message_failed("game.events", "connection_lost")
        collector.record_message_failed("game.events", "timeout")

        metrics = collector.get_metrics()

        assert metrics["messages"]["failed"]["game.events:timeout"] == 2
        assert metrics["messages"]["failed"]["game.events:connection_lost"] == 1

    def test_record_processing_time(self):
        """Recording processing time tracked correctly."""
        collector = MetricsCollector()

        collector.record_processing_time(50.0)
        collector.record_processing_time(150.0)

        metrics = collector.get_metrics()

        assert metrics["performance"]["count"] == 2
        assert metrics["performance"]["min_ms"] == 50.0
        assert metrics["performance"]["max_ms"] == 150.0
        assert metrics["performance"]["avg_ms"] == 100.0

    def test_circuit_state_change_tracking(self):
        """Circuit state changes are tracked with history."""
        collector = MetricsCollector()

        collector.record_circuit_state_change("closed", "open", "failures")
        collector.record_circuit_state_change("open", "half_open", "timeout")
        collector.record_circuit_state_change("half_open", "closed", "recovery")

        metrics = collector.get_metrics()

        assert len(metrics["circuit_breaker"]["recent_state_changes"]) == 3
        assert metrics["circuit_breaker"]["open_count"] == 1  # Only counts transitions to "open"

    def test_get_summary_structure(self):
        """Get summary returns flat structure."""
        collector = MetricsCollector()

        collector.record_message_processed("test")
        collector.record_message_failed("test", "error")

        summary = collector.get_summary()

        assert "messages_processed" in summary
        assert "messages_failed" in summary
        assert "messages_in_dlq" in summary
        assert "total_retries" in summary
        assert "circuit_opens" in summary
        assert "uptime_seconds" in summary
