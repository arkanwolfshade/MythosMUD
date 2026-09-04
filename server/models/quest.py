"""
Quest subsystem models: quest_definitions, quest_instances, quest_offers.

Maps to Alembic migration 2026_02_19_add_quest_tables.
"""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy model data classes

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Text, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class QuestDefinition(Base):
    """Quest template: id (PK), definition JSONB, timestamps."""

    __tablename__ = "quest_definitions"
    __table_args__ = {"extend_existing": True}

    id: Mapped[str] = mapped_column(Text, primary_key=True, nullable=False)
    definition: Mapped[dict[str, Any]] = mapped_column(
        MutableDict.as_mutable(JSONB),
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),  # PostgreSQL now(); avoids func.now() type-checker false positive
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),  # PostgreSQL now(); avoids func.now() type-checker false positive
        onupdate=lambda: datetime.now(UTC),
    )


class QuestInstance(Base):
    """Per-character quest state: one row per player per quest."""

    __tablename__ = "quest_instances"
    __table_args__ = {"extend_existing": True}

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    player_id: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    quest_id: Mapped[str] = mapped_column(
        Text,
        ForeignKey("quest_definitions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    state: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    progress: Mapped[dict[str, Any]] = mapped_column(
        MutableDict.as_mutable(JSONB),
        nullable=False,
        default=dict,
        server_default="{}",
    )
    accepted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),  # PostgreSQL now(); avoids func.now() type-checker false positive
    )
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )


class QuestOffer(Base):
    """Junction: links a quest to an NPC or room that offers it."""

    __tablename__ = "quest_offers"
    __table_args__ = {"extend_existing": True}

    quest_id: Mapped[str] = mapped_column(
        Text,
        ForeignKey("quest_definitions.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    offer_entity_type: Mapped[str] = mapped_column(Text, primary_key=True, nullable=False)
    offer_entity_id: Mapped[str] = mapped_column(Text, primary_key=True, nullable=False)
