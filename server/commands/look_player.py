"""
Player look functionality for MythosMUD.

This module handles looking at players, including finding matching players,
formatting player display, and handling player look requests.
"""

import uuid
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from .look_helpers import _get_health_label, _get_lucidity_label, _get_visible_equipment

logger = get_logger(__name__)


async def _get_players_in_room(room: Any, persistence: Any) -> list[Any]:
    """
    Get all Player objects currently in the room.

    Args:
        room: Room object with get_players() method
        persistence: AsyncPersistenceLayer object with get_player_by_id() method

    Returns:
        List of Player objects in the room (None players filtered out)
    """
    player_ids = room.get_players() if hasattr(room, "get_players") else []
    # Ensure player_ids is iterable (handle Mock objects in tests)
    # Check if it's a list/tuple first, then try to iterate safely
    if not isinstance(player_ids, (list, tuple)):
        # If it's not a list/tuple, try to convert it safely
        # Mock objects can be iterable but might not behave as expected
        try:
            # Try to convert to list to validate it's truly iterable
            if player_ids is not None:
                player_ids = list(player_ids)
            else:
                player_ids = []
        except (TypeError, ValueError) as e:
            logger.debug(
                "room.get_players() returned non-iterable value",
                room_id=getattr(room, "id", None),
                error=str(e),
            )
            return []
    players = []
    try:
        for player_id_str in player_ids:
            try:
                # Convert string to UUID if needed
                player_id = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                # Use get_player_by_id (async method)
                player = await persistence.get_player_by_id(player_id) if hasattr(persistence, "get_player_by_id") else None
                if player:
                    players.append(player)
            except (ValueError, AttributeError):
                # Invalid UUID format or persistence doesn't have get_player
                logger.debug("Failed to get player", player_id=player_id_str, error="Invalid UUID or missing method")
                continue
    except TypeError as e:
        # Handle case where player_ids is not iterable (e.g., Mock object)
        logger.debug("Cannot iterate over player_ids", room_id=getattr(room, "id", None), error=str(e))
        return []
    return players


async def _find_matching_players(target_lower: str, room: Any, persistence: Any) -> list[Any]:
    """Find players in room matching the target name."""
    players_in_room = await _get_players_in_room(room, persistence)
    matching_players = []
    for p in players_in_room:
        if hasattr(p, "name") and target_lower in p.name.lower():
            matching_players.append(p)
    return matching_players


def _select_target_player(
    matching_players: list[Any],
    target: str,
    instance_number: int | None,
    player_name: str,
) -> tuple[Any, dict[str, str] | None]:
    """
    Select target player from matching players, handling instance numbers and multiple matches.

    Returns:
        tuple: (target_player, error_result) - error_result is None if selection succeeded
    """
    if not matching_players:
        return (None, {"result": f"You don't see anyone named '{target}' here."})

    if instance_number is not None:
        if instance_number < 1 or instance_number > len(matching_players):
            return (None, {"result": f"There aren't that many '{target}' here."})
        return (matching_players[instance_number - 1], None)

    if len(matching_players) == 1:
        return (matching_players[0], None)

    player_names = [p.name for p in matching_players if hasattr(p, "name")]
    logger.debug("Multiple players match target", player=player_name, target=target, matches=player_names)
    return (None, {"result": f"You see multiple players matching '{target}': {', '.join(player_names)}"})


def _format_player_look_display(target_player: Any) -> str:
    """Format the display text for looking at a player."""
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    stats = target_player.get_stats() if hasattr(target_player, "get_stats") else {}
    position = stats.get("position", "standing") if stats else "standing"

    health_label = _get_health_label(stats)
    lucidity_label = _get_lucidity_label(stats)
    visible_equipment = _get_visible_equipment(target_player)

    lines = [player_name_display]
    if visible_equipment:
        equipment_parts = []
        for slot, item in visible_equipment.items():
            item_name = item.get("item_name", "Unknown") if isinstance(item, dict) else str(item)
            equipment_parts.append(f"{slot}: {item_name}")
        if equipment_parts:
            lines.append(f"Visible Equipment: {', '.join(equipment_parts)}")

    lines.append(f"Position: {position}")
    lines.append(f"Health: {health_label}")
    lines.append(f"lucidity: {lucidity_label}")

    return "\n".join(lines)


async def _handle_player_look(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Handle looking at a specific player."""
    logger.debug(
        "Looking at player", player=player_name, target=target, room_id=room.id if hasattr(room, "id") else None
    )

    matching_players = await _find_matching_players(target_lower, room, persistence)
    target_player, error_result = _select_target_player(matching_players, target, instance_number, player_name)

    if error_result:
        if not matching_players:
            logger.debug("No players match target", player=player_name, target=target)
        return error_result

    result_text = _format_player_look_display(target_player)
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    logger.debug("Player look completed", player=player_name, target=target, target_player=player_name_display)
    return {"result": result_text}


async def _try_lookup_player_implicit(
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
) -> dict[str, Any] | None:
    """Try to find and display a player in implicit lookup."""
    matching_players = await _find_matching_players(target_lower, room, persistence)
    if not matching_players:
        return None

    target_player, error_result = _select_target_player(matching_players, target, instance_number, player_name)
    if error_result:
        return error_result

    result_text = _format_player_look_display(target_player)
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    logger.debug("Player look completed", player=player_name, target=target, target_player=player_name_display)
    return {"result": result_text}


__all__ = [
    "_get_players_in_room",
    "_find_matching_players",
    "_select_target_player",
    "_format_player_look_display",
    "_handle_player_look",
    "_try_lookup_player_implicit",
]
