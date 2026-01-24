"""
Profession model for game data.

This module defines the Profession model that stores profession data
including requirements, effects, and availability status.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

import json
from typing import Any, cast

from sqlalchemy import BigInteger, Boolean, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Profession(Base):
    """
    Profession model for game data.

    Stores profession information including name, description, flavor text,
    stat requirements, mechanical effects, and availability status.
    """

    __tablename__ = "professions"
    __table_args__ = (
        Index("idx_professions_available", "is_available"),
        {"extend_existing": True},
    )

    # Primary key
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    # Profession information
    name: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)
    flavor_text: Mapped[str] = mapped_column(Text(), nullable=False)

    # Game mechanics stored as JSON in TEXT fields
    stat_requirements: Mapped[str] = mapped_column(Text(), nullable=False, default="{}")
    mechanical_effects: Mapped[str] = mapped_column(Text(), nullable=False, default="{}")

    # Availability status
    is_available: Mapped[bool] = mapped_column(Boolean(), default=True, nullable=False)

    def __repr__(self) -> str:
        """String representation of the profession."""
        return f"<Profession(id={self.id}, name='{self.name}', is_available={self.is_available})>"

    def get_stat_requirements(self) -> dict[str, Any]:
        """Get profession stat requirements as dictionary."""
        try:
            return cast(dict[str, Any], json.loads(self.stat_requirements))
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_stat_requirements(self, requirements: dict[str, Any]) -> None:
        """Set profession stat requirements from dictionary."""
        self.stat_requirements = json.dumps(requirements)

    def get_mechanical_effects(self) -> dict[str, Any]:
        """Get profession mechanical effects as dictionary."""
        try:
            return cast(dict[str, Any], json.loads(self.mechanical_effects))
        except (json.JSONDecodeError, TypeError):
            return {}

    def set_mechanical_effects(self, effects: dict[str, Any]) -> None:
        """Set profession mechanical effects from dictionary."""
        self.mechanical_effects = json.dumps(effects)

    def meets_stat_requirements(self, stats: dict[str, int]) -> bool:
        """
        Check if given stats meet the profession requirements.

        Args:
            stats: Dictionary of stat names to values

        Returns:
            True if all requirements are met, False otherwise
        """
        requirements = self.get_stat_requirements()

        for stat_name, min_value in requirements.items():
            if stats.get(stat_name, 0) < min_value:
                return False

        return True

    def is_available_for_selection(self) -> bool:
        """Check if profession is available for player selection."""
        return bool(self.is_available)

    def get_requirement_display_text(self) -> str:
        """
        Get formatted text for displaying stat requirements.

        Returns:
            Formatted string like "Minimum: Strength 12, Intelligence 10" or "No requirements"
        """
        requirements = self.get_stat_requirements()

        if not requirements:
            return "No requirements"

        requirement_parts = []
        for stat_name, min_value in requirements.items():
            # Capitalize first letter of stat name
            formatted_stat = stat_name.capitalize()
            requirement_parts.append(f"{formatted_stat} {min_value}")

        return f"Minimum: {', '.join(requirement_parts)}"
