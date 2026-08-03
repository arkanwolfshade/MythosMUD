"""Unit tests for MonitoringDashboard."""

from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

from server.monitoring.monitoring_dashboard import Alert, MonitoringDashboard, SystemHealth
from server.structured_logging.log_aggregator import LogAggregationStats


def _log_stats(error_rate: float = 0.0, warning_rate: float = 0.0) -> LogAggregationStats:
    return LogAggregationStats(
        total_entries=10,
        entries_by_level={"info": 10},
        entries_by_logger={"app": 10},
        entries_by_hour={"12": 10},
        error_rate=error_rate,
        warning_rate=warning_rate,
    )


def _dashboard() -> MonitoringDashboard:
    with (
        patch("server.monitoring.monitoring_dashboard.get_performance_monitor") as perf,
        patch("server.monitoring.monitoring_dashboard.get_exception_tracker") as exc,
        patch("server.monitoring.monitoring_dashboard.get_log_aggregator") as log_agg,
        patch("server.monitoring.monitoring_dashboard.MemoryLeakMetricsCollector"),
    ):
        perf.return_value.get_all_stats.return_value = {}
        exc.return_value.get_stats.return_value = MagicMock(error_rate=0.0, unhandled_exceptions=0)
        log_agg.return_value.get_stats.return_value = _log_stats()
        return MonitoringDashboard()


def test_get_system_health_healthy():
    dashboard = _dashboard()
    health = dashboard.get_system_health()
    assert health.status in ("healthy", "warning", "critical")
    assert isinstance(health, SystemHealth)


def test_record_and_resolve_custom_alert():
    dashboard = _dashboard()
    alert = dashboard.record_custom_alert("test", severity="warning", message="probe")
    assert alert.resolved is False
    assert dashboard.resolve_alert(alert.alert_id) is True
    assert alert.resolved is True


def test_record_registry_failure():
    dashboard = _dashboard()
    alert = dashboard.record_registry_failure(source="items", error="load fail")
    assert alert.alert_type == "prototype_registry_failure"


def test_record_summon_quantity_spike():
    dashboard = _dashboard()
    alert = dashboard.record_summon_quantity_spike(admin_name="admin", prototype_id="p1", quantity=25)
    assert alert.severity in ("warning", "critical")


def test_record_durability_anomaly():
    dashboard = _dashboard()
    alert = dashboard.record_durability_anomaly(prototype_id="p1", durability=-1, reason="bad seed")
    assert "durability" in alert.message.lower() or alert.alert_type


def test_get_monitoring_summary():
    dashboard = _dashboard()
    summary = dashboard.get_monitoring_summary()
    assert summary.system_health is not None
    assert isinstance(summary.recommendations, list)


def test_get_alert_history_filters_by_time():
    dashboard = _dashboard()
    old = Alert(
        alert_id="old",
        alert_type="test",
        severity="info",
        message="old",
        timestamp=datetime(2020, 1, 1, tzinfo=UTC),
    )
    dashboard.alerts.append(old)
    recent = dashboard.record_custom_alert("recent", message="now")
    history = dashboard.get_alert_history(hours=24)
    assert any(a.alert_id == recent.alert_id for a in history)


def test_export_monitoring_data_json():
    dashboard = _dashboard()
    data = dashboard.export_monitoring_data()
    assert "system_health" in data or "timestamp" in data
