"""Active SAN adjustment helpers for encounters and recovery rituals."""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from ..logging.enhanced_logging_config import get_logger
from ..models.sanity import SanityExposureState
from .sanity_service import SanityService

logger = get_logger(__name__)


class SanityActionError(RuntimeError):
    """Base error for sanity action operations."""


class UnknownSanityActionError(SanityActionError):
    """Raised when an unrecognised recovery action is requested."""


class SanityActionOnCooldownError(SanityActionError):
    """Raised when a recovery action is attempted during its cooldown."""


class UnknownEncounterCategoryError(RuntimeError):
    """Raised when an encounter category is not recognised."""


@dataclass(frozen=True)
class EncounterProfile:
    """Damage profile for a Mythos encounter category."""

    first_time: int
    repeat: int


@dataclass(frozen=True)
class RecoveryActionProfile:
    """Recovery action configuration."""

    san_delta: int
    cooldown: timedelta


class ActiveSanityService:
    """Handle active sanity adjustments such as encounters and recovery actions."""

    ENCOUNTER_PROFILES: dict[str, EncounterProfile] = {
        "disturbing": EncounterProfile(first_time=-6, repeat=-2),
        "horrific": EncounterProfile(first_time=-12, repeat=-5),
        "cosmic": EncounterProfile(first_time=-20, repeat=-10),
    }

    RECOVERY_ACTIONS: dict[str, RecoveryActionProfile] = {
        "pray": RecoveryActionProfile(san_delta=8, cooldown=timedelta(minutes=15)),
        "meditate": RecoveryActionProfile(san_delta=6, cooldown=timedelta(minutes=10)),
        "group_solace": RecoveryActionProfile(san_delta=4, cooldown=timedelta(minutes=20)),
        "therapy": RecoveryActionProfile(san_delta=15, cooldown=timedelta(hours=12)),
        "folk_tonic": RecoveryActionProfile(san_delta=3, cooldown=timedelta(minutes=30)),
    }

    ACCLIMATION_THRESHOLD = 6  # total encounters before acclimation applies

    def __init__(
        self,
        session: AsyncSession,
        *,
        now_provider: Callable[[], datetime] | None = None,
    ) -> None:
        self._session = session
        self._sanity_service = SanityService(session)
        self._now_provider = now_provider or (lambda: datetime.now(UTC))

    async def apply_encounter_sanity_loss(
        self,
        player_id: str,
        entity_archetype: str,
        *,
        category: str,
        location_id: str | None = None,
    ):
        """Apply SAN loss for a Mythos encounter."""

        category_key = category.lower()
        profile = self.ENCOUNTER_PROFILES.get(category_key)
        if profile is None:
            raise UnknownEncounterCategoryError(category)

        exposure: SanityExposureState = await self._sanity_service.increment_exposure_state(
            player_id, entity_archetype
        )
        encounter_count = exposure.encounter_count

        if encounter_count == 1:
            delta = profile.first_time
        elif encounter_count >= self.ACCLIMATION_THRESHOLD:
            half = profile.repeat / 2
            half_value = math.trunc(half)
            if half_value == 0 and profile.repeat < 0:
                half_value = -1
            delta = half_value
        else:
            delta = profile.repeat

        metadata = {
            "encounter_category": category_key,
            "entity_archetype": entity_archetype,
            "encounter_count": encounter_count,
        }

        return await self._sanity_service.apply_sanity_adjustment(
            player_id,
            delta,
            reason_code=f"encounter_{category_key}",
            metadata=metadata,
            location_id=location_id,
        )

    async def perform_recovery_action(
        self,
        player_id: str,
        *,
        action_code: str,
        location_id: str | None = None,
    ):
        """Perform a recovery action and enforce cooldowns."""

        action_key = action_code.lower()
        profile = self.RECOVERY_ACTIONS.get(action_key)
        if profile is None:
            raise UnknownSanityActionError(action_code)

        now = self._now_provider()
        cooldown = await self._sanity_service.get_cooldown(player_id, action_key)
        if cooldown and cooldown.cooldown_expires_at:
            cooldown_expiry = cooldown.cooldown_expires_at
            if cooldown_expiry.tzinfo is None:
                cooldown_expiry = cooldown_expiry.replace(tzinfo=UTC)
            if cooldown_expiry > now:
                raise SanityActionOnCooldownError(action_key)

        metadata = {
            "recovery_action": action_key,
        }

        result = await self._sanity_service.apply_sanity_adjustment(
            player_id,
            profile.san_delta,
            reason_code=f"recovery_{action_key}",
            metadata=metadata,
            location_id=location_id,
        )

        expires_at = (now + profile.cooldown).replace(tzinfo=None)
        await self._sanity_service.set_cooldown(player_id, action_key, expires_at)

        logger.info(
            "Recovery action performed",
            player_id=player_id,
            action=action_key,
            san_delta=profile.san_delta,
            cooldown_minutes=profile.cooldown.total_seconds() / 60,
        )

        return result

    async def get_action_cooldown(self, player_id: str, action_code: str):
        """Fetch the cooldown record for a recovery action."""
        return await self._sanity_service.get_cooldown(player_id, action_code.lower())


__all__ = [
    "ActiveSanityService",
    "SanityActionError",
    "UnknownSanityActionError",
    "SanityActionOnCooldownError",
    "UnknownEncounterCategoryError",
]
