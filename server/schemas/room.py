"""
Room API response schemas for MythosMUD server.

This module provides Pydantic models for room-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

# Room data is dynamic, so we use dict[str, Any] directly for the response
# This matches the structure returned by room_service.get_room()
# The response model will be dict[str, Any] with proper typing


class RoomListResponse(BaseModel):
    """Response model for listing rooms."""

    rooms: list[dict[str, Any]] = Field(..., description="List of room data dictionaries")
    total: int = Field(..., description="Total number of rooms returned")
    plane: str = Field(..., description="Plane name used for filtering")
    zone: str = Field(..., description="Zone name used for filtering")
    sub_zone: str | None = Field(default=None, description="Sub-zone name used for filtering (if any)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "rooms": [
                    {
                        "id": "earth_arkhamcity_sanitarium_room_foyer_001",
                        "name": "Sanitarium Foyer",
                        "description": "A dimly lit entrance hall...",
                    }
                ],
                "total": 1,
                "plane": "earth",
                "zone": "arkhamcity",
                "sub_zone": "sanitarium",
            }
        }
    )


class RoomPositionUpdateResponse(BaseModel):
    """Response model for updating room position."""

    room_id: str = Field(..., description="Room ID that was updated")
    map_x: float = Field(..., description="Updated X coordinate")
    map_y: float = Field(..., description="Updated Y coordinate")
    message: str = Field(..., description="Success message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "map_x": 100.5,
                "map_y": 200.3,
                "message": "Room position updated successfully",
            }
        }
    )


class RoomResponse(BaseModel):
    """Response model for single room information.

    This model uses a flexible structure to accommodate dynamic room data
    returned by the room service, which may include various fields depending
    on the room type and configuration.
    """

    model_config = ConfigDict(extra="allow", json_schema_extra={"example": {"id": "arkham_001", "name": "Arkham Room"}})
