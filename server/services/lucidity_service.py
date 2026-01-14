"""Lucidity repository and service for eldritch stability management."""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-lines  # Reason: Lucidity service requires many parameters for context and lucidity operations. Lucidity service requires extensive lucidity management logic for comprehensive eldritch stability tracking.

from __future__ import annotations

import json
import uuid
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Protocol

from sqlalchemy import Select, delete, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..models.lucidity import LucidityAdjustmentLog, LucidityCooldown, LucidityExposureState, PlayerLucidity
from ..structured_logging.enhanced_logging_config import get_logger
from .lucidity_event_dispatcher import (
    send_catatonia_event,
    send_lucidity_change_event,
    send_rescue_update_event,
)

logger = get_logger(__name__)


def _utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


LIABILITY_CATALOG: Sequence[str] = (
    "night_frayed_reflexes",
    "murmuring_chorus",
    "ritual_compulsion",
    "ethereal_chill",
    "bleak_outlook",
)

Tier = str

TIER_ORDER: Sequence[Tier] = ("lucid", "uneasy", "fractured", "deranged", "catatonic")


def resolve_tier(lucidity_value: int) -> Tier:
    """Derive tier label based on LCD thresholds."""
    if lucidity_value >= 70:
        return "lucid"
    if lucidity_value >= 40:
        return "uneasy"
    if lucidity_value >= 20:
        return "fractured"
    if lucidity_value >= 1:
        return "deranged"
    return "catatonic"


def clamp_lucidity(value: int) -> int:
    """Clamp LCD to allowed range."""
    return max(-100, min(100, value))


def decode_liabilities(payload: str | None) -> list[dict[str, Any]]:
    """Decode liability JSON into structured list."""
    if not payload:
        return []
    try:
        data = json.loads(payload)
    except (TypeError, json.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    normalized: list[dict[str, Any]] = []
    for entry in data:
        if isinstance(entry, dict) and "code" in entry:
            code = str(entry["code"])
            stacks = entry.get("stacks", 1)
            try:
                stacks_int = int(stacks)
            except (TypeError, ValueError):
                stacks_int = 1
            normalized.append({"code": code, "stacks": max(1, stacks_int)})
    return normalized


def encode_liabilities(entries: Iterable[dict[str, Any]]) -> str:
    """Serialize liability structures into JSON string."""
    sanitized: list[dict[str, Any]] = []
    for entry in entries:
        code = str(entry.get("code", "")).strip()
        stacks = entry.get("stacks", 1)
        try:
            stacks_int = int(stacks)
        except (TypeError, ValueError):
            stacks_int = 1
        if code:
            sanitized.append({"code": code, "stacks": max(1, stacks_int)})
    return json.dumps(sanitized)


class LucidityRepository:
    """Data-access helpers for lucidity persistence."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_player_lucidity(self, player_id: uuid.UUID) -> PlayerLucidity | None:
        """Get player lucidity record.

        Args:
            player_id: The UUID of the player

        Returns:
            PlayerLucidity | None: The player's lucidity record or None if not found
        """
        stmt: Select[tuple[PlayerLucidity]] = (
            select(PlayerLucidity)
            .options(selectinload(PlayerLucidity.player))
            .where(PlayerLucidity.player_id == player_id)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_or_create_player_lucidity(self, player_id: uuid.UUID) -> PlayerLucidity:
        """Get existing player lucidity record or create a new one.

        Args:
            player_id: The UUID of the player

        Returns:
            PlayerLucidity: The player's lucidity record (existing or newly created)
        """
        record = await self.get_player_lucidity(player_id)
        if record is not None:
            return record

        record = PlayerLucidity(player_id=player_id)
        self._session.add(record)
        await self._session.flush()
        return record

    async def add_adjustment_log(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Adjustment log requires many parameters for complete logging context
        self,
        player_id: uuid.UUID,
        delta: int,
        reason_code: str,
        metadata: str,
        location_id: str | None,
    ) -> LucidityAdjustmentLog:
        """Add a lucidity adjustment log entry.

        Args:
            player_id: The UUID of the player
            delta: The change in lucidity value
            reason_code: Code describing the reason for the adjustment
            metadata: Additional metadata as JSON string
            location_id: Optional location ID where the adjustment occurred

        Returns:
            LucidityAdjustmentLog: The created log entry
        """
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
        """Get exposure state for a player and entity archetype.

        Args:
            player_id: The UUID of the player
            entity_archetype: The entity archetype identifier

        Returns:
            LucidityExposureState | None: The exposure state or None if not found
        """
        stmt: Select[tuple[LucidityExposureState]] = select(LucidityExposureState).where(
            LucidityExposureState.player_id == player_id,
            LucidityExposureState.entity_archetype == entity_archetype,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def increment_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> LucidityExposureState:
        """Increment exposure state for a player and entity archetype.

        Args:
            player_id: The UUID of the player
            entity_archetype: The entity archetype identifier

        Returns:
            LucidityExposureState: The updated or newly created exposure state
        """
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
        """Get cooldown state for a player and action.

        Args:
            player_id: The UUID of the player
            action_code: The action code identifier

        Returns:
            LucidityCooldown | None: The cooldown state or None if not found
        """
        stmt: Select[tuple[LucidityCooldown]] = select(LucidityCooldown).where(
            LucidityCooldown.player_id == player_id,
            LucidityCooldown.action_code == action_code,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> LucidityCooldown:
        """Set or update cooldown for a player and action.

        Args:
            player_id: The UUID of the player
            action_code: The action code identifier
            expires_at: The datetime when the cooldown expires

        Returns:
            LucidityCooldown: The updated or newly created cooldown state
        """
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
        """
        Delete all cooldowns for a player matching an action code pattern.

        Args:
            player_id: Player ID
            action_code_pattern: Action code pattern (e.g., 'hallucination_timer' or 'hallucination_%')

        Returns:
            Number of cooldowns deleted
        """
        stmt = delete(LucidityCooldown).where(
            LucidityCooldown.player_id == player_id,
            LucidityCooldown.action_code.like(action_code_pattern),
        )
        result = await self._session.execute(stmt)
        await self._session.flush()
        # SQLAlchemy Result objects have rowcount attribute at runtime, but mypy stubs don't reflect this
        deleted_count: int = getattr(result, "rowcount", 0)
        return deleted_count


class CatatoniaObserverProtocol(Protocol):
    """Protocol for observers interested in catatonia state changes."""

    def on_catatonia_entered(self, *, player_id: uuid.UUID, entered_at: datetime, current_lcd: int) -> None:
        """Handle a player crossing into catatonia."""

    def on_catatonia_cleared(self, *, player_id: uuid.UUID, resolved_at: datetime) -> None:
        """Handle a player returning from catatonia."""

    def on_sanitarium_failover(self, *, player_id: uuid.UUID, current_lcd: int) -> None:
        """Handle a player requiring sanitarium failover."""


@dataclass
class LucidityUpdateResult:
    """Normalized response describing the outcome of a lucidity adjustment."""

    player_id: uuid.UUID
    previous_lcd: int
    new_lcd: int
    previous_tier: Tier
    new_tier: Tier
    delta: int
    liabilities_added: list[str]


class LucidityService:
    """High-level operations for lucidity adjustments and liability tracking."""

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

    async def _handle_catatonia_transitions(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Catatonia transition handling requires many parameters for context and state updates
        self, record: Any, player_id: uuid.UUID, new_tier: str, previous_tier: str, new_lcd: int
    ) -> None:
        """Handle catatonia entry and exit transitions."""
        if new_tier == "catatonic":
            if record.catatonia_entered_at is None:
                entered_at = _utc_now()
                record.catatonia_entered_at = entered_at
                logger.warning(
                    "Player entered catatonia", player_id=player_id, previous_tier=previous_tier, lcd=new_lcd
                )
                if self._catatonia_observer:
                    self._catatonia_observer.on_catatonia_entered(
                        player_id=player_id, entered_at=entered_at, current_lcd=new_lcd
                    )
                await send_catatonia_event(
                    player_id=player_id,
                    current_lcd=new_lcd,
                    message="Your senses collapse into static; only allies can reach you now.",
                    status="catatonic",
                )
        else:
            if record.catatonia_entered_at is not None:
                resolved_at = _utc_now()
                record.catatonia_entered_at = None
                logger.info("Catatonia resolved", player_id=player_id, tier_after=new_tier, lcd=new_lcd)
                if self._catatonia_observer:
                    self._catatonia_observer.on_catatonia_cleared(player_id=player_id, resolved_at=resolved_at)
                await send_rescue_update_event(
                    player_id=player_id,
                    status="success",
                    current_lcd=new_lcd,
                    message="Consciousness steadies; the grounding ritual completes.",
                )

    async def _handle_delirium_and_sanitarium_triggers(
        self, player_id: uuid.UUID, new_lcd: int, previous_lcd: int
    ) -> None:
        """Handle delirium respawn and sanitarium failover triggers."""
        if new_lcd <= -10 and previous_lcd > -10:
            logger.warning(
                "Delirium respawn threshold reached", player_id=player_id, previous_lcd=previous_lcd, lcd=new_lcd
            )
            await send_rescue_update_event(
                player_id=str(player_id),
                status="delirium",
                current_lcd=new_lcd,
                message="Your mind fractures completely. The sanitarium calls you back from the edge of madness...",
            )

        if new_lcd <= -100 and previous_lcd > -100 and self._catatonia_observer:
            logger.error("Sanitarium failover triggered", player_id=player_id, previous_lcd=previous_lcd, lcd=new_lcd)
            self._catatonia_observer.on_sanitarium_failover(player_id=player_id, current_lcd=new_lcd)
            await send_rescue_update_event(
                player_id=str(player_id),
                status="sanitarium",
                current_lcd=new_lcd,
                message="Orderlies whisk you to Arkham Sanitarium for observation.",
            )

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
        elif self._worsened_tier(previous_tier, new_tier):
            liability_code = self._liability_picker(str(player_id), previous_lcd, new_lcd, reason_code)
            if liability_code:
                liability_added = await self.add_liability(player_id, liability_code)
                if liability_added:
                    liabilities_added.append(liability_added)
        return liabilities_added

    async def _calculate_max_lcd(self, record: Any, player_id: uuid.UUID) -> int:
        """Calculate max_lcd from player's education stat."""
        max_lcd = 100  # Default fallback
        try:
            # Try to safely check if player relationship is already loaded
            # Use inspect to check relationship state without triggering lazy load
            from sqlalchemy import inspect as sqlalchemy_inspect

            player_obj = None
            try:
                insp = sqlalchemy_inspect(record)
                if hasattr(insp, "attrs") and "player" in insp.attrs:
                    attr_state = insp.attrs.player
                    # Check if relationship is loaded using the state's loaded_value or value attribute
                    # loaded_value is set when relationship is eagerly loaded
                    if hasattr(attr_state, "loaded_value") and attr_state.loaded_value is not None:
                        player_obj = attr_state.loaded_value
                    elif hasattr(attr_state, "value") and attr_state.value is not None:
                        player_obj = attr_state.value
            except Exception:
                # If inspect fails (e.g., on new records), fall through to explicit load
                pass

            # Verify player_obj is actually a Player instance (not a LoaderCallableStatus)
            if player_obj is not None and hasattr(player_obj, "get_stats"):
                try:
                    stats = player_obj.get_stats()
                    max_lcd = stats.get("max_lucidity") or stats.get("education") or 100
                except AttributeError:
                    # player_obj is not actually a Player (e.g., LoaderCallableStatus) - fall through to explicit load
                    player_obj = None  # Force explicit load path

            if player_obj is None:
                # Player relationship not loaded or inspect failed - use explicit async load
                from ..models.player import Player

                player = await self._session.get(Player, player_id)
                if player:
                    stats = player.get_stats()
                    max_lcd = stats.get("max_lucidity") or stats.get("education") or 100
        except (AttributeError, SQLAlchemyError, TypeError) as e:
            logger.warning(
                "Failed to calculate max_lcd from player stats, using default", player_id=player_id, error=str(e)
            )
        return max_lcd

    async def _send_lucidity_change_event_if_needed(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event sending requires many parameters for complete event context
        self,
        player_id: uuid.UUID,
        record: Any,
        delta: int,
        previous_tier: str,
        new_tier: str,
        new_lcd: int,
        reason_code: str,
        metadata_map: dict[str, Any],
        location_id: str | None,
    ) -> None:
        """Send lucidity change event if delta or tier changed."""
        if delta or previous_tier != new_tier:
            max_lcd = await self._calculate_max_lcd(record, player_id)
            current_lcd_to_send = min(new_lcd, max_lcd)
            await send_lucidity_change_event(
                player_id=player_id,
                current_lcd=current_lcd_to_send,
                delta=delta,
                tier=new_tier,
                max_lcd=max_lcd,
                liabilities=decode_liabilities(record.liabilities),
                reason=reason_code,
                source=str(
                    metadata_map.get("source")
                    or metadata_map.get("encounter_category")
                    or metadata_map.get("environment")
                    or location_id
                    or ""
                ).strip()
                or None,
                metadata=metadata_map if metadata_map else None,
            )

    async def apply_lucidity_adjustment(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Lucidity adjustment requires many parameters for context and adjustment tracking
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: dict[str, Any] | str | None = None,
        location_id: str | None = None,
    ) -> LucidityUpdateResult:
        """Apply a LCD delta, log the change, and evaluate liabilities."""
        record = await self._repo.get_or_create_player_lucidity(player_id)

        previous_lcd = record.current_lcd
        previous_tier = record.current_tier

        new_lcd = clamp_lucidity(previous_lcd + delta)
        new_tier = resolve_tier(new_lcd)

        record.current_lcd = new_lcd
        record.current_tier = new_tier
        record.last_updated_at = _utc_now()

        await self._handle_catatonia_transitions(record, player_id, new_tier, previous_tier, new_lcd)
        await self._handle_delirium_and_sanitarium_triggers(player_id, new_lcd, previous_lcd)

        metadata_map = self._coerce_metadata_dict(metadata)
        metadata_payload = self._normalize_metadata(metadata)
        await self._repo.add_adjustment_log(player_id, delta, reason_code, metadata_payload, location_id)

        liabilities_added = await self._add_liabilities_for_adjustment(
            player_id, delta, previous_lcd, new_lcd, previous_tier, new_tier, reason_code
        )

        await self._session.flush()

        await self._send_lucidity_change_event_if_needed(
            player_id, record, delta, previous_tier, new_tier, new_lcd, reason_code, metadata_map, location_id
        )

        logger.info(
            "Lucidity adjustment applied",
            player_id=player_id,
            lcd_change=delta,
            reason=reason_code,
            tier_before=previous_tier,
            tier_after=new_tier,
            liabilities_added=liabilities_added,
        )

        return LucidityUpdateResult(
            player_id=player_id,
            previous_lcd=previous_lcd,
            new_lcd=new_lcd,
            previous_tier=previous_tier,
            new_tier=new_tier,
            delta=delta,
            liabilities_added=liabilities_added,
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
        updated: list[dict[str, Any]] = []
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

    def _worsened_tier(self, previous_tier: Tier, new_tier: Tier) -> bool:
        return TIER_ORDER.index(new_tier) > TIER_ORDER.index(previous_tier)

    def _normalize_metadata(self, metadata: dict[str, Any] | str | None) -> str:
        if metadata is None:
            return "{}"
        if isinstance(metadata, str):
            return metadata
        try:
            return json.dumps(metadata)
        except (TypeError, ValueError):
            return "{}"

    def _default_liability_picker(
        self, player_id: str, _previous_lcd: int, _new_lcd: int, _reason_code: str
    ) -> str | None:
        """Select the first liability not already applied, falling back to the first option."""
        # This deterministic picker ensures predictable unit tests while allowing overrides.
        # Implementations can provide more complex logic with randomization or weighting.
        existing = set()
        # Attempt to read liabilities from session identity map if available.
        # Convert string player_id to UUID for identity_key
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        identity_key = self._session.identity_key(PlayerLucidity, (player_id_uuid,))
        instance = self._session.identity_map.get(identity_key)
        if instance is not None:
            for entry in decode_liabilities(instance.liabilities):
                existing.add(entry["code"])

        for code in LIABILITY_CATALOG:
            if code not in existing:
                return code
        return LIABILITY_CATALOG[0] if LIABILITY_CATALOG else None

    def _coerce_metadata_dict(self, metadata: dict[str, Any] | str | None) -> dict[str, Any]:
        """Best-effort conversion of metadata payloads into dictionaries."""
        if metadata is None:
            return {}
        if isinstance(metadata, dict):
            return metadata
        if isinstance(metadata, str):
            try:
                parsed = json.loads(metadata)
            except json.JSONDecodeError:
                return {}
            if isinstance(parsed, dict):
                return parsed
        return {}
