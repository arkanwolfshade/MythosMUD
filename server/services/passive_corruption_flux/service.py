"""
Passive corruption flux scheduler (#815 PR-5).

Deliberately much smaller than passive_lucidity_flux.service.LucidityFluxService: the plan for
this PR calls out exactly five concerns -- rate resolution, residual accumulation, bounds, tick
cadence, and the write path -- and none of lucidity's companion modifiers, adaptive camping
resistance, or hallucination triggers apply here. Building those in would be unrequested scope,
not fidelity to "follow the lucidity model."

The one genuine difference from lucidity's engine: lucidity zones supply a *signed* flux value
directly (a drain zone is negative, a recovery zone is positive). Corruption rooms instead supply
a *target* a lingering player converges toward, plus a *rate* magnitude -- the sign of the actual
flux is derived per player by comparing their current value to the room's target. A room can't
supply a fixed sign the way lucidity's zones do, because the same corrupt room must pull a pure
player up and push an already-more-corrupt player down toward the same point.
"""

from __future__ import annotations

import math
import uuid
from collections.abc import Callable, Mapping
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Protocol, cast

from sqlalchemy.exc import DatabaseError, SQLAlchemyError

from ...models.corruption import CorruptionTier, compute_tier
from ...structured_logging.enhanced_logging_config import get_logger
from ...utils.int_coercion import coerce_int
from ..corruption_service import CorruptionPersistenceProtocol, CorruptionService
from .config import (
    DEFAULT_ENVIRONMENT_CONFIG,
    CorruptionFluxServiceConfig,
    CorruptionOverride,
    lookup_profile,
    period_label,
)
from .models import PassiveCorruptionFluxContext
from .rate_overrides import build_override_key, load_corruption_overrides

if TYPE_CHECKING:
    from ...async_persistence import AsyncPersistenceLayer
    from ...models.player import Player

logger = get_logger(__name__)

__all__ = ["FluxRoom", "PassiveCorruptionFluxService"]


class FluxRoom(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Room fields used for corruption flux resolution."""

    id: str
    sub_zone: str
    zone: str
    plane: str
    environment: str
    attributes: dict[str, object]


def _as_str_attr(value: object, default: str = "") -> str:
    return value if isinstance(value, str) else default


def _as_float(value: object, default: float = 0.0) -> float:
    return float(value) if isinstance(value, int | float) else default


def _profile_map(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, dict):
        return {}
    raw_dict = cast(dict[object, object], raw)
    out: dict[str, dict[str, float]] = {}
    for key, profile in raw_dict.items():
        if isinstance(key, str) and isinstance(profile, dict):
            profile_dict = cast(dict[object, object], profile)
            out[key] = {str(pk): _as_float(pv) for pk, pv in profile_dict.items()}
    return out


class PassiveCorruptionFluxService:
    """Converges lingering players' corruption toward each room's target, each ~0.6s tick."""

    _persistence: AsyncPersistenceLayer | None
    _default_rate: float
    _default_target: float
    _environment_rate_defaults: dict[str, dict[str, float]]
    _environment_target_defaults: dict[str, dict[str, float]]
    _sub_zone_rate_overrides: dict[str, dict[str, float]]
    _sub_zone_target_overrides: dict[str, dict[str, float]]
    _room_rate_overrides: dict[str, dict[str, float]]
    _room_target_overrides: dict[str, dict[str, float]]
    _ticks_per_minute: int
    _context_resolver: Callable[[Player, datetime], PassiveCorruptionFluxContext] | None
    _now_provider: Callable[[], datetime]
    _db_overrides: dict[str, CorruptionOverride]
    _epsilon: float
    _residuals: dict[str, float]

    def __init__(
        self,
        persistence: AsyncPersistenceLayer | None = None,
        *,
        config: CorruptionFluxServiceConfig | None = None,
    ) -> None:
        cfg = config or CorruptionFluxServiceConfig()
        self._persistence = persistence
        env_cfg = cfg.environment_config or DEFAULT_ENVIRONMENT_CONFIG
        self._default_rate = _as_float(env_cfg.get("default_rate"))
        self._default_target = _as_float(env_cfg.get("default_target"))
        self._environment_rate_defaults = _profile_map(env_cfg.get("environment_rate_defaults"))
        self._environment_target_defaults = _profile_map(env_cfg.get("environment_target_defaults"))
        self._sub_zone_rate_overrides = _profile_map(env_cfg.get("sub_zone_rate_overrides"))
        self._sub_zone_target_overrides = _profile_map(env_cfg.get("sub_zone_target_overrides"))
        self._room_rate_overrides = _profile_map(env_cfg.get("room_rate_overrides"))
        self._room_target_overrides = _profile_map(env_cfg.get("room_target_overrides"))
        self._ticks_per_minute = max(1, cfg.ticks_per_minute)
        self._context_resolver = cfg.context_resolver
        self._now_provider = cfg.now_provider or (lambda: datetime.now(UTC))
        self._db_overrides = (
            cfg.corruption_overrides if cfg.corruption_overrides is not None else load_corruption_overrides()
        )
        self._epsilon = 1e-6
        self._residuals = {}

        logger.info(
            "PassiveCorruptionFluxService initialized",
            ticks_per_minute=self._ticks_per_minute,
            db_overrides=len(self._db_overrides),
        )

    def _should_process_tick(self, tick_count: int) -> bool:
        return self._ticks_per_minute <= 1 or not tick_count % self._ticks_per_minute

    def _get_room(self, room_id: str) -> FluxRoom | None:
        if self._persistence is None:
            return None
        try:
            return cast(FluxRoom, self._persistence.get_room_by_id(room_id))
        except (DatabaseError, SQLAlchemyError) as exc:  # pragma: no cover - defensive logging
            logger.warning("Failed to resolve room for corruption flux", room_id=room_id, error=str(exc))
            return None

    def _lookup_rate_for_room(self, room: FluxRoom, period: str) -> tuple[float, str]:
        room_id = _as_str_attr(room.id)
        sub_zone = _as_str_attr(room.sub_zone)
        zone = _as_str_attr(room.zone)
        environment = _as_str_attr(room.environment)

        if room_id in self._room_rate_overrides:
            return lookup_profile(self._room_rate_overrides[room_id], period, self._default_rate), f"room:{room_id}"
        if sub_zone in self._sub_zone_rate_overrides:
            return (
                lookup_profile(self._sub_zone_rate_overrides[sub_zone], period, self._default_rate),
                f"sub_zone:{sub_zone}",
            )
        if zone in self._sub_zone_rate_overrides:
            return lookup_profile(self._sub_zone_rate_overrides[zone], period, self._default_rate), f"zone:{zone}"
        if environment in self._environment_rate_defaults:
            return (
                lookup_profile(self._environment_rate_defaults[environment], period, self._default_rate),
                f"environment:{environment}",
            )
        return self._default_rate, "default"

    def _lookup_target_for_room(self, room: FluxRoom, period: str) -> tuple[float, str]:
        # Room's own attributes.corruption takes precedence over everything -- authored the same
        # way NPC base_stats corruption is (#815 PR-4), no DDL required.
        own_corruption = room.attributes.get("corruption")
        if isinstance(own_corruption, int | float):
            return float(own_corruption), f"room:{_as_str_attr(room.id)}"

        room_id = _as_str_attr(room.id)
        sub_zone = _as_str_attr(room.sub_zone)
        zone = _as_str_attr(room.zone)
        environment = _as_str_attr(room.environment)

        if room_id in self._room_target_overrides:
            return (
                lookup_profile(self._room_target_overrides[room_id], period, self._default_target),
                f"room:{room_id}",
            )
        if sub_zone in self._sub_zone_target_overrides:
            return (
                lookup_profile(self._sub_zone_target_overrides[sub_zone], period, self._default_target),
                f"sub_zone:{sub_zone}",
            )
        if zone in self._sub_zone_target_overrides:
            return (
                lookup_profile(self._sub_zone_target_overrides[zone], period, self._default_target),
                f"zone:{zone}",
            )
        if environment in self._environment_target_defaults:
            return (
                lookup_profile(self._environment_target_defaults[environment], period, self._default_target),
                f"environment:{environment}",
            )
        return self._default_target, "default"

    def _lookup_db_override(self, room: FluxRoom) -> CorruptionOverride | None:
        if not self._db_overrides:
            return None
        plane = _as_str_attr(room.plane)
        zone = _as_str_attr(room.zone)
        sub_zone = _as_str_attr(room.sub_zone)
        for key in (
            build_override_key(plane, zone, sub_zone),
            build_override_key(plane, zone, None),
            build_override_key(plane, None, None),
        ):
            override = self._db_overrides.get(key)
            if override is not None:
                return override
        return None

    def _resolve_context(self, room: FluxRoom | None, timestamp: datetime) -> PassiveCorruptionFluxContext:
        if room is None:
            return PassiveCorruptionFluxContext(target=self._default_target, rate=self._default_rate, source="no_room")

        period = period_label(timestamp)
        rate, rate_source = self._lookup_rate_for_room(room, period)
        target, target_source = self._lookup_target_for_room(room, period)
        source = target_source if target != self._default_target else rate_source

        db_override = self._lookup_db_override(room)
        if db_override is not None:
            if db_override.rate is not None:
                rate = db_override.rate
                source = "db_override"
            if db_override.target is not None:
                target = db_override.target
                source = "db_override"

        tags = frozenset({_as_str_attr(room.environment)})
        metadata: dict[str, object] = {
            "room_id": _as_str_attr(room.id),
            "zone": _as_str_attr(room.zone),
            "sub_zone": _as_str_attr(room.sub_zone),
        }
        return PassiveCorruptionFluxContext(target=target, rate=rate, tags=tags, source=source, metadata=metadata)

    def _apply_residual(self, player_id: str, signed_flux: float) -> int:
        """Fractional-to-integer bank, identical in shape to passive_lucidity_flux's -- a slow
        rate still produces clean integer deltas instead of rounding away to nothing every tick."""
        previous_residual = self._residuals.get(player_id, 0.0)
        residual = previous_residual + signed_flux
        delta = 0

        if residual >= 1.0 - self._epsilon:
            delta = math.floor(residual + self._epsilon)
        elif residual <= -1.0 + self._epsilon:
            delta = math.ceil(residual - self._epsilon)

        residual -= delta
        self._residuals[player_id] = residual
        return delta

    @staticmethod
    def _tier_floor(current_value: int) -> int:
        """Bottom of the player's CURRENT tier -- a purifying room cleanses within a tier but
        never crosses a tier boundary downward on its own; only /cleanse does that (#815)."""
        tier = compute_tier(current_value)
        if tier is CorruptionTier.WARPED:
            return 75
        if tier is CorruptionTier.CORRUPTED:
            return 50
        if tier is CorruptionTier.MARKED:
            return 25
        if tier is CorruptionTier.TOUCHED:
            return 1
        return 0

    @staticmethod
    def _signed_flux_toward_target(current: int, target: float, rate: float) -> float:
        """Direction is derived from current-vs-target; a room can't supply a fixed sign the way
        a lucidity drain/recovery zone does (see module docstring)."""
        if current < target:
            return rate
        if current > target:
            return -rate
        return 0.0

    def _bound_delta(self, current: int, raw_delta: int, target: float) -> int:
        """Clamp the residual bank's raw delta to the room's ceiling (rising) or the player's
        current tier floor (falling) -- only /cleanse crosses a tier boundary downward (#815)."""
        proposed = current + raw_delta
        if raw_delta > 0:
            bounded = min(proposed, int(round(target)))
        else:
            bounded = max(proposed, self._tier_floor(current))
        return bounded - current

    async def _resolve_player_and_context(
        self, player_id: uuid.UUID, timestamp: datetime
    ) -> tuple[Player, FluxRoom | None, PassiveCorruptionFluxContext] | None:
        """Load the player and their room, and resolve this tick's flux context. None on any
        missing prerequisite (no persistence, unknown player)."""
        if self._persistence is None:
            return None
        player = await self._persistence.get_player_by_id(player_id)
        if player is None:
            return None
        room_id = player.current_room_id
        room = self._get_room(room_id) if room_id else None
        context = (
            self._context_resolver(player, timestamp)
            if self._context_resolver
            else self._resolve_context(room, timestamp)
        )
        return player, room, context

    async def process_tick_for_player(
        self, player_id: uuid.UUID, tick_count: int, *, now: datetime | None = None
    ) -> Mapping[str, object]:
        """Evaluate and, if warranted, apply one player's room corruption flux for this tick."""
        if not self._should_process_tick(tick_count):
            return {"delta": 0}

        timestamp = now or self._now_provider()
        resolved = await self._resolve_player_and_context(player_id, timestamp)
        if resolved is None:
            return {"delta": 0}
        player, room, context = resolved

        current = coerce_int(player.get_stats().get("corruption", 0), default=0)
        signed_flux = self._signed_flux_toward_target(current, context.target, context.rate)
        raw_delta = self._apply_residual(str(player_id), signed_flux)
        if not raw_delta:
            return {"delta": 0}

        actual_delta = self._bound_delta(current, raw_delta, context.target)
        if not actual_delta:
            return {"delta": 0}

        if self._persistence is None:  # pragma: no cover - _resolve_player_and_context already guarded this
            return {"delta": 0}
        # Cast needed: AsyncPersistenceLayer.save_player(player: Player) doesn't structurally
        # satisfy CorruptionPersistenceProtocol's (player: CorruptionPersistencePlayer) parameter
        # under strict contravariance, even though Player satisfies CorruptionPersistencePlayer --
        # same cast as game/mechanics.py's apply_corruption.
        persistence = cast(CorruptionPersistenceProtocol, cast(object, self._persistence))
        result = await CorruptionService(persistence).apply_corruption_adjustment(
            player_id,
            actual_delta,
            reason_code="room_flux",
            location_id=_as_str_attr(room.id) if room else None,
            metadata={
                "source": context.source,
                "target": context.target,
                "rate": context.rate,
                "tick_count": tick_count,
            },
        )
        return {"delta": actual_delta, "new_value": result.new_value}
