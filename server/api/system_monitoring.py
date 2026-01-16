"""
System monitoring API endpoints for MythosMUD.

This module provides root-level REST API endpoints for system-wide
monitoring, health checks, and alerting.

As noted in the Pnakotic Manuscripts, proper system monitoring APIs
are essential for maintaining oversight of our eldritch infrastructure.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from fastapi import APIRouter, Request

from ..exceptions import LoggedHTTPException
from ..monitoring.monitoring_dashboard import get_monitoring_dashboard
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request
from .monitoring_models import (
    AlertResolveResponse,
    SystemAlertsResponse,
    SystemHealthResponse,
    SystemMetricsResponse,
    SystemMonitoringSummaryResponse,
)

logger = get_logger(__name__)

# System-level monitoring router (for root-level endpoints)
system_monitoring_router = APIRouter(tags=["monitoring", "system"])


@system_monitoring_router.get("/health", response_model=SystemHealthResponse)
async def get_system_health(request: Request) -> SystemHealthResponse:
    """Enhanced health check endpoint using monitoring dashboard."""
    try:
        dashboard = get_monitoring_dashboard()
        system_health = dashboard.get_system_health()

        return SystemHealthResponse(
            status=system_health.status,
            timestamp=system_health.timestamp.isoformat(),
            performance_score=system_health.performance_score,
            error_rate=system_health.error_rate,
            warning_rate=system_health.warning_rate,
            active_users=system_health.active_users,
        )
    except Exception as error:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_system_health"
        raise LoggedHTTPException(status_code=503, detail="Health check failed", context=context) from error


@system_monitoring_router.get("/metrics", response_model=SystemMetricsResponse)
async def get_system_metrics(request: Request) -> SystemMetricsResponse:
    """Get system metrics from monitoring dashboard."""
    try:
        dashboard = get_monitoring_dashboard()
        result = dashboard.export_monitoring_data()
        if not isinstance(result, dict):
            raise TypeError("export_monitoring_data must return a dict")
        # Type narrowing: after isinstance check, result is guaranteed to be a dict
        result_dict: dict[str, Any] = result

        # Add cache metrics from CacheManager
        try:
            from ..caching.lru_cache import get_cache_manager

            cache_manager = get_cache_manager()
            cache_stats = cache_manager.get_all_stats()
            result_dict["cache_metrics"] = cache_stats
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cache metrics errors should not fail main endpoint
            logger.warning("Failed to collect cache metrics", error=str(e))

        # Add memory leak metrics from unified collector (Task 6: Memory Leak Monitoring)
        try:
            from ..monitoring.memory_leak_metrics import MemoryLeakMetricsCollector

            collector = MemoryLeakMetricsCollector()
            leak_metrics = collector.collect_all_metrics()
            result_dict["memory_leak_metrics"] = {
                "connection": leak_metrics.get("connection", {}),
                "event": leak_metrics.get("event", {}),
                "cache": leak_metrics.get("cache", {}),
                "task": leak_metrics.get("task", {}),
                "nats": leak_metrics.get("nats", {}),
                "alerts": collector.check_alerts(leak_metrics),
                "growth_rates": collector.calculate_growth_rates(),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory leak metrics errors should not fail main endpoint
            logger.warning("Failed to collect memory leak metrics", error=str(e))

        return SystemMetricsResponse(**result_dict)
    except Exception as error:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_system_metrics"
        raise LoggedHTTPException(status_code=500, detail="Metrics retrieval failed", context=context) from error


@system_monitoring_router.get("/monitoring/summary", response_model=SystemMonitoringSummaryResponse)
async def get_system_monitoring_summary(request: Request) -> SystemMonitoringSummaryResponse:
    """Get comprehensive monitoring summary."""
    try:
        dashboard = get_monitoring_dashboard()
        result = dashboard.get_monitoring_summary()
        # Convert MonitoringSummary dataclass to dict for Pydantic model
        result_dict = asdict(result)

        # Add event metrics from EventBus
        try:
            from .monitoring import _resolve_event_bus_from_request

            event_bus = _resolve_event_bus_from_request(request)
            subscriber_counts = event_bus.get_all_subscriber_counts()
            lifecycle_metrics = event_bus.get_subscriber_lifecycle_metrics()
            result_dict["event_metrics"] = {
                "subscriber_counts_by_type": subscriber_counts,
                "total_subscribers": lifecycle_metrics["total_subscribers"],
                "active_task_count": event_bus.get_active_task_count(),
                "subscription_churn_rate": lifecycle_metrics["subscription_churn_rate"],
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event metrics errors should not fail main endpoint
            logger.warning("Failed to collect event metrics", error=str(e))
            result_dict["event_metrics"] = {"error": "Failed to collect metrics"}

        return SystemMonitoringSummaryResponse(**result_dict)
    except Exception as error:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_system_monitoring_summary"
        raise LoggedHTTPException(status_code=500, detail="Monitoring summary failed", context=context) from error


@system_monitoring_router.get("/monitoring/alerts", response_model=SystemAlertsResponse)
async def get_system_monitoring_alerts(request: Request) -> SystemAlertsResponse:
    """Get system alerts from monitoring dashboard."""
    try:
        dashboard = get_monitoring_dashboard()
        alerts = dashboard.check_alerts()
        return SystemAlertsResponse(
            alerts=[alert.to_dict() if hasattr(alert, "to_dict") else alert for alert in alerts]
        )
    except Exception as error:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_system_monitoring_alerts"
        raise LoggedHTTPException(status_code=500, detail="Alert retrieval failed", context=context) from error


@system_monitoring_router.post("/monitoring/alerts/{alert_id}/resolve", response_model=AlertResolveResponse)
async def resolve_system_alert(alert_id: str, request: Request) -> AlertResolveResponse:
    """Resolve a system alert."""
    try:
        dashboard = get_monitoring_dashboard()
        success = dashboard.resolve_alert(alert_id)

        if success:
            return AlertResolveResponse(message=f"Alert {alert_id} resolved")
        context = create_context_from_request(request)
        context.metadata["operation"] = "resolve_system_alert"
        context.metadata["alert_id"] = alert_id
        raise LoggedHTTPException(status_code=404, detail="Alert not found", context=context)
    except LoggedHTTPException:
        raise
    except Exception as error:
        context = create_context_from_request(request)
        context.metadata["operation"] = "resolve_system_alert"
        context.metadata["alert_id"] = alert_id
        raise LoggedHTTPException(status_code=500, detail="Alert resolution failed", context=context) from error
