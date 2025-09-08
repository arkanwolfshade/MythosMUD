"""
Health monitoring models for MythosMUD.

This module contains Pydantic models for health endpoint responses,
providing structured data for system health monitoring and diagnostics.

As noted in the Pnakotic Manuscripts, proper monitoring of our eldritch
systems is essential for maintaining the delicate balance between order
and chaos in our digital realm.
"""

from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class HealthStatus(str, Enum):
    """Health status enumeration for system components."""

    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


class ServerComponent(BaseModel):
    """Server component health status and metrics."""

    status: HealthStatus = Field(..., description="Server health status")
    uptime_seconds: float = Field(..., description="Server uptime in seconds")
    memory_usage_mb: float = Field(..., description="Memory usage in MB")
    cpu_usage_percent: float = Field(..., description="CPU usage percentage")


class DatabaseComponent(BaseModel):
    """Database component health status and metrics."""

    status: HealthStatus = Field(..., description="Database health status")
    connection_count: int = Field(..., description="Active database connections")
    last_query_time_ms: float | None = Field(None, description="Last query response time in milliseconds")


class ConnectionsComponent(BaseModel):
    """Connection manager health status and metrics."""

    status: HealthStatus = Field(..., description="Connection manager health status")
    active_connections: int = Field(..., description="Current active connections")
    max_connections: int = Field(..., description="Maximum allowed connections")
    connection_rate_per_minute: float = Field(..., description="Connection rate per minute")


class HealthComponents(BaseModel):
    """Health status for all system components."""

    server: ServerComponent = Field(..., description="Server component health")
    database: DatabaseComponent = Field(..., description="Database component health")
    connections: ConnectionsComponent = Field(..., description="Connection manager health")


class HealthResponse(BaseModel):
    """Complete health response for the system."""

    status: HealthStatus = Field(..., description="Overall system health status")
    timestamp: str = Field(..., description="ISO-8601 timestamp of health check")
    uptime_seconds: float = Field(..., description="Server uptime in seconds")
    version: str = Field(..., description="Server version")
    components: HealthComponents = Field(..., description="Individual component health status")
    alerts: list[str] = Field(default_factory=list, description="List of active alerts")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "healthy",
                "timestamp": "2025-08-27T15:30:45.123456Z",
                "uptime_seconds": 12345.67,
                "version": "0.1.0",
                "components": {
                    "server": {
                        "status": "healthy",
                        "uptime_seconds": 12345.67,
                        "memory_usage_mb": 256.5,
                        "cpu_usage_percent": 15.2,
                    },
                    "database": {"status": "healthy", "connection_count": 5, "last_query_time_ms": 12.5},
                    "connections": {
                        "status": "healthy",
                        "active_connections": 3,
                        "max_connections": 100,
                        "connection_rate_per_minute": 45.2,
                    },
                },
                "alerts": [],
            }
        }
    )


class HealthErrorResponse(BaseModel):
    """Error response for health check failures."""

    error: str = Field(..., description="Error message")
    detail: str = Field(..., description="Detailed error information")
    timestamp: str = Field(..., description="ISO-8601 timestamp of error")
