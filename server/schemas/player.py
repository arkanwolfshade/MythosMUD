"""
Pydantic schemas for Player model.

This module defines Pydantic schemas for player creation, reading,
and updating operations.
"""

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class PlayerBase(BaseModel):
    """Base player schema with common fields."""

    name: str = Field(..., min_length=1, max_length=50, description="Player name")
    current_room_id: str = Field(
        default="earth_arkham_city_northside_intersection_derby_high", description="Current room ID"
    )
    experience_points: int = Field(default=0, ge=0, description="Experience points")
    level: int = Field(default=1, ge=1, description="Player level")


class PlayerCreate(PlayerBase):
    """Schema for creating a new player."""

    user_id: uuid.UUID = Field(..., description="Associated user ID")
    stats: dict[str, Any] = Field(default={"health": 100, "sanity": 100, "strength": 10}, description="Player stats")
    inventory: list[dict[str, Any]] = Field(default=[], description="Player inventory")
    status_effects: list[dict[str, Any]] = Field(default=[], description="Player status effects")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "ProfessorWolfshade",
                "current_room_id": "earth_arkham_city_northside_intersection_derby_high",
                "experience_points": 0,
                "level": 1,
                "stats": {"health": 100, "sanity": 100, "strength": 10},
                "inventory": [],
                "status_effects": [],
            }
        }
    )


class PlayerRead(PlayerBase):
    """Schema for reading player data."""

    id: uuid.UUID = Field(..., description="Player's unique identifier")
    user_id: uuid.UUID = Field(..., description="Associated user ID")
    stats: dict[str, Any] = Field(..., description="Player stats")
    inventory: list[dict[str, Any]] = Field(..., description="Player inventory")
    status_effects: list[dict[str, Any]] = Field(..., description="Player status effects")
    created_at: datetime = Field(..., description="Player creation timestamp")
    last_active: datetime = Field(..., description="Player last active timestamp")
    is_admin: bool = Field(default=False, description="Whether player has admin privileges")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "ProfessorWolfshade",
                "current_room_id": "earth_arkham_city_northside_intersection_derby_high",
                "experience_points": 150,
                "level": 2,
                "stats": {"health": 95, "sanity": 88, "strength": 12},
                "inventory": [{"id": "sword", "name": "Rusty Sword"}],
                "status_effects": [{"type": "poison", "duration": 5}],
                "created_at": "2024-01-01T00:00:00Z",
                "last_active": "2024-01-01T12:00:00Z",
            }
        },
    )


class PlayerUpdate(BaseModel):
    """Schema for updating player data."""

    name: str | None = Field(None, min_length=1, max_length=50, description="Player name")
    current_room_id: str | None = Field(None, description="Current room ID")
    experience_points: int | None = Field(None, ge=0, description="Experience points")
    level: int | None = Field(None, ge=1, description="Player level")
    stats: dict[str, Any] | None = Field(None, description="Player stats")
    inventory: list[dict[str, Any]] | None = Field(None, description="Player inventory")
    status_effects: list[dict[str, Any]] | None = Field(None, description="Player status effects")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "NewPlayerName",
                "current_room_id": "arkham_002",
                "experience_points": 200,
                "level": 3,
                "stats": {"health": 100, "sanity": 90, "strength": 15},
                "inventory": [{"id": "potion", "name": "Health Potion"}],
                "status_effects": [],
            }
        }
    )
