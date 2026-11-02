"""Active LCD adjustments: Mythos encounters and recovery rituals, on the player registry (ADR-029 step 5b-ii)."""

from __future__ import annotations

import math
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING

from ..game.player_registry import PlayerNotFoundError
from ..structured_logging.enhanced_logging_config import get_logger
from .lucidity_helpers import PlayerGoneError
from .lucidity_service import CatatoniaObserverProtocol, LucidityService, LucidityUpdateResult

if TYPE_CHECKING:
    from ..game.player_registry import PlayerRegistry

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
    }

    ACCLIMATION_THRESHOLD = 6  # total encounters before acclimation applies

    def __init__(
        self,
        registry: PlayerRegistry,
        *,
        now_provider: Callable[[], datetime] | None = None,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
    ) -> None:
        """Lucidity, exposure and cooldowns all live in ``registry`` (ADR-029 steps 5b-i, 5b-ii)."""
        self._registry: PlayerRegistry = registry
        self._lucidity_service: LucidityService = LucidityService(registry, catatonia_observer=catatonia_observer)
        self._now_provider: Callable[[], datetime] = now_provider or (lambda: datetime.now(UTC))

    @classmethod
    def encounter_delta(cls, profile: EncounterProfile, encounter_count: int) -> int:
        """The LCD an encounter costs: the first sight, a repeat, or half a repeat once acclimated (at least 1)."""
        if encounter_count == 1:
            return profile.first_time
        if encounter_count >= cls.ACCLIMATION_THRESHOLD:
            half_value = math.trunc(profile.repeat / 2)
            return -1 if not half_value and profile.repeat < 0 else half_value
        return profile.repeat

    async def apply_encounter_lucidity_loss(
        self,
        player_id: uuid.UUID | str,
        entity_archetype: str,
        *,
        category: str,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        """Apply LCD loss for a Mythos encounter: count the encounter and take the loss in one unit."""
        player_id_uuid = _as_uuid(player_id)
        category_key = category.lower()
        profile = self.ENCOUNTER_PROFILES.get(category_key)
        if profile is None:
            raise UnknownEncounterCategoryError(category)

        try:
            async with self._registry.mutate(player_id_uuid) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                encounter_count = player.exposure.record_encounter(entity_archetype, self._now_provider())
                applied = self._lucidity_service.apply_in(
                    player,
                    self.encounter_delta(profile, encounter_count),
                    reason_code=f"encounter_{category_key}",
                    metadata={
                        "encounter_category": category_key,
                        "entity_archetype": entity_archetype,
                        "encounter_count": encounter_count,
                    },
                    location_id=location_id,
                )
        except PlayerNotFoundError as error:
            raise PlayerGoneError(str(player_id_uuid)) from error
        if applied is None:  # pragma: no cover - an encounter always costs LCD
            raise RuntimeError("encounter adjustment applied nothing")
        await self._lucidity_service.announce(applied)
        return applied.result

    async def perform_recovery_action(
        self,
        player_id: uuid.UUID | str,
        *,
        action_code: str,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        """Perform a recovery action and enforce cooldowns."""
        player_id_uuid = _as_uuid(player_id)
        action_key = action_code.lower()
        profile = self.RECOVERY_ACTIONS.get(action_key)
        if profile is None:
            raise UnknownLucidityActionError(action_code)

        return await self.apply_timed_recovery(
            player_id_uuid,
            cooldown_key=action_key,
            lcd_delta=profile.lcd_delta,
            cooldown=profile.cooldown,
            location_id=location_id,
        )

    async def apply_timed_recovery(
        self,
        player_id: uuid.UUID,
        *,
        cooldown_key: str,
        lcd_delta: int,
        cooldown: timedelta,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        """Apply an LCD gain under a named cooldown (shared by recovery actions and consumable items).

        The key names the cooldown and the audit reason code (``recovery_<key>``), so several sources may share one
        cooldown by sharing a key. The check, the gain and the new cooldown are one unit: two rites at once cannot both
        pass the check.
        """
        now = self._now_provider()
        try:
            async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                if player.cooldowns.active(cooldown_key, now):
                    raise LucidityActionOnCooldownError(cooldown_key)
                applied = self._lucidity_service.apply_in(
                    player,
                    lcd_delta,
                    reason_code=f"recovery_{cooldown_key}",
                    metadata={"recovery_action": cooldown_key},
                    location_id=location_id,
                )
                player.cooldowns.set(cooldown_key, now + cooldown)
        except PlayerNotFoundError as error:
            raise PlayerGoneError(str(player_id)) from error
        if applied is None:  # pragma: no cover - a fixed delta is always applied
            raise RuntimeError("recovery adjustment applied nothing")
        await self._lucidity_service.announce(applied)

        logger.info(
            "Recovery action performed",
            # Structlog handles UUID objects automatically, no need to convert to string
            player_id=player_id,
            action=cooldown_key,
            lcd_delta=lcd_delta,
            cooldown_minutes=cooldown.total_seconds() / 60,
        )
        return applied.result

    async def get_action_cooldown(self, player_id: uuid.UUID | str, action_code: str) -> datetime | None:
        """When the player's cooldown on a recovery action expires, or None if there is none."""
        player = await self._registry.get(_as_uuid(player_id))
        return player.cooldowns.expires_at(action_code.lower()) if player is not None else None


def _as_uuid(player_id: uuid.UUID | str) -> uuid.UUID:
    if isinstance(player_id, uuid.UUID):
        return player_id
    try:
        return uuid.UUID(player_id)
    except ValueError, AttributeError:
        logger.error("Invalid player_id format", player_id=player_id)
        raise ValueError(f"Invalid player_id format: {player_id}") from None


__all__ = [
    "ActiveLucidityService",
    "LucidityActionError",
    "UnknownLucidityActionError",
    "LucidityActionOnCooldownError",
    "UnknownEncounterCategoryError",
]
