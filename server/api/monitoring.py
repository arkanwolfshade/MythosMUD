"""
Monitoring API endpoints for MythosMUD.

This module provides REST API endpoints for accessing movement
system metrics, validation results, and performance data.

As noted in the Pnakotic Manuscripts, proper monitoring APIs
are essential for maintaining oversight of our eldritch systems.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from ..exceptions import LoggedHTTPException
from ..game.movement_monitor import get_movement_monitor
from ..models.health import HealthErrorResponse, HealthResponse, HealthStatus
from ..persistence import get_persistence
from ..realtime.connection_manager import resolve_connection_manager, set_global_connection_manager
from ..services.health_service import get_health_service
from ..utils.error_logging import create_context_from_request

monitoring_router = APIRouter(prefix="/monitoring", tags=["monitoring"])


def _resolve_connection_manager_from_request(request: Request):
    """
    Resolve a connection manager for routes that require it, preferring the container-managed
    instance while remaining compatible with legacy module-level injection used in tests.
    """
    container = getattr(request.app.state, "container", None)
    candidate = getattr(container, "connection_manager", None) if container else None
    manager = resolve_connection_manager(candidate)
    if manager is not None:
        set_global_connection_manager(manager)
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
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_movement_metrics"
        raise LoggedHTTPException(status_code=500, detail=f"Error retrieving metrics: {str(e)}", context=context) from e


@monitoring_router.get("/integrity", response_model=IntegrityResponse)
async def validate_room_integrity(request: Request) -> IntegrityResponse:
    """Validate room data integrity and return results."""
    try:
        monitor = get_movement_monitor()
        persistence = get_persistence()

        # Get all rooms from persistence
        rooms = {}
        room_list = persistence.list_rooms()
        for room in room_list:
            rooms[room.id] = room

        result = monitor.validate_room_integrity(rooms)
        result["timestamp"] = result["timestamp"].isoformat()

        return IntegrityResponse(**result)
    except Exception as e:
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
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_system_alerts"
        raise LoggedHTTPException(status_code=500, detail=f"Error retrieving alerts: {str(e)}", context=context) from e


@monitoring_router.post("/reset")
async def reset_metrics(request: Request) -> dict[str, str]:
    """Reset all movement metrics (admin only)."""
    try:
        from ..game.movement_monitor import reset_movement_monitor

        reset_movement_monitor()
        return {"message": "Metrics reset successfully"}
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "reset_metrics"
        raise LoggedHTTPException(status_code=500, detail=f"Error resetting metrics: {str(e)}", context=context) from e


@monitoring_router.get("/performance-summary")
async def get_performance_summary(request: Request) -> dict[str, Any]:
    """Get a human-readable performance summary."""
    try:
        monitor = get_movement_monitor()
        metrics = monitor.get_metrics()
        alerts = monitor.get_alerts()

        summary = {
            "summary": {
                "total_movements": metrics["total_movements"],
                "success_rate": f"{metrics['success_rate']:.2%}",
                "avg_movement_time": f"{metrics['avg_movement_time_ms']:.2f}ms",
                "current_concurrent": metrics["current_concurrent_movements"],
                "max_concurrent": metrics["max_concurrent_movements"],
                "integrity_rate": f"{metrics['integrity_rate']:.2%}",
                "uptime": f"{metrics['uptime_seconds']:.1f}s",
                "alert_count": len(alerts),
            },
            "alerts": alerts,
            "timestamp": metrics["timestamp"].isoformat(),
        }

        return summary
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_performance_summary"
        raise LoggedHTTPException(status_code=500, detail=f"Error retrieving summary: {str(e)}", context=context) from e


@monitoring_router.get("/memory", response_model=MemoryStatsResponse)
async def get_memory_stats(request: Request) -> MemoryStatsResponse:
    """Get comprehensive memory and connection statistics."""
    try:
        import datetime

        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        memory_stats = connection_manager.get_memory_stats()
        memory_stats["timestamp"] = datetime.datetime.now(datetime.UTC).isoformat()

        return MemoryStatsResponse(**memory_stats)
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_memory_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving memory stats: {str(e)}", context=context
        ) from e


@monitoring_router.get("/memory-alerts", response_model=MemoryAlertsResponse)
async def get_memory_alerts(request: Request) -> MemoryAlertsResponse:
    """Get memory-related alerts and warnings."""
    try:
        import datetime

        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        alerts = connection_manager.get_memory_alerts()

        return MemoryAlertsResponse(
            alerts=alerts, alert_count=len(alerts), timestamp=datetime.datetime.now(datetime.UTC).isoformat()
        )
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_memory_alerts"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving memory alerts: {str(e)}", context=context
        ) from e


@monitoring_router.post("/memory/cleanup")
async def force_memory_cleanup(request: Request) -> dict[str, str]:
    """Force immediate memory cleanup (admin only)."""
    try:
        # AI Agent: Get connection_manager from container instead of global import
        connection_manager = _resolve_connection_manager_from_request(request)
        await connection_manager.force_cleanup()
        return {"message": "Memory cleanup completed successfully"}
    except Exception as e:
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
    except Exception as e:
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
    except Exception as e:
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
    except Exception as e:
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_connection_health_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving connection health stats: {str(e)}", context=context
        ) from e


@monitoring_router.get("/health", response_model=HealthResponse)
async def get_health_status(request: Request) -> HealthResponse | JSONResponse:
    """Get comprehensive system health status."""
    try:
        connection_manager = _resolve_connection_manager_from_request(request)
        health_service = get_health_service(connection_manager=connection_manager)
        health_response = health_service.get_health_status()

        # Return appropriate HTTP status code based on health status
        if health_response.status == HealthStatus.HEALTHY:
            return health_response
        elif health_response.status == HealthStatus.DEGRADED:
            # Return 200 with degraded status in response body
            return health_response
        else:  # UNHEALTHY
            # Return 503 Service Unavailable for unhealthy status
            return JSONResponse(status_code=503, content=health_response.model_dump())
    except Exception as e:
        # Return 500 Internal Server Error if health check itself fails
        error_response = HealthErrorResponse(
            error="Health check failed", detail=str(e), timestamp=datetime.now(UTC).isoformat()
        )
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_health_status"
        raise LoggedHTTPException(status_code=500, detail=error_response.model_dump(), context=context) from e  # type: ignore[arg-type]
