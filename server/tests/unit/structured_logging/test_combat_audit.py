"""
Unit tests for combat audit logging.

Tests the combat_audit module classes and functions.
"""

from datetime import UTC, datetime
from unittest.mock import patch

from server.structured_logging.combat_audit import CombatAuditLogger, combat_audit_logger


def test_combat_audit_logger_init():
    """Test CombatAuditLogger.__init__() initializes logger."""
    logger = CombatAuditLogger()

    assert hasattr(logger, "logger")


def test_combat_audit_logger_log_combat_start():
    """Test CombatAuditLogger.log_combat_start() logs combat start."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    target_id = "target_123"
    target_name = "TestTarget"
    room_id = "room_123"
    action_type = "attack"

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_start(player_id, player_name, target_id, target_name, room_id, action_type)

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_start"
        assert call_kwargs["player_id"] == player_id
        assert call_kwargs["target_id"] == target_id


def test_combat_audit_logger_log_combat_start_with_timestamp():
    """Test CombatAuditLogger.log_combat_start() uses provided timestamp."""
    logger = CombatAuditLogger()
    timestamp = datetime.now(UTC)

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_start("player_123", "TestPlayer", "target_123", "TestTarget", "room_123", "attack", timestamp)

        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["timestamp"] == timestamp.isoformat()


def test_combat_audit_logger_log_combat_attack():
    """Test CombatAuditLogger.log_combat_attack() logs combat attack."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    target_id = "target_123"
    target_name = "TestTarget"
    action_type = "attack"
    damage_dealt = 10
    target_dp_before = 50
    target_dp_after = 40
    success = True

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_attack(
            player_id,
            player_name,
            target_id,
            target_name,
            action_type,
            damage_dealt,
            target_dp_before,
            target_dp_after,
            success,
        )

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_attack"
        assert call_kwargs["damage_dealt"] == damage_dealt
        assert call_kwargs["success"] is True


def test_combat_audit_logger_log_combat_death():
    """Test CombatAuditLogger.log_combat_death() logs combat death."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    target_id = "target_123"
    target_name = "TestTarget"
    xp_gained = 100

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_death(player_id, player_name, target_id, target_name, xp_gained)

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_death"
        assert call_kwargs["xp_gained"] == xp_gained


def test_combat_audit_logger_log_combat_end():
    """Test CombatAuditLogger.log_combat_end() logs combat end."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    target_id = "target_123"
    target_name = "TestTarget"
    reason = "death"
    duration_seconds = 30

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_end(player_id, player_name, target_id, target_name, reason, duration_seconds)

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_end"
        assert call_kwargs["reason"] == reason
        assert call_kwargs["duration_seconds"] == duration_seconds


def test_combat_audit_logger_log_combat_security_event():
    """Test CombatAuditLogger.log_combat_security_event() logs security event."""
    logger = CombatAuditLogger()
    event_type = "suspicious_activity"
    player_id = "player_123"
    player_name = "TestPlayer"
    security_level = "high"
    description = "Multiple rapid attacks"
    additional_data = {"attack_count": 10}

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_security_event(
            event_type, player_id, player_name, security_level, description, additional_data
        )

        mock_warning.assert_called_once()
        call_kwargs = mock_warning.call_args[1]
        assert call_kwargs["event_type"] == "combat_security_suspicious_activity"
        assert call_kwargs["security_level"] == security_level
        assert call_kwargs["attack_count"] == 10


def test_combat_audit_logger_log_combat_security_event_no_additional_data():
    """Test CombatAuditLogger.log_combat_security_event() handles no additional data."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_security_event("event", "player_123", "TestPlayer", "medium", "Description", None)

        mock_warning.assert_called_once()


def test_combat_audit_logger_log_combat_validation_failure():
    """Test CombatAuditLogger.log_combat_validation_failure() logs validation failure."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    validation_type = "target_validation"
    failure_reason = "Target not found"
    command_data = {"command": "attack", "target": "invalid"}

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_validation_failure(player_id, player_name, validation_type, failure_reason, command_data)

        mock_warning.assert_called_once()
        call_kwargs = mock_warning.call_args[1]
        assert call_kwargs["event_type"] == "combat_validation_failure"
        assert call_kwargs["validation_type"] == validation_type
        assert call_kwargs["command_data"] == command_data


def test_combat_audit_logger_log_combat_rate_limit():
    """Test CombatAuditLogger.log_combat_rate_limit() logs rate limit."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    rate_limit_type = "attack_rate"
    attempts = 20
    time_window = 60

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_rate_limit(player_id, player_name, rate_limit_type, attempts, time_window)

        mock_warning.assert_called_once()
        call_kwargs = mock_warning.call_args[1]
        assert call_kwargs["event_type"] == "combat_rate_limit"
        assert call_kwargs["attempts"] == attempts
        assert call_kwargs["time_window"] == time_window


def test_combat_audit_logger_log_combat_monitoring_alert_high():
    """Test CombatAuditLogger.log_combat_monitoring_alert() logs high severity alert."""
    logger = CombatAuditLogger()
    alert_type = "anomaly"
    severity = "high"
    description = "Unusual combat pattern"

    with patch.object(logger.logger, "error") as mock_error:
        logger.log_combat_monitoring_alert(alert_type, severity, description)

        mock_error.assert_called_once()
        call_kwargs = mock_error.call_args[1]
        assert call_kwargs["event_type"] == "combat_monitoring_anomaly"
        assert call_kwargs["severity"] == severity


def test_combat_audit_logger_log_combat_monitoring_alert_low():
    """Test CombatAuditLogger.log_combat_monitoring_alert() logs low severity alert."""
    logger = CombatAuditLogger()
    alert_type = "anomaly"
    severity = "low"
    description = "Minor issue"

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_monitoring_alert(alert_type, severity, description)

        mock_warning.assert_called_once()


def test_combat_audit_logger_log_combat_monitoring_alert_with_player():
    """Test CombatAuditLogger.log_combat_monitoring_alert() includes player info."""
    logger = CombatAuditLogger()
    player_id = "player_123"
    player_name = "TestPlayer"
    additional_data = {"key": "value"}

    with patch.object(logger.logger, "error") as mock_error:
        logger.log_combat_monitoring_alert("anomaly", "high", "Description", player_id, player_name, additional_data)

        call_kwargs = mock_error.call_args[1]
        assert call_kwargs["player_id"] == player_id
        assert call_kwargs["player_name"] == player_name
        assert call_kwargs["key"] == "value"


def test_combat_audit_logger_get_combat_audit_summary():
    """Test CombatAuditLogger.get_combat_audit_summary() returns summary."""
    logger = CombatAuditLogger()

    summary = logger.get_combat_audit_summary()

    assert isinstance(summary, dict)
    assert "total_combat_events" in summary
    assert "security_events" in summary
    assert "validation_failures" in summary
    assert "rate_limit_events" in summary


def test_combat_audit_logger_get_combat_audit_summary_with_player():
    """Test CombatAuditLogger.get_combat_audit_summary() filters by player."""
    logger = CombatAuditLogger()
    player_id = "player_123"

    summary = logger.get_combat_audit_summary(player_id=player_id)

    assert summary["player_id"] == player_id


def test_combat_audit_logger_get_combat_audit_summary_with_time_range():
    """Test CombatAuditLogger.get_combat_audit_summary() uses time range."""
    logger = CombatAuditLogger()
    time_range_hours = 48

    summary = logger.get_combat_audit_summary(time_range_hours=time_range_hours)

    assert summary["time_range_hours"] == time_range_hours


def test_global_combat_audit_logger():
    """Test global combat_audit_logger instance exists."""
    assert isinstance(combat_audit_logger, CombatAuditLogger)
