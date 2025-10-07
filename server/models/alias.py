"""
Alias model for command aliases.

This module defines the Alias model for storing player command aliases.
"""

import uuid
from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


class Alias(BaseModel):
    """
    Alias model for command aliases.

    Stores player command aliases for quick access to frequently used commands.
    """

    __slots__ = ()  # Performance optimization for frequently instantiated aliases

    model_config = ConfigDict(
        # Security: reject unknown fields to prevent injection
        extra="forbid",
        # Validate assignment
        validate_assignment=True,
    )

    id: str = Field(default_factory=lambda: str(uuid.uuid4()), description="Alias unique identifier")
    name: str = Field(..., description="Alias name")
    command: str = Field(..., description="Command to execute")
    # Store naive UTC to keep JSON/Z formatting stable while avoiding utcnow deprecation
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC).replace(tzinfo=None), description="Creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC).replace(tzinfo=None), description="Last update timestamp"
    )

    def __repr__(self) -> str:
        """String representation of the alias."""
        return f"<Alias(id={self.id}, name={self.name}, command={self.command})>"

    def model_dump(self) -> dict:
        """Convert alias to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "command": self.command,
            "created_at": self.created_at.isoformat() + "Z",
            "updated_at": self.updated_at.isoformat() + "Z",
        }
