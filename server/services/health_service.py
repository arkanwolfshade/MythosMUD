"""
Health monitoring service for MythosMUD.

This module provides comprehensive system health monitoring including
server metrics, database connectivity, and connection statistics.

As noted in the Pnakotic Manuscripts, proper monitoring of our eldritch
systems is essential for maintaining the delicate balance between order
and chaos in our digital realm.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Health service requires many state tracking attributes

import asyncio
import time
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

import psutil

from ..models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)
from ..realtime.connection_manager import resolve_connection_manager
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..realtime.connection_manager import ConnectionManager
logger = get_logger(__name__)


class HealthService:
    """
    Health monitoring service for MythosMUD server.

    Provides comprehensive health checks for all system components
    including server metrics, database connectivity, and connection statistics.
    """

    def __init__(self, connection_manager: Any | None = None) -> None:
        """
        Initialize the health service.

        Args:
            connection_manager: ConnectionManager instance (optional, for connection stats)

        AI Agent: connection_manager injected via constructor to eliminate global singleton
        """
        self.start_time = time.time()
        self.last_health_check: datetime | None = None
        self.health_check_count = 0
        self.connection_manager = connection_manager  # AI Agent: Injected dependency

        # Performance thresholds
        self.memory_threshold_mb = 1024  # 1GB
        self.cpu_threshold_percent = 80.0
        self.database_timeout_ms = 1000  # 1 second
        self.connection_threshold_percent = 80.0
        self.health_check_timeout_seconds = 5.0  # Overall health check timeout

        logger.info("HealthService initialized")

    def get_server_uptime(self) -> float:
        """Get server uptime in seconds."""
        return time.time() - self.start_time

    def get_memory_usage(self) -> float:
        """Get current memory usage in MB."""
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            return memory_info.rss / 1024 / 1024  # Convert to MB
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: System monitoring errors unpredictable, must return default value to prevent health check failure
            logger.warning("Failed to get memory usage", error=str(e))
            return 0.0

    def get_cpu_usage(self) -> float:
        """Get current CPU usage percentage."""
        try:
            return psutil.cpu_percent(interval=0.1)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: System monitoring errors unpredictable, must return default value to prevent health check failure
            logger.warning("Failed to get CPU usage", error=str(e))
            return 0.0

    def _create_health_response(
        self, status: HealthStatus, connection_count: int, query_time_ms: float | None
    ) -> dict[str, Any]:
        """Create a standardized health check response dictionary.

        Args:
            status: Health status enum value
            connection_count: Number of connections
            query_time_ms: Query time in milliseconds or None

        Returns:
            dict: Standardized health response
        """
        return {
            "status": status,
            "connection_count": connection_count,
            "last_query_time_ms": query_time_ms,
        }

    async def check_database_health_async(self) -> dict[str, Any]:  # pylint: disable=too-many-return-statements  # Reason: Health check function requires multiple return paths for different failure scenarios (no container, no persistence, no pool, timeout, fallback, exception). Extracting all returns would reduce readability.
        """
        Check database connectivity and health with actual query validation.

        This method performs an actual database query to validate connectivity,
        not just service existence. Should be called from async context.

        Returns:
            dict: Database health status with connection count and query time
        """
        try:
            from ..container import ApplicationContainer

            start_time = time.time()
            container = ApplicationContainer.get_instance()

            if not container:
                return self._create_health_response(HealthStatus.UNHEALTHY, 0, None)

            # Get async persistence layer for actual database connectivity check
            async_persistence = getattr(container, "async_persistence", None)
            if async_persistence:
                # Perform actual database query with timeout
                try:
                    query_start = time.time()
                    # SQLAlchemy path: AsyncPersistenceLayer uses get_async_session(), no _pool.
                    # Run a simple SELECT 1 to validate connectivity.
                    pool = getattr(async_persistence, "_pool", None)
                    if pool:
                        # asyncpg-style pool (legacy path)
                        pool_size = getattr(pool, "_size", 0)
                        query_time_ms = (time.time() - query_start) * 1000
                        if pool_size > 0 and query_time_ms < 100:
                            status = HealthStatus.HEALTHY
                        elif pool_size > 0 and query_time_ms < self.database_timeout_ms:
                            status = HealthStatus.DEGRADED
                        else:
                            status = HealthStatus.UNHEALTHY
                        return self._create_health_response(status, pool_size, query_time_ms)

                    # SQLAlchemy path: validate with a real query via get_async_session
                    from sqlalchemy import text

                    from ..database import get_async_session

                    async def _run_ping() -> None:
                        async for session in get_async_session():
                            await session.execute(text("SELECT 1"))
                            break

                    await asyncio.wait_for(
                        _run_ping(),
                        timeout=self.database_timeout_ms / 1000.0,
                    )
                    query_time_ms = (time.time() - query_start) * 1000
                    status = (
                        HealthStatus.HEALTHY
                        if query_time_ms < 100
                        else HealthStatus.DEGRADED
                        if query_time_ms < self.database_timeout_ms
                        else HealthStatus.UNHEALTHY
                    )
                    return self._create_health_response(status, 1, query_time_ms)
                except TimeoutError:
                    logger.warning("Database health check timed out")
                    return self._create_health_response(HealthStatus.UNHEALTHY, 0, self.database_timeout_ms)
            # Fallback: check if room service exists (legacy check)
            room_service = getattr(container, "room_service", None)
            if room_service:
                return self._create_health_response(HealthStatus.DEGRADED, 0, (time.time() - start_time) * 1000)
            return self._create_health_response(HealthStatus.UNHEALTHY, 0, None)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Database health check errors unpredictable, must return fallback
            logger.warning("Database health check failed", error=str(e))
            return self._create_health_response(HealthStatus.UNHEALTHY, 0, None)

    def check_database_health(self) -> dict[str, Any]:
        """
        Check database connectivity and health (sync wrapper).

        For async contexts, use check_database_health_async() instead.
        This method provides backward compatibility for sync callers.
        """
        try:
            from ..container import ApplicationContainer

            start_time = time.time()
            container = ApplicationContainer.get_instance()

            if not container:
                return {
                    "status": HealthStatus.UNHEALTHY,
                    "connection_count": 0,
                    "last_query_time_ms": None,
                }

            # Check if async persistence exists
            async_persistence = getattr(container, "async_persistence", None)
            if async_persistence:
                pool = getattr(async_persistence, "_pool", None)
                if pool:
                    pool_size = getattr(pool, "_size", 0)
                    query_time_ms = (time.time() - start_time) * 1000

                    if pool_size > 0 and query_time_ms < 100:
                        status = HealthStatus.HEALTHY
                    elif pool_size > 0 and query_time_ms < self.database_timeout_ms:
                        status = HealthStatus.DEGRADED
                    else:
                        status = HealthStatus.UNHEALTHY

                    return {
                        "status": status,
                        "connection_count": pool_size,
                        "last_query_time_ms": query_time_ms,
                    }

            # Fallback: service existence check
            room_service = getattr(container, "room_service", None)
            if room_service:
                return {
                    "status": HealthStatus.DEGRADED,  # Degraded because we can't validate connectivity
                    "connection_count": 0,
                    "last_query_time_ms": (time.time() - start_time) * 1000,
                }
            return {
                "status": HealthStatus.UNHEALTHY,
                "connection_count": 0,
                "last_query_time_ms": None,
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Database health check errors unpredictable, must return fallback
            logger.warning("Database health check failed", error=str(e))
            return {
                "status": HealthStatus.UNHEALTHY,
                "connection_count": 0,
                "last_query_time_ms": None,
            }

    def check_connections_health(self) -> dict[str, Any]:
        """Check connection manager health."""
        try:
            # AI Agent: Use injected connection_manager instead of global import
            if not self.connection_manager:
                fallback_manager = resolve_connection_manager()
                if fallback_manager:
                    self.connection_manager = fallback_manager
                else:
                    logger.warning("Connection manager not available for health check")
                    return {
                        "status": HealthStatus.UNHEALTHY,
                        "active_connections": 0,
                        "max_connections": 0,
                        "connection_rate_per_minute": 0.0,
                    }

            memory_stats = self.connection_manager.get_memory_stats()
            connections_data = memory_stats.get("connections", {})

            active_connections = connections_data.get("active_connections", 0)
            max_connections = connections_data.get("max_connections", 100)
            connection_rate = connections_data.get("connection_rate_per_minute", 0.0)

            # Determine connection status
            connection_percentage = (active_connections / max_connections) * 100 if max_connections > 0 else 0

            if connection_percentage < 50:
                status = HealthStatus.HEALTHY
            elif connection_percentage < self.connection_threshold_percent:
                status = HealthStatus.DEGRADED
            else:
                status = HealthStatus.UNHEALTHY

            return {
                "status": status,
                "active_connections": active_connections,
                "max_connections": max_connections,
                "connection_rate_per_minute": connection_rate,
            }
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Connection health check errors unpredictable, must return fallback
            logger.warning("Connection health check failed", error=str(e))
            return {
                "status": HealthStatus.UNHEALTHY,
                "active_connections": 0,
                "max_connections": 100,
                "connection_rate_per_minute": 0.0,
            }

    def get_server_component_health(self) -> ServerComponent:
        """Get server component health status."""
        uptime_seconds = self.get_server_uptime()
        memory_usage_mb = self.get_memory_usage()
        cpu_usage_percent = self.get_cpu_usage()

        # Determine server status
        if memory_usage_mb < self.memory_threshold_mb and cpu_usage_percent < self.cpu_threshold_percent:
            status = HealthStatus.HEALTHY
        elif memory_usage_mb < self.memory_threshold_mb * 1.5 and cpu_usage_percent < self.cpu_threshold_percent * 1.2:
            status = HealthStatus.DEGRADED
        else:
            status = HealthStatus.UNHEALTHY

        return ServerComponent(
            status=status,
            uptime_seconds=uptime_seconds,
            memory_usage_mb=memory_usage_mb,
            cpu_usage_percent=cpu_usage_percent,
        )

    async def get_database_component_health_async(self) -> DatabaseComponent:
        """Get database component health status (async version with actual validation)."""
        db_health = await self.check_database_health_async()

        return DatabaseComponent(
            status=db_health["status"],
            connection_count=db_health["connection_count"],
            last_query_time_ms=db_health["last_query_time_ms"],
        )

    def get_database_component_health(self) -> DatabaseComponent:
        """Get database component health status (sync version)."""
        db_health = self.check_database_health()

        return DatabaseComponent(
            status=db_health["status"],
            connection_count=db_health["connection_count"],
            last_query_time_ms=db_health["last_query_time_ms"],
        )

    def get_connections_component_health(self) -> ConnectionsComponent:
        """Get connections component health status."""
        conn_health = self.check_connections_health()

        return ConnectionsComponent(
            status=conn_health["status"],
            active_connections=conn_health["active_connections"],
            max_connections=conn_health["max_connections"],
            connection_rate_per_minute=conn_health["connection_rate_per_minute"],
        )

    def generate_alerts(self, components: HealthComponents) -> list[str]:
        """Generate alerts based on component health."""
        alerts = []

        # Server alerts
        if components.server.status == HealthStatus.DEGRADED:
            alerts.append("Server performance degraded")
        elif components.server.status == HealthStatus.UNHEALTHY:
            alerts.append("Server performance critical")

        if components.server.memory_usage_mb > self.memory_threshold_mb:
            alerts.append(f"High memory usage: {components.server.memory_usage_mb:.1f}MB")

        if components.server.cpu_usage_percent > self.cpu_threshold_percent:
            alerts.append(f"High CPU usage: {components.server.cpu_usage_percent:.1f}%")

        # Database alerts
        if components.database.status == HealthStatus.DEGRADED:
            alerts.append("Database response time elevated")
        elif components.database.status == HealthStatus.UNHEALTHY:
            alerts.append("Database connection issues detected")

        # Connection alerts
        if components.connections.status == HealthStatus.DEGRADED:
            alerts.append("Connection pool utilization high")
        elif components.connections.status == HealthStatus.UNHEALTHY:
            alerts.append("Connection pool at capacity")

        return alerts

    def determine_overall_status(self, components: HealthComponents) -> HealthStatus:
        """Determine overall system health status."""
        # If any component is unhealthy, overall status is unhealthy
        if HealthStatus.UNHEALTHY in (
            components.server.status,
            components.database.status,
            components.connections.status,
        ):
            return HealthStatus.UNHEALTHY

        # If any component is degraded, overall status is degraded
        if HealthStatus.DEGRADED in (
            components.server.status,
            components.database.status,
            components.connections.status,
        ):
            return HealthStatus.DEGRADED

        # All components healthy
        return HealthStatus.HEALTHY

    def get_health_status(self) -> HealthResponse:
        """Get comprehensive health status for the system."""
        try:
            # Get component health
            server_health = self.get_server_component_health()
            database_health = self.get_database_component_health()
            connections_health = self.get_connections_component_health()

            # Create components object
            components = HealthComponents(
                server=server_health,
                database=database_health,
                connections=connections_health,
            )

            # Determine overall status
            overall_status = self.determine_overall_status(components)

            # Generate alerts
            alerts = self.generate_alerts(components)

            # Update health check statistics
            self.health_check_count += 1
            self.last_health_check = datetime.now(UTC)

            # Get version from project configuration
            import importlib.metadata

            try:
                version = importlib.metadata.version("mythosmud")
            except importlib.metadata.PackageNotFoundError:
                version = "0.1.0"  # Fallback version

            return HealthResponse(
                status=overall_status,
                timestamp=datetime.now(UTC).isoformat(),
                uptime_seconds=self.get_server_uptime(),
                version=version,
                components=components,
                alerts=alerts,
            )
        except Exception as e:
            logger.error("Health check failed", error=str(e), exc_info=True)
            raise


# Global health service instance
_health_service: HealthService | None = None  # pylint: disable=invalid-name  # Reason: Private module-level singleton, intentionally uses _ prefix


def get_health_service(connection_manager: "ConnectionManager | None" = None) -> HealthService:
    """
    Get the global health service instance.

    Args:
        connection_manager: Optional ConnectionManager to bind to the service.
            When provided, ensures the singleton tracks the current container-managed instance.
    """
    global _health_service  # pylint: disable=global-statement  # Reason: Singleton pattern requires global variable to maintain single instance across module scope
    if _health_service is None:
        _health_service = HealthService(connection_manager=connection_manager)
    elif connection_manager is not None:
        _health_service.connection_manager = connection_manager
    return _health_service
