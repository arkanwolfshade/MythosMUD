"""Lucidity tracking models drawn from the Pnakotic Manuscripts."""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import BigInteger, CheckConstraint, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint
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
    current_lcd: Mapped[int] = mapped_column(Integer(), nullable=False, default=lambda: 100)
    current_tier: Mapped[str] = mapped_column(String(length=32), nullable=False, default=lambda: "lucid")
    liabilities: Mapped[str] = mapped_column(Text(), nullable=False, default=lambda: "[]")
    last_updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)
    catatonia_entered_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity",
        uselist=False,
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize PlayerLucidity with defaults."""
        super().__init__(*args, **kwargs)
        # Apply defaults if not provided (SQLAlchemy may set to None initially)
        _sentinel = object()
        current_lcd_val = getattr(self, "current_lcd", _sentinel)
        if current_lcd_val is _sentinel or current_lcd_val is None:
            object.__setattr__(self, "current_lcd", 100)
        current_tier_val = getattr(self, "current_tier", _sentinel)
        if current_tier_val is _sentinel or current_tier_val is None:
            object.__setattr__(self, "current_tier", "lucid")
        liabilities_val = getattr(self, "liabilities", _sentinel)
        if liabilities_val is _sentinel or liabilities_val is None:
            object.__setattr__(self, "liabilities", "[]")
        last_updated_at_val = getattr(self, "last_updated_at", _sentinel)
        if last_updated_at_val is _sentinel or last_updated_at_val is None:
            object.__setattr__(self, "last_updated_at", _utc_now())


class LucidityAdjustmentLog(Base):
    """Immutable ledger for every lucidity gain or loss event."""

    __tablename__ = "lucidity_adjustment_log"
    __table_args__ = (Index("idx_lucidity_adjustment_player_created", "player_id", "created_at"),)

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    delta: Mapped[int] = mapped_column(Integer(), nullable=False)
    reason_code: Mapped[str] = mapped_column(Text(), nullable=False)
    metadata_payload: Mapped[str] = mapped_column("metadata", Text(), nullable=False, default=lambda: "{}")
    location_id: Mapped[str | None] = mapped_column(String(length=255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity_adjustments",
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize LucidityAdjustmentLog with defaults."""
        super().__init__(*args, **kwargs)
        # Apply defaults if not provided (SQLAlchemy may set to None initially)
        _sentinel = object()
        metadata_payload_val = getattr(self, "metadata_payload", _sentinel)
        if metadata_payload_val is _sentinel or metadata_payload_val is None:
            object.__setattr__(self, "metadata_payload", "{}")
        created_at_val = getattr(self, "created_at", _sentinel)
        if created_at_val is _sentinel or created_at_val is None:
            object.__setattr__(self, "created_at", _utc_now())


class LucidityExposureState(Base):
    """Tracks repeated exposure to particular eldritch archetypes."""

    __tablename__ = "lucidity_exposure_state"
    __table_args__ = (UniqueConstraint("player_id", "entity_archetype", name="uq_lucidity_exposure_player_archetype"),)

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    entity_archetype: Mapped[str] = mapped_column(Text(), nullable=False)
    encounter_count: Mapped[int] = mapped_column(Integer(), nullable=False, default=lambda: 0)
    last_encounter_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity_exposures",
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize LucidityExposureState with defaults."""
        super().__init__(*args, **kwargs)
        # Apply defaults if not provided (SQLAlchemy may set to None initially)
        _sentinel = object()
        encounter_count_val = getattr(self, "encounter_count", _sentinel)
        if encounter_count_val is _sentinel or encounter_count_val is None:
            object.__setattr__(self, "encounter_count", 0)
        last_encounter_at_val = getattr(self, "last_encounter_at", _sentinel)
        if last_encounter_at_val is _sentinel or last_encounter_at_val is None:
            object.__setattr__(self, "last_encounter_at", _utc_now())


class LucidityCooldown(Base):
    """Cooldown tracker for recovery rituals and hallucination timers."""

    __tablename__ = "lucidity_cooldowns"
    __table_args__ = (UniqueConstraint("player_id", "action_code", name="uq_lucidity_cooldown_player_action"),)

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    action_code: Mapped[str] = mapped_column(Text(), nullable=False)
    cooldown_expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="lucidity_cooldowns",
    )
