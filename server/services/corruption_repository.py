"""Repository layer for corruption ledger and cooldown persistence (#804)."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.corruption import CorruptionAdjustmentLog, CorruptionCooldown


def _utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


class CorruptionRepository:
    """Data-access helpers for corruption persistence. Mirrors `LucidityRepository`."""

    _session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def add_adjustment_log(
        self,
        player_id: uuid.UUID,
        delta: int,
        reason_code: str,
        metadata: str,
        location_id: str | None,
    ) -> CorruptionAdjustmentLog:
        """Add a corruption adjustment log entry."""
        log_entry = CorruptionAdjustmentLog(
            player_id=player_id,
            delta=delta,
            reason_code=reason_code,
            metadata_payload=metadata,
            location_id=location_id,
            created_at=_utc_now(),
        )
        self._session.add(log_entry)
        await self._session.flush()
        return log_entry

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> CorruptionCooldown | None:
        """Get cooldown state for a player and action."""
        stmt: Select[tuple[CorruptionCooldown]] = select(CorruptionCooldown).where(
            CorruptionCooldown.player_id == player_id,
            CorruptionCooldown.action_code == action_code,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> CorruptionCooldown:
        """Set or update cooldown for a player and action."""
        cooldown = await self.get_cooldown(player_id, action_code)
        if cooldown is None:
            cooldown = CorruptionCooldown(
                player_id=player_id,
                action_code=action_code,
                cooldown_expires_at=expires_at,
            )
            self._session.add(cooldown)
        else:
            cooldown.cooldown_expires_at = expires_at
        await self._session.flush()
        return cooldown


__all__ = ["CorruptionRepository"]
