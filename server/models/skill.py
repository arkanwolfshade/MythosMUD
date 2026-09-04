"""
Skill model for the  skills catalog.

Defines the Skill model used for the skills table (character creation revamp 4.2).
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Boolean, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player_skill import PlayerSkill


class Skill(Base):
    """
    Skill catalog entry.

    id: primary key (identity).
    key: stable identifier (e.g. accounting, cthulhu_mythos).
    name: display name.
    description: optional description.
    base_value: base percentage 0-100 from CoC sheet; Own Language uses EDU at creation.
    allow_at_creation: if False, cannot be chosen in occupation/personal slots (e.g. Cthulhu Mythos).
    category: optional grouping (e.g. knowledge, interpersonal).
    """

    __tablename__ = "skills"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    key: Mapped[str] = mapped_column(String(80), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(Text(), nullable=False)
    description: Mapped[str | None] = mapped_column(Text(), nullable=True)
    base_value: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    allow_at_creation: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=True)
    category: Mapped[str | None] = mapped_column(Text(), nullable=True)

    player_skills: Mapped[list[PlayerSkill]] = relationship("PlayerSkill", back_populates="skill", lazy="noload")

    def __repr__(self) -> str:
        """String representation of the skill."""
        return (
            f"<Skill(id={self.id}, key='{self.key}', name='{self.name}', allow_at_creation={self.allow_at_creation})>"
        )
