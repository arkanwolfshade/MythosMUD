"""
Monitoring API response models for MythosMUD.

This module contains Pydantic response models used by monitoring API endpoints.

As noted in the Pnakotic Manuscripts, proper data models ensure
consistent responses from our eldritch monitoring systems.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict


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

    memory: dict[str, Any]
    connections: dict[str, Any]
    data_structures: dict[str, Any]
    cleanup_stats: dict[str, Any]
    memory_monitor: dict[str, Any]
    timestamp: str


class MemoryAlertsResponse(BaseModel):
    """Response model for memory alerts."""

    alerts: list[str]
    alert_count: int
    timestamp: str


class DualConnectionStatsResponse(BaseModel):
    """Response model for dual connection statistics."""

    connection_distribution: dict[str, Any]
    connection_health: dict[str, Any]
    session_metrics: dict[str, Any]
    connection_lifecycle: dict[str, Any]
    performance_metrics: dict[str, Any]
    timestamp: float


class PerformanceStatsResponse(BaseModel):
    """Response model for connection performance statistics."""

    connection_establishment: dict[str, Any]
    message_delivery: dict[str, Any]
    disconnections: dict[str, Any]
    session_management: dict[str, Any]
    health_monitoring: dict[str, Any]
    timestamp: float


class ConnectionHealthStatsResponse(BaseModel):
    """Response model for connection health statistics."""

    overall_health: dict[str, Any]
    connection_type_health: dict[str, Any]
    connection_lifecycle: dict[str, Any]
    session_health: dict[str, Any]
    health_trends: dict[str, Any]
    timestamp: float


class EventBusMetricsResponse(BaseModel):
    """Response model for EventBus metrics."""

    subscriber_counts_by_type: dict[str, int]
    total_subscribers: int
    active_task_count: int
    task_details: list[dict[str, Any]]
    subscription_churn_rate: float
    subscription_count: int
    unsubscription_count: int
    recent_subscriptions_last_hour: int
    recent_unsubscriptions_last_hour: int
    timestamp: str


class CacheMetricsResponse(BaseModel):
    """Response model for cache metrics."""

    cache_sizes: dict[str, int]
    cache_hit_rates: dict[str, float]
    expired_entry_counts: dict[str, int]
    expiration_rates: dict[str, float]
    capacity_utilization: dict[str, float]
    cache_stats: dict[str, dict[str, Any]]
    timestamp: str


class TaskMetricsResponse(BaseModel):
    """Response model for TaskRegistry metrics."""

    active_task_count: int
    task_creation_count: int
    task_completion_count: int
    task_cancellation_count: int
    tasks_by_type: dict[str, int]
    tasks_by_service: dict[str, int]
    task_creation_rate: int
    task_completion_rate: int
    orphaned_task_count: int
    lifecycle_tasks_count: int
    timestamp: str


class MemoryLeakMetricsResponse(BaseModel):
    """Response model for comprehensive memory leak metrics."""

    connection: dict[str, Any]
    event: dict[str, Any]
    cache: dict[str, Any]
    task: dict[str, Any]
    nats: dict[str, Any]
    growth_rates: dict[str, float]
    alerts: list[str]
    timestamp: float


class MessageResponse(BaseModel):
    """Generic response model for operations that return a simple message."""

    message: str


class PerformanceSummaryResponse(BaseModel):
    """Response model for performance summary endpoint."""

    summary: dict[str, Any]
    alerts: list[dict[str, Any]]
    timestamp: str


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
