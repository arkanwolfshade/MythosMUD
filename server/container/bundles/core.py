"""
Core bundle: config, database, tasks, event bus, persistence.

First bundle in initialization order. No dependencies.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.project_paths import normalize_environment

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

# Attributes this bundle owns (for flattening onto container)
CORE_ATTRS = (
    "config",
    "database_manager",
    "task_registry",
    "tracked_task_manager",
    "event_bus",
    "persistence",
    "async_persistence",
)


class CoreBundle:
    """Core infrastructure: config, database, tasks, event bus, persistence."""

    config: Any = None
    database_manager: Any = None
    task_registry: Any = None
    tracked_task_manager: Any = None
    event_bus: Any = None
    persistence: Any = None
    async_persistence: Any = None

    async def initialize(self, _container: ApplicationContainer) -> None:
        """Initialize core services. No dependencies."""
        # Phase 1: Configuration
        logger.debug("Loading configuration...")
        from server.config import get_config

        self.config = get_config()
        logging_environment = self.config.logging.environment
        normalized_environment = normalize_environment(logging_environment)
        logger.info("Configuration loaded", environment=normalized_environment)

        # Phase 2: Database
        logger.debug("Initializing database infrastructure...")
        from server.database import DatabaseManager, init_db
        from server.npc_database import init_npc_db

        self.database_manager = DatabaseManager.get_instance()
        await init_db()
        await init_npc_db()
        logger.info("Database infrastructure initialized")

        # Phase 3: Task management
        logger.debug("Initializing task management...")
        from server.app.task_registry import TaskRegistry
        from server.app.tracked_task_manager import TrackedTaskManager

        self.task_registry = TaskRegistry()
        self.tracked_task_manager = TrackedTaskManager()
        self.tracked_task_manager.set_task_registry(self.task_registry)
        logger.info("Task management initialized")

        # Phase 4: Event system (DistributedEventBus for NATS-backed distribution)
        logger.debug("Initializing event system...")
        from server.events.distributed_event_bus import DistributedEventBus

        self.event_bus = DistributedEventBus(nats_service=None)
        logger.info("Event system initialized (NATS bridge will start when NATS connects)")

        # Phase 5: Persistence
        logger.debug("Initializing persistence layer...")
        from server.async_persistence import AsyncPersistenceLayer

        self.async_persistence = AsyncPersistenceLayer(event_bus=self.event_bus)
        self.persistence = self.async_persistence
        logger.info("Persistence layer initialized (async only)")

        # Phase 5.1: Room cache warmup
        logger.debug("Warming up room cache and connection pool...")
        try:
            await self.async_persistence.warmup_room_cache()
            logger.info("Room cache warmed up successfully")
        # Warmup is best-effort; avoid failing startup on any error.
        except Exception as e:  # pylint: disable=broad-exception-caught
            logger.warning(
                "Room cache warmup failed, will load on first access",
                error=str(e),
                error_type=type(e).__name__,
            )

    async def shutdown(self, _container: ApplicationContainer) -> None:
        """Shutdown core services."""
        # Event bus first (may have pending tasks)
        if self.event_bus is not None:
            try:
                await self.event_bus.shutdown()
                logger.debug("Event bus shutdown")
            except RuntimeError as e:
                logger.error("Error shutting down event bus", error=str(e))

        # Database services
        if self.database_manager is not None:
            try:
                await self.database_manager.close()
                logger.debug("Database connections closed")
            except RuntimeError as e:
                logger.error("Error closing database connections", error=str(e))

        if self.async_persistence is not None:
            try:
                await self.async_persistence.close()
                logger.debug("Async persistence connection pool closed")
            except RuntimeError as e:
                logger.error("Error closing async persistence pool", error=str(e))

        try:
            from server.npc_database import close_npc_db

            await close_npc_db()
            logger.debug("NPC database connections closed")
        except RuntimeError as e:
            logger.error("Error closing NPC database connections", error=str(e))
