"""Active LCD adjustment helpers for encounters and recovery rituals."""

from __future__ import annotations

import math
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from ..models.lucidity import LucidityExposureState
from ..structured_logging.enhanced_logging_config import get_logger
from .lucidity_service import CatatoniaObserverProtocol, LucidityService

logger = get_logger(__name__)


class LucidityActionError(RuntimeError):
    """Base error for lucidity action operations."""


class UnknownLucidityActionError(LucidityActionError):
    """Raised when an unrecognised recovery action is requested."""


class LucidityActionOnCooldownError(LucidityActionError):
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

    lcd_delta: int
    cooldown: timedelta


class ActiveLucidityService:
    """Handle active lucidity adjustments such as encounters and recovery actions."""

    ENCOUNTER_PROFILES: dict[str, EncounterProfile] = {
        "disturbing": EncounterProfile(first_time=-6, repeat=-2),
        "horrific": EncounterProfile(first_time=-12, repeat=-5),
        "cosmic": EncounterProfile(first_time=-20, repeat=-10),
    }

    RECOVERY_ACTIONS: dict[str, RecoveryActionProfile] = {
        "pray": RecoveryActionProfile(lcd_delta=8, cooldown=timedelta(minutes=15)),
        "meditate": RecoveryActionProfile(lcd_delta=6, cooldown=timedelta(minutes=10)),
        "group_solace": RecoveryActionProfile(lcd_delta=4, cooldown=timedelta(minutes=20)),
        "therapy": RecoveryActionProfile(lcd_delta=15, cooldown=timedelta(hours=12)),
        "folk_tonic": RecoveryActionProfile(lcd_delta=3, cooldown=timedelta(minutes=30)),
    }

    ACCLIMATION_THRESHOLD = 6  # total encounters before acclimation applies

    def __init__(
        self,
        session: AsyncSession,
        *,
        now_provider: Callable[[], datetime] | None = None,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
    ) -> None:
        self._session = session
        self._lucidity_service = LucidityService(session, catatonia_observer=catatonia_observer)
        self._now_provider = now_provider or (lambda: datetime.now(UTC))

    async def apply_encounter_lucidity_loss(
        self,
        player_id: uuid.UUID | str,
        entity_archetype: str,
        *,
        category: str,
        location_id: str | None = None,
    ):
        """Apply LCD loss for a Mythos encounter."""

        # Convert player_id to UUID if it's a string
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
                logger.error("Invalid player_id format", player_id=player_id)
                raise ValueError(f"Invalid player_id format: {player_id}") from None
        else:
            player_id_uuid = player_id

        category_key = category.lower()
        profile = self.ENCOUNTER_PROFILES.get(category_key)
        if profile is None:
            raise UnknownEncounterCategoryError(category)

        exposure: LucidityExposureState = await self._lucidity_service.increment_exposure_state(
            player_id_uuid, entity_archetype
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

        return await self._lucidity_service.apply_lucidity_adjustment(
            player_id_uuid,
            delta,
            reason_code=f"encounter_{category_key}",
            metadata=metadata,
            location_id=location_id,
        )

    async def perform_recovery_action(
        self,
        player_id: uuid.UUID | str,
        *,
        action_code: str,
        location_id: str | None = None,
    ):
        """Perform a recovery action and enforce cooldowns."""

        # Convert player_id to UUID if it's a string
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
                logger.error("Invalid player_id format", player_id=player_id)
                raise ValueError(f"Invalid player_id format: {player_id}") from None
        else:
            player_id_uuid = player_id

        action_key = action_code.lower()
        profile = self.RECOVERY_ACTIONS.get(action_key)
        if profile is None:
            raise UnknownLucidityActionError(action_code)

        now = self._now_provider()
        cooldown = await self._lucidity_service.get_cooldown(player_id_uuid, action_key)
        if cooldown and cooldown.cooldown_expires_at:
            cooldown_expiry = cooldown.cooldown_expires_at
            if cooldown_expiry.tzinfo is None:
                cooldown_expiry = cooldown_expiry.replace(tzinfo=UTC)
            if cooldown_expiry > now:
                raise LucidityActionOnCooldownError(action_key)

        metadata = {
            "recovery_action": action_key,
        }

        result = await self._lucidity_service.apply_lucidity_adjustment(
            player_id_uuid,
            profile.lcd_delta,
            reason_code=f"recovery_{action_key}",
            metadata=metadata,
            location_id=location_id,
        )

        expires_at = (now + profile.cooldown).replace(tzinfo=None)
        await self._lucidity_service.set_cooldown(player_id_uuid, action_key, expires_at)

        logger.info(
            "Recovery action performed",
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player_id_uuid,
            action=action_key,
            lcd_delta=profile.lcd_delta,
            cooldown_minutes=profile.cooldown.total_seconds() / 60,
        )

        return result

    async def get_action_cooldown(self, player_id: uuid.UUID | str, action_code: str):
        """Fetch the cooldown record for a recovery action."""
        # Convert player_id to UUID if it's a string
        if isinstance(player_id, str):
            try:
                player_id_uuid = uuid.UUID(player_id)
            except (ValueError, AttributeError):
                logger.error("Invalid player_id format", player_id=player_id)
                raise ValueError(f"Invalid player_id format: {player_id}") from None
        else:
            player_id_uuid = player_id
        return await self._lucidity_service.get_cooldown(player_id_uuid, action_code.lower())


__all__ = [
    "ActiveLucidityService",
    "LucidityActionError",
    "UnknownLucidityActionError",
    "LucidityActionOnCooldownError",
    "UnknownEncounterCategoryError",
]
