"""Shared lucidity tier, liability, and result types for lucidity services."""

from __future__ import annotations

import json
import uuid
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol, cast

from ..models.lucidity import PlayerLucidity
from ..utils.int_coercion import coerce_int
from ..utils.liability_types import LiabilityStackEntry

LIABILITY_CATALOG: tuple[str, ...] = (
    "night_frayed_reflexes",
    "murmuring_chorus",
    "ritual_compulsion",
    "ethereal_chill",
    "bleak_outlook",
)

Tier = str

TIER_ORDER: tuple[Tier, ...] = ("lucid", "uneasy", "fractured", "deranged", "catatonic")


def utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


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


def decode_liabilities(payload: str | None) -> list[LiabilityStackEntry]:
    """Decode liability JSON into structured list."""
    if not payload:
        return []
    try:
        data = cast(object, json.loads(payload))
    except (TypeError, json.JSONDecodeError):
        return []

    if not isinstance(data, list):
        return []

    items: list[object] = cast(list[object], data)
    normalized: list[LiabilityStackEntry] = []
    for entry in items:
        if isinstance(entry, dict) and "code" in entry:
            row = cast(dict[str, object], entry)
            code = str(row["code"])
            stacks_int = coerce_int(row.get("stacks", 1), default=1)
            normalized.append({"code": code, "stacks": max(1, stacks_int)})
    return normalized


def encode_liabilities(entries: Iterable[LiabilityStackEntry]) -> str:
    """Serialize liability structures into JSON string."""
    sanitized: list[LiabilityStackEntry] = []
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


def worsened_tier(previous_tier: Tier, new_tier: Tier) -> bool:
    """Return True when the new tier is worse than the previous tier."""
    return TIER_ORDER.index(new_tier) > TIER_ORDER.index(previous_tier)


class CatatoniaObserverProtocol(Protocol):
    """Protocol for observers interested in catatonia state changes."""

    def on_catatonia_entered(self, *, player_id: uuid.UUID, entered_at: datetime, current_lcd: int) -> None:
        """Handle a player crossing into catatonia."""

    def on_catatonia_cleared(self, *, player_id: uuid.UUID, resolved_at: datetime) -> None:
        """Handle a player returning from catatonia."""

    def on_sanitarium_failover(self, *, player_id: uuid.UUID, current_lcd: int) -> None:
        """Handle a player requiring sanitarium failover."""

    def should_trigger_sanitarium_failover(self, player_id: uuid.UUID | str) -> bool:
        """Return False to suppress failover (debounce); True allows failover handling."""
        return True  # Structural Protocol stub; concrete observers (e.g. CatatoniaRegistry) override.


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


@dataclass(frozen=True)
class LucidityChangeEventContext:
    """Context for sending a lucidity change event (reduces parameter count)."""

    record: PlayerLucidity
    delta: int
    previous_tier: str
    new_tier: str
    new_lcd: int
    reason_code: str
    metadata_map: dict[str, object]
    location_id: str | None


@dataclass(frozen=True)
class LucidityAdjustmentFinalizeContext:
    """Context for persisting logs, liabilities, and events after an LCD change."""

    player_id: uuid.UUID
    record: PlayerLucidity
    delta: int
    reason_code: str
    previous_lcd: int
    previous_tier: str
    new_lcd: int
    new_tier: str
    metadata: Mapping[str, object] | str | None
    location_id: str | None


def normalize_metadata(metadata: Mapping[str, object] | str | None) -> str:
    """Serialize metadata for persistence."""
    if metadata is None:
        return "{}"
    if isinstance(metadata, str):
        return metadata
    try:
        return json.dumps(metadata)
    except (TypeError, ValueError):
        return "{}"


def coerce_metadata_dict(metadata: Mapping[str, object] | str | None) -> dict[str, object]:
    """Best-effort conversion of metadata payloads into dictionaries."""
    if metadata is None:
        return {}
    if isinstance(metadata, dict):
        return dict(metadata)
    if isinstance(metadata, str):
        try:
            parsed = cast(object, json.loads(metadata))
        except json.JSONDecodeError:
            return {}
        if isinstance(parsed, dict):
            return cast(dict[str, object], parsed)
    return {}


def lucidity_event_source(metadata_map: Mapping[str, object], location_id: str | None) -> str | None:
    """Build source string for lucidity change event from metadata and location."""
    raw = (
        metadata_map.get("source")
        or metadata_map.get("encounter_category")
        or metadata_map.get("environment")
        or location_id
        or ""
    )
    return str(raw).strip() or None
