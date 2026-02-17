"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

import uuid
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Depends, Query, Request, status
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.users import get_current_user
from ..database import get_async_session
from ..dependencies import AsyncPersistenceDep, ExplorationServiceDep, RoomServiceDep
from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..models.user import User
from ..schemas.rooms import RoomListResponse, RoomPositionUpdateResponse, RoomResponse
from ..services.admin_auth_service import AdminAction, get_admin_auth_service
from ..services.exploration_service import ExplorationService
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])

logger.info("Rooms API router initialized", prefix="/rooms")


async def _apply_exploration_filter_if_needed(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exploration filtering requires multiple dependencies (user, services, persistence, session) for proper validation and filtering
    rooms: list[dict[str, Any]],
    filter_explored: bool,
    current_user: User | None,
    room_service: RoomService,
    persistence: "AsyncPersistenceLayer",
    exploration_service: ExplorationService,
    session: AsyncSession,
) -> list[dict[str, Any]]:
    """
    Apply exploration filter to rooms if requested and user is not admin.

    Args:
        rooms: List of room dictionaries
        filter_explored: Whether to filter by explored rooms
        current_user: Current authenticated user
        room_service: Room service instance
        persistence: Persistence layer instance
        exploration_service: Exploration service instance
        session: Database session

    Returns:
        Filtered list of room dictionaries
    """
    if not filter_explored or not current_user:
        return rooms

    # Admins see all rooms regardless of exploration status
    is_admin = current_user.is_admin or current_user.is_superuser
    if is_admin:
        logger.debug(
            "Admin user requested filtered rooms, but admins see all rooms",
            user_id=str(current_user.id),
            username=current_user.username,
        )
        return rooms

    # Get player from user
    user_id = str(current_user.id)
    player = await persistence.get_player_by_user_id(user_id)

    if player:
        # Get explored rooms for this player using RoomService
        player_id = uuid.UUID(str(player.player_id))
        return await room_service.filter_rooms_by_exploration(rooms, player_id, exploration_service, session)

    logger.warning("Player not found for user, cannot filter by exploration", user_id=user_id)
    return rooms


def _validate_room_position_update(current_user: User | None, room_id: str, request: Request) -> None:
    """Validate authentication and admin permissions for room position update."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=401,
            detail="Authentication required",
            requested_room_id=room_id,
        )

    auth_service = get_admin_auth_service()
    auth_service.validate_permission(current_user, AdminAction.UPDATE_ROOM_POSITION, request)


async def _update_room_position_in_db(
    session: AsyncSession, room_id: str, map_x: int, map_y: int, _request: Request
) -> None:
    """Update room position in database and verify the update succeeded."""
    update_query = text(
        """
        UPDATE rooms
        SET map_x = :map_x, map_y = :map_y
        WHERE stable_id = :room_id
        """
    )

    result = await session.execute(
        update_query,
        {
            "map_x": map_x,
            "map_y": map_y,
            "room_id": room_id,
        },
    )

    rowcount: int = getattr(result, "rowcount", 0)
    if not rowcount:
        logger.warning("No rows updated for room position", room_id=room_id)
        raise LoggedHTTPException(
            status_code=404,
            detail="Room not found in database",
            requested_room_id=room_id,
        )

    await session.commit()


async def _invalidate_room_cache(room_service: RoomService, room_id: str) -> None:
    """Invalidate room cache to force reload."""
    if room_service.room_cache:
        room_service.room_cache.invalidate_room(room_id)


# IMPORTANT: /list route must come BEFORE /{room_id} route
# FastAPI matches routes in order, and /{room_id} would match /list otherwise
@room_router.get("/list", response_model=RoomListResponse)
async def list_rooms(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: API endpoint requires many query parameters and intermediate variables for room listing
    _request: Request,
    plane: str = Query(..., description="Plane name (required)"),
    zone: str = Query(..., description="Zone name (required)"),
    sub_zone: str | None = Query(None, description="Optional sub-zone name for filtering"),
    include_exits: bool = Query(True, description="Whether to include exit data in response"),
    filter_explored: bool = Query(False, description="Filter to only show explored rooms (requires authentication)"),
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
    persistence: "AsyncPersistenceLayer" = AsyncPersistenceDep,
    exploration_service: ExplorationService = ExplorationServiceDep,
) -> RoomListResponse:
    """
    List rooms filtered by plane, zone, and optionally sub_zone.

    Returns room data in the same format as the single room endpoint,
    including map_x and map_y coordinates when available in the database.

    If filter_explored is True and a user is authenticated:
    - Admin users: See all rooms (filtering is skipped)
    - Non-admin users: Only see rooms that the player has explored
    """
    logger.debug(
        "Room list requested",
        plane=plane,
        zone=zone,
        sub_zone=sub_zone,
        include_exits=include_exits,
        filter_explored=filter_explored,
        has_user=current_user is not None,
    )

    try:  # pylint: disable=too-many-nested-blocks  # Reason: Room listing requires complex nested logic for filtering, error handling, and response formatting
        rooms = await room_service.list_rooms(
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            include_exits=include_exits,
        )

        rooms = await _apply_exploration_filter_if_needed(
            rooms, filter_explored, current_user, room_service, persistence, exploration_service, session
        )

        logger.debug(
            "Room list returned",
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            count=len(rooms),
            filtered=filter_explored,
            is_admin=(current_user.is_admin or current_user.is_superuser) if current_user else False,
        )

        return RoomListResponse(
            rooms=rooms,
            total=len(rooms),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room listing errors unpredictable, must handle gracefully
        logger.error(
            "Error listing rooms",
            error=str(e),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            exc_info=True,
        )
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to retrieve room list",
        ) from e


class RoomPositionUpdate(BaseModel):
    """Request model for updating room map coordinates."""

    map_x: float = Field(..., description="X coordinate for map position", ge=-10000, le=10000)
    map_y: float = Field(..., description="Y coordinate for map position", ge=-10000, le=10000)


@room_router.post("/{room_id}/position", response_model=RoomPositionUpdateResponse)
async def update_room_position(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: API endpoint requires many parameters for room position updates
    room_id: str,
    position_data: RoomPositionUpdate,
    _request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> RoomPositionUpdateResponse:
    """
    Update room map coordinates (admin only).

    Updates the map_x and map_y columns in the rooms table for the specified room.
    Requires admin privileges.
    """
    try:
        # Validate authentication and permissions
        _validate_room_position_update(current_user, room_id, _request)

        auth_service = get_admin_auth_service()
        logger.info(
            "Room position update requested",
            user=auth_service.get_username(current_user),
            room_id=room_id,
            map_x=position_data.map_x,
            map_y=position_data.map_y,
        )

        # Verify room exists
        room = await room_service.get_room(room_id)
        if not room:
            logger.warning("Room not found for position update", room_id=room_id)
            raise LoggedHTTPException(
                status_code=404,
                detail="Room not found",
                requested_room_id=room_id,
            )

        # Update room position in database
        await _update_room_position_in_db(
            session, room_id, int(position_data.map_x), int(position_data.map_y), _request
        )

        logger.info(
            "Room position updated successfully",
            room_id=room_id,
            map_x=position_data.map_x,
            map_y=position_data.map_y,
        )

        # Invalidate room cache
        await _invalidate_room_cache(room_service, room_id)

        return RoomPositionUpdateResponse(
            room_id=room_id,
            map_x=position_data.map_x,
            map_y=position_data.map_y,
            message="Room position updated successfully",
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room creation errors unpredictable, must rollback and create context
        await session.rollback()
        logger.error(
            "Error updating room position",
            error=str(e),
            exc_info=True,
            requested_room_id=room_id,
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update room position",
            requested_room_id=room_id,
        ) from e


@room_router.get("/{room_id}", response_model=RoomResponse)
async def get_room(
    room_id: str,
    _request: Request,
    room_service: RoomService = RoomServiceDep,
) -> RoomResponse:
    """Get room information by room ID."""
    logger.debug("Room information requested", room_id=room_id)

    room = await room_service.get_room(room_id)
    if not room:
        logger.warning("Room not found", room_id=room_id)
        raise LoggedHTTPException(
            status_code=404,
            detail="Room not found",
            requested_room_id=room_id,
        )

    logger.debug("Room information returned", room_id=room_id, room_name=room.get("name", "Unknown"))
    if not isinstance(room, dict):
        raise TypeError("room must be a dict")
    return RoomResponse(**room)
