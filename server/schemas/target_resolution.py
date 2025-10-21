"""
Target resolution schemas for MythosMUD.

This module defines Pydantic models for target resolution results,
supporting both player and NPC targets with proper validation.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class TargetType(str, Enum):
    """Enumeration of possible target types."""

    PLAYER = "player"
    NPC = "npc"


class TargetMatch(BaseModel):
    """
    Represents a single target match.

    This model contains information about a potential target
    that matches the search criteria.
    """

    target_id: str = Field(..., description="Unique identifier for the target")
    target_name: str = Field(..., description="Display name of the target")
    target_type: TargetType = Field(..., description="Type of target (player or NPC)")
    room_id: str = Field(..., description="Room ID where the target is located")
    disambiguation_suffix: str | None = Field(
        None, description="Suffix for disambiguation (e.g., '-1', '-2') when multiple targets have same name"
    )
    metadata: dict[str, Any] = Field(default_factory=dict, description="Additional metadata about the target")


class TargetResolutionResult(BaseModel):
    """
    Result of target resolution operation.

    This model contains the complete result of a target resolution
    operation, including success status, matches, and error information.
    """

    success: bool = Field(..., description="Whether the resolution was successful")
    matches: list[TargetMatch] = Field(default_factory=list, description="List of matching targets found")
    error_message: str | None = Field(None, description="Error message if resolution failed")
    disambiguation_required: bool = Field(
        False, description="Whether disambiguation is required due to multiple matches"
    )
    search_term: str = Field(..., description="The original search term used")
    room_id: str = Field(..., description="Room ID where the search was performed")

    def get_single_match(self) -> TargetMatch | None:
        """Get the single match if exactly one target was found."""
        if self.success and len(self.matches) == 1:
            return self.matches[0]
        return None

    def get_disambiguation_list(self) -> list[str]:
        """Get list of disambiguation options for multiple matches."""
        if not self.disambiguation_required:
            return []

        options = []
        for match in self.matches:
            if match.disambiguation_suffix:
                options.append(f"{match.target_name}{match.disambiguation_suffix}")
            else:
                options.append(match.target_name)
        return options
