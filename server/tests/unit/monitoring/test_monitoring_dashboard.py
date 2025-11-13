from __future__ import annotations

from server.monitoring.monitoring_dashboard import MonitoringDashboard


def test_record_registry_failure_sets_metadata():
    dashboard = MonitoringDashboard()
    alert = dashboard.record_registry_failure(
        source="prototype_registry",
        error="validation_error",
        metadata={"file_path": "/tmp/prototype.json"},
    )

    assert alert.alert_type == "prototype_registry_failure"
    assert alert.metadata["source"] == "prototype_registry"
    assert alert.metadata["file_path"] == "/tmp/prototype.json"
    assert alert.metadata["error"] == "validation_error"


def test_record_summon_quantity_spike_respects_thresholds():
    dashboard = MonitoringDashboard()

    warning_quantity = int(dashboard.alert_thresholds["summon_quantity_warning"])
    warning_alert = dashboard.record_summon_quantity_spike(
        admin_name="Armitage",
        prototype_id="artifact.miskatonic.codex",
        quantity=warning_quantity,
    )
    assert warning_alert.severity in {"warning", "critical"}

    critical_quantity = int(dashboard.alert_thresholds["summon_quantity_critical"])
    critical_alert = dashboard.record_summon_quantity_spike(
        admin_name="Armitage",
        prototype_id="artifact.miskatonic.codex",
        quantity=critical_quantity,
    )
    assert critical_alert.severity == "critical"
    assert critical_alert.metadata["quantity"] == critical_quantity


def test_record_durability_anomaly_marks_warning():
    dashboard = MonitoringDashboard()
    alert = dashboard.record_durability_anomaly(
        prototype_id="artifact.miskatonic.codex",
        durability=None,
        reason="missing_durability_value",
        metadata={"file_path": "artifact.json"},
    )

    assert alert.alert_type == "durability_anomaly"
    assert alert.severity == "warning"
    assert alert.metadata["reason"] == "missing_durability_value"
    assert alert.metadata["file_path"] == "artifact.json"
