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

# pylint: disable=too-many-return-statements,too-many-lines,wrong-import-position  # Reason: Container methods require multiple return statements for service resolution logic (type checking, initialization states, error handling). Container requires extensive service registration and lifecycle management code. Imports after TYPE_CHECKING block are intentional to avoid circular dependencies.

import json
import threading
from datetime import datetime
from json import JSONDecodeError
from pathlib import Path
from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse

from anyio import Lock
from pydantic import ValidationError

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
    from .game.movement_service import MovementService
    from .game.player_service import PlayerService
    from .game.room_service import RoomService
    from .monitoring.exception_tracker import ExceptionTracker
    from .monitoring.monitoring_dashboard import MonitoringDashboard
    from .monitoring.performance_monitor import PerformanceMonitor

    # Removed: from .persistence import PersistenceLayer - now using AsyncPersistenceLayer only
    from .realtime.connection_manager import ConnectionManager
    from .realtime.event_handler import RealTimeEventHandler
    from .services.exploration_service import ExplorationService
    from .services.holiday_service import HolidayService
    from .services.nats_service import NATSService
    from .services.schedule_service import ScheduleService
    from .services.user_manager import UserManager
    from .structured_logging.log_aggregator import LogAggregator
    from .time.tick_scheduler import MythosTickScheduler

from .structured_logging.enhanced_logging_config import get_logger
from .utils.project_paths import (
    get_calendar_paths_for_environment,
    get_environment_data_dir,
    get_project_root,
    normalize_environment,
)

logger = get_logger(__name__)


class ApplicationContainer:  # pylint: disable=too-many-instance-attributes  # Reason: DI container requires many service instances and configuration attributes
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

    def __init__(self) -> None:  # pylint: disable=too-many-statements  # Reason: Container initialization requires many attribute declarations (56 statements) for all service references; breaking this into smaller functions would reduce clarity and is not standard Python practice for __init__
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
        # Persistence layer (async only - persistence alias for backward compatibility)
        self.persistence: AsyncPersistenceLayer | None = None
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
        self.movement_service: MovementService | None = None
        self.exploration_service: ExplorationService | None = None
        self.user_manager: UserManager | None = None
        self.container_service: Any | None = None  # ContainerService type hint would create circular import

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

        # Combat services
        self.player_combat_service: Any | None = None  # PlayerCombatService type hint would create circular import
        self.player_death_service: Any | None = None  # PlayerDeathService type hint would create circular import
        self.player_respawn_service: Any | None = None  # PlayerRespawnService type hint would create circular import
        self.combat_service: Any | None = None  # CombatService type hint would create circular import

        # Magic services
        self.magic_service: Any | None = None  # MagicService type hint would create circular import
        self.spell_registry: Any | None = None  # SpellRegistry type hint would create circular import
        self.spell_targeting_service: Any | None = None  # SpellTargetingService type hint would create circular import
        self.spell_effects: Any | None = None  # SpellEffects type hint would create circular import
        self.spell_learning_service: Any | None = None  # SpellLearningService type hint would create circular import
        self.mp_regeneration_service: Any | None = None  # MPRegenerationService type hint would create circular import

        # NPC services
        self.npc_lifecycle_manager: Any | None = None  # NPCLifecycleManager type hint would create circular import
        self.npc_spawning_service: Any | None = None  # NPCSpawningService type hint would create circular import
        self.npc_population_controller: Any | None = (
            None  # NPCPopulationController type hint would create circular import
        )

        # Other services
        self.catatonia_registry: Any | None = None  # CatatoniaRegistry type hint would create circular import
        self.passive_lucidity_flux_service: Any | None = (
            None  # PassiveLucidityFluxService type hint would create circular import
        )
        self.mythos_time_consumer: Any | None = None  # MythosTimeEventConsumer type hint would create circular import
        self.chat_service: Any | None = None  # ChatService type hint would create circular import

        # State flags
        self.server_shutdown_pending: bool = False
        self.shutdown_data: dict[str, Any] | None = None
        self.tick_task: Any | None = None  # Task reference from TaskRegistry

        # Initialization state
        self._initialized: bool = False
        self._initialization_lock = Lock()
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

    @classmethod
    def set_instance(cls, instance: "ApplicationContainer") -> None:
        """
        Set the singleton container instance.

        This method is used during application startup to register the container
        instance that was created and initialized in the lifespan context.

        Args:
            instance: The ApplicationContainer instance to set as the singleton

        AI: This provides a public API for setting the instance, avoiding direct
            access to protected members (_lock, _instance) from external code.
        """
        with cls._lock:
            cls._instance = instance
        logger.debug("ApplicationContainer instance set via set_instance()")

    async def initialize(self) -> None:  # pylint: disable=too-many-locals,too-many-statements  # Reason: Service initialization requires many intermediate variables and statements for complex dependency setup
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
                # Access logging config directly - self.config.logging is a LoggingConfig instance
                logging_environment = self.config.logging.environment
                logger.info("Configuration loaded", environment=logging_environment)
                normalized_environment = normalize_environment(logging_environment)

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

                # Phase 5: Persistence layer (async only)
                logger.debug("Initializing persistence layer...")
                from .async_persistence import AsyncPersistenceLayer

                self.async_persistence = AsyncPersistenceLayer(event_bus=self.event_bus)
                # Use async_persistence as persistence for backward compatibility during migration
                self.persistence = self.async_persistence
                logger.info("Persistence layer initialized (async only)")

                # Phase 5.1: Warm up room cache and connection pool
                logger.debug("Warming up room cache and connection pool...")
                try:
                    await self.async_persistence.warmup_room_cache()
                    logger.info("Room cache warmed up successfully")
                except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room cache warmup errors should not block server startup, log and continue
                    logger.warning(
                        "Room cache warmup failed, will load on first access",
                        error=str(e),
                        error_type=type(e).__name__,
                    )

                # Phase 5.2: Gameplay services
                logger.debug("Initializing gameplay services...")
                from .game.movement_service import MovementService
                from .services.exploration_service import ExplorationService

                self.exploration_service = ExplorationService(database_manager=self.database_manager)
                self.movement_service = MovementService(
                    event_bus=self.event_bus,
                    async_persistence=self.async_persistence,
                    exploration_service=self.exploration_service,
                )
                logger.info("Exploration and movement services initialized")

                # Phase 5.5: Temporal services (holidays and schedules - require async_persistence)
                logger.debug("Initializing temporal services...")
                from .services.holiday_service import HolidayService
                from .services.schedule_service import ScheduleService
                from .time.time_service import get_mythos_chronicle

                holidays_path, schedules_dir = get_calendar_paths_for_environment(normalized_environment)
                self.holiday_service = HolidayService(
                    chronicle=get_mythos_chronicle(),
                    data_path=holidays_path,
                    environment=normalized_environment,
                    async_persistence=self.async_persistence,
                )
                self.schedule_service = ScheduleService(
                    schedule_dir=schedules_dir,
                    environment=normalized_environment,
                    async_persistence=self.async_persistence,
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
                    except (
                        ValueError,
                        TypeError,
                        AttributeError,
                        RuntimeError,
                    ) as exc:  # pragma: no cover - defensive logging
                        logger.warning("Failed to resolve holiday window for tick scheduler", error=str(exc))
                        return []

                self.mythos_tick_scheduler = MythosTickScheduler(
                    chronicle=get_mythos_chronicle(),
                    event_bus=self.event_bus,
                    task_registry=self.task_registry,
                    holiday_resolver=_resolve_hourly_holidays,
                )
                logger.info("Mythos tick scheduler prepared")

                # Phase 6: Real-time communication
                logger.debug("Initializing real-time communication...")
                from .realtime.connection_manager import ConnectionManager
                from .realtime.event_handler import RealTimeEventHandler
                from .services.nats_service import NATSService

                # Initialize NATS service if enabled
                if self.config.nats.enabled:  # pylint: disable=no-member  # Reason: Pydantic model fields are dynamically accessible after validation, pylint cannot detect them statically
                    self.nats_service = NATSService(config=self.config.nats)
                    await self.nats_service.connect()
                    logger.info("NATS service connected")
                else:
                    logger.warning("NATS service disabled in configuration")

                # Initialize connection manager FIRST (needed by other services)
                self.connection_manager = ConnectionManager()
                # ARCHITECTURAL FIX: Use async_persistence instead of sync persistence
                # This eliminates the need for asyncio.to_thread() wrappers and provides
                # true async database operations that don't block the event loop
                # Set async_persistence on BOTH connection_manager and room_manager directly
                self.connection_manager.async_persistence = self.async_persistence
                self.connection_manager.room_manager.async_persistence = self.async_persistence
                self.connection_manager.set_event_bus(self.event_bus)

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

                # Initialize container service
                from .services.container_service import ContainerService

                self.container_service = ContainerService(persistence=self.persistence)
                logger.info("Container service initialized")

                logger.info("Game services initialized")

                # Initialize item prototype registry and factory
                await self._initialize_item_services()

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
                from .monitoring.exception_tracker import ExceptionTracker
                from .monitoring.monitoring_dashboard import MonitoringDashboard
                from .monitoring.performance_monitor import PerformanceMonitor
                from .structured_logging.log_aggregator import LogAggregator

                # Initialize monitoring services directly (no singleton pattern)
                self.performance_monitor = PerformanceMonitor()
                self.exception_tracker = ExceptionTracker()
                self.monitoring_dashboard = MonitoringDashboard()  # No constructor params
                self.log_aggregator = LogAggregator()
                logger.info("Monitoring services initialized")

                # Phase 10: Combat services (depends on persistence, event_bus, connection_manager, movement_service)
                await self._initialize_combat_services()

                # Phase 11: NPC services (depends on event_bus, persistence, async_persistence)
                await self._initialize_npc_services()

                # Phase 12: NATS and combat service (depends on nats_service, combat services)
                await self._initialize_nats_combat_service()

                # Phase 13: Magic services (depends on player_service, combat_service, player_combat_service)
                await self._initialize_magic_services()

                # Phase 14: Chat service (depends on persistence, player_service, nats_service, user_manager)
                await self._initialize_chat_service()

                # Phase 15: Mythos time consumer (depends on event_bus, holiday_service, schedule_service, room_service, npc_lifecycle_manager)
                await self._initialize_mythos_time_consumer()

                self._initialized = True
                logger.info(
                    "ApplicationContainer initialization complete",
                    services_initialized=[
                        "config",
                        "database",
                        "event_bus",
                        "persistence",
                        "connection_manager",
                        "movement_service",
                        "exploration_service",
                        "player_service",
                        "room_service",
                        "user_manager",
                        "monitoring",
                        "combat_services",
                        "npc_services",
                        "magic_services",
                        "chat_service",
                        "mythos_time_consumer",
                    ],
                )

            except Exception as e:
                logger.error("ApplicationContainer initialization failed", error=str(e), exc_info=True)
                # Cleanup on failure
                await self.shutdown()
                raise RuntimeError(f"Failed to initialize application container: {e}") from e

    async def _initialize_item_services(self) -> None:  # pylint: disable=too-many-locals  # Reason: Item service initialization requires many intermediate variables
        """Load item prototypes from PostgreSQL and create the shared item factory."""
        from sqlalchemy import select
        from sqlalchemy.exc import SQLAlchemyError

        from .game.items.item_factory import ItemFactory
        from .game.items.models import ItemPrototypeModel
        from .game.items.prototype_registry import PrototypeRegistry
        from .models.item import ItemPrototype

        if not self.database_manager:
            logger.warning("Database manager not initialized; item services will remain unavailable")
            self.item_prototype_registry = None
            self.item_factory = None
            return

        prototypes: dict[str, ItemPrototypeModel] = {}
        invalid_entries: list[dict[str, Any]] = []

        try:
            session_maker = self.database_manager.get_session_maker()

            async with session_maker() as session:
                # Query item_prototypes from PostgreSQL using ORM
                result = await session.execute(select(ItemPrototype))
                item_prototypes = result.scalars().all()

                for db_prototype in item_prototypes:
                    payload = {
                        "prototype_id": db_prototype.prototype_id,
                        "name": db_prototype.name,
                        "short_description": db_prototype.short_description,
                        "long_description": db_prototype.long_description,
                        "item_type": db_prototype.item_type,
                        "weight": float(db_prototype.weight) if db_prototype.weight is not None else 0.0,
                        "base_value": int(db_prototype.base_value) if db_prototype.base_value is not None else 0,
                        "durability": int(db_prototype.durability) if db_prototype.durability is not None else None,
                        "flags": self._decode_json_column(db_prototype.flags, list),
                        "wear_slots": self._decode_json_column(db_prototype.wear_slots, list),
                        "stacking_rules": self._decode_json_column(db_prototype.stacking_rules, dict),
                        "usage_restrictions": self._decode_json_column(db_prototype.usage_restrictions, dict),
                        "effect_components": self._decode_json_column(db_prototype.effect_components, list),
                        "metadata": self._decode_json_column(db_prototype.metadata_payload, dict),
                        "tags": self._decode_json_column(db_prototype.tags, list),
                    }

                    try:
                        prototype = ItemPrototypeModel.model_validate(payload)
                        prototypes[prototype.prototype_id] = prototype
                    except ValidationError as exc:
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
                "Item services initialized from PostgreSQL",
                prototype_count=len(prototypes),
                invalid_count=len(invalid_entries),
            )
        except SQLAlchemyError as exc:
            logger.error(
                "Failed to load item prototypes from PostgreSQL database", error=str(exc), error_type=type(exc).__name__
            )
            self.item_prototype_registry = None
            self.item_factory = None

    def _decode_json_column(self, value: Any, expected_type: type) -> Any:
        """Decode a JSON column value, returning the type's default on failure."""
        if value is None or not value:
            return expected_type()
        if isinstance(value, list | dict):
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
        except JSONDecodeError:  # noqa: BLE001  # Reason: JSON decode errors are expected for malformed data, caught explicitly to return default value, no security risk from logging
            logger.warning("Failed to decode JSON column; using default value", column_value=value)
            return expected_type()

    async def _sanitarium_failover_callback(self, player_id: str, current_lcd: int) -> None:
        """Failover callback that relocates catatonic players to the sanitarium."""
        import uuid as uuid_lib

        from anyio import sleep

        from .services.lucidity_service import LucidityService

        # 10-second fade before transport per spec
        await sleep(10.0)

        if self.database_manager is None:
            logger.error("Database manager not available for catatonia failover", player_id=player_id)
            return

        try:
            session_maker = self.database_manager.get_session_maker()
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as exc:
            logger.error(
                "Failed to get session maker for catatonia failover",
                player_id=player_id,
                error=str(exc),
                exc_info=True,
            )
            return

        async with session_maker() as session:
            try:
                # Clear all active hallucination timers per spec requirement
                player_id_uuid = uuid_lib.UUID(player_id) if isinstance(player_id, str) else player_id
                lucidity_service = LucidityService(session)
                timers_cleared = await lucidity_service.clear_hallucination_timers(player_id_uuid)
                logger.debug(
                    "Hallucination timers cleared in failover",
                    player_id=player_id,
                    timers_cleared=timers_cleared,
                )

                if self.player_respawn_service is None:
                    logger.error("PlayerRespawnService not available for catatonia failover", player_id=player_id)
                    return

                await self.player_respawn_service.move_player_to_limbo(player_id, "catatonia_failover", session)
                await self.player_respawn_service.respawn_player_from_sanitarium(player_id, session)
                logger.info("Catatonia failover completed", player_id=player_id, lcd=current_lcd)
            except (
                ValueError,
                TypeError,
                AttributeError,
                KeyError,
                RuntimeError,
            ) as exc:  # pragma: no cover - defensive
                logger.error("Catatonia failover failed", player_id=player_id, error=str(exc), exc_info=True)
                await session.rollback()

    async def _initialize_combat_services(self) -> None:  # pylint: disable=too-many-locals  # Reason: Combat service initialization requires many intermediate variables for dependency setup
        """Initialize combat-related services."""
        if self.persistence is None:
            raise RuntimeError("Persistence must be initialized before combat services")
        if self.event_bus is None:
            raise RuntimeError("EventBus must be initialized before combat services")

        logger.debug("Initializing combat services...")

        from .services.catatonia_registry import CatatoniaRegistry
        from .services.passive_lucidity_flux_service import PassiveLucidityFluxService
        from .services.player_combat_service import PlayerCombatService
        from .services.player_death_service import PlayerDeathService
        from .services.player_respawn_service import PlayerRespawnService

        # Initialize PlayerCombatService
        self.player_combat_service = PlayerCombatService(self.persistence, self.event_bus)
        if self.connection_manager is not None:
            self.connection_manager.set_player_combat_service(self.player_combat_service)
        # Update MovementService with combat service if it exists
        if self.movement_service is not None:
            self.movement_service.set_player_combat_service(self.player_combat_service)
            logger.info("MovementService updated with player_combat_service")
        logger.info("Player combat service initialized")

        # Initialize PlayerDeathService
        self.player_death_service = PlayerDeathService(
            event_bus=self.event_bus, player_combat_service=self.player_combat_service
        )
        logger.info("Player death service initialized")

        # Initialize PlayerRespawnService
        self.player_respawn_service = PlayerRespawnService(
            event_bus=self.event_bus, player_combat_service=self.player_combat_service
        )
        logger.info("Player respawn service initialized")

        # Initialize CatatoniaRegistry with failover callback
        self.catatonia_registry = CatatoniaRegistry(failover_callback=self._sanitarium_failover_callback)
        logger.info("Catatonia registry initialized")

        # Initialize PassiveLucidityFluxService
        if self.performance_monitor is None:
            raise RuntimeError("PerformanceMonitor must be initialized before passive_lucidity_flux_service")
        self.passive_lucidity_flux_service = PassiveLucidityFluxService(
            persistence=self.async_persistence,
            performance_monitor=self.performance_monitor,
            catatonia_observer=self.catatonia_registry,
        )
        logger.info("Passive lucidity flux service initialized")

        logger.info("All combat services initialized")

    async def _initialize_npc_services(self) -> None:
        """Initialize NPC services and load definitions."""
        if self.event_bus is None:
            raise RuntimeError("EventBus must be initialized before NPC services")
        if self.persistence is None:
            raise RuntimeError("Persistence must be initialized before NPC services")
        if self.async_persistence is None:
            raise RuntimeError("AsyncPersistence must be initialized before NPC services")

        logger.debug("Initializing NPC services...")

        from .npc.lifecycle_manager import NPCLifecycleManager
        from .npc.population_control import NPCPopulationController
        from .npc.spawning_service import NPCSpawningService
        from .npc_database import get_npc_session
        from .services.npc_instance_service import initialize_npc_instance_service
        from .services.npc_service import NPCService

        # Initialize NPCSpawningService
        self.npc_spawning_service = NPCSpawningService(self.event_bus, None)

        # Initialize NPCLifecycleManager
        self.npc_lifecycle_manager = NPCLifecycleManager(
            event_bus=self.event_bus,
            population_controller=None,
            spawning_service=self.npc_spawning_service,
            persistence=self.persistence,
        )

        # Initialize NPCPopulationController
        self.npc_population_controller = NPCPopulationController(
            self.event_bus,
            self.npc_spawning_service,
            self.npc_lifecycle_manager,
            async_persistence=self.async_persistence,
        )

        # Wire up circular dependencies
        self.npc_spawning_service.population_controller = self.npc_population_controller
        self.npc_lifecycle_manager.population_controller = self.npc_population_controller

        # Initialize NPC instance service
        initialize_npc_instance_service(
            lifecycle_manager=self.npc_lifecycle_manager,
            spawning_service=self.npc_spawning_service,
            population_controller=self.npc_population_controller,
            event_bus=self.event_bus,
        )

        # Load NPC definitions and spawn rules
        npc_service = NPCService()
        async for npc_session in get_npc_session():
            try:
                definitions = await npc_service.get_npc_definitions(npc_session)
                self.npc_population_controller.load_npc_definitions(definitions)
                logger.info("NPC definitions loaded", count=len(definitions))

                spawn_rules = await npc_service.get_spawn_rules(npc_session)
                self.npc_population_controller.load_spawn_rules(spawn_rules)
                logger.info("NPC spawn rules loaded", count=len(spawn_rules))
            except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                logger.error("Error loading NPC definitions and spawn rules", error=str(e))
            break

        logger.info("NPC services initialized")

        # Start NPC thread manager if available
        if hasattr(self.npc_lifecycle_manager, "thread_manager"):
            try:
                await self.npc_lifecycle_manager.thread_manager.start()
                logger.info("NPC thread manager started")

                if hasattr(self.npc_lifecycle_manager, "_pending_thread_starts"):
                    # Accessing protected member via getattr() for internal state initialization
                    # This is safe as we check existence first and handle gracefully
                    pending_starts = getattr(self.npc_lifecycle_manager, "_pending_thread_starts", [])  # pylint: disable=protected-access  # Reason: Accessing internal state for startup initialization, existence checked first and handled gracefully
                    for npc_id, definition in pending_starts:
                        try:
                            await self.npc_lifecycle_manager.thread_manager.start_npc_thread(npc_id, definition)
                            logger.debug("Started queued NPC thread", npc_id=npc_id)
                        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                            logger.warning("Failed to start queued NPC thread", npc_id=npc_id, error=str(e))
                    pending_starts.clear()
            except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                logger.error("Failed to start NPC thread manager", error=str(e))

    async def _initialize_nats_combat_service(self) -> None:
        """Initialize NATS-dependent services including combat service."""
        if self.config is None:
            raise RuntimeError("Config must be initialized before NATS combat service")
        if self.player_combat_service is None:
            raise RuntimeError("PlayerCombatService must be initialized before combat service")
        if self.player_death_service is None:
            raise RuntimeError("PlayerDeathService must be initialized before combat service")
        if self.player_respawn_service is None:
            raise RuntimeError("PlayerRespawnService must be initialized before combat service")
        if self.event_bus is None:
            raise RuntimeError("EventBus must be initialized before combat service")

        logger.debug("Initializing NATS and combat service...")

        is_testing = self.config.logging.environment in ("unit_test", "e2e_test")  # pylint: disable=no-member  # Reason: Pydantic model field access - pylint doesn't recognize dynamic field access on Pydantic models

        if self.nats_service is not None and self.nats_service.is_connected():
            logger.info("NATS service available from container")

            # Lazy import to avoid circular dependency with combat_service
            from .services.combat_service import CombatService, set_combat_service

            self.combat_service = CombatService(
                self.player_combat_service,
                self.nats_service,
                player_death_service=self.player_death_service,
                player_respawn_service=self.player_respawn_service,
                event_bus=self.event_bus,
            )

            set_combat_service(self.combat_service)

            if self.player_service is None:
                raise RuntimeError("PlayerService must be initialized")
            self.player_service.combat_service = self.combat_service
            self.player_service.player_combat_service = self.player_combat_service
            logger.info("Combat service initialized")

            # Start NATS message handler if available
            try:
                if self.nats_message_handler:
                    await self.nats_message_handler.start()
                    logger.info("NATS message handler started successfully from container")
                else:
                    logger.warning("NATS message handler not available in container (NATS disabled or failed)")
            except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                logger.error("Error starting NATS message handler", error=str(e))
        else:
            if is_testing:
                logger.warning("NATS service not available in test environment - using mock NATS service")
                self.combat_service = None
            else:
                logger.error("NATS service not available - NATS is required for chat functionality")
                raise RuntimeError("NATS connection failed - NATS is mandatory for chat system")

    async def _initialize_magic_services(self) -> None:  # pylint: disable=too-many-locals  # Reason: Magic service initialization requires many intermediate variables for dependency setup
        """Initialize magic system services."""
        if self.async_persistence is None:
            raise RuntimeError("async_persistence must be initialized before magic services")
        if self.player_service is None:
            raise RuntimeError("player_service must be initialized before magic services")

        logger.debug("Initializing magic services...")

        # Import here to avoid circular imports: spell_targeting -> combat_service -> lifespan -> lifespan_startup
        from .game.magic.magic_service import MagicService
        from .game.magic.mp_regeneration_service import MPRegenerationService
        from .game.magic.spell_effects import SpellEffects
        from .game.magic.spell_learning_service import SpellLearningService
        from .game.magic.spell_registry import SpellRegistry
        from .game.magic.spell_targeting import SpellTargetingService
        from .persistence.repositories.player_spell_repository import PlayerSpellRepository
        from .persistence.repositories.spell_repository import SpellRepository as SpellRepositoryClass
        from .services.target_resolution_service import TargetResolutionService

        logger.info("Initializing magic system services...")

        # Initialize repositories
        spell_repository = SpellRepositoryClass()
        player_spell_repository = PlayerSpellRepository()
        logger.info("Spell repositories initialized")

        # Initialize SpellRegistry and load spells
        self.spell_registry = SpellRegistry(spell_repository)
        await self.spell_registry.load_spells()
        spell_count = len(self.spell_registry._spells)  # pylint: disable=protected-access  # Reason: Accessing internal spell dictionary for initialization logging, SpellRegistry manages this as internal state
        logger.info("SpellRegistry initialized and loaded", spell_count=spell_count)

        # Initialize SpellTargetingService (needs TargetResolutionService, CombatService, PlayerCombatService)
        # TargetResolutionService accepts both sync and async persistence layers
        # The protocol is too strict for mypy, but the service handles both at runtime
        target_resolution_service = TargetResolutionService(
            persistence=self.async_persistence,  # type: ignore[arg-type]  # Reason: TargetResolutionService accepts both sync and async persistence at runtime, but mypy protocol is too strict
            player_service=self.player_service,
        )
        self.spell_targeting_service = SpellTargetingService(
            target_resolution_service=target_resolution_service,
            combat_service=self.combat_service,
            player_combat_service=self.player_combat_service,
        )
        logger.info("SpellTargetingService initialized")

        # Initialize SpellEffects (needs PlayerService)
        self.spell_effects = SpellEffects(player_service=self.player_service)
        logger.info("SpellEffects initialized")

        # Initialize SpellLearningService (needs SpellRegistry, PlayerService, PlayerSpellRepository)
        self.spell_learning_service = SpellLearningService(
            spell_registry=self.spell_registry,
            player_service=self.player_service,
            player_spell_repository=player_spell_repository,
        )
        logger.info("SpellLearningService initialized")

        # Initialize MPRegenerationService (needs PlayerService)
        self.mp_regeneration_service = MPRegenerationService(player_service=self.player_service)
        logger.info("MPRegenerationService initialized")

        # Initialize MagicService (needs all of the above)
        self.magic_service = MagicService(
            spell_registry=self.spell_registry,
            player_service=self.player_service,
            spell_targeting_service=self.spell_targeting_service,
            spell_effects=self.spell_effects,
            player_spell_repository=player_spell_repository,
            spell_learning_service=self.spell_learning_service,
            combat_service=self.combat_service,
        )

        # Set magic_service reference in combat_service if available
        if self.combat_service:
            self.combat_service.magic_service = self.magic_service
            logger.info("MagicService linked to CombatService")

        logger.info("MagicService initialized")
        logger.info("All magic system services initialized")

    async def _initialize_chat_service(self) -> None:
        """Initialize chat service."""
        if self.config is None:
            raise RuntimeError("Config must be initialized before chat service")
        if self.persistence is None:
            raise RuntimeError("Persistence must be initialized before chat service")
        if self.player_service is None:
            raise RuntimeError("PlayerService must be initialized before chat service")
        if self.user_manager is None:
            raise RuntimeError("UserManager must be initialized before chat service")

        logger.debug("Initializing chat service...")

        from .game.chat_service import ChatService
        from .services.nats_subject_manager import nats_subject_manager

        is_testing = self.config.logging.environment in ("unit_test", "e2e_test")  # pylint: disable=no-member  # Reason: Pydantic model field access - pylint doesn't recognize dynamic field access on Pydantic models

        subject_manager = None
        nats_service = self.nats_service
        if nats_service and getattr(nats_service, "subject_manager", None):
            subject_manager = nats_service.subject_manager
        else:
            subject_manager = nats_subject_manager

        self.chat_service = ChatService(
            persistence=self.persistence,
            room_service=self.persistence,
            player_service=self.player_service,
            nats_service=nats_service,
            user_manager_instance=self.user_manager,
            subject_manager=subject_manager,
        )

        if self.chat_service.nats_service and self.chat_service.nats_service.is_connected():
            logger.info("Chat service NATS connection verified")
        elif is_testing:
            logger.info("Chat service running in test mode without NATS connection")
        else:
            logger.error("Chat service NATS connection failed")
            raise RuntimeError("Chat service NATS connection failed - NATS is mandatory for chat system")

        logger.info("Chat service initialized")

    async def _initialize_mythos_time_consumer(self) -> None:
        """Initialize Mythos time event consumer."""
        if (
            self.event_bus
            and self.holiday_service
            and self.schedule_service
            and self.room_service
            and self.npc_lifecycle_manager
        ):
            from .time.time_event_consumer import MythosTimeEventConsumer
            from .time.time_service import get_mythos_chronicle

            self.mythos_time_consumer = MythosTimeEventConsumer(
                event_bus=self.event_bus,
                chronicle=get_mythos_chronicle(),
                holiday_service=self.holiday_service,
                schedule_service=self.schedule_service,
                room_service=self.room_service,
                npc_lifecycle_manager=self.npc_lifecycle_manager,
            )
            logger.info("Mythos time consumer initialized and subscribed to hour ticks")
        else:
            logger.warning("Mythos time consumer not initialized due to missing dependencies")

    def _normalize_path_from_url_or_path(self, raw: str, project_root: Path) -> Path | None:
        """
        Normalize an item database override into a filesystem path.

        DEPRECATED: Items are now stored in PostgreSQL. This method is kept for
        backward compatibility but should not be used for new code.

        Args:
            raw: Database URL or file path
            project_root: Project root directory for relative paths

        Returns:
            Path | None: Normalized path or None if invalid
        """
        try:
            if "://" in raw:
                parsed = urlparse(raw)
                # PostgreSQL URLs don't have file paths - return None
                if parsed.scheme.startswith("postgresql"):
                    logger.warning(
                        "Item database override with PostgreSQL URL is not supported - items are in PostgreSQL",
                        url=raw,
                    )
                    return None
                # For other URL schemes, try to extract path
                return Path(parsed.path or "").resolve() if parsed.path else None

            # Handle file paths
            path = Path(raw)
            if not path.is_absolute():
                path = (project_root / path).resolve()
            return path
        except (ValueError, OSError) as exc:
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
            await self._shutdown_log_aggregator()
            await self._shutdown_nats_services()
            await self._shutdown_event_bus()
            await self._shutdown_database_services()

            logger.info("ApplicationContainer shutdown complete")

        except RuntimeError as e:
            logger.error("Error during ApplicationContainer shutdown", error=str(e), exc_info=True)
            # Don't re-raise - best effort cleanup

    async def _shutdown_log_aggregator(self) -> None:
        """Shutdown log aggregator service."""
        if self.log_aggregator is not None:
            try:
                self.log_aggregator.shutdown()
                logger.debug("Log aggregator shutdown")
            except RuntimeError as e:
                logger.error("Error shutting down log aggregator", error=str(e))

    async def _shutdown_nats_services(self) -> None:
        """Shutdown NATS-related services."""
        # Stop NATS message handler first (depends on NATS service)
        if self.nats_message_handler is not None:
            try:
                await self.nats_message_handler.stop()
                logger.debug("NATS message handler stopped")
            except RuntimeError as e:
                logger.error("Error stopping NATS message handler", error=str(e))

        # Then disconnect NATS service
        if self.nats_service is not None:
            try:
                await self.nats_service.disconnect()
                logger.debug("NATS service disconnected")
            except RuntimeError as e:
                logger.error("Error disconnecting NATS service", error=str(e))

    async def _shutdown_event_bus(self) -> None:
        """Shutdown event bus service."""
        if self.event_bus is not None:
            try:
                await self.event_bus.shutdown()
                logger.debug("Event bus shutdown")
            except RuntimeError as e:
                logger.error("Error shutting down event bus", error=str(e))

    async def _shutdown_database_services(self) -> None:
        """Shutdown all database-related services."""
        # Close database connections
        if self.database_manager is not None:
            try:
                await self.database_manager.close()
                logger.debug("Database connections closed")
            except RuntimeError as e:
                logger.error("Error closing database connections", error=str(e))

        # Close async persistence connection pool
        if self.async_persistence is not None:
            try:
                await self.async_persistence.close()
                logger.debug("Async persistence connection pool closed")
            except RuntimeError as e:
                logger.error("Error closing async persistence pool", error=str(e))

        # Close NPC database connections
        try:
            from .npc_database import close_npc_db

            await close_npc_db()
            logger.debug("NPC database connections closed")
        except RuntimeError as e:
            logger.error("Error closing NPC database connections", error=str(e))

    def _get_project_root(self) -> Path:
        """Return and cache the repository root directory."""

        if self._project_root is None:
            self._project_root = get_project_root()
        return self._project_root

    def get_service(self, service_name: str) -> Any:
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
