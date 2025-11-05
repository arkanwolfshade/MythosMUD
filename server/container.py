"""
Dependency Injection Container for MythosMUD.

This module implements the Application Container pattern to manage all service
dependencies and eliminate global singleton anti-patterns throughout the codebase.

As noted in the Necronomicon: "The binding of services must be explicit and
orderly, lest the chaos of global state consume the very fabric of our architecture."

ARCHITECTURE NOTES:
- Replaces 19+ module-level global singletons with explicit dependency injection
- Provides single source of truth for service lifecycle management
- Enables proper testing through constructor injection
- Follows Dependency Inversion Principle (depend on abstractions)

USAGE:
    # In application startup (lifespan.py):
    container = ApplicationContainer()
    await container.initialize()
    app.state.container = container

    # In dependency injection (dependencies.py):
    def get_player_service(request: Request) -> PlayerService:
        return request.app.state.container.player_service

    # In tests:
    container = ApplicationContainer()
    await container.initialize()
    player_service = container.player_service  # No global state!
"""

import asyncio
import threading
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .app.task_registry import TaskRegistry
    from .app.tracked_task_manager import TrackedTaskManager
    from .async_persistence import AsyncPersistenceLayer
    from .caching.cache_service import ProfessionCacheService, RoomCacheService
    from .config.models import AppConfig
    from .database import DatabaseManager
    from .events.event_bus import EventBus
    from .game.player_service import PlayerService
    from .game.room_service import RoomService
    from .logging.log_aggregator import LogAggregator
    from .monitoring.exception_tracker import ExceptionTracker
    from .monitoring.monitoring_dashboard import MonitoringDashboard
    from .monitoring.performance_monitor import PerformanceMonitor
    from .persistence import PersistenceLayer
    from .realtime.connection_manager import ConnectionManager
    from .realtime.event_handler import RealTimeEventHandler
    from .services.nats_service import NATSService
    from .services.user_manager import UserManager

from .logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class ApplicationContainer:
    """
    Dependency Injection Container for MythosMUD application.

    This container manages the lifecycle and dependencies of all major services,
    replacing the previous global singleton pattern with explicit dependency injection.

    ARCHITECTURE:
    - Singleton behavior maintained at container level (one container per app)
    - Services are NOT singletons - they're instances managed by container
    - Dependencies injected through constructor, not retrieved from globals
    - Thread-safe initialization with proper async/sync coordination

    AI: This is the central nervous system of the application - all services
        flow through here. Maintains proper initialization order and dependency graph.
    """

    _instance: "ApplicationContainer | None" = None
    _lock: threading.Lock = threading.Lock()

    def __init__(self):
        """
        Initialize the container.

        Note: Services are NOT initialized here - use initialize() method.
        This allows container creation without side effects.
        """
        if ApplicationContainer._instance is not None:
            logger.warning("Multiple ApplicationContainer instances created - this may indicate a problem")

        # Configuration - loaded immediately (no async)
        self.config: AppConfig | None = None

        # Core infrastructure
        self.database_manager: DatabaseManager | None = None
        self.task_registry: TaskRegistry | None = None
        self.tracked_task_manager: TrackedTaskManager | None = None

        # Event system
        self.event_bus: EventBus | None = None

        # Persistence layer (sync and async versions)
        self.persistence: PersistenceLayer | None = None
        self.async_persistence: AsyncPersistenceLayer | None = None

        # Real-time communication
        self.connection_manager: ConnectionManager | None = None
        self.real_time_event_handler: RealTimeEventHandler | None = None
        self.nats_service: NATSService | None = None

        # Game services
        self.player_service: PlayerService | None = None
        self.room_service: RoomService | None = None
        self.user_manager: UserManager | None = None

        # Caching services
        self.room_cache_service: RoomCacheService | None = None
        self.profession_cache_service: ProfessionCacheService | None = None

        # Monitoring and logging
        self.performance_monitor: PerformanceMonitor | None = None
        self.exception_tracker: ExceptionTracker | None = None
        self.monitoring_dashboard: MonitoringDashboard | None = None
        self.log_aggregator: LogAggregator | None = None

        # Initialization state
        self._initialized: bool = False
        self._initialization_lock = asyncio.Lock()

        logger.info("ApplicationContainer created (not yet initialized)")

    @classmethod
    def get_instance(cls) -> "ApplicationContainer":
        """
        Get the singleton container instance.

        This method maintains singleton behavior at the container level,
        but individual services are managed instances, not globals.

        Returns:
            ApplicationContainer: The singleton container

        AI: This is the ONLY acceptable use of singleton pattern in the application.
            Everything else should be injected through this container.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """
        Reset the container singleton.

        ONLY use this in tests. Production code should never reset the container.
        """
        with cls._lock:
            if cls._instance is not None:
                # Cleanup happens in shutdown() method
                cls._instance = None
        logger.info("ApplicationContainer instance reset")

    async def initialize(self) -> None:
        """
        Initialize all services in proper dependency order.

        This method must be called during application startup (lifespan context).
        It ensures all services are initialized in the correct order based on
        their dependencies.

        INITIALIZATION ORDER:
        1. Configuration (no dependencies)
        2. Database infrastructure (depends on config)
        3. Task management (depends on config)
        4. Event system (depends on task management)
        5. Persistence (depends on database, event bus)
        6. Real-time communication (depends on persistence, event bus)
        7. Game services (depends on persistence)
        8. Monitoring (depends on everything)

        Raises:
            RuntimeError: If initialization fails or is called multiple times
        """
        async with self._initialization_lock:
            if self._initialized:
                logger.warning("Container already initialized - skipping re-initialization")
                return

            logger.info("Initializing ApplicationContainer...")

            try:
                # Phase 1: Configuration (no dependencies)
                logger.debug("Loading configuration...")
                from .config import get_config

                self.config = get_config()
                logger.info("Configuration loaded", environment=self.config.logging.environment)

                # Phase 2: Database infrastructure
                logger.debug("Initializing database infrastructure...")
                from .database import DatabaseManager, init_db
                from .npc_database import init_npc_db

                self.database_manager = DatabaseManager.get_instance()
                await init_db()
                await init_npc_db()
                logger.info("Database infrastructure initialized")

                # Phase 3: Task management
                logger.debug("Initializing task management...")
                from .app.task_registry import TaskRegistry
                from .app.tracked_task_manager import TrackedTaskManager

                self.task_registry = TaskRegistry()
                self.tracked_task_manager = TrackedTaskManager()
                self.tracked_task_manager.set_task_registry(self.task_registry)
                logger.info("Task management initialized")

                # Phase 4: Event system
                logger.debug("Initializing event system...")
                from .events.event_bus import EventBus

                self.event_bus = EventBus()  # EventBus doesn't accept task_registry parameter
                logger.info("Event system initialized")

                # Phase 5: Persistence layer (both sync and async versions)
                logger.debug("Initializing persistence layer...")
                from .async_persistence import AsyncPersistenceLayer
                from .persistence import PersistenceLayer

                self.persistence = PersistenceLayer(event_bus=self.event_bus)
                self.async_persistence = AsyncPersistenceLayer(event_bus=self.event_bus)
                logger.info("Persistence layers initialized (sync and async)")

                # Phase 6: Real-time communication
                logger.debug("Initializing real-time communication...")
                from .realtime.connection_manager import ConnectionManager
                from .realtime.event_handler import RealTimeEventHandler
                from .services.nats_service import NATSService

                # Initialize NATS service if enabled
                if self.config.nats.enabled:
                    self.nats_service = NATSService(config=self.config.nats)
                    await self.nats_service.connect()
                    logger.info("NATS service connected")
                else:
                    logger.warning("NATS service disabled in configuration")

                # Initialize real-time event handler with event bus
                self.real_time_event_handler = RealTimeEventHandler(
                    event_bus=self.event_bus, task_registry=self.task_registry
                )

                # Initialize connection manager (no singleton - direct instantiation)
                self.connection_manager = ConnectionManager()
                self.connection_manager.persistence = self.persistence
                self.connection_manager._event_bus = self.event_bus
                logger.info("Real-time communication initialized")

                # Phase 7: Game services
                logger.debug("Initializing game services...")
                from .game.player_service import PlayerService
                from .game.room_service import RoomService
                from .services.user_manager import UserManager

                self.player_service = PlayerService(persistence=self.persistence)
                self.room_service = RoomService(persistence=self.persistence)

                # UserManager requires environment-aware data directory
                from pathlib import Path

                current_file = Path(__file__).resolve()
                project_root = current_file.parent
                while project_root.parent != project_root:
                    if (project_root / "pyproject.toml").exists():
                        break
                    project_root = project_root.parent

                user_management_dir = project_root / "data" / self.config.logging.environment / "user_management"
                self.user_manager = UserManager(data_dir=user_management_dir)
                logger.info("Game services initialized")

                # Phase 8: Caching services (optional, may fail gracefully)
                logger.debug("Initializing caching services...")
                try:
                    from .caching.cache_service import ProfessionCacheService, RoomCacheService

                    self.room_cache_service = RoomCacheService(self.persistence)
                    self.profession_cache_service = ProfessionCacheService(self.persistence)
                    logger.info("Caching services initialized")
                except RuntimeError as e:
                    logger.warning(
                        "Caching services initialization failed - will use persistence directly", error=str(e)
                    )
                    self.room_cache_service = None
                    self.profession_cache_service = None

                # Phase 9: Monitoring and observability
                logger.debug("Initializing monitoring services...")
                from .logging.log_aggregator import LogAggregator
                from .monitoring.exception_tracker import ExceptionTracker
                from .monitoring.monitoring_dashboard import MonitoringDashboard
                from .monitoring.performance_monitor import PerformanceMonitor

                # Initialize monitoring services directly (no singleton pattern)
                self.performance_monitor = PerformanceMonitor()
                self.exception_tracker = ExceptionTracker()
                self.monitoring_dashboard = MonitoringDashboard()  # No constructor params
                self.log_aggregator = LogAggregator()
                logger.info("Monitoring services initialized")

                self._initialized = True
                logger.info(
                    "ApplicationContainer initialization complete",
                    services_initialized=[
                        "config",
                        "database",
                        "event_bus",
                        "persistence",
                        "connection_manager",
                        "player_service",
                        "room_service",
                        "user_manager",
                        "monitoring",
                    ],
                )

            except Exception as e:
                logger.error("ApplicationContainer initialization failed", error=str(e), exc_info=True)
                # Cleanup on failure
                await self.shutdown()
                raise RuntimeError(f"Failed to initialize application container: {e}") from e

    async def shutdown(self) -> None:
        """
        Shutdown all services in reverse dependency order.

        This ensures proper cleanup of resources and prevents resource leaks.
        Should be called during application shutdown.
        """
        logger.info("Shutting down ApplicationContainer...")

        try:
            # Shutdown in reverse order of initialization

            # 1. Stop monitoring services
            if self.log_aggregator is not None:
                try:
                    self.log_aggregator.shutdown()
                    logger.debug("Log aggregator shutdown")
                except Exception as e:
                    logger.error("Error shutting down log aggregator", error=str(e))

            # 2. Stop real-time services
            if self.nats_service is not None:
                try:
                    await self.nats_service.disconnect()
                    logger.debug("NATS service disconnected")
                except Exception as e:
                    logger.error("Error disconnecting NATS service", error=str(e))

            # 3. Stop event bus
            if self.event_bus is not None:
                try:
                    await self.event_bus.shutdown()
                    logger.debug("Event bus shutdown")
                except Exception as e:
                    logger.error("Error shutting down event bus", error=str(e))

            # 4. Close database connections
            if self.database_manager is not None:
                try:
                    await self.database_manager.close()
                    logger.debug("Database connections closed")
                except Exception as e:
                    logger.error("Error closing database connections", error=str(e))

            logger.info("ApplicationContainer shutdown complete")

        except Exception as e:
            logger.error("Error during ApplicationContainer shutdown", error=str(e), exc_info=True)
            # Don't re-raise - best effort cleanup

    def get_service(self, service_name: str):
        """
        Get a service by name.

        This is a convenience method for dynamic service access.
        Prefer direct attribute access (container.player_service) when possible.

        Args:
            service_name: Name of the service to retrieve

        Returns:
            The requested service instance

        Raises:
            ValueError: If service name is invalid or not initialized
        """
        if not self._initialized:
            raise RuntimeError("Container not initialized - call initialize() first")

        if not hasattr(self, service_name):
            raise ValueError(f"Unknown service: {service_name}")

        service = getattr(self, service_name)
        if service is None:
            raise ValueError(f"Service not initialized: {service_name}")

        return service

    @property
    def is_initialized(self) -> bool:
        """Check if container is fully initialized."""
        return self._initialized


# Container factory function for backward compatibility
def get_container() -> ApplicationContainer:
    """
    Get the application container singleton.

    This is a convenience function that maintains backward compatibility
    with the previous singleton pattern while using the new container.

    Returns:
        ApplicationContainer: The singleton container

    Note: Prefer explicit dependency injection over using this function.
          This exists primarily for gradual migration.
    """
    return ApplicationContainer.get_instance()


def reset_container() -> None:
    """
    Reset the container singleton.

    ONLY use this in tests. Production code should never reset the container.
    """
    ApplicationContainer.reset_instance()
