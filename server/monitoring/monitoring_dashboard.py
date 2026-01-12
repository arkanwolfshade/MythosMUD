"""
Comprehensive monitoring dashboard for MythosMUD server.

This module provides a centralized monitoring dashboard that aggregates
performance metrics, exception tracking, and log aggregation data for
comprehensive system monitoring and alerting.

As noted in the Pnakotic Manuscripts, understanding the interconnected
patterns of our systems is essential for maintaining their stability.
"""

# pylint: disable=too-many-lines  # Reason: Monitoring dashboard requires extensive dashboard logic for comprehensive system monitoring and metrics aggregation

from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any

from server.structured_logging.enhanced_logging_config import get_logger, log_with_context
from server.structured_logging.log_aggregator import LogAggregationStats, get_log_aggregator

from .exception_tracker import ExceptionStats, get_exception_tracker
from .performance_monitor import PerformanceStats, get_performance_monitor

logger = get_logger(__name__)


@dataclass
class SystemHealth:  # pylint: disable=too-many-instance-attributes  # Reason: System health requires many fields to capture complete health status
    """Represents overall system health status."""

    status: str  # healthy, warning, critical
    timestamp: datetime
    performance_score: float
    error_rate: float
    warning_rate: float
    active_users: int
    system_load: float
    memory_usage: float
    disk_usage: float
    details: dict[str, Any] = field(default_factory=dict)


@dataclass
class Alert:
    """Represents a system alert."""

    alert_id: str
    alert_type: str
    severity: str
    message: str
    timestamp: datetime
    resolved: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class MonitoringSummary:
    """Comprehensive monitoring summary."""

    timestamp: datetime
    system_health: SystemHealth
    performance_stats: dict[str, PerformanceStats]
    exception_stats: ExceptionStats
    log_stats: LogAggregationStats
    alerts: list[Alert]
    recommendations: list[str] = field(default_factory=list)


class MonitoringDashboard:
    """
    Comprehensive monitoring dashboard system.

    This class provides a centralized dashboard that aggregates all monitoring
    data including performance metrics, exception tracking, and log aggregation.
    """

    def __init__(self) -> None:
        """Initialize the monitoring dashboard."""
        self.performance_monitor = get_performance_monitor()
        self.exception_tracker = get_exception_tracker()
        self.log_aggregator = get_log_aggregator()

        # Alert system
        self.alerts: list[Alert] = []
        self.alert_thresholds = {
            "error_rate": 5.0,  # 5% error rate threshold
            "warning_rate": 10.0,  # 10% warning rate threshold
            "response_time": 1000.0,  # 1 second response time threshold
            "exception_rate": 1.0,  # 1% exception rate threshold
            "summon_quantity_warning": 5,
            "summon_quantity_critical": 20,
        }

        logger.info("Monitoring dashboard initialized")

    def get_system_health(self) -> SystemHealth:
        """
        Get overall system health status.

        Returns:
            Current system health status
        """
        # Get performance statistics
        perf_stats_raw = self.performance_monitor.get_all_stats()
        # Filter out None values for type safety
        perf_stats: dict[str, PerformanceStats] = {k: v for k, v in perf_stats_raw.items() if v is not None}

        # Get exception statistics
        exc_stats = self.exception_tracker.get_stats()

        # Get log statistics
        log_stats = self.log_aggregator.get_stats()

        # Calculate performance score (0-100)
        performance_score = self._calculate_performance_score(perf_stats)

        # Calculate error and warning rates
        error_rate = log_stats.error_rate
        warning_rate = log_stats.warning_rate

        # Determine overall status
        status = self._determine_health_status(performance_score, error_rate, warning_rate, exc_stats.error_rate)

        # Get system metrics (simplified for now)
        active_users = self._get_active_users()
        system_load = self._get_system_load()
        memory_usage = self._get_memory_usage()
        disk_usage = self._get_disk_usage()

        return SystemHealth(
            status=status,
            timestamp=datetime.now(UTC),
            performance_score=performance_score,
            error_rate=error_rate,
            warning_rate=warning_rate,
            active_users=active_users,
            system_load=system_load,
            memory_usage=memory_usage,
            disk_usage=disk_usage,
            details={"performance_stats": perf_stats, "exception_stats": exc_stats, "log_stats": log_stats},
        )

    def get_monitoring_summary(self) -> MonitoringSummary:
        """
        Get comprehensive monitoring summary.

        Returns:
            Complete monitoring summary with all metrics
        """
        system_health = self.get_system_health()
        performance_stats_raw = self.performance_monitor.get_all_stats()
        # Filter out None values for type safety
        performance_stats: dict[str, PerformanceStats] = {
            k: v for k, v in performance_stats_raw.items() if v is not None
        }
        exception_stats = self.exception_tracker.get_stats()
        log_stats = self.log_aggregator.get_stats()

        # Get active alerts
        active_alerts = [alert for alert in self.alerts if not alert.resolved]

        # Generate recommendations
        recommendations = self._generate_recommendations(system_health, performance_stats, exception_stats, log_stats)

        return MonitoringSummary(
            timestamp=datetime.now(UTC),
            system_health=system_health,
            performance_stats=performance_stats,
            exception_stats=exception_stats,
            log_stats=log_stats,
            alerts=active_alerts,
            recommendations=recommendations,
        )

    def check_alerts(self) -> list[Alert]:
        """
        Check for system alerts based on current metrics.

        Returns:
            List of new alerts
        """
        new_alerts = []
        system_health = self.get_system_health()

        # Check error rate threshold
        if system_health.error_rate > self.alert_thresholds["error_rate"]:
            alert = Alert(
                alert_id=f"error_rate_{datetime.now(UTC).timestamp()}",
                alert_type="error_rate",
                severity="critical" if system_health.error_rate > 10.0 else "warning",
                message=f"Error rate is {system_health.error_rate:.2f}% (threshold: {self.alert_thresholds['error_rate']}%)",
                timestamp=datetime.now(UTC),
                metadata={"error_rate": system_health.error_rate},
            )
            new_alerts.append(alert)

        # Check warning rate threshold
        if system_health.warning_rate > self.alert_thresholds["warning_rate"]:
            alert = Alert(
                alert_id=f"warning_rate_{datetime.now(UTC).timestamp()}",
                alert_type="warning_rate",
                severity="warning",
                message=f"Warning rate is {system_health.warning_rate:.2f}% (threshold: {self.alert_thresholds['warning_rate']}%)",
                timestamp=datetime.now(UTC),
                metadata={"warning_rate": system_health.warning_rate},
            )
            new_alerts.append(alert)

        # Check performance score
        if system_health.performance_score < 70.0:
            alert = Alert(
                alert_id=f"performance_{datetime.now(UTC).timestamp()}",
                alert_type="performance",
                severity="critical" if system_health.performance_score < 50.0 else "warning",
                message=f"Performance score is {system_health.performance_score:.2f} (threshold: 70.0)",
                timestamp=datetime.now(UTC),
                metadata={"performance_score": system_health.performance_score},
            )
            new_alerts.append(alert)

        # Check exception rate
        if (
            system_health.details.get("exception_stats", {}).get("error_rate", 0)
            > self.alert_thresholds["exception_rate"]
        ):
            alert = Alert(
                alert_id=f"exception_rate_{datetime.now(UTC).timestamp()}",
                alert_type="exception_rate",
                severity="critical",
                message=f"Exception rate is {system_health.details['exception_stats']['error_rate']:.2f}% (threshold: {self.alert_thresholds['exception_rate']}%)",
                timestamp=datetime.now(UTC),
                metadata={"exception_rate": system_health.details["exception_stats"]["error_rate"]},
            )
            new_alerts.append(alert)

        # Add new alerts to the list
        self.alerts.extend(new_alerts)

        # Log new alerts
        for alert in new_alerts:
            log_with_context(
                logger,
                alert.severity,
                f"System alert: {alert.alert_type}",
                alert_id=alert.alert_id,
                alert_type=alert.alert_type,
                severity=alert.severity,
                alert_message=alert.message,
                metadata=alert.metadata,
            )

        return new_alerts

    def record_custom_alert(
        self,
        alert_type: str,
        *,
        severity: str = "warning",
        message: str,
        metadata: dict[str, Any] | None = None,
    ) -> Alert:
        """
        Record a custom alert emitted by subsystems.

        Args:
            alert_type: Identifier for the alert source.
            severity: Alert severity (info, warning, critical, etc.).
            message: Human readable alert description.
            metadata: Optional structured metadata for responders.

        Returns:
            The recorded `Alert` instance.
        """

        alert = Alert(
            alert_id=f"{alert_type}_{datetime.now(UTC).timestamp()}",
            alert_type=alert_type,
            severity=severity,
            message=message,
            timestamp=datetime.now(UTC),
            metadata=metadata or {},
        )
        self.alerts.append(alert)

        log_with_context(
            logger,
            severity,
            f"Custom alert recorded: {alert_type}",
            alert_id=alert.alert_id,
            alert_type=alert_type,
            severity=severity,
            alert_message=message,
            metadata=metadata or {},
        )

        return alert

    def record_registry_failure(
        self,
        *,
        source: str,
        error: str,
        metadata: dict[str, Any] | None = None,
        severity: str | None = None,
    ) -> Alert:
        """
        Record an alert related to prototype registry loading.

        Args:
            source: Which subsystem encountered the failure.
            error: Short error code such as 'directory_missing' or 'validation_error'.
            metadata: Optional structured metadata.
            severity: Override severity (defaults to warning unless failure is critical).
        """

        alert_metadata = {"source": source, "error": error}
        if metadata:
            alert_metadata.update(metadata)

        resolved_severity = severity or ("critical" if error == "directory_missing" else "warning")

        return self.record_custom_alert(
            "prototype_registry_failure",
            severity=resolved_severity,
            message=f"Prototype registry failure detected ({error})",
            metadata=alert_metadata,
        )

    def record_summon_quantity_spike(
        self,
        *,
        admin_name: str,
        prototype_id: str | None,
        quantity: int,
        metadata: dict[str, Any] | None = None,
    ) -> Alert:
        """
        Record an alert when administrative summon quantities exceed thresholds.
        """

        warning_threshold = int(self.alert_thresholds.get("summon_quantity_warning", 5))
        critical_threshold = int(self.alert_thresholds.get("summon_quantity_critical", 20))
        severity = "info"
        if quantity >= critical_threshold:
            severity = "critical"
        elif quantity >= warning_threshold:
            severity = "warning"

        alert_metadata = {
            "admin": admin_name,
            "prototype_id": prototype_id,
            "quantity": quantity,
        }
        if metadata:
            alert_metadata.update(metadata)

        return self.record_custom_alert(
            "summon_quantity_spike",
            severity=severity,
            message=f"Summon quantity spike detected ({quantity} requested by {admin_name})",
            metadata=alert_metadata,
        )

    def record_durability_anomaly(
        self,
        *,
        prototype_id: str,
        durability: int | None,
        reason: str,
        metadata: dict[str, Any] | None = None,
    ) -> Alert:
        """
        Record an alert for durability anomalies on item prototypes.
        """

        alert_metadata = {
            "prototype_id": prototype_id,
            "durability": durability,
            "reason": reason,
        }
        if metadata:
            alert_metadata.update(metadata)

        return self.record_custom_alert(
            "durability_anomaly",
            severity="warning",
            message=f"Durability anomaly detected for {prototype_id} ({reason})",
            metadata=alert_metadata,
        )

    def resolve_alert(self, alert_id: str) -> bool:
        """
        Resolve an alert.

        Args:
            alert_id: ID of the alert to resolve

        Returns:
            True if alert was resolved, False if not found
        """
        for alert in self.alerts:
            if alert.alert_id == alert_id:
                alert.resolved = True
                log_with_context(
                    logger,
                    "info",
                    f"Alert resolved: {alert.alert_type}",
                    alert_id=alert_id,
                    alert_type=alert.alert_type,
                )
                return True
        return False

    def get_alert_history(self, hours: int = 24) -> list[Alert]:
        """
        Get alert history for the specified time period.

        Args:
            hours: Number of hours to look back

        Returns:
            List of alerts from the specified time period
        """
        cutoff_time = datetime.now(UTC) - timedelta(hours=hours)
        return [alert for alert in self.alerts if alert.timestamp >= cutoff_time]

    def export_monitoring_data(self, _format: str = "json") -> dict[str, Any]:  # pylint: disable=unused-argument  # Reason: Parameter reserved for future format support (currently only JSON)
        """
        Export comprehensive monitoring data.

        Args:
            format: Export format (currently only JSON supported)

        Returns:
            Exported monitoring data
        """
        summary = self.get_monitoring_summary()

        return {
            "timestamp": summary.timestamp.isoformat(),
            "system_health": {
                "status": summary.system_health.status,
                "performance_score": summary.system_health.performance_score,
                "error_rate": summary.system_health.error_rate,
                "warning_rate": summary.system_health.warning_rate,
                "active_users": summary.system_health.active_users,
                "system_load": summary.system_health.system_load,
                "memory_usage": summary.system_health.memory_usage,
                "disk_usage": summary.system_health.disk_usage,
            },
            "performance_stats": {
                op: {
                    "count": stats.count,
                    "avg_duration_ms": stats.avg_duration_ms,
                    "min_duration_ms": stats.min_duration_ms,
                    "max_duration_ms": stats.max_duration_ms,
                    "success_rate": stats.success_rate,
                    "error_rate": stats.error_rate,
                }
                for op, stats in summary.performance_stats.items()
            },
            "exception_stats": {
                "total_exceptions": summary.exception_stats.total_exceptions,
                "exceptions_by_type": dict(summary.exception_stats.exceptions_by_type),
                "unhandled_exceptions": summary.exception_stats.unhandled_exceptions,
                "critical_exceptions": summary.exception_stats.critical_exceptions,
                "error_rate": summary.exception_stats.error_rate,
            },
            "log_stats": {
                "total_entries": summary.log_stats.total_entries,
                "entries_by_level": dict(summary.log_stats.entries_by_level),
                "entries_by_logger": dict(summary.log_stats.entries_by_logger),
                "error_rate": summary.log_stats.error_rate,
                "warning_rate": summary.log_stats.warning_rate,
            },
            "alerts": [
                {
                    "alert_id": alert.alert_id,
                    "alert_type": alert.alert_type,
                    "severity": alert.severity,
                    "message": alert.message,
                    "timestamp": alert.timestamp.isoformat(),
                    "resolved": alert.resolved,
                    "metadata": alert.metadata,
                }
                for alert in summary.alerts
            ],
            "recommendations": summary.recommendations,
        }

    def _calculate_performance_score(self, perf_stats: dict[str, PerformanceStats]) -> float:
        """Calculate overall performance score (0-100)."""
        if not perf_stats:
            return 100.0

        total_score = 0.0
        count = 0

        for stats in perf_stats.values():
            # Base score on success rate and response time
            success_score = stats.success_rate
            time_score = max(0, 100 - (stats.avg_duration_ms / 10))  # Penalty for slow operations
            operation_score = (success_score + time_score) / 2
            total_score += operation_score
            count += 1

        return total_score / count if count > 0 else 100.0

    def _determine_health_status(
        self, performance_score: float, error_rate: float, warning_rate: float, exception_rate: float
    ) -> str:
        """Determine overall health status."""
        if performance_score < 50.0 or error_rate > 10.0 or exception_rate > 5.0:
            return "critical"
        if performance_score < 70.0 or error_rate > 5.0 or warning_rate > 15.0 or exception_rate > 2.0:
            return "warning"
        return "healthy"

    def _generate_recommendations(
        self,
        system_health: SystemHealth,
        _perf_stats: dict[str, PerformanceStats],  # pylint: disable=unused-argument  # Reason: Parameter reserved for future performance-based alerting
        exc_stats: ExceptionStats,
        _log_stats: LogAggregationStats,  # pylint: disable=unused-argument  # Reason: Parameter reserved for future log-based alerting
    ) -> list[str]:
        """Generate system recommendations based on current metrics."""
        recommendations = []

        # Performance recommendations
        if system_health.performance_score < 80.0:
            recommendations.append("Consider optimizing slow operations to improve performance")

        # Error rate recommendations
        if system_health.error_rate > 2.0:
            recommendations.append("High error rate detected - investigate recent errors")

        # Exception recommendations
        if exc_stats.unhandled_exceptions > 10:
            recommendations.append("Multiple unhandled exceptions detected - review error handling")

        # Warning rate recommendations
        if system_health.warning_rate > 10.0:
            recommendations.append("High warning rate - review system configuration")

        # Memory recommendations
        if system_health.memory_usage > 80.0:
            recommendations.append("High memory usage - consider memory optimization")

        # Disk recommendations
        if system_health.disk_usage > 90.0:
            recommendations.append("High disk usage - consider cleanup or expansion")

        return recommendations

    def _get_active_users(self) -> int:
        """Get number of active users (simplified implementation)."""
        # This would integrate with your user management system
        return 0

    def _get_system_load(self) -> float:
        """Get system load (simplified implementation)."""
        # This would integrate with system monitoring
        return 0.0

    def _get_memory_usage(self) -> float:
        """Get memory usage percentage (simplified implementation)."""
        # This would integrate with system monitoring
        return 0.0

    def _get_disk_usage(self) -> float:
        """Get disk usage percentage (simplified implementation)."""
        # This would integrate with system monitoring
        return 0.0


# Global monitoring dashboard instance
_monitoring_dashboard: MonitoringDashboard | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_monitoring_dashboard() -> MonitoringDashboard:
    """
    Get the global monitoring dashboard instance.

    Returns:
        Global MonitoringDashboard instance
    """
    global _monitoring_dashboard  # pylint: disable=global-statement  # Reason: Singleton pattern for monitoring dashboard
    if _monitoring_dashboard is None:
        _monitoring_dashboard = MonitoringDashboard()
    return _monitoring_dashboard
