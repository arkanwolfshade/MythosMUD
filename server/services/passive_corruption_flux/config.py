"""Configuration for passive corruption flux (#815 PR-5).

`period_label`, `normalize_environment_config`, and `lookup_profile` are pure, data-agnostic
string/dict helpers with nothing lucidity-specific in them -- reused directly from
passive_lucidity_flux.config rather than duplicated here.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from ..passive_lucidity_flux.config import lookup_profile, normalize_environment_config, period_label
from .models import PassiveCorruptionFluxContext

if TYPE_CHECKING:
    from ...models.player import Player

__all__ = [
    "DEFAULT_ENVIRONMENT_CONFIG",
    "CorruptionFluxServiceConfig",
    "CorruptionOverride",
    "lookup_profile",
    "normalize_environment_config",
    "period_label",
]


@dataclass(frozen=True)
class CorruptionOverride:
    """A zone/subzone-level override for corruption flux rate and/or target (#815)."""

    rate: float | None = None
    target: float | None = None


@dataclass
class CorruptionFluxServiceConfig:
    """Optional configuration for PassiveCorruptionFluxService. All fields have defaults."""

    environment_config: dict[str, object] | None = None
    ticks_per_minute: int = 6
    context_resolver: Callable[[Player, datetime], PassiveCorruptionFluxContext] | None = None
    now_provider: Callable[[], datetime] | None = None
    corruption_overrides: dict[str, CorruptionOverride] | None = None


# Rate is a magnitude (points per invocation, roughly once every 0.6s -- see service.py's
# _should_process_tick), not a signed flux: the room's target decides direction, this decides
# speed. Target is the corruption value a lingering player converges toward; 0 (the default) means
# "no ambient effect at all" rather than "pulls toward purity" -- only a room/zone that explicitly
# sets a target does anything.
DEFAULT_ENVIRONMENT_CONFIG: dict[str, object] = {
    "default_rate": 0.0,
    "default_target": 0.0,
    "environment_rate_defaults": {
        "eldritch": {"day": 0.03, "night": 0.06},
        "haunted": {"day": 0.02, "night": 0.04},
        "graveyard": {"day": 0.02, "night": 0.03},
    },
    "environment_target_defaults": {
        "eldritch": {"all": 80.0},
        "haunted": {"all": 60.0},
        "graveyard": {"all": 40.0},
    },
    "sub_zone_rate_overrides": {},
    "sub_zone_target_overrides": {},
    "room_rate_overrides": {},
    "room_target_overrides": {},
}
