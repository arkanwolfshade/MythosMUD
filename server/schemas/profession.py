"""
Profession API response schemas for MythosMUD server.

This module provides Pydantic models for profession-related API responses,
ensuring type safety and automatic OpenAPI documentation.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class StatRequirement(BaseModel):
    """Stat requirement for a profession."""

    stat: str = Field(..., description="Stat name (e.g., 'str', 'int', 'con')")
    minimum: int = Field(..., description="Minimum stat value required")


class MechanicalEffect(BaseModel):
    """Mechanical effect of a profession."""

    effect_type: str = Field(..., description="Type of mechanical effect")
    value: int | float = Field(..., description="Effect value")
    description: str | None = Field(default=None, description="Description of the effect")


class ProfessionData(BaseModel):
    """Profession data model."""

    id: int = Field(..., description="Profession ID")
    name: str = Field(..., description="Profession name")
    description: str = Field(..., description="Profession description")
    flavor_text: str | None = Field(default=None, description="Flavor text for the profession")
    stat_requirements: list[StatRequirement] = Field(default_factory=list, description="Stat requirements")
    mechanical_effects: list[MechanicalEffect] = Field(default_factory=list, description="Mechanical effects")
    is_available: bool = Field(..., description="Whether the profession is available for selection")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Investigator",
                "description": "A skilled investigator of the unknown",
                "flavor_text": "You have seen things that cannot be unseen...",
                "stat_requirements": [{"stat": "int", "minimum": 12}],
                "mechanical_effects": [
                    {"effect_type": "skill_bonus", "value": 5, "description": "+5 to investigation"}
                ],
                "is_available": True,
            }
        }
    )


class ProfessionListResponse(BaseModel):
    """Response model for listing all professions."""

    professions: list[ProfessionData] = Field(..., description="List of available professions")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "professions": [
                    {
                        "id": 1,
                        "name": "Investigator",
                        "description": "A skilled investigator",
                        "is_available": True,
                    }
                ]
            }
        }
    )


class ProfessionResponse(BaseModel):
    """Response model for a single profession."""

    id: int = Field(..., description="Profession ID")
    name: str = Field(..., description="Profession name")
    description: str = Field(..., description="Profession description")
    flavor_text: str | None = Field(default=None, description="Flavor text for the profession")
    stat_requirements: dict[str, Any] = Field(..., description="Stat requirements as dictionary")
    mechanical_effects: dict[str, Any] = Field(..., description="Mechanical effects as dictionary")
    is_available: bool = Field(..., description="Whether the profession is available for selection")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "name": "Investigator",
                "description": "A skilled investigator of the unknown",
                "flavor_text": "You have seen things that cannot be unseen...",
                "stat_requirements": {"int": 12},
                "mechanical_effects": {"skill_bonus": 5},
                "is_available": True,
            }
        }
    )
