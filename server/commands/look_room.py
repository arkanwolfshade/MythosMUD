"""
Room look functionality for MythosMUD.

This module handles looking at rooms, including formatting room descriptions,
listing items, NPCs, players, and exits in the room.
"""

from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..utils.room_renderer import format_room_drop_lines
from .look_npc import _get_npcs_in_room
from .look_player import _get_players_in_room

logger = get_logger(__name__)


def _format_items_section(room_drops: list[dict[str, Any]]) -> list[str]:
    """Format the items/containers/corpses section of room look."""
    drop_lines = format_room_drop_lines(room_drops)
    if not drop_lines:
        return []
    return [str(line) for line in drop_lines] + [""]


async def _format_npcs_section(room_id: str | None) -> list[str]:
    """Format the NPCs/Mobs section of room look."""
    if not room_id:
        return []
    npc_names = await _get_npcs_in_room(room_id)
    if not npc_names:
        return []
    if len(npc_names) == 1:
        return [f"You see {npc_names[0]} here.", ""]
    npc_list = ", ".join(npc_names)
    return [f"You see {npc_list} here.", ""]


def _filter_other_players(players_in_room: list[Any], player_name: str) -> list[str]:
    """Filter out the current player from the list of players in room."""
    player_names = []
    for p in players_in_room:
        if hasattr(p, "name") and p.name != player_name:
            player_names.append(p.name)
    return player_names


def _format_players_section(player_names: list[str]) -> list[str]:
    """Format the players section of room look."""
    if not player_names:
        return []
    if len(player_names) == 1:
        return [f"{player_names[0]} is here.", ""]
    player_list = ", ".join(player_names)
    return [f"{player_list} are here.", ""]


def _get_room_description(room: Any) -> str:
    """Get room description with fallback."""
    if room.description is not None:
        return str(room.description)
    return "You see nothing special."


def _get_room_id(room: Any) -> str | None:
    """Get room ID safely."""
    if hasattr(room, "id"):
        return room.id
    return None


def _format_exits_list(exits: dict[str, Any]) -> str:
    """Format exits list for room look."""
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    if valid_exits:
        return ", ".join(valid_exits)
    return "none"


async def _handle_room_look(
    room: Any,
    room_drops: list[dict[str, Any]],
    persistence: Any,
    player_name: str,
) -> dict[str, Any]:
    """Handle looking at the current room."""
    desc = _get_room_description(room)
    exit_list = _format_exits_list(room.exits)
    room_id = _get_room_id(room)

    logger.debug(
        "Looked at current room",
        player=player_name,
        room_id=room_id,
        exits=[d for d, rid in room.exits.items() if rid is not None],
    )

    lines = [desc, ""]

    # 3. Items/containers/corpses
    lines.extend(_format_items_section(room_drops))

    # 5. NPCs/Mobs
    lines.extend(await _format_npcs_section(room_id))

    # 7. Players
    players_in_room = await _get_players_in_room(room, persistence)
    player_names = _filter_other_players(players_in_room, player_name)
    lines.extend(_format_players_section(player_names))

    # 9. Exits
    lines.append(f"Exits: {exit_list}")
    rendered = "\n".join(lines)

    drop_lines = format_room_drop_lines(room_drops)
    return {
        "result": rendered,
        "drop_summary": "\n".join(drop_lines),  # Keep for backward compatibility
        "room_drops": room_drops,  # Keep for backward compatibility
    }


async def _handle_direction_look(
    direction: str,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle looking in a specific direction."""
    direction = direction.lower()
    logger.debug("Looking in direction", player=player_name, direction=direction)
    exits = room.exits
    target_room_id = exits.get(direction)
    if target_room_id:
        target_room = persistence.get_room_by_id(target_room_id)
        if target_room:
            name = str(target_room.name) if target_room.name is not None else "Unknown Room"
            desc = str(target_room.description) if target_room.description is not None else "You see nothing special."
            logger.debug(
                "Looked at room in direction",
                player=player_name,
                direction=direction,
                target_room_id=target_room_id,
            )
            return {"result": f"{name}\n{desc}"}
    logger.debug("No valid exit in direction", player=player_name, direction=direction)
    return {"result": "You see nothing special that way."}


__all__ = [
    "_format_items_section",
    "_format_npcs_section",
    "_filter_other_players",
    "_format_players_section",
    "_get_room_description",
    "_get_room_id",
    "_format_exits_list",
    "_handle_room_look",
    "_handle_direction_look",
]
