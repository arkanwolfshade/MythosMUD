"""
Monitoring bundle: performance monitor, exception tracker, dashboard, log aggregator.

No initialization dependencies.
"""

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
)


class MonitoringBundle:
    """Monitoring and observability services."""

    performance_monitor: Any = None
    exception_tracker: Any = None
    monitoring_dashboard: Any = None
    log_aggregator: Any = None

    async def initialize(self, _container: ApplicationContainer) -> None:
        """Initialize monitoring services. No dependencies."""
        logger.debug("Initializing monitoring services...")
        from server.monitoring.exception_tracker import ExceptionTracker
        from server.monitoring.monitoring_dashboard import MonitoringDashboard
        from server.monitoring.performance_monitor import PerformanceMonitor
        from server.structured_logging.log_aggregator import LogAggregator

        self.performance_monitor = PerformanceMonitor()
        self.exception_tracker = ExceptionTracker()
        self.monitoring_dashboard = MonitoringDashboard()
        self.log_aggregator = LogAggregator()
        logger.info("Monitoring services initialized")

    async def shutdown(self, _container: ApplicationContainer) -> None:
        """Shutdown log aggregator."""
        if self.log_aggregator is not None:
            try:
                self.log_aggregator.shutdown()
                logger.debug("Log aggregator shutdown")
            except RuntimeError as e:
                logger.error("Error shutting down log aggregator", error=str(e))
