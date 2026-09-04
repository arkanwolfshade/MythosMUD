"""
Player spell learning and mastery models.

This module contains SQLAlchemy models for tracking which spells players have learned
and their mastery level with each spell.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

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

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("players.player_id", ondelete="CASCADE"), nullable=False, index=True
    )
    spell_id: Mapped[str] = mapped_column(
        String(255), ForeignKey("spells.spell_id", ondelete="CASCADE"), nullable=False, index=True
    )
    mastery: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))
    learned_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("NOW()"))
    last_cast_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    times_cast: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default=text("0"))

    # Relationships
    player: Mapped["Player"] = relationship("Player", back_populates="spells")
    spell: Mapped["SpellDB"] = relationship("SpellDB", back_populates="player_spells")

    def __repr__(self) -> str:
        """String representation of PlayerSpell."""
        return f"<PlayerSpell(player_id={self.player_id}, spell_id={self.spell_id}, mastery={self.mastery})>"
