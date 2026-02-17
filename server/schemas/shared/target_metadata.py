"""
Target metadata schema for MythosMUD.

This module defines Pydantic models for target resolution metadata.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class TargetMetadata(BaseModel):
    """
    Metadata about a target in target resolution.

    This model represents additional information about a target that may be
    useful for disambiguation or context.
    """

    model_config = ConfigDict(
        extra="allow",  # Allow extra fields for dynamic metadata
        validate_assignment=True,
        str_strip_whitespace=True,
        validate_default=True,
    )

    # Common metadata fields (may not always be present)
    level: int | None = Field(default=None, description="Target level")
    profession: str | None = Field(default=None, description="Target profession")
    status: str | None = Field(default=None, description="Target status")
    additional_info: dict[str, Any] = Field(default_factory=dict, description="Additional metadata fields")
