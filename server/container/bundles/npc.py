"""
NPC bundle: lifecycle manager, spawning service, population controller.

Depends on Core (event_bus, persistence, async_persistence).
"""

# pyright: reportImportCycles=false
# Reason: container/main.py imports this module (function-scoped) to construct NPCBundle;
# this file only imports ApplicationContainer under TYPE_CHECKING for parameter annotations.
# Same precedent as server/models/player.py and server/services/combat_service.py.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from server.structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.container.main import ApplicationContainer

logger = get_logger(__name__)

NPC_ATTRS = (
    "npc_lifecycle_manager",
    "npc_spawning_service",
    "npc_population_controller",
    "npc_startup_service",
)


class NPCBundle:  # pylint: disable=too-few-public-methods
    """NPC services: lifecycle, spawning, population control."""

    npc_lifecycle_manager: Any = None
    npc_spawning_service: Any = None
    npc_population_controller: Any = None
    npc_startup_service: Any = None

    async def _create_npc_services(self, container: ApplicationContainer) -> None:
        from server.npc.combat_integration import NPCCombatIntegration
        from server.npc.lifecycle_manager import NPCLifecycleManager
        from server.npc.population_control import NPCPopulationController
        from server.npc.spawning_service import NPCSpawningService
        from server.services.npc_instance_service import initialize_npc_instance_service
        from server.services.npc_startup_service import NPCStartupService

        self.npc_startup_service = NPCStartupService(async_persistence=container.async_persistence)

        combat_integration = NPCCombatIntegration(
            event_bus=container.event_bus, async_persistence=container.async_persistence
        )
        self.npc_spawning_service = NPCSpawningService(container.event_bus, None, combat_integration=combat_integration)
        self.npc_lifecycle_manager = NPCLifecycleManager(
            event_bus=container.event_bus,
            population_controller=None,
            spawning_service=self.npc_spawning_service,
            persistence=container.persistence,
        )
        self.npc_population_controller = NPCPopulationController(
            container.event_bus,
            self.npc_spawning_service,
            self.npc_lifecycle_manager,
            async_persistence=container.async_persistence,
        )
        self.npc_spawning_service.population_controller = self.npc_population_controller
        self.npc_lifecycle_manager.population_controller = self.npc_population_controller
        initialize_npc_instance_service(
            lifecycle_manager=self.npc_lifecycle_manager,
            spawning_service=self.npc_spawning_service,
            population_controller=self.npc_population_controller,
            event_bus=container.event_bus,
        )

    async def _load_npc_definitions(self) -> None:
        from server.npc_database import get_npc_session
        from server.services.npc_service import NPCService

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

    async def _start_npc_threads(self) -> None:
        if not hasattr(self.npc_lifecycle_manager, "thread_manager"):
            return
        try:
            await self.npc_lifecycle_manager.thread_manager.start()
            logger.info("NPC thread manager started")
            pending_starts = getattr(self.npc_lifecycle_manager, "_pending_thread_starts", [])
            for npc_id, definition in pending_starts:
                try:
                    await self.npc_lifecycle_manager.thread_manager.start_npc_thread(npc_id, definition)
                    logger.debug("Started queued NPC thread", npc_id=npc_id)
                except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
                    logger.warning("Failed to start queued NPC thread", npc_id=npc_id, error=str(e))
            pending_starts.clear()
        except (ValueError, TypeError, AttributeError, KeyError, RuntimeError) as e:
            logger.error("Failed to start NPC thread manager", error=str(e))

    async def initialize(self, container: ApplicationContainer) -> None:
        """Initialize NPC services and load definitions."""
        if container.event_bus is None:
            raise RuntimeError("EventBus must be initialized before NPC services")
        if container.persistence is None:
            raise RuntimeError("Persistence must be initialized before NPC services")
        if container.async_persistence is None:
            raise RuntimeError("AsyncPersistence must be initialized before NPC services")

        logger.debug("Initializing NPC services...")
        await self._create_npc_services(container)
        await self._load_npc_definitions()
        logger.info("NPC services initialized")
        await self._start_npc_threads()
