"""
Combat-specific audit logging and monitoring.

This module provides specialized logging for combat events to ensure
security, compliance, and monitoring of combat activities in the MUD.
"""

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

from server.structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@dataclass(frozen=True)
class CombatParties:
    """Player and target identity for combat audit events."""

    player_id: str
    player_name: str
    target_id: str
    target_name: str


@dataclass(frozen=True)
class CombatAttackDetails:
    """Attack outcome fields for combat audit."""

    action_type: str
    damage_dealt: int
    target_dp_before: int
    target_dp_after: int
    success: bool
    timestamp: datetime | None = None


@dataclass(frozen=True)
class CombatSecurityEvent:
    """Security event payload for combat audit."""

    event_type: str
    player_id: str
    player_name: str
    security_level: str
    description: str
    additional_data: dict[str, Any] | None = None
    timestamp: datetime | None = None


@dataclass(frozen=True)
class CombatMonitoringAlert:
    """Monitoring alert payload for combat audit."""

    alert_type: str
    severity: str
    description: str
    player_id: str | None = None
    player_name: str | None = None
    additional_data: dict[str, Any] | None = None
    timestamp: datetime | None = None


def _ts(timestamp: datetime | None) -> datetime:
    return timestamp if timestamp is not None else datetime.now(UTC)


class CombatAuditLogger:
    """Specialized logger for combat events and security monitoring."""

    def __init__(self) -> None:
        """Initialize the combat audit logger."""
        self.logger = get_logger("combat.audit")

    def log_combat_start(
        self,
        parties: CombatParties,
        room_id: str,
        action_type: str,
        timestamp: datetime | None = None,
    ) -> None:
        """Log the start of a combat encounter."""
        ts = _ts(timestamp)
        self.logger.info(
            "Combat encounter initiated",
            event_type="combat_start",
            player_id=parties.player_id,
            player_name=parties.player_name,
            target_id=parties.target_id,
            target_name=parties.target_name,
            room_id=room_id,
            action_type=action_type,
            timestamp=ts.isoformat(),
            security_level="medium",
            compliance_required=True,
        )

    def log_combat_attack(self, parties: CombatParties, details: CombatAttackDetails) -> None:
        """Log a combat attack."""
        ts = _ts(details.timestamp)
        self.logger.info(
            "Combat attack executed",
            event_type="combat_attack",
            player_id=parties.player_id,
            player_name=parties.player_name,
            target_id=parties.target_id,
            target_name=parties.target_name,
            action_type=details.action_type,
            damage_dealt=details.damage_dealt,
            target_dp_before=details.target_dp_before,
            target_dp_after=details.target_dp_after,
            success=details.success,
            timestamp=ts.isoformat(),
            security_level="medium",
            compliance_required=True,
        )

    def log_combat_death(
        self,
        parties: CombatParties,
        xp_gained: int,
        timestamp: datetime | None = None,
    ) -> None:
        """Log the death of a combat target."""
        ts = _ts(timestamp)
        self.logger.info(
            "Combat target defeated",
            event_type="combat_death",
            player_id=parties.player_id,
            player_name=parties.player_name,
            target_id=parties.target_id,
            target_name=parties.target_name,
            xp_gained=xp_gained,
            timestamp=ts.isoformat(),
            security_level="medium",
            compliance_required=True,
        )

    def log_combat_end(
        self,
        parties: CombatParties,
        reason: str,
        duration_seconds: int,
        timestamp: datetime | None = None,
    ) -> None:
        """Log the end of a combat encounter."""
        ts = _ts(timestamp)
        self.logger.info(
            "Combat encounter ended",
            event_type="combat_end",
            player_id=parties.player_id,
            player_name=parties.player_name,
            target_id=parties.target_id,
            target_name=parties.target_name,
            reason=reason,
            duration_seconds=duration_seconds,
            timestamp=ts.isoformat(),
            security_level="medium",
            compliance_required=True,
        )

    def log_combat_security_event(self, event: CombatSecurityEvent) -> None:
        """Log a combat-related security event."""
        ts = _ts(event.timestamp)
        log_data: dict[str, Any] = {
            "event_type": f"combat_security_{event.event_type}",
            "player_id": event.player_id,
            "player_name": event.player_name,
            "security_level": event.security_level,
            "description": event.description,
            "timestamp": ts.isoformat(),
            "compliance_required": True,
        }
        if event.additional_data:
            log_data.update(event.additional_data)
        self.logger.warning("Combat security event detected", **log_data)

    def log_combat_validation_failure(
        self,
        player_id: str,
        player_name: str,
        validation_type: str,
        failure_reason: str,
        command_data: dict[str, Any],
        timestamp: datetime | None = None,
    ) -> None:
        """Log a combat validation failure."""
        ts = _ts(timestamp)
        self.logger.warning(
            "Combat validation failure",
            event_type="combat_validation_failure",
            player_id=player_id,
            player_name=player_name,
            validation_type=validation_type,
            failure_reason=failure_reason,
            command_data=command_data,
            timestamp=ts.isoformat(),
            security_level="high",
            compliance_required=True,
        )

    def log_combat_rate_limit(
        self,
        player_id: str,
        player_name: str,
        rate_limit_type: str,
        attempts: int,
        time_window: int,
        timestamp: datetime | None = None,
    ) -> None:
        """Log a combat rate limit event."""
        ts = _ts(timestamp)
        self.logger.warning(
            "Combat rate limit triggered",
            event_type="combat_rate_limit",
            player_id=player_id,
            player_name=player_name,
            rate_limit_type=rate_limit_type,
            attempts=attempts,
            time_window=time_window,
            timestamp=ts.isoformat(),
            security_level="high",
            compliance_required=True,
        )

    def log_combat_monitoring_alert(self, alert: CombatMonitoringAlert) -> None:
        """Log a combat monitoring alert."""
        ts = _ts(alert.timestamp)
        log_data: dict[str, Any] = {
            "event_type": f"combat_monitoring_{alert.alert_type}",
            "severity": alert.severity,
            "description": alert.description,
            "timestamp": ts.isoformat(),
            "compliance_required": True,
        }
        if alert.player_id:
            log_data["player_id"] = alert.player_id
        if alert.player_name:
            log_data["player_name"] = alert.player_name
        if alert.additional_data:
            log_data.update(alert.additional_data)
        if alert.severity in ["high", "critical"]:
            self.logger.error("Combat monitoring alert", **log_data)
        else:
            self.logger.warning("Combat monitoring alert", **log_data)

    def get_combat_audit_summary(
        self,
        player_id: str | None = None,
        time_range_hours: int = 24,
    ) -> dict[str, Any]:
        """Get a summary of combat audit events (placeholder)."""
        return {
            "total_combat_events": 0,
            "security_events": 0,
            "validation_failures": 0,
            "rate_limit_events": 0,
            "time_range_hours": time_range_hours,
            "player_id": player_id,
        }


# Global combat audit logger instance
combat_audit_logger = CombatAuditLogger()
