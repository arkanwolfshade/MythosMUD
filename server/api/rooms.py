"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

from fastapi import APIRouter, HTTPException, Request

from ..game.room_service import RoomService
from ..logging_config import get_logger

logger = get_logger(__name__)

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])

logger.info("Rooms API router initialized", prefix="/rooms")


@room_router.get("/{room_id}")
def get_room(room_id: str, request: Request = None):
    """Get room information by room ID."""
    logger.debug("Room information requested", room_id=room_id)

    persistence = request.app.state.persistence
    room_service = RoomService(persistence)

    room = room_service.get_room(room_id)
    if not room:
        logger.warning("Room not found", room_id=room_id)
        raise HTTPException(status_code=404, detail="Room not found")

    logger.debug("Room information returned", room_id=room_id, room_name=room.get("name", "Unknown"))
    return room
