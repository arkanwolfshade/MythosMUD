"""
PlayerSkill model: per-character skill values.

Links a player to a skill with a value (0-100). Plan 4.3.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy model data class

from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player
    from .skill import Skill


class PlayerSkill(Base):
    """
    Per-character skill value (player_id, skill_id, value).

    Created at character creation via SkillService.set_player_skills;
    updated on level-up improvement (plan 4.5).
    """

    __tablename__ = "player_skills"
    __table_args__ = {"extend_existing": True}

    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    skill_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("skills.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    value: Mapped[int] = mapped_column(Integer(), nullable=False)

    player: Mapped[Player] = relationship("Player", back_populates="player_skills")
    skill: Mapped[Skill] = relationship("Skill", back_populates="player_skills", lazy="joined")

    def __repr__(self) -> str:
        return f"<PlayerSkill(player_id={self.player_id!r}, skill_id={self.skill_id}, value={self.value})>"
