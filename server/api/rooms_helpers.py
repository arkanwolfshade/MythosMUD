"""
Shared DB/validation/memory-mutation helper functions for room API endpoints.

Split out of rooms.py to keep that module's file-nloc under the project limit (#787).
"""

import uuid
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, cast

from fastapi import Request, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..models.user import User
from ..models.world import ROOM_ENVIRONMENTS
from ..schemas.rooms import (
    RoomListResponse,
    RoomPositionUpdateResponse,
    RoomUpdateRequest,
    RoomUpdateResponse,
)
from ..schemas.rooms.room_data import RoomData
from ..services.admin_auth_service import AdminAction, get_admin_auth_service
from ..services.exploration_service import ExplorationService
from ..structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)


async def apply_exploration_filter_if_needed(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Exploration filtering requires multiple dependencies (user, services, persistence, session) for proper validation and filtering
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


@dataclass(frozen=True)
class RoomListQuery:
    """The /list route's query parameters, grouped so fetch_room_list stays under the arg limit."""

    plane: str
    zone: str
    sub_zone: str | None
    include_exits: bool
    filter_explored: bool


async def fetch_room_list(
    query: RoomListQuery,
    current_user: User | None,
    room_service: RoomService,
    persistence: "AsyncPersistenceLayer",
    exploration_service: ExplorationService,
    session: AsyncSession,
) -> RoomListResponse:
    """
    Fetch rooms for plane/zone/sub_zone, apply the exploration filter, and log both steps.

    Raises:
        LoggedHTTPException: 500 if the room service or filter raises.
    """
    plane, zone, sub_zone = query.plane, query.zone, query.sub_zone
    include_exits, filter_explored = query.include_exits, query.filter_explored
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
        rooms = await room_service.list_rooms(plane=plane, zone=zone, sub_zone=sub_zone, include_exits=include_exits)
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

        # room_service.list_rooms returns plain dicts; RoomListResponse (pydantic) validates/coerces
        # them into RoomData at construction, same as the pre-extraction call site did.
        return RoomListResponse(
            rooms=cast(list[RoomData], rooms), total=len(rooms), plane=plane, zone=zone, sub_zone=sub_zone
        )
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room listing errors unpredictable, must handle gracefully
        logger.error("Error listing rooms", error=str(e), plane=plane, zone=zone, sub_zone=sub_zone, exc_info=True)
        raise LoggedHTTPException(status_code=500, detail="Failed to retrieve room list") from e


def validate_admin_room_action(current_user: User | None, room_id: str, request: Request, action: AdminAction) -> None:
    """Validate authentication and admin permissions for a room write action."""
    if not current_user:
        raise LoggedHTTPException(
            status_code=401,
            detail="Authentication required",
            requested_room_id=room_id,
        )

    auth_service = get_admin_auth_service()
    auth_service.validate_permission(current_user, action, request)


def validate_room_position_update(current_user: User | None, room_id: str, request: Request) -> None:
    """Validate authentication and admin permissions for room position update."""
    validate_admin_room_action(current_user, room_id, request, AdminAction.UPDATE_ROOM_POSITION)


def validate_room_update_environment(update_data: RoomUpdateRequest, room_id: str) -> tuple[bool, str | None]:
    """Resolve the requested environment change and reject an unknown environment value."""
    set_environment = update_data.environment_is_set()
    environment = update_data.environment if update_data.environment else None
    if set_environment and environment is not None and environment not in ROOM_ENVIRONMENTS:
        raise LoggedHTTPException(
            status_code=422,
            detail=f"Invalid environment: {environment}",
            requested_room_id=room_id,
        )
    return set_environment, environment


async def update_room_position_in_db(
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

    if not bool(cast(object, result.scalar())):
        logger.warning("No rows updated for room position", room_id=room_id)
        raise LoggedHTTPException(
            status_code=404,
            detail="Room not found in database",
            requested_room_id=room_id,
        )

    await session.commit()


async def handle_update_room_position(
    room_id: str,
    map_x: float,
    map_y: float,
    request: Request,
    current_user: User | None,
    session: AsyncSession,
    room_service: RoomService,
) -> RoomPositionUpdateResponse:
    """
    Update room map coordinates (admin only).

    Updates the map_x and map_y columns in the rooms table for the specified room.

    Raises:
        LoggedHTTPException: 404 (room not found) or 500.
    """
    try:
        validate_room_position_update(current_user, room_id, request)

        auth_service = get_admin_auth_service()
        logger.info(
            "Room position update requested",
            user=auth_service.get_username(current_user),
            room_id=room_id,
            map_x=map_x,
            map_y=map_y,
        )

        room = await room_service.get_room(room_id)
        if not room:
            logger.warning("Room not found for position update", room_id=room_id)
            raise LoggedHTTPException(status_code=404, detail="Room not found", requested_room_id=room_id)

        await update_room_position_in_db(session, room_id, int(map_x), int(map_y), request)

        logger.info("Room position updated successfully", room_id=room_id, map_x=map_x, map_y=map_y)

        await invalidate_room_cache(room_service, room_id)

        return RoomPositionUpdateResponse(
            room_id=room_id,
            map_x=map_x,
            map_y=map_y,
            message="Room position updated successfully",
        )

    except LoggedHTTPException:
        raise
    except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room creation errors unpredictable, must rollback and create context
        await session.rollback()
        logger.error("Error updating room position", error=str(e), exc_info=True, requested_room_id=room_id)
        raise LoggedHTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update room position",
            requested_room_id=room_id,
        ) from e


async def invalidate_room_cache(room_service: RoomService, room_id: str) -> None:
    """Invalidate room cache to force reload."""
    if room_service.room_cache:
        room_service.room_cache.invalidate_room(room_id)


def apply_room_properties_to_memory(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: mirrors DB property fields plus set_environment flag
    room_service: RoomService,
    room_id: str,
    name: str | None,
    description: str | None,
    environment: str | None,
    set_environment: bool,
    resolved_environment: str | None,
) -> None:
    """Mutate RoomRepository memory so list_rooms sees property edits (LRU invalidate alone is not enough)."""
    persistence = getattr(room_service, "persistence", None)
    if persistence is None:
        return
    memory_room = persistence.get_room_by_id(room_id)
    if memory_room is None:
        return
    if name is not None:
        memory_room.name = name
    if description is not None:
        memory_room.description = description
    if not set_environment:
        return
    # #663: environment lives in rooms.environment now, not attributes. room_environment is the
    # room's own raw value (None = inherit); environment is the DB-resolved cascade, so the
    # inheritance rule stays defined once, in SQL.
    memory_room.room_environment = environment
    memory_room.environment = resolved_environment or "outdoors"


async def update_room_properties_in_db(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: room property update needs each field plus the explicit set-environment flag
    session: AsyncSession,
    room_id: str,
    name: str | None,
    description: str | None,
    environment: str | None,
    set_environment: bool,
) -> tuple[bool, str | None]:
    """
    Update room name/description/environment via update_room_properties().

    Returns (updated, resolved_environment) -- resolved_environment is the room's environment
    after the room -> subzone -> zone -> 'outdoors' cascade (#663), computed in SQL so the
    in-memory Room stays in sync with the database's inheritance rule. (False, None) if the room
    doesn't exist.
    """
    query = text(
        "SELECT updated, resolved_environment FROM update_room_properties(:room_id, :name, :description, :environment, :set_environment)"
    )
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
    updated, resolved_environment = cast(tuple[bool, str | None], cast(object, result.one()))
    updated = bool(updated)
    if updated:
        await session.commit()
    return updated, resolved_environment


async def handle_update_room(
    room_id: str,
    update_data: RoomUpdateRequest,
    request: Request,
    current_user: User | None,
    session: AsyncSession,
    room_service: RoomService,
) -> RoomUpdateResponse:
    """
    Update room name/description/environment (admin only).

    Zone and sub_zone are intentionally not editable here -- changing them means re-parenting the
    room to a different subzone, which is a structural move (stable_id is unique per subzone) and
    out of scope for this endpoint. See #627.

    Raises:
        LoggedHTTPException: 404 (room not found) or 500.
    """
    try:
        validate_admin_room_action(current_user, room_id, request, AdminAction.UPDATE_ROOM)

        room = await room_service.get_room(room_id)
        if not room:
            logger.warning("Room not found for property update", room_id=room_id)
            raise LoggedHTTPException(status_code=404, detail="Room not found", requested_room_id=room_id)

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


# Exit (room_links) helpers moved to rooms_helpers_exits.py to keep this module's line
# count under Pylint's too-many-lines limit (C0302). rooms.py imports them from there
# directly (not re-exported here) to avoid a circular import back into this module.
