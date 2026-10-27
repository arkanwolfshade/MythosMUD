"""
Player effect model for the effects system (ADR-019, ADR-029 step 3b-i).

Every player status effect is a row in player_effects: the login ward, spell effects, and the tick-driven effects
(heal/damage over time, the lucidity drain), whose parameters and mutable state live in ``payload``.
"""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player


class PlayerEffect(Base):
    """
    Persistent player effect (status effect).

    Table: player_effects. ``remaining_seconds`` counts game seconds left, ticked down only while the player is online
    (NULL = until removed). ``instance_scoped`` effects are cleared when the player's instance is lost.
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
    remaining_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)
    payload: Mapped[dict[str, object]] = mapped_column(JSONB, nullable=False, default=dict)
    instance_scoped: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
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
