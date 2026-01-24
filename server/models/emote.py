"""
SQLAlchemy models for emotes.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

from sqlalchemy import ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Emote(Base):
    """Predefined emote definitions."""

    __tablename__ = "emotes"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    stable_id: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    self_message: Mapped[str] = mapped_column(Text, nullable=False)
    other_message: Mapped[str] = mapped_column(Text, nullable=False)


class EmoteAlias(Base):
    """Aliases for predefined emotes."""

    __tablename__ = "emote_aliases"

    emote_id: Mapped[str] = mapped_column(
        UUID(as_uuid=False), ForeignKey("emotes.id", ondelete="CASCADE"), primary_key=True
    )
    alias: Mapped[str] = mapped_column(Text, primary_key=True)
