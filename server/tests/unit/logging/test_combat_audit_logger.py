"""
Unit tests for the CombatAuditLogger class.

This module tests combat-specific audit logging and monitoring
in isolation from other systems.
"""

from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from server.logging.combat_audit import CombatAuditLogger


class TestCombatAuditLoggerUnit:
    """Unit tests for CombatAuditLogger core functionality."""

    @pytest.fixture
    def combat_audit_logger(self):
        """Create a combat audit logger instance for testing."""
        return CombatAuditLogger()

    @pytest.fixture
    def mock_logger(self):
        """Create a mock logger for testing."""
        return Mock()

    def test_combat_audit_logger_initialization(self, combat_audit_logger):
        """Test combat audit logger initialization."""
        assert hasattr(combat_audit_logger, "logger")
        assert combat_audit_logger.logger is not None

    @patch("server.logging.combat_audit.get_logger")
    def test_combat_audit_logger_uses_correct_logger_name(self, mock_get_logger, mock_logger):
        """Test that combat audit logger uses correct logger name."""
        mock_get_logger.return_value = mock_logger

        CombatAuditLogger()

        mock_get_logger.assert_called_once_with("combat.audit")

    def test_log_combat_start(self, combat_audit_logger, mock_logger):
        """Test logging combat start event."""
        combat_audit_logger.logger = mock_logger

        player_id = "test_player_id"
        player_name = "TestPlayer"
        target_id = "test_target_id"
        target_name = "TestTarget"
        room_id = "test_room"
        action_type = "attack"

        combat_audit_logger.log_combat_start(
            player_id=player_id,
            player_name=player_name,
            target_id=target_id,
            target_name=target_name,
            room_id=room_id,
            action_type=action_type,
        )

        # Verify logger was called with correct parameters
        mock_logger.info.assert_called_once()
        call_args = mock_logger.info.call_args

        assert call_args[0][0] == "Combat encounter initiated"
        assert call_args[1]["event_type"] == "combat_start"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["target_id"] == target_id
        assert call_args[1]["target_name"] == target_name
        assert call_args[1]["room_id"] == room_id
        assert call_args[1]["action_type"] == action_type
        assert call_args[1]["security_level"] == "medium"
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_start_with_timestamp(self, combat_audit_logger, mock_logger):
        """Test logging combat start event with custom timestamp."""
        combat_audit_logger.logger = mock_logger

        custom_timestamp = datetime(2024, 1, 1, 12, 0, 0)

        combat_audit_logger.log_combat_start(
            player_id="test_player_id",
            player_name="TestPlayer",
            target_id="test_target_id",
            target_name="TestTarget",
            room_id="test_room",
            action_type="attack",
            timestamp=custom_timestamp,
        )

        # Verify timestamp was used
        call_args = mock_logger.info.call_args
        assert call_args[1]["timestamp"] == custom_timestamp.isoformat()

    def test_log_combat_attack(self, combat_audit_logger, mock_logger):
        """Test logging combat attack event."""
        combat_audit_logger.logger = mock_logger

        player_id = "test_player_id"
        player_name = "TestPlayer"
        target_id = "test_target_id"
        target_name = "TestTarget"
        action_type = "punch"
        damage_dealt = 5
        target_hp_before = 50
        target_hp_after = 45
        success = True

        combat_audit_logger.log_combat_attack(
            player_id=player_id,
            player_name=player_name,
            target_id=target_id,
            target_name=target_name,
            action_type=action_type,
            damage_dealt=damage_dealt,
            target_hp_before=target_hp_before,
            target_hp_after=target_hp_after,
            success=success,
        )

        # Verify logger was called with correct parameters
        mock_logger.info.assert_called_once()
        call_args = mock_logger.info.call_args

        assert call_args[0][0] == "Combat attack executed"
        assert call_args[1]["event_type"] == "combat_attack"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["target_id"] == target_id
        assert call_args[1]["target_name"] == target_name
        assert call_args[1]["action_type"] == action_type
        assert call_args[1]["damage_dealt"] == damage_dealt
        assert call_args[1]["target_hp_before"] == target_hp_before
        assert call_args[1]["target_hp_after"] == target_hp_after
        assert call_args[1]["success"] == success
        assert call_args[1]["security_level"] == "medium"
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_death(self, combat_audit_logger, mock_logger):
        """Test logging combat death event."""
        combat_audit_logger.logger = mock_logger

        player_id = "test_player_id"
        player_name = "TestPlayer"
        target_id = "test_target_id"
        target_name = "TestTarget"
        xp_gained = 10

        combat_audit_logger.log_combat_death(
            player_id=player_id,
            player_name=player_name,
            target_id=target_id,
            target_name=target_name,
            xp_gained=xp_gained,
        )

        # Verify logger was called with correct parameters
        mock_logger.info.assert_called_once()
        call_args = mock_logger.info.call_args

        assert call_args[0][0] == "Combat target defeated"
        assert call_args[1]["event_type"] == "combat_death"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["target_id"] == target_id
        assert call_args[1]["target_name"] == target_name
        assert call_args[1]["xp_gained"] == xp_gained
        assert call_args[1]["security_level"] == "medium"
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_end(self, combat_audit_logger, mock_logger):
        """Test logging combat end event."""
        combat_audit_logger.logger = mock_logger

        player_id = "test_player_id"
        player_name = "TestPlayer"
        target_id = "test_target_id"
        target_name = "TestTarget"
        reason = "Target defeated"
        duration_seconds = 30

        combat_audit_logger.log_combat_end(
            player_id=player_id,
            player_name=player_name,
            target_id=target_id,
            target_name=target_name,
            reason=reason,
            duration_seconds=duration_seconds,
        )

        # Verify logger was called with correct parameters
        mock_logger.info.assert_called_once()
        call_args = mock_logger.info.call_args

        assert call_args[0][0] == "Combat encounter ended"
        assert call_args[1]["event_type"] == "combat_end"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["target_id"] == target_id
        assert call_args[1]["target_name"] == target_name
        assert call_args[1]["reason"] == reason
        assert call_args[1]["duration_seconds"] == duration_seconds
        assert call_args[1]["security_level"] == "medium"
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_security_event(self, combat_audit_logger, mock_logger):
        """Test logging combat security event."""
        combat_audit_logger.logger = mock_logger

        event_type = "suspicious_activity"
        player_id = "test_player_id"
        player_name = "TestPlayer"
        security_level = "high"
        description = "Multiple rapid attacks detected"
        additional_data = {"attempts": 10, "time_window": 60}

        combat_audit_logger.log_combat_security_event(
            event_type=event_type,
            player_id=player_id,
            player_name=player_name,
            security_level=security_level,
            description=description,
            additional_data=additional_data,
        )

        # Verify logger was called with correct parameters
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        assert call_args[0][0] == "Combat security event detected"
        assert call_args[1]["event_type"] == f"combat_security_{event_type}"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["security_level"] == security_level
        assert call_args[1]["description"] == description
        assert call_args[1]["additional_data"] == additional_data
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_security_event_without_additional_data(self, combat_audit_logger, mock_logger):
        """Test logging combat security event without additional data."""
        combat_audit_logger.logger = mock_logger

        event_type = "rate_limit_exceeded"
        player_id = "test_player_id"
        player_name = "TestPlayer"
        security_level = "medium"
        description = "Rate limit exceeded"

        combat_audit_logger.log_combat_security_event(
            event_type=event_type,
            player_id=player_id,
            player_name=player_name,
            security_level=security_level,
            description=description,
        )

        # Verify logger was called without additional_data
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        assert call_args[0][0] == "Combat security event detected"
        assert "additional_data" not in call_args[1]

    def test_log_combat_validation_failure(self, combat_audit_logger, mock_logger):
        """Test logging combat validation failure."""
        combat_audit_logger.logger = mock_logger

        player_id = "test_player_id"
        player_name = "TestPlayer"
        validation_type = "command_validation"
        failure_reason = "Invalid target name"
        command_data = {"command": "attack", "target": "<script>"}

        combat_audit_logger.log_combat_validation_failure(
            player_id=player_id,
            player_name=player_name,
            validation_type=validation_type,
            failure_reason=failure_reason,
            command_data=command_data,
        )

        # Verify logger was called with correct parameters
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        assert call_args[0][0] == "Combat validation failure"
        assert call_args[1]["event_type"] == "combat_validation_failure"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["validation_type"] == validation_type
        assert call_args[1]["failure_reason"] == failure_reason
        assert call_args[1]["command_data"] == command_data
        assert call_args[1]["security_level"] == "high"
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_rate_limit(self, combat_audit_logger, mock_logger):
        """Test logging combat rate limit event."""
        combat_audit_logger.logger = mock_logger

        player_id = "test_player_id"
        player_name = "TestPlayer"
        rate_limit_type = "attack_frequency"
        attempts = 15
        time_window = 60

        combat_audit_logger.log_combat_rate_limit(
            player_id=player_id,
            player_name=player_name,
            rate_limit_type=rate_limit_type,
            attempts=attempts,
            time_window=time_window,
        )

        # Verify logger was called with correct parameters
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        assert call_args[0][0] == "Combat rate limit triggered"
        assert call_args[1]["event_type"] == "combat_rate_limit"
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["rate_limit_type"] == rate_limit_type
        assert call_args[1]["attempts"] == attempts
        assert call_args[1]["time_window"] == time_window
        assert call_args[1]["security_level"] == "high"
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_monitoring_alert_high_severity(self, combat_audit_logger, mock_logger):
        """Test logging combat monitoring alert with high severity."""
        combat_audit_logger.logger = mock_logger

        alert_type = "unusual_activity"
        severity = "high"
        description = "Unusual combat patterns detected"
        player_id = "test_player_id"
        player_name = "TestPlayer"
        additional_data = {"pattern": "rapid_fire", "count": 50}

        combat_audit_logger.log_combat_monitoring_alert(
            alert_type=alert_type,
            severity=severity,
            description=description,
            player_id=player_id,
            player_name=player_name,
            additional_data=additional_data,
        )

        # Verify logger was called with error level for high severity
        mock_logger.error.assert_called_once()
        call_args = mock_logger.error.call_args

        assert call_args[0][0] == "Combat monitoring alert"
        assert call_args[1]["event_type"] == f"combat_monitoring_{alert_type}"
        assert call_args[1]["severity"] == severity
        assert call_args[1]["description"] == description
        assert call_args[1]["player_id"] == player_id
        assert call_args[1]["player_name"] == player_name
        assert call_args[1]["additional_data"] == additional_data
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_monitoring_alert_low_severity(self, combat_audit_logger, mock_logger):
        """Test logging combat monitoring alert with low severity."""
        combat_audit_logger.logger = mock_logger

        alert_type = "normal_activity"
        severity = "low"
        description = "Normal combat activity"

        combat_audit_logger.log_combat_monitoring_alert(
            alert_type=alert_type,
            severity=severity,
            description=description,
        )

        # Verify logger was called with warning level for low severity
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        assert call_args[0][0] == "Combat monitoring alert"
        assert call_args[1]["event_type"] == f"combat_monitoring_{alert_type}"
        assert call_args[1]["severity"] == severity
        assert call_args[1]["description"] == description
        assert call_args[1]["compliance_required"] is True

    def test_log_combat_monitoring_alert_without_player_info(self, combat_audit_logger, mock_logger):
        """Test logging combat monitoring alert without player information."""
        combat_audit_logger.logger = mock_logger

        alert_type = "system_alert"
        severity = "medium"
        description = "System-wide combat alert"

        combat_audit_logger.log_combat_monitoring_alert(
            alert_type=alert_type,
            severity=severity,
            description=description,
        )

        # Verify logger was called without player information
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        assert call_args[0][0] == "Combat monitoring alert"
        assert "player_id" not in call_args[1]
        assert "player_name" not in call_args[1]

    def test_get_combat_audit_summary(self, combat_audit_logger):
        """Test getting combat audit summary."""
        player_id = "test_player_id"
        time_range_hours = 48

        summary = combat_audit_logger.get_combat_audit_summary(
            player_id=player_id,
            time_range_hours=time_range_hours,
        )

        # Verify summary structure
        assert isinstance(summary, dict)
        assert "total_combat_events" in summary
        assert "security_events" in summary
        assert "validation_failures" in summary
        assert "rate_limit_events" in summary
        assert "time_range_hours" in summary
        assert "player_id" in summary

        assert summary["time_range_hours"] == time_range_hours
        assert summary["player_id"] == player_id

    def test_get_combat_audit_summary_defaults(self, combat_audit_logger):
        """Test getting combat audit summary with default parameters."""
        summary = combat_audit_logger.get_combat_audit_summary()

        # Verify default values
        assert summary["time_range_hours"] == 24
        assert summary["player_id"] is None

    def test_all_logging_methods_use_timestamp(self, combat_audit_logger, mock_logger):
        """Test that all logging methods use timestamp."""
        combat_audit_logger.logger = mock_logger

        # Test all logging methods
        combat_audit_logger.log_combat_start(
            player_id="test",
            player_name="Test",
            target_id="test",
            target_name="Test",
            room_id="test",
            action_type="attack",
        )
        combat_audit_logger.log_combat_attack(
            player_id="test",
            player_name="Test",
            target_id="test",
            target_name="Test",
            action_type="attack",
            damage_dealt=1,
            target_hp_before=50,
            target_hp_after=49,
            success=True,
        )
        combat_audit_logger.log_combat_death(
            player_id="test", player_name="Test", target_id="test", target_name="Test", xp_gained=10
        )
        combat_audit_logger.log_combat_end(
            player_id="test",
            player_name="Test",
            target_id="test",
            target_name="Test",
            reason="test",
            duration_seconds=30,
        )
        combat_audit_logger.log_combat_security_event(
            event_type="test", player_id="test", player_name="Test", security_level="medium", description="test"
        )
        combat_audit_logger.log_combat_validation_failure(
            player_id="test", player_name="Test", validation_type="test", failure_reason="test", command_data={}
        )
        combat_audit_logger.log_combat_rate_limit(
            player_id="test", player_name="Test", rate_limit_type="test", attempts=1, time_window=60
        )
        combat_audit_logger.log_combat_monitoring_alert(alert_type="test", severity="low", description="test")

        # Verify all calls included timestamp
        for call in (
            mock_logger.info.call_args_list + mock_logger.warning.call_args_list + mock_logger.error.call_args_list
        ):
            assert "timestamp" in call[1]
            assert isinstance(call[1]["timestamp"], str)
