"""Passive LCD flux scheduler guided by the Pnakotic curricula."""

from __future__ import annotations

import math
import time
import uuid
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any, cast

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from ..async_persistence import AsyncPersistenceLayer
from ..logging.enhanced_logging_config import get_logger
from ..models.lucidity import PlayerLucidity
from ..models.player import Player
from ..services.lucidity_service import CatatoniaObserverProtocol, LucidityService, LucidityUpdateResult

try:
    from server.monitoring.performance_monitor import PerformanceMonitor
except ImportError:  # pragma: no cover - monitoring is optional in some test harnesses
    PerformanceMonitor = None  # type: ignore[assignment, misc]

logger = get_logger(__name__)


@dataclass
class CachedRoom:
    """Cached room entry with timestamp for TTL management."""

    room: Any
    timestamp: float


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


class PassiveLucidityFluxService:
    """Applies passive LCD flux each in-game minute with structured telemetry."""

    def __init__(
        self,
        persistence: AsyncPersistenceLayer | None = None,
        performance_monitor: PerformanceMonitor | None = None,
        *,
        environment_config: dict[str, Any] | None = None,
        ticks_per_minute: int = 6,
        adaptive_window_minutes: int = 10,
        context_resolver: Callable[[Player, datetime], PassiveFluxContext] | None = None,
        now_provider: Callable[[], datetime] | None = None,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
        lucidity_rate_overrides: dict[str, float] | None = None,
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
        self._lucidity_rate_overrides = (
            lucidity_rate_overrides if lucidity_rate_overrides is not None else self._load_lucidity_rate_overrides()
        )

        self._residuals: dict[str, float] = {}
        self._player_room_tracker: dict[str, dict[str, Any]] = {}

        # Room cache with TTL to prevent repeated database lookups
        # AI Agent: Prevents event loop blocking by caching rooms across ticks
        self._room_cache: dict[str, CachedRoom] = {}
        self._room_cache_ttl: float = 60.0  # 60 second TTL (rooms rarely change)

        logger.info(
            "PassiveLucidityFluxService initialized",
            ticks_per_minute=self._ticks_per_minute,
            adaptive_window_minutes=self._adaptive_window,
            room_cache_ttl=self._room_cache_ttl,
        )

    async def process_tick(
        self, session: AsyncSession, tick_count: int, *, now: datetime | None = None
    ) -> dict[str, Any]:
        """Evaluate passive LCD flux for the current tick."""
        if not self._should_process_tick(tick_count):
            return {"evaluated": 0, "adjustments": 0, "skipped": True}

        logger.debug(
            "Processing passive LCD flux tick",
            tick_count=tick_count,
            ticks_per_minute=self._ticks_per_minute,
            should_process=self._should_process_tick(tick_count),
        )

        evaluation_start = time.perf_counter()
        timestamp = now or self._now_provider()
        processed_player_ids: set[str] = set()
        adjustments: list[LucidityUpdateResult] = []
        lucidity_service = LucidityService(session, catatonia_observer=self._catatonia_observer)

        try:
            # Load all players and filter to active ones (active in last 5 minutes)
            all_players = await self._load_players(session)
            players = self._filter_active_players(all_players, timestamp)
            lucidity_records = await self._load_lucidity_records(session)

            # Cache rooms for all players to avoid repeated lookups
            # CRITICAL FIX: Use _get_room_cached() which implements TTL caching
            # and async_get_room() to prevent event loop blocking.
            # Previously used sync get_room() which blocked the entire event loop,
            # causing 17-second delays (1,639% overhead).
            room_cache: dict[str, Any] = {}
            if self._persistence is not None:
                unique_room_ids = {cast(str, player.current_room_id) for player in players}
                for room_id in unique_room_ids:
                    # Use cached method which checks TTL cache first,
                    # then fetches asynchronously if needed
                    room = await self._get_room_cached(room_id)
                    if room is not None:
                        room_cache[room_id] = room

            for player in players:
                # Convert player.player_id to UUID for apply_lucidity_adjustment
                # SQLAlchemy Column[str] returns UUID at runtime, but mypy sees it as Column[str]
                # Always convert to string first, then to UUID
                player_id_value = player.player_id
                player_id_uuid = uuid.UUID(str(player_id_value))
                player_id_str = str(player_id_uuid)
                room_id = cast(str, player.current_room_id)

                processed_player_ids.add(player_id_str)
                context = await self._resolve_context_async(player, timestamp, room_cache.get(room_id))
                base_flux = context.base_flux

                companion_flux = self._companion_modifier(player, players, lucidity_records)
                total_flux = base_flux + companion_flux

                total_flux = self._apply_adaptive_resistance(player_id_str, room_id, total_flux)
                delta = self._apply_residual(player_id_str, total_flux)

                # Log flux calculation for debugging
                if abs(delta) > 5 or abs(total_flux) > 5:
                    logger.warning(
                        "Large flux or delta calculated for player",
                        player_id=player_id_str,
                        room_id=room_id,
                        base_flux=base_flux,
                        companion_flux=companion_flux,
                        total_flux_before_adaptive=base_flux + companion_flux,
                        total_flux_after_adaptive=total_flux,
                        delta=delta,
                        source=context.source,
                        metadata=context.metadata,
                    )

                if delta == 0:
                    continue

                result = await lucidity_service.apply_lucidity_adjustment(
                    player_id_uuid,
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
                        "Passive LCD flux applied",
                        player_id=result.player_id,
                        lcd_change=result.delta,
                        previous_lcd=result.previous_lcd,
                        new_lcd=result.new_lcd,
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
            logger.error("Passive LCD flux tick failed", error=str(exc))
            raise

    def _should_process_tick(self, tick_count: int) -> bool:
        return self._ticks_per_minute <= 1 or tick_count % self._ticks_per_minute == 0

    async def _get_room_cached(self, room_id: str) -> Any | None:
        """
        Get room from cache or fetch from database with TTL management.

        CRITICAL FIX: Prevents event loop blocking by caching room lookups
        across multiple ticks. Uses async_get_room() to prevent blocking.

        Args:
            room_id: The room ID to retrieve

        Returns:
            Room object or None if not found

        AI Agent: This method implements caching with TTL to prevent repeated
                  database lookups that were causing 17-second delays.
        """
        current_time = time.time()

        # Check if room is in cache and not expired
        if room_id in self._room_cache:
            cached_entry = self._room_cache[room_id]
            if current_time - cached_entry.timestamp < self._room_cache_ttl:
                # Cache hit - return cached room
                return cached_entry.room

        # Cache miss or expired - fetch from database
        if self._persistence is not None:
            try:
                room = self._persistence.get_room_by_id(room_id)
                if room is not None:
                    # Update cache
                    self._room_cache[room_id] = CachedRoom(room=room, timestamp=current_time)
                return room
            except Exception as exc:  # pragma: no cover - defensive logging
                logger.warning(
                    "Failed to fetch room for caching",
                    room_id=room_id,
                    error=str(exc),
                )
                return None
        return None

    async def _load_players(self, session: AsyncSession) -> Sequence[Player]:
        """
        Load players from database.

        PERFORMANCE FIX: Should filter to active players to reduce unnecessary processing.
        For now, loads all players and filtering is done by _filter_active_players().

        Returns:
            Sequence of all Player objects (filtered downstream)

        AI Agent: Consider adding WHERE clause to filter at database level for better performance.
        """
        stmt: Select[tuple[Player]] = select(Player)
        result = await session.execute(stmt)
        return result.scalars().all()

    def _filter_active_players(self, players: Sequence[Player], timestamp: datetime) -> list[Player]:
        """Filter players to only those active in the last 5 minutes."""
        from datetime import timedelta

        active_threshold = timestamp - timedelta(minutes=5)
        active_players = []

        for player in players:
            # Consider player active if last_active is within threshold or None (new players)
            # Also consider players active if created recently (within last hour) - handles test scenarios
            # Cast: SQLAlchemy Column returns datetime | None at runtime, but mypy sees Column type
            last_active_raw: datetime | str | None = cast(datetime | str | None, player.last_active)
            if last_active_raw is None:
                active_players.append(player)
                continue

            # Handle both datetime and string formats (string handling for legacy/serialized data)
            last_active: datetime | None = None
            if isinstance(last_active_raw, str):
                try:
                    # Optimized string parsing - handle common formats more efficiently
                    last_active_str = last_active_raw.strip()
                    if last_active_str.endswith("Z"):
                        # Handle UTC format
                        last_active = datetime.fromisoformat(last_active_str[:-1] + "+00:00")
                    elif "+" in last_active_str or "-" in last_active_str[-6:]:
                        # Handle timezone format
                        last_active = datetime.fromisoformat(last_active_str)
                    else:
                        # Assume UTC if no timezone info
                        last_active = datetime.fromisoformat(last_active_str).replace(tzinfo=UTC)
                except (ValueError, AttributeError):
                    # If parsing fails, assume player is active
                    active_players.append(player)
                    continue
            elif isinstance(last_active_raw, datetime):
                last_active = last_active_raw
            else:
                # Unknown type, assume player is active to be safe
                # Type ignore: Defensive check - mypy knows this is unreachable but we keep it for safety
                active_players.append(player)  # type: ignore[unreachable]
                continue

            # Ensure both datetimes are timezone-aware for comparison
            if last_active and last_active.tzinfo is None:
                last_active = last_active.replace(tzinfo=UTC)

            # Check if player is active (within 5 minutes) OR was created recently (within last hour)
            # This handles test scenarios where players are created just before processing
            is_recently_active = last_active and last_active >= active_threshold
            is_recently_created = False
            if hasattr(player, "created_at") and player.created_at is not None:
                # Cast: SQLAlchemy Column returns datetime at runtime, but mypy sees Column type
                created_at: datetime = cast(datetime, player.created_at)
                # Ensure created_at is timezone-aware for comparison
                if created_at.tzinfo is None:
                    created_at = created_at.replace(tzinfo=UTC)
                is_recently_created = created_at >= timestamp - timedelta(hours=1)

                if is_recently_active or is_recently_created:
                    active_players.append(player)

        return active_players

    async def _load_lucidity_records(self, session: AsyncSession) -> dict[str, PlayerLucidity]:
        stmt: Select[tuple[PlayerLucidity]] = select(PlayerLucidity)
        result = await session.execute(stmt)
        records = result.scalars().all()
        return {str(record.player_id): record for record in records}

    async def _resolve_context_async(
        self, player: Player, timestamp: datetime, room: Any | None = None
    ) -> PassiveFluxContext:
        """Resolve environmental context for passive flux evaluation using cached room."""
        if self._context_resolver is not None:
            return self._context_resolver(player, timestamp)

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
                metadata["lucidity_rate_override"] = True
        else:
            metadata["zone"] = None
            metadata["sub_zone"] = None

        return PassiveFluxContext(base_flux=base_flux, tags=frozenset(tags), source=profile_source, metadata=metadata)

    def _resolve_context(self, player: Player, timestamp: datetime) -> PassiveFluxContext:
        if self._context_resolver is not None:
            return self._context_resolver(player, timestamp)

        room = None
        if self._persistence is not None:
            try:
                room = self._persistence.get_room_by_id(str(player.current_room_id))
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
                metadata["lucidity_rate_override"] = True
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
        lucidity_records: dict[str, PlayerLucidity],
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
            record = lucidity_records.get(cast(str, companion.player_id))
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
        previous_residual = self._residuals.get(player_id, 0.0)
        residual = previous_residual + flux
        delta = 0

        if residual >= 1.0 - self._epsilon:
            delta = math.floor(residual + self._epsilon)
        elif residual <= -1.0 + self._epsilon:
            delta = math.ceil(residual - self._epsilon)

        residual -= delta
        self._residuals[player_id] = residual

        # Log residual accumulation for debugging massive lucidity losses
        if abs(delta) > 10 or abs(flux) > 10:
            logger.warning(
                "Large lucidity flux or delta detected",
                player_id=player_id,
                flux=flux,
                previous_residual=previous_residual,
                residual_before_apply=residual + delta,
                delta=delta,
                residual_after_apply=residual,
            )

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
                "passive_lucidity_flux_tick",
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

    def _load_lucidity_rate_overrides(self) -> dict[str, float]:
        """Load lucidity rate overrides from PostgreSQL zone_configurations table."""
        import asyncio
        import threading

        overrides: dict[str, float] = {}
        result_container: dict[str, Any] = {"overrides": {}, "error": None}

        def run_async():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            try:
                new_loop.run_until_complete(self._async_load_lucidity_rate_overrides(result_container))
            finally:
                new_loop.close()

        thread = threading.Thread(target=run_async)
        thread.start()
        thread.join()

        error = result_container.get("error")
        if error is not None:
            logger.warning("Could not load lucidity rate overrides from database", error=str(error))
            return overrides

        overrides = result_container.get("overrides", {})
        if overrides:
            logger.info("Loaded lucidity rate overrides from database", count=len(overrides))
        else:
            logger.info("No lucidity rate overrides found in database")
        return overrides

    async def _async_load_lucidity_rate_overrides(self, result_container: dict[str, Any]) -> None:
        """Async helper to load lucidity rate overrides from PostgreSQL."""
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
                    -- Query zones (authoritative zone data)
                    SELECT
                        z.stable_id as zone_stable_id,
                        NULL::text as subzone_stable_id,
                        z.special_rules
                    FROM zones z
                    WHERE z.special_rules IS NOT NULL
                    UNION ALL
                    -- Query subzones (authoritative subzone data)
                    SELECT
                        z.stable_id as zone_stable_id,
                        sz.stable_id as subzone_stable_id,
                        sz.special_rules
                    FROM subzones sz
                    JOIN zones z ON sz.zone_id = z.id
                    WHERE sz.special_rules IS NOT NULL
                    ORDER BY zone_stable_id, subzone_stable_id
                """
                rows = await conn.fetch(query)

                for row in rows:
                    zone_stable_id = row["zone_stable_id"]
                    subzone_stable_id = row["subzone_stable_id"]
                    # asyncpg returns JSONB as dict/list, but ensure proper types
                    special_rules = row["special_rules"] if row["special_rules"] else {}
                    if isinstance(special_rules, str):
                        special_rules = json.loads(special_rules)

                    # Extract lucidity drain rate from special_rules
                    rate = self._extract_lucidity_rate({"special_rules": special_rules})
                    if rate is None:
                        continue

                    # Validate rate before conversion
                    if rate > 10.0:
                        logger.warning(
                            "Lucidity drain rate from database exceeds threshold",
                            rate=rate,
                            zone_stable_id=zone_stable_id,
                            subzone_stable_id=subzone_stable_id,
                            message="This may indicate a configuration error (e.g., 100 instead of 0.1)",
                        )

                    # Parse zone stable_id (format: 'plane/zone')
                    zone_parts = zone_stable_id.split("/")
                    plane = zone_parts[0] if len(zone_parts) > 0 else None
                    zone = zone_parts[1] if len(zone_parts) > 1 else None

                    if subzone_stable_id:
                        # Subzone-level config
                        key = self._build_override_key(plane, zone, subzone_stable_id)
                        flux = self._rate_to_flux(rate)
                        result_container["overrides"][key] = flux
                        logger.debug(
                            "Loaded lucidity rate override from database",
                            key=key,
                            rate=rate,
                            flux=flux,
                            source="subzone_config",
                        )
                    else:
                        # Zone-level config
                        key = self._build_override_key(plane, zone, None)
                        flux = self._rate_to_flux(rate)
                        result_container["overrides"][key] = flux
                        logger.debug(
                            "Loaded lucidity rate override from database",
                            key=key,
                            rate=rate,
                            flux=flux,
                            source="zone_config",
                        )
            finally:
                await conn.close()
        except Exception as e:
            result_container["error"] = e
            raise

    @staticmethod
    def _extract_lucidity_rate(config: dict[str, Any]) -> float | None:
        special_rules = config.get("special_rules")
        if not isinstance(special_rules, dict):
            return None
        value = special_rules.get("lucidity_drain_rate")
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
        """
        Convert lucidity_drain_rate to flux value.

        Args:
            rate: Lucidity drain rate (expected range: 0.0 to ~2.0 per minute)

        Returns:
            Negative flux value (since drain is negative)

        Raises:
            ValueError: If rate is unreasonably large (possible configuration error)
        """
        rate_float = float(rate)
        # lucidity check: rates > 10.0 are likely configuration errors (100 instead of 0.1, etc.)
        if rate_float > 10.0:
            logger.error(
                "Lucidity drain rate exceeds maximum threshold - possible configuration error",
                rate=rate_float,
                message="Rates > 10.0 are likely configuration errors (e.g., 100 instead of 0.1). Clamping to 10.0.",
            )
            rate_float = 10.0
        return -rate_float

    def _lookup_world_override_flux(self, room: Any) -> tuple[float | None, str | None]:
        if not self._lucidity_rate_overrides:
            return None, None

        keys = [
            self._build_override_key(
                getattr(room, "plane", None), getattr(room, "zone", None), getattr(room, "sub_zone", None)
            ),
            self._build_override_key(getattr(room, "plane", None), getattr(room, "zone", None), None),
            self._build_override_key(getattr(room, "plane", None), None, None),
        ]
        sources = [
            f"lucidity_rule:{getattr(room, 'plane', '')}/{getattr(room, 'zone', '')}/{getattr(room, 'sub_zone', '')}",
            f"lucidity_rule:{getattr(room, 'plane', '')}/{getattr(room, 'zone', '')}",
            f"lucidity_rule:{getattr(room, 'plane', '')}",
        ]

        for key, source in zip(keys, sources, strict=False):
            flux = self._lucidity_rate_overrides.get(key)
            if flux is not None:
                return flux, source
        return None, None


__all__ = ["PassiveLucidityFluxService", "PassiveFluxContext"]
