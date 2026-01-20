"""
Unit tests for memory leak metrics collector.

Tests the MemoryLeakMetricsCollector class for accurate metrics collection,
alerting thresholds, and performance.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.monitoring.memory_leak_metrics import MemoryLeakMetricsCollector

# pylint: disable=redefined-outer-name  # Reason: pytest fixtures are used as function parameters, which triggers this warning


@pytest.fixture
def collector():
    """Create a MemoryLeakMetricsCollector instance."""
    return MemoryLeakMetricsCollector()


def test_collector_initialization(collector):
    """Test MemoryLeakMetricsCollector initialization."""
    # pylint: disable=protected-access  # Reason: Tests need to verify internal state not exposed by public APIs
    assert collector._history.maxlen == 100
    assert "closed_websockets_max" in collector._alert_thresholds
    assert collector._alert_thresholds["closed_websockets_max"] == 5000


def test_collect_connection_metrics(collector):
    """Test collection of connection metrics."""
    with patch("server.realtime.connection_manager.resolve_connection_manager") as mock_resolve:
        mock_manager = MagicMock()
        mock_manager.get_memory_stats.return_value = {
            "connections": {
                "active_websockets_count": 10,
                "connection_metadata_count": 10,
                "player_websockets_count": 8,
                "closed_websockets_count": 100,
                "active_to_player_ratio": 1.25,
                "orphaned_connections": 2,
            }
        }
        mock_resolve.return_value = mock_manager

        metrics = collector.collect_connection_metrics()

        assert metrics["active_websockets_count"] == 10
        assert metrics["connection_metadata_count"] == 10
        assert metrics["player_websockets_count"] == 8
        assert metrics["closed_websockets_count"] == 100
        assert metrics["active_to_player_ratio"] == 1.25
        assert metrics["orphaned_connections"] == 2


def test_collect_connection_metrics_no_manager(collector):
    """Test collection of connection metrics when manager is not available."""
    with patch("server.realtime.connection_manager.resolve_connection_manager") as mock_resolve:
        mock_resolve.return_value = None

        metrics = collector.collect_connection_metrics()

        assert "error" in metrics


def test_collect_event_metrics(collector):
    """Test collection of event metrics."""
    with patch("server.container.ApplicationContainer") as mock_container_class:
        mock_container = MagicMock()
        mock_container_class.get_instance.return_value = mock_container
        mock_event_bus = MagicMock()
        mock_container.event_bus = mock_event_bus
        mock_event_bus.get_all_subscriber_counts.return_value = {"EventType1": 5, "EventType2": 3}
        mock_event_bus.get_subscriber_lifecycle_metrics.return_value = {
            "total_subscribers": 8,
            "subscription_churn_rate": 0.1,
        }
        mock_event_bus.get_active_task_count.return_value = 2
        mock_event_bus.get_subscriber_stats.return_value = {
            "services_tracked": 3,
            "tracked_subscriptions": 8,
        }

        metrics = collector.collect_event_metrics()

        assert metrics["total_subscribers"] == 8
        assert metrics["active_task_count"] == 2
        assert metrics["subscription_churn_rate"] == 0.1
        assert metrics["services_tracked"] == 3
        assert metrics["tracked_subscriptions"] == 8


def test_collect_event_metrics_no_bus(collector):
    """Test collection of event metrics when event bus is not available."""
    with patch("server.container.ApplicationContainer") as mock_container_class:
        mock_container = MagicMock()
        mock_container_class.get_instance.return_value = mock_container
        mock_container.event_bus = None

        metrics = collector.collect_event_metrics()

        assert "error" in metrics


def test_collect_cache_metrics(collector):
    """Test collection of cache metrics."""
    with patch("server.caching.lru_cache.get_cache_manager") as mock_get_cache:
        mock_cache_manager = MagicMock()
        mock_get_cache.return_value = mock_cache_manager
        mock_cache_manager.get_all_stats.return_value = {
            "rooms": {"size": 100, "capacity_utilization": 0.5, "expired_count": 10},
            "players": {"size": 50, "capacity_utilization": 0.8, "expired_count": 5},
        }

        metrics = collector.collect_cache_metrics()

        assert "cache_sizes" in metrics
        assert "capacity_utilization" in metrics
        assert "expired_entry_counts" in metrics
        assert metrics["cache_sizes"]["rooms"] == 100
        assert metrics["cache_sizes"]["players"] == 50
        assert metrics["capacity_utilization"]["rooms"] == 0.5
        assert metrics["capacity_utilization"]["players"] == 0.8
        assert metrics["expired_entry_counts"]["rooms"] == 10
        assert metrics["expired_entry_counts"]["players"] == 5


def test_collect_task_metrics(collector):
    """Test collection of task metrics."""
    with patch("server.app.task_registry.get_registry") as mock_get_registry:
        mock_registry = MagicMock()
        mock_get_registry.return_value = mock_registry
        mock_registry.get_task_lifecycle_metrics.return_value = {
            "active_task_count": 15,
            "tasks_by_type": {"background": 10, "periodic": 5},
            "task_creation_rate": 2.5,
            "task_completion_rate": 2.0,
            "orphaned_task_count": 1,
        }

        metrics = collector.collect_task_metrics()

        assert metrics["active_task_count"] == 15
        assert metrics["tasks_by_type"]["background"] == 10
        assert metrics["tasks_by_type"]["periodic"] == 5
        assert metrics["task_creation_rate"] == 2.5
        assert metrics["task_completion_rate"] == 2.0
        assert metrics["orphaned_task_count"] == 1


def test_collect_nats_metrics(collector):
    """Test collection of NATS metrics."""
    with patch("server.container.ApplicationContainer") as mock_container_class:
        mock_container = MagicMock()
        mock_container_class.get_instance.return_value = mock_container
        mock_nats_service = MagicMock()
        mock_container.nats_service = mock_nats_service
        mock_nats_service.get_active_subscriptions.return_value = ["subject1", "subject2", "subject3"]
        mock_nats_service._last_cleanup_time = 1234567890.0  # pylint: disable=protected-access  # Reason: Test needs to set internal state on mock object

        metrics = collector.collect_nats_metrics()

        assert metrics["subscription_count"] == 3
        assert len(metrics["active_subscriptions"]) == 3
        assert metrics["last_cleanup_time"] == 1234567890.0


def test_collect_all_metrics(collector):
    """Test collection of all metrics."""
    # pylint: disable=protected-access  # Reason: Tests need to verify internal state not exposed by public APIs
    with patch.object(collector, "collect_connection_metrics", return_value={"test": "connection"}):
        with patch.object(collector, "collect_event_metrics", return_value={"test": "event"}):
            with patch.object(collector, "collect_cache_metrics", return_value={"test": "cache"}):
                with patch.object(collector, "collect_task_metrics", return_value={"test": "task"}):
                    with patch.object(collector, "collect_nats_metrics", return_value={"test": "nats"}):
                        metrics = collector.collect_all_metrics()

                        assert "connection" in metrics
                        assert "event" in metrics
                        assert "cache" in metrics
                        assert "task" in metrics
                        assert "nats" in metrics
                        assert "timestamp" in metrics
                        assert len(collector._history) == 1


def test_calculate_growth_rates(collector):
    """Test calculation of growth rates."""
    # pylint: disable=protected-access  # Reason: Tests need to set internal state not exposed by public APIs
    # Add two metrics to history
    collector._history.append(
        {
            "connection": {"closed_websockets_count": 100},
            "event": {"total_subscribers": 10},
            "task": {"active_task_count": 20},
        }
    )
    collector._history.append(
        {
            "connection": {"closed_websockets_count": 150},
            "event": {"total_subscribers": 12},
            "task": {"active_task_count": 25},
        }
    )

    growth_rates = collector.calculate_growth_rates()

    assert "closed_websockets" in growth_rates
    assert "subscribers" in growth_rates
    assert "tasks" in growth_rates
    assert growth_rates["closed_websockets"] == 0.5  # (150-100)/100
    assert growth_rates["subscribers"] == 0.2  # (12-10)/10
    assert growth_rates["tasks"] == 0.25  # (25-20)/20


def test_calculate_growth_rates_insufficient_history(collector):
    """Test growth rate calculation with insufficient history."""
    # pylint: disable=protected-access  # Reason: Tests need to set internal state not exposed by public APIs
    # Add only one metric to history
    collector._history.append({"connection": {"closed_websockets_count": 100}})

    growth_rates = collector.calculate_growth_rates()

    assert growth_rates == {}


def test_check_alerts_closed_websockets_threshold(collector):
    """Test alert checking for closed websockets threshold."""
    metrics = {
        "connection": {"closed_websockets_count": 6000},  # Exceeds threshold of 5000
    }

    alerts = collector.check_alerts(metrics)

    assert len(alerts) > 0
    assert any("closed websockets" in alert.lower() for alert in alerts)
    assert any("6000" in alert for alert in alerts)


def test_check_alerts_subscriber_growth_rate(collector):
    """Test alert checking for subscriber growth rate."""
    # pylint: disable=protected-access  # Reason: Tests need to set internal state not exposed by public APIs
    metrics = {
        "event": {"total_subscribers": 12},
    }

    # Set up history for growth rate calculation
    collector._history.append({"event": {"total_subscribers": 10}})
    collector._history.append({"event": {"total_subscribers": 12}})

    alerts = collector.check_alerts(metrics)

    # Growth rate is 0.2 (20%), which exceeds threshold of 0.1 (10%)
    assert len(alerts) > 0
    assert any("subscriber" in alert.lower() for alert in alerts)


def test_check_alerts_cache_capacity(collector):
    """Test alert checking for cache capacity utilization."""
    metrics = {
        "cache": {
            "capacity_utilization": {
                "test_cache": 1.2,  # 120% exceeds threshold of 110%
            }
        }
    }

    alerts = collector.check_alerts(metrics)

    assert len(alerts) > 0
    assert any("cache" in alert.lower() for alert in alerts)
    assert any("test_cache" in alert for alert in alerts)


def test_check_alerts_task_growth_rate(collector):
    """Test alert checking for task growth rate."""
    # pylint: disable=protected-access  # Reason: Tests need to set internal state not exposed by public APIs
    metrics = {
        "task": {"active_task_count": 30},
    }

    # Set up history for growth rate calculation
    collector._history.append({"task": {"active_task_count": 20}})
    collector._history.append({"task": {"active_task_count": 30}})

    alerts = collector.check_alerts(metrics)

    # Growth rate is 0.5 (50%), which exceeds threshold of 0.2 (20%)
    assert len(alerts) > 0
    assert any("task" in alert.lower() for alert in alerts)


def test_check_alerts_no_alerts(collector):
    """Test alert checking when no thresholds are exceeded."""
    # pylint: disable=protected-access  # Reason: Tests need to set internal state not exposed by public APIs
    metrics = {
        "connection": {"closed_websockets_count": 100},  # Below threshold
        "event": {"total_subscribers": 10},
        "cache": {"capacity_utilization": {"test_cache": 0.5}},  # Below threshold
        "task": {"active_task_count": 20},
    }

    # Set up history with no growth
    collector._history.append({"event": {"total_subscribers": 10}})
    collector._history.append({"event": {"total_subscribers": 10}})
    collector._history.append({"task": {"active_task_count": 20}})
    collector._history.append({"task": {"active_task_count": 20}})

    alerts = collector.check_alerts(metrics)

    # Should have no alerts (or only informational)
    assert len([a for a in alerts if "WARNING" in a]) == 0


def test_metrics_collection_performance(collector):
    """Test that metrics collection doesn't significantly impact performance."""
    import time

    # Mock all dependencies
    with patch.object(collector, "collect_connection_metrics", return_value={}):
        with patch.object(collector, "collect_event_metrics", return_value={}):
            with patch.object(collector, "collect_cache_metrics", return_value={}):
                with patch.object(collector, "collect_task_metrics", return_value={}):
                    with patch.object(collector, "collect_nats_metrics", return_value={}):
                        start_time = time.time()
                        for _ in range(100):  # Collect metrics 100 times
                            collector.collect_all_metrics()
                        elapsed_time = time.time() - start_time

                        # Should complete 100 collections in less than 1 second
                        # (allowing margin for test environment variability)
                        assert elapsed_time < 1.0, f"Metrics collection took {elapsed_time}s, expected < 1.0s"


def test_metrics_history_bounded(collector):
    """Test that metrics history is bounded."""
    # pylint: disable=protected-access  # Reason: Tests need to set and verify internal state not exposed by public APIs
    # Add more metrics than maxlen
    for i in range(150):
        collector._history.append({"timestamp": i, "test": "data"})

    # History should be bounded at maxlen (100)
    assert len(collector._history) == 100
    # Oldest entries should be removed
    assert collector._history[0]["timestamp"] == 50  # First entry is now the 50th


def test_collect_all_metrics_error_handling(collector):
    """Test that metrics collection handles errors gracefully."""
    with patch.object(collector, "collect_connection_metrics", side_effect=Exception("Test error")):
        metrics = collector.collect_all_metrics()

        # Should return error dict instead of crashing
        assert "error" in metrics
        assert "timestamp" in metrics
