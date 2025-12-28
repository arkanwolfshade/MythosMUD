"""
Spawn Validator Module.

This module provides logic for validating whether NPCs should spawn based on
population limits, spawn rules, and game state conditions.
"""

import random
from typing import Any

from server.models.npc import NPCDefinition, NPCSpawnRule

from ..structured_logging.enhanced_logging_config import get_logger
from .zone_configuration import ZoneConfiguration

logger = get_logger(__name__)


def should_spawn_npc(
    definition: NPCDefinition,
    zone_config: ZoneConfiguration,
    room_id: str,  # noqa: ARG001
    population_stats: Any | None,
    spawn_rules: dict[int, list[NPCSpawnRule]],
    current_game_state: dict[str, Any],
) -> bool:
    """
    Determine if an NPC should spawn based on conditions.

    Args:
        definition: NPC definition
        zone_config: Zone configuration
        room_id: Target room ID
        population_stats: Population statistics for the zone (PopulationStats or None)
        spawn_rules: Dictionary mapping NPC definition IDs to spawn rules
        current_game_state: Current game state dictionary

    Returns:
        True if NPC should spawn, False otherwise
    """
    logger.info("Evaluating spawn conditions for NPC", npc_id=definition.id, npc_name=definition.name)

    # Check population limits
    if population_stats:
        # Check by individual NPC definition ID, not by type
        current_count = population_stats.npcs_by_definition.get(int(definition.id), 0)
        logger.info(
            "Current count for NPC in zone",
            npc_id=definition.id,
            npc_name=definition.name,
            current_count=current_count,
        )
        if not definition.can_spawn(current_count):
            logger.info(
                "NPC cannot spawn due to population limits",
                npc_id=definition.id,
                current_count=current_count,
                max_population=definition.max_population,
            )
            return False
    else:
        logger.info("No population stats found for zone")

    # Check spawn rules
    if int(definition.id) in spawn_rules:
        logger.info("Found spawn rules for NPC", rule_count=len(spawn_rules[int(definition.id)]), npc_id=definition.id)
        # Get current NPC count for population checks
        current_npc_count = population_stats.npcs_by_definition.get(int(definition.id), 0) if population_stats else 0

        for i, rule in enumerate(spawn_rules[int(definition.id)]):
            logger.info("Checking spawn rule", rule_number=i + 1, npc_id=definition.id)

            # Check if current NPC population is below the rule's max_population limit
            if not rule.can_spawn_with_population(current_npc_count):
                logger.info(
                    "Spawn rule failed population check",
                    rule_index=i + 1,
                    current_npc_count=current_npc_count,
                    max_population=rule.max_population,
                )
                continue

            logger.info("Spawn rule spawn conditions", rule_number=i + 1, spawn_conditions=rule.spawn_conditions)
            logger.info("Current game state", game_state=current_game_state)
            if not rule.check_spawn_conditions(current_game_state):
                logger.info("Spawn rule failed spawn conditions check", rule_number=i + 1)
                continue

            # Check spawn probability with zone modifier
            effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
            random_roll = random.random()
            logger.info(
                "Spawn rule probability check",
                rule_index=i + 1,
                roll=random_roll,
                threshold=effective_probability,
            )
            if random_roll <= effective_probability:
                logger.info("NPC should spawn based on spawn rule", npc_id=definition.id, rule_number=i + 1)
                return True
            else:
                logger.info("NPC failed probability roll for spawn rule", npc_id=definition.id, rule_number=i + 1)
    else:
        logger.info("No spawn rules found for NPC", npc_id=definition.id)

    # Required NPCs always spawn if conditions are met
    if definition.is_required():
        logger.info("NPC is required and conditions are met, spawning", npc_id=definition.id)
        return True

    logger.info("NPC should not spawn", npc_id=definition.id)
    return False
