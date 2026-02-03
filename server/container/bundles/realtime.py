"""
Realtime bundle: NATS, connection manager, event handler, event publisher.

Depends on CoreBundle (config, event_bus, task_registry, async_persistence).
"""

from __future__ import annotations

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

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize real-time services. Requires CoreBundle attributes on container."""
        config = container.config
        event_bus = container.event_bus
        task_registry = container.task_registry
        async_persistence = container.async_persistence

        if config is None or event_bus is None or task_registry is None or async_persistence is None:
            raise RuntimeError("Core services must be initialized before RealtimeBundle")

        logger.debug("Initializing real-time communication...")
        from server.realtime.connection_manager import ConnectionManager
        from server.realtime.event_handler import RealTimeEventHandler
        from server.services.nats_service import NATSService

        if config.nats.enabled:
            self.nats_service = NATSService(config=config.nats)
            await self.nats_service.connect()
            logger.info("NATS service connected")
            # Start distributed EventBus bridge for cross-instance domain events
            if hasattr(event_bus, "set_nats_service"):
                event_bus.set_nats_service(self.nats_service)
                logger.info("NATS EventBus bridge enabled for distributed domain events")
        else:
            logger.warning("NATS service disabled in configuration")

        self.connection_manager = ConnectionManager()
        self.connection_manager.async_persistence = async_persistence
        self.connection_manager.room_manager.async_persistence = async_persistence
        self.connection_manager.set_event_bus(event_bus)

        self.real_time_event_handler = RealTimeEventHandler(
            event_bus=event_bus,
            task_registry=task_registry,
            connection_manager=self.connection_manager,
        )

        if self.nats_service:
            subject_manager = getattr(self.nats_service, "subject_manager", None)
            from server.realtime.event_publisher import EventPublisher

            self.event_publisher = EventPublisher(self.nats_service, subject_manager)
            logger.info("Event publisher initialized")

            from server.realtime.nats_message_handler import NATSMessageHandler

            self.nats_message_handler = NATSMessageHandler(self.nats_service, subject_manager, self.connection_manager)
            logger.info("NATS message handler initialized with injected connection_manager")
        else:
            self.event_publisher = None
            self.nats_message_handler = None
            logger.info("NATS-dependent services skipped (NATS disabled or not connected)")

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
