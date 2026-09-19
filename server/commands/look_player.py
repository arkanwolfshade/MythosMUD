"""
Player look functionality for MythosMUD.

This module handles looking at players, including finding matching players,
formatting player display, and handling player look requests.
"""

# pylint: disable=too-many-arguments  # Reason: Player look requires many parameters for context and target resolution

import uuid
from typing import Any

from ..realtime.disconnect_grace_period import is_player_in_grace_period
from ..realtime.login_grace_period import is_player_in_login_grace_period
from ..structured_logging.enhanced_logging_config import get_logger
from .look_helpers import (
    _get_corruption_label,
    _get_corruption_prose,
    _get_health_label,
    _get_lucidity_label,
    _get_visible_equipment,
)

logger = get_logger(__name__)


# Reason: DYNAMIC_DISPATCH - room/player_ids are duck-typed (hasattr-checked, Mock-like-in-tests)
# values; matches _get_players_in_room's own established, unsuppressed Any signature below.
# Appropriate because: this module intentionally accepts loosely-shaped room/persistence objects
# rather than a strict Protocol, since callers (including tests) pass partial/mock implementations.
def _normalize_room_player_ids(
    room: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - same duck-typed convention as room above.
    # Appropriate because: same unsuppressed convention as this function's own room parameter.
    player_ids: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - same duck-typed convention as the parameters above.
    # Appropriate because: same unsuppressed convention as this function's own parameters.
) -> list[Any] | None:  # pyright: ignore[reportExplicitAny]
    """Coerce room.get_players()'s result to a list; return None if it isn't iterable."""
    if isinstance(player_ids, list | tuple):
        return list(player_ids)  # pyright: ignore[reportUnknownArgumentType]
    # Mock objects can be iterable but might not behave as expected; validate by converting.
    try:
        # Reason: DYNAMIC_DISPATCH - player_ids is Any per this function's own parameter above.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        return list(player_ids) if player_ids is not None else []  # pyright: ignore[reportAny]
    except (TypeError, ValueError) as e:
        logger.debug(
            "room.get_players() returned non-iterable value",
            # Reason: DYNAMIC_DISPATCH - room is Any per this function's own parameter above.
            # Appropriate because: same unsuppressed convention as this function's own signature.
            room_id=getattr(room, "id", None),  # pyright: ignore[reportAny]
            error=str(e),
        )
        return None


# Reason: DYNAMIC_DISPATCH - persistence/player_id_str are duck-typed values; player_id_str comes
# from the room's own duck-typed player-id list.
# Appropriate because: same unsuppressed convention as _get_players_in_room below.
async def _resolve_room_player(
    persistence: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - same duck-typed convention as persistence above.
    # Appropriate because: same unsuppressed convention as this function's own persistence parameter.
    player_id_str: Any,  # pyright: ignore[reportAny, reportExplicitAny]
    # Reason: DYNAMIC_DISPATCH - same duck-typed convention as the parameters above.
    # Appropriate because: same unsuppressed convention as this function's own parameters.
) -> Any | None:  # pyright: ignore[reportExplicitAny]
    """Resolve one room-membership entry to a Player object, or None if unresolvable."""
    try:
        player_id = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
        # Reason: DYNAMIC_DISPATCH - persistence is Any per this function's own parameter above.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        if not hasattr(persistence, "get_player_by_id"):  # pyright: ignore[reportAny]
            return None
        # Reason: DYNAMIC_DISPATCH - persistence is Any per this function's own parameter above.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        return await persistence.get_player_by_id(player_id)  # pyright: ignore[reportAny]
    except (ValueError, AttributeError):
        logger.debug("Failed to get player", player_id=player_id_str, error="Invalid UUID or missing method")
        return None


async def _get_players_in_room(room: Any, persistence: Any) -> list[Any]:
    """
    Get all Player objects currently in the room.

    Args:
        room: Room object with get_players() method
        persistence: AsyncPersistenceLayer object with get_player_by_id() method

    Returns:
        List of Player objects in the room (None players filtered out)
    """
    # Reason: DYNAMIC_DISPATCH - room is a duck-typed object; get_players() is only called after
    # a hasattr check.
    # Appropriate because: same unsuppressed convention as this function's own signature above.
    raw_player_ids = room.get_players() if hasattr(room, "get_players") else []  # pyright: ignore[reportAny, reportUnknownVariableType]
    player_ids = _normalize_room_player_ids(room, raw_player_ids)
    if player_ids is None:
        return []

    players = []
    try:
        # Reason: DYNAMIC_DISPATCH - player_ids items are Any from the duck-typed room object.
        # Appropriate because: same unsuppressed convention as _normalize_room_player_ids above.
        for player_id_str in player_ids:  # pyright: ignore[reportAny]
            player = await _resolve_room_player(persistence, player_id_str)
            if player:
                # Reason: DYNAMIC_DISPATCH - player is Any per _resolve_room_player's own return type.
                # Appropriate because: same unsuppressed convention as this function's own signature.
                players.append(player)  # pyright: ignore[reportUnknownMemberType, reportAny]
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


def _player_id_uuid(target_player: Any) -> uuid.UUID | None:
    if not hasattr(target_player, "player_id"):
        return None
    try:
        player_id = target_player.player_id
        return uuid.UUID(player_id) if isinstance(player_id, str) else player_id
    except (ValueError, AttributeError, TypeError):
        return None


def _apply_grace_period_labels(player_name_display: str, target_player: Any, connection_manager: Any | None) -> str:
    if not connection_manager:
        return player_name_display

    player_id = _player_id_uuid(target_player)
    if player_id is None:
        return player_name_display

    try:
        if is_player_in_grace_period(player_id, connection_manager):
            player_name_display = f"{player_name_display} (linkdead)"
        if is_player_in_login_grace_period(player_id, connection_manager):
            player_name_display = f"{player_name_display} (warded)"
    except (ValueError, AttributeError, ImportError, TypeError):
        pass
    return player_name_display


def _format_player_look_display(target_player: Any, connection_manager: Any | None = None) -> str:
    """
    Format the display text for looking at a player.
    Adds "(linkdead)" indicator if player is in grace period.

    Args:
        target_player: The player object to format
        connection_manager: ConnectionManager instance for checking grace period

    Returns:
        Formatted display text
    """
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    player_name_display = _apply_grace_period_labels(player_name_display, target_player, connection_manager)

    stats = target_player.get_stats() if hasattr(target_player, "get_stats") else {}
    position = stats.get("position", "standing") if stats else "standing"

    health_label = _get_health_label(stats)
    lucidity_label = _get_lucidity_label(stats)
    corruption_label = _get_corruption_label(stats)  # pyright: ignore[reportUnknownArgumentType] -- stats is Any here, same as the health/lucidity calls above (target_player: Any)
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
    lines.append(f"Corruption: {corruption_label}")

    # #815: atmosphere for a marked-or-worse tier -- the permanent `touched` scar (label alone,
    # no prose) stays undramatic and private to close examination.
    corruption_prose = _get_corruption_prose(stats)  # pyright: ignore[reportUnknownArgumentType] -- same Any-from-target_player shape as above
    if corruption_prose:
        lines.append("")
        lines.append(corruption_prose)

    return "\n".join(lines)


async def _handle_player_look(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Player look requires many parameters for context and target resolution
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
    connection_manager: Any | None = None,
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

    result_text = _format_player_look_display(target_player, connection_manager)
    player_name_display = target_player.name if hasattr(target_player, "name") else "Unknown"
    logger.debug("Player look completed", player=player_name, target=target, target_player=player_name_display)
    return {"result": result_text}


async def _try_lookup_player_implicit(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Player look requires many parameters for context and target resolution
    target: str,
    target_lower: str,
    instance_number: int | None,
    room: Any,
    persistence: Any,
    player_name: str,
    connection_manager: Any | None = None,
) -> dict[str, Any] | None:
    """Try to find and display a player in implicit lookup."""
    matching_players = await _find_matching_players(target_lower, room, persistence)
    if not matching_players:
        return None

    target_player, error_result = _select_target_player(matching_players, target, instance_number, player_name)
    if error_result:
        return error_result

    result_text = _format_player_look_display(target_player, connection_manager)
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
