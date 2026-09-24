"""
Shared DB/validation/memory-mutation helper functions for room API endpoints.

Split out of rooms.py to keep that module's file-nloc under the project limit (#787).
"""

import json
import uuid
from typing import TYPE_CHECKING, Any, cast

from fastapi import Request
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..models.user import User
from ..models.world import ROOM_ENVIRONMENTS
from ..schemas.rooms import RoomUpdateRequest
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

    if not bool(result.scalar()):
        logger.warning("No rows updated for room position", room_id=room_id)
        raise LoggedHTTPException(
            status_code=404,
            detail="Room not found in database",
            requested_room_id=room_id,
        )

    await session.commit()


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


def apply_room_exit_to_memory(
    room_service: RoomService,
    room_id: str,
    direction: str,
    target_room_id: str | None,
    *,
    delete: bool = False,
) -> None:
    """Mutate Room.exits in memory so list_rooms sees exit CRUD (LRU invalidate alone is not enough)."""
    persistence = getattr(room_service, "persistence", None)
    if persistence is None:
        return
    memory_room = persistence.get_room_by_id(room_id)
    if memory_room is None:
        return
    exits = getattr(memory_room, "exits", None)
    if not isinstance(exits, dict):
        return
    if delete:
        exits.pop(direction, None)
        return
    if target_room_id is not None:
        exits[direction] = target_room_id


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


def build_exit_attributes(flags: list[str] | None, description: str | None) -> str:
    """Build the room_links.attributes JSONB payload (as a JSON string) from flags/description."""
    payload: dict[str, list[str] | str] = {}
    if flags:
        payload["flags"] = flags
    if description:
        payload["description"] = description
    return json.dumps(payload)


async def create_room_link_in_db(
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


async def update_room_link_in_db(
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


async def delete_room_link_in_db(session: AsyncSession, from_room_id: str, direction: str) -> bool:
    """Delete a room exit via delete_room_link(). Returns False if the room or exit isn't found."""
    query = text("SELECT delete_room_link(:from_room_id, :direction)")
    result = await session.execute(query, {"from_room_id": from_room_id, "direction": direction})
    deleted = bool(result.scalar())
    if deleted:
        await session.commit()
    return deleted
