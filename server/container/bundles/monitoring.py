"""
Monitoring bundle: performance monitor, exception tracker, dashboard, log aggregator.

No initialization dependencies.
"""

# pyright: reportImportCycles=false
# Reason: container/main.py imports this module (function-scoped) to construct MonitoringBundle;
# this file only imports ApplicationContainer under TYPE_CHECKING for parameter annotations.
# Same precedent as server/models/player.py and server/services/combat_service.py.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

MONITORING_ATTRS = (
    "performance_monitor",
    "exception_tracker",
    "monitoring_dashboard",
    "log_aggregator",
    "memory_leak_collector",
    "health_service",
)


class MonitoringBundle:
    """Monitoring and observability services."""

    performance_monitor: Any = None
    exception_tracker: Any = None
    monitoring_dashboard: Any = None
    log_aggregator: Any = None
    memory_leak_collector: Any = None
    health_service: Any = None

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize monitoring services. Depends on Core/Realtime/Game for injected deps."""
        logger.debug("Initializing monitoring services...")
        from server.monitoring.exception_tracker import ExceptionTracker
        from server.monitoring.memory_leak_metrics import MemoryLeakMetricsCollector
        from server.monitoring.monitoring_dashboard import MonitoringDashboard
        from server.monitoring.performance_monitor import PerformanceMonitor
        from server.services.health_service import HealthService
        from server.structured_logging.log_aggregator import LogAggregator

        self.performance_monitor = PerformanceMonitor()
        self.exception_tracker = ExceptionTracker()
        self.memory_leak_collector = MemoryLeakMetricsCollector()
        self.monitoring_dashboard = MonitoringDashboard(memory_leak_collector=self.memory_leak_collector)
        self.log_aggregator = LogAggregator()
        self.health_service = HealthService(
            connection_manager=getattr(container, "connection_manager", None),
            async_persistence=container.async_persistence,
            room_service=getattr(container, "room_service", None),
        )
        logger.info("Monitoring services initialized")

    async def shutdown(self, _container: ApplicationContainer) -> None:
        """Shutdown log aggregator."""
        if self.log_aggregator is not None:
            try:
                self.log_aggregator.shutdown()
                logger.debug("Log aggregator shutdown")
            except RuntimeError as e:
                logger.error("Error shutting down log aggregator", error=str(e))
