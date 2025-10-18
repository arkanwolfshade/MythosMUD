"""
Tests for combat monitoring service.

These tests verify that the combat monitoring service properly tracks
combat metrics, generates alerts, and provides reliable monitoring
capabilities.
"""

import time
from unittest.mock import MagicMock, patch

import pytest

from server.services.combat_monitoring_service import (
    Alert,
    AlertSeverity,
    AlertType,
    CombatMetrics,
    CombatMonitoringService,
    end_combat_monitoring,
    get_combat_metrics,
    get_combat_monitoring,
    record_combat_error,
    start_combat_monitoring,
)


@pytest.fixture
def mock_config():
    """Mock configuration for testing."""
    mock_config = MagicMock()
    mock_config.game.combat_performance_threshold = 1000
    mock_config.game.combat_error_threshold = 3
    mock_config.game.combat_alert_threshold = 5
    return mock_config


@pytest.fixture
def mock_feature_flags():
    """Mock feature flags for testing."""
    mock_flags = MagicMock()
    mock_flags.is_combat_monitoring_enabled.return_value = True
    return mock_flags


@pytest.fixture
def mock_combat_config():
    """Mock combat configuration for testing."""
    mock_config = MagicMock()
    return mock_config


class TestCombatMetrics:
    """Test CombatMetrics data class."""

    def test_combat_metrics_defaults(self):
        """Test default combat metrics values."""
        metrics = CombatMetrics()

        assert metrics.total_combats == 0
        assert metrics.active_combats == 0
        assert metrics.completed_combats == 0
        assert metrics.failed_combats == 0
        assert metrics.average_combat_duration == 0.0
        assert metrics.average_turn_time == 0.0
        assert metrics.max_combat_duration == 0.0
        assert metrics.total_errors == 0
        assert metrics.validation_errors == 0
        assert metrics.timeout_errors == 0
        assert metrics.system_errors == 0
        assert metrics.memory_usage_mb == 0.0
        assert metrics.cpu_usage_percent == 0.0
        assert metrics.combats_per_minute == 0.0
        assert metrics.errors_per_minute == 0.0

    def test_combat_metrics_custom_values(self):
        """Test custom combat metrics values."""
        metrics = CombatMetrics(
            total_combats=10, active_combats=2, completed_combats=8, total_errors=1, average_combat_duration=5.5
        )

        assert metrics.total_combats == 10
        assert metrics.active_combats == 2
        assert metrics.completed_combats == 8
        assert metrics.total_errors == 1
        assert metrics.average_combat_duration == 5.5

    def test_combat_metrics_to_dict(self):
        """Test converting metrics to dictionary."""
        metrics = CombatMetrics(total_combats=5, active_combats=1)
        metrics_dict = metrics.to_dict()

        assert metrics_dict["total_combats"] == 5
        assert metrics_dict["active_combats"] == 1
        assert "average_combat_duration" in metrics_dict


class TestAlert:
    """Test Alert data class."""

    def test_alert_creation(self):
        """Test alert creation."""
        alert = Alert(
            alert_id="test_alert_1",
            alert_type=AlertType.PERFORMANCE,
            severity=AlertSeverity.HIGH,
            title="Test Alert",
            message="This is a test alert",
            timestamp=time.time(),
        )

        assert alert.alert_id == "test_alert_1"
        assert alert.alert_type == AlertType.PERFORMANCE
        assert alert.severity == AlertSeverity.HIGH
        assert alert.title == "Test Alert"
        assert alert.message == "This is a test alert"
        assert alert.resolved is False
        assert alert.resolved_timestamp is None

    def test_alert_to_dict(self):
        """Test converting alert to dictionary."""
        alert = Alert(
            alert_id="test_alert_1",
            alert_type=AlertType.ERROR,
            severity=AlertSeverity.CRITICAL,
            title="Critical Error",
            message="A critical error occurred",
            timestamp=time.time(),
            metadata={"error_code": 500},
        )

        alert_dict = alert.to_dict()

        assert alert_dict["alert_id"] == "test_alert_1"
        assert alert_dict["alert_type"] == "error"
        assert alert_dict["severity"] == "critical"
        assert alert_dict["title"] == "Critical Error"
        assert alert_dict["message"] == "A critical error occurred"
        assert alert_dict["metadata"]["error_code"] == 500
        assert alert_dict["resolved"] is False


class TestCombatMonitoringService:
    """Test CombatMonitoringService functionality."""

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_service_initialization(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test service initialization."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()
        assert service._config == mock_config
        assert service._feature_flags == mock_feature_flags
        assert service._combat_config == mock_combat_config

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_start_combat_monitoring(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test starting combat monitoring."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        service.start_combat_monitoring("combat_123")

        assert service._metrics.total_combats == 1
        assert service._metrics.active_combats == 1
        assert "combat_123" in service._combat_start_times

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_end_combat_monitoring_success(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test ending combat monitoring with success."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Start combat
        service.start_combat_monitoring("combat_123")
        time.sleep(0.01)  # Small delay to ensure duration > 0

        # End combat
        service.end_combat_monitoring("combat_123", success=True)

        assert service._metrics.active_combats == 0
        assert service._metrics.completed_combats == 1
        assert service._metrics.failed_combats == 0
        assert "combat_123" not in service._combat_start_times

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_end_combat_monitoring_failure(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test ending combat monitoring with failure."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Start combat
        service.start_combat_monitoring("combat_123")

        # End combat with failure
        service.end_combat_monitoring("combat_123", success=False)

        assert service._metrics.active_combats == 0
        assert service._metrics.completed_combats == 0
        assert service._metrics.failed_combats == 1

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_turn_monitoring(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test turn monitoring."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Start and end turn
        service.start_turn_monitoring("combat_123")
        time.sleep(0.01)  # Small delay
        service.end_turn_monitoring("combat_123")

        assert "combat_123" not in service._turn_start_times

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_record_combat_error(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test recording combat errors."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Record different types of errors
        service.record_combat_error("validation", "combat_123")
        service.record_combat_error("timeout", "combat_456")
        service.record_combat_error("system", "combat_789")

        assert service._metrics.total_errors == 3
        assert service._metrics.validation_errors == 1
        assert service._metrics.timeout_errors == 1
        assert service._metrics.system_errors == 1

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_update_resource_metrics(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test updating resource metrics."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        service.update_resource_metrics(memory_mb=150.5, cpu_percent=85.2)

        assert service._metrics.memory_usage_mb == 150.5
        assert service._metrics.cpu_usage_percent == 85.2

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_get_current_metrics(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test getting current metrics."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        metrics = service.get_current_metrics()
        assert isinstance(metrics, CombatMetrics)

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_alert_callback(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test alert callback functionality."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Add callback
        callback_called = []

        def test_callback(alert):
            callback_called.append(alert)

        service.add_alert_callback(test_callback)

        # Trigger alert by exceeding error threshold
        for _i in range(4):  # Exceed threshold of 3
            service.record_combat_error("system")

        # Verify callback was called
        assert len(callback_called) > 0
        assert callback_called[0].alert_type == AlertType.ERROR

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_resolve_alert(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test resolving alerts."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Generate an alert
        for _i in range(4):
            service.record_combat_error("system")

        # Get active alerts
        active_alerts = service.get_active_alerts()
        assert len(active_alerts) > 0

        alert_id = active_alerts[0]["alert_id"]

        # Resolve alert
        resolved = service.resolve_alert(alert_id)
        assert resolved is True

        # Verify alert is resolved
        active_alerts_after = service.get_active_alerts()
        assert len(active_alerts_after) < len(active_alerts)

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_clear_resolved_alerts(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test clearing resolved alerts."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Generate alerts
        for _i in range(4):
            service.record_combat_error("system")

        # Resolve all alerts
        active_alerts = service.get_active_alerts()
        for alert in active_alerts:
            service.resolve_alert(alert["alert_id"])

        # Clear resolved alerts
        cleared_count = service.clear_resolved_alerts()
        assert cleared_count > 0

        # Verify alerts are cleared
        all_alerts = service.get_all_alerts()
        assert len(all_alerts) == 0

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_get_monitoring_summary(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test getting monitoring summary."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        summary = service.get_monitoring_summary()

        assert "metrics" in summary
        assert "active_alerts" in summary
        assert "total_alerts" in summary
        assert "monitoring_enabled" in summary
        assert "thresholds" in summary
        assert "resource_usage" in summary

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_monitoring_disabled(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test behavior when monitoring is disabled."""
        mock_get_config.return_value = mock_config
        mock_feature_flags.is_combat_monitoring_enabled.return_value = False
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Try to start monitoring
        service.start_combat_monitoring("combat_123")

        # Should not update metrics when monitoring is disabled
        assert service._metrics.total_combats == 0
        assert service._metrics.active_combats == 0


class TestGlobalCombatMonitoringFunctions:
    """Test global combat monitoring functions."""

    @patch("server.services.combat_monitoring_service.combat_monitoring")
    def test_get_combat_monitoring(self, mock_monitoring):
        """Test getting global combat monitoring service."""
        result = get_combat_monitoring()
        assert result == mock_monitoring

    @patch("server.services.combat_monitoring_service.combat_monitoring")
    def test_start_combat_monitoring_convenience(self, mock_monitoring):
        """Test convenience function for starting combat monitoring."""
        start_combat_monitoring("combat_123")
        mock_monitoring.start_combat_monitoring.assert_called_once_with("combat_123")

    @patch("server.services.combat_monitoring_service.combat_monitoring")
    def test_end_combat_monitoring_convenience(self, mock_monitoring):
        """Test convenience function for ending combat monitoring."""
        end_combat_monitoring("combat_123", success=True)
        mock_monitoring.end_combat_monitoring.assert_called_once_with("combat_123", True)

    @patch("server.services.combat_monitoring_service.combat_monitoring")
    def test_record_combat_error_convenience(self, mock_monitoring):
        """Test convenience function for recording combat error."""
        record_combat_error("validation", "combat_123", {"details": "test"})
        mock_monitoring.record_combat_error.assert_called_once_with("validation", "combat_123", {"details": "test"})

    @patch("server.services.combat_monitoring_service.combat_monitoring")
    def test_get_combat_metrics_convenience(self, mock_monitoring):
        """Test convenience function for getting combat metrics."""
        mock_monitoring.get_current_metrics.return_value = CombatMetrics()

        result = get_combat_metrics()
        assert isinstance(result, CombatMetrics)
        mock_monitoring.get_current_metrics.assert_called_once()


class TestCombatMonitoringServiceIntegration:
    """Test combat monitoring service integration scenarios."""

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_complete_combat_lifecycle(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test complete combat lifecycle monitoring."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Start combat
        service.start_combat_monitoring("combat_123")
        assert service._metrics.total_combats == 1
        assert service._metrics.active_combats == 1

        # Monitor turns
        service.start_turn_monitoring("combat_123")
        time.sleep(0.01)
        service.end_turn_monitoring("combat_123")

        # Record some errors
        service.record_combat_error("validation", "combat_123")
        service.record_combat_error("timeout", "combat_123")

        # End combat
        service.end_combat_monitoring("combat_123", success=True)

        # Verify final state
        assert service._metrics.total_combats == 1
        assert service._metrics.active_combats == 0
        assert service._metrics.completed_combats == 1
        assert service._metrics.failed_combats == 0
        assert service._metrics.total_errors == 2
        assert service._metrics.validation_errors == 1
        assert service._metrics.timeout_errors == 1

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_alert_threshold_exceeded(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test alert generation when thresholds are exceeded."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Exceed error threshold
        for _i in range(4):  # Threshold is 3
            service.record_combat_error("system")

        # Check that alert was generated
        active_alerts = service.get_active_alerts()
        assert len(active_alerts) > 0

        error_alerts = [a for a in active_alerts if a["alert_type"] == "error"]
        assert len(error_alerts) > 0
        assert error_alerts[0]["severity"] == "high"

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_resource_threshold_alerts(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test resource threshold alert generation."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Update resource metrics to exceed thresholds
        service.update_resource_metrics(memory_mb=150.0, cpu_percent=85.0)

        # Check that alerts were generated
        active_alerts = service.get_active_alerts()

        # Should have memory and CPU alerts
        performance_alerts = [a for a in active_alerts if a["alert_type"] == "performance"]
        assert len(performance_alerts) >= 2  # Should have at least 2 alerts (memory and CPU)

        # Check for memory alert
        memory_alerts = [a for a in performance_alerts if "memory" in a["message"].lower()]
        assert len(memory_alerts) >= 1

        # Check for CPU alert
        cpu_alerts = [a for a in performance_alerts if "cpu" in a["message"].lower()]
        assert len(cpu_alerts) >= 1


class TestCombatMonitoringServiceErrorHandling:
    """Test combat monitoring service error handling."""

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_alert_callback_error_handling(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test error handling in alert callbacks."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Add callback that raises exception
        def error_callback(alert):
            raise Exception("Callback error")

        service.add_alert_callback(error_callback)

        # Trigger alert - should not raise exception
        for _i in range(4):
            service.record_combat_error("system")

        # Should still have alerts despite callback error
        active_alerts = service.get_active_alerts()
        assert len(active_alerts) > 0

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_resolve_nonexistent_alert(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test resolving nonexistent alert."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Try to resolve nonexistent alert
        resolved = service.resolve_alert("nonexistent_alert")
        assert resolved is False

    @patch("server.services.combat_monitoring_service.get_config")
    @patch("server.services.combat_monitoring_service.get_feature_flags")
    @patch("server.services.combat_monitoring_service.get_combat_config")
    def test_end_monitoring_nonexistent_combat(
        self,
        mock_get_combat_config,
        mock_get_feature_flags,
        mock_get_config,
        mock_config,
        mock_feature_flags,
        mock_combat_config,
    ):
        """Test ending monitoring for nonexistent combat."""
        mock_get_config.return_value = mock_config
        mock_get_feature_flags.return_value = mock_feature_flags
        mock_get_combat_config.return_value = mock_combat_config

        service = CombatMonitoringService()

        # Try to end monitoring for nonexistent combat
        service.end_combat_monitoring("nonexistent_combat")

        # Should not raise exception and metrics should remain unchanged
        assert service._metrics.active_combats == 0
