"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

from fastapi import APIRouter, HTTPException, Request

from ..game.room_service import RoomService

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])


@room_router.get("/{room_id}")
def get_room(room_id: str, request: Request = None):
    """Get room information by room ID."""
    persistence = request.app.state.persistence
    room_service = RoomService(persistence)

    room = room_service.get_room(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    return room
