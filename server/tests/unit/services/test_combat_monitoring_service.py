"""
Unit tests for combat monitoring service.

Tests the CombatMonitoringService class for monitoring combat system health,
performance metrics, and automated alerting.
"""

import time
from unittest.mock import MagicMock, patch

import pytest

from server.services.combat_monitoring_service import (
    AlertSeverity,
    AlertType,
    CombatMetrics,
    CombatMonitoringService,
    get_combat_metrics,
    get_combat_monitoring,
)


@pytest.fixture
def mock_config():
    """Create mock config."""
    mock = MagicMock()
    mock.game.combat_performance_threshold = 1000  # 1000ms
    mock.game.combat_error_threshold = 10
    mock.game.combat_alert_threshold = 5
    return mock


@pytest.fixture
def mock_feature_flags():
    """Create mock feature flags."""
    mock = MagicMock()
    mock.is_combat_monitoring_enabled.return_value = True
    return mock


@pytest.fixture
def mock_combat_config():
    """Create mock combat config."""
    return MagicMock()


@pytest.fixture
def monitoring_service(mock_config, mock_feature_flags, mock_combat_config):
    """Create CombatMonitoringService instance with mocked dependencies."""
    with patch("server.services.combat_monitoring_service.get_config", return_value=mock_config):
        with patch("server.services.combat_monitoring_service.get_feature_flags", return_value=mock_feature_flags):
            with patch("server.services.combat_monitoring_service.get_combat_config", return_value=mock_combat_config):
                service = CombatMonitoringService()
                return service


def test_combat_monitoring_service_init(monitoring_service):
    """Test CombatMonitoringService initialization."""
    assert monitoring_service._metrics is not None
    assert isinstance(monitoring_service._metrics, CombatMetrics)
    assert monitoring_service._performance_threshold == 1000


def test_start_combat_monitoring(monitoring_service):
    """Test start_combat_monitoring tracks combat."""
    combat_id = "combat_001"
    monitoring_service.start_combat_monitoring(combat_id)

    assert combat_id in monitoring_service._combat_start_times
    assert monitoring_service._metrics.total_combats == 1
    assert monitoring_service._metrics.active_combats == 1


def test_start_combat_monitoring_disabled(mock_config, mock_feature_flags, mock_combat_config):
    """Test start_combat_monitoring when monitoring is disabled."""
    mock_feature_flags.is_combat_monitoring_enabled.return_value = False
    with patch("server.services.combat_monitoring_service.get_config", return_value=mock_config):
        with patch("server.services.combat_monitoring_service.get_feature_flags", return_value=mock_feature_flags):
            with patch("server.services.combat_monitoring_service.get_combat_config", return_value=mock_combat_config):
                service = CombatMonitoringService()
                service.start_combat_monitoring("combat_001")

                assert "combat_001" not in service._combat_start_times
                assert service._metrics.total_combats == 0


def test_end_combat_monitoring_success(monitoring_service):
    """Test end_combat_monitoring with successful combat."""
    combat_id = "combat_001"
    monitoring_service.start_combat_monitoring(combat_id)
    time.sleep(0.01)  # Small delay to ensure duration > 0

    monitoring_service.end_combat_monitoring(combat_id, success=True)

    assert combat_id not in monitoring_service._combat_start_times
    assert monitoring_service._metrics.active_combats == 0
    assert monitoring_service._metrics.completed_combats == 1
    assert monitoring_service._metrics.failed_combats == 0


def test_end_combat_monitoring_failure(monitoring_service):
    """Test end_combat_monitoring with failed combat."""
    combat_id = "combat_001"
    monitoring_service.start_combat_monitoring(combat_id)

    monitoring_service.end_combat_monitoring(combat_id, success=False)

    assert monitoring_service._metrics.completed_combats == 0
    assert monitoring_service._metrics.failed_combats == 1


def test_end_combat_monitoring_not_found(monitoring_service):
    """Test end_combat_monitoring when combat not found."""
    # Should not raise, just log warning
    monitoring_service.end_combat_monitoring("nonexistent")


def test_start_turn_monitoring(monitoring_service):
    """Test start_turn_monitoring tracks turn."""
    combat_id = "combat_001"
    monitoring_service.start_turn_monitoring(combat_id)

    assert combat_id in monitoring_service._turn_start_times


def test_end_turn_monitoring(monitoring_service):
    """Test end_turn_monitoring updates metrics."""
    combat_id = "combat_001"
    monitoring_service.start_combat_monitoring(combat_id)
    monitoring_service.start_turn_monitoring(combat_id)
    time.sleep(0.01)

    monitoring_service.end_turn_monitoring(combat_id)

    assert combat_id not in monitoring_service._turn_start_times


def test_end_turn_monitoring_not_found(monitoring_service):
    """Test end_turn_monitoring when turn not found."""
    # Should not raise, just log warning
    monitoring_service.end_turn_monitoring("nonexistent")


def test_record_combat_error_validation(monitoring_service):
    """Test record_combat_error with validation error."""
    monitoring_service.record_combat_error("validation", "combat_001")

    assert monitoring_service._metrics.total_errors == 1
    assert monitoring_service._metrics.validation_errors == 1


def test_record_combat_error_timeout(monitoring_service):
    """Test record_combat_error with timeout error."""
    monitoring_service.record_combat_error("timeout", "combat_001")

    assert monitoring_service._metrics.total_errors == 1
    assert monitoring_service._metrics.timeout_errors == 1


def test_record_combat_error_system(monitoring_service):
    """Test record_combat_error with system error."""
    monitoring_service.record_combat_error("system", "combat_001")

    assert monitoring_service._metrics.total_errors == 1
    assert monitoring_service._metrics.system_errors == 1


def test_record_combat_error_disabled(mock_config, mock_feature_flags, mock_combat_config):
    """Test record_combat_error when monitoring is disabled."""
    mock_feature_flags.is_combat_monitoring_enabled.return_value = False
    with patch("server.services.combat_monitoring_service.get_config", return_value=mock_config):
        with patch("server.services.combat_monitoring_service.get_feature_flags", return_value=mock_feature_flags):
            with patch("server.services.combat_monitoring_service.get_combat_config", return_value=mock_combat_config):
                service = CombatMonitoringService()
                service.record_combat_error("validation", "combat_001")

                assert service._metrics.total_errors == 0


def test_update_resource_metrics(monitoring_service):
    """Test update_resource_metrics updates metrics."""
    monitoring_service.update_resource_metrics(50.0, 25.0)

    assert monitoring_service._metrics.memory_usage_mb == 50.0
    assert monitoring_service._metrics.cpu_usage_percent == 25.0


def test_get_current_metrics(monitoring_service):
    """Test get_current_metrics returns metrics."""
    metrics = monitoring_service.get_current_metrics()
    assert isinstance(metrics, CombatMetrics)


def test_get_metrics_history(monitoring_service):
    """Test get_metrics_history returns history."""
    history = monitoring_service.get_metrics_history()
    assert isinstance(history, list)


def test_get_metrics_history_with_limit(monitoring_service):
    """Test get_metrics_history with limit."""
    # Add some snapshots
    for _ in range(5):
        monitoring_service._save_metrics_snapshot()

    history = monitoring_service.get_metrics_history(limit=3)
    assert len(history) == 3


def test_add_alert_callback(monitoring_service):
    """Test add_alert_callback adds callback."""
    callback = MagicMock()
    monitoring_service.add_alert_callback(callback)

    assert callback in monitoring_service._alert_callbacks


def test_remove_alert_callback(monitoring_service):
    """Test remove_alert_callback removes callback."""
    callback = MagicMock()
    monitoring_service.add_alert_callback(callback)
    monitoring_service.remove_alert_callback(callback)

    assert callback not in monitoring_service._alert_callbacks


def test_get_active_alerts(monitoring_service):
    """Test get_active_alerts returns unresolved alerts."""
    # Generate an alert
    alert = monitoring_service._generate_alert(AlertType.ERROR, AlertSeverity.HIGH, "Test Alert", "Test message")

    active_alerts = monitoring_service.get_active_alerts()
    assert len(active_alerts) == 1
    assert active_alerts[0]["alert_id"] == alert.alert_id


def test_get_all_alerts(monitoring_service):
    """Test get_all_alerts returns all alerts."""
    monitoring_service._generate_alert(AlertType.ERROR, AlertSeverity.HIGH, "Alert 1", "Message 1")
    monitoring_service._generate_alert(AlertType.PERFORMANCE, AlertSeverity.MEDIUM, "Alert 2", "Message 2")

    all_alerts = monitoring_service.get_all_alerts()
    assert len(all_alerts) == 2


def test_resolve_alert(monitoring_service):
    """Test resolve_alert resolves an alert."""
    alert = monitoring_service._generate_alert(AlertType.ERROR, AlertSeverity.HIGH, "Test Alert", "Test message")

    result = monitoring_service.resolve_alert(alert.alert_id)

    assert result is True
    assert alert.resolved is True
    assert alert.resolved_timestamp is not None


def test_resolve_alert_not_found(monitoring_service):
    """Test resolve_alert returns False when alert not found."""
    result = monitoring_service.resolve_alert("nonexistent")

    assert result is False


def test_clear_resolved_alerts(monitoring_service):
    """Test clear_resolved_alerts removes resolved alerts."""
    alert1 = monitoring_service._generate_alert(AlertType.ERROR, AlertSeverity.HIGH, "Alert 1", "Message 1")
    alert2 = monitoring_service._generate_alert(AlertType.PERFORMANCE, AlertSeverity.MEDIUM, "Alert 2", "Message 2")

    monitoring_service.resolve_alert(alert1.alert_id)
    cleared = monitoring_service.clear_resolved_alerts()

    assert cleared == 1
    assert len(monitoring_service._alerts) == 1
    assert alert2.alert_id in monitoring_service._alerts


def test_get_monitoring_summary(monitoring_service):
    """Test get_monitoring_summary returns summary."""
    summary = monitoring_service.get_monitoring_summary()

    assert "metrics" in summary
    assert "active_alerts" in summary
    assert "total_alerts" in summary
    assert "monitoring_enabled" in summary
    assert "thresholds" in summary
    assert "resource_usage" in summary


def test_check_error_threshold(monitoring_service):
    """Test _check_error_threshold generates alert when exceeded."""
    # Set error count to threshold
    monitoring_service._metrics.total_errors = 10
    monitoring_service._error_threshold = 10

    monitoring_service._check_error_threshold()

    active_alerts = monitoring_service.get_active_alerts()
    assert len(active_alerts) == 1
    assert active_alerts[0]["alert_type"] == AlertType.ERROR.value


def test_check_resource_thresholds_memory(monitoring_service):
    """Test _check_resource_thresholds generates alert for high memory."""
    monitoring_service._metrics.memory_usage_mb = 150.0

    monitoring_service._check_resource_thresholds()

    active_alerts = monitoring_service.get_active_alerts()
    assert len(active_alerts) == 1
    assert active_alerts[0]["alert_type"] == AlertType.PERFORMANCE.value


def test_check_resource_thresholds_cpu(monitoring_service):
    """Test _check_resource_thresholds generates alert for high CPU."""
    monitoring_service._metrics.cpu_usage_percent = 85.0

    monitoring_service._check_resource_thresholds()

    active_alerts = monitoring_service.get_active_alerts()
    assert len(active_alerts) == 1
    assert active_alerts[0]["alert_type"] == AlertType.PERFORMANCE.value


def test_check_performance_threshold(monitoring_service):
    """Test _check_performance_threshold generates alert when exceeded."""
    # Set average duration above threshold (threshold is in ms, duration in seconds)
    monitoring_service._metrics.average_combat_duration = 2.0  # 2 seconds = 2000ms
    monitoring_service._performance_threshold = 1000  # 1000ms

    monitoring_service._check_performance_threshold()

    active_alerts = monitoring_service.get_active_alerts()
    assert len(active_alerts) == 1


def test_generate_alert(monitoring_service):
    """Test _generate_alert creates and dispatches alert."""
    callback = MagicMock()
    monitoring_service.add_alert_callback(callback)

    alert = monitoring_service._generate_alert(
        AlertType.ERROR, AlertSeverity.HIGH, "Test Alert", "Test message", {"key": "value"}
    )

    assert alert.alert_type == AlertType.ERROR
    assert alert.severity == AlertSeverity.HIGH
    assert alert.title == "Test Alert"
    assert alert.message == "Test message"
    assert alert.metadata == {"key": "value"}
    callback.assert_called_once_with(alert)


def test_generate_alert_callback_error(monitoring_service):
    """Test _generate_alert handles callback errors gracefully."""
    callback = MagicMock(side_effect=Exception("Callback error"))
    monitoring_service.add_alert_callback(callback)

    # Should not raise
    alert = monitoring_service._generate_alert(AlertType.ERROR, AlertSeverity.HIGH, "Test Alert", "Test message")

    assert alert is not None


def test_save_metrics_snapshot(monitoring_service):
    """Test _save_metrics_snapshot saves snapshot."""
    monitoring_service._metrics.total_combats = 10
    monitoring_service._save_metrics_snapshot()

    history = monitoring_service.get_metrics_history()
    assert len(history) == 1
    assert history[0]["total_combats"] == 10


def test_refresh_configuration(monitoring_service, mock_config):
    """Test refresh_configuration updates thresholds."""
    mock_config.game.combat_performance_threshold = 2000
    mock_config.game.combat_error_threshold = 20

    with patch("server.services.combat_monitoring_service.get_config", return_value=mock_config):
        monitoring_service.refresh_configuration()

    assert monitoring_service._performance_threshold == 2000
    assert monitoring_service._error_threshold == 20


def test_get_combat_monitoring():
    """Test get_combat_monitoring returns global instance."""
    service = get_combat_monitoring()
    assert isinstance(service, CombatMonitoringService)


def test_get_combat_metrics():
    """Test get_combat_metrics returns metrics."""
    metrics = get_combat_metrics()
    assert isinstance(metrics, CombatMetrics)


def test_metrics_to_dict(monitoring_service):
    """Test CombatMetrics.to_dict converts to dictionary."""
    monitoring_service._metrics.total_combats = 5
    metrics_dict = monitoring_service._metrics.to_dict()

    assert isinstance(metrics_dict, dict)
    assert metrics_dict["total_combats"] == 5


def test_alert_to_dict(monitoring_service):
    """Test Alert.to_dict converts to dictionary."""
    alert = monitoring_service._generate_alert(AlertType.ERROR, AlertSeverity.HIGH, "Test Alert", "Test message")
    alert_dict = alert.to_dict()

    assert isinstance(alert_dict, dict)
    assert alert_dict["alert_type"] == AlertType.ERROR.value
    assert alert_dict["severity"] == AlertSeverity.HIGH.value
    assert alert_dict["title"] == "Test Alert"


def test_update_timing_metrics(monitoring_service):
    """Test _update_timing_metrics updates average and max duration."""
    # Simulate 1 completed combat with average 1.0, now adding second combat with duration 2.0
    # When _update_timing_metrics is called, completed_combats should be 2 (after increment)
    monitoring_service._metrics.completed_combats = 2
    monitoring_service._metrics.average_combat_duration = 1.0

    monitoring_service._update_timing_metrics(2.0)

    # Expected: (1.0 * (2-1) + 2.0) / 2 = (1.0 + 2.0) / 2 = 1.5
    assert monitoring_service._metrics.average_combat_duration == 1.5
    assert monitoring_service._metrics.max_combat_duration == 2.0


def test_update_turn_timing_metrics(monitoring_service):
    """Test _update_turn_timing_metrics updates average turn time."""
    # Simulate 1 combat with average 0.5, now adding second turn with duration 1.0
    # When _update_turn_timing_metrics is called, total_combats should be 2 (after increment)
    monitoring_service._metrics.total_combats = 2
    monitoring_service._metrics.average_turn_time = 0.5

    monitoring_service._update_turn_timing_metrics(1.0)

    # Expected: (0.5 * (2-1) + 1.0) / 2 = (0.5 + 1.0) / 2 = 0.75
    assert monitoring_service._metrics.average_turn_time == 0.75
