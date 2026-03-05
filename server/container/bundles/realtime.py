"""
Realtime bundle: NATS, connection manager, event handler, event publisher.

Depends on CoreBundle (config, event_bus, task_registry, async_persistence).
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

REALTIME_ATTRS = (
    "connection_manager",
    "real_time_event_handler",
    "nats_service",
    "nats_message_handler",
    "event_publisher",
)


class RealtimeBundle:
    """Real-time communication: NATS, connection manager, event handler."""

    connection_manager: Any = None
    real_time_event_handler: Any = None
    nats_service: Any = None
    nats_message_handler: Any = None
    event_publisher: Any = None

    @staticmethod
    def _require_core_services(container: ApplicationContainer) -> None:
        """Raise if any core dependency is missing."""
        if container.config is None:
            raise RuntimeError("Core services must be initialized before RealtimeBundle")
        if container.event_bus is None:
            raise RuntimeError("Core services must be initialized before RealtimeBundle")
        if container.task_registry is None:
            raise RuntimeError("Core services must be initialized before RealtimeBundle")
        if container.async_persistence is None:
            raise RuntimeError("Core services must be initialized before RealtimeBundle")

    async def _connect_nats(self, config: Any, event_bus: Any) -> Any:
        """Connect to NATS if enabled and not unit_test. Returns NATSService or None."""
        from server.services.nats_service import NATSService

        logging_env = getattr(config.logging, "environment", "") if config.logging else ""
        if logging_env == "unit_test":
            logger.debug("NATS skipped for unit test environment", environment=logging_env)
            return None
        if not config.nats.enabled:
            logger.warning("NATS service disabled in configuration")
            return None

        nats_service = NATSService(config=config.nats)
        connect_timeout = getattr(config.nats, "connect_timeout", 5) + 5
        try:
            connected = await asyncio.wait_for(nats_service.connect(), timeout=float(connect_timeout))
            if not connected:
                logger.warning("NATS connect returned False; continuing without NATS")
                return None
            logger.info("NATS service connected")
            if hasattr(event_bus, "set_nats_service"):
                event_bus.set_nats_service(nats_service)
                logger.info("NATS EventBus bridge enabled for distributed domain events")
            return nats_service
        except (TimeoutError, OSError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Startup must not block on NATS; log and continue without NATS
            err_msg = str(e).strip() or type(e).__name__
            logger.warning(
                "NATS connect failed or timed out; continuing without NATS",
                error=err_msg,
                error_type=type(e).__name__,
                url=getattr(config.nats, "url", "nats://localhost:4222"),
            )
            return None

    def _setup_nats_dependent_services(self) -> None:
        """Attach event publisher and message handler when NATS is available."""
        if not self.nats_service:
            self.event_publisher = None
            self.nats_message_handler = None
            logger.info("NATS-dependent services skipped (NATS disabled or not connected)")
            return
        subject_manager = getattr(self.nats_service, "subject_manager", None)
        from server.realtime.event_publisher import EventPublisher
        from server.realtime.nats_message_handler import NATSMessageHandler

        self.event_publisher = EventPublisher(self.nats_service, subject_manager)
        logger.info("Event publisher initialized")
        self.nats_message_handler = NATSMessageHandler(self.nats_service, subject_manager, self.connection_manager)
        logger.info("NATS message handler initialized with injected connection_manager")

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize real-time services. Requires CoreBundle attributes on container."""
        self._require_core_services(container)
        config = container.config
        event_bus = container.event_bus
        task_registry = container.task_registry
        async_persistence = container.async_persistence

        logger.debug("Initializing real-time communication...")
        from server.realtime.connection_manager import ConnectionManager
        from server.realtime.event_handler import RealTimeEventHandler

        self.nats_service = await self._connect_nats(config, event_bus)

        self.connection_manager = ConnectionManager()
        self.connection_manager.async_persistence = async_persistence
        self.connection_manager.room_manager.async_persistence = async_persistence
        self.connection_manager.set_event_bus(event_bus)

        self.real_time_event_handler = RealTimeEventHandler(
            event_bus=event_bus,
            task_registry=task_registry,
            connection_manager=self.connection_manager,
        )

        self._setup_nats_dependent_services()
        logger.info("Real-time communication initialized")

    async def shutdown(self, _container: ApplicationContainer) -> None:
        """Shutdown NATS-related services."""
        if self.nats_message_handler is not None:
            try:
                await self.nats_message_handler.stop()
                logger.debug("NATS message handler stopped")
            except RuntimeError as e:
                logger.error("Error stopping NATS message handler", error=str(e))

        if self.nats_service is not None:
            try:
                await self.nats_service.disconnect()
                logger.debug("NATS service disconnected")
            except RuntimeError as e:
                logger.error("Error disconnecting NATS service", error=str(e))
