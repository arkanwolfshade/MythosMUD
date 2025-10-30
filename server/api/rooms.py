"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

from typing import Any
from fastapi import APIRouter, Request

from ..dependencies import RoomServiceDep
from ..exceptions import LoggedHTTPException
from ..game.room_service import RoomService
from ..logging.enhanced_logging_config import get_logger
from ..utils.error_logging import create_context_from_request

logger = get_logger(__name__)

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])

logger.info("Rooms API router initialized", prefix="/rooms")


@room_router.get("/{room_id}")  # type: ignore[misc]
async def get_room(room_id: str, request: Request = None, room_service: RoomService = RoomServiceDep) -> dict[str, Any]:
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
