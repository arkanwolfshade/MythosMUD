"""
Pydantic schemas for Player model.

This module defines Pydantic schemas for player creation, reading,
and updating operations.
"""

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from ...models.game import InventoryItem, PositionState, Stats, StatusEffect
from .class_definition import ClassDefinition


class PlayerBase(BaseModel):
    """Base player schema with common fields."""

    __slots__ = ()  # Performance optimization

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    name: str = Field(..., min_length=1, max_length=50, description="Player name")
    current_room_id: str = Field(default="earth_arkhamcity_sanitarium_room_foyer_001", description="Current room ID")
    experience_points: int = Field(default=0, ge=0, description="Experience points")
    level: int = Field(default=1, ge=1, description="Player level")


class PlayerCreate(PlayerBase):
    """Schema for creating a new player."""

    __slots__ = ()  # Performance optimization

    user_id: uuid.UUID = Field(..., description="Associated user ID")
    stats: Stats = Field(default_factory=Stats, description="Player stats")
    inventory: list[InventoryItem] = Field(default_factory=list, description="Player inventory")
    status_effects: list[StatusEffect] = Field(default_factory=list, description="Player status effects")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        json_schema_extra={
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "ProfessorWolfshade",
                "current_room_id": "earth_arkhamcity_northside_intersection_derby_high",
                "experience_points": 0,
                "level": 1,
                "stats": {"health": 100, "lucidity": 100, "strength": 50},
                "inventory": [],
                "status_effects": [],
            }
        },
    )


class PlayerRead(PlayerBase):
    """Schema for reading player data."""

    __slots__ = ()  # Performance optimization

    id: uuid.UUID = Field(..., description="Player's unique identifier")
    user_id: uuid.UUID = Field(..., description="Associated user ID")
    profession_id: int = Field(default=0, description="Player's profession ID")
    profession_name: str | None = Field(default=None, description="Player's profession name")
    profession_description: str | None = Field(default=None, description="Player's profession description")
    profession_flavor_text: str | None = Field(default=None, description="Player's profession flavor text")
    stats: Stats = Field(..., description="Player stats")
    inventory: list[InventoryItem] = Field(..., description="Player inventory")
    status_effects: list[StatusEffect] = Field(..., description="Player status effects")
    created_at: datetime = Field(..., description="Player creation timestamp")
    last_active: datetime = Field(..., description="Player last active timestamp")
    is_admin: bool = Field(default=False, description="Whether player has admin privileges")
    in_combat: bool = Field(default=False, description="Whether player is currently in combat")
    position: PositionState = Field(default=PositionState.STANDING, description="Current body posture")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        from_attributes=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "ProfessorWolfshade",
                "profession_id": 0,
                "profession_name": "Tramp",
                "profession_description": "A wandering soul with no particular skills or connections.",
                "profession_flavor_text": "You have spent your days drifting from place to place, learning to survive on your wits alone.",
                "current_room_id": "earth_arkhamcity_northside_intersection_derby_high",
                "experience_points": 150,
                "level": 2,
                "stats": {"health": 95, "lucidity": 88, "strength": 12},
                "inventory": [{"id": "sword", "name": "Rusty Sword"}],
                "status_effects": [{"type": "poison", "duration": 5}],
                "created_at": "2024-01-01T00:00:00Z",
                "last_active": "2024-01-01T12:00:00Z",
            }
        },
    )


class CharacterInfo(BaseModel):
    """Schema for character information in login response.

    MULTI-CHARACTER: Lightweight character info for character selection screen.
    """

    __slots__ = ()  # Performance optimization

    player_id: str = Field(..., description="Character ID (player_id)")
    name: str = Field(..., description="Character name")
    profession_id: int = Field(default=0, description="Profession ID")
    profession_name: str | None = Field(default=None, description="Profession name")
    level: int = Field(default=1, description="Character level")
    created_at: datetime = Field(..., description="Character creation timestamp")
    last_active: datetime = Field(..., description="Character last active timestamp")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        from_attributes=True,
    )


class PlayerUpdate(BaseModel):
    """Schema for updating player data."""

    __slots__ = ()  # Performance optimization

    name: str | None = Field(None, min_length=1, max_length=50, description="Player name")
    current_room_id: str | None = Field(None, description="Current room ID")
    experience_points: int | None = Field(None, ge=0, description="Experience points")
    level: int | None = Field(None, ge=1, description="Player level")
    stats: Stats | None = Field(None, description="Player stats")
    inventory: list[InventoryItem] | None = Field(None, description="Player inventory")
    status_effects: list[StatusEffect] | None = Field(None, description="Player status effects")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        json_schema_extra={
            "example": {
                "name": "NewPlayerName",
                "current_room_id": "arkham_002",
                "experience_points": 200,
                "level": 3,
                "stats": {"health": 100, "lucidity": 90, "strength": 15},
                "inventory": [{"id": "potion", "name": "Health Potion"}],
                "status_effects": [],
            }
        },
    )


class AvailableClassesResponse(BaseModel):
    """Response model for available character classes endpoint."""

    classes: dict[str, ClassDefinition] = Field(
        ..., description="Dictionary of class names to their prerequisites and descriptions"
    )
    stat_range: dict[str, int] = Field(..., description="Stat range information (min and max values)")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        json_schema_extra={
            "example": {
                "classes": {
                    "investigator": {
                        "prerequisites": {"int": 12},
                        "description": "A skilled researcher and detective",
                    }
                },
                "stat_range": {"min": 3, "max": 18},
            }
        },
    )


class MessageResponse(BaseModel):
    """Generic response model for operations that return a simple message."""

    message: str = Field(..., description="Success or status message")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        json_schema_extra={
            "example": {
                "message": "Operation completed successfully",
            }
        },
    )


class DeleteCharacterResponse(BaseModel):
    """Response model for character deletion."""

    success: bool = Field(..., description="Whether deletion was successful")
    message: str = Field(..., description="Deletion result message")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Character deleted successfully",
            }
        },
    )


class LoginGracePeriodResponse(BaseModel):
    """Response model for login grace period operations."""

    success: bool = Field(..., description="Whether operation was successful")
    message: str = Field(..., description="Status message")
    grace_period_active: bool = Field(..., description="Whether grace period is currently active")
    grace_period_remaining: float = Field(..., description="Remaining grace period time in seconds")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Login grace period started",
                "grace_period_active": True,
                "grace_period_remaining": 10.0,
            }
        },
    )


__all__ = [
    "PlayerBase",
    "PlayerCreate",
    "PlayerRead",
    "PlayerUpdate",
    "CharacterInfo",
    "AvailableClassesResponse",
    "MessageResponse",
    "DeleteCharacterResponse",
    "LoginGracePeriodResponse",
    "PositionState",
]
