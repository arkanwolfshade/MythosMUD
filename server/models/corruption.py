"""Corruption tracking models — taint accrued from Mythos exposure (#804, #145)."""

# pylint: disable=too-few-public-methods  # Reason: SQLAlchemy models are data classes, no instance methods needed
# pyright: reportImportCycles=false
# Mirrors lucidity.py's identical Player<->model cycle (already baselined there); this file is
# new, so it has no baseline entry of its own for the same, otherwise-unavoidable
# TYPE_CHECKING-only back-reference every relationship-typed model in this package uses.

from __future__ import annotations

import uuid
from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, ForeignKey, Index, Integer, String, Text, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .player import Player


class CorruptionTier(StrEnum):
    """Corruption bands over 0..100.

    `PURE` is reserved for exactly 0 (#815) -- `CorruptionService.apply_corruption_adjustment`
    floors any player who has ever been corrupted at 1, so `PURE` is an absorbing state you can
    only ever leave. `TOUCHED` (1-24) exists so that permanent scar is *observable*: without it,
    a cleansed veteran sitting at 1 and a novice at 0 would read identically everywhere the tier
    is consulted.

    The `corrupted` floor MUST stay at exactly 50 -- `Stats.is_corrupted()`
    (`server/models/game.py:322`) already treats `>= 50` as corrupted, and moving this
    boundary silently changes that check's behavior everywhere it's read.
    """

    PURE = "pure"
    TOUCHED = "touched"
    MARKED = "marked"
    CORRUPTED = "corrupted"
    WARPED = "warped"


def compute_tier(value: int) -> CorruptionTier:
    """Derive a corruption tier from the raw stat value. Pure function, no I/O.

    Unlike lucidity's tier (persisted on `PlayerLucidity.current_tier`), corruption's tier is
    never stored -- it's a total function of a value every caller already holds in memory, so
    there is nothing to keep in sync. `CorruptionTierCache` exists only to remember the
    *previous* tier long enough to detect a crossing; it does not replace this function.
    """
    if value >= 75:
        return CorruptionTier.WARPED
    if value >= 50:
        return CorruptionTier.CORRUPTED
    if value >= 25:
        return CorruptionTier.MARKED
    if value >= 1:
        return CorruptionTier.TOUCHED
    return CorruptionTier.PURE


class CorruptionAdjustmentLog(Base):
    """Immutable ledger for every corruption gain or loss event."""

    __tablename__: str = "corruption_adjustment_log"
    __table_args__: tuple[Index, ...] = (Index("idx_corruption_adjustment_player_created", "player_id", "created_at"),)

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
    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        nullable=False,
        insert_default=func.now(),  # pylint: disable=not-callable  # func.now() callable at runtime
    )

    player: Mapped[Player] = relationship("Player", back_populates="corruption_adjustments")


class CorruptionCooldown(Base):
    """Cooldown tracker for corruption recovery rites (e.g. `/cleanse`)."""

    __tablename__: str = "corruption_cooldowns"
    __table_args__: tuple[UniqueConstraint, ...] = (
        UniqueConstraint("player_id", "action_code", name="uq_corruption_cooldown_player_action"),
    )

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)
    player_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=False),
        ForeignKey("players.player_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    action_code: Mapped[str] = mapped_column(Text(), nullable=False)
    cooldown_expires_at: Mapped[datetime] = mapped_column(DateTime(), nullable=False)

    player: Mapped[Player] = relationship("Player", back_populates="corruption_cooldowns")


__all__ = ["CorruptionAdjustmentLog", "CorruptionCooldown", "CorruptionTier", "compute_tier"]
