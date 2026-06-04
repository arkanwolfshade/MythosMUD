"""Lucidity repository and service for eldritch stability management."""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Lucidity service requires many parameters for context and lucidity operations.

from __future__ import annotations

import uuid
from collections.abc import Callable, Mapping
from datetime import datetime
from typing import cast

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.lucidity import LucidityCooldown, LucidityExposureState, PlayerLucidity
from ..structured_logging.enhanced_logging_config import get_logger
from ..utils.int_coercion import coerce_int
from ..utils.liability_types import LiabilityStackEntry
from .lucidity_event_dispatcher import LucidityChangeEventExtras, send_lucidity_change_event
from .lucidity_helpers import (
    LIABILITY_CATALOG,
    TIER_ORDER,
    CatatoniaObserverProtocol,
    LucidityAdjustmentFinalizeContext,
    LucidityChangeEventContext,
    LucidityUpdateResult,
    Tier,
    clamp_lucidity,
    coerce_metadata_dict,
    decode_liabilities,
    encode_liabilities,
    lucidity_event_source,
    normalize_metadata,
    resolve_tier,
    utc_now,
    worsened_tier,
)
from .lucidity_repository import LucidityRepository
from .lucidity_trigger_handlers import handle_catatonia_transitions, handle_delirium_and_sanitarium_triggers

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


class LucidityService:
    """High-level operations for lucidity adjustments and liability tracking."""

    _session: AsyncSession
    _repo: LucidityRepository
    _liability_picker: Callable[[str, int, int, str], str | None]
    _liability_threshold: int
    _catatonia_observer: CatatoniaObserverProtocol | None

    def __init__(
        self,
        session: AsyncSession,
        liability_picker: Callable[[str, int, int, str], str | None] | None = None,
        liability_threshold: int = 15,
        *,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
    ) -> None:
        self._session = session
        self._repo = LucidityRepository(session)
        self._liability_picker = liability_picker or self._default_liability_picker
        self._liability_threshold = liability_threshold
        self._catatonia_observer = catatonia_observer

    async def _add_liabilities_for_adjustment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Liability addition requires many parameters for context and liability tracking
        self,
        player_id: uuid.UUID,
        delta: int,
        previous_lcd: int,
        new_lcd: int,
        previous_tier: str,
        new_tier: str,
        reason_code: str,
    ) -> list[str]:
        """Add liabilities based on delta or tier worsening."""
        liabilities_added: list[str] = []
        if delta < 0 and abs(delta) >= self._liability_threshold:
            liability_code = self._liability_picker(str(player_id), previous_lcd, new_lcd, reason_code)
            if liability_code:
                liability_added = await self.add_liability(player_id, liability_code)
                if liability_added:
                    liabilities_added.append(liability_added)
        elif worsened_tier(previous_tier, new_tier):
            liability_code = self._liability_picker(str(player_id), previous_lcd, new_lcd, reason_code)
            if liability_code:
                liability_added = await self.add_liability(player_id, liability_code)
                if liability_added:
                    liabilities_added.append(liability_added)
        return liabilities_added

    def _get_player_from_record_inspect(self, record: PlayerLucidity) -> object | None:
        """Get player from record's relationship via SQLAlchemy inspect if already loaded. Returns None otherwise."""
        try:
            from sqlalchemy import inspect as sqlalchemy_inspect

            insp = sqlalchemy_inspect(record)
            if not hasattr(insp, "attrs") or "player" not in insp.attrs:
                return None
            attr_state = insp.attrs.player
            loaded_raw = getattr(attr_state, "loaded_value", None)
            if loaded_raw is not None:
                return cast(object, loaded_raw)
            value_raw = getattr(attr_state, "value", None)
            if value_raw is not None:
                return cast(object, value_raw)
            return None
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: inspect can fail in many ways; fallback to explicit load
            logger.debug("Inspect operation failed, falling through to explicit load", exc_info=e)
            return None

    @staticmethod
    def _max_lcd_from_stats(stats: Mapping[str, object]) -> int:
        """Return max_lcd from stats dict (max_lucidity, education, or 100)."""
        raw = stats.get("max_lucidity") or stats.get("education") or 100
        return coerce_int(raw, default=100)

    async def _calculate_max_lcd(self, record: PlayerLucidity, player_id: uuid.UUID) -> int:
        """Calculate max_lcd from player's education stat."""
        default = 100
        player_obj = self._get_player_from_record_inspect(record)
        if player_obj is not None:
            get_stats_fn = getattr(player_obj, "get_stats", None)
            if callable(get_stats_fn):
                try:
                    return self._max_lcd_from_stats(cast(dict[str, object], get_stats_fn()))
                except AttributeError:
                    pass  # Not a real Player (e.g. LoaderCallableStatus); fall through to explicit load
        try:
            from ..models.player import Player

            player = await self._session.get(Player, player_id)
            if player is not None:
                return self._max_lcd_from_stats(player.get_stats())
        except (AttributeError, SQLAlchemyError, TypeError) as e:
            logger.warning(
                "Failed to calculate max_lcd from player stats, using default", player_id=player_id, error=str(e)
            )
        return default

    async def _send_lucidity_change_event_if_needed(
        self,
        player_id: uuid.UUID,
        ctx: LucidityChangeEventContext,
    ) -> None:
        """Send lucidity change event if delta or tier changed."""
        if ctx.delta or ctx.previous_tier != ctx.new_tier:
            max_lcd = await self._calculate_max_lcd(ctx.record, player_id)
            current_lcd_to_send = min(ctx.new_lcd, max_lcd)
            await send_lucidity_change_event(
                player_id=player_id,
                current_lcd=current_lcd_to_send,
                delta=ctx.delta,
                tier=ctx.new_tier,
                extras=LucidityChangeEventExtras(
                    max_lcd=max_lcd,
                    liabilities=decode_liabilities(ctx.record.liabilities),
                    reason=ctx.reason_code,
                    source=lucidity_event_source(ctx.metadata_map, ctx.location_id),
                    metadata=ctx.metadata_map if ctx.metadata_map else None,
                ),
            )

    @staticmethod
    def _apply_delta_to_record(record: PlayerLucidity, delta: int) -> tuple[int, Tier, int, Tier]:
        """Update record LCD/tier from delta; return previous and new LCD/tier values."""
        previous_lcd = record.current_lcd
        previous_tier = record.current_tier
        new_lcd = clamp_lucidity(previous_lcd + delta)
        new_tier = resolve_tier(new_lcd)
        record.current_lcd = new_lcd
        record.current_tier = new_tier
        record.last_updated_at = utc_now()
        return previous_lcd, previous_tier, new_lcd, new_tier

    async def _finalize_lucidity_adjustment(self, ctx: LucidityAdjustmentFinalizeContext) -> LucidityUpdateResult:
        """Persist adjustment logs, liabilities, events, and return the update result."""
        metadata_map = coerce_metadata_dict(ctx.metadata)
        metadata_payload = normalize_metadata(ctx.metadata)
        _ = await self._repo.add_adjustment_log(
            ctx.player_id, ctx.delta, ctx.reason_code, metadata_payload, ctx.location_id
        )
        liabilities_added = await self._add_liabilities_for_adjustment(
            ctx.player_id,
            ctx.delta,
            ctx.previous_lcd,
            ctx.new_lcd,
            ctx.previous_tier,
            ctx.new_tier,
            ctx.reason_code,
        )
        await self._session.flush()
        await self._send_lucidity_change_event_if_needed(
            ctx.player_id,
            LucidityChangeEventContext(
                record=ctx.record,
                delta=ctx.delta,
                previous_tier=ctx.previous_tier,
                new_tier=ctx.new_tier,
                new_lcd=ctx.new_lcd,
                reason_code=ctx.reason_code,
                metadata_map=metadata_map,
                location_id=ctx.location_id,
            ),
        )
        logger.info(
            "Lucidity adjustment applied",
            player_id=ctx.player_id,
            lcd_change=ctx.delta,
            reason=ctx.reason_code,
            tier_before=ctx.previous_tier,
            tier_after=ctx.new_tier,
            liabilities_added=liabilities_added,
        )
        return LucidityUpdateResult(
            player_id=ctx.player_id,
            previous_lcd=ctx.previous_lcd,
            new_lcd=ctx.new_lcd,
            previous_tier=ctx.previous_tier,
            new_tier=ctx.new_tier,
            delta=ctx.delta,
            liabilities_added=liabilities_added,
        )

    async def apply_lucidity_adjustment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Lucidity adjustment requires many parameters for context and adjustment tracking
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: Mapping[str, object] | str | None = None,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        """Apply a LCD delta, log the change, and evaluate liabilities."""
        record = await self._repo.get_or_create_player_lucidity(player_id)
        previous_lcd, previous_tier, new_lcd, new_tier = self._apply_delta_to_record(record, delta)
        await handle_catatonia_transitions(
            record=record,
            player_id=player_id,
            new_tier=new_tier,
            previous_tier=previous_tier,
            new_lcd=new_lcd,
            catatonia_observer=self._catatonia_observer,
        )
        await handle_delirium_and_sanitarium_triggers(player_id, new_lcd, previous_lcd, self._catatonia_observer)
        return await self._finalize_lucidity_adjustment(
            LucidityAdjustmentFinalizeContext(
                player_id=player_id,
                record=record,
                delta=delta,
                reason_code=reason_code,
                previous_lcd=previous_lcd,
                previous_tier=previous_tier,
                new_lcd=new_lcd,
                new_tier=new_tier,
                metadata=metadata,
                location_id=location_id,
            )
        )

    async def add_liability(self, player_id: uuid.UUID, liability_code: str) -> str | None:
        """Add or stack a liability on the player."""

        record = await self._repo.get_or_create_player_lucidity(player_id)
        liabilities = decode_liabilities(record.liabilities)

        for entry in liabilities:
            if entry["code"] == liability_code:
                entry["stacks"] += 1
                record.liabilities = encode_liabilities(liabilities)
                await self._session.flush()
                logger.info(
                    "Liability stack increased",
                    player_id=player_id,
                    liability_code=liability_code,
                    stacks=entry["stacks"],
                )
                return liability_code

        liabilities.append({"code": liability_code, "stacks": 1})
        record.liabilities = encode_liabilities(liabilities)
        await self._session.flush()

        logger.info("Liability added", player_id=player_id, liability_code=liability_code, stacks=1)
        return liability_code

    async def clear_liability(self, player_id: uuid.UUID, liability_code: str, *, remove_all: bool = False) -> bool:
        """Reduce or remove a liability stack."""

        record = await self._repo.get_or_create_player_lucidity(player_id)
        liabilities = decode_liabilities(record.liabilities)

        changed = False
        updated: list[LiabilityStackEntry] = []
        for entry in liabilities:
            if entry["code"] != liability_code:
                updated.append(entry)
                continue

            if remove_all or entry["stacks"] <= 1:
                changed = True
                continue

            entry["stacks"] -= 1
            updated.append(entry)
            changed = True

        if changed:
            record.liabilities = encode_liabilities(updated)
            await self._session.flush()
            logger.info("Liability updated", player_id=player_id, liability_code=liability_code, remove_all=remove_all)
        return changed

    async def get_player_lucidity(self, player_id: uuid.UUID) -> PlayerLucidity:
        """Retrieve the player's lucidity record, creating it if needed."""
        return await self._repo.get_or_create_player_lucidity(player_id)

    async def increment_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> LucidityExposureState:
        """Increment encounter count for a player/entity archetype exposure."""
        return await self._repo.increment_exposure_state(player_id, entity_archetype)

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> LucidityCooldown | None:
        """Retrieve cooldown record for a specific action."""
        return await self._repo.get_cooldown(player_id, action_code)

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> LucidityCooldown:
        """Set or update an action cooldown."""
        return await self._repo.set_cooldown(player_id, action_code, expires_at)

    async def clear_hallucination_timers(self, player_id: uuid.UUID) -> int:
        """
        Clear all hallucination timer cooldowns for a player.

        Used when player enters sanitarium failover state (LCD -100).

        Args:
            player_id: Player ID

        Returns:
            Number of hallucination timers cleared
        """
        # Delete all cooldowns with action_code matching 'hallucination_timer' or 'hallucination_%'
        # Using pattern matching to catch any hallucination-related timers
        deleted_count = await self._repo.delete_cooldowns_by_action_code_pattern(player_id, "hallucination_%")
        if deleted_count > 0:
            logger.info(
                "Hallucination timers cleared for sanitarium failover",
                player_id=player_id,
                timers_cleared=deleted_count,
            )
        return deleted_count

    def _default_liability_picker(
        self, player_id: str, _previous_lcd: int, _new_lcd: int, _reason_code: str
    ) -> str | None:
        """Select the first liability not already applied, falling back to the first option."""
        # This deterministic picker ensures predictable unit tests while allowing overrides.
        # Implementations can provide more complex logic with randomization or weighting.
        existing: set[str] = set()
        # Attempt to read liabilities from session identity map if available.
        # Parse player_id to UUID for identity_key (parameter is str).
        player_id_uuid = uuid.UUID(player_id)
        identity_key = self._session.identity_key(PlayerLucidity, (player_id_uuid,))
        instance = self._session.identity_map.get(identity_key)
        if isinstance(instance, PlayerLucidity):
            for entry in decode_liabilities(instance.liabilities):
                existing.add(entry["code"])

        for code in LIABILITY_CATALOG:
            if code not in existing:
                return code
        return LIABILITY_CATALOG[0] if LIABILITY_CATALOG else None
