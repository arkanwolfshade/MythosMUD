"""
Map API endpoints for MythosMUD server.

This module handles ASCII map rendering and coordinate management endpoints.
"""

# pylint: disable=too-many-lines  # Reason: Map API requires extensive endpoint handlers for coordinate management, map rendering, and room visualization

import uuid
from typing import TYPE_CHECKING, Any, NoReturn

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
from .map_helpers import MapZoneContext, load_rooms_with_coordinates
from .map_minimap import generate_minimap_html

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


async def _ensure_coordinates_generated(
    session: AsyncSession,
    zone_ctx: MapZoneContext,
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
        zone_ctx: Plane, zone, and sub_zone for the map area
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
        await generator.generate_coordinates_for_zone(zone_ctx.plane, zone_ctx.zone, zone_ctx.sub_zone)
        rooms = await load_rooms_with_coordinates(session, zone_ctx.plane, zone_ctx.zone, zone_ctx.sub_zone)

    rooms = await _apply_exploration_filter_if_needed(
        rooms, current_user, player, player_id, exploration_service, session, room_service
    )

    return rooms


async def _prepare_ascii_map_context(
    request: Request,
    zone_context: MapZoneContext,
    current_user: User | None,
    session: AsyncSession,
    persistence: "AsyncPersistenceLayer",
    exploration_service: ExplorationService,
    room_service: RoomService,
) -> tuple[list[dict[str, Any]], str | None]:
    """
    Prepare rooms and current_room_id for ASCII map rendering.
    """
    current_room_id = await _get_current_room_id(request, current_user, persistence)

    rooms = await load_rooms_with_coordinates(session, zone_context.plane, zone_context.zone, zone_context.sub_zone)

    player, player_id, _ = await _get_player_and_exploration_service(current_user, persistence, exploration_service)

    if player and exploration_service and player_id:
        rooms = await _filter_explored_rooms(rooms, player_id, exploration_service, session, room_service)

    rooms = await _ensure_coordinates_generated(
        session,
        zone_context,
        rooms,
        player,
        player_id,
        exploration_service,
        current_user,
        room_service,
    )

    return rooms, current_room_id


def _handle_ascii_map_error(e: Exception, plane: str, zone: str, sub_zone: str | None) -> NoReturn:
    """
    Log and wrap ASCII map errors in LoggedHTTPException. Always raises.
    """
    logger.error(
        "Error generating ASCII map",
        error=str(e),
        plane=plane,
        zone=zone,
        sub_zone=sub_zone,
        exc_info=True,
    )
    raise LoggedHTTPException(
        status_code=500,
        detail="Failed to generate ASCII map",
    ) from e


async def _get_minimap_player_and_room_id(
    request: Request,
    current_user: User | None,
    persistence: "AsyncPersistenceLayer",
) -> tuple[Any, str | None]:
    """
    Resolve player and current_room_id for minimap. Raises LoggedHTTPException if not authenticated or player not found.
    Returns (player, current_room_id).
    """
    if not current_user:
        raise LoggedHTTPException(status_code=401, detail="Authentication required")
    player = await persistence.get_player_by_user_id(str(current_user.id))
    if not player:
        raise LoggedHTTPException(status_code=404, detail="Player not found")
    current_room_id = request.query_params.get("current_room_id") or player.current_room_id
    return player, current_room_id


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
        zone_context = MapZoneContext(plane, zone, sub_zone)
        rooms, current_room_id = await _prepare_ascii_map_context(
            request=request,
            zone_context=zone_context,
            current_user=current_user,
            session=session,
            persistence=persistence,
            exploration_service=exploration_service,
            room_service=room_service,
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
            viewport={"x": viewport_x, "y": viewport_y, "width": viewport_width, "height": viewport_height},
        )

    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Map generation errors unpredictable, must handle gracefully
        _handle_ascii_map_error(e, plane, zone, sub_zone)


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
        player, current_room_id = await _get_minimap_player_and_room_id(request, current_user, persistence)
        # Type narrowing and runtime guard; _get_minimap_player_and_room_id raises if unauthenticated
        if current_user is None:
            raise LoggedHTTPException(status_code=401, detail="Authentication required")

        player_id = uuid.UUID(str(player.player_id)) if player else None
        is_admin = current_user.is_admin or current_user.is_superuser
        zone_context = MapZoneContext(plane=plane, zone=zone, sub_zone=sub_zone)
        html_map = await generate_minimap_html(
            session=session,
            zone_context=zone_context,
            size=size,
            current_room_id=current_room_id,
            is_admin=is_admin,
            player_id=player_id,
            exploration_service=exploration_service,
            room_service=room_service,
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
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to generate ASCII minimap",
        ) from e


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
            raise LoggedHTTPException(status_code=401, detail="Authentication required")

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
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to recalculate coordinates",
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
            raise LoggedHTTPException(
                status_code=401,
                detail="Authentication required",
                requested_room_id=room_id,
            )

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
            raise LoggedHTTPException(
                status_code=404,
                detail="Room not found",
                requested_room_id=room_id,
            )

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
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to set map origin",
            requested_room_id=room_id,
        ) from e
