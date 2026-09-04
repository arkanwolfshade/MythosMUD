"""
NPC look functionality for MythosMUD.

This module handles looking at NPCs, including finding matching NPCs,
formatting NPC descriptions, and handling NPC look requests.
"""

import json
from datetime import datetime
from typing import Any, cast

from ..services.npc_instance_service import get_npc_instance_service
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


def _find_matching_npcs(target_lower: str, npc_ids: list[Any]) -> list[Any]:
    """Find NPCs matching the target name."""
    matching_npcs = []
    for npc_id in npc_ids:
        npc_instance_service = get_npc_instance_service()
        if not hasattr(npc_instance_service, "lifecycle_manager"):
            continue

        lifecycle_manager = npc_instance_service.lifecycle_manager
        if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
            continue

        npc_instance = lifecycle_manager.active_npcs[npc_id]
        if npc_instance and target_lower in npc_instance.name.lower():
            matching_npcs.append(npc_instance)

    return matching_npcs


def _format_npc_description(npc: Any) -> str:
    """Format NPC description with fallback."""
    definition = npc.definition
    description = getattr(definition, "description", None)
    # Try alternative attributes if description is None
    if not description:
        description = getattr(definition, "long_description", None)
    if not description:
        description = getattr(definition, "short_description", None)
    if not description:
        description = getattr(definition, "desc", None)
    if not description or not description.strip():
        return "You see nothing remarkable about them."
    return cast(str, description)


def _parse_npc_stats_dict(npc_stats: Any) -> dict[str, Any]:
    """Parse NPC stats dictionary, handling both dict and JSON string formats."""
    if isinstance(npc_stats, str):
        try:
            return cast(dict[str, Any], json.loads(npc_stats))
        except (json.JSONDecodeError, TypeError):
            return {}
    if isinstance(npc_stats, dict):
        return npc_stats
    return {}


def _format_core_attributes(npc_stats: dict[str, Any]) -> list[str]:
    """Format core attributes section."""
    core_attributes = {
        "strength": "STR",
        "dexterity": "DEX",
        "constitution": "CON",
        "size": "SIZ",
        "intelligence": "INT",
        "power": "POW",
        "education": "EDU",
        "charisma": "CHA",
        "luck": "LUCK",
    }

    core_lines = []
    for attr_key, attr_label in core_attributes.items():
        if attr_key in npc_stats:
            core_lines.append(f"  {attr_label}: {npc_stats[attr_key]}")

    if not core_lines:
        return []

    result = ["\nCore Attributes:"]
    result.extend(core_lines)
    return result


def _format_other_stats(npc_stats: dict[str, Any]) -> list[str]:
    """Format other stats section (excluding core attributes)."""
    core_attributes = {
        "strength",
        "dexterity",
        "constitution",
        "size",
        "intelligence",
        "power",
        "education",
        "charisma",
        "luck",
    }
    other_stats = {k: v for k, v in npc_stats.items() if k not in core_attributes}

    if not other_stats:
        return []

    result = ["\nOther Stats:"]
    for key, value in sorted(other_stats.items()):
        result.append(f"  {key}: {value}")
    return result


def _parse_stat_datetime(dt_value: Any) -> str:
    """Parse datetime value from various formats and return formatted string."""
    if not dt_value:
        return "Unknown"

    try:
        if isinstance(dt_value, int | float):
            dt = datetime.fromtimestamp(dt_value)
        elif isinstance(dt_value, datetime):
            dt = dt_value
        else:
            dt = datetime.fromisoformat(str(dt_value))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError, OSError):
        return str(dt_value)


def _format_lifecycle_info(stats: dict[str, Any]) -> list[str]:
    """Format lifecycle information section."""
    if "lifecycle_state" not in stats:
        return []

    result = ["\nLifecycle:"]
    result.append(f"  State: {stats.get('lifecycle_state', 'Unknown')}")

    if "spawn_time" in stats:
        spawn_time_str = _parse_stat_datetime(stats.get("spawn_time"))
        result.append(f"  Spawn Time: {spawn_time_str}")

    if "last_activity" in stats:
        activity_str = _parse_stat_datetime(stats.get("last_activity"))
        result.append(f"  Last Activity: {activity_str}")

    if "spawn_count" in stats:
        result.append(f"  Spawn Count: {stats.get('spawn_count', 0)}")

    if "despawn_count" in stats:
        result.append(f"  Despawn Count: {stats.get('despawn_count', 0)}")

    return result


async def _format_npc_stats_for_admin(npc: Any) -> str:
    """Format NPC stats for admin display."""
    try:
        npc_id = getattr(npc, "npc_id", None)
        if not npc_id:
            return "\n--- Admin Stats ---\n(Error: NPC ID not found)"
        npc_instance_service = get_npc_instance_service()
        stats = await npc_instance_service.get_npc_stats(npc_id)

        stat_lines = ["\n--- Admin Stats ---"]
        stat_lines.append(f"NPC ID: {stats.get('npc_id', 'Unknown')}")
        stat_lines.append(f"Type: {stats.get('npc_type', 'Unknown')}")
        stat_lines.append(f"Room: {stats.get('current_room_id', 'Unknown')}")
        stat_lines.append(f"Alive: {stats.get('is_alive', 'Unknown')}")

        # Format the stats dictionary if it exists
        npc_stats_raw = stats.get("stats", {})
        if npc_stats_raw:
            npc_stats = _parse_npc_stats_dict(npc_stats_raw)
            if npc_stats:
                stat_lines.extend(_format_core_attributes(npc_stats))
                stat_lines.extend(_format_other_stats(npc_stats))

        # Add lifecycle info if available
        stat_lines.extend(_format_lifecycle_info(stats))

        return "\n".join(stat_lines)
    except (ValueError, TypeError, AttributeError) as e:
        logger.warning("Error formatting NPC stats for admin", npc_id=getattr(npc, "npc_id", None), error=str(e))
        return "\n--- Admin Stats ---\n(Error retrieving stats)"


async def _format_single_npc_result(npc: Any, player_name: str, player: Any | None = None) -> dict[str, Any]:
    """Format result for a single matching NPC."""
    npc_id = getattr(npc, "npc_id", None)
    logger.debug("Found NPC to look at", player=player_name, npc_name=getattr(npc, "name", "Unknown"), npc_id=npc_id)
    description = _format_npc_description(npc)
    result_text = f"{npc.name}\n{description}"

    # If player is admin, append stats
    if player and hasattr(player, "is_admin") and getattr(player, "is_admin", False):
        stats_text = await _format_npc_stats_for_admin(npc)
        result_text += stats_text

    return {"result": result_text}


def _format_multiple_npcs_result(matching_npcs: list[Any], target_lower: str, player_name: str) -> dict[str, Any]:
    """Format result for multiple matching NPCs."""
    npc_names = [npc.name for npc in matching_npcs]
    logger.debug("Multiple NPCs match target", player=player_name, matches=npc_names)
    return {"result": f"You see multiple NPCs matching '{target_lower}': {', '.join(npc_names)}"}


async def _try_lookup_npc_implicit(
    target_lower: str, room: Any, player_name: str, player: Any | None = None
) -> dict[str, Any] | None:
    """Try to find and display an NPC in implicit lookup."""
    npc_ids = room.get_npcs()
    if not npc_ids:
        return None

    matching_npcs = _find_matching_npcs(target_lower, npc_ids)
    if not matching_npcs:
        return None

    if len(matching_npcs) == 1:
        return await _format_single_npc_result(matching_npcs[0], player_name, player)

    return _format_multiple_npcs_result(matching_npcs, target_lower, player_name)


def _get_lifecycle_manager() -> Any | None:
    """Get the lifecycle manager from the NPC instance service."""
    try:
        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
            return None

        lifecycle_manager = npc_instance_service.lifecycle_manager
        if not lifecycle_manager or not hasattr(lifecycle_manager, "active_npcs"):
            return None

        return lifecycle_manager
    except (AttributeError, TypeError, ValueError):
        return None


def _get_npc_room_id(npc_instance: Any) -> str | None:
    """Get the room ID from an NPC instance, checking both current_room and current_room_id."""
    current_room = None
    if hasattr(npc_instance, "current_room"):
        current_room = getattr(npc_instance, "current_room", None)
    current_room_id = None
    if hasattr(npc_instance, "current_room_id"):
        current_room_id = getattr(npc_instance, "current_room_id", None)
    # Prefer current_room_id over current_room, but use current_room if current_room_id is None
    return current_room_id if current_room_id is not None else current_room


def _should_include_npc(npc_instance: Any) -> bool:
    """Check if an NPC should be included in the results (has name and is alive)."""
    npc_name = getattr(npc_instance, "name", None)
    is_alive = getattr(npc_instance, "is_alive", True)
    return bool(npc_name and is_alive)


async def _get_npcs_in_room(room_id: str) -> list[str]:
    """Get list of NPC names in a room from lifecycle manager."""
    npc_names: list[str] = []
    try:
        lifecycle_manager = _get_lifecycle_manager()
        if not lifecycle_manager:
            return npc_names

        active_npcs_dict = lifecycle_manager.active_npcs
        for _npc_id, npc_instance in active_npcs_dict.items():
            npc_room_id = _get_npc_room_id(npc_instance)
            if npc_room_id == room_id and _should_include_npc(npc_instance):
                npc_name = getattr(npc_instance, "name", None)
                if isinstance(npc_name, str):
                    npc_names.append(npc_name)
    except (AttributeError, TypeError, ValueError) as e:
        logger.warning("Error getting NPCs from lifecycle manager for room look", room_id=room_id, error=str(e))

    return npc_names


__all__ = [
    "_find_matching_npcs",
    "_format_npc_description",
    "_format_npc_stats_for_admin",
    "_format_single_npc_result",
    "_format_multiple_npcs_result",
    "_try_lookup_npc_implicit",
    "_get_lifecycle_manager",
    "_get_npc_room_id",
    "_should_include_npc",
    "_get_npcs_in_room",
]
