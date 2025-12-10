"""
NPC look functionality for MythosMUD.

This module handles looking at NPCs, including finding matching NPCs,
formatting NPC descriptions, and handling NPC look requests.
"""

from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..services.npc_instance_service import get_npc_instance_service

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
    if not description or description.strip() == "":
        return "You see nothing remarkable about them."
    return description


def _format_single_npc_result(npc: Any, player_name: str) -> dict[str, Any]:
    """Format result for a single matching NPC."""
    logger.debug("Found NPC to look at", player=player_name, npc_name=npc.name, npc_id=npc.npc_id)
    description = _format_npc_description(npc)
    return {"result": f"{npc.name}\n{description}"}


def _format_multiple_npcs_result(matching_npcs: list[Any], target_lower: str, player_name: str) -> dict[str, Any]:
    """Format result for multiple matching NPCs."""
    npc_names = [npc.name for npc in matching_npcs]
    logger.debug("Multiple NPCs match target", player=player_name, matches=npc_names)
    return {"result": f"You see multiple NPCs matching '{target_lower}': {', '.join(npc_names)}"}


async def _try_lookup_npc_implicit(target_lower: str, room: Any, player_name: str) -> dict[str, Any] | None:
    """Try to find and display an NPC in implicit lookup."""
    npc_ids = room.get_npcs()
    if not npc_ids:
        return None

    matching_npcs = _find_matching_npcs(target_lower, npc_ids)
    if not matching_npcs:
        return None

    if len(matching_npcs) == 1:
        return _format_single_npc_result(matching_npcs[0], player_name)

    return _format_multiple_npcs_result(matching_npcs, target_lower, player_name)


async def _get_npcs_in_room(room_id: str) -> list[str]:
    """Get list of NPC names in a room from lifecycle manager."""
    npc_names: list[str] = []
    try:
        npc_instance_service = get_npc_instance_service()
        if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
            return npc_names

        lifecycle_manager = npc_instance_service.lifecycle_manager
        if not lifecycle_manager or not hasattr(lifecycle_manager, "active_npcs"):
            return npc_names

        active_npcs_dict = lifecycle_manager.active_npcs
        for _npc_id, npc_instance in active_npcs_dict.items():
            # Check both current_room and current_room_id for compatibility
            # Use hasattr to check if attribute exists to avoid MagicMock auto-creation
            current_room = None
            if hasattr(npc_instance, "current_room"):
                current_room = getattr(npc_instance, "current_room", None)
            current_room_id = None
            if hasattr(npc_instance, "current_room_id"):
                current_room_id = getattr(npc_instance, "current_room_id", None)
            # Prefer current_room_id over current_room, but use current_room if current_room_id is None
            npc_room_id = current_room_id if current_room_id is not None else current_room
            if npc_room_id == room_id:
                npc_name = getattr(npc_instance, "name", None)
                if npc_name and getattr(npc_instance, "is_alive", True):
                    npc_names.append(npc_name)
    except (AttributeError, TypeError, ValueError) as e:
        logger.warning("Error getting NPCs from lifecycle manager for room look", room_id=room_id, error=str(e))

    return npc_names


__all__ = [
    "_find_matching_npcs",
    "_format_npc_description",
    "_format_single_npc_result",
    "_format_multiple_npcs_result",
    "_try_lookup_npc_implicit",
    "_get_npcs_in_room",
]
