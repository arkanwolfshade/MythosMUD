"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

import json
import uuid
from typing import TYPE_CHECKING, Any

from fastapi import APIRouter, Depends, Query, Request, status
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.users import get_current_user
from ..database import get_async_session
from ..dependencies import AsyncPersistenceDep, ExplorationServiceDep, RoomServiceDep
from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..models.command_base import Direction
from ..models.user import User
from ..models.world import ROOM_ENVIRONMENTS
from ..schemas.rooms import (
    ExitCreateRequest,
    ExitResponse,
    ExitUpdateRequest,
    RoomListResponse,
    RoomPositionUpdateResponse,
    RoomResponse,
    RoomUpdateRequest,
    RoomUpdateResponse,
)
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


def _validate_admin_room_action(current_user: User | None, room_id: str, request: Request, action: AdminAction) -> None:
    """Validate authentication and admin permissions for a room write action."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=401,
            detail="Authentication required",
            requested_room_id=room_id,
        )

    auth_service = get_admin_auth_service()
    auth_service.validate_permission(current_user, action, request)


def _validate_room_position_update(current_user: User | None, room_id: str, request: Request) -> None:
    """Validate authentication and admin permissions for room position update."""
    _validate_admin_room_action(current_user, room_id, request, AdminAction.UPDATE_ROOM_POSITION)


async def _update_room_position_in_db(
    session: AsyncSession, room_id: str, map_x: int, map_y: int, _request: Request
) -> None:
    """Update room position in database and verify the update succeeded."""
    update_query = text("SELECT update_room_map_position(:room_id, :map_x, :map_y)")

    result = await session.execute(
        update_query,
        {
            "map_x": map_x,
            "map_y": map_y,
            "room_id": room_id,
        },
    )

    if not bool(result.scalar()):
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


async def _update_room_properties_in_db(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: room property update needs each field plus the explicit set-environment flag
    session: AsyncSession,
    room_id: str,
    name: str | None,
    description: str | None,
    environment: str | None,
    set_environment: bool,
) -> bool:
    """Update room name/description/environment via update_room_properties(). Returns False if the room doesn't exist."""
    query = text("SELECT update_room_properties(:room_id, :name, :description, :environment, :set_environment)")
    result = await session.execute(
        query,
        {
            "room_id": room_id,
            "name": name,
            "description": description,
            "environment": environment,
            "set_environment": set_environment,
        },
    )
    updated = bool(result.scalar())
    if updated:
        await session.commit()
    return updated


def _build_exit_attributes(flags: list[str] | None, description: str | None) -> str:
    """Build the room_links.attributes JSONB payload (as a JSON string) from flags/description."""
    payload: dict[str, list[str] | str] = {}
    if flags:
        payload["flags"] = flags
    if description:
        payload["description"] = description
    return json.dumps(payload)


async def _create_room_link_in_db(
    session: AsyncSession, from_room_id: str, direction: str, to_room_id: str, attributes_json: str
) -> bool:
    """Create a room exit via create_room_link(). Returns False if either room doesn't exist.

    Raises sqlalchemy.exc.IntegrityError on a UNIQUE (from_room_id, direction) collision.
    """
    query = text("SELECT create_room_link(:from_room_id, :direction, :to_room_id, CAST(:attributes AS jsonb))")
    result = await session.execute(
        query,
        {"from_room_id": from_room_id, "direction": direction, "to_room_id": to_room_id, "attributes": attributes_json},
    )
    created = bool(result.scalar())
    if created:
        await session.commit()
    return created


async def _update_room_link_in_db(
    session: AsyncSession, from_room_id: str, direction: str, to_room_id: str | None, attributes_json: str | None
) -> bool:
    """Update a room exit via update_room_link(). Returns False if the room, target, or exit isn't found."""
    query = text("SELECT update_room_link(:from_room_id, :direction, :to_room_id, CAST(:attributes AS jsonb))")
    result = await session.execute(
        query,
        {"from_room_id": from_room_id, "direction": direction, "to_room_id": to_room_id, "attributes": attributes_json},
    )
    updated = bool(result.scalar())
    if updated:
        await session.commit()
    return updated


async def _delete_room_link_in_db(session: AsyncSession, from_room_id: str, direction: str) -> bool:
    """Delete a room exit via delete_room_link(). Returns False if the room or exit isn't found."""
    query = text("SELECT delete_room_link(:from_room_id, :direction)")
    result = await session.execute(query, {"from_room_id": from_room_id, "direction": direction})
    deleted = bool(result.scalar())
    if deleted:
        await session.commit()
    return deleted


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


@room_router.put("/{room_id}", response_model=RoomUpdateResponse)
async def update_room(
    room_id: str,
    update_data: RoomUpdateRequest,
    _request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> RoomUpdateResponse:
    """
    Update room properties: name, description, environment (admin only).

    Zone and sub_zone are intentionally not editable here -- changing them means re-parenting the
    room to a different subzone, which is a structural move (stable_id is unique per subzone) and
    out of scope for this endpoint. See #627.
    """
    try:
        _validate_admin_room_action(current_user, room_id, _request, AdminAction.UPDATE_ROOM)

        room = await room_service.get_room(room_id)
        if not room:
            logger.warning("Room not found for property update", room_id=room_id)
            raise LoggedHTTPException(
                status_code=404,
                detail="Room not found",
                requested_room_id=room_id,
            )

        set_environment = update_data.environment_is_set()
        environment = update_data.environment if update_data.environment else None
        if set_environment and environment is not None and environment not in ROOM_ENVIRONMENTS:
            raise LoggedHTTPException(
                status_code=422,
                detail=f"Invalid environment: {environment}",
                requested_room_id=room_id,
            )

        updated = await _update_room_properties_in_db(
            session, room_id, update_data.name, update_data.description, environment, set_environment
        )
        if not updated:
            logger.warning("No rows updated for room properties", room_id=room_id)
            raise LoggedHTTPException(
                status_code=404,
                detail="Room not found in database",
                requested_room_id=room_id,
            )

        logger.info("Room properties updated successfully", room_id=room_id)

        await _invalidate_room_cache(room_service, room_id)

        return RoomUpdateResponse(
            room_id=room_id,
            name=update_data.name,
            description=update_data.description,
            environment=environment if set_environment else None,
            message="Room updated successfully",
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room update errors unpredictable, must rollback and create context
        await session.rollback()
        logger.error("Error updating room properties", error=str(e), exc_info=True, requested_room_id=room_id)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update room",
            requested_room_id=room_id,
        ) from e


@room_router.post("/{room_id}/exits", response_model=ExitResponse, status_code=status.HTTP_201_CREATED)
async def create_room_exit(
    room_id: str,
    exit_data: ExitCreateRequest,
    _request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> ExitResponse:
    """
    Create a single directed room exit (admin only).

    Writes exactly one room_links row for the given direction. A two-way corridor is two calls
    (one per direction) -- this endpoint never synthesizes a reverse exit. See #627.
    """
    try:
        _validate_admin_room_action(current_user, room_id, _request, AdminAction.CREATE_ROOM_EXIT)

        source_room = await room_service.get_room(room_id)
        if not source_room:
            raise LoggedHTTPException(status_code=404, detail="Room not found", requested_room_id=room_id)

        target_room = await room_service.get_room(exit_data.target_room_id)
        if not target_room:
            raise LoggedHTTPException(
                status_code=404,
                detail="Target room not found",
                requested_room_id=exit_data.target_room_id,
            )

        attributes_json = _build_exit_attributes(exit_data.flags, exit_data.description)

        try:
            created = await _create_room_link_in_db(
                session, room_id, exit_data.direction.value, exit_data.target_room_id, attributes_json
            )
        except IntegrityError as e:
            await session.rollback()
            logger.warning("Exit already exists", room_id=room_id, direction=exit_data.direction.value)
            raise LoggedHTTPException(
                status_code=409,
                detail=f"Exit already exists: {exit_data.direction.value}",
                requested_room_id=room_id,
            ) from e

        if not created:
            raise LoggedHTTPException(status_code=404, detail="Room not found in database", requested_room_id=room_id)

        logger.info("Room exit created successfully", room_id=room_id, direction=exit_data.direction.value)

        await _invalidate_room_cache(room_service, room_id)

        return ExitResponse(
            room_id=room_id,
            direction=exit_data.direction.value,
            target_room_id=exit_data.target_room_id,
            message="Exit created successfully",
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Exit creation errors unpredictable, must rollback and create context
        await session.rollback()
        logger.error("Error creating room exit", error=str(e), exc_info=True, requested_room_id=room_id)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create exit",
            requested_room_id=room_id,
        ) from e


@room_router.put("/{room_id}/exits/{direction}", response_model=ExitResponse)
async def update_room_exit(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: endpoint needs room_id, direction, body, request, and DI params
    room_id: str,
    direction: Direction,
    exit_data: ExitUpdateRequest,
    _request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> ExitResponse:
    """Update an existing room exit's target room and/or flags/description (admin only)."""
    try:
        _validate_admin_room_action(current_user, room_id, _request, AdminAction.UPDATE_ROOM_EXIT)

        source_room = await room_service.get_room(room_id)
        if not source_room:
            raise LoggedHTTPException(status_code=404, detail="Room not found", requested_room_id=room_id)

        if exit_data.target_room_id is not None:
            target_room = await room_service.get_room(exit_data.target_room_id)
            if not target_room:
                raise LoggedHTTPException(
                    status_code=404,
                    detail="Target room not found",
                    requested_room_id=exit_data.target_room_id,
                )

        attributes_json = None
        if exit_data.flags is not None or exit_data.description is not None:
            attributes_json = _build_exit_attributes(exit_data.flags, exit_data.description)

        updated = await _update_room_link_in_db(session, room_id, direction.value, exit_data.target_room_id, attributes_json)
        if not updated:
            raise LoggedHTTPException(status_code=404, detail="Exit not found", requested_room_id=room_id)

        logger.info("Room exit updated successfully", room_id=room_id, direction=direction.value)

        await _invalidate_room_cache(room_service, room_id)

        return ExitResponse(
            room_id=room_id,
            direction=direction.value,
            target_room_id=exit_data.target_room_id,
            message="Exit updated successfully",
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Exit update errors unpredictable, must rollback and create context
        await session.rollback()
        logger.error("Error updating room exit", error=str(e), exc_info=True, requested_room_id=room_id)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update exit",
            requested_room_id=room_id,
        ) from e


@room_router.delete("/{room_id}/exits/{direction}", response_model=ExitResponse)
async def delete_room_exit(
    room_id: str,
    direction: Direction,
    _request: Request,
    current_user: User | None = Depends(get_current_user),
    session: AsyncSession = Depends(get_async_session),
    room_service: RoomService = RoomServiceDep,
) -> ExitResponse:
    """Delete a room exit (admin only)."""
    try:
        _validate_admin_room_action(current_user, room_id, _request, AdminAction.DELETE_ROOM_EXIT)

        deleted = await _delete_room_link_in_db(session, room_id, direction.value)
        if not deleted:
            raise LoggedHTTPException(status_code=404, detail="Exit not found", requested_room_id=room_id)

        logger.info("Room exit deleted successfully", room_id=room_id, direction=direction.value)

        await _invalidate_room_cache(room_service, room_id)

        return ExitResponse(
            room_id=room_id,
            direction=direction.value,
            target_room_id=None,
            message="Exit deleted successfully",
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Exit deletion errors unpredictable, must rollback and create context
        await session.rollback()
        logger.error("Error deleting room exit", error=str(e), exc_info=True, requested_room_id=room_id)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete exit",
            requested_room_id=room_id,
        ) from e
