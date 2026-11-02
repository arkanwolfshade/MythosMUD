"""Lucidity service: LCD adjustments, tiers, liabilities and catatonia, on the player registry (ADR-029 step 5b-i).

Lucidity lives in the registry's lucidity part. Each operation is one registry unit; the change is lazy (the sweep
writes it, with its ``lucidity_adjustment_log`` row). Everything that reaches outside the player (the catatonia
observer, client events, the phantom and fake-sender clears, the tier cache) runs after the unit, so nothing is
announced for a change that rolled back and no network send happens under the player's lock.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Lucidity service requires many parameters for context and lucidity operations.

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from ..game.player_registry import LucidityData, PlayerAggregate, PlayerNotFoundError
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from ..utils.liability_types import LiabilityStackEntry
from .lucidity_event_dispatcher import LucidityChangeEventExtras, send_lucidity_change_event
from .lucidity_helpers import (
    LIABILITY_CATALOG,
    TIER_ORDER,
    CatatoniaObserverProtocol,
    LucidityUpdateResult,
    Tier,
    clamp_lucidity,
    coerce_metadata_dict,
    decode_liabilities,
    encode_liabilities,
    lucidity_event_source,
    normalize_metadata,
    resolve_tier,
    worsened_tier,
)
from .lucidity_repository import PlayerGoneError
from .lucidity_trigger_handlers import (
    CatatoniaTransition,
    announce_catatonia_transition,
    handle_delirium_and_sanitarium_triggers,
)

if TYPE_CHECKING:
    from ..game.player_registry import PlayerRegistry

logger = get_logger(__name__)

__all__ = [
    "CatatoniaObserverProtocol",
    "LIABILITY_CATALOG",
    "LucidityService",
    "LucidityUpdateResult",
    "TIER_ORDER",
    "Tier",
    "clamp_lucidity",
    "decode_liabilities",
    "encode_liabilities",
    "resolve_tier",
]

# A delta, or a function of the player's current LCD that returns one (0 = leave lucidity alone).
LucidityDelta = int | Callable[[int], int]
LiabilityPicker = Callable[[str, int, int, str], str | None]


@dataclass(frozen=True)
class _Applied:  # pylint: disable=too-many-instance-attributes  # Reason: everything the notifications after the unit need
    """What one adjustment changed, for the notifications sent after its unit."""

    result: LucidityUpdateResult
    reason_code: str
    metadata: dict[str, object]
    location_id: str | None
    max_lcd: int
    liabilities: list[LiabilityStackEntry]
    catatonia: CatatoniaTransition | None
    at: datetime


def max_lcd_from_stats(stats: Mapping[str, object]) -> int:
    """The player's LCD ceiling: ``max_lucidity``, else ``education``, else 100."""
    return coerce_int(stats.get("max_lucidity") or stats.get("education") or 100, default=100)


def _first_new_liability(liabilities: list[LiabilityStackEntry]) -> str | None:
    """The first catalogue liability the player does not have, else the first in the catalogue."""
    existing = {entry["code"] for entry in liabilities}
    for code in LIABILITY_CATALOG:
        if code not in existing:
            return code
    return LIABILITY_CATALOG[0] if LIABILITY_CATALOG else None


def _stack_liability(liabilities: list[LiabilityStackEntry], liability_code: str) -> None:
    """Add one stack of ``liability_code`` (a new entry if the player has none)."""
    for entry in liabilities:
        if entry["code"] == liability_code:
            entry["stacks"] += 1
            return
    liabilities.append({"code": liability_code, "stacks": 1})


class LucidityService:
    """High-level operations for lucidity adjustments and liability tracking."""

    _registry: PlayerRegistry
    _liability_picker: LiabilityPicker | None
    _liability_threshold: int
    _catatonia_observer: CatatoniaObserverProtocol | None

    def __init__(
        self,
        registry: PlayerRegistry,
        liability_picker: LiabilityPicker | None = None,
        liability_threshold: int = 15,
        *,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
    ) -> None:
        self._registry = registry
        self._liability_picker = liability_picker
        self._liability_threshold = liability_threshold
        self._catatonia_observer = catatonia_observer

    # ---- reads ----

    async def get_lucidity(self, player_id: uuid.UUID) -> LucidityData:
        """The player's lucidity (the starting values if they have never had a change).

        Raises:
            PlayerGoneError: there is no such player.
        """
        player = await self._registry.get(player_id)
        if player is None:
            raise PlayerGoneError(str(player_id))
        return player.lucidity.data

    # ---- adjustments ----

    async def apply_lucidity_adjustment(
        self,
        player_id: uuid.UUID,
        delta: LucidityDelta,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        """Apply a LCD delta, log the change, and evaluate liabilities.

        ``delta`` may be a function of the current LCD, evaluated inside the unit, so a read-then-adjust (a decay
        that stops at a floor, a rescue that lifts to 1) cannot act on a stale value. When it returns 0 nothing
        changes and nothing is logged.

        Raises:
            PlayerGoneError: there is no such player.
        """
        try:
            async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
                current = player.lucidity.data
                applied = self._apply(player, delta, reason_code, metadata, location_id)
        except PlayerNotFoundError as error:
            raise PlayerGoneError(str(player_id)) from error
        if applied is None:
            return LucidityUpdateResult(player_id, current.lcd, current.lcd, current.tier, current.tier, 0, [])
        await self._announce(applied)
        return applied.result

    def _apply(
        self,
        player: PlayerAggregate,
        delta: LucidityDelta,
        reason_code: str,
        metadata: Mapping[str, object] | str | None,
        location_id: str | None,
    ) -> _Applied | None:
        """The in-unit half of an adjustment: LCD, tier, catatonia, liabilities and the ledger row."""
        part = player.lucidity
        previous = part.data
        if callable(delta):
            delta = delta(previous.lcd)
            if not delta:
                return None
        new_lcd = clamp_lucidity(previous.lcd + delta)
        new_tier = resolve_tier(new_lcd)
        now = datetime.now(UTC)
        catatonia: CatatoniaTransition | None = None
        if new_tier == "catatonic" and previous.catatonia_entered_at is None:
            catatonia = "entered"
        elif new_tier != "catatonic" and previous.catatonia_entered_at is not None:
            catatonia = "cleared"

        liabilities = decode_liabilities(previous.liabilities)
        added = self._liabilities_for(player.player_id, liabilities, delta, previous, new_lcd, new_tier, reason_code)
        for code in added:
            _stack_liability(liabilities, code)

        _ = part.set(
            lcd=new_lcd,
            tier=new_tier,
            liabilities=encode_liabilities(liabilities) if added else None,
            catatonia_entered_at=now if catatonia == "entered" else None,
            clear_catatonia=catatonia == "cleared",
        )
        part.log(delta, reason_code, normalize_metadata(metadata), location_id)
        return _Applied(
            result=LucidityUpdateResult(
                player_id=player.player_id,
                previous_lcd=previous.lcd,
                new_lcd=new_lcd,
                previous_tier=previous.tier,
                new_tier=new_tier,
                delta=delta,
                liabilities_added=added,
            ),
            reason_code=reason_code,
            metadata=coerce_metadata_dict(metadata),
            location_id=location_id,
            max_lcd=max_lcd_from_stats(player.row.stats),
            liabilities=liabilities,
            catatonia=catatonia,
            at=now,
        )

    def _liabilities_for(
        self,
        player_id: uuid.UUID,
        liabilities: list[LiabilityStackEntry],
        delta: int,
        previous: LucidityData,
        new_lcd: int,
        new_tier: str,
        reason_code: str,
    ) -> list[str]:
        """The liability an adjustment adds: one for a large loss or a worsened tier, else none."""
        if not ((delta < 0 and abs(delta) >= self._liability_threshold) or worsened_tier(previous.tier, new_tier)):
            return []
        if self._liability_picker is not None:
            code = self._liability_picker(str(player_id), previous.lcd, new_lcd, reason_code)
        else:
            code = _first_new_liability(liabilities)
        return [code] if code else []

    async def _announce(self, applied: _Applied) -> None:
        """The after-unit half of an adjustment: observers, client events, hallucination clears, the tier cache."""
        result = applied.result
        player_id = result.player_id
        if applied.catatonia is not None:
            await announce_catatonia_transition(
                transition=applied.catatonia,
                player_id=player_id,
                at=applied.at,
                new_lcd=result.new_lcd,
                catatonia_observer=self._catatonia_observer,
                reason_code=applied.reason_code,
            )
        await handle_delirium_and_sanitarium_triggers(
            player_id, result.new_lcd, result.previous_lcd, self._catatonia_observer
        )
        if result.delta or result.previous_tier != result.new_tier:
            await send_lucidity_change_event(
                player_id=player_id,
                current_lcd=min(result.new_lcd, applied.max_lcd),
                delta=result.delta,
                tier=result.new_tier,
                extras=LucidityChangeEventExtras(
                    max_lcd=applied.max_lcd,
                    liabilities=applied.liabilities,
                    reason=applied.reason_code,
                    source=lucidity_event_source(applied.metadata, applied.location_id),
                    metadata=applied.metadata or None,
                ),
            )
        logger.info(
            "Lucidity adjustment applied",
            player_id=player_id,
            lcd_change=result.delta,
            reason=applied.reason_code,
            tier_before=result.previous_tier,
            tier_after=result.new_tier,
            liabilities_added=result.liabilities_added,
        )
        # #625/#714: phantoms and fake whisper senders only make sense while the player remains
        # in a hallucination-eligible tier. Leaving fractured/deranged (in either direction)
        # clears both.
        if result.previous_tier != result.new_tier and result.new_tier not in ("fractured", "deranged"):
            from .fake_sender_registry import fake_sender_registry
            from .phantom_hostile_service import phantom_hostile_service

            phantom_hostile_service.clear_all_phantoms(player_id)
            fake_sender_registry.clear(player_id)
        # #714: keep the in-memory tier cache (exit hallucination's cheap eligibility check)
        # write-through fresh -- write unconditionally, not just on a transition, since this is
        # the authoritative point where new_tier was just computed.
        from .lucidity_tier_cache import lucidity_tier_cache

        lucidity_tier_cache.set_tier(player_id, result.new_tier)

    # ---- liabilities ----

    async def add_liability(self, player_id: uuid.UUID, liability_code: str) -> str | None:
        """Add or stack a liability on the player."""
        async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            liabilities = decode_liabilities(player.lucidity.data.liabilities)
            _stack_liability(liabilities, liability_code)
            _ = player.lucidity.set(liabilities=encode_liabilities(liabilities))
        logger.info("Liability added", player_id=player_id, liability_code=liability_code)
        return liability_code

    async def clear_liability(self, player_id: uuid.UUID, liability_code: str, *, remove_all: bool = False) -> bool:
        """Reduce or remove a liability stack."""
        async with self._registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            changed = False
            updated: list[LiabilityStackEntry] = []
            for entry in decode_liabilities(player.lucidity.data.liabilities):
                if entry["code"] != liability_code:
                    updated.append(entry)
                    continue
                changed = True
                if not remove_all and entry["stacks"] > 1:
                    entry["stacks"] -= 1
                    updated.append(entry)
            if changed:
                _ = player.lucidity.set(liabilities=encode_liabilities(updated))
        if changed:
            logger.info("Liability updated", player_id=player_id, liability_code=liability_code, remove_all=remove_all)
        return changed
