"""
SQLAlchemy models for calendar data (holidays and NPC schedules).
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

from sqlalchemy import SmallInteger, String, Text, text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class HolidayModel(Base):
    """Mythos holidays tracker."""

    __tablename__ = "calendar_holidays"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    stable_id: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    tradition: Mapped[str] = mapped_column(Text, nullable=False)
    month: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    day: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    duration_hours: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    season: Mapped[str] = mapped_column(String(20), nullable=False)  # Enum handled as string for simplicity in tests
    bonus_tags: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False, server_default=text("'{}'::text[]"))


class NPCScheduleModel(Base):
    """Schedules for NPCs."""

    __tablename__ = "calendar_npc_schedules"

    id: Mapped[str] = mapped_column(UUID(as_uuid=False), primary_key=True)
    stable_id: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    category: Mapped[str] = mapped_column(Text, nullable=False)
    start_hour: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    end_hour: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    days: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False)
    applies_to: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False)
    effects: Mapped[list[str]] = mapped_column(ARRAY(Text), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
