"""
Container API request/response models.

Pydantic models for container API endpoints, defining the structure
of requests and responses for container operations.
"""

from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field, field_validator


class OpenContainerRequest(BaseModel):
    """Request model for opening a container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container to open")


class TransferContainerRequest(BaseModel):
    """Request model for transferring items to/from container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container")
    mutation_token: str = Field(..., description="Mutation token from open_container")
    direction: str = Field(..., description="Transfer direction: 'to_container' or 'to_player'")
    stack: dict[str, Any] = Field(..., description="Item stack to transfer")
    quantity: int = Field(..., ge=1, description="Quantity to transfer")

    @field_validator("direction")
    @classmethod
    def validate_direction(cls, v: str) -> str:
        """Validate transfer direction."""
        if v not in ("to_container", "to_player"):
            raise ValueError("direction must be 'to_container' or 'to_player'")
        return v


class CloseContainerRequest(BaseModel):
    """Request model for closing a container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container to close")
    mutation_token: str = Field(..., description="Mutation token from open_container")


class LootAllRequest(BaseModel):
    """Request model for looting all items from a container."""

    __slots__ = ()  # Performance optimization

    container_id: UUID = Field(..., description="UUID of the container")
    mutation_token: str = Field(..., description="Mutation token from open_container")
