"""
Room exit (room_links) DB/validation/memory-mutation helper functions.

Split out of rooms_helpers.py to keep that module's file-nloc under the project's
too-many-lines limit (Pylint C0302), same reason rooms_helpers.py itself was split
out of rooms.py (#787).
"""

import json
from typing import TYPE_CHECKING, cast

from fastapi import Request, status
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..models.user import User
from ..schemas.rooms import ExitCreateRequest, ExitResponse
from ..services.admin_auth_service import AdminAction
from ..structured_logging.enhanced_logging_config import get_logger
from .rooms_helpers import invalidate_room_cache, validate_admin_room_action

if TYPE_CHECKING:
    from ..async_persistence import AsyncPersistenceLayer

logger = get_logger(__name__)


def apply_room_exit_to_memory(
    room_service: RoomService,
    room_id: str,
    direction: str,
    target_room_id: str | None,
    *,
    delete: bool = False,
) -> None:
    """Mutate Room.exits in memory so list_rooms sees exit CRUD (LRU invalidate alone is not enough)."""
    persistence = cast("AsyncPersistenceLayer | None", getattr(room_service, "persistence", None))
    if persistence is None:
        return
    memory_room = persistence.get_room_by_id(room_id)
    if memory_room is None:
        return
    exits = cast("dict[str, str] | None", getattr(memory_room, "exits", None))
    if not isinstance(exits, dict):
        return
    if delete:
        _ = exits.pop(direction, None)
        return
    if target_room_id is not None:
        exits[direction] = target_room_id


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


async def handle_create_room_exit(
    room_id: str,
    exit_data: ExitCreateRequest,
    request: Request,
    current_user: User | None,
    session: AsyncSession,
    room_service: RoomService,
) -> ExitResponse:
    """
    Validate, persist, and mirror-to-memory a single directed room exit (admin only).

    Writes exactly one room_links row for the given direction -- never synthesizes a reverse
    exit (a two-way corridor is two calls, one per direction; see #627).

    Raises:
        LoggedHTTPException: 404 (room/target not found), 409 (exit already exists), or 500.
    """
    try:
        validate_admin_room_action(current_user, room_id, request, AdminAction.CREATE_ROOM_EXIT)

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
