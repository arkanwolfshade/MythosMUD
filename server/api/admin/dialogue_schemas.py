"""Admin dialogue definition schemas (#583)."""

# pylint: disable=too-few-public-methods  # Reason: Pydantic DTOs; fields are the API surface

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from ...schemas.dialogue import DialogueTree


class DialogueDefinitionCreate(BaseModel):
    """Create or upsert body for a dialogue tree."""

    id: str = Field(min_length=1, max_length=128)
    definition: DialogueTree
    npc_definition_id: int | None = None


class DialogueDefinitionUpdate(BaseModel):
    """Partial update; id comes from path."""

    definition: DialogueTree
    npc_definition_id: int | None = None


class DialogueDefinitionResponse(BaseModel):
    """API response for a stored dialogue definition."""

    id: str
    definition: dict[str, Any]
    npc_definition_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = {"from_attributes": True}
