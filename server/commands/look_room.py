"""
Room look functionality for MythosMUD.

This module handles looking at rooms, including formatting room descriptions,
listing items, NPCs, players, and exits in the room.
"""

from collections.abc import Mapping, Sequence
from typing import Any, cast

from ..constants.message_category import MessageCategory
from ..constants.message_segments import (
    MessageSegment,
    SegmentPart,
    join_parts,
    message_with_segments,
    npc_name_segment,
)
from ..realtime.occupant_display import format_occupant_display_name
from ..services.exit_hallucination import get_hallucinated_exits
from ..services.lucidity_tier_cache import lucidity_tier_cache
from ..services.phantom_visibility import get_viewer_phantom_occupants
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.room_renderer import format_room_drop_lines
from .look_npc import _get_npc_occupants_in_room
from .look_player import _get_players_in_room

logger = get_logger(__name__)


def _format_items_section(room_drops: list[dict[str, Any]]) -> list[str]:
    """Format the items section of room look."""
    drop_lines = format_room_drop_lines(room_drops)
    if not drop_lines:
        return []
    return [str(line) for line in drop_lines] + [""]


def _container_metadata(container: Mapping[str, object]) -> Mapping[str, object]:
    """A container record's metadata: persistence rows carry metadata_json, room summaries metadata (#917)."""
    raw = container.get("metadata_json") or container.get("metadata")
    return cast("Mapping[str, object]", raw) if isinstance(raw, Mapping) else {}


def _classify_containers_and_corpses(containers_data: Sequence[Mapping[str, object]]) -> tuple[list[str], list[str]]:
    """Split room container records into (environment container names, corpse descriptions)."""
    containers: list[str] = []
    corpses: list[str] = []
    for container in containers_data:
        source_type = container.get("source_type", "")
        metadata = _container_metadata(container)
        if source_type == "corpse":
            corpses.append(f"the corpse of {metadata.get('player_name', 'Unknown')}")
        elif source_type == "environment":
            containers.append(str(metadata.get("name", "Unknown Container")))
    return containers, corpses


# Reason: SERIALIZATION_BOUNDARY - persistence is Any per this module's established convention.
# Appropriate because: the persistence layer is duck-typed here and this module has no shared protocol for it.
async def _format_containers_section(room_id: str | None, persistence: Any) -> list[str]:  # pyright: ignore[reportAny, reportExplicitAny]
    """Format the containers/corpses section of room look."""
    if not room_id or not persistence:
        return []
    try:
        # Reason: SERIALIZATION_BOUNDARY - persistence is Any per this function's own parameter.
        # Appropriate because: same unsuppressed convention as this function's own signature.
        containers_data: Sequence[Mapping[str, object]] = await persistence.get_containers_by_room_id(room_id)  # pyright: ignore[reportAny]
    except (AttributeError, TypeError) as exc:  # pragma: no cover - defensive logging path
        logger.debug("Failed to get containers by room id", room_id=room_id, error=str(exc))
        return []
    if not containers_data:
        return []

    containers, corpses = _classify_containers_and_corpses(containers_data)
    lines = []
    if containers:
        container_list = ", ".join(containers)
        lines.append(f"You see: {container_list}")
    if corpses:
        lines.extend(corpses)
    if lines:
        lines.append("")
    return lines


async def _npc_section_parts(room_id: str | None, viewer_player_id: str | None = None) -> list[SegmentPart]:
    """
    The "Also here: ..." line as parts, each NPC name styled by its disposition (#1036).

    Includes the viewer's own phantoms, tagged exactly like a real hostile (ADR-024). Empty when nobody is here.
    """
    if not room_id:
        return []
    npcs = [*await _get_npc_occupants_in_room(room_id), *get_viewer_phantom_occupants(viewer_player_id, room_id)]
    if not npcs:
        return []
    parts: list[SegmentPart] = ["Also here: "]
    for index, npc in enumerate(npcs):
        if index:
            parts.append(", ")
        parts.append(npc_name_segment(npc["name"], npc["disposition"]))
    return parts


def _npc_section_lines(parts: list[SegmentPart]) -> list[str]:
    """The plain-text lines of the NPC section (the "Also here" line and a spacer), or none."""
    return [join_parts(parts), ""] if parts else []


async def _format_npcs_section(room_id: str | None, viewer_player_id: Any | None = None) -> list[str]:
    """Format the NPCs/Mobs section of room look, including the viewer's own phantoms."""
    viewer = str(cast("object", viewer_player_id)) if viewer_player_id is not None else None
    return _npc_section_lines(await _npc_section_parts(room_id, viewer))


def _joined_with_newlines(entries: list[list[SegmentPart]]) -> list[SegmentPart]:
    """The parts of ``"\n".join(...)`` over lines that are each a list of parts."""
    parts: list[SegmentPart] = []
    for index, entry in enumerate(entries):
        if index:
            parts.append("\n")
        parts.extend(entry)
    return parts


async def _try_lookup_phantom_implicit(target_lower: str, room: Any, player: Any) -> dict[str, Any] | None:
    """
    Look at one of the player's own active phantom hostiles in this room (#625).

    Generic description text -- phantoms don't need per-name flavor text across the 8-name pool.
    """
    player_id = getattr(player, "player_id", None)
    room_id = _get_room_id(room)
    if not player_id or not room_id:
        return None
    from ..services.phantom_hostile_service import phantom_hostile_service

    data = phantom_hostile_service.find_phantom_by_name_in_room(player_id, room_id, target_lower)
    if not data:
        return None
    return {"result": f"{data['name']}\nIts form wavers at the edges of perception, not quite real."}


async def _filter_other_players(
    players_in_room: list[Any], player_name: str, connection_manager: Any | None = None
) -> list[str]:
    """
    Filter out the current player from the list of players in room.
    Adds "(linkdead)" indicator for players in grace period.

    Args:
        players_in_room: List of player objects
        player_name: Current player's name (to filter out)
        connection_manager: ConnectionManager instance for checking grace period

    Returns:
        List of player names with "(linkdead)" indicator if applicable
    """
    player_names = []
    for p in players_in_room:
        if hasattr(p, "name") and p.name != player_name:
            player_id = getattr(p, "player_id", None)
            player_names.append(format_occupant_display_name(p.name, player_id, connection_manager))
    return player_names


def _format_players_section(player_names: list[str]) -> list[str]:
    """Format the players section of room look."""
    if not player_names:
        return []
    player_list = ", ".join(player_names)
    return [f"Also here: {player_list}", ""]


def _get_room_description(room: Any) -> str:
    """Get room description with fallback."""
    if room.description is not None:
        return str(room.description)
    return "You see nothing special."


def _get_room_id(room: Any) -> str | None:
    """Get room ID safely."""
    if hasattr(room, "id"):
        return cast(str | None, room.id)
    return None


def _format_exits_list(exits: dict[str, Any]) -> str:
    """Format exits list for room look."""
    valid_exits = [direction for direction, room_id in exits.items() if room_id is not None]
    if valid_exits:
        return ", ".join(valid_exits)
    return "none"


def _room_exit_list(exits: dict[str, object], room_id: str | None, viewer_id_str: str | None) -> str:
    """The rendered exit list; a deranged viewer gets the seeded hallucinated set (#626/#714)."""
    # #626/#714: a deranged viewer sees the same seeded, hallucinated exit set here as in the
    # room_update/game_state payloads -- server-authoritative, so /look can no longer contradict
    # the client's Location panel the way #626's client-side-only version did.
    if room_id and viewer_id_str and lucidity_tier_cache.is_deranged(viewer_id_str):
        return ", ".join(get_hallucinated_exits(room_id, viewer_id_str)) or "none"
    return _format_exits_list(exits)


def _room_look_segments(
    lines: list[str], npc_start: int, npc_end: int, npc_parts: list[SegmentPart], rendered: str
) -> dict[str, list[MessageSegment]]:
    """``{"segments": ...}`` for the room text with NPC names styled (#1036), or ``{}`` when there is nothing to style."""
    if not npc_parts:
        return {}
    head: list[list[SegmentPart]] = [[line] for line in lines[:npc_start]]
    tail: list[list[SegmentPart]] = [[line] for line in lines[npc_end:]]
    built = message_with_segments(_joined_with_newlines([*head, npc_parts, [""], *tail]))
    return {"segments": built["segments"]} if built["message"] == rendered else {}


async def _handle_room_look(
    room: Any,
    room_drops: list[dict[str, Any]],
    persistence: Any,
    player_name: str,
    request: Any | None = None,
    viewer_player_id: Any | None = None,
) -> dict[str, Any]:
    """Handle looking at the current room."""
    desc = _get_room_description(room)
    room_id = _get_room_id(room)
    # viewer_player_id comes in as Any (this module's caller-supplied values are untyped
    # throughout); narrow it once, here, rather than passing Any into is_deranged/
    # get_hallucinated_exits below.
    viewer_id_str = str(cast("object", viewer_player_id)) if viewer_player_id is not None else None
    exit_list = _room_exit_list(cast("dict[str, object]", room.exits), room_id, viewer_id_str)

    logger.debug(
        "Looked at current room",
        player=player_name,
        room_id=room_id,
        exits=[d for d, rid in room.exits.items() if rid is not None],
    )

    lines = [desc, ""]

    # 3. Items (room drops)
    lines.extend(_format_items_section(room_drops))

    # 4. Containers and corpses
    lines.extend(await _format_containers_section(room_id, persistence))

    # 5. NPCs/Mobs
    npc_parts = await _npc_section_parts(room_id, viewer_id_str)
    npc_start = len(lines)
    lines.extend(_npc_section_lines(npc_parts))
    npc_end = len(lines)

    # 6. Players
    players_in_room = await _get_players_in_room(room, persistence)
    # Get connection_manager for grace period check
    app = getattr(request, "app", None)
    connection_manager = getattr(app.state, "connection_manager", None) if app else None
    player_names = await _filter_other_players(players_in_room, player_name, connection_manager)
    lines.extend(_format_players_section(player_names))

    # 9. Exits
    lines.append(f"Exits: {exit_list}")
    rendered = "\n".join(lines)
    drop_lines = format_room_drop_lines(room_drops)
    return {
        "result": rendered,
        "category": MessageCategory.ROOM_DESCRIPTION,
        **_room_look_segments(lines, npc_start, npc_end, npc_parts, rendered),
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
            return {"result": f"{name}\n{desc}", "category": MessageCategory.ROOM_DESCRIPTION}
    logger.debug("No valid exit in direction", player=player_name, direction=direction)
    return {"result": "You see nothing special that way."}


__all__ = [
    "_format_items_section",
    "_format_containers_section",
    "_format_npcs_section",
    "_try_lookup_phantom_implicit",
    "_filter_other_players",
    "_format_players_section",
    "_get_room_description",
    "_get_room_id",
    "_format_exits_list",
    "_handle_room_look",
    "_handle_direction_look",
]
