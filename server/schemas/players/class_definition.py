"""
Class definition schema for MythosMUD.

This module defines Pydantic models for character class definitions and prerequisites.
"""

from pydantic import BaseModel, ConfigDict, Field


class ClassDefinition(BaseModel):
    """
    Definition of a character class with prerequisites and description.

    This model represents the requirements and metadata for a character class,
    including stat prerequisites and descriptive text.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    prerequisites: dict[str, int] = Field(
        ..., description="Dictionary mapping attribute names to minimum required values"
    )
    description: str = Field(..., description="Description of the character class")
