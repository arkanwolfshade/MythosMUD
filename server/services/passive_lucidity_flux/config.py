"""Configuration and normalization for passive lucidity flux."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any

from .models import PassiveFluxContext

if TYPE_CHECKING:
    from ...models.player import Player


@dataclass
class FluxServiceConfig:
    """Optional configuration for PassiveLucidityFluxService. All fields have defaults."""

    environment_config: dict[str, Any] | None = None
    ticks_per_minute: int = 6
    adaptive_window_minutes: int = 10
    context_resolver: Callable[[Player, datetime], PassiveFluxContext] | None = None
    now_provider: Callable[[], datetime] | None = None
    lucidity_rate_overrides: dict[str, float] | None = None


DEFAULT_ENVIRONMENT_CONFIG: dict[str, Any] = {
    "default": 0.0,
    "environment_defaults": {
        # Recovery anchors
        "sun_sanctuary": {"day": 0.6, "night": 0.3},
        "sanctuary": {"day": 0.6, "night": 0.3},
        "temple": {"day": 0.6, "night": 0.3},
        "street_paved": {"day": 0.2, "night": 0.0},  # Neutral civic zones
        "camp": {"day": 0.2, "night": 0.2},
        "safehouse": {"day": 0.6, "night": 0.3},
        # Drain zones
        "graveyard": {"day": -0.4, "night": -0.8},
        "haunted": {"day": -0.4, "night": -0.8},
        "eldritch": {"day": -1.2, "night": -1.5},
        "storm": {"day": -0.3, "night": -0.3},
        "forsaken": {"day": -0.5, "night": -0.2},
        # Generic fallback for common values
        "indoors": {"day": 0.0, "night": 0.0},
        "outdoors": {"day": 0.0, "night": 0.0},
    },
    "sub_zone_overrides": {
        "sanitarium": {"all": -0.5},
    },
    "room_overrides": {},
}


def period_label(timestamp: datetime) -> str:
    """Return a coarse period label used for environment profiles."""
    hour = timestamp.hour
    if 6 <= hour < 18:
        return "day"
    return "night"


def normalize_environment_config(config: dict[str, Any]) -> dict[str, Any]:
    """Normalize environment config to validated structure."""

    def _normalize_profile(profile: dict[str, float]) -> dict[str, float]:
        return {
            key: float(value)
            for key, value in profile.items()
            if key in {"day", "night", "all"} and isinstance(value, int | float)
        }

    normalized = {
        "default": config.get("default", 0.0),
        "environment_defaults": {},
        "sub_zone_overrides": {},
        "room_overrides": {},
    }

    for key, profile in config.get("environment_defaults", {}).items():
        if isinstance(profile, dict):
            normalized["environment_defaults"][key] = _normalize_profile(profile)

    for key, profile in config.get("sub_zone_overrides", {}).items():
        if isinstance(profile, dict):
            normalized["sub_zone_overrides"][key] = _normalize_profile(profile)

    for key, profile in config.get("room_overrides", {}).items():
        if isinstance(profile, dict):
            normalized["room_overrides"][key] = _normalize_profile(profile)

    return normalized


def lookup_profile(profile: dict[str, float], period: str, default: float) -> float:
    """Look up flux value from profile by period."""
    if period in profile:
        return profile[period]
    if "all" in profile:
        return profile["all"]
    return default
