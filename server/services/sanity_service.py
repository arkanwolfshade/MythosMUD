"""Sanity repository and service for eldritch stability management."""

from __future__ import annotations

import json
import uuid
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any, Protocol

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..logging.enhanced_logging_config import get_logger
from ..models.sanity import PlayerSanity, SanityAdjustmentLog, SanityCooldown, SanityExposureState
from .sanity_event_dispatcher import (
    send_catatonia_event,
    send_rescue_update_event,
    send_sanity_change_event,
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


def resolve_tier(sanity_value: int) -> Tier:
    """Derive tier label based on SAN thresholds."""
    if sanity_value >= 70:
        return "lucid"
    if sanity_value >= 40:
        return "uneasy"
    if sanity_value >= 20:
        return "fractured"
    if sanity_value >= 1:
        return "deranged"
    return "catatonic"


def clamp_sanity(value: int) -> int:
    """Clamp SAN to allowed range."""
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


class SanityRepository:
    """Data-access helpers for sanity persistence."""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_player_sanity(self, player_id: uuid.UUID) -> PlayerSanity | None:
        stmt: Select[tuple[PlayerSanity]] = (
            select(PlayerSanity).options(selectinload(PlayerSanity.player)).where(PlayerSanity.player_id == player_id)
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_or_create_player_sanity(self, player_id: uuid.UUID) -> PlayerSanity:
        record = await self.get_player_sanity(player_id)
        if record is not None:
            return record

        record = PlayerSanity(player_id=player_id)
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
    ) -> SanityAdjustmentLog:
        log_entry = SanityAdjustmentLog(
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

    async def get_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> SanityExposureState | None:
        stmt: Select[tuple[SanityExposureState]] = select(SanityExposureState).where(
            SanityExposureState.player_id == player_id,
            SanityExposureState.entity_archetype == entity_archetype,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def increment_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> SanityExposureState:
        exposure = await self.get_exposure_state(player_id, entity_archetype)
        if exposure is None:
            exposure = SanityExposureState(
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

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> SanityCooldown | None:
        stmt: Select[tuple[SanityCooldown]] = select(SanityCooldown).where(
            SanityCooldown.player_id == player_id,
            SanityCooldown.action_code == action_code,
        )
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> SanityCooldown:
        cooldown = await self.get_cooldown(player_id, action_code)
        if cooldown is None:
            cooldown = SanityCooldown(
                player_id=player_id,
                action_code=action_code,
                cooldown_expires_at=expires_at,
            )
            self._session.add(cooldown)
        else:
            cooldown.cooldown_expires_at = expires_at
        await self._session.flush()
        return cooldown


class CatatoniaObserverProtocol(Protocol):
    """Protocol for observers interested in catatonia state changes."""

    def on_catatonia_entered(self, *, player_id: uuid.UUID, entered_at: datetime, current_san: int) -> None:
        """Handle a player crossing into catatonia."""

    def on_catatonia_cleared(self, *, player_id: uuid.UUID, resolved_at: datetime) -> None:
        """Handle a player returning from catatonia."""

    def on_sanitarium_failover(self, *, player_id: uuid.UUID, current_san: int) -> None:
        """Handle a player requiring sanitarium failover."""


@dataclass
class SanityUpdateResult:
    """Normalized response describing the outcome of a sanity adjustment."""

    player_id: uuid.UUID
    previous_san: int
    new_san: int
    previous_tier: Tier
    new_tier: Tier
    delta: int
    liabilities_added: list[str]


class SanityService:
    """High-level operations for sanity adjustments and liability tracking."""

    def __init__(
        self,
        session: AsyncSession,
        liability_picker: Callable[[str, int, int, str], str | None] | None = None,
        liability_threshold: int = 15,
        *,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
    ) -> None:
        self._session = session
        self._repo = SanityRepository(session)
        self._liability_picker = liability_picker or self._default_liability_picker
        self._liability_threshold = liability_threshold
        self._catatonia_observer = catatonia_observer

    async def apply_sanity_adjustment(
        self,
        player_id: uuid.UUID,
        delta: int,
        *,
        reason_code: str,
        metadata: dict[str, Any] | str | None = None,
        location_id: str | None = None,
    ) -> SanityUpdateResult:
        """Apply a SAN delta, log the change, and evaluate liabilities."""

        record = await self._repo.get_or_create_player_sanity(player_id)

        previous_san = record.current_san
        previous_tier = record.current_tier

        new_san = clamp_sanity(previous_san + delta)
        new_tier = resolve_tier(new_san)

        record.current_san = new_san
        record.current_tier = new_tier
        record.last_updated_at = _utc_now()

        # Handle catatonia transitions
        if new_tier == "catatonic":
            if record.catatonia_entered_at is None:
                entered_at = _utc_now()
                record.catatonia_entered_at = entered_at
                logger.warning(
                    "Player entered catatonia",
                    player_id=player_id,
                    previous_tier=previous_tier,
                    san=new_san,
                )
                if self._catatonia_observer:
                    self._catatonia_observer.on_catatonia_entered(
                        player_id=player_id,
                        entered_at=entered_at,
                        current_san=new_san,
                    )
                await send_catatonia_event(
                    player_id=player_id,
                    current_san=new_san,
                    message="Your senses collapse into static; only allies can reach you now.",
                    status="catatonic",
                )
        else:
            if record.catatonia_entered_at is not None:
                resolved_at = _utc_now()
                record.catatonia_entered_at = None
                logger.info(
                    "Catatonia resolved",
                    player_id=player_id,
                    tier_after=new_tier,
                    san=new_san,
                )
                if self._catatonia_observer:
                    self._catatonia_observer.on_catatonia_cleared(
                        player_id=player_id,
                        resolved_at=resolved_at,
                    )
                await send_rescue_update_event(
                    player_id=player_id,
                    status="success",
                    current_san=new_san,
                    message="Consciousness steadies; the grounding ritual completes.",
                )

        if new_san <= -100 and previous_san > -100 and self._catatonia_observer:
            logger.error(
                "Sanitarium failover triggered",
                player_id=player_id,
                previous_san=previous_san,
                san=new_san,
            )
            self._catatonia_observer.on_sanitarium_failover(player_id=player_id, current_san=new_san)
            await send_rescue_update_event(
                player_id=str(player_id),
                status="sanitarium",
                current_san=new_san,
                message="Orderlies whisk you to Arkham Sanitarium for observation.",
            )

        metadata_map = self._coerce_metadata_dict(metadata)
        metadata_payload = self._normalize_metadata(metadata)
        await self._repo.add_adjustment_log(player_id, delta, reason_code, metadata_payload, location_id)

        liabilities_added: list[str] = []
        if delta < 0 and abs(delta) >= self._liability_threshold:
            liability_code = self._liability_picker(str(player_id), previous_san, new_san, reason_code)
            if liability_code:
                liability_added = await self.add_liability(player_id, liability_code)
                if liability_added:
                    liabilities_added.append(liability_added)
        elif self._worsened_tier(previous_tier, new_tier):
            liability_code = self._liability_picker(str(player_id), previous_san, new_san, reason_code)
            if liability_code:
                liability_added = await self.add_liability(player_id, liability_code)
                if liability_added:
                    liabilities_added.append(liability_added)

        await self._session.flush()

        if delta != 0 or previous_tier != new_tier:
            await send_sanity_change_event(
                player_id=player_id,
                current_san=new_san,
                delta=delta,
                tier=new_tier,
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

        logger.info(
            "Sanity adjustment applied",
            player_id=player_id,
            san_change=delta,
            reason=reason_code,
            tier_before=previous_tier,
            tier_after=new_tier,
            liabilities_added=liabilities_added,
        )

        return SanityUpdateResult(
            player_id=player_id,
            previous_san=previous_san,
            new_san=new_san,
            previous_tier=previous_tier,
            new_tier=new_tier,
            delta=delta,
            liabilities_added=liabilities_added,
        )

    async def add_liability(self, player_id: uuid.UUID, liability_code: str) -> str | None:
        """Add or stack a liability on the player."""

        record = await self._repo.get_or_create_player_sanity(player_id)
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

        record = await self._repo.get_or_create_player_sanity(player_id)
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

    async def get_player_sanity(self, player_id: uuid.UUID) -> PlayerSanity:
        """Retrieve the player's sanity record, creating it if needed."""
        return await self._repo.get_or_create_player_sanity(player_id)

    async def increment_exposure_state(self, player_id: uuid.UUID, entity_archetype: str) -> SanityExposureState:
        """Increment encounter count for a player/entity archetype exposure."""
        return await self._repo.increment_exposure_state(player_id, entity_archetype)

    async def get_cooldown(self, player_id: uuid.UUID, action_code: str) -> SanityCooldown | None:
        """Retrieve cooldown record for a specific action."""
        return await self._repo.get_cooldown(player_id, action_code)

    async def set_cooldown(self, player_id: uuid.UUID, action_code: str, expires_at: datetime) -> SanityCooldown:
        """Set or update an action cooldown."""
        return await self._repo.set_cooldown(player_id, action_code, expires_at)

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
        self, player_id: str, previous_san: int, new_san: int, reason_code: str
    ) -> str | None:
        """Select the first liability not already applied, falling back to the first option."""
        # This deterministic picker ensures predictable unit tests while allowing overrides.
        # Implementations can provide more complex logic with randomization or weighting.
        existing = set()
        # Attempt to read liabilities from session identity map if available.
        # Convert string player_id to UUID for identity_key
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        identity_key = self._session.identity_key(PlayerSanity, (player_id_uuid,))
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
