"""
Minimap orchestration for the map API.

Extracted from maps.py so the router stays focused on HTTP and delegation.
This module loads rooms, applies exploration filtering, ensures the current
room is included, applies fallback coordinates, and renders the minimap HTML.
"""

import uuid
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from ..game.room_service import RoomService
from ..services.ascii_map_renderer import AsciiMapRenderer
from ..services.exploration_service import ExplorationService
from ..structured_logging.enhanced_logging_config import get_logger
from .map_helpers import load_rooms_with_coordinates, load_single_room_with_coordinates

logger = get_logger(__name__)


async def _resolve_current_room_for_minimap(
    rooms_before_filter: list[dict[str, Any]],
    current_room_id: str,
    session: AsyncSession,
) -> dict[str, Any] | None:
    """
    Get current room from pre-filter list or load by stable_id. Returns None if not found.
    """
    current_room = next(
        (r for r in rooms_before_filter if (r.get("id") or r.get("stable_id")) == current_room_id),
        None,
    )
    if not current_room:
        current_room = await load_single_room_with_coordinates(session, current_room_id)
    return current_room


def _append_room_with_fallback_coords_if_needed(rooms: list[dict[str, Any]], room: dict[str, Any]) -> None:
    """
    Append room to list; use fallback map_x/map_y=0 if room has None coords. Mutates rooms in place.
    """
    had_coords = room.get("map_x") is not None and room.get("map_y") is not None
    if not had_coords:
        room_to_append = dict(room)
        room_to_append["map_x"] = 0.0
        room_to_append["map_y"] = 0.0
        rooms.append(room_to_append)
    else:
        rooms.append(room)


async def _ensure_current_room_in_minimap_rooms(
    rooms: list[dict[str, Any]],
    rooms_before_filter: list[dict[str, Any]],
    current_room_id: str | None,
    session: AsyncSession,
) -> None:
    """
    If current_room_id is missing from rooms, re-add it from rooms_before_filter or load it.
    Mutates rooms in place. Used so minimap can center on player after zone change.
    """
    if not current_room_id:
        return
    if current_room_id in {r.get("id") for r in rooms}:
        return
    current_room = await _resolve_current_room_for_minimap(rooms_before_filter, current_room_id, session)
    if current_room:
        _append_room_with_fallback_coords_if_needed(rooms, current_room)


def _apply_minimap_fallback_coordinates(
    rooms: list[dict[str, Any]],
    current_room_id: str | None,
    is_admin: bool,
    fallback_grid_width: int = 20,
) -> None:
    """
    Set fallback map_x/map_y for rooms that have None. Admins get a grid layout;
    non-admins only get fallback for the current room. Mutates rooms in place.
    """
    for i, room in enumerate(rooms):
        need_fallback = room.get("map_x") is None or room.get("map_y") is None
        if not need_fallback:
            continue
        if is_admin:
            room["map_x"] = float(i % fallback_grid_width)
            room["map_y"] = float(i // fallback_grid_width)
        elif current_room_id and (room.get("id") or room.get("stable_id")) == current_room_id:
            room["map_x"] = 0.0
            room["map_y"] = 0.0
            break


async def generate_minimap_html(
    session: AsyncSession,
    plane: str,
    zone: str,
    sub_zone: str | None,
    size: int,
    current_room_id: str | None,
    is_admin: bool,
    player_id: uuid.UUID | None,
    exploration_service: ExplorationService,
    room_service: RoomService,
) -> str:
    """
    Load rooms for the zone, apply exploration filter, ensure current room is included,
    apply fallback coordinates, and render minimap HTML.

    Args:
        session: Database session
        plane: Plane name
        zone: Zone name
        sub_zone: Optional sub-zone name
        size: Minimap grid size (e.g. 5 for 5x5)
        current_room_id: Player's current room ID (for centering and fallback)
        is_admin: Whether the user is admin/superuser (sees all rooms)
        player_id: Player UUID for exploration filter (None if admin)
        exploration_service: Exploration service instance
        room_service: Room service instance

    Returns:
        Rendered minimap HTML string
    """
    rooms = await load_rooms_with_coordinates(session, plane, zone, sub_zone)
    rooms_before_filter = list(rooms)

    if not is_admin and player_id is not None:
        rooms = await room_service.filter_rooms_by_exploration(rooms, player_id, exploration_service, session)
        logger.debug(
            "Filtered rooms by exploration for minimap",
            filtered_count=len(rooms),
        )
        await _ensure_current_room_in_minimap_rooms(rooms, rooms_before_filter, current_room_id, session)

    _apply_minimap_fallback_coordinates(rooms, current_room_id, is_admin)

    renderer = AsciiMapRenderer()
    return renderer.render_map(
        rooms=rooms,
        current_room_id=current_room_id,
        viewport_width=size,
        viewport_height=size,
        viewport_x=0,
        viewport_y=0,
    )
