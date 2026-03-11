"""
Periodic maintenance and optional NPC spawn checks for lifecycle.

Extracted from lifecycle_manager to keep file NLOC under complexity limits.
"""

import random
import time
from typing import Any

from server.models.npc import NPCDefinition

from ..config.npc_config import NPCMaintenanceConfig
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def cleanup_old_records_impl(manager: Any, max_age_seconds: int = 86400) -> int:
    """Clean up old lifecycle records. Returns number of records removed."""
    current_time = time.time()
    records_to_remove = []

    from .lifecycle_types import NPCLifecycleState

    for npc_id, record in list(manager.lifecycle_records.items()):
        age = current_time - record.created_at
        if age > max_age_seconds and record.current_state in (
            NPCLifecycleState.DESPAWNED,
            NPCLifecycleState.ERROR,
        ):
            records_to_remove.append(npc_id)

    for npc_id in records_to_remove:
        del manager.lifecycle_records[npc_id]

    if records_to_remove:
        logger.info("Cleaned up old lifecycle records", count=len(records_to_remove))

    return len(records_to_remove)


def run_periodic_maintenance_impl(manager: Any) -> dict[str, Any]:
    """Run respawn queue, optional NPC spawn checks, and cleanup. Returns results dict."""
    current_time = time.time()
    results = {}

    respawned_count = manager.process_respawn_queue()
    results["respawned_npcs"] = respawned_count

    try:
        spawn_check_results = check_optional_npc_spawns_impl(manager)
        results["spawned_npcs"] = spawn_check_results["spawned_count"]
        results["spawn_checks_performed"] = spawn_check_results["checks_performed"]
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Periodic spawn check errors unpredictable
        logger.error("Error during periodic spawn checks", error=str(e))
        results["spawned_npcs"] = 0
        results["spawn_checks_performed"] = 0

    if current_time - manager.last_cleanup > manager.cleanup_interval:
        cleaned_count = cleanup_old_records_impl(manager)
        results["cleaned_records"] = cleaned_count
        manager.last_cleanup = current_time

    return results


def check_optional_npc_spawns_impl(manager: Any) -> dict[str, int]:
    """Check if optional NPCs should spawn; return spawned_count and checks_performed."""
    if not manager.population_controller:
        return {"spawned_count": 0, "checks_performed": 0}

    current_time = time.time()
    spawned_count = 0
    checks_performed = 0

    for definition_id, definition in manager.population_controller.npc_definitions.items():
        should_skip, _last_check = _should_skip_optional_npc(manager, definition_id, definition, current_time)
        if should_skip:
            continue

        manager.last_spawn_check[definition_id] = current_time
        checks_performed += 1

        zone_key = get_zone_key_for_definition(manager, definition)
        if not zone_key:
            continue

        can_spawn, _ = _check_spawn_conditions_for_optional_npc(manager, definition_id, definition, zone_key)
        if not can_spawn:
            continue

        npc_id = _attempt_optional_npc_spawn(manager, definition, zone_key)
        if npc_id:
            spawned_count += 1

    return {"spawned_count": spawned_count, "checks_performed": checks_performed}


def _should_skip_optional_npc(
    manager: Any, definition_id: int, definition: Any, current_time: float
) -> tuple[bool, float]:
    """Return (should_skip, last_check_time)."""
    if definition.is_required():
        return True, 0

    npc_in_respawn_queue = any(data["definition"].id == definition_id for data in manager.respawn_queue.values())
    if npc_in_respawn_queue:
        logger.debug(
            "Skipping periodic spawn check - NPC in respawn queue",
            npc_name=definition.name,
            definition_id=definition_id,
        )
        return True, 0

    last_check = manager.last_spawn_check.get(definition_id, 0)
    if current_time - last_check < NPCMaintenanceConfig.MIN_SPAWN_CHECK_INTERVAL:
        return True, last_check

    return False, last_check


def _check_spawn_conditions_for_optional_npc(
    manager: Any, definition_id: int, definition: Any, zone_key: str
) -> tuple[bool, int]:
    """Return (can_spawn, current_count)."""
    if manager.population_controller is None:
        return False, 0

    zone_config = manager.population_controller.get_zone_configuration(zone_key)
    if not zone_config:
        return False, 0

    stats = manager.population_controller.get_population_stats(zone_key)
    current_count = stats.npcs_by_definition.get(definition_id, 0) if stats else 0

    if not definition.can_spawn(current_count):
        logger.debug(
            "Optional NPC spawn check: population limit reached",
            npc_name=definition.name,
            current_count=current_count,
            max_population=definition.max_population,
        )
        return False, current_count

    return True, current_count


def _attempt_optional_npc_spawn(manager: Any, definition: Any, zone_key: str) -> str | None:
    """Attempt to spawn an optional NPC. Returns npc_id if spawned, else None."""
    if manager.population_controller is None:
        return None

    zone_config = manager.population_controller.get_zone_configuration(zone_key)
    if zone_config is None:
        return None

    effective_probability = zone_config.get_effective_spawn_probability(float(definition.spawn_probability))
    if random.random() > effective_probability:  # nosec B311: Game mechanics spawn probability
        return None

    spawn_room_id = get_spawn_room_for_definition(manager, definition)
    if not spawn_room_id:
        logger.warning("No spawn room found for optional NPC", npc_name=definition.name)
        return None

    npc_id: str | None
    npc_id, _ = manager.spawn_npc(definition, spawn_room_id, "periodic_spawn_check")
    if npc_id is not None:
        logger.info(
            "Periodic spawn check successful",
            npc_name=definition.name,
            npc_id=npc_id,
            room_id=spawn_room_id,
        )
    return npc_id


def get_zone_key_for_definition(manager: Any, definition: NPCDefinition) -> str | None:
    """Get zone key for an NPC definition (e.g. from sub_zone_id / room_id)."""
    if not definition.sub_zone_id:
        return None

    if manager.population_controller and int(definition.id) in manager.population_controller.spawn_rules:
        if definition.room_id:
            zone_key: str = manager.population_controller._get_zone_key_from_room_id(  # pylint: disable=protected-access
                str(definition.room_id)
            )
            return zone_key
    return None


def get_spawn_room_for_definition(manager: Any, definition: NPCDefinition) -> str | None:  # pylint: disable=unused-argument  # Reason: manager kept for API consistency with other helpers
    """Get spawn room ID for an NPC definition."""
    if definition.room_id:
        return str(definition.room_id)
    logger.warning(
        "No room_id configured for NPC definition",
        npc_name=definition.name,
        definition_id=definition.id,
    )
    return None
