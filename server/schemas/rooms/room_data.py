"""
Room data schema for MythosMUD.

This module defines Pydantic models for room data structures used in API responses.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class RoomData(BaseModel):
    """
    Room data structure for API responses.

    This model represents room information with core required fields,
    while allowing additional dynamic fields for flexibility.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic room data (containers, players, npcs, etc.)
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    id: str = Field(..., description="Room identifier")
    name: str = Field(..., description="Room name")
    description: str = Field(..., description="Room description")
    plane: str | None = Field(default=None, description="Plane name")
    zone: str | None = Field(default=None, description="Zone name")
    sub_zone: str | None = Field(default=None, description="Sub-zone name")
    environment: str | None = Field(default=None, description="Environment type")
    exits: dict[str, str | None] = Field(default_factory=dict, description="Room exits mapping direction to room ID")
    containers: list[Any] | None = Field(default=None, description="Containers in the room")
    players: list[Any] | None = Field(default=None, description="Players in the room")
    objects: list[Any] | None = Field(default=None, description="Objects in the room")
    npcs: list[Any] | None = Field(default=None, description="NPCs in the room")
    occupant_count: int | None = Field(default=None, description="Total occupant count")
    map_x: float | None = Field(default=None, description="Map X coordinate")
    map_y: float | None = Field(default=None, description="Map Y coordinate")
