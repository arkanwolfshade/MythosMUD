"""
Alias model for command aliases.

This module defines the Alias model for storing player command aliases.
"""

import uuid
from datetime import UTC, datetime
from typing import Any

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
    version: str = Field(default="1.0", description="Alias version for compatibility tracking")
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

    def __eq__(self, other: object) -> bool:
        """Check equality based on name and command."""
        if not isinstance(other, Alias):
            return False
        return self.name == other.name and self.command == other.command

    def __hash__(self) -> int:
        """Hash based on name and command for use in sets/dicts."""
        return hash((self.name, self.command))

    def update_timestamp(self) -> None:
        """Update the updated_at timestamp to current time."""
        object.__setattr__(self, "updated_at", datetime.now(UTC).replace(tzinfo=None))

    def is_reserved_command(self) -> bool:
        """Check if the alias name conflicts with a reserved command."""
        reserved_commands = {
            "help",
            "quit",
            "look",
            "inventory",
            "stats",
            "alias",
            "unalias",
            "who",
            "say",
            "tell",
            "whisper",
            "shout",
            "emote",
        }
        return self.name.lower() in reserved_commands

    def validate_name(self) -> bool:
        """Validate the alias name is not empty."""
        return bool(self.name and self.name.strip())

    def get_expanded_command(self, args: list[str] | None = None) -> str:
        """Get the expanded command with optional arguments appended."""
        # Current implementation: just return the command as-is
        # Future enhancement: could support argument substitution
        return self.command

    def model_dump(self, **kwargs) -> dict[str, Any]:
        """Convert alias to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "command": self.command,
            "version": self.version,
            "created_at": self.created_at.isoformat() + "Z",
            "updated_at": self.updated_at.isoformat() + "Z",
        }
