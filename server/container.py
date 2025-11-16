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
import json
import os
import sqlite3
import threading
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse

if TYPE_CHECKING:
    from .app.task_registry import TaskRegistry
    from .app.tracked_task_manager import TrackedTaskManager
    from .async_persistence import AsyncPersistenceLayer
    from .caching.cache_service import ProfessionCacheService, RoomCacheService
    from .config.models import AppConfig
    from .database import DatabaseManager
    from .events.event_bus import EventBus
    from .game.items.item_factory import ItemFactory
    from .game.items.prototype_registry import PrototypeRegistry
    from .game.player_service import PlayerService
    from .game.room_service import RoomService
    from .logging.log_aggregator import LogAggregator
    from .monitoring.exception_tracker import ExceptionTracker
    from .monitoring.monitoring_dashboard import MonitoringDashboard
    from .monitoring.performance_monitor import PerformanceMonitor
    from .persistence import PersistenceLayer
    from .realtime.connection_manager import ConnectionManager
    from .realtime.event_handler import RealTimeEventHandler
    from .services.holiday_service import HolidayService
    from .services.nats_service import NATSService
    from .services.schedule_service import ScheduleService
    from .services.user_manager import UserManager
    from .time.tick_scheduler import MythosTickScheduler

from .logging.enhanced_logging_config import get_logger
from .utils.project_paths import (
    get_calendar_paths_for_environment,
    get_environment_data_dir,
    get_project_root,
    normalize_environment,
)

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
        self.nats_message_handler: Any | None = None  # NATSMessageHandler type hint would create circular import
        self.event_publisher: Any | None = None  # EventPublisher type hint would create circular import

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

        # Temporal services
        self.holiday_service: HolidayService | None = None
        self.schedule_service: ScheduleService | None = None

        # Mythos timekeeping
        self.mythos_tick_scheduler: MythosTickScheduler | None = None

        # Item system services
        self.item_prototype_registry: PrototypeRegistry | None = None
        self.item_factory: ItemFactory | None = None

        # Initialization state
        self._initialized: bool = False
        self._initialization_lock = asyncio.Lock()
        self._project_root: Path | None = None

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
                project_root = self._get_project_root()
                normalized_environment = normalize_environment(self.config.logging.environment)

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

                from .services.holiday_service import HolidayService
                from .services.schedule_service import ScheduleService
                from .time.time_service import get_mythos_chronicle

                holidays_path, schedules_dir = get_calendar_paths_for_environment(normalized_environment)
                self.holiday_service = HolidayService(
                    chronicle=get_mythos_chronicle(),
                    data_path=holidays_path,
                    environment=normalized_environment,
                )
                self.schedule_service = ScheduleService(
                    schedule_dir=schedules_dir,
                    environment=normalized_environment,
                )
                logger.info(
                    "Temporal schedule and holiday services initialized",
                    holiday_count=len(self.holiday_service.collection.holidays),
                    schedule_entries=self.schedule_service.entry_count if self.schedule_service else 0,
                )

                from .time.tick_scheduler import MythosTickScheduler

                holiday_service = self.holiday_service

                def _resolve_hourly_holidays(mythos_dt: datetime) -> list[str]:
                    if not holiday_service:
                        return []
                    try:
                        active = holiday_service.refresh_active(mythos_dt)
                        return [entry.name for entry in active]
                    except Exception as exc:  # pragma: no cover - defensive logging
                        logger.warning("Failed to resolve holiday window for tick scheduler", error=str(exc))
                        return []

                self.mythos_tick_scheduler = MythosTickScheduler(
                    chronicle=get_mythos_chronicle(),
                    event_bus=self.event_bus,
                    task_registry=self.task_registry,
                    holiday_resolver=_resolve_hourly_holidays,
                )
                logger.info("Mythos tick scheduler prepared")

                # Phase 5: Persistence layer (both sync and async versions)
                logger.debug("Initializing persistence layer...")
                from .async_persistence import AsyncPersistenceLayer
                from .persistence import PersistenceLayer

                self.persistence = PersistenceLayer(event_bus=self.event_bus)
                self.async_persistence = AsyncPersistenceLayer(event_bus=self.event_bus)
                logger.info("Persistence layers initialized (sync and async)")

                # Phase 6: Real-time communication
                logger.debug("Initializing real-time communication...")
                from .realtime import nats_message_handler as nats_module
                from .realtime.connection_manager import ConnectionManager, set_global_connection_manager
                from .realtime.event_handler import RealTimeEventHandler
                from .services.nats_service import NATSService

                # Initialize NATS service if enabled
                if self.config.nats.enabled:
                    self.nats_service = NATSService(config=self.config.nats)
                    await self.nats_service.connect()
                    logger.info("NATS service connected")
                else:
                    logger.warning("NATS service disabled in configuration")

                # Initialize connection manager FIRST (needed by other services)
                self.connection_manager = ConnectionManager()
                set_global_connection_manager(self.connection_manager)
                self.connection_manager.persistence = self.persistence
                self.connection_manager._event_bus = self.event_bus

                # Initialize real-time event handler with event bus and connection_manager
                # AI Agent: Pass connection_manager as dependency to complete migration
                self.real_time_event_handler = RealTimeEventHandler(
                    event_bus=self.event_bus,
                    task_registry=self.task_registry,
                    connection_manager=self.connection_manager,
                )

                # Initialize NATS-dependent services (if NATS is enabled and connected)
                if self.nats_service:
                    # Get subject manager from NATS service if available
                    subject_manager = getattr(self.nats_service, "subject_manager", None)

                    # Initialize event publisher (previously global singleton)
                    from .realtime.event_publisher import EventPublisher

                    self.event_publisher = EventPublisher(self.nats_service, subject_manager)
                    logger.info("Event publisher initialized")

                    # Initialize NATS message handler (previously global singleton)
                    # AI Agent: Pass connection_manager as dependency instead of using global import
                    from .realtime.nats_message_handler import NATSMessageHandler

                    self.nats_message_handler = NATSMessageHandler(
                        self.nats_service, subject_manager, self.connection_manager
                    )
                    logger.info("NATS message handler initialized with injected connection_manager")
                else:
                    self.event_publisher = None
                    self.nats_message_handler = None
                    logger.info("NATS-dependent services skipped (NATS disabled or not connected)")

                # Ensure legacy module-level reference is updated for tests and legacy imports
                nats_module.set_global_connection_manager(self.connection_manager)

                logger.info("Real-time communication initialized")

                # Phase 7: Game services
                logger.debug("Initializing game services...")
                from .game.player_service import PlayerService
                from .game.room_service import RoomService
                from .services.user_manager import UserManager

                self.player_service = PlayerService(persistence=self.persistence)
                self.room_service = RoomService(persistence=self.persistence)

                # UserManager requires environment-aware data directory
                user_management_dir = get_environment_data_dir(normalized_environment) / "user_management"
                self.user_manager = UserManager(data_dir=user_management_dir)
                if self.nats_message_handler is not None:
                    self.nats_message_handler.user_manager = self.user_manager
                logger.info("Game services initialized")

                # Initialize item prototype registry and factory
                self._initialize_item_services(project_root)

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

    def _initialize_item_services(self, project_root: Path) -> None:
        """Load item prototypes and create the shared item factory."""
        from .game.items.item_factory import ItemFactory
        from .game.items.models import ItemPrototypeModel
        from .game.items.prototype_registry import PrototypeRegistry

        item_db_path = self._resolve_item_database_path(project_root)
        if item_db_path is None:
            logger.warning("Item database path could not be resolved; item services will remain unavailable")
            self.item_prototype_registry = None
            self.item_factory = None
            return

        if not item_db_path.exists():
            logger.warning("Item database not found; item services unavailable", item_db=str(item_db_path))
            self.item_prototype_registry = None
            self.item_factory = None
            return

        prototypes: dict[str, ItemPrototypeModel] = {}
        invalid_entries: list[dict[str, Any]] = []

        try:
            with sqlite3.connect(item_db_path) as connection:
                connection.row_factory = sqlite3.Row
                rows = connection.execute(
                    """
                    SELECT
                        prototype_id,
                        name,
                        short_description,
                        long_description,
                        item_type,
                        weight,
                        base_value,
                        durability,
                        flags,
                        wear_slots,
                        stacking_rules,
                        usage_restrictions,
                        effect_components,
                        metadata,
                        tags
                    FROM item_prototypes
                    """
                ).fetchall()

                for row in rows:
                    payload = {
                        "prototype_id": row["prototype_id"],
                        "name": row["name"],
                        "short_description": row["short_description"],
                        "long_description": row["long_description"],
                        "item_type": row["item_type"],
                        "weight": row["weight"],
                        "base_value": row["base_value"],
                        "durability": row["durability"],
                        "flags": self._decode_json_column(row["flags"], list),
                        "wear_slots": self._decode_json_column(row["wear_slots"], list),
                        "stacking_rules": self._decode_json_column(row["stacking_rules"], dict),
                        "usage_restrictions": self._decode_json_column(row["usage_restrictions"], dict),
                        "effect_components": self._decode_json_column(row["effect_components"], list),
                        "metadata": self._decode_json_column(row["metadata"], dict),
                        "tags": self._decode_json_column(row["tags"], list),
                    }

                    try:
                        prototype = ItemPrototypeModel.model_validate(payload)
                        prototypes[prototype.prototype_id] = prototype
                    except Exception as exc:  # noqa: BLE001 - validation errors vary
                        logger.warning(
                            "Invalid item prototype skipped during initialization",
                            prototype_id=payload.get("prototype_id"),
                            error=str(exc),
                        )
                        invalid_entries.append(
                            {
                                "prototype_id": payload.get("prototype_id"),
                                "error": str(exc),
                            }
                        )

            registry = PrototypeRegistry(prototypes, invalid_entries)
            self.item_prototype_registry = registry
            self.item_factory = ItemFactory(registry)

            logger.info(
                "Item services initialized",
                prototype_count=len(prototypes),
                invalid_count=len(invalid_entries),
                item_db=str(item_db_path),
            )
        except sqlite3.Error as exc:
            logger.error("Failed to load item prototypes from database", error=str(exc), item_db=str(item_db_path))
            self.item_prototype_registry = None
            self.item_factory = None

    def _decode_json_column(self, value: Any, expected_type: type) -> Any:
        """Decode a JSON column value, returning the type's default on failure."""
        if value is None or value == "":
            return expected_type()
        if isinstance(value, (list, dict)):
            return value
        try:
            decoded = json.loads(value)
            if isinstance(decoded, expected_type):
                return decoded
            if expected_type is list:
                return list(decoded)
            if expected_type is dict:
                return dict(decoded)
            return decoded
        except Exception:  # noqa: BLE001
            logger.warning("Failed to decode JSON column; using default value", column_value=value)
            return expected_type()

    def _resolve_item_database_path(self, project_root: Path) -> Path | None:
        """Resolve the path to the item prototype database based on configuration and overrides."""
        override = os.environ.get("ITEM_DATABASE_URL") or os.environ.get("ITEM_DATABASE_PATH")
        if override:
            normalized = self._normalize_path_from_url_or_path(override, project_root)
            if normalized:
                return normalized

        if not self.config:
            return None

        environment = getattr(self.config.logging, "environment", "local")
        env_map = {
            "local": Path("data") / "local" / "items" / "local_items.db",
            "e2e_test": Path("data") / "e2e_test" / "items" / "e2e_items.db",
            "unit_test": Path("data") / "unit_test" / "items" / "unit_test_items.db",
        }

        relative = env_map.get(environment)
        if relative is None:
            relative = Path("data") / environment / "items" / f"{environment}_items.db"

        return (project_root / relative).resolve()

    def _normalize_path_from_url_or_path(self, raw: str, project_root: Path) -> Path | None:
        """Normalize an item database override into a filesystem path."""
        try:
            if "://" in raw:
                parsed = urlparse(raw)
                if parsed.scheme.startswith("sqlite"):
                    path_str = parsed.path
                    if path_str.startswith("/") and len(path_str) > 3 and path_str[2] == ":":
                        path_str = path_str.lstrip("/")
                    return Path(path_str).resolve()
                return Path(parsed.path or "").resolve()

            path = Path(raw)
            if not path.is_absolute():
                path = (project_root / path).resolve()
            return path
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to normalize item database override", override=raw, error=str(exc))
            return None

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
            # Stop NATS message handler first (depends on NATS service)
            if self.nats_message_handler is not None:
                try:
                    await self.nats_message_handler.stop()
                    logger.debug("NATS message handler stopped")
                except Exception as e:
                    logger.error("Error stopping NATS message handler", error=str(e))

            # Then disconnect NATS service
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

            # 5. Close NPC database connections
            try:
                from .npc_database import close_npc_db
                await close_npc_db()
                logger.debug("NPC database connections closed")
            except Exception as e:
                logger.error("Error closing NPC database connections", error=str(e))

            logger.info("ApplicationContainer shutdown complete")

        except Exception as e:
            logger.error("Error during ApplicationContainer shutdown", error=str(e), exc_info=True)
            # Don't re-raise - best effort cleanup

    def _get_project_root(self) -> Path:
        """Return and cache the repository root directory."""

        if self._project_root is None:
            self._project_root = get_project_root()
        return self._project_root

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
