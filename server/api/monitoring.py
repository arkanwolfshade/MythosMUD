"""
Monitoring API endpoints for MythosMUD.

This module provides REST API endpoints for accessing movement
system metrics, validation results, and performance data.

As noted in the Pnakotic Manuscripts, proper monitoring APIs
are essential for maintaining oversight of our eldritch systems.
"""

from __future__ import annotations

from dataclasses import asdict
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict

from ..dependencies import AsyncPersistenceDep
from ..exceptions import LoggedHTTPException
from ..game.movement_monitor import get_movement_monitor
from ..models.health import HealthErrorResponse, HealthResponse, HealthStatus
from ..monitoring.monitoring_dashboard import get_monitoring_dashboard
from ..realtime.connection_manager import resolve_connection_manager
from ..services.health_service import get_health_service
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)

monitoring_router = APIRouter(prefix="/monitoring", tags=["monitoring"])

# System-level monitoring router (for root-level endpoints)
system_monitoring_router = APIRouter(tags=["monitoring", "system"])


def _resolve_connection_manager_from_request(request: Request) -> Any:
    """
    Resolve a connection manager for routes that require it, preferring the container-managed
    instance while remaining compatible with legacy module-level injection used in tests.

    Returns:
        Connection manager instance (raises RuntimeError if not configured).
    """
    container = getattr(request.app.state, "container", None)
    candidate = getattr(container, "connection_manager", None) if container else None
    manager = resolve_connection_manager(candidate)
    if manager is None:
        raise RuntimeError("Connection manager is not configured")
    return manager


class MetricsResponse(BaseModel):
    """Response model for movement metrics."""

    total_movements: int
    successful_movements: int
    failed_movements: int
    success_rate: float
    failure_rate: float
    current_concurrent_movements: int
    max_concurrent_movements: int
    avg_movement_time_ms: float
    max_movement_time_ms: float
    min_movement_time_ms: float
    movements_per_second: float
    uptime_seconds: float
    integrity_checks: int
    integrity_violations: int
    integrity_rate: float
    last_movement_time: str | None
    last_validation_time: str | None
    room_occupancy: dict[str, int]
    player_movement_counts: dict[str, int]
    timestamp: str


class IntegrityResponse(BaseModel):
    """Response model for room integrity validation."""

    valid: bool
    violations: list[str]
    total_rooms: int
    total_players: int
    avg_occupancy: float
    max_occupancy: int
    timestamp: str


class AlertsResponse(BaseModel):
    """Response model for system alerts."""

    alerts: list[str]
    alert_count: int
    timestamp: str


class MemoryStatsResponse(BaseModel):
    """Response model for memory statistics."""

    memory: dict
    connections: dict
    data_structures: dict
    cleanup_stats: dict
    memory_monitor: dict
    timestamp: str


class MemoryAlertsResponse(BaseModel):
    """Response model for memory alerts."""

    alerts: list[str]
    alert_count: int
    timestamp: str


class DualConnectionStatsResponse(BaseModel):
    """Response model for dual connection statistics."""

    connection_distribution: dict
    connection_health: dict
    session_metrics: dict
    connection_lifecycle: dict
    performance_metrics: dict
    timestamp: float


class PerformanceStatsResponse(BaseModel):
    """Response model for connection performance statistics."""

    connection_establishment: dict
    message_delivery: dict
    disconnections: dict
    session_management: dict
    health_monitoring: dict
    timestamp: float


class ConnectionHealthStatsResponse(BaseModel):
    """Response model for connection health statistics."""

    overall_health: dict
    connection_type_health: dict
    connection_lifecycle: dict
    session_health: dict
    health_trends: dict
    timestamp: float


class MessageResponse(BaseModel):
    """Generic response model for operations that return a simple message."""

    message: str


class PerformanceSummaryResponse(BaseModel):
    """Response model for performance summary endpoint."""

    summary: dict[str, Any]
    alerts: list[dict[str, Any]]
    timestamp: str


@monitoring_router.get("/metrics", response_model=MetricsResponse)
async def get_movement_metrics(request: Request) -> MetricsResponse:
    """Get comprehensive movement system metrics."""
    try:
        monitor = get_movement_monitor()
        metrics = monitor.get_metrics()

        # Convert datetime objects to strings for JSON serialization
        if metrics["last_movement_time"]:
            metrics["last_movement_time"] = metrics["last_movement_time"].isoformat()
        if metrics["last_validation_time"]:
            metrics["last_validation_time"] = metrics["last_validation_time"].isoformat()
        metrics["timestamp"] = metrics["timestamp"].isoformat()

        return MetricsResponse(**metrics)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Metrics retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_movement_metrics"
        raise LoggedHTTPException(status_code=500, detail=f"Error retrieving metrics: {str(e)}", context=context) from e


@monitoring_router.get("/integrity", response_model=IntegrityResponse)
async def validate_room_integrity(
    request: Request, persistence: AsyncPersistenceLayer = AsyncPersistenceDep
) -> IntegrityResponse:
    """Validate room data integrity and return results."""
    try:
        monitor = get_movement_monitor()

        # Get all rooms from persistence
        rooms = {}
        room_list = persistence.list_rooms()
        for room in room_list:
            rooms[room.id] = room

        result = monitor.validate_room_integrity(rooms)
        result["timestamp"] = result["timestamp"].isoformat()

        return IntegrityResponse(**result)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Integrity validation errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "validate_room_integrity"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error validating integrity: {str(e)}", context=context
        ) from e


@monitoring_router.get("/alerts", response_model=AlertsResponse)
async def get_system_alerts(request: Request) -> AlertsResponse:
    """Get current system alerts."""
    try:
        monitor = get_movement_monitor()
        alerts = monitor.get_alerts()

        return AlertsResponse(
            alerts=alerts,
            alert_count=len(alerts),
            timestamp=get_movement_monitor().get_metrics()["timestamp"].isoformat(),
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Alert retrieval errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_system_alerts"
        raise LoggedHTTPException(status_code=500, detail=f"Error retrieving alerts: {str(e)}", context=context) from e


@monitoring_router.post("/reset", response_model=MessageResponse)
async def reset_metrics(request: Request) -> MessageResponse:
    """Reset all movement metrics (admin only)."""
    try:
        from ..game.movement_monitor import reset_movement_monitor

        reset_movement_monitor()
        return MessageResponse(message="Metrics reset successfully")
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Metrics reset errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "reset_metrics"
        raise LoggedHTTPException(status_code=500, detail=f"Error resetting metrics: {str(e)}", context=context) from e


@monitoring_router.get("/performance-summary", response_model=PerformanceSummaryResponse)
async def get_performance_summary(request: Request) -> PerformanceSummaryResponse:
    """Get a human-readable performance summary."""
    try:
        monitor = get_movement_monitor()
        # Use service method that handles formatting internally
        summary = monitor.get_performance_summary()

        return PerformanceSummaryResponse(**summary)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Performance summary errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_performance_summary"
        raise LoggedHTTPException(status_code=500, detail=f"Error retrieving summary: {str(e)}", context=context) from e


@monitoring_router.get("/memory", response_model=MemoryStatsResponse)
async def get_memory_stats(request: Request) -> MemoryStatsResponse:
    """Get comprehensive memory and connection statistics."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        memory_stats = connection_manager.get_memory_stats()
        memory_stats["timestamp"] = datetime.now(UTC).isoformat()

        return MemoryStatsResponse(**memory_stats)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_memory_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving memory stats: {str(e)}", context=context
        ) from e


@monitoring_router.get("/memory-alerts", response_model=MemoryAlertsResponse)
async def get_memory_alerts(request: Request) -> MemoryAlertsResponse:
    """Get memory-related alerts and warnings."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        alerts = connection_manager.get_memory_alerts()

        return MemoryAlertsResponse(alerts=alerts, alert_count=len(alerts), timestamp=datetime.now(UTC).isoformat())
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory alerts errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_memory_alerts"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving memory alerts: {str(e)}", context=context
        ) from e


@monitoring_router.post("/memory/cleanup", response_model=MessageResponse)
async def force_memory_cleanup(request: Request) -> MessageResponse:
    """Force immediate memory cleanup (admin only)."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        await connection_manager.force_cleanup()
        return MessageResponse(message="Memory cleanup completed successfully")
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory cleanup errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "force_memory_cleanup"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error during memory cleanup: {str(e)}", context=context
        ) from e


@monitoring_router.get("/dual-connections", response_model=DualConnectionStatsResponse)
async def get_dual_connection_stats(request: Request) -> DualConnectionStatsResponse:
    """Get comprehensive dual connection statistics."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        dual_connection_stats = connection_manager.get_dual_connection_stats()
        return DualConnectionStatsResponse(**dual_connection_stats)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Connection stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_dual_connection_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving dual connection stats: {str(e)}", context=context
        ) from e


@monitoring_router.get("/performance", response_model=PerformanceStatsResponse)
async def get_performance_stats(request: Request) -> PerformanceStatsResponse:
    """Get connection performance statistics."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        performance_stats = connection_manager.get_performance_stats()
        return PerformanceStatsResponse(**performance_stats)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Performance stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_performance_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving performance stats: {str(e)}", context=context
        ) from e


@monitoring_router.get("/connection-health", response_model=ConnectionHealthStatsResponse)
async def get_connection_health_stats(request: Request) -> ConnectionHealthStatsResponse:
    """Get connection health statistics."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        health_stats = connection_manager.get_connection_health_stats()
        return ConnectionHealthStatsResponse(**health_stats)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_connection_health_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving connection health stats: {str(e)}", context=context
        ) from e


@monitoring_router.get("/health", response_model=HealthResponse)
async def get_health_status(request: Request) -> HealthResponse | JSONResponse:
    """
    Get comprehensive system health status with timeout protection.

    This endpoint validates all critical components:
    - Server metrics (CPU, memory, uptime)
    - Database connectivity (actual query validation)
    - Connection manager health
    - Event loop health

    Returns appropriate HTTP status codes:
    - 200 OK: System healthy or degraded (status in response body)
    - 503 Service Unavailable: System unhealthy
    - 500 Internal Server Error: Health check itself failed
    """
    import asyncio

    try:
        connection_manager = _resolve_connection_manager_from_request(request)
        health_service = get_health_service(connection_manager=connection_manager)

        # Use async health check with timeout protection
        try:
            # Get component health with async validation
            server_health = health_service.get_server_component_health()
            database_health = await asyncio.wait_for(
                health_service.get_database_component_health_async(),
                timeout=health_service.health_check_timeout_seconds,
            )
            connections_health = health_service.get_connections_component_health()

            # Create components object
            from ..models.health import HealthComponents

            components = HealthComponents(
                server=server_health,
                database=database_health,
                connections=connections_health,
            )

            # Determine overall status
            overall_status = health_service.determine_overall_status(components)

            # Generate alerts
            alerts = health_service.generate_alerts(components)

            # Update health check statistics
            health_service.health_check_count += 1
            health_service.last_health_check = datetime.now(UTC)

            # Get version from project configuration
            import importlib.metadata

            try:
                version = importlib.metadata.version("mythosmud")
            except importlib.metadata.PackageNotFoundError:
                version = "0.1.0"  # Fallback version

            health_response = HealthResponse(
                status=overall_status,
                timestamp=datetime.now(UTC).isoformat(),
                uptime_seconds=health_service.get_server_uptime(),
                version=version,
                components=components,
                alerts=alerts,
            )

            # Return appropriate HTTP status code based on health status
            if health_response.status == HealthStatus.HEALTHY:
                return health_response
            if health_response.status == HealthStatus.DEGRADED:
                # Return 200 with degraded status in response body
                return health_response
            # UNHEALTHY
            # Return 503 Service Unavailable for unhealthy status
            return JSONResponse(status_code=503, content=health_response.model_dump())

        except TimeoutError:
            # Health check timed out - return unhealthy
            logger.warning("Health check timed out", timeout=health_service.health_check_timeout_seconds)
            error_response = HealthErrorResponse(
                error="Health check timeout",
                detail=f"Health check exceeded timeout of {health_service.health_check_timeout_seconds}s",
                timestamp=datetime.now(UTC).isoformat(),
            )
            context = create_context_from_request(request)
            context.metadata["operation"] = "get_health_status"
            context.metadata["timeout"] = health_service.health_check_timeout_seconds
            raise LoggedHTTPException(status_code=503, detail=error_response.model_dump(), context=context) from None  # type: ignore[arg-type]  # Reason: LoggedHTTPException accepts context parameter, but mypy cannot infer it from FastAPI exception base class signature

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health check errors unpredictable, must return error response
        # Return 500 Internal Server Error if health check itself fails
        error_response = HealthErrorResponse(
            error="Health check failed", detail=str(e), timestamp=datetime.now(UTC).isoformat()
        )
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_health_status"
        raise LoggedHTTPException(status_code=500, detail=error_response.model_dump(), context=context) from e  # type: ignore[arg-type]  # Reason: LoggedHTTPException accepts context parameter, but mypy cannot infer it from FastAPI exception base class signature


# System-level monitoring endpoints (moved from main.py)
# These use the general monitoring dashboard, not the movement monitor


class SystemHealthResponse(BaseModel):
    """Response model for system health check."""

    status: str
    timestamp: str
    performance_score: float
    error_rate: float
    warning_rate: float
    active_users: int


class SystemMetricsResponse(BaseModel):
    """Response model for system metrics."""

    model_config = ConfigDict(extra="allow")


class SystemMonitoringSummaryResponse(BaseModel):
    """Response model for system monitoring summary."""

    model_config = ConfigDict(extra="allow")


class SystemAlertsResponse(BaseModel):
    """Response model for system alerts."""

    alerts: list[dict[str, Any]]


class AlertResolveResponse(BaseModel):
    """Response model for alert resolution."""

    message: str


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
