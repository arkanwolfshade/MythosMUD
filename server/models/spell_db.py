"""
SQLAlchemy database model for spells table.

This module contains the SQLAlchemy ORM model for the spells table,
separate from the Pydantic Spell model used for validation.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, Integer, String, Text, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from .player_spells import PlayerSpell


class SpellDB(Base):
    """
    SQLAlchemy model for the spells table.

    This is the database representation of spells, separate from the
    Pydantic Spell model used for validation and business logic.
    """

    __tablename__ = "spells"
    __table_args__ = {"extend_existing": True}

    spell_id = Column(String(255), primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    school = Column(String(50), nullable=False)
    mp_cost = Column(Integer, nullable=False)
    lucidity_cost = Column(Integer, nullable=False, default=0, server_default=text("0"))
    corruption_on_learn = Column(Integer, nullable=False, default=0, server_default=text("0"))
    corruption_on_cast = Column(Integer, nullable=False, default=0, server_default=text("0"))
    casting_time_seconds = Column(Integer, nullable=False, default=0, server_default=text("0"))
    target_type = Column(String(50), nullable=False)
    range_type = Column(String(50), nullable=False)
    effect_type = Column(String(50), nullable=False)
    effect_data = Column(JSONB, nullable=False, default={}, server_default=text("'{}'::jsonb"))
    materials = Column(JSONB, nullable=False, default=[], server_default=text("'[]'::jsonb"))
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))

    # Relationships
    player_spells: Mapped[list["PlayerSpell"]] = relationship("PlayerSpell", back_populates="spell")

    def __repr__(self) -> str:
        """String representation of SpellDB."""
        return f"<SpellDB(spell_id={self.spell_id}, name={self.name}, school={self.school})>"
