"""Dialogue subsystem model: dialogue_definitions (NPC talk trees, #583)."""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy model data class

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from sqlalchemy import BigInteger, DateTime, ForeignKey, Text, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DialogueDefinition(Base):
    """NPC dialogue tree template: id (PK), definition JSONB, optional npc link."""

    __tablename__ = "dialogue_definitions"
    __table_args__ = {"extend_existing": True}

    id: Mapped[str] = mapped_column(Text, primary_key=True, nullable=False)
    definition: Mapped[dict[str, Any]] = mapped_column(
        MutableDict.as_mutable(JSONB),
        nullable=False,
    )
    npc_definition_id: Mapped[int | None] = mapped_column(
        BigInteger,
        ForeignKey("npc_definitions.id", ondelete="SET NULL"),
        nullable=True,
        unique=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=text("now()"),
        onupdate=lambda: datetime.now(UTC),
    )
