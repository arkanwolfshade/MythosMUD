"""Startup wiring for instance content (furniture, floor items and NPCs of instanced rooms)."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from ..container import ApplicationContainer
from ..game.items.item_factory import ItemFactory
from ..game.items.prototype_registry import PrototypeRegistry
from ..services.instance_content import InstanceContentPersistence, InstanceContentService, InstanceNpcHost
from ..services.instance_npc_host import PopulationInstanceNpcHost
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController
    from ..realtime.connection_manager import ConnectionManager

logger = get_logger("server.lifespan.instance")


def wire_instance_content(container: ApplicationContainer) -> InstanceContentService | None:
    """Build the instance content service and attach it to the flush service and the container.

    Needs the item prototype registry and factory, persistence, the realtime room manager and the
    flush service. The NPC services are optional: without them instances get no NPCs. Returns None,
    and wires nothing, when a required service is missing; instances then simply stay unpopulated.
    """
    flusher = container.instance_flush_service
    registry = cast(object, container.item_prototype_registry)
    factory = cast(object, container.item_factory)
    persistence = cast(object | None, container.async_persistence)
    connection_manager = cast("ConnectionManager | None", container.connection_manager)
    if (
        flusher is None
        or persistence is None
        or connection_manager is None
        or not isinstance(registry, PrototypeRegistry)
        or not isinstance(factory, ItemFactory)
    ):
        logger.warning("Instance content not wired: item services, persistence or flush service unavailable")
        return None
    population = cast("NPCPopulationController | None", container.npc_population_controller)
    lifecycle = cast("NPCLifecycleManager | None", container.npc_lifecycle_manager)
    npcs: InstanceNpcHost | None = (
        PopulationInstanceNpcHost(population, lifecycle) if population is not None and lifecycle is not None else None
    )
    content = InstanceContentService(
        cast(InstanceContentPersistence, persistence),
        registry,
        factory,
        connection_manager.room_manager,
        npcs,
    )
    flusher.attach_content(content)
    container.instance_content_service = content
    logger.info("Instance content wired", npcs=npcs is not None)
    return content
