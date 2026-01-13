"""
Player effects API response schemas for MythosMUD server.

This module provides Pydantic models for player effect-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, ConfigDict, Field


class EffectResponse(BaseModel):
    """Response model for player effect endpoints (lucidity loss, fear, corruption, etc.)."""

    message: str = Field(..., description="Success message describing the effect applied")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Applied 5 lucidity loss to Player Name",
            }
        }
    )
