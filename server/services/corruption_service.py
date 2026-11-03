"""
Corruption service -- the single write path for player corruption (#804, #145), on the player registry (ADR-029
step 5c).

The value is ``stats.corruption`` in the aggregate's row part; its ledger rows (``corruption_adjustment_log``) and the
recovery cooldowns (``corruption_cooldowns``) are parts of the aggregate too. Each operation is one registry unit,
and a sync one: the value, its ledger row and any cooldown commit together before the call returns, so the many
readers that still load players from the database see the new value. The client event, the tier cache and the
tier-crossing message come after the unit, so nothing is announced for a change that rolled back.

Callers must route ALL corruption changes through this service -- a direct ``stats["corruption"] = ...`` bypasses the
ledger and tier cache, and ``upsert_player`` no longer writes an existing player's corruption at all.
"""

# pylint: disable=missing-function-docstring  # Reason: Protocol method stubs; contracts live in class docstrings
# pylint: disable=too-few-public-methods  # Reason: Protocol/dataclass stubs and error classes, no behavior needed

from __future__ import annotations

import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import TYPE_CHECKING, NoReturn, Protocol

from ..exceptions import ValidationError
from ..game.player_registry import PlayerAggregate, PlayerNotFoundError
from ..models.corruption import CorruptionTier, CorruptionUpdateResult, compute_tier
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.enhanced_error_logging import log_and_raise_enhanced
from ..utils.int_coercion import coerce_int
from .corruption_tier_cache import corruption_tier_cache
from .lucidity_helpers import normalize_metadata

if TYPE_CHECKING:
    from ..game.player_registry import PlayerRegistry

logger = get_logger(__name__)

# Tier-crossing narration -- fires once per crossing, never per adjustment. Deliberately vague
# about cause; the player learns "something changed", not the mechanism, matching the mystery
# the design doc's tier-feedback discussion favored.
#
# #815: under the permanence floor, PURE is unreachable as a *new* tier via normal writes.
# #816: admin setstat may call apply_corruption_adjustment(bypass_permanence_floor=True) and
# re-enter PURE; the fall message below narrates that GM wipe.
_TIER_RISE_MESSAGES: dict[CorruptionTier, str] = {
    CorruptionTier.TOUCHED: "Something in you gives way, just slightly. The taint has taken hold.",
    CorruptionTier.MARKED: "A faint wrongness clings to your thoughts. You have been marked.",
    CorruptionTier.CORRUPTED: "The taint settles deeper into you. You feel less yourself.",
    CorruptionTier.WARPED: "Something in you has come loose. The world looks subtly, permanently wrong.",
}
_TIER_FALL_MESSAGES: dict[CorruptionTier, str] = {
    CorruptionTier.PURE: "The last of the taint leaves you. For a moment, you feel almost whole again.",
    CorruptionTier.TOUCHED: "The wrongness fades to little more than a shadow -- though it never fully leaves you.",
    CorruptionTier.MARKED: "The taint loosens its grip, if only somewhat.",
    CorruptionTier.CORRUPTED: "You claw back some measure of yourself from the warp.",
}


class CorruptionActionError(RuntimeError):
    """Base error for corruption action operations."""


class CorruptionActionOnCooldownError(CorruptionActionError):
    """Raised when a corruption recovery action is attempted during its cooldown."""


class CorruptionPersistence(Protocol):
    """The slice of the persistence layer that corruption writers holding only ``persistence`` call: its
    ``adjust_corruption`` runs ``CorruptionService.apply_corruption_adjustment`` (injected at startup)."""

    async def adjust_corruption(
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
        bypass_permanence_floor: bool = False,
    ) -> CorruptionUpdateResult: ...


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

    _registry: PlayerRegistry

    def __init__(self, registry: PlayerRegistry) -> None:
        self._registry = registry

    def apply_in(
        self,
        player: PlayerAggregate,
        delta: int,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
        bypass_permanence_floor: bool = False,
    ) -> CorruptionUpdateResult:
        """Apply a corruption delta inside the caller's unit: clamp it, set it and queue its ledger row (both sync).

        For composite units (a recovery rite and its cooldown); call ``announce`` with the result after the unit.
        ``bypass_permanence_floor=True`` is reserved for admin setstat (#816) so GMs can wipe to 0.
        """
        previous_value = coerce_int(player.row.stats.get("corruption", 0), default=0)
        # #815: once a soul has been touched at all, it can never fall back to 0 through this
        # service -- the floor is derived from the current value, not tracked separately, so a
        # player who has never been corrupted is unaffected.
        floor = 0 if bypass_permanence_floor else (1 if previous_value > 0 else 0)
        new_value = max(floor, min(100, previous_value + delta))
        player.row.set_stat("corruption", new_value, sync=True)
        player.corruption_ledger.log(delta, reason_code, normalize_metadata(metadata), location_id, sync=True)
        return CorruptionUpdateResult(
            player_id=player.player_id,
            previous_value=previous_value,
            new_value=new_value,
            previous_tier=compute_tier(previous_value),
            new_tier=compute_tier(new_value),
            delta=delta,
        )

    async def announce(self, result: CorruptionUpdateResult) -> None:
        """After the unit has committed: the client event, the tier cache, and the tier-crossing message."""
        await self._send_corruption_update_event(result.player_id, result.new_value)
        corruption_tier_cache.set_tier(result.player_id, result.new_tier)
        logger.info(
            "Corruption adjustment applied",
            player_id=result.player_id,
            delta=result.delta,
            tier_before=result.previous_tier,
            tier_after=result.new_tier,
        )
        if result.previous_tier != result.new_tier:
            await self._notify_tier_crossing(result.player_id, result.previous_tier, result.new_tier)

    async def apply_corruption_adjustment(
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
        bypass_permanence_floor: bool = False,
    ) -> CorruptionUpdateResult:
        """Apply a corruption delta as one unit, then announce it (see ``apply_in``)."""
        try:
            async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                result = self.apply_in(
                    player,
                    delta,
                    reason_code=reason_code,
                    metadata=metadata,
                    location_id=location_id,
                    bypass_permanence_floor=bypass_permanence_floor,
                )
        except PlayerNotFoundError:
            _player_not_found(player_id, "apply_corruption_adjustment")
        await self.announce(result)
        return result

    async def _send_corruption_update_event(self, player_id: uuid.UUID, new_value: int) -> None:
        """Push the new corruption value to the client. Client reads it via the existing
        player_update handling -- no new event *type*, per SUBSYSTEM_CORRUPTION_DESIGN.md §4, but
        this service must actually be the one sending it (nothing else pushes corruption)."""
        try:
            from ..realtime.connection_manager_api import send_game_event

            await send_game_event(player_id, "player_update", {"stats": {"corruption": new_value}})
        except (ValueError, AttributeError, RuntimeError, OSError) as e:
            # RuntimeError: connection manager unavailable (e.g. unit tests, offline player).
            logger.warning("Failed to send corruption update event", player_id=player_id, error=str(e))

    async def _notify_tier_crossing(
        self, player_id: uuid.UUID, previous_tier: CorruptionTier, new_tier: CorruptionTier
    ) -> None:
        """Deliver a personal system message exactly once per tier crossing."""
        rose = list(CorruptionTier).index(new_tier) > list(CorruptionTier).index(previous_tier)
        message = _TIER_RISE_MESSAGES.get(new_tier) if rose else _TIER_FALL_MESSAGES.get(new_tier)
        if message:
            # Imported here, as the other callers do: chat_npc_system -> chat_message_helpers -> services imports this
            # module while chat_npc_system is still initialising (#1128).
            from ..game.chat_npc_system import deliver_personal_system

            _ = await deliver_personal_system(player_id, message)

    async def get_cooldown_expiry(self, player_id: uuid.UUID, action_code: str) -> datetime | None:
        """The cooldown expiry for a recovery action, or None if it is not on cooldown (or there is no such player)."""
        player = await self._registry.get(player_id)
        return player.corruption_cooldowns.expires_at(action_code) if player is not None else None

    async def perform_recovery_action(
        self,
        player_id: uuid.UUID,
        *,
        action_code: str,
        location_id: str | None = None,
    ) -> CorruptionUpdateResult:
        """Perform a corruption recovery rite (e.g. `/cleanse`): the cooldown check, the change and the new cooldown
        are one unit."""
        action_key = action_code.lower()
        profile = self.RECOVERY_ACTIONS.get(action_key)
        if profile is None:
            raise CorruptionActionError(f"Unknown corruption recovery action: {action_code}")

        now = datetime.now(UTC)
        try:
            async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                if player.corruption_cooldowns.active(action_key, now):
                    raise CorruptionActionOnCooldownError(action_key)
                result = self.apply_in(
                    player,
                    profile.corruption_delta,
                    reason_code=f"ritual_{action_key}",
                    metadata={"recovery_action": action_key},
                    location_id=location_id,
                )
                player.corruption_cooldowns.set(action_key, now + profile.cooldown)
        except PlayerNotFoundError:
            _player_not_found(player_id, "perform_recovery_action")
        await self.announce(result)

        logger.info(
            "Corruption recovery action performed",
            player_id=player_id,
            action=action_key,
            delta=profile.corruption_delta,
            cooldown_hours=profile.cooldown.total_seconds() / 3600,
        )
        return result


def _player_not_found(player_id: uuid.UUID, operation: str) -> NoReturn:
    log_and_raise_enhanced(
        ValidationError,
        f"Player not found: {player_id}",
        player_id=str(player_id),
        operation=operation,
        details={"player_id": str(player_id)},
        user_friendly="Player not found",
    )
