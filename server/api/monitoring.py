"""
Monitoring API endpoints for MythosMUD.

This module provides REST API endpoints for accessing movement
system metrics, validation results, and performance data.

As noted in the Pnakotic Manuscripts, proper monitoring APIs
are essential for maintaining oversight of our eldritch systems.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from ..dependencies import AsyncPersistenceDep
from ..exceptions import LoggedHTTPException
from ..game.movement_monitor import get_movement_monitor
from ..models.health import HealthErrorResponse, HealthResponse, HealthStatus
from ..realtime.connection_manager import resolve_connection_manager
from ..services.health_service import get_health_service
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request
from .monitoring_models import (
    AlertsResponse,
    CacheMetricsResponse,
    ConnectionHealthStatsResponse,
    DualConnectionStatsResponse,
    EventBusMetricsResponse,
    IntegrityResponse,
    MemoryAlertsResponse,
    MemoryLeakMetricsResponse,
    MemoryStatsResponse,
    MessageResponse,
    MetricsResponse,
    PerformanceStatsResponse,
    PerformanceSummaryResponse,
    TaskMetricsResponse,
)

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)

monitoring_router = APIRouter(prefix="/monitoring", tags=["monitoring"])


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

        # Add memory leak metrics from unified collector
        try:
            collector = _resolve_memory_leak_collector()
            leak_metrics = collector.collect_all_metrics()
            # Add memory leak metrics to response
            memory_stats["memory_leak_metrics"] = {
                "connection": leak_metrics.get("connection", {}),
                "event": leak_metrics.get("event", {}),
                "cache": leak_metrics.get("cache", {}),
                "task": leak_metrics.get("task", {}),
                "nats": leak_metrics.get("nats", {}),
                "alerts": collector.check_alerts(leak_metrics),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory leak metrics collection errors should not fail main endpoint
            logger.warning("Failed to collect memory leak metrics", error=str(e))
            memory_stats["memory_leak_metrics"] = {"error": "Failed to collect metrics"}

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

        # Add memory leak metrics (Task 6: Memory Leak Monitoring)
        try:
            collector = _resolve_memory_leak_collector()
            leak_metrics = collector.collect_all_metrics()
            dual_connection_stats["memory_leak_metrics"] = {
                "connection": leak_metrics.get("connection", {}),
                "alerts": collector.check_alerts(leak_metrics),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory leak metrics errors should not fail main endpoint
            logger.warning("Failed to collect memory leak metrics for dual connections", error=str(e))

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

        # Add memory leak metrics (Task 6: Memory Leak Monitoring)
        try:
            collector = _resolve_memory_leak_collector()
            leak_metrics = collector.collect_all_metrics()
            health_stats["memory_leak_metrics"] = {
                "connection": leak_metrics.get("connection", {}),
                "alerts": collector.check_alerts(leak_metrics),
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory leak metrics errors should not fail main endpoint
            logger.warning("Failed to collect memory leak metrics for connection health", error=str(e))

        return ConnectionHealthStatsResponse(**health_stats)
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Health stats errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_connection_health_stats"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving connection health stats: {str(e)}", context=context
        ) from e


def _resolve_event_bus_from_request(request: Request) -> Any:
    """
    Resolve an EventBus for routes that require it, preferring the container-managed
    instance while remaining compatible with legacy module-level injection used in tests.

    Returns:
        EventBus instance (raises RuntimeError if not configured).
    """
    container = getattr(request.app.state, "container", None)
    event_bus = getattr(container, "event_bus", None) if container else None
    if event_bus is None:
        raise RuntimeError("EventBus is not configured")
    return event_bus


@monitoring_router.get("/eventbus", response_model=EventBusMetricsResponse)
async def get_eventbus_metrics(request: Request) -> EventBusMetricsResponse:
    """
    Get EventBus metrics including subscriber counts and task information.

    Returns metrics for detecting memory leaks in the event subscription system:
    - Subscriber counts by event type (normal: stable, abnormal: growing unbounded)
    - Active task count in EventBus (normal: < 10, warning: > 50)
    - Subscription churn rate (normal: < 0.1, warning: > 0.2 indicates leaks)
    - Recent subscription/unsubscription activity

    Thresholds:
    - subscription_churn_rate: Warning if > 0.1 (10% growth per hour)
    - active_task_count: Warning if > 50 active tasks
    - total_subscribers: Should remain stable, growing count indicates leaks
    """
    try:
        event_bus = _resolve_event_bus_from_request(request)
        subscriber_counts = event_bus.get_all_subscriber_counts()
        lifecycle_metrics = event_bus.get_subscriber_lifecycle_metrics()
        active_task_count = event_bus.get_active_task_count()
        task_details = event_bus.get_active_task_details()

        return EventBusMetricsResponse(
            subscriber_counts_by_type=subscriber_counts,
            total_subscribers=lifecycle_metrics["total_subscribers"],
            active_task_count=active_task_count,
            task_details=task_details,
            subscription_churn_rate=lifecycle_metrics["subscription_churn_rate"],
            subscription_count=lifecycle_metrics["subscription_count"],
            unsubscription_count=lifecycle_metrics["unsubscription_count"],
            recent_subscriptions_last_hour=lifecycle_metrics["recent_subscriptions_last_hour"],
            recent_unsubscriptions_last_hour=lifecycle_metrics["recent_unsubscriptions_last_hour"],
            timestamp=datetime.now(UTC).isoformat(),
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: EventBus metrics errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_eventbus_metrics"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving EventBus metrics: {str(e)}", context=context
        ) from e


def _resolve_cache_manager_from_request(request: Request) -> Any:
    """
    Resolve a CacheManager for routes that require it, preferring the container-managed
    instance while remaining compatible with legacy module-level injection used in tests.

    Returns:
        CacheManager instance (raises RuntimeError if not configured).
    """
    # Try to get from container first
    container = getattr(request.app.state, "container", None)
    if container:
        # CacheManager might be in container or accessible via cache service
        cache_manager = getattr(container, "cache_manager", None)
        if cache_manager:
            return cache_manager

    # Fallback to global cache manager
    from ..caching.lru_cache import get_cache_manager

    return get_cache_manager()


@monitoring_router.get("/caches", response_model=CacheMetricsResponse)
async def get_cache_metrics(request: Request) -> CacheMetricsResponse:
    """
    Get cache metrics including sizes, hit rates, and expiration rates.

    Returns metrics for detecting memory leaks in cache management:
    - Cache sizes for all caches (normal: within max_size, abnormal: exceeds max_size)
    - Cache hit rates (normal: > 0.7, low indicates cache issues)
    - Expired entry counts (indicates TTL working correctly)
    - Expiration rates (normal: varies by cache, high indicates TTL working)
    - Capacity utilization (normal: < 100%, warning: > 110% indicates leak)

    Thresholds:
    - capacity_utilization: Warning if > 1.1 (110% of max_size)
    - cache_sizes: Warning if any cache exceeds its max_size
    - expiration_rates: High rates are normal for TTL caches, low rates with high sizes indicate leaks
    """
    try:
        cache_manager = _resolve_cache_manager_from_request(request)
        all_stats = cache_manager.get_all_stats()

        # Extract metrics from stats
        cache_sizes = {name: stats.get("size", 0) for name, stats in all_stats.items()}
        cache_hit_rates = {name: stats.get("hit_rate", 0.0) for name, stats in all_stats.items()}
        expired_entry_counts = {name: stats.get("expired_count", 0) for name, stats in all_stats.items()}
        expiration_rates = {name: stats.get("expiration_rate", 0.0) for name, stats in all_stats.items()}
        capacity_utilization = {name: stats.get("capacity_utilization", 0.0) for name, stats in all_stats.items()}

        return CacheMetricsResponse(
            cache_sizes=cache_sizes,
            cache_hit_rates=cache_hit_rates,
            expired_entry_counts=expired_entry_counts,
            expiration_rates=expiration_rates,
            capacity_utilization=capacity_utilization,
            cache_stats=all_stats,
            timestamp=datetime.now(UTC).isoformat(),
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Cache metrics errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_cache_metrics"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving cache metrics: {str(e)}", context=context
        ) from e


def _resolve_task_registry() -> Any:
    """
    Resolve a TaskRegistry for routes that require it.

    Returns:
        TaskRegistry instance (raises RuntimeError if not configured).
    """
    from ..app.task_registry import get_registry

    return get_registry()


@monitoring_router.get("/tasks", response_model=TaskMetricsResponse)
async def get_task_metrics(request: Request) -> TaskMetricsResponse:
    """
    Get TaskRegistry metrics including task counts and lifecycle information.

    Returns metrics for detecting memory leaks in task management:
    - Active task count (normal: stable, abnormal: growing unbounded)
    - Task breakdown by type and service
    - Task creation and completion rates (should be balanced)
    - Orphaned task count (normal: 0, warning: > 5)

    Thresholds:
    - task_growth_rate: Warning if > 0.2 (20% growth per hour)
    - orphaned_task_count: Warning if > 5
    - active_task_count: Should remain relatively stable, growing count indicates leaks
    """
    try:
        task_registry = _resolve_task_registry()
        lifecycle_metrics = task_registry.get_task_lifecycle_metrics()

        return TaskMetricsResponse(
            active_task_count=lifecycle_metrics["active_task_count"],
            task_creation_count=lifecycle_metrics["task_creation_count"],
            task_completion_count=lifecycle_metrics["task_completion_count"],
            task_cancellation_count=lifecycle_metrics["task_cancellation_count"],
            tasks_by_type=lifecycle_metrics["tasks_by_type"],
            tasks_by_service=lifecycle_metrics["tasks_by_service"],
            task_creation_rate=lifecycle_metrics["task_creation_rate"],
            task_completion_rate=lifecycle_metrics["task_completion_rate"],
            orphaned_task_count=lifecycle_metrics["orphaned_task_count"],
            lifecycle_tasks_count=lifecycle_metrics["lifecycle_tasks_count"],
            timestamp=datetime.now(UTC).isoformat(),
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Task metrics errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_task_metrics"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving task metrics: {str(e)}", context=context
        ) from e


# Module-level singleton instance for MemoryLeakMetricsCollector
_memory_leak_collector_instance: Any = None  # pylint: disable=invalid-name  # Reason: Module-level singleton pattern uses underscore prefix to indicate private module variable, not a constant


def _resolve_memory_leak_collector() -> Any:
    """
    Get or create MemoryLeakMetricsCollector instance.

    Returns:
        MemoryLeakMetricsCollector instance
    """
    global _memory_leak_collector_instance  # pylint: disable=global-statement  # Reason: Module-level singleton pattern requires global
    from ..monitoring.memory_leak_metrics import MemoryLeakMetricsCollector

    if _memory_leak_collector_instance is None:
        _memory_leak_collector_instance = MemoryLeakMetricsCollector()
    return _memory_leak_collector_instance


@monitoring_router.get("/memory-leaks", response_model=MemoryLeakMetricsResponse)
async def get_memory_leak_metrics(request: Request) -> MemoryLeakMetricsResponse:
    """
    Get comprehensive memory leak metrics from all sources.

    Returns aggregated metrics from all monitoring sources for comprehensive
    memory leak detection. Includes connection, event, cache, task, and NATS metrics
    along with growth rate calculations and automated alerts.

    This endpoint provides:
    - Connection metrics (websockets, metadata, orphaned connections)
    - Event system metrics (subscribers, tasks, churn rates)
    - Cache metrics (sizes, expiration, utilization)
    - Task metrics (counts, lifecycle, orphaned tasks)
    - NATS metrics (subscriptions, cleanup status)
    - Growth rates (calculated from historical data)
    - Automated alerts (based on configured thresholds)

    Thresholds (configured in MemoryLeakMetricsCollector):
    - closed_websockets_max: 5000 (warning), 10000 (critical)
    - subscriber_growth_rate: 0.1 (10% per period)
    - cache_size_limit_factor: 1.1 (110% of max_size)
    - task_growth_rate: 0.2 (20% per period)

    Example normal values:
    - closed_websockets_count: < 1000
    - active_to_player_ratio: 0.8-1.2
    - subscription_churn_rate: < 0.1
    - capacity_utilization: < 1.0

    Example abnormal values (indicate potential leaks):
    - closed_websockets_count: > 5000
    - active_to_player_ratio: > 2.0
    - subscription_churn_rate: > 0.2
    - capacity_utilization: > 1.1
    - orphaned_connections: > 10
    - orphaned_task_count: > 5
    """
    try:
        collector = _resolve_memory_leak_collector()
        metrics = collector.collect_all_metrics()
        growth_rates = collector.calculate_growth_rates()
        alerts = collector.check_alerts(metrics)

        return MemoryLeakMetricsResponse(
            connection=metrics.get("connection", {}),
            event=metrics.get("event", {}),
            cache=metrics.get("cache", {}),
            task=metrics.get("task", {}),
            nats=metrics.get("nats", {}),
            growth_rates=growth_rates,
            alerts=alerts,
            timestamp=metrics.get("timestamp", 0.0),
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Memory leak metrics errors unpredictable, must create error context
        context = create_context_from_request(request)
        context.metadata["operation"] = "get_memory_leak_metrics"
        raise LoggedHTTPException(
            status_code=500, detail=f"Error retrieving memory leak metrics: {str(e)}", context=context
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
