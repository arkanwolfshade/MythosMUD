"""
Combat monitoring and alerting service for MythosMUD.

This service provides comprehensive monitoring of combat system health,
performance metrics, and automated alerting when thresholds are exceeded.

As noted in the restricted archives: "The cosmic forces that govern
our realm must be watched with eternal vigilance, lest they spiral
beyond mortal comprehension."
"""

import time
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

from server.config import get_config
from server.logging_config import get_logger
from server.services.combat_configuration_service import get_combat_config
from server.services.feature_flag_service import get_feature_flags

logger = get_logger(__name__)


class AlertSeverity(Enum):
    """Alert severity levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AlertType(Enum):
    """Alert types for combat monitoring."""

    PERFORMANCE = "performance"
    ERROR = "error"
    THRESHOLD = "threshold"
    AVAILABILITY = "availability"
    CONFIGURATION = "configuration"


@dataclass
class CombatMetrics:
    """Combat system metrics."""

    # Performance metrics
    total_combats: int = 0
    active_combats: int = 0
    completed_combats: int = 0
    failed_combats: int = 0

    # Timing metrics
    average_combat_duration: float = 0.0
    average_turn_time: float = 0.0
    max_combat_duration: float = 0.0

    # Error metrics
    total_errors: int = 0
    validation_errors: int = 0
    timeout_errors: int = 0
    system_errors: int = 0

    # Resource metrics
    memory_usage_mb: float = 0.0
    cpu_usage_percent: float = 0.0

    # Rate metrics
    combats_per_minute: float = 0.0
    errors_per_minute: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "total_combats": self.total_combats,
            "active_combats": self.active_combats,
            "completed_combats": self.completed_combats,
            "failed_combats": self.failed_combats,
            "average_combat_duration": self.average_combat_duration,
            "average_turn_time": self.average_turn_time,
            "max_combat_duration": self.max_combat_duration,
            "total_errors": self.total_errors,
            "validation_errors": self.validation_errors,
            "timeout_errors": self.timeout_errors,
            "system_errors": self.system_errors,
            "memory_usage_mb": self.memory_usage_mb,
            "cpu_usage_percent": self.cpu_usage_percent,
            "combats_per_minute": self.combats_per_minute,
            "errors_per_minute": self.errors_per_minute,
        }


@dataclass
class Alert:
    """Combat system alert."""

    alert_id: str
    alert_type: AlertType
    severity: AlertSeverity
    title: str
    message: str
    timestamp: float
    metadata: dict[str, Any] = field(default_factory=dict)
    resolved: bool = False
    resolved_timestamp: float | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "alert_id": self.alert_id,
            "alert_type": self.alert_type.value,
            "severity": self.severity.value,
            "title": self.title,
            "message": self.message,
            "timestamp": self.timestamp,
            "metadata": self.metadata,
            "resolved": self.resolved,
            "resolved_timestamp": self.resolved_timestamp,
        }


class CombatMonitoringService:
    """
    Comprehensive combat monitoring and alerting service.

    Tracks combat system health, performance, and generates alerts
    when thresholds are exceeded.
    """

    def __init__(self):
        """Initialize the combat monitoring service."""
        self._config = get_config()
        self._feature_flags = get_feature_flags()
        self._combat_config = get_combat_config()

        # Metrics tracking
        self._metrics = CombatMetrics()
        self._metrics_history: deque = deque(maxlen=1000)  # Keep last 1000 data points
        self._combat_start_times: dict[str, float] = {}
        self._turn_start_times: dict[str, float] = {}

        # Alerting
        self._alerts: dict[str, Alert] = {}
        self._alert_callbacks: list[Callable[[Alert], None]] = []
        self._alert_counter: int = 0

        # Thresholds
        self._performance_threshold = self._config.game.combat_performance_threshold
        self._error_threshold = self._config.game.combat_error_threshold
        self._alert_threshold = self._config.game.combat_alert_threshold

        logger.debug("Combat monitoring service initialized")

    def start_combat_monitoring(self, combat_id: str) -> None:
        """
        Start monitoring a combat instance.

        Args:
            combat_id: Unique combat identifier
        """
        if not self._feature_flags.is_combat_monitoring_enabled():
            return

        self._combat_start_times[combat_id] = time.time()
        self._metrics.total_combats += 1
        self._metrics.active_combats += 1

        logger.debug(f"Started monitoring combat {combat_id}")

    def end_combat_monitoring(self, combat_id: str, success: bool = True) -> None:
        """
        End monitoring a combat instance.

        Args:
            combat_id: Unique combat identifier
            success: Whether the combat completed successfully
        """
        if not self._feature_flags.is_combat_monitoring_enabled():
            return

        if combat_id not in self._combat_start_times:
            logger.warning(f"Combat {combat_id} not found in monitoring")
            return

        # Calculate combat duration
        start_time = self._combat_start_times[combat_id]
        duration = time.time() - start_time

        # Update metrics
        self._metrics.active_combats -= 1
        if success:
            self._metrics.completed_combats += 1
        else:
            self._metrics.failed_combats += 1

        # Update timing metrics
        self._update_timing_metrics(duration)

        # Clean up
        del self._combat_start_times[combat_id]
        if combat_id in self._turn_start_times:
            del self._turn_start_times[combat_id]

        logger.debug(f"Ended monitoring combat {combat_id}, duration: {duration:.2f}s")

    def start_turn_monitoring(self, combat_id: str) -> None:
        """
        Start monitoring a combat turn.

        Args:
            combat_id: Unique combat identifier
        """
        if not self._feature_flags.is_combat_monitoring_enabled():
            return

        self._turn_start_times[combat_id] = time.time()
        logger.debug(f"Started monitoring turn for combat {combat_id}")

    def end_turn_monitoring(self, combat_id: str) -> None:
        """
        End monitoring a combat turn.

        Args:
            combat_id: Unique combat identifier
        """
        if not self._feature_flags.is_combat_monitoring_enabled():
            return

        if combat_id not in self._turn_start_times:
            logger.warning(f"Turn for combat {combat_id} not found in monitoring")
            return

        # Calculate turn duration
        start_time = self._turn_start_times[combat_id]
        duration = time.time() - start_time

        # Update turn timing metrics
        self._update_turn_timing_metrics(duration)

        # Clean up
        del self._turn_start_times[combat_id]

        logger.debug(f"Ended monitoring turn for combat {combat_id}, duration: {duration:.2f}s")

    def record_combat_error(
        self, error_type: str, combat_id: str | None = None, error_details: dict[str, Any] | None = None
    ) -> None:
        """
        Record a combat error.

        Args:
            error_type: Type of error (validation, timeout, system)
            combat_id: Optional combat identifier
            error_details: Optional error details
        """
        if not self._feature_flags.is_combat_monitoring_enabled():
            return

        self._metrics.total_errors += 1

        # Update specific error counters
        if error_type == "validation":
            self._metrics.validation_errors += 1
        elif error_type == "timeout":
            self._metrics.timeout_errors += 1
        elif error_type == "system":
            self._metrics.system_errors += 1

        # Check error threshold
        self._check_error_threshold()

        logger.debug(f"Recorded combat error: {error_type}, combat: {combat_id}")

    def update_resource_metrics(self, memory_mb: float, cpu_percent: float) -> None:
        """
        Update resource usage metrics.

        Args:
            memory_mb: Memory usage in MB
            cpu_percent: CPU usage percentage
        """
        if not self._feature_flags.is_combat_monitoring_enabled():
            return

        self._metrics.memory_usage_mb = memory_mb
        self._metrics.cpu_usage_percent = cpu_percent

        # Check resource thresholds
        self._check_resource_thresholds()

    def get_current_metrics(self) -> CombatMetrics:
        """
        Get current combat metrics.

        Returns:
            CombatMetrics: Current metrics
        """
        return self._metrics

    def get_metrics_history(self, limit: int | None = None) -> list[dict[str, Any]]:
        """
        Get metrics history.

        Args:
            limit: Optional limit on number of records

        Returns:
            List[Dict[str, Any]]: Metrics history
        """
        history = [metrics.to_dict() for metrics in self._metrics_history]
        if limit:
            history = history[-limit:]
        return history

    def add_alert_callback(self, callback: Callable[[Alert], None]) -> None:
        """
        Add alert callback function.

        Args:
            callback: Function to call when alert is generated
        """
        self._alert_callbacks.append(callback)

    def remove_alert_callback(self, callback: Callable[[Alert], None]) -> None:
        """
        Remove alert callback function.

        Args:
            callback: Function to remove
        """
        if callback in self._alert_callbacks:
            self._alert_callbacks.remove(callback)

    def get_active_alerts(self) -> list[dict[str, Any]]:
        """
        Get active alerts.

        Returns:
            List[Dict[str, Any]]: Active alerts
        """
        return [alert.to_dict() for alert in self._alerts.values() if not alert.resolved]

    def get_all_alerts(self) -> list[dict[str, Any]]:
        """
        Get all alerts.

        Returns:
            List[Dict[str, Any]]: All alerts
        """
        return [alert.to_dict() for alert in self._alerts.values()]

    def resolve_alert(self, alert_id: str) -> bool:
        """
        Resolve an alert.

        Args:
            alert_id: Alert identifier

        Returns:
            bool: True if alert was resolved, False if not found
        """
        if alert_id not in self._alerts:
            return False

        alert = self._alerts[alert_id]
        alert.resolved = True
        alert.resolved_timestamp = time.time()

        logger.info(f"Resolved alert {alert_id}: {alert.title}")
        return True

    def clear_resolved_alerts(self) -> int:
        """
        Clear resolved alerts.

        Returns:
            int: Number of alerts cleared
        """
        resolved_alert_ids = [alert_id for alert_id, alert in self._alerts.items() if alert.resolved]

        for alert_id in resolved_alert_ids:
            del self._alerts[alert_id]

        logger.info(f"Cleared {len(resolved_alert_ids)} resolved alerts")
        return len(resolved_alert_ids)

    def get_monitoring_summary(self) -> dict[str, Any]:
        """
        Get monitoring summary.

        Returns:
            Dict[str, Any]]: Monitoring summary
        """
        return {
            "metrics": self._metrics.to_dict(),
            "active_alerts": len([a for a in self._alerts.values() if not a.resolved]),
            "total_alerts": len(self._alerts),
            "monitoring_enabled": self._feature_flags.is_combat_monitoring_enabled(),
            "thresholds": {
                "performance_threshold": self._performance_threshold,
                "error_threshold": self._error_threshold,
                "alert_threshold": self._alert_threshold,
            },
            "resource_usage": {
                "memory_mb": self._metrics.memory_usage_mb,
                "cpu_percent": self._metrics.cpu_usage_percent,
            },
        }

    def _update_timing_metrics(self, duration: float) -> None:
        """Update timing metrics with new combat duration."""
        # Update max duration
        if duration > self._metrics.max_combat_duration:
            self._metrics.max_combat_duration = duration

        # Update average duration (simple moving average)
        if self._metrics.completed_combats > 0:
            total_duration = self._metrics.average_combat_duration * (self._metrics.completed_combats - 1)
            self._metrics.average_combat_duration = (total_duration + duration) / self._metrics.completed_combats

    def _update_turn_timing_metrics(self, duration: float) -> None:
        """Update turn timing metrics."""
        # Update average turn time (simple moving average)
        if self._metrics.total_combats > 0:
            total_turn_time = self._metrics.average_turn_time * (self._metrics.total_combats - 1)
            self._metrics.average_turn_time = (total_turn_time + duration) / self._metrics.total_combats

    def _check_error_threshold(self) -> None:
        """Check if error threshold has been exceeded."""
        if self._metrics.total_errors >= self._error_threshold:
            self._generate_alert(
                AlertType.ERROR,
                AlertSeverity.HIGH,
                "Combat Error Threshold Exceeded",
                f"Total errors ({self._metrics.total_errors}) exceeded threshold ({self._error_threshold})",
                {"error_count": self._metrics.total_errors, "threshold": self._error_threshold},
            )

    def _check_resource_thresholds(self) -> None:
        """Check resource usage thresholds."""
        # Check memory usage (assuming 100MB threshold)
        if self._metrics.memory_usage_mb > 100:
            self._generate_alert(
                AlertType.PERFORMANCE,
                AlertSeverity.MEDIUM,
                "High Memory Usage",
                f"Memory usage ({self._metrics.memory_usage_mb:.1f}MB) is high",
                {"memory_mb": self._metrics.memory_usage_mb},
            )

        # Check CPU usage (assuming 80% threshold)
        if self._metrics.cpu_usage_percent > 80:
            self._generate_alert(
                AlertType.PERFORMANCE,
                AlertSeverity.HIGH,
                "High CPU Usage",
                f"CPU usage ({self._metrics.cpu_usage_percent:.1f}%) is high",
                {"cpu_percent": self._metrics.cpu_usage_percent},
            )

    def _check_performance_threshold(self) -> None:
        """Check if performance threshold has been exceeded."""
        if self._metrics.average_combat_duration > (self._performance_threshold / 1000):  # Convert ms to seconds
            self._generate_alert(
                AlertType.PERFORMANCE,
                AlertSeverity.MEDIUM,
                "Combat Performance Degraded",
                f"Average combat duration ({self._metrics.average_combat_duration:.2f}s) exceeded threshold ({self._performance_threshold}ms)",
                {
                    "average_duration": self._metrics.average_combat_duration,
                    "threshold_ms": self._performance_threshold,
                },
            )

    def _generate_alert(
        self,
        alert_type: AlertType,
        severity: AlertSeverity,
        title: str,
        message: str,
        metadata: dict[str, Any] | None = None,
    ) -> Alert:
        """Generate and dispatch an alert."""
        # Use counter to ensure unique IDs
        self._alert_counter += 1
        alert_id = f"{alert_type.value}_{self._alert_counter}_{int(time.time())}"

        alert = Alert(
            alert_id=alert_id,
            alert_type=alert_type,
            severity=severity,
            title=title,
            message=message,
            timestamp=time.time(),
            metadata=metadata or {},
        )

        # Store alert
        self._alerts[alert_id] = alert

        # Dispatch to callbacks
        for callback in self._alert_callbacks:
            try:
                callback(alert)
            except Exception as e:
                logger.error(f"Error in alert callback: {e}")

        logger.warning(f"Generated alert {alert_id}: {title}")
        return alert

    def _save_metrics_snapshot(self) -> None:
        """Save current metrics as a snapshot."""
        snapshot = CombatMetrics(
            total_combats=self._metrics.total_combats,
            active_combats=self._metrics.active_combats,
            completed_combats=self._metrics.completed_combats,
            failed_combats=self._metrics.failed_combats,
            average_combat_duration=self._metrics.average_combat_duration,
            average_turn_time=self._metrics.average_turn_time,
            max_combat_duration=self._metrics.max_combat_duration,
            total_errors=self._metrics.total_errors,
            validation_errors=self._metrics.validation_errors,
            timeout_errors=self._metrics.timeout_errors,
            system_errors=self._metrics.system_errors,
            memory_usage_mb=self._metrics.memory_usage_mb,
            cpu_usage_percent=self._metrics.cpu_usage_percent,
            combats_per_minute=self._metrics.combats_per_minute,
            errors_per_minute=self._metrics.errors_per_minute,
        )

        self._metrics_history.append(snapshot)

    def refresh_configuration(self) -> None:
        """Refresh configuration from source."""
        self._config = get_config()
        self._performance_threshold = self._config.game.combat_performance_threshold
        self._error_threshold = self._config.game.combat_error_threshold
        self._alert_threshold = self._config.game.combat_alert_threshold
        logger.info("Combat monitoring configuration refreshed")


# Global combat monitoring service instance
combat_monitoring = CombatMonitoringService()


def get_combat_monitoring() -> CombatMonitoringService:
    """
    Get the global combat monitoring service instance.

    Returns:
        CombatMonitoringService: The global combat monitoring service
    """
    return combat_monitoring


def start_combat_monitoring(combat_id: str) -> None:
    """
    Convenience function to start combat monitoring.

    Args:
        combat_id: Unique combat identifier
    """
    combat_monitoring.start_combat_monitoring(combat_id)


def end_combat_monitoring(combat_id: str, success: bool = True) -> None:
    """
    Convenience function to end combat monitoring.

    Args:
        combat_id: Unique combat identifier
        success: Whether the combat completed successfully
    """
    combat_monitoring.end_combat_monitoring(combat_id, success)


def record_combat_error(
    error_type: str, combat_id: str | None = None, error_details: dict[str, Any] | None = None
) -> None:
    """
    Convenience function to record combat error.

    Args:
        error_type: Type of error
        combat_id: Optional combat identifier
        error_details: Optional error details
    """
    combat_monitoring.record_combat_error(error_type, combat_id, error_details)


def get_combat_metrics() -> CombatMetrics:
    """
    Convenience function to get current combat metrics.

    Returns:
        CombatMetrics: Current metrics
    """
    return combat_monitoring.get_current_metrics()
