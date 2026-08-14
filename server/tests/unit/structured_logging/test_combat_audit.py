"""
Unit tests for combat audit logging.

Tests the combat_audit module classes and functions.
"""

from datetime import UTC, datetime
from unittest.mock import patch

from server.structured_logging.combat_audit import (
    CombatAttackDetails,
    CombatAuditLogger,
    CombatMonitoringAlert,
    CombatParties,
    CombatSecurityEvent,
    combat_audit_logger,
)


def _parties() -> CombatParties:
    return CombatParties("player_123", "TestPlayer", "target_123", "TestTarget")


def test_combat_audit_logger_init():
    """Test CombatAuditLogger.__init__() initializes logger."""
    logger = CombatAuditLogger()

    assert hasattr(logger, "logger")


def test_combat_audit_logger_log_combat_start():
    """Test CombatAuditLogger.log_combat_start() logs combat start."""
    logger = CombatAuditLogger()
    parties = _parties()

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_start(parties, "room_123", "attack")

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_start"
        assert call_kwargs["player_id"] == parties.player_id
        assert call_kwargs["target_id"] == parties.target_id


def test_combat_audit_logger_log_combat_start_with_timestamp():
    """Test CombatAuditLogger.log_combat_start() uses provided timestamp."""
    logger = CombatAuditLogger()
    timestamp = datetime.now(UTC)

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_start(_parties(), "room_123", "attack", timestamp)

        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["timestamp"] == timestamp.isoformat()


def test_combat_audit_logger_log_combat_attack():
    """Test CombatAuditLogger.log_combat_attack() logs combat attack."""
    logger = CombatAuditLogger()
    details = CombatAttackDetails("attack", 10, 50, 40, True)

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_attack(_parties(), details)

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_attack"
        assert call_kwargs["damage_dealt"] == 10
        assert call_kwargs["success"] is True


def test_combat_audit_logger_log_combat_death():
    """Test CombatAuditLogger.log_combat_death() logs combat death."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_death(_parties(), 100)

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_death"
        assert call_kwargs["xp_gained"] == 100


def test_combat_audit_logger_log_combat_end():
    """Test CombatAuditLogger.log_combat_end() logs combat end."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "info") as mock_info:
        logger.log_combat_end(_parties(), "death", 30)

        mock_info.assert_called_once()
        call_kwargs = mock_info.call_args[1]
        assert call_kwargs["event_type"] == "combat_end"
        assert call_kwargs["reason"] == "death"
        assert call_kwargs["duration_seconds"] == 30


def test_combat_audit_logger_log_combat_security_event():
    """Test CombatAuditLogger.log_combat_security_event() logs security event."""
    logger = CombatAuditLogger()
    event = CombatSecurityEvent(
        "suspicious_activity",
        "player_123",
        "TestPlayer",
        "high",
        "Multiple rapid attacks",
        {"attack_count": 10},
    )

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_security_event(event)

        mock_warning.assert_called_once()
        call_kwargs = mock_warning.call_args[1]
        assert call_kwargs["event_type"] == "combat_security_suspicious_activity"
        assert call_kwargs["security_level"] == "high"
        assert call_kwargs["attack_count"] == 10


def test_combat_audit_logger_log_combat_security_event_no_additional_data():
    """Test CombatAuditLogger.log_combat_security_event() handles no additional data."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_security_event(
            CombatSecurityEvent("event", "player_123", "TestPlayer", "medium", "Description")
        )

        mock_warning.assert_called_once()


def test_combat_audit_logger_log_combat_validation_failure():
    """Test CombatAuditLogger.log_combat_validation_failure() logs validation failure."""
    logger = CombatAuditLogger()
    command_data = {"command": "attack", "target": "invalid"}

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_validation_failure(
            "player_123", "TestPlayer", "target_validation", "Target not found", command_data
        )

        mock_warning.assert_called_once()
        call_kwargs = mock_warning.call_args[1]
        assert call_kwargs["event_type"] == "combat_validation_failure"
        assert call_kwargs["validation_type"] == "target_validation"
        assert call_kwargs["command_data"] == command_data


def test_combat_audit_logger_log_combat_rate_limit():
    """Test CombatAuditLogger.log_combat_rate_limit() logs rate limit."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_rate_limit("player_123", "TestPlayer", "attack_rate", 20, 60)

        mock_warning.assert_called_once()
        call_kwargs = mock_warning.call_args[1]
        assert call_kwargs["event_type"] == "combat_rate_limit"
        assert call_kwargs["attempts"] == 20
        assert call_kwargs["time_window"] == 60


def test_combat_audit_logger_log_combat_monitoring_alert_high():
    """Test CombatAuditLogger.log_combat_monitoring_alert() logs high severity alert."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "error") as mock_error:
        logger.log_combat_monitoring_alert(CombatMonitoringAlert("anomaly", "high", "Unusual combat pattern"))

        mock_error.assert_called_once()
        call_kwargs = mock_error.call_args[1]
        assert call_kwargs["event_type"] == "combat_monitoring_anomaly"
        assert call_kwargs["severity"] == "high"


def test_combat_audit_logger_log_combat_monitoring_alert_low():
    """Test CombatAuditLogger.log_combat_monitoring_alert() logs low severity alert."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "warning") as mock_warning:
        logger.log_combat_monitoring_alert(CombatMonitoringAlert("anomaly", "low", "Minor issue"))

        mock_warning.assert_called_once()


def test_combat_audit_logger_log_combat_monitoring_alert_with_player():
    """Test CombatAuditLogger.log_combat_monitoring_alert() includes player info."""
    logger = CombatAuditLogger()

    with patch.object(logger.logger, "error") as mock_error:
        logger.log_combat_monitoring_alert(
            CombatMonitoringAlert("anomaly", "high", "Description", "player_123", "TestPlayer", {"key": "value"})
        )

        call_kwargs = mock_error.call_args[1]
        assert call_kwargs["player_id"] == "player_123"
        assert call_kwargs["player_name"] == "TestPlayer"
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
