"""
Skill catalog API response schemas.

Used by GET /v1/skills (or equivalent) for character creation revamp 4.2.
"""

from pydantic import BaseModel, ConfigDict, Field


class SkillData(BaseModel):
    """Single skill catalog entry."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    id: int = Field(..., description="Skill primary key")
    key: str = Field(..., description="Stable identifier (e.g. accounting, cthulhu_mythos)")
    name: str = Field(..., description="Display name")
    description: str | None = Field(default=None, description="Optional description")
    base_value: int = Field(..., description="Base percentage 0-100 from CoC sheet")
    allow_at_creation: bool = Field(
        ...,
        description="If false, cannot be chosen in occupation/personal slots (e.g. Cthulhu Mythos)",
    )
    category: str | None = Field(default=None, description="Optional category for UI grouping")


class SkillListResponse(BaseModel):
    """Response model for skills catalog list."""

    skills: list[SkillData] = Field(..., description="List of skills in the catalog")

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )


class PlayerSkillEntry(BaseModel):
    """Single player skill (character creation revamp 4.3)."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True, validate_default=True)

    skill_id: int = Field(..., description="Skill catalog id")
    skill_key: str = Field(..., description="Skill key (e.g. accounting)")
    skill_name: str = Field(..., description="Display name")
    value: int = Field(..., description="Current percentage 0-99")


class PlayerSkillsResponse(BaseModel):
    """Response for GET /v1/api/players/{player_id}/skills."""

    skills: list[PlayerSkillEntry] = Field(..., description="That character's skills")

    model_config = ConfigDict(extra="forbid", validate_assignment=True, validate_default=True)
