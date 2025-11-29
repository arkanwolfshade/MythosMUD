"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

import uuid
from typing import Any

from fastapi import APIRouter, Depends, Query, Request, status
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.users import get_current_user
from ..database import get_async_session
from ..dependencies import RoomServiceDep
from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..logging.enhanced_logging_config import get_logger
from ..models.user import User
from ..persistence import get_persistence
from ..services.admin_auth_service import AdminAction, get_admin_auth_service
from ..services.exploration_service import get_exploration_service
from ..utils.error_logging import create_context_from_request

logger = get_logger(__name__)

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])

logger.info("Rooms API router initialized", prefix="/rooms")


# IMPORTANT: /list route must come BEFORE /{room_id} route
# FastAPI matches routes in order, and /{room_id} would match /list otherwise
@room_router.get("/list")
async def list_rooms(
    request: Request,
    plane: str = Query(..., description="Plane name (required)"),
    zone: str = Query(..., description="Zone name (required)"),
    sub_zone: str | None = Query(None, description="Optional sub-zone name for filtering"),
    include_exits: bool = Query(True, description="Whether to include exit data in response"),
    filter_explored: bool = Query(False, description="Filter to only show explored rooms (requires authentication)"),
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> dict[str, Any]:
    """
    List rooms filtered by plane, zone, and optionally sub_zone.

    Returns room data in the same format as the single room endpoint,
    including map_x and map_y coordinates when available in the database.

    If filter_explored is True and a user is authenticated, only returns
    rooms that the player has explored.
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

    try:
        rooms = await room_service.list_rooms(
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            include_exits=include_exits,
        )

        # Filter by explored rooms if requested and user is authenticated
        if filter_explored and current_user:
            try:
                # Get player from user
                persistence = get_persistence()
                user_id = str(current_user.id)
                player = persistence.get_player_by_user_id(user_id)

                if player:
                    # Get explored rooms for this player
                    exploration_service = get_exploration_service()
                    player_id = uuid.UUID(str(player.player_id))
                    explored_room_ids = await exploration_service.get_explored_rooms(player_id, session)

                    # Convert explored room UUIDs to stable_ids for filtering
                    # We need to look up stable_ids from room UUIDs
                    if explored_room_ids:
                        # Query to get stable_ids from room UUIDs (using PostgreSQL array syntax)
                        lookup_query = text("SELECT stable_id FROM rooms WHERE id = ANY(:room_ids::uuid[])")
                        result = await session.execute(lookup_query, {"room_ids": explored_room_ids})
                        explored_stable_ids = {row[0] for row in result.fetchall()}

                        # Filter rooms to only include explored ones
                        rooms = [room for room in rooms if room.get("id") in explored_stable_ids]

                        logger.debug(
                            "Filtered rooms by exploration",
                            explored_count=len(explored_stable_ids),
                            filtered_count=len(rooms),
                        )
                    else:
                        # Player has explored no rooms - return empty list
                        rooms = []
                        logger.debug("Player has explored no rooms, returning empty list")
                else:
                    logger.warning("Player not found for user, cannot filter by exploration", user_id=user_id)
            except Exception as e:
                # Log error but don't fail the request - just return all rooms
                logger.warning(
                    "Error filtering by explored rooms, returning all rooms",
                    error=str(e),
                    error_type=type(e).__name__,
                )

        logger.debug(
            "Room list returned",
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            count=len(rooms),
            filtered=filter_explored,
        )

        return {
            "rooms": rooms,
            "total": len(rooms),
            "plane": plane,
            "zone": zone,
            "sub_zone": sub_zone,
        }
    except Exception as e:
        logger.error(
            "Error listing rooms",
            error=str(e),
            plane=plane,
            zone=zone,
            sub_zone=sub_zone,
            exc_info=True,
        )
        context = create_context_from_request(request)
        raise LoggedHTTPException(
            status_code=500,
            detail="Failed to retrieve room list",
            context=context,
        ) from e


class RoomPositionUpdate(BaseModel):
    """Request model for updating room map coordinates."""

    map_x: float = Field(..., description="X coordinate for map position", ge=-10000, le=10000)
    map_y: float = Field(..., description="Y coordinate for map position", ge=-10000, le=10000)


@room_router.post("/{room_id}/position")
async def update_room_position(
    room_id: str,
    position_data: RoomPositionUpdate,
    request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> dict[str, Any]:
    """
    Update room map coordinates (admin only).

    Updates the map_x and map_y columns in the rooms table for the specified room.
    Requires admin privileges.
    """
    try:
        # Check authentication first
        if not current_user:
            context = create_context_from_request(request)
            context.metadata["requested_room_id"] = room_id
            raise LoggedHTTPException(status_code=401, detail="Authentication required", context=context)

        # Validate admin permission
        auth_service = get_admin_auth_service()
        auth_service.validate_permission(current_user, AdminAction.UPDATE_ROOM_POSITION, request)

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
            context = create_context_from_request(request)
            context.metadata["requested_room_id"] = room_id
            raise LoggedHTTPException(status_code=404, detail="Room not found", context=context)

        # Update room position in database
        # Note: This assumes map_x and map_y columns exist (will be added in Task 10)
        # The query uses stable_id to find the room, as that's the unique identifier in the database
        # The room_id passed to the API is the full hierarchical ID, which should match stable_id
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
                "map_x": position_data.map_x,
                "map_y": position_data.map_y,
                "room_id": room_id,  # room_id should match stable_id in database
            },
        )

        # Check if any rows were updated
        # SQLAlchemy 2.0 async Result has rowcount for UPDATE statements
        # Use getattr with default to handle type checking
        rowcount: int = getattr(result, "rowcount", 0)
        if rowcount == 0:
            logger.warning("No rows updated for room position", room_id=room_id)
            context = create_context_from_request(request)
            context.metadata["requested_room_id"] = room_id
            raise LoggedHTTPException(
                status_code=404,
                detail="Room not found in database",
                context=context,
            )

        # Commit the transaction
        await session.commit()

        logger.info(
            "Room position updated successfully",
            room_id=room_id,
            map_x=position_data.map_x,
            map_y=position_data.map_y,
        )

        # Invalidate room cache to force reload
        if room_service.room_cache:
            await room_service.room_cache.invalidate_room(room_id)

        return {
            "room_id": room_id,
            "map_x": position_data.map_x,
            "map_y": position_data.map_y,
            "message": "Room position updated successfully",
        }

    except LoggedHTTPException:
        raise
    except Exception as e:
        await session.rollback()
        context = create_context_from_request(request)
        logger.error(
            "Error updating room position",
            error=str(e),
            room_id=room_id,
            exc_info=True,
            **context.to_dict(),
        )
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update room position",
            context=context,
        ) from e


@room_router.get("/{room_id}")
async def get_room(
    room_id: str,
    request: Request,
    room_service: RoomService = RoomServiceDep,
) -> dict[str, Any]:
    """Get room information by room ID."""
    logger.debug("Room information requested", room_id=room_id)

    room = await room_service.get_room(room_id)
    if not room:
        logger.warning("Room not found", room_id=room_id)
        context = create_context_from_request(request)
        context.metadata["requested_room_id"] = room_id
        raise LoggedHTTPException(status_code=404, detail="Room not found", context=context)

    logger.debug("Room information returned", room_id=room_id, room_name=room.get("name", "Unknown"))
    assert isinstance(room, dict)
    return room
