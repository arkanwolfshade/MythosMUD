"""Passive SAN flux scheduler guided by the Pnakotic curricula."""

from __future__ import annotations

import math
import time
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, cast

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..logging.enhanced_logging_config import get_logger
from ..models.player import Player
from ..models.sanity import PlayerSanity
from ..persistence import PersistenceLayer
from ..services.sanity_service import CatatoniaObserverProtocol, SanityService, SanityUpdateResult

try:
    from ..monitoring.performance_monitor import PerformanceMonitor
except ImportError:  # pragma: no cover - monitoring is optional in some test harnesses
    PerformanceMonitor = None  # type: ignore[misc,assignment]

logger = get_logger(__name__)


@dataclass(frozen=True)
class PassiveFluxContext:
    """Resolved environmental context for passive flux evaluation."""

    base_flux: float
    tags: frozenset[str] = field(default_factory=frozenset)
    source: str = "unspecified"
    metadata: dict[str, Any] = field(default_factory=dict)


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


def _period_label(timestamp: datetime) -> str:
    """Return a coarse period label used for environment profiles."""
    hour = timestamp.hour
    if 6 <= hour < 18:
        return "day"
    return "night"


class PassiveSanityFluxService:
    """Applies passive SAN flux each in-game minute with structured telemetry."""

    def __init__(
        self,
        persistence: PersistenceLayer | None = None,
        performance_monitor: PerformanceMonitor | None = None,
        *,
        environment_config: dict[str, Any] | None = None,
        ticks_per_minute: int = 6,
        adaptive_window_minutes: int = 10,
        context_resolver: Callable[[Player, datetime], PassiveFluxContext] | None = None,
        now_provider: Callable[[], datetime] | None = None,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
        sanity_rate_overrides: dict[str, float] | None = None,
    ) -> None:
        self._persistence = persistence
        self._performance_monitor = performance_monitor
        self._environment_config = self._normalize_environment_config(environment_config or DEFAULT_ENVIRONMENT_CONFIG)
        self._ticks_per_minute = max(1, ticks_per_minute)
        self._adaptive_window = max(1, adaptive_window_minutes)
        self._epsilon = 1e-6
        self._context_resolver = context_resolver
        self._now_provider = now_provider or (lambda: datetime.now(UTC))
        self._catatonia_observer = catatonia_observer
        self._sanity_rate_overrides = (
            sanity_rate_overrides if sanity_rate_overrides is not None else self._load_sanity_rate_overrides()
        )

        self._residuals: dict[str, float] = {}
        self._player_room_tracker: dict[str, dict[str, Any]] = {}

        logger.info(
            "PassiveSanityFluxService initialized",
            ticks_per_minute=self._ticks_per_minute,
            adaptive_window_minutes=self._adaptive_window,
        )

    async def process_tick(
        self, session: AsyncSession, tick_count: int, *, now: datetime | None = None
    ) -> dict[str, Any]:
        """Evaluate passive SAN flux for the current tick."""
        if not self._should_process_tick(tick_count):
            return {"evaluated": 0, "adjustments": 0, "skipped": True}

        evaluation_start = time.perf_counter()
        timestamp = now or self._now_provider()
        processed_player_ids: set[str] = set()
        adjustments: list[SanityUpdateResult] = []
        sanity_service = SanityService(session, catatonia_observer=self._catatonia_observer)

        try:
            players = await self._load_players(session)
            sanity_records = await self._load_sanity_records(session)

            for player in players:
                player_id = cast(str, player.player_id)
                room_id = cast(str, player.current_room_id)

                processed_player_ids.add(player_id)
                context = self._resolve_context(player, timestamp)
                base_flux = context.base_flux

                companion_flux = self._companion_modifier(player, players, sanity_records)
                total_flux = base_flux + companion_flux

                total_flux = self._apply_adaptive_resistance(player_id, room_id, total_flux)
                delta = self._apply_residual(player_id, total_flux)

                if delta == 0:
                    continue

                result = await sanity_service.apply_sanity_adjustment(
                    player_id,
                    delta,
                    reason_code="passive_flux",
                    metadata={
                        "context_tags": list(context.tags),
                        "source": context.source,
                        "base_flux": base_flux,
                        "companion_flux": companion_flux,
                        "total_flux": total_flux,
                        "tick_count": tick_count,
                        **context.metadata,
                    },
                )
                adjustments.append(result)

            if adjustments:
                await session.commit()
            self._prune_trackers(processed_player_ids)

            duration_ms = (time.perf_counter() - evaluation_start) * 1000
            self._emit_telemetry(duration_ms, len(players), len(adjustments), True)

            if adjustments:
                for result in adjustments:
                    logger.info(
                        "Passive SAN flux applied",
                        player_id=result.player_id,
                        san_change=result.delta,
                        previous_san=result.previous_san,
                        new_san=result.new_san,
                        tier_before=result.previous_tier,
                        tier_after=result.new_tier,
                    )

            return {
                "evaluated": len(players),
                "adjustments": len(adjustments),
                "skipped": False,
            }
        except Exception as exc:  # pragma: no cover - defensive logging
            await session.rollback()
            duration_ms = (time.perf_counter() - evaluation_start) * 1000
            self._emit_telemetry(duration_ms, 0, 0, False, error=str(exc))
            logger.error("Passive SAN flux tick failed", error=str(exc))
            raise

    def _should_process_tick(self, tick_count: int) -> bool:
        return self._ticks_per_minute <= 1 or tick_count % self._ticks_per_minute == 0

    async def _load_players(self, session: AsyncSession) -> Sequence[Player]:
        stmt: Select[tuple[Player]] = select(Player)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def _load_sanity_records(self, session: AsyncSession) -> dict[str, PlayerSanity]:
        stmt: Select[tuple[PlayerSanity]] = select(PlayerSanity)
        result = await session.execute(stmt)
        records = result.scalars().all()
        return {str(record.player_id): record for record in records}

    def _resolve_context(self, player: Player, timestamp: datetime) -> PassiveFluxContext:
        if self._context_resolver is not None:
            return self._context_resolver(player, timestamp)

        room = None
        if self._persistence is not None:
            try:
                room = self._persistence.get_room(str(player.current_room_id))
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.warning(
                    "Failed to resolve room for passive flux",
                    player_id=player.player_id,
                    room_id=str(player.current_room_id),
                    error=str(exc),
                )

        period = _period_label(timestamp)
        profile_source = "default"
        base_flux = self._environment_config["default"]
        tags: set[str] = set()
        metadata: dict[str, Any] = {
            "room_id": str(player.current_room_id),
        }

        if room is not None:
            tags.add(room.environment)
            metadata["zone"] = room.zone
            metadata["sub_zone"] = room.sub_zone

            room_overrides = self._environment_config["room_overrides"]
            subzone_overrides = self._environment_config["sub_zone_overrides"]
            environment_defaults = self._environment_config["environment_defaults"]

            if room.id in room_overrides:
                base_flux = self._lookup_profile(room_overrides[room.id], period)
                profile_source = f"room:{room.id}"
            elif room.sub_zone in subzone_overrides:
                base_flux = self._lookup_profile(subzone_overrides[room.sub_zone], period)
                profile_source = f"sub_zone:{room.sub_zone}"
            elif room.zone in subzone_overrides:
                base_flux = self._lookup_profile(subzone_overrides[room.zone], period)
                profile_source = f"zone:{room.zone}"
            elif room.environment in environment_defaults:
                base_flux = self._lookup_profile(environment_defaults[room.environment], period)
                profile_source = f"environment:{room.environment}"

            override_flux, override_source = self._lookup_world_override_flux(room)
            if override_flux is not None:
                base_flux = override_flux
                profile_source = override_source or profile_source
                metadata["sanity_rate_override"] = True
        else:
            metadata["zone"] = None
            metadata["sub_zone"] = None

        return PassiveFluxContext(base_flux=base_flux, tags=frozenset(tags), source=profile_source, metadata=metadata)

    def _lookup_profile(self, profile: dict[str, float], period: str) -> float:
        if period in profile:
            return profile[period]
        if "all" in profile:
            return profile["all"]
        return self._environment_config["default"]

    def _companion_modifier(
        self,
        player: Player,
        players: Sequence[Player],
        sanity_records: dict[str, PlayerSanity],
    ) -> float:
        companions = [
            other
            for other in players
            if other.player_id != player.player_id and other.current_room_id == player.current_room_id
        ]
        if not companions:
            return 0.0

        lucid_companions = 0
        has_destabilizing_companion = False

        for companion in companions:
            record = sanity_records.get(cast(str, companion.player_id))
            tier = record.current_tier if record else "lucid"

            if tier in {"lucid", "uneasy"}:
                lucid_companions += 1
            if tier in {"deranged", "catatonic"}:
                has_destabilizing_companion = True

        companion_flux = min(lucid_companions * 0.1, 0.3)
        if has_destabilizing_companion:
            companion_flux += -0.2
        return companion_flux

    def _apply_adaptive_resistance(self, player_id: str, room_id: str, flux: float) -> float:
        tracker = self._player_room_tracker.get(player_id)
        if tracker is None or tracker["room_id"] != room_id:
            self._player_room_tracker[player_id] = {"room_id": room_id, "minutes": 1}
            return flux

        tracker["minutes"] += 1
        minutes = tracker["minutes"]

        if flux >= 0:
            return flux

        # Determine reduction steps: each full adaptive window after the first reduces magnitude by 25%, min 50%
        steps = max(0, min((minutes - 1) // self._adaptive_window, 2))
        multiplier = max(0.5, 1.0 - (steps * 0.25))
        return flux * multiplier

    def _apply_residual(self, player_id: str, flux: float) -> int:
        residual = self._residuals.get(player_id, 0.0) + flux
        delta = 0

        if residual >= 1.0 - self._epsilon:
            delta = math.floor(residual + self._epsilon)
        elif residual <= -1.0 + self._epsilon:
            delta = math.ceil(residual - self._epsilon)

        residual -= delta
        self._residuals[player_id] = residual
        return delta

    def _prune_trackers(self, active_player_ids: Iterable[str]) -> None:
        active_set = set(active_player_ids)
        self._residuals = {pid: residual for pid, residual in self._residuals.items() if pid in active_set}
        self._player_room_tracker = {
            pid: tracker for pid, tracker in self._player_room_tracker.items() if pid in active_set
        }

    def _emit_telemetry(
        self,
        duration_ms: float,
        evaluated_players: int,
        applied_adjustments: int,
        success: bool,
        error: str | None = None,
    ) -> None:
        if self._performance_monitor is not None:
            metadata: dict[str, int | str] = {
                "evaluated_players": evaluated_players,
                "applied_adjustments": applied_adjustments,
            }
            if error:
                metadata["error"] = error
            self._performance_monitor.record_metric(
                "passive_sanity_flux_tick",
                duration_ms,
                success=success,
                metadata=metadata,
            )

    def _normalize_environment_config(self, config: dict[str, Any]) -> dict[str, Any]:
        normalized = {
            "default": config.get("default", 0.0),
            "environment_defaults": {},
            "sub_zone_overrides": {},
            "room_overrides": {},
        }

        def _normalize_profile(profile: dict[str, float]) -> dict[str, float]:
            return {
                key: float(value)
                for key, value in profile.items()
                if key in {"day", "night", "all"} and isinstance(value, (int, float))
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

    def _load_sanity_rate_overrides(self) -> dict[str, float]:
        """Load sanity rate overrides from PostgreSQL zone_configurations table."""
        import asyncio
        import threading

        overrides: dict[str, float] = {}
        result_container: dict[str, Any] = {"overrides": {}, "error": None}

        def run_async():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                new_loop.run_until_complete(self._async_load_sanity_rate_overrides(result_container))
            finally:
                new_loop.close()

        thread = threading.Thread(target=run_async)
        thread.start()
        thread.join()

        error = result_container.get("error")
        if error is not None:
            logger.warning("Could not load sanity rate overrides from database", error=str(error))
            return overrides

        overrides = result_container.get("overrides", {})
        if overrides:
            logger.info("Loaded sanity rate overrides from database", count=len(overrides))
        else:
            logger.info("No sanity rate overrides found in database")
        return overrides

    async def _async_load_sanity_rate_overrides(self, result_container: dict[str, Any]) -> None:
        """Async helper to load sanity rate overrides from PostgreSQL."""
        import json
        import os

        import asyncpg

        try:
            # Get database URL from environment
            database_url = os.getenv("DATABASE_URL")
            if not database_url:
                raise ValueError("DATABASE_URL environment variable not set")

            # Convert SQLAlchemy-style URL to asyncpg-compatible format
            if database_url.startswith("postgresql+asyncpg://"):
                database_url = database_url.replace("postgresql+asyncpg://", "postgresql://", 1)

            # Use asyncpg directly to avoid event loop conflicts
            conn = await asyncpg.connect(database_url)
            try:
                # Query zone configurations
                query = """
                    SELECT
                        z.stable_id as zone_stable_id,
                        sz.stable_id as subzone_stable_id,
                        zc.configuration_type,
                        zc.special_rules
                    FROM zone_configurations zc
                    JOIN zones z ON zc.zone_id = z.id
                    LEFT JOIN subzones sz ON zc.subzone_id = sz.id
                    WHERE zc.special_rules IS NOT NULL
                    ORDER BY z.stable_id, sz.stable_id, zc.configuration_type
                """
                rows = await conn.fetch(query)

                for row in rows:
                    zone_stable_id = row["zone_stable_id"]
                    subzone_stable_id = row["subzone_stable_id"]
                    config_type = row["configuration_type"]
                    # asyncpg returns JSONB as dict/list, but ensure proper types
                    special_rules = row["special_rules"] if row["special_rules"] else {}
                    if isinstance(special_rules, str):
                        special_rules = json.loads(special_rules)

                    # Extract sanity drain rate from special_rules
                    rate = self._extract_sanity_rate({"special_rules": special_rules})
                    if rate is None:
                        continue

                    # Parse zone stable_id (format: 'plane/zone')
                    zone_parts = zone_stable_id.split("/")
                    plane = zone_parts[0] if len(zone_parts) > 0 else None
                    zone = zone_parts[1] if len(zone_parts) > 1 else None

                    if config_type == "zone":
                        # Zone-level config
                        key = self._build_override_key(plane, zone, None)
                        result_container["overrides"][key] = self._rate_to_flux(rate)
                    elif config_type == "subzone" and subzone_stable_id:
                        # Subzone-level config
                        key = self._build_override_key(plane, zone, subzone_stable_id)
                        result_container["overrides"][key] = self._rate_to_flux(rate)
            finally:
                await conn.close()
        except Exception as e:
            result_container["error"] = e
            raise

    @staticmethod
    def _extract_sanity_rate(config: dict[str, Any]) -> float | None:
        special_rules = config.get("special_rules")
        if not isinstance(special_rules, dict):
            return None
        value = special_rules.get("sanity_drain_rate")
        if isinstance(value, (int, float)):
            return float(value)
        return None

    @staticmethod
    def _parse_hierarchy_path(path: str) -> tuple[str | None, str | None, str | None]:
        parts = path.split("/")
        plane = parts[0] if len(parts) > 0 else None
        zone = parts[1] if len(parts) > 1 else None
        sub_zone = parts[2] if len(parts) > 2 else None
        return plane, zone, sub_zone

    @staticmethod
    def _build_override_key(plane: str | None, zone: str | None, sub_zone: str | None) -> str:
        plane_part = (plane or "*").lower()
        zone_part = (zone or "*").lower()
        sub_zone_part = (sub_zone or "*").lower()
        return f"{plane_part}|{zone_part}|{sub_zone_part}"

    @staticmethod
    def _rate_to_flux(rate: float) -> float:
        return -float(rate)

    def _lookup_world_override_flux(self, room: Any) -> tuple[float | None, str | None]:
        if not self._sanity_rate_overrides:
            return None, None

        keys = [
            self._build_override_key(
                getattr(room, "plane", None), getattr(room, "zone", None), getattr(room, "sub_zone", None)
            ),
            self._build_override_key(getattr(room, "plane", None), getattr(room, "zone", None), None),
            self._build_override_key(getattr(room, "plane", None), None, None),
        ]
        sources = [
            f"sanity_rule:{getattr(room, 'plane', '')}/{getattr(room, 'zone', '')}/{getattr(room, 'sub_zone', '')}",
            f"sanity_rule:{getattr(room, 'plane', '')}/{getattr(room, 'zone', '')}",
            f"sanity_rule:{getattr(room, 'plane', '')}",
        ]

        for key, source in zip(keys, sources, strict=False):
            flux = self._sanity_rate_overrides.get(key)
            if flux is not None:
                return flux, source
        return None, None


__all__ = ["PassiveSanityFluxService", "PassiveFluxContext"]
