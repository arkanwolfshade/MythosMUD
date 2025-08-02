"""
Room management API endpoints for MythosMUD server.

This module handles all room-related API operations including
room information retrieval and room state management.
"""

from fastapi import APIRouter, Request

# Create room router
room_router = APIRouter(prefix="/rooms", tags=["rooms"])


@room_router.get("/{room_id}")
def get_room(room_id: str, request: Request = None):
    """Get room information by room ID."""
    persistence = request.app.state.persistence
    room = persistence.get_room(room_id)
    if not room:
        return {"error": "Room not found"}
    return room
