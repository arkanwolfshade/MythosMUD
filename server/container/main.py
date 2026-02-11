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

    def __init__(self) -> None:
        """Initialize the container. Services are NOT initialized here - use initialize()."""
        if ApplicationContainer._instance is not None:
            logger.warning("Multiple ApplicationContainer instances created - this may indicate a problem")

        self.config: Any = None
        self.database_manager: Any = None
        self.task_registry: Any = None
        self.tracked_task_manager: Any = None
        self.event_bus: Any = None
        self.persistence: Any = None
        self.async_persistence: Any = None

        self.connection_manager: Any = None
        self.real_time_event_handler: Any = None
        self.nats_service: Any = None
        self.nats_message_handler: Any = None
        self.event_publisher: Any = None

        self.player_service: Any = None
        self.room_service: Any = None
        self.movement_service: Any = None
        self.follow_service: Any = None
        self.party_service: Any = None
        self.exploration_service: Any = None
        self.user_manager: Any = None
        self.container_service: Any = None

        self.room_cache_service: Any = None
        self.profession_cache_service: Any = None

        self.performance_monitor: Any = None
        self.exception_tracker: Any = None
        self.monitoring_dashboard: Any = None
        self.log_aggregator: Any = None

        self.holiday_service: Any = None
        self.schedule_service: Any = None
        self.mythos_tick_scheduler: Any = None

        self.item_prototype_registry: Any = None
        self.item_factory: Any = None

        self.player_combat_service: Any = None
        self.player_death_service: Any = None
        self.player_respawn_service: Any = None
        self.combat_service: Any = None

        self.magic_service: Any = None
        self.spell_registry: Any = None
        self.spell_targeting_service: Any = None
        self.spell_effects: Any = None
        self.spell_learning_service: Any = None
        self.mp_regeneration_service: Any = None

        self.npc_lifecycle_manager: Any = None
        self.npc_spawning_service: Any = None
        self.npc_population_controller: Any = None

        self.catatonia_registry: Any = None
        self.passive_lucidity_flux_service: Any = None
        self.mythos_time_consumer: Any = None
        self.chat_service: Any = None

        self.server_shutdown_pending: bool = False
        self.shutdown_data: dict[str, Any] | None = None
        self.tick_task: Any = None

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

    async def initialize(self) -> None:  # pylint: disable=too-many-locals
        """Initialize all services via domain bundles in dependency order."""
        from server.container.bundles import (
            ChatBundle,
            CombatBundle,
            CoreBundle,
            GameBundle,
            MagicBundle,
            MonitoringBundle,
            NPCBundle,
            RealtimeBundle,
            TimeBundle,
        )
        from server.container.bundles.chat import CHAT_ATTRS
        from server.container.bundles.combat import COMBAT_ATTRS
        from server.container.bundles.core import CORE_ATTRS
        from server.container.bundles.game import GAME_ATTRS
        from server.container.bundles.magic import MAGIC_ATTRS
        from server.container.bundles.monitoring import MONITORING_ATTRS
        from server.container.bundles.npc import NPC_ATTRS
        from server.container.bundles.realtime import REALTIME_ATTRS
        from server.container.bundles.time import TIME_ATTRS

        async with self._initialization_lock:
            if self._initialized:
                logger.warning("Container already initialized - skipping re-initialization")
                return

            logger.info("Initializing ApplicationContainer...")

            try:
                core = CoreBundle()
                await core.initialize(self)
                _flatten_bundle(self, core, CORE_ATTRS)

                realtime = RealtimeBundle()
                await realtime.initialize(self)
                _flatten_bundle(self, realtime, REALTIME_ATTRS)

                game = GameBundle()
                await game.initialize(self)
                _flatten_bundle(self, game, GAME_ATTRS)

                monitoring = MonitoringBundle()
                await monitoring.initialize(self)
                _flatten_bundle(self, monitoring, MONITORING_ATTRS)

                combat = CombatBundle()
                await combat.initialize(self)
                _flatten_bundle(self, combat, COMBAT_ATTRS)

                npc_bundle = NPCBundle()
                await npc_bundle.initialize(self)
                _flatten_bundle(self, npc_bundle, NPC_ATTRS)

                await combat.initialize_nats_combat(self)
                _flatten_bundle(self, combat, COMBAT_ATTRS)

                magic = MagicBundle()
                await magic.initialize(self)
                _flatten_bundle(self, magic, MAGIC_ATTRS)

                if self.combat_service and self.magic_service:
                    self.combat_service.magic_service = self.magic_service
                    logger.info("MagicService linked to CombatService")

                chat = ChatBundle()
                await chat.initialize(self)
                _flatten_bundle(self, chat, CHAT_ATTRS)

                time_bundle = TimeBundle()
                await time_bundle.initialize(self)
                _flatten_bundle(self, time_bundle, TIME_ATTRS)

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
