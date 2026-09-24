"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, Query, Request, status
from pydantic import Field
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.users import get_current_user
from ..database import get_async_session
from ..dependencies import AsyncPersistenceDep, ExplorationServiceDep, RoomServiceDep
from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..models.command_base import Direction
from ..models.user import User
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
from ..schemas.shared.base import SecureBaseModel
from ..services.admin_auth_service import AdminAction, get_admin_auth_service
from ..services.exploration_service import ExplorationService
from ..structured_logging.enhanced_logging_config import get_logger
from .rooms_helpers import (
    apply_exploration_filter_if_needed,
    apply_room_exit_to_memory,
    apply_room_properties_to_memory,
    build_exit_attributes,
    create_room_link_in_db,
    delete_room_link_in_db,
    invalidate_room_cache,
    update_room_link_in_db,
    update_room_position_in_db,
    update_room_properties_in_db,
    validate_admin_room_action,
    validate_room_position_update,
    validate_room_update_environment,
)

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)

# Re-exported so tests can keep importing/patching these as server.api.rooms.<name> (pre-split API).
__all__ = [
    "room_router",
    "apply_exploration_filter_if_needed",
    "apply_room_exit_to_memory",
    "apply_room_properties_to_memory",
    "build_exit_attributes",
    "create_room_link_in_db",
    "delete_room_link_in_db",
    "invalidate_room_cache",
    "update_room_link_in_db",
    "update_room_position_in_db",
    "update_room_properties_in_db",
    "validate_admin_room_action",
    "validate_room_position_update",
    "validate_room_update_environment",
]

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])

logger.info("Rooms API router initialized", prefix="/rooms")


# IMPORTANT: /list route must come BEFORE /{room_id} route
# FastAPI matches routes in order, and /{room_id} would match /list otherwise
@room_router.get("/list", response_model=RoomListResponse)
async def list_rooms(  # pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: API endpoint requires many query parameters and intermediate variables for room listing  # lizard: allow nloc (multi-line Query() signature plus structured-log checkpoints, not branching; CCN 4, see #787)
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

        rooms = await apply_exploration_filter_if_needed(
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


class RoomPositionUpdate(SecureBaseModel):
    """Request model for updating room map coordinates."""

    map_x: float = Field(..., description="X coordinate for map position", ge=-10000, le=10000)
    map_y: float = Field(..., description="Y coordinate for map position", ge=-10000, le=10000)


@room_router.post("/{room_id}/position", response_model=RoomPositionUpdateResponse)
async def update_room_position(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: API endpoint requires many parameters for room position updates  # lizard: allow nloc (structured-log checkpoints around already-extracted DB/cache helpers, not branching; CCN 4, see #787)
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
        validate_room_position_update(current_user, room_id, _request)

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
        await update_room_position_in_db(
            session, room_id, int(position_data.map_x), int(position_data.map_y), _request
        )

        logger.info(
            "Room position updated successfully",
            room_id=room_id,
            map_x=position_data.map_x,
            map_y=position_data.map_y,
        )

        # Invalidate room cache
        await invalidate_room_cache(room_service, room_id)

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
        validate_admin_room_action(current_user, room_id, _request, AdminAction.UPDATE_ROOM)

        room = await room_service.get_room(room_id)
        if not room:
            logger.warning("Room not found for property update", room_id=room_id)
            raise LoggedHTTPException(
                status_code=404,
                detail="Room not found",
                requested_room_id=room_id,
            )

        set_environment, environment = validate_room_update_environment(update_data, room_id)

        updated, resolved_environment = await update_room_properties_in_db(
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

        apply_room_properties_to_memory(
            room_service,
            room_id,
            update_data.name,
            update_data.description,
            environment,
            set_environment,
            resolved_environment,
        )
        await invalidate_room_cache(room_service, room_id)

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
        validate_admin_room_action(current_user, room_id, _request, AdminAction.CREATE_ROOM_EXIT)

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

        attributes_json = build_exit_attributes(exit_data.flags, exit_data.description)

        try:
            created = await create_room_link_in_db(
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

        apply_room_exit_to_memory(room_service, room_id, exit_data.direction.value, exit_data.target_room_id)
        await invalidate_room_cache(room_service, room_id)

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
        validate_admin_room_action(current_user, room_id, _request, AdminAction.UPDATE_ROOM_EXIT)

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
            attributes_json = build_exit_attributes(exit_data.flags, exit_data.description)

        updated = await update_room_link_in_db(
            session, room_id, direction.value, exit_data.target_room_id, attributes_json
        )
        if not updated:
            raise LoggedHTTPException(status_code=404, detail="Exit not found", requested_room_id=room_id)

        logger.info("Room exit updated successfully", room_id=room_id, direction=direction.value)

        apply_room_exit_to_memory(room_service, room_id, direction.value, exit_data.target_room_id)
        await invalidate_room_cache(room_service, room_id)

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
        validate_admin_room_action(current_user, room_id, _request, AdminAction.DELETE_ROOM_EXIT)

        deleted = await delete_room_link_in_db(session, room_id, direction.value)
        if not deleted:
            raise LoggedHTTPException(status_code=404, detail="Exit not found", requested_room_id=room_id)

        logger.info("Room exit deleted successfully", room_id=room_id, direction=direction.value)

        apply_room_exit_to_memory(room_service, room_id, direction.value, None, delete=True)
        await invalidate_room_cache(room_service, room_id)

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
