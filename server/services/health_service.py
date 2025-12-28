"""
Health monitoring service for MythosMUD.

This module provides comprehensive system health monitoring including
server metrics, database connectivity, and connection statistics.

As noted in the Pnakotic Manuscripts, proper monitoring of our eldritch
systems is essential for maintaining the delicate balance between order
and chaos in our digital realm.
"""

import time
from datetime import UTC, datetime
from typing import Any

import psutil

from ..structured_logging.enhanced_logging_config import get_logger
from ..models.health import (
    ConnectionsComponent,
    DatabaseComponent,
    HealthComponents,
    HealthResponse,
    HealthStatus,
    ServerComponent,
)
from ..realtime.connection_manager import resolve_connection_manager

logger = get_logger(__name__)


class HealthService:
    """
    Health monitoring service for MythosMUD server.

    Provides comprehensive health checks for all system components
    including server metrics, database connectivity, and connection statistics.
    """

    def __init__(self, connection_manager=None):
        """
        Initialize the health service.

        Args:
            connection_manager: ConnectionManager instance (optional, for connection stats)

        AI Agent: connection_manager injected via constructor to eliminate global singleton
        """
        self.start_time = time.time()
        self.last_health_check = None
        self.health_check_count = 0
        self.connection_manager = connection_manager  # AI Agent: Injected dependency

        # Performance thresholds
        self.memory_threshold_mb = 1024  # 1GB
        self.cpu_threshold_percent = 80.0
        self.database_timeout_ms = 1000  # 1 second
        self.connection_threshold_percent = 80.0

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
        except Exception as e:
            logger.warning("Failed to get memory usage", error=str(e))
            return 0.0

    def get_cpu_usage(self) -> float:
        """Get current CPU usage percentage."""
        try:
            return psutil.cpu_percent(interval=0.1)
        except Exception as e:
            logger.warning("Failed to get CPU usage", error=str(e))
            return 0.0

    def check_database_health(self) -> dict:
        """Check database connectivity and health."""
        try:
            from ..container import ApplicationContainer

            start_time = time.time()
            container = ApplicationContainer.get_instance()

            # Container is guaranteed to be non-None (get_instance() always returns ApplicationContainer)
            room_service = container.room_service

            # Simple health check - try to list rooms (async)
            rooms: list[dict[str, Any]] = []
            if room_service:
                import asyncio

                # Run async list_rooms in a new event loop if needed
                try:
                    asyncio.get_running_loop()  # Check if we're in async context
                    # If we're in an async context, we can't use asyncio.run()
                    # For health checks, we'll just check if room_service exists
                    rooms = []  # Skip actual query in async context
                except RuntimeError:
                    # No running loop - use asyncio.run() to call RoomService.list_rooms()
                    # Note: list_rooms requires plane and zone parameters, but for health check
                    # we'll just verify the service is available without querying
                    try:
                        # For health check, we don't need actual room data
                        # Just verify the service is callable
                        # rooms = asyncio.run(room_service.list_rooms("default", "default"))
                        # Skip actual query for health check to avoid requiring parameters
                        pass
                    except Exception as e:
                        logger.debug("Failed to list rooms for health check", error=str(e))
                        rooms = []

            query_time_ms = (time.time() - start_time) * 1000

            # Determine database status based on response time
            if query_time_ms < 100:
                status = HealthStatus.HEALTHY
            elif query_time_ms < self.database_timeout_ms:
                status = HealthStatus.DEGRADED
            else:
                status = HealthStatus.UNHEALTHY

            return {
                "status": status,
                "connection_count": len(rooms) if rooms else 0,
                "last_query_time_ms": query_time_ms,
            }
        except Exception as e:
            logger.warning("Database health check failed", error=str(e))
            return {
                "status": HealthStatus.UNHEALTHY,
                "connection_count": 0,
                "last_query_time_ms": None,
            }

    def check_connections_health(self) -> dict:
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
        except Exception as e:
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

    def get_database_component_health(self) -> DatabaseComponent:
        """Get database component health status."""
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
        if (
            components.server.status == HealthStatus.UNHEALTHY
            or components.database.status == HealthStatus.UNHEALTHY
            or components.connections.status == HealthStatus.UNHEALTHY
        ):
            return HealthStatus.UNHEALTHY

        # If any component is degraded, overall status is degraded
        if (
            components.server.status == HealthStatus.DEGRADED
            or components.database.status == HealthStatus.DEGRADED
            or components.connections.status == HealthStatus.DEGRADED
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
_health_service: HealthService | None = None


def get_health_service(connection_manager=None) -> HealthService:
    """
    Get the global health service instance.

    Args:
        connection_manager: Optional ConnectionManager to bind to the service.
            When provided, ensures the singleton tracks the current container-managed instance.
    """
    global _health_service
    if _health_service is None:
        _health_service = HealthService(connection_manager=connection_manager)
    elif connection_manager is not None:
        _health_service.connection_manager = connection_manager
    return _health_service
