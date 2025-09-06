"""
Monitoring API endpoints for MythosMUD.

This module provides REST API endpoints for accessing movement
system metrics, validation results, and performance data.

As noted in the Pnakotic Manuscripts, proper monitoring APIs
are essential for maintaining oversight of our eldritch systems.
"""

from datetime import UTC, datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..game.movement_monitor import get_movement_monitor
from ..models.health import HealthErrorResponse, HealthResponse, HealthStatus
from ..persistence import get_persistence
from ..realtime.connection_manager import connection_manager
from ..services.health_service import get_health_service

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


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


@router.get("/metrics", response_model=MetricsResponse)
async def get_movement_metrics():
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
        raise HTTPException(status_code=500, detail=f"Error retrieving metrics: {str(e)}") from e


@router.get("/integrity", response_model=IntegrityResponse)
async def validate_room_integrity():
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
        raise HTTPException(status_code=500, detail=f"Error validating integrity: {str(e)}") from e


@router.get("/alerts", response_model=AlertsResponse)
async def get_system_alerts():
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
        raise HTTPException(status_code=500, detail=f"Error retrieving alerts: {str(e)}") from e


@router.post("/reset")
async def reset_metrics():
    """Reset all movement metrics (admin only)."""
    try:
        from ..game.movement_monitor import reset_movement_monitor

        reset_movement_monitor()
        return {"message": "Metrics reset successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error resetting metrics: {str(e)}") from e


@router.get("/performance-summary")
async def get_performance_summary():
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
        raise HTTPException(status_code=500, detail=f"Error retrieving summary: {str(e)}") from e


@router.get("/memory", response_model=MemoryStatsResponse)
async def get_memory_stats():
    """Get comprehensive memory and connection statistics."""
    try:
        import datetime

        memory_stats = connection_manager.get_memory_stats()
        memory_stats["timestamp"] = datetime.datetime.now(datetime.UTC).isoformat()

        return MemoryStatsResponse(**memory_stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving memory stats: {str(e)}") from e


@router.get("/memory-alerts", response_model=MemoryAlertsResponse)
async def get_memory_alerts():
    """Get memory-related alerts and warnings."""
    try:
        import datetime

        alerts = connection_manager.get_memory_alerts()

        return MemoryAlertsResponse(
            alerts=alerts, alert_count=len(alerts), timestamp=datetime.datetime.now(datetime.UTC).isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving memory alerts: {str(e)}") from e


@router.post("/memory/cleanup")
async def force_memory_cleanup():
    """Force immediate memory cleanup (admin only)."""
    try:
        await connection_manager.force_cleanup()
        return {"message": "Memory cleanup completed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during memory cleanup: {str(e)}") from e


@router.get("/dual-connections", response_model=DualConnectionStatsResponse)
async def get_dual_connection_stats():
    """Get comprehensive dual connection statistics."""
    try:
        dual_connection_stats = connection_manager.get_dual_connection_stats()
        return DualConnectionStatsResponse(**dual_connection_stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving dual connection stats: {str(e)}") from e


@router.get("/performance", response_model=PerformanceStatsResponse)
async def get_performance_stats():
    """Get connection performance statistics."""
    try:
        performance_stats = connection_manager.get_performance_stats()
        return PerformanceStatsResponse(**performance_stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving performance stats: {str(e)}") from e


@router.get("/connection-health", response_model=ConnectionHealthStatsResponse)
async def get_connection_health_stats():
    """Get connection health statistics."""
    try:
        health_stats = connection_manager.get_connection_health_stats()
        return ConnectionHealthStatsResponse(**health_stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving connection health stats: {str(e)}") from e


@router.get("/health", response_model=HealthResponse)
async def get_health_status():
    """Get comprehensive system health status."""
    try:
        health_service = get_health_service()
        health_response = health_service.get_health_status()

        # Return appropriate HTTP status code based on health status
        if health_response.status == HealthStatus.HEALTHY:
            return health_response
        elif health_response.status == HealthStatus.DEGRADED:
            # Return 200 with degraded status in response body
            return health_response
        else:  # UNHEALTHY
            # Return 503 Service Unavailable for unhealthy status
            from fastapi.responses import JSONResponse

            return JSONResponse(status_code=503, content=health_response.model_dump())
    except Exception as e:
        # Return 500 Internal Server Error if health check itself fails
        error_response = HealthErrorResponse(
            error="Health check failed", detail=str(e), timestamp=datetime.now(UTC).isoformat()
        )
        raise HTTPException(status_code=500, detail=error_response.model_dump()) from e
