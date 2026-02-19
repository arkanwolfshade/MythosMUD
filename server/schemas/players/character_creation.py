"""
Character creation API response schemas for MythosMUD server.

This module provides Pydantic models for character creation-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from pydantic import BaseModel, ConfigDict, Field

from .player import PlayerRead
from .stat_values import RolledStats


class StatSummary(BaseModel):
    """Summary of rolled character stats."""

    total: int = Field(..., description="Total stat points")
    average: float = Field(..., description="Average stat value")
    highest: int = Field(..., description="Highest stat value")
    lowest: int = Field(..., description="Lowest stat value")


class RollStatsResponse(BaseModel):
    """Response model for rolling character stats."""

    stats: RolledStats = Field(..., description="Rolled character stats (send these on create-character)")
    stat_summary: StatSummary = Field(..., description="Summary of the rolled stats")
    profession_id: int | None = Field(default=None, description="Profession ID (if profession-based rolling)")
    stats_with_profession_modifiers: RolledStats | None = Field(
        default=None,
        description="Rolled stats with profession stat_modifiers applied (preview only)",
    )
    available_classes: list[str] | None = Field(default=None, description="Available classes (if class-based rolling)")
    meets_requirements: bool | None = Field(default=None, description="Whether stats meet profession requirements")
    meets_class_requirements: bool | None = Field(default=None, description="Whether stats meet class requirements")
    method_used: str = Field(..., description="Stats rolling method used")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "stats": {"str": 12, "int": 14, "con": 13},
                "stat_summary": {"total": 39, "average": 13.0, "highest": 14, "lowest": 12},
                "profession_id": 1,
                "meets_requirements": True,
                "method_used": "standard",
            }
        }
    )


class CreateCharacterResponse(BaseModel):
    """Response model for character creation."""

    player: PlayerRead = Field(..., description="Created player character data")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "player": {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Test Character",
                    "stats": {"str": 12, "int": 14},
                }
            }
        }
    )


class ValidateStatsResponse(BaseModel):
    """Response model for stats validation."""

    meets_prerequisites: bool | None = Field(
        default=None, description="Whether stats meet class prerequisites (if class_name provided)"
    )
    failed_requirements: list[str] = Field(default_factory=list, description="List of failed requirements")
    available_classes: list[str] = Field(default_factory=list, description="List of available classes for these stats")
    requested_class: str | None = Field(default=None, description="Requested class name (if class_name provided)")
    stat_summary: StatSummary | None = Field(default=None, description="Stat summary (if no class_name provided)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "meets_prerequisites": True,
                "failed_requirements": [],
                "available_classes": ["investigator", "scholar"],
                "requested_class": "investigator",
            }
        }
    )
