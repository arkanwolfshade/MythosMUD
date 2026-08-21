"""
Request/response schemas for room editor write operations.

Covers PUT /rooms/{room_id} (property updates) and the exit (room_links) CRUD endpoints.
See #627 and .cursor/plans/room_editor_backend_apis.plan.md for the feature this backs.
"""

from pydantic import BaseModel, ConfigDict, Field

from ...models.command_base import Direction


class RoomUpdateRequest(BaseModel):
    """Request model for updating room properties (name, description, environment).

    All fields are optional; omitted fields are left unchanged. `environment: ""` clears the
    environment to unset (the client's "Not Set" option) -- the CHECK constraint on
    rooms.attributes->>'environment' permits NULL but not an empty string, so the API layer
    is responsible for that translation.
    """

    name: str | None = Field(default=None, description="New room name")
    description: str | None = Field(default=None, description="New room description")
    environment: str | None = Field(
        default=None,
        description="New environment value; omit to leave unchanged, '' to clear",
    )

    def environment_is_set(self) -> bool:
        """Return True if this request wants to change the environment field at all."""
        return "environment" in self.model_fields_set


class RoomUpdateResponse(BaseModel):
    """Response model for a successful room property update."""

    room_id: str = Field(..., description="Room ID that was updated")
    name: str | None = Field(default=None, description="Updated room name, if changed")
    description: str | None = Field(default=None, description="Updated room description, if changed")
    environment: str | None = Field(default=None, description="Updated environment, if changed")
    message: str = Field(..., description="Success message")


class ExitCreateRequest(BaseModel):
    """Request model for creating a single directed room exit."""

    direction: Direction = Field(..., description="Exit direction")
    target_room_id: str = Field(..., description="stable_id of the destination room")
    flags: list[str] | None = Field(default=None, description="Exit flags, e.g. ['one_way', 'hidden']")
    description: str | None = Field(default=None, description="Custom exit description")


class ExitUpdateRequest(BaseModel):
    """Request model for updating an existing room exit's target and/or metadata."""

    target_room_id: str | None = Field(default=None, description="New destination room stable_id")
    flags: list[str] | None = Field(default=None, description="Exit flags")
    description: str | None = Field(default=None, description="Custom exit description")


class ExitResponse(BaseModel):
    """Response model for a successful exit create/update/delete."""

    room_id: str = Field(..., description="Source room ID")
    direction: str = Field(..., description="Exit direction")
    target_room_id: str | None = Field(default=None, description="Destination room stable_id, when applicable")
    message: str = Field(..., description="Success message")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "direction": "north",
                "target_room_id": "earth_arkhamcity_sanitarium_room_hall_001",
                "message": "Exit created successfully",
            }
        }
    )


__all__ = [
    "ExitCreateRequest",
    "ExitResponse",
    "ExitUpdateRequest",
    "RoomUpdateRequest",
    "RoomUpdateResponse",
]
