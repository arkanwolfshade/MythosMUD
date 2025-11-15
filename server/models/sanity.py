"""Sanity tracking models drawn from the Pnakotic Manuscripts."""

from __future__ import annotations

from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player


def _utc_now() -> datetime:
    """Return naive UTC timestamps for SQLite compatibility."""
    return datetime.now(UTC).replace(tzinfo=None)


class PlayerSanity(Base):
    """Authoritative sanity state for a single investigator."""

    __tablename__ = "player_sanity"
    __table_args__ = (
        CheckConstraint("current_san BETWEEN -100 AND 100", name="ck_player_sanity_range"),
        CheckConstraint(
            "current_tier IN ('lucid','uneasy','fractured','deranged','catatonic')",
            name="ck_player_sanity_tier",
        ),
        Index("idx_player_sanity_tier", "current_tier"),
    )

    player_id: Mapped[str] = mapped_column(
        String(length=255),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        primary_key=True,
    )
    current_san: Mapped[int] = mapped_column(Integer(), nullable=False, default=100)
    current_tier: Mapped[str] = mapped_column(String(length=32), nullable=False, default="lucid")
    liabilities: Mapped[str] = mapped_column(Text(), nullable=False, default="[]")
    last_updated_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)
    catatonia_entered_at: Mapped[datetime | None] = mapped_column(DateTime(), nullable=True)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="sanity",
        uselist=False,
    )


class SanityAdjustmentLog(Base):
    """Immutable ledger for every sanity gain or loss event."""

    __tablename__ = "sanity_adjustment_log"
    __table_args__ = (Index("idx_sanity_adjustment_player_created", "player_id", "created_at"),)

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    player_id: Mapped[str] = mapped_column(
        String(length=255),
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
        back_populates="sanity_adjustments",
    )


class SanityExposureState(Base):
    """Tracks repeated exposure to particular eldritch archetypes."""

    __tablename__ = "sanity_exposure_state"
    __table_args__ = (UniqueConstraint("player_id", "entity_archetype", name="uq_sanity_exposure_player_archetype"),)

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    player_id: Mapped[str] = mapped_column(
        String(length=255),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    entity_archetype: Mapped[str] = mapped_column(String(length=128), nullable=False)
    encounter_count: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    last_encounter_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False, default=_utc_now)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="sanity_exposures",
    )


class SanityCooldown(Base):
    """Cooldown tracker for recovery rituals and hallucination timers."""

    __tablename__ = "sanity_cooldowns"
    __table_args__ = (UniqueConstraint("player_id", "action_code", name="uq_sanity_cooldown_player_action"),)

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    player_id: Mapped[str] = mapped_column(
        String(length=255),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    action_code: Mapped[str] = mapped_column(String(length=64), nullable=False)
    cooldown_expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)

    player: Mapped[Player] = relationship(
        "Player",
        back_populates="sanity_cooldowns",
    )
