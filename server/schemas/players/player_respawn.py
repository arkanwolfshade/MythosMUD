"""
Player respawn API response schemas for MythosMUD server.

This module provides Pydantic models for player respawn-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class RespawnPlayerData(BaseModel):
    """Simplified player data returned in respawn responses."""

    id: str = Field(..., description="Player UUID")
    name: str = Field(..., description="Player name")
    dp: int = Field(..., description="Current damage points")
    max_dp: int = Field(..., description="Maximum damage points")
    current_room_id: str = Field(..., description="Current room ID after respawn")
    lucidity: int | None = Field(default=None, description="Current lucidity (for delirium respawn)")


class RespawnResponse(BaseModel):
    """Response model for player respawn endpoints."""

    success: bool = Field(..., description="Whether respawn was successful")
    player: RespawnPlayerData = Field(..., description="Updated player data after respawn")
    room: dict[str, Any] = Field(..., description="Room data for the respawn location")
    message: str = Field(..., description="Respawn message for the player")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "player": {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Test Player",
                    "dp": 100,
                    "max_dp": 100,
                    "current_room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                    "lucidity": 10,
                },
                "room": {
                    "id": "earth_arkhamcity_sanitarium_room_foyer_001",
                    "name": "Sanitarium Foyer",
                    "description": "A clean, sterile room...",
                },
                "message": "You have been restored to lucidity and returned to the Sanitarium",
            }
        }
    )
