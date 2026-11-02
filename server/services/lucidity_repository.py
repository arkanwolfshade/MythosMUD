"""Repository for the lucidity tables the player registry does not hold yet: exposure state and cooldowns.

``player_lucidity`` and its ledger live in the registry's lucidity part (ADR-029 step 5b-i); exposure state and
``lucidity_cooldowns`` move there in step 5b-ii.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

from sqlalchemy import Select, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.lucidity import LucidityCooldown, LucidityExposureState
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class PlayerGoneError(LookupError):
    """The player row no longer exists (deleted or reset), so there is no lucidity to create or change (#1147)."""


def _utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


class LucidityRepository:
    """Data-access helpers for lucidity exposure state and cooldowns."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

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

    async def clear_hallucination_timers(self, player_id: uuid.UUID) -> int:
        """Delete every hallucination timer cooldown of the player (sanitarium failover, LCD -100)."""
        deleted_count = await self.delete_cooldowns_by_action_code_pattern(player_id, "hallucination_%")
        if deleted_count > 0:
            logger.info(
                "Hallucination timers cleared for sanitarium failover",
                player_id=player_id,
                timers_cleared=deleted_count,
            )
        return deleted_count
