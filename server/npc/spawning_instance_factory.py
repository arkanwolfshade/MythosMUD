"""Construct NPC behavior instances from definitions (no queue or population logic)."""

from __future__ import annotations

import random
import time
from typing import TYPE_CHECKING, cast

from structlog.stdlib import BoundLogger

from server.events.event_bus import EventBus
from server.models.npc import NPCDefinition
from server.npc.behaviors import AggressiveMobNPC, NPCBase, PassiveMobNPC, ShopkeeperNPC
from server.npc.combat_integration import NPCCombatIntegration
from server.npc.spawning_models import SimpleNPCDefinition

from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.services.npc_combat_integration_service import NPCCombatIntegrationService

logger: BoundLogger = cast(BoundLogger, get_logger(__name__))


def generate_npc_id(definition: NPCDefinition | SimpleNPCDefinition, room_id: str) -> str:
    """Build a unique NPC id from definition name, room, time, and a short random suffix."""
    timestamp = int(time.time())
    random_suffix = random.randint(1000, 9999)  # nosec B311: game id, not crypto
    definition_name = getattr(definition, "name", "unknown_npc")
    return f"{definition_name.lower().replace(' ', '_')}_{room_id}_{timestamp}_{random_suffix}"


def _coerce_simple_definition(definition: NPCDefinition) -> SimpleNPCDefinition:
    """Copy ORM definition fields into a plain SimpleNPCDefinition."""
    return SimpleNPCDefinition(
        id=getattr(definition, "id", 0),
        name=getattr(definition, "name", "Unknown NPC"),
        npc_type=getattr(definition, "npc_type", "unknown"),
        room_id=getattr(definition, "room_id", None),
        description=getattr(definition, "description", None),
        base_stats=getattr(definition, "base_stats", "{}"),
        behavior_config=getattr(definition, "behavior_config", "{}"),
        ai_integration_stub=getattr(definition, "ai_integration_stub", "{}"),
    )


def _build_shopkeeper(simple: SimpleNPCDefinition, npc_id: str, event_bus: EventBus) -> NPCBase:
    return ShopkeeperNPC(
        definition=simple,
        npc_id=npc_id,
        event_bus=event_bus,
        event_reaction_system=None,
    )


def _build_passive(simple: SimpleNPCDefinition, npc_id: str, event_bus: EventBus) -> NPCBase:
    return PassiveMobNPC(
        definition=simple,
        npc_id=npc_id,
        event_bus=event_bus,
        event_reaction_system=None,
    )


def _build_aggressive(
    simple: SimpleNPCDefinition,
    npc_id: str,
    event_bus: EventBus,
    combat_integration: NPCCombatIntegration | NPCCombatIntegrationService | None,
) -> NPCBase:
    npc = AggressiveMobNPC(
        definition=cast(NPCDefinition, cast(object, simple)),
        npc_id=npc_id,
        event_bus=event_bus,
        event_reaction_system=None,
    )
    if combat_integration:
        npc.combat_integration = combat_integration
    return npc


def _instantiate_by_type(
    simple: SimpleNPCDefinition,
    npc_id: str,
    event_bus: EventBus,
    combat_integration: NPCCombatIntegration | NPCCombatIntegrationService | None,
) -> NPCBase | None:
    kind = simple.npc_type
    if kind == "shopkeeper":
        return _build_shopkeeper(simple, npc_id, event_bus)
    if kind == "passive_mob":
        return _build_passive(simple, npc_id, event_bus)
    if kind == "aggressive_mob":
        return _build_aggressive(simple, npc_id, event_bus, combat_integration)
    if kind == "quest_giver":
        return _build_passive(simple, npc_id, event_bus)
    logger.warning("Unknown NPC type", npc_type=kind)
    return None


def _set_spawn_room(npc: NPCBase, room_id: str) -> None:
    npc.current_room = room_id
    npc.spawn_room_id = room_id


def create_npc_instance(
    definition: NPCDefinition,
    room_id: str,
    event_bus: EventBus,
    combat_integration: NPCCombatIntegration | NPCCombatIntegrationService | None,
    npc_id: str | None = None,
) -> NPCBase | None:
    """
    Create an NPC instance from a definition.

    Returns None if creation failed.
    """
    try:
        simple = _coerce_simple_definition(definition)
        resolved_id = npc_id if npc_id is not None else generate_npc_id(simple, room_id)
        npc_instance = _instantiate_by_type(simple, resolved_id, event_bus, combat_integration)
        if npc_instance is None:
            return None
        _set_spawn_room(npc_instance, room_id)
        return npc_instance

    except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: creation errors unpredictable
        logger.error(
            "Failed to create NPC instance",
            npc_type=getattr(definition, "npc_type", "unknown"),
            room_id=room_id,
            error=str(e),
        )
        return None
