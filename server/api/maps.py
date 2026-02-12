"""
Map API endpoints for MythosMUD server.

This module handles ASCII map rendering and coordinate management endpoints.
"""

# pylint: disable=too-many-lines  # Reason: Map API requires extensive endpoint handlers for coordinate management, map rendering, and room visualization

import uuid
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Depends, Query, Request
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.users import get_current_user
from ..database import get_async_session
from ..dependencies import AsyncPersistenceDep, ExplorationServiceDep, RoomServiceDep
from ..exceptions import DatabaseError, LoggedHTTPException
from ..game.room_service import RoomService
from ..models.user import User
from ..schemas.maps import (
    AsciiMapResponse,
    AsciiMinimapResponse,
    CoordinateRecalculationResponse,
    MapOriginSetResponse,
)
from ..services.admin_auth_service import AdminAction, get_admin_auth_service
from ..services.ascii_map_renderer import AsciiMapRenderer
from ..services.coordinate_generator import CoordinateGenerator
from ..services.coordinate_validator import CoordinateValidator
from ..services.exploration_service import ExplorationService
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)

# Create map router
map_router = APIRouter(prefix="/maps", tags=["maps"])

logger.info("Maps API router initialized", prefix="/maps")


async def _get_current_room_id(
    request: Request, current_user: User | None, persistence: "AsyncPersistenceLayer"
) -> str | None:
    """Get current room ID from query params or database. Returns room ID or None."""
    current_room_id = request.query_params.get("current_room_id")
    if not current_room_id and current_user:
        try:
            user_id = str(current_user.id)
            player = await persistence.get_player_by_user_id(user_id)
            if player:
                current_room_id = player.current_room_id
        except (DatabaseError, SQLAlchemyError) as e:
            logger.warning("Error getting player room for map", error=str(e))
    return current_room_id


async def _get_player_and_exploration_service(
    current_user: User | None, persistence: "AsyncPersistenceLayer", exploration_service: ExplorationService
) -> tuple[Any, uuid.UUID | None, ExplorationService | None]:
    """Get player, player_id, and exploration service. Returns (player, player_id, exploration_service)."""
    if current_user and not (current_user.is_admin or current_user.is_superuser):
        user_id = str(current_user.id)
        player = await persistence.get_player_by_user_id(user_id)
        if player:
            player_id = uuid.UUID(str(player.player_id))
            return player, player_id, exploration_service
    return None, None, None


async def _filter_explored_rooms(
    rooms: list[dict[str, Any]],
    player_id: uuid.UUID,
    exploration_service: ExplorationService,
    session: AsyncSession,
    room_service: RoomService,
) -> list[dict[str, Any]]:
    """
    Filter rooms to only include explored ones using RoomService.

    This is a thin wrapper around RoomService.filter_rooms_by_exploration()
    to maintain backward compatibility with existing code.
    """
    return await room_service.filter_rooms_by_exploration(rooms, player_id, exploration_service, session)


def _needs_coordinate_generation(rooms: list[dict[str, Any]]) -> bool:
    """
    Check if rooms need coordinate generation.

    Args:
        rooms: List of room dictionaries

    Returns:
        True if coordinates need to be generated, False otherwise
    """
    return not rooms or any(r.get("map_x") is None or r.get("map_y") is None for r in rooms)


async def _apply_exploration_filter_if_needed(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exploration filtering requires multiple dependencies (user, player, services, session) for proper validation and filtering
    rooms: list[dict[str, Any]],
    current_user: User | None,
    player: Any,
    player_id: uuid.UUID | None,
    exploration_service: ExplorationService,
    session: AsyncSession,
    room_service: RoomService,
) -> list[dict[str, Any]]:
    """
    Apply exploration filter to rooms if user is not admin/superuser.

    Args:
        rooms: List of room dictionaries
        current_user: Current user object
        player: Player object
        player_id: Player UUID
        exploration_service: Exploration service instance
        session: Database session
        room_service: Room service instance

    Returns:
        Filtered list of rooms
    """
    if current_user and not (current_user.is_admin or current_user.is_superuser):
        if player and exploration_service and player_id:
            rooms = await _filter_explored_rooms(rooms, player_id, exploration_service, session, room_service)
    return rooms


async def _ensure_coordinates_generated(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Coordinate generation requires many parameters for plane/zone/subzone context
    session: AsyncSession,
    plane: str,
    zone: str,
    sub_zone: str | None,
    rooms: list[dict[str, Any]],
    player: Any,
    player_id: uuid.UUID | None,
    exploration_service: ExplorationService,
    current_user: User | None,
    room_service: RoomService,
) -> list[dict[str, Any]]:
    """
    Generate coordinates if missing and reload rooms.

    Returns updated rooms list with coordinates and exploration filtering applied.

    Args:
        session: Database session
        plane: Plane name
        zone: Zone name
        sub_zone: Optional sub-zone name
        rooms: List of room dictionaries
        player: Player object
        player_id: Player UUID
        exploration_service: Exploration service instance
        current_user: Current user object
        room_service: Room service instance

    Returns:
        Updated list of room dictionaries with coordinates
    """
    if _needs_coordinate_generation(rooms):
        logger.debug("Generating missing coordinates", room_count=len(rooms))
        generator = CoordinateGenerator(session)
        await generator.generate_coordinates_for_zone(plane, zone, sub_zone)
        rooms = await _load_rooms_with_coordinates(session, plane, zone, sub_zone)

    rooms = await _apply_exploration_filter_if_needed(
        rooms, current_user, player, player_id, exploration_service, session, room_service
    )

    return rooms


@map_router.get("/ascii", response_model=AsciiMapResponse)
async def get_ascii_map(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: API endpoint requires many query parameters and intermediate variables for map generation
    request: Request,
    plane: str = Query(..., description="Plane name"),
    zone: str = Query(..., description="Zone name"),
    sub_zone: str | None = Query(None, description="Sub-zone name"),
    viewport_x: int = Query(0, description="Viewport X offset"),
    viewport_y: int = Query(0, description="Viewport Y offset"),
    viewport_width: int = Query(80, description="Viewport width in characters"),
    viewport_height: int = Query(24, description="Viewport height in lines"),
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    persistence: "AsyncPersistenceLayer" = AsyncPersistenceDep,
    exploration_service: ExplorationService = ExplorationServiceDep,
    room_service: RoomService = RoomServiceDep,
) -> AsciiMapResponse:
    """
    Get ASCII map for a zone/subzone.

    Returns HTML string with ASCII map rendered. For authenticated players,
    only shows explored rooms. Admins see all rooms.
    """
    try:
        logger.debug(
            "ASCII map requested",
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            viewport_x=viewport_x,
            viewport_y=viewport_y,
        )

        current_room_id = await _get_current_room_id(request, current_user, persistence)

        rooms = await _load_rooms_with_coordinates(session, plane, zone, sub_zone)

        player, player_id, _ = await _get_player_and_exploration_service(current_user, persistence, exploration_service)

        if player and exploration_service and player_id:
            rooms = await _filter_explored_rooms(rooms, player_id, exploration_service, session, room_service)

        rooms = await _ensure_coordinates_generated(
            session, plane, zone, sub_zone, rooms, player, player_id, exploration_service, current_user, room_service
        )

        renderer = AsciiMapRenderer()
        html_map = renderer.render_map(
            rooms=rooms,
            current_room_id=current_room_id,
            viewport_width=viewport_width,
            viewport_height=viewport_height,
            viewport_x=viewport_x,
            viewport_y=viewport_y,
        )

        return AsciiMapResponse(
            map_html=html_map,
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            viewport={
                "x": viewport_x,
                "y": viewport_y,
                "width": viewport_width,
                "height": viewport_height,
            },
        )

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Map generation errors unpredictable, must handle gracefully
        logger.error(
            "Error generating ASCII map",
            error=str(e),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            exc_info=True,
        )
        context = create_context_from_request(request)
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to generate ASCII map",
            context=context,
        ) from e


@map_router.get("/ascii/minimap", response_model=AsciiMinimapResponse)
async def get_ascii_minimap(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: API endpoint requires many query parameters and intermediate variables for minimap generation
    request: Request,
    plane: str = Query(..., description="Plane name"),
    zone: str = Query(..., description="Zone name"),
    sub_zone: str | None = Query(None, description="Sub-zone name"),
    size: int = Query(5, description="Minimap size in characters (e.g., 5 means 5x5 grid)"),
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    persistence: "AsyncPersistenceLayer" = AsyncPersistenceDep,
    exploration_service: ExplorationService = ExplorationServiceDep,
    room_service: RoomService = RoomServiceDep,
) -> AsciiMinimapResponse:
    """
    Get ASCII minimap centered on player.

    Returns a small ASCII map showing area around the player's current room.
    """
    try:
        if not current_user:
            context = create_context_from_request(request)
            raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)

        # Get player object (needed for exploration filtering)
        user_id = str(current_user.id)
        player = await persistence.get_player_by_user_id(user_id)
        if not player:
            context = create_context_from_request(request)
            raise LoggedHTTPException(status_code=404, detail="Player not found", context=context)

        # Get current room ID - prefer client-provided value, fallback to database
        current_room_id = request.query_params.get("current_room_id") or player.current_room_id

        # Load rooms with coordinates
        rooms = await _load_rooms_with_coordinates(session, plane, zone, sub_zone)

        # Filter to explored rooms if not admin
        if not (current_user.is_admin or current_user.is_superuser):
            player_id = uuid.UUID(str(player.player_id))
            rooms = await room_service.filter_rooms_by_exploration(rooms, player_id, exploration_service, session)

            logger.debug(
                "Filtered rooms by exploration for minimap",
                filtered_count=len(rooms),
            )
        else:
            # Player has explored no rooms - return empty list
            rooms = []
            logger.debug("Player has explored no rooms for minimap, returning empty list")

        # Render minimap (always centers on player)
        # Size parameter directly controls dimensions (e.g., size=5 means 5x5 grid)
        renderer = AsciiMapRenderer()
        html_map = renderer.render_map(
            rooms=rooms,
            current_room_id=current_room_id,
            viewport_width=size,
            viewport_height=size,
            viewport_x=0,  # Will be auto-centered
            viewport_y=0,  # Will be auto-centered
        )

        return AsciiMinimapResponse(
            map_html=html_map,
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            size=size,
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Minimap generation errors unpredictable, must handle gracefully
        logger.error(
            "Error generating ASCII minimap",
            error=str(e),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            exc_info=True,
        )
        context = create_context_from_request(request)
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to generate ASCII minimap",
            context=context,
        ) from e


def _build_zone_pattern(plane: str, zone: str, sub_zone: str | None) -> str:
    """
    Build zone pattern for room query.

    Args:
        plane: Plane name
        zone: Zone name
        sub_zone: Optional sub-zone name

    Returns:
        Zone pattern string for SQL LIKE query
    """
    zone_pattern = f"{plane}_{zone}"
    if sub_zone:
        zone_pattern = f"{zone_pattern}_{sub_zone}"
    return zone_pattern


def _build_room_dict(row: Any) -> dict[str, Any]:
    """
    Build room dictionary from database row.

    Args:
        row: Database row result

    Returns:
        Room dictionary with all room properties
    """
    attrs = row[3] if row[3] else {}
    return {
        "id": row[1],  # Use stable_id as id
        "uuid": str(row[0]),
        "stable_id": row[1],
        "name": row[2],
        "attributes": attrs,
        "map_x": float(row[4]) if row[4] is not None else None,
        "map_y": float(row[5]) if row[5] is not None else None,
        "map_origin_zone": bool(row[6]) if row[6] is not None else False,
        "map_symbol": row[7],
        "map_style": row[8],
        "environment": attrs.get("environment", "outdoors"),
        "exits": {},
    }


async def _load_room_exits(session: AsyncSession, rooms: list[dict[str, Any]]) -> None:
    """
    Load exits for rooms and attach them to room dictionaries.

    Args:
        session: Database session
        rooms: List of room dictionaries to populate with exits
    """
    if not rooms:
        return

    stable_ids = [r["stable_id"] for r in rooms]
    exits_query = text("""
        SELECT r1.stable_id as from_stable_id, r2.stable_id as to_stable_id, rl.direction
        FROM room_links rl
        JOIN rooms r1 ON rl.from_room_id = r1.id
        JOIN rooms r2 ON rl.to_room_id = r2.id
        WHERE r1.stable_id = ANY(:stable_ids)
    """)
    exits_result = await session.execute(exits_query, {"stable_ids": stable_ids})

    exits_by_room: dict[str, dict[str, str]] = {}
    for row in exits_result:
        from_stable = row[0]
        to_stable = row[1]
        direction = row[2]
        if from_stable not in exits_by_room:
            exits_by_room[from_stable] = {}
        exits_by_room[from_stable][direction] = to_stable

    for room in rooms:
        room["exits"] = exits_by_room.get(room["stable_id"], {})


async def _load_rooms_with_coordinates(
    session: AsyncSession, plane: str, zone: str, sub_zone: str | None
) -> list[dict[str, Any]]:
    """
    Load rooms with their coordinates and exits.

    Args:
        session: Database session
        plane: Plane name
        zone: Zone name
        sub_zone: Optional sub-zone name

    Returns:
        List of room dictionaries with coordinates and exits
    """
    zone_pattern = _build_zone_pattern(plane, zone, sub_zone)

    query = text("""
        SELECT
            r.id,
            r.stable_id,
            r.name,
            r.attributes,
            r.map_x,
            r.map_y,
            r.map_origin_zone,
            r.map_symbol,
            r.map_style
        FROM rooms r
        JOIN subzones sz ON r.subzone_id = sz.id
        JOIN zones z ON sz.zone_id = z.id
        WHERE r.stable_id LIKE :pattern || '%'
    """)

    result = await session.execute(query, {"pattern": zone_pattern})
    rooms = [_build_room_dict(row) for row in result]

    await _load_room_exits(session, rooms)

    return rooms


@map_router.post("/coordinates/recalculate", response_model=CoordinateRecalculationResponse)
async def recalculate_coordinates(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: API endpoint requires many query parameters for coordinate recalculation
    request: Request,
    plane: str = Query(..., description="Plane name"),
    zone: str = Query(..., description="Zone name"),
    sub_zone: str | None = Query(None, description="Sub-zone name"),
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> CoordinateRecalculationResponse:
    """
    Trigger coordinate recalculation for a zone/subzone (admin only).

    Returns list of conflicts if any.
    """
    try:
        # Validate admin permissions
        if not current_user:
            context = create_context_from_request(request)
            raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)

        auth_service = get_admin_auth_service()
        auth_service.validate_permission(current_user, AdminAction.UPDATE_ROOM_POSITION, request)

        logger.info(
            "Coordinate recalculation requested",
            user=auth_service.get_username(current_user),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
        )

        # Generate coordinates
        generator = CoordinateGenerator(session)
        result = await generator.generate_coordinates_for_zone(plane, zone, sub_zone)

        # Validate for conflicts
        validator = CoordinateValidator(session)
        validation_result = await validator.validate_coordinates(plane, zone, sub_zone)

        return CoordinateRecalculationResponse(
            message="Coordinates recalculated",
            coordinates_generated=len(result["coordinates"]),
            conflicts=validation_result["conflicts"],
            conflict_count=validation_result["conflict_count"],
            valid=validation_result["valid"],
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Coordinate recalculation errors unpredictable, must handle gracefully
        logger.error(
            "Error recalculating coordinates",
            error=str(e),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            exc_info=True,
        )
        context = create_context_from_request(request)
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to recalculate coordinates",
            context=context,
        ) from e


class SetOriginRequest(BaseModel):
    """Request model for setting map origin."""

    plane: str = Field(..., description="Plane name")
    zone: str = Field(..., description="Zone name")
    sub_zone: str | None = Field(None, description="Sub-zone name")


@map_router.post("/rooms/{room_id}/origin", response_model=MapOriginSetResponse)
async def set_map_origin(  # pylint: disable=too-many-locals  # Reason: Map origin setting requires many intermediate variables for validation and processing
    room_id: str,
    origin_data: SetOriginRequest,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
) -> MapOriginSetResponse:
    """
    Set a room as the map origin for its zone/subzone (admin only).

    Triggers coordinate recalculation.
    """
    try:
        # Validate admin permissions
        if not current_user:
            context = create_context_from_request(request)
            context.metadata["requested_room_id"] = room_id
            raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)

        auth_service = get_admin_auth_service()
        auth_service.validate_permission(current_user, AdminAction.UPDATE_ROOM_POSITION, request)

        logger.info(
            "Map origin set requested",
            user=auth_service.get_username(current_user),
            room_id=room_id,
            plane=origin_data.plane,
            zone=origin_data.zone,
            sub_zone=origin_data.sub_zone,
        )

        # Clear existing origin for this zone/subzone
        zone_pattern = f"{origin_data.plane}_{origin_data.zone}"
        if origin_data.sub_zone:
            zone_pattern = f"{zone_pattern}_{origin_data.sub_zone}"

        clear_query = text("""
            UPDATE rooms
            SET map_origin_zone = FALSE
            WHERE stable_id LIKE :pattern || '%'
            AND map_origin_zone = TRUE
        """)
        await session.execute(clear_query, {"pattern": zone_pattern})

        # Set new origin
        set_query = text("""
            UPDATE rooms
            SET map_origin_zone = TRUE
            WHERE stable_id = :room_id
        """)
        update_result = await session.execute(set_query, {"room_id": room_id})
        await session.commit()

        # SQLAlchemy Result objects have rowcount attribute at runtime, but mypy stubs don't reflect this
        if not update_result.rowcount:  # type: ignore[attr-defined]  # Reason: SQLAlchemy Result objects have rowcount attribute at runtime, but mypy stubs don't reflect this
            context = create_context_from_request(request)
            context.metadata["requested_room_id"] = room_id
            raise LoggedHTTPException(status_code=404, detail="Room not found", context=context)

        # Trigger coordinate recalculation
        generator = CoordinateGenerator(session)
        coordinate_result = await generator.generate_coordinates_for_zone(
            origin_data.plane, origin_data.zone, origin_data.sub_zone
        )

        # Validate for conflicts
        validator = CoordinateValidator(session)
        validation_result = await validator.validate_coordinates(
            origin_data.plane, origin_data.zone, origin_data.sub_zone
        )

        logger.info(
            "Map origin set successfully",
            room_id=room_id,
            coordinates_generated=len(coordinate_result["coordinates"]),
            conflicts=validation_result["conflict_count"],
        )

        return MapOriginSetResponse(
            room_id=room_id,
            message="Map origin set and coordinates recalculated",
            coordinates_generated=len(coordinate_result["coordinates"]),
            conflicts=validation_result["conflicts"],
            conflict_count=validation_result["conflict_count"],
            valid=validation_result["valid"],
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Map operation errors unpredictable, must rollback and handle
        await session.rollback()
        logger.error(
            "Error setting map origin",
            error=str(e),
            room_id=room_id,
            exc_info=True,
        )
        context = create_context_from_request(request)
        context.metadata["requested_room_id"] = room_id
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to set map origin",
            context=context,
        ) from e
