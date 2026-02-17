"""
Player effect model for the effects system (ADR-009).

Persistent, tick-based status effects stored in a separate player_effects table.
"""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player


class PlayerEffect(Base):
    """
    Persistent player effect (status effect) with tick-based duration.

    Table: player_effects. Per ADR-009: separate table, duration and applied_at_tick
    for remaining = duration - (current_tick - applied_at_tick).
    """

    __tablename__ = "player_effects"
    __table_args__ = {"extend_existing": True}

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        primary_key=True,
        default=lambda: str(uuid4()),
    )
    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    effect_type: Mapped[str] = mapped_column(String(length=64), nullable=False, index=True)
    category: Mapped[str] = mapped_column(String(length=64), nullable=False, index=True)
    duration: Mapped[int] = mapped_column(Integer, nullable=False)  # ticks
    applied_at_tick: Mapped[int] = mapped_column(Integer, nullable=False)
    intensity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    source: Mapped[str | None] = mapped_column(String(length=128), nullable=True)
    visibility_level: Mapped[str] = mapped_column(String(length=32), nullable=False, default="visible")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        insert_default=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime
        nullable=False,
    )

    # Relationship back to Player
    player: Mapped["Player"] = relationship("Player", back_populates="player_effects")
