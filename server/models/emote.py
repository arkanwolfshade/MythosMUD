"""
SQLAlchemy models for emotes.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID

from .base import Base


class Emote(Base):
    """Predefined emote definitions."""

    __tablename__ = "emotes"

    id = Column(UUID(as_uuid=False), primary_key=True)
    stable_id = Column(Text, nullable=False, unique=True)
    self_message = Column(Text, nullable=False)
    other_message = Column(Text, nullable=False)


class EmoteAlias(Base):
    """Aliases for predefined emotes."""

    __tablename__ = "emote_aliases"

    emote_id = Column(UUID(as_uuid=False), ForeignKey("emotes.id", ondelete="CASCADE"), primary_key=True)
    alias = Column(Text, primary_key=True)
