"""
Corruption service -- the single write path for player corruption (#804, #145).

Mirrors `LucidityService` structurally (adjustment + ledger + tier cache), but corruption has
no dedicated table the way `PlayerLucidity` gives lucidity: the raw value lives in
`players.stats->>'corruption'` (`server/models/game.py:174`). So this service reads/writes that
stat directly via the `persistence` object every caller already holds, and opens its own
short-lived session (mirroring `lucidity_recovery_commands.py`'s `_run_recovery_session` pattern)
only for the ledger and cooldown tables, which do need SQLAlchemy ORM access.

Callers must route ALL corruption changes through `apply_corruption_adjustment` -- direct
`stats["corruption"] = ...` mutation or calls to `persistence.apply_corruption` bypass the ledger
and tier cache, which then go stale.
"""

# pylint: disable=missing-function-docstring  # Reason: Protocol method stubs; contracts live in class docstrings
# pylint: disable=too-few-public-methods  # Reason: Protocol/dataclass stubs and error classes, no behavior needed

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Protocol

from ..database import get_async_session
from ..exceptions import ValidationError
from ..game.chat_npc_system import deliver_personal_system
from ..models.corruption import CorruptionTier, compute_tier
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.enhanced_error_logging import log_and_raise_enhanced
from ..utils.int_coercion import coerce_int
from .corruption_repository import CorruptionRepository
from .corruption_tier_cache import corruption_tier_cache
from .lucidity_helpers import normalize_metadata

logger = get_logger(__name__)

# Tier-crossing narration -- fires once per crossing, never per adjustment. Deliberately vague
# about cause; the player learns "something changed", not the mechanism, matching the mystery
# the design doc's tier-feedback discussion favored.
_TIER_RISE_MESSAGES: dict[CorruptionTier, str] = {
    CorruptionTier.MARKED: "A faint wrongness clings to your thoughts. You have been marked.",
    CorruptionTier.CORRUPTED: "The taint settles deeper into you. You feel less yourself.",
    CorruptionTier.WARPED: "Something in you has come loose. The world looks subtly, permanently wrong.",
}
_TIER_FALL_MESSAGES: dict[CorruptionTier, str] = {
    CorruptionTier.PURE: "The wrongness recedes. For the first time in a while, your mind feels wholly your own.",
    CorruptionTier.MARKED: "The taint loosens its grip, if only somewhat.",
    CorruptionTier.CORRUPTED: "You claw back some measure of yourself from the warp.",
}


class CorruptionPersistencePlayer(Protocol):
    """Structural shape a player object must expose for corruption adjustment."""

    def get_stats(self) -> dict[str, object]: ...
    def set_stats(self, stats: dict[str, object]) -> None: ...


class CorruptionPersistenceProtocol(Protocol):
    """Structural shape of the persistence object every corruption writer already holds."""

    async def get_player_by_id(self, player_id: uuid.UUID) -> CorruptionPersistencePlayer | None: ...
    async def save_player(self, player: CorruptionPersistencePlayer) -> None: ...


@dataclass
class CorruptionUpdateResult:
    """Normalized response describing the outcome of a corruption adjustment."""

    player_id: uuid.UUID
    previous_value: int
    new_value: int
    previous_tier: CorruptionTier
    new_tier: CorruptionTier
    delta: int


class CorruptionActionError(RuntimeError):
    """Base error for corruption action operations."""


class CorruptionActionOnCooldownError(CorruptionActionError):
    """Raised when a corruption recovery action is attempted during its cooldown."""


@dataclass(frozen=True)
class RecoveryActionProfile:
    """Recovery action configuration -- mirrors `active_lucidity_service.RecoveryActionProfile`."""

    corruption_delta: int
    cooldown: timedelta


class CorruptionService:
    """High-level operations for corruption adjustments. The single write path for `corruption`."""

    # Cleanse is deliberately slow and only partial per use -- corruption recovery is meant to
    # cost real play time, not be a full reset (SUBSYSTEM_CORRUPTION_DESIGN.md's asymmetric-
    # recovery decision).
    RECOVERY_ACTIONS: dict[str, RecoveryActionProfile] = {
        "cleanse": RecoveryActionProfile(corruption_delta=-8, cooldown=timedelta(hours=6)),
    }

    _persistence: CorruptionPersistenceProtocol

    def __init__(self, persistence: CorruptionPersistenceProtocol) -> None:
        self._persistence = persistence

    async def apply_corruption_adjustment(
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
    ) -> CorruptionUpdateResult:
        """Apply a corruption delta, clamp it, log it, update the tier cache, notify on crossing."""
        player = await self._persistence.get_player_by_id(player_id)
        if player is None:
            log_and_raise_enhanced(
                ValidationError,
                f"Player not found: {player_id}",
                player_id=str(player_id),
                operation="apply_corruption_adjustment",
                details={"player_id": str(player_id)},
                user_friendly="Player not found",
            )

        stats = player.get_stats()
        previous_value = coerce_int(stats.get("corruption", 0), default=0)
        new_value = max(0, min(100, previous_value + delta))
        stats["corruption"] = new_value
        player.set_stats(stats)
        await self._persistence.save_player(player)

        previous_tier = compute_tier(previous_value)
        new_tier = compute_tier(new_value)

        metadata_payload = normalize_metadata(metadata)
        async for session in get_async_session():
            repo = CorruptionRepository(session)
            _ = await repo.add_adjustment_log(player_id, delta, reason_code, metadata_payload, location_id)
            await session.commit()
            break

        corruption_tier_cache.set_tier(player_id, new_tier)

        logger.info(
            "Corruption adjustment applied",
            player_id=player_id,
            delta=delta,
            reason=reason_code,
            tier_before=previous_tier,
            tier_after=new_tier,
        )

        if previous_tier != new_tier:
            await self._notify_tier_crossing(player_id, previous_tier, new_tier)

        return CorruptionUpdateResult(
            player_id=player_id,
            previous_value=previous_value,
            new_value=new_value,
            previous_tier=previous_tier,
            new_tier=new_tier,
            delta=delta,
        )

    async def _notify_tier_crossing(
        self, player_id: uuid.UUID, previous_tier: CorruptionTier, new_tier: CorruptionTier
    ) -> None:
        """Deliver a personal system message exactly once per tier crossing."""
        rose = list(CorruptionTier).index(new_tier) > list(CorruptionTier).index(previous_tier)
        message = _TIER_RISE_MESSAGES.get(new_tier) if rose else _TIER_FALL_MESSAGES.get(new_tier)
        if message:
            _ = await deliver_personal_system(player_id, message)

    async def get_cooldown_expiry(self, player_id: uuid.UUID, action_code: str) -> datetime | None:
        """Fetch the cooldown expiry for a recovery action, or None if not on cooldown."""
        async for session in get_async_session():
            repo = CorruptionRepository(session)
            cooldown = await repo.get_cooldown(player_id, action_code)
            return cooldown.cooldown_expires_at if cooldown else None
        return None

    async def perform_recovery_action(
        self,
        player_id: uuid.UUID,
        *,
        action_code: str,
        location_id: str | None = None,
    ) -> CorruptionUpdateResult:
        """Perform a corruption recovery rite (e.g. `/cleanse`) and enforce its cooldown."""
        action_key = action_code.lower()
        profile = self.RECOVERY_ACTIONS.get(action_key)
        if profile is None:
            raise CorruptionActionError(f"Unknown corruption recovery action: {action_code}")

        now = datetime.now(UTC)
        expiry = await self.get_cooldown_expiry(player_id, action_key)
        if expiry is not None:
            expiry_aware = expiry if expiry.tzinfo is not None else expiry.replace(tzinfo=UTC)
            if expiry_aware > now:
                raise CorruptionActionOnCooldownError(action_key)

        result = await self.apply_corruption_adjustment(
            player_id,
            profile.corruption_delta,
            reason_code=f"ritual_{action_key}",
            metadata={"recovery_action": action_key},
            location_id=location_id,
        )

        expires_at = (now + profile.cooldown).replace(tzinfo=None)
        async for session in get_async_session():
            repo = CorruptionRepository(session)
            _ = await repo.set_cooldown(player_id, action_key, expires_at)
            await session.commit()
            break

        logger.info(
            "Corruption recovery action performed",
            player_id=player_id,
            action=action_key,
            delta=profile.corruption_delta,
            cooldown_hours=profile.cooldown.total_seconds() / 3600,
        )
        return result


__all__ = [
    "CorruptionActionError",
    "CorruptionActionOnCooldownError",
    "CorruptionPersistencePlayer",
    "CorruptionPersistenceProtocol",
    "CorruptionService",
    "CorruptionUpdateResult",
    "RecoveryActionProfile",
]
