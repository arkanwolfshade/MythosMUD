"""
ApplicationContainer main module - orchestrates domain bundles and preserves public API.

Phase 1: Bundles own initialization; container delegates and flattens attributes.
"""

# pylint: disable=too-many-instance-attributes,too-many-statements  # Reason: DI container requires many service instances; __init__ declares all attributes for backward compatibility
import threading
from pathlib import Path
from typing import Any

from anyio import Lock

from server.container.utils import decode_json_column, normalize_path_from_url_or_path
from server.structured_logging.enhanced_logging_config import get_logger
from server.utils.project_paths import get_project_root

logger = get_logger(__name__)


def _flatten_bundle(container: "ApplicationContainer", bundle: Any, attrs: tuple[str, ...]) -> None:
    """Copy bundle attributes onto container for backward compatibility."""
    for attr in attrs:
        if hasattr(bundle, attr):
            setattr(container, attr, getattr(bundle, attr))


class ApplicationContainer:
    """
    Dependency Injection Container for MythosMUD application.

    Orchestrates domain-specific bundles and flattens their attributes onto self
    so existing code (container.player_service, etc.) continues to work.
    """

    _instance: "ApplicationContainer | None" = None
    _lock: threading.Lock = threading.Lock()

    # Class annotations keep pyright from freezing attrs as forever-None (self.x = None
    # without a declaration). Real service types land at runtime via bundles; DI surface
    # is wide, so Any|None is intentional (narrow/cast at call sites when needed).
    config: Any
    database_manager: Any
    task_registry: Any
    tracked_task_manager: Any
    event_bus: Any
    persistence: Any
    async_persistence: Any
    connection_manager: Any
    real_time_event_handler: Any
    nats_service: Any
    nats_message_handler: Any
    event_publisher: Any
    player_service: Any
    room_service: Any
    movement_service: Any
    player_position_service: Any
    follow_service: Any
    party_service: Any
    exploration_service: Any
    user_manager: Any
    container_service: Any
    level_service: Any
    skill_service: Any
    room_cache_service: Any
    profession_cache_service: Any
    performance_monitor: Any
    exception_tracker: Any
    monitoring_dashboard: Any
    log_aggregator: Any
    holiday_service: Any
    schedule_service: Any
    mythos_tick_scheduler: Any
    item_prototype_registry: Any
    item_factory: Any
    player_combat_service: Any
    player_death_service: Any
    player_respawn_service: Any
    combat_service: Any
    magic_service: Any
    spell_registry: Any
    spell_targeting_service: Any
    spell_effects: Any
    spell_learning_service: Any
    mp_regeneration_service: Any
    quest_definition_repository: Any
    quest_instance_repository: Any
    quest_service: Any
    npc_lifecycle_manager: Any
    npc_spawning_service: Any
    npc_population_controller: Any
    catatonia_registry: Any
    passive_lucidity_flux_service: Any
    mythos_time_consumer: Any
    chat_service: Any
    server_shutdown_pending: bool
    shutdown_data: Any
    tick_task: Any

    def _init_core_attributes(self) -> None:
        self.config = None
        self.database_manager = None
        self.task_registry = None
        self.tracked_task_manager = None
        self.event_bus = None
        self.persistence = None
        self.async_persistence = None

    def _init_realtime_attributes(self) -> None:
        self.connection_manager = None
        self.real_time_event_handler = None
        self.nats_service = None
        self.nats_message_handler = None
        self.event_publisher = None

    def _init_game_attributes(self) -> None:
        self.player_service = None
        self.room_service = None
        self.movement_service = None
        self.player_position_service = None
        self.follow_service = None
        self.party_service = None
        self.exploration_service = None
        self.user_manager = None
        self.container_service = None
        self.level_service = None
        self.skill_service = None
        self.room_cache_service = None
        self.profession_cache_service = None

    def _init_extended_attributes(self) -> None:
        self.performance_monitor = None
        self.exception_tracker = None
        self.monitoring_dashboard = None
        self.log_aggregator = None
        self.holiday_service = None
        self.schedule_service = None
        self.mythos_tick_scheduler = None
        self.item_prototype_registry = None
        self.item_factory = None
        self.player_combat_service = None
        self.player_death_service = None
        self.player_respawn_service = None
        self.combat_service = None
        self.magic_service = None
        self.spell_registry = None
        self.spell_targeting_service = None
        self.spell_effects = None
        self.spell_learning_service = None
        self.mp_regeneration_service = None
        self.quest_definition_repository = None
        self.quest_instance_repository = None
        self.quest_service = None
        self.npc_lifecycle_manager = None
        self.npc_spawning_service = None
        self.npc_population_controller = None
        self.catatonia_registry = None
        self.passive_lucidity_flux_service = None
        self.mythos_time_consumer = None
        self.chat_service = None
        self.server_shutdown_pending = False
        self.shutdown_data = None
        self.tick_task = None

    def __init__(self) -> None:
        """Initialize the container. Services are NOT initialized here - use initialize()."""
        if ApplicationContainer._instance is not None:
            logger.warning("Multiple ApplicationContainer instances created - this may indicate a problem")

        self._init_core_attributes()
        self._init_realtime_attributes()
        self._init_game_attributes()
        self._init_extended_attributes()

        self._initialized: bool = False
        self._initialization_lock = Lock()
        self._project_root: Path | None = None

        logger.info("ApplicationContainer created (not yet initialized)")

    @classmethod
    def get_instance(cls) -> "ApplicationContainer":
        """Get the singleton container instance."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls) -> None:
        """Reset the container singleton. ONLY use this in tests."""
        with cls._lock:
            if cls._instance is not None:
                cls._instance = None
        logger.info("ApplicationContainer instance reset")

    @classmethod
    def set_instance(cls, instance: "ApplicationContainer") -> None:
        """Set the singleton container instance."""
        with cls._lock:
            cls._instance = instance
        logger.debug("ApplicationContainer instance set via set_instance()")

    async def _initialize_primary_bundles(self) -> None:
        from server.container.bundles import (
            CombatBundle,
            CoreBundle,
            GameBundle,
            MagicBundle,
            MonitoringBundle,
            NPCBundle,
            RealtimeBundle,
        )
        from server.container.bundles.combat import COMBAT_ATTRS
        from server.container.bundles.core import CORE_ATTRS
        from server.container.bundles.game import GAME_ATTRS
        from server.container.bundles.magic import MAGIC_ATTRS
        from server.container.bundles.monitoring import MONITORING_ATTRS
        from server.container.bundles.npc import NPC_ATTRS
        from server.container.bundles.realtime import REALTIME_ATTRS

        combat = CombatBundle()
        for bundle, attrs in (
            (CoreBundle(), CORE_ATTRS),
            (RealtimeBundle(), REALTIME_ATTRS),
            (GameBundle(), GAME_ATTRS),
            (MonitoringBundle(), MONITORING_ATTRS),
            (combat, COMBAT_ATTRS),
            (NPCBundle(), NPC_ATTRS),
        ):
            await bundle.initialize(self)
            _flatten_bundle(self, bundle, attrs)

        # Same instance as above: a fresh CombatBundle() has no services and fails NATS prerequisites.
        await combat.initialize_nats_combat(self)
        _flatten_bundle(self, combat, COMBAT_ATTRS)

        magic = MagicBundle()
        await magic.initialize(self)
        _flatten_bundle(self, magic, MAGIC_ATTRS)

    async def _initialize_secondary_bundles(self) -> None:
        from server.container.bundles import ChatBundle, TimeBundle
        from server.container.bundles.chat import CHAT_ATTRS
        from server.container.bundles.time import TIME_ATTRS

        chat = ChatBundle()
        await chat.initialize(self)
        _flatten_bundle(self, chat, CHAT_ATTRS)

        time_bundle = TimeBundle()
        await time_bundle.initialize(self)
        _flatten_bundle(self, time_bundle, TIME_ATTRS)

    def _link_cross_bundle_services(self) -> None:
        if self.combat_service and self.magic_service:
            self.combat_service.magic_service = self.magic_service
            logger.info("MagicService linked to CombatService")
        if self.quest_service and self.spell_learning_service:
            self.quest_service.set_spell_learning_service(self.spell_learning_service)
            logger.info("SpellLearningService linked to QuestService")

    async def initialize(self) -> None:  # pylint: disable=too-many-locals
        """Initialize all services via domain bundles in dependency order."""
        async with self._initialization_lock:
            if self._initialized:
                logger.warning("Container already initialized - skipping re-initialization")
                return

            logger.info("Initializing ApplicationContainer...")

            try:
                await self._initialize_primary_bundles()
                self._link_cross_bundle_services()
                await self._initialize_secondary_bundles()
                self._initialized = True
                logger.info("ApplicationContainer initialization complete")

            except Exception as e:
                logger.error(
                    "Failed to initialize application container",
                    error=str(e),
                    exc_info=True,
                )
                raise RuntimeError(f"Failed to initialize application container: {e}") from e

    async def shutdown(self) -> None:
        """Shutdown all services in reverse dependency order via bundles."""
        logger.info("Shutting down ApplicationContainer...")

        try:
            from server.container.bundles import CoreBundle, MonitoringBundle, RealtimeBundle

            monitoring = MonitoringBundle()
            monitoring.log_aggregator = self.log_aggregator
            await monitoring.shutdown(self)

            realtime = RealtimeBundle()
            realtime.nats_message_handler = self.nats_message_handler
            realtime.nats_service = self.nats_service
            await realtime.shutdown(self)

            core = CoreBundle()
            core.event_bus = self.event_bus
            core.database_manager = self.database_manager
            core.async_persistence = self.async_persistence
            await core.shutdown(self)

            logger.info("ApplicationContainer shutdown complete")

        except RuntimeError as e:
            logger.error(
                "Error during ApplicationContainer shutdown",
                error=str(e),
                exc_info=True,
            )

    def _get_project_root(self) -> Path:
        """Return and cache the repository root directory."""
        if self._project_root is None:
            self._project_root = get_project_root()
        return self._project_root

    def _decode_json_column(self, value: Any, expected_type: type) -> Any:
        """Delegate to shared util. Kept for backward compatibility."""
        return decode_json_column(value, expected_type)

    def _normalize_path_from_url_or_path(self, raw: str, project_root: Path) -> Path | None:
        """Delegate to shared util. Kept for backward compatibility."""
        return normalize_path_from_url_or_path(raw, project_root)

    def get_service(self, service_name: str) -> Any:
        """Get a service by name."""
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


def get_container() -> ApplicationContainer:
    """Get the application container singleton. Backward compatibility."""
    return ApplicationContainer.get_instance()


def reset_container() -> None:
    """Reset the container singleton. ONLY use this in tests."""
    ApplicationContainer.reset_instance()
