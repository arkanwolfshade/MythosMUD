"""
SkillUseLog model: log of successful skill use per character at level (plan 4.5).

Used for CoC-style improvement rolls on level-up.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy model data class

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    pass


class SkillUseLog(Base):
    """
    One recorded successful use of a skill by a character at a given level.

    character_level_at_use is the character's level when the skill was used;
    used for run_improvement_rolls(level = previous level) on level-up.
    """

    __tablename__ = "skill_use_log"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    player_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
    )
    skill_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("skills.id", ondelete="CASCADE"),
        nullable=False,
    )
    character_level_at_use: Mapped[int] = mapped_column(Integer, nullable=False)
    used_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), nullable=False)

    def __repr__(self) -> str:
        return (
            f"<SkillUseLog(id={self.id}, player_id={self.player_id!r}, skill_id={self.skill_id}, "
            f"level={self.character_level_at_use})>"
        )
