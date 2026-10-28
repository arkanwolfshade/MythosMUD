"""
The NPC side of instance content: spawn an NPC definition by name into an instance room, clear a set of rooms.

InstanceContentService talks to this through its InstanceNpcHost protocol. Spawns go through the
population controller so they are tracked like any other NPC, with the "instance_spawn" reason so
the zone-wide population limits (which count every player's private copy) do not refuse them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from ..npc.npc_utils import extract_room_id_from_npc
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..npc.lifecycle_manager import NPCLifecycleManager
    from ..npc.population_control import NPCPopulationController

logger = get_logger(__name__)

INSTANCE_SPAWN_REASON = "instance_spawn"
INSTANCE_DESPAWN_REASON = "instance_teardown"


class PopulationInstanceNpcHost:
    """Spawns and despawns instance NPCs through the population controller and lifecycle manager."""

    def __init__(self, population_controller: NPCPopulationController, lifecycle_manager: NPCLifecycleManager) -> None:
        """Wire the controller that spawns NPCs and the lifecycle manager that tracks the live ones."""
        self._population: NPCPopulationController = population_controller
        self._lifecycle: NPCLifecycleManager = lifecycle_manager

    def spawn(self, definition_name: str, room_id: str) -> str | None:
        """Spawn the NPC definition called definition_name in room_id; its npc id, or None if it could not spawn."""
        definition = next(
            (candidate for candidate in self._population.npc_definitions.values() if candidate.name == definition_name),
            None,
        )
        if definition is None:
            logger.warning("Instance NPC definition not found", definition_name=definition_name, room_id=room_id)
            return None
        npc_id, failure = self._population.spawn_npc(definition, room_id, INSTANCE_SPAWN_REASON)
        if npc_id is None:
            logger.warning(
                "Instance NPC spawn refused", definition_name=definition_name, room_id=room_id, failure=failure
            )
        return npc_id

    def despawn_in_rooms(self, room_prefix: str) -> int:
        """Despawn every live NPC whose room id starts with room_prefix; returns how many were despawned."""
        inside = [
            npc_id
            for npc_id, npc in list(self._lifecycle.active_npcs.items())
            if extract_room_id_from_npc(npc).startswith(room_prefix)
        ]
        return sum(1 for npc_id in inside if self._lifecycle.despawn_npc(npc_id, INSTANCE_DESPAWN_REASON))
