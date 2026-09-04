"""Repository layer for lucidity-related persistence."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from sqlalchemy import Select, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..models.lucidity import LucidityAdjustmentLog, LucidityCooldown, LucidityExposureState, PlayerLucidity


def _utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


class LucidityRepository:
    """Data-access helpers for lucidity persistence."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_player_lucidity(self, player_id: uuid.UUID) -> PlayerLucidity | None:
        """Get player lucidity record."""
        stmt: Select[tuple[PlayerLucidity]] = (
            select(PlayerLucidity)
            .options(selectinload(PlayerLucidity.player))
            .where(PlayerLucidity.player_id == player_id)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_or_create_player_lucidity(self, player_id: uuid.UUID) -> PlayerLucidity:
        """Get existing player lucidity record or create a new one."""
        record = await self.get_player_lucidity(player_id)
        if record is not None:
            return record

        record = PlayerLucidity(player_id=player_id)
        self._session.add(record)
        await self._session.flush()
        return record

    async def add_adjustment_log(
        self,
        player_id: uuid.UUID,
        delta: int,
        reason_code: str,
        metadata: str,
        location_id: str | None,
    ) -> LucidityAdjustmentLog:
        """Add a lucidity adjustment log entry."""
        log_entry = LucidityAdjustmentLog(
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

    async def get_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> LucidityExposureState | None:
        """Get exposure state for a player and entity archetype."""
        stmt: Select[tuple[LucidityExposureState]] = select(LucidityExposureState).where(
            LucidityExposureState.player_id == player_id,
            LucidityExposureState.entity_archetype == entity_archetype,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def increment_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> LucidityExposureState:
        """Increment exposure state for a player and entity archetype."""
        exposure = await self.get_exposure_state(player_id, entity_archetype)
        if exposure is None:
            exposure = LucidityExposureState(
                player_id=player_id,
                entity_archetype=entity_archetype,
                encounter_count=1,
                last_encounter_at=_utc_now(),
            )
            self._session.add(exposure)
        else:
            exposure.encounter_count += 1
            exposure.last_encounter_at = _utc_now()
        await self._session.flush()
        return exposure

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> LucidityCooldown | None:
        """Get cooldown state for a player and action."""
        stmt: Select[tuple[LucidityCooldown]] = select(LucidityCooldown).where(
            LucidityCooldown.player_id == player_id,
            LucidityCooldown.action_code == action_code,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> LucidityCooldown:
        """Set or update cooldown for a player and action."""
        cooldown = await self.get_cooldown(player_id, action_code)
        if cooldown is None:
            cooldown = LucidityCooldown(
                player_id=player_id,
                action_code=action_code,
                cooldown_expires_at=expires_at,
            )
            self._session.add(cooldown)
        else:
            cooldown.cooldown_expires_at = expires_at
        await self._session.flush()
        return cooldown

    async def delete_cooldowns_by_action_code_pattern(self, player_id: uuid.UUID, action_code_pattern: str) -> int:
        """Delete all cooldowns for a player matching an action code pattern."""
        stmt = delete(LucidityCooldown).where(
            LucidityCooldown.player_id == player_id,
            LucidityCooldown.action_code.like(action_code_pattern),
        )
        result = await self._session.execute(stmt)
        await self._session.flush()
        deleted_count: int = getattr(result, "rowcount", 0)
        return deleted_count
