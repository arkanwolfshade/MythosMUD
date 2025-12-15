"""
Player spell learning and mastery models.

This module contains SQLAlchemy models for tracking which spells players have learned
and their mastery level with each spell.
"""

from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player
    from .spell_db import SpellDB


class PlayerSpell(Base):
    """
    Model for tracking player spell learning and mastery.

    This table tracks which spells each player has learned, their mastery level,
    and casting statistics.
    """

    __tablename__ = "player_spells"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(
        UUID(as_uuid=False), ForeignKey("players.player_id", ondelete="CASCADE"), nullable=False, index=True
    )
    spell_id = Column(String(255), ForeignKey("spells.spell_id", ondelete="CASCADE"), nullable=False, index=True)
    mastery = Column(Integer, nullable=False, default=0, server_default=text("0"))
    learned_at = Column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    last_cast_at = Column(DateTime(timezone=True), nullable=True)
    times_cast = Column(Integer, nullable=False, default=0, server_default=text("0"))

    # Relationships
    player: Mapped["Player"] = relationship("Player", back_populates="spells")
    spell: Mapped["SpellDB"] = relationship("SpellDB", back_populates="player_spells")

    def __repr__(self) -> str:
        """String representation of PlayerSpell."""
        return f"<PlayerSpell(player_id={self.player_id}, spell_id={self.spell_id}, mastery={self.mastery})>"
