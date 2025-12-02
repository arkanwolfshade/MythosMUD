"""Lucidity tracking models drawn from the Pnakotic Manuscripts."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player


def _utc_now() -> datetime:
    """Return naive UTC timestamps for PostgreSQL TIMESTAMP WITHOUT TIME ZONE compatibility."""
    return datetime.now(UTC).replace(tzinfo=None)


class PlayerLucidity(Base):
    """Authoritative lucidity state for a single investigator."""

    __tablename__ = "player_lucidity"
    __table_args__ = (
        CheckConstraint("current_lcd BETWEEN -100 AND 100", name="ck_player_lucidity_range"),
        CheckConstraint(
            "current_tier IN ('lucid','uneasy','fractured','deranged','catatonic')",
            name="ck_player_lucidity_tier",
        ),
        Index("idx_player_lucidity_tier", "current_tier"),
    )

    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        primary_key=True,
    )
    current_lcd: Mapped[int] = mapped_column(Integer(), nullable=False, default=100)
    current_tier: Mapped[str] = mapped_column(String(length=32), nullable=False, default="lucid")
    liabilities: Mapped[str] = mapped_column(Text(), nullable=False, default="[]")
    last_updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)
    catatonia_entered_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity",
        uselist=False,
    )


class LucidityAdjustmentLog(Base):
    """Immutable ledger for every lucidity gain or loss event."""

    __tablename__ = "lucidity_adjustment_log"
    __table_args__ = (Index("idx_lucidity_adjustment_player_created", "player_id", "created_at"),)

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    delta: Mapped[int] = mapped_column(Integer(), nullable=False)
    reason_code: Mapped[str] = mapped_column(String(length=64), nullable=False)
    metadata_payload: Mapped[str] = mapped_column("metadata", Text(), nullable=False, default="{}")
    location_id: Mapped[str | None] = mapped_column(String(length=255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity_adjustments",
    )


class LucidityExposureState(Base):
    """Tracks repeated exposure to particular eldritch archetypes."""

    __tablename__ = "lucidity_exposure_state"
    __table_args__ = (UniqueConstraint("player_id", "entity_archetype", name="uq_lucidity_exposure_player_archetype"),)

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    entity_archetype: Mapped[str] = mapped_column(String(length=128), nullable=False)
    encounter_count: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    last_encounter_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity_exposures",
    )


class LucidityCooldown(Base):
    """Cooldown tracker for recovery rituals and hallucination timers."""

    __tablename__ = "lucidity_cooldowns"
    __table_args__ = (UniqueConstraint("player_id", "action_code", name="uq_lucidity_cooldown_player_action"),)

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    action_code: Mapped[str] = mapped_column(String(length=64), nullable=False)
    cooldown_expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity_cooldowns",
    )
