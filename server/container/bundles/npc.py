"""
NPC bundle: lifecycle manager, spawning service, population controller.

Depends on Core (event_bus, persistence, async_persistence).
"""

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
)


class NPCBundle:  # pylint: disable=too-few-public-methods
    """NPC services: lifecycle, spawning, population control."""

    npc_lifecycle_manager: Any = None
    npc_spawning_service: Any = None
    npc_population_controller: Any = None

    async def initialize(self, container: ApplicationContainer) -> None:  # pylint: disable=too-many-locals
        """Initialize NPC services and load definitions."""
        if container.event_bus is None:
            raise RuntimeError("EventBus must be initialized before NPC services")
        if container.persistence is None:
            raise RuntimeError("Persistence must be initialized before NPC services")
        if container.async_persistence is None:
            raise RuntimeError("AsyncPersistence must be initialized before NPC services")

        logger.debug("Initializing NPC services...")

        from server.npc.lifecycle_manager import NPCLifecycleManager
        from server.npc.population_control import NPCPopulationController
        from server.npc.spawning_service import NPCSpawningService
        from server.npc_database import get_npc_session
        from server.services.npc_instance_service import initialize_npc_instance_service
        from server.services.npc_service import NPCService

        self.npc_spawning_service = NPCSpawningService(container.event_bus, None)

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

        if hasattr(self.npc_lifecycle_manager, "thread_manager"):
            try:
                await self.npc_lifecycle_manager.thread_manager.start()
                logger.info("NPC thread manager started")

                if hasattr(self.npc_lifecycle_manager, "_pending_thread_starts"):
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
