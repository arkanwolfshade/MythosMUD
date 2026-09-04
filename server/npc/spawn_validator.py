"""
Spawn Validator Module.

This module provides logic for validating whether NPCs should spawn based on
population limits, spawn rules, and game state conditions.
"""

import random
from collections.abc import Mapping
from typing import Any

from server.models.npc import NPCDefinition, NPCSpawnRule

from ..structured_logging.enhanced_logging_config import get_logger
from .zone_configuration import ZoneConfiguration

logger = get_logger(__name__)


def _population_allows_spawn(definition: NPCDefinition, population_stats: Any | None) -> bool:
    """Return False when zone population blocks this NPC definition."""
    if not population_stats:
        logger.info("No population stats found for zone")
        return True

    current_count = population_stats.npcs_by_definition.get(int(definition.id), 0)
    logger.info(
        "Current count for NPC in zone",
        npc_id=definition.id,
        npc_name=definition.name,
        current_count=current_count,
    )
    if definition.can_spawn(current_count):
        return True

    logger.info(
        "NPC cannot spawn due to population limits",
        npc_id=definition.id,
        current_count=current_count,
        max_population=definition.max_population,
    )
    return False


def _spawn_rule_passes(
    rule: NPCSpawnRule,
    rule_index: int,
    definition: NPCDefinition,
    zone_config: ZoneConfiguration,
    current_npc_count: int,
    current_game_state: Mapping[str, object],
) -> bool:
    """Evaluate one spawn rule; return True when probability roll succeeds."""
    logger.info("Checking spawn rule", rule_number=rule_index + 1, npc_id=definition.id)
    if not rule.can_spawn_with_population(current_npc_count):
        logger.info(
            "Spawn rule failed population check",
            rule_index=rule_index + 1,
            current_npc_count=current_npc_count,
            max_population=rule.max_population,
        )
        return False

    logger.info("Spawn rule spawn conditions", rule_number=rule_index + 1, spawn_conditions=rule.spawn_conditions)
    logger.info("Current game state", game_state=current_game_state)
    if not rule.check_spawn_conditions(current_game_state):
        logger.info("Spawn rule failed spawn conditions check", rule_number=rule_index + 1)
        return False

    effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
    random_roll = random.random()  # nosec B311: Game mechanics spawn probability check, not cryptographic
    logger.info(
        "Spawn rule probability check",
        rule_index=rule_index + 1,
        roll=random_roll,
        threshold=effective_probability,
    )
    if random_roll <= effective_probability:
        logger.info("NPC should spawn based on spawn rule", npc_id=definition.id, rule_number=rule_index + 1)
        return True

    logger.info("NPC failed probability roll for spawn rule", npc_id=definition.id, rule_number=rule_index + 1)
    return False


def _try_spawn_rules(
    definition: NPCDefinition,
    zone_config: ZoneConfiguration,
    population_stats: Any | None,
    spawn_rules: dict[int, list[NPCSpawnRule]],
    current_game_state: Mapping[str, object],
) -> bool:
    """Return True when any spawn rule passes probability checks."""
    rules = spawn_rules.get(int(definition.id))
    if not rules:
        logger.info("No spawn rules found for NPC", npc_id=definition.id)
        return False

    logger.info("Found spawn rules for NPC", rule_count=len(rules), npc_id=definition.id)
    current_npc_count = population_stats.npcs_by_definition.get(int(definition.id), 0) if population_stats else 0
    for index, rule in enumerate(rules):
        if _spawn_rule_passes(rule, index, definition, zone_config, current_npc_count, current_game_state):
            return True
    return False


def should_spawn_npc(
    definition: NPCDefinition,
    zone_config: ZoneConfiguration,
    _room_id: str,  # pylint: disable=unused-argument  # Reason: Parameter reserved for future room-based validation
    population_stats: Any | None,
    spawn_rules: dict[int, list[NPCSpawnRule]],
    current_game_state: Mapping[str, object],
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

    if not _population_allows_spawn(definition, population_stats):
        return False

    if _try_spawn_rules(definition, zone_config, population_stats, spawn_rules, current_game_state):
        return True

    if definition.is_required():
        logger.info("NPC is required and conditions are met, spawning", npc_id=definition.id)
        return True

    logger.info("NPC should not spawn", npc_id=definition.id)
    return False
