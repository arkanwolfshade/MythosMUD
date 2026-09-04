"""Passive LCD flux scheduler guided by the Pnakotic curricula."""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-locals,too-many-lines  # Reason: Lucidity flux service requires many state attributes, parameters, and intermediate variables for comprehensive lucidity management; tick/path/companion logic stays in one module for cohesion.

from __future__ import annotations

import math
import time
import uuid
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol, cast

from sqlalchemy import Select, select
from sqlalchemy.exc import DatabaseError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from ...async_persistence import AsyncPersistenceLayer
from ...models.lucidity import PlayerLucidity
from ...models.player import Player
from ...services.lucidity_service import CatatoniaObserverProtocol, LucidityService, LucidityUpdateResult
from ...structured_logging.enhanced_logging_config import get_logger
from .config import (
    DEFAULT_ENVIRONMENT_CONFIG,
    FluxServiceConfig,
    lookup_profile,
    normalize_environment_config,
    period_label,
)
from .hallucinations import handle_hallucination_triggers
from .models import CachedRoom, PassiveFluxContext
from .rate_overrides import build_override_key, load_lucidity_rate_overrides

try:
    from server.monitoring.performance_monitor import PerformanceMonitor
except ImportError:  # pragma: no cover - monitoring is optional in some test harnesses
    PerformanceMonitor = None  # type: ignore[assignment, misc]  # Reason: PerformanceMonitor is optional dependency

logger = get_logger(__name__)


class FluxRoom(Protocol):  # pylint: disable=too-few-public-methods  # Reason: Protocol stub
    """Room fields used for lucidity environment lookup."""

    id: str
    sub_zone: str
    zone: str
    environment: str
    plane: str


def _as_str_attr(value: object, default: str = "") -> str:
    return value if isinstance(value, str) else default


def _as_float(value: object, default: float = 0.0) -> float:
    return float(value) if isinstance(value, int | float) else default


def _profile_map(raw: object) -> dict[str, dict[str, float]]:
    if not isinstance(raw, dict):
        return {}
    out: dict[str, dict[str, float]] = {}
    for key, profile in raw.items():
        if isinstance(key, str) and isinstance(profile, dict):
            out[key] = {str(pk): _as_float(pv) for pk, pv in profile.items()}
    return out


@dataclass
class PlayerFluxCtx:  # pylint: disable=too-few-public-methods  # Reason: dataclass bundle for lizard PARAM
    """Bundle for _process_single_player (lizard PARAM)."""

    player: Player | None
    players: list[Player]
    lucidity_records: dict[str, PlayerLucidity]
    room_cache: dict[str, FluxRoom]
    timestamp: datetime
    tick_count: int
    lucidity_service: LucidityService
    session: AsyncSession


class LucidityFluxService:  # pylint: disable=too-many-instance-attributes  # Reason: Lucidity flux service requires many state tracking and configuration attributes
    """Applies passive LCD flux each in-game minute with structured telemetry."""

    def __init__(
        self,
        persistence: AsyncPersistenceLayer | None = None,
        performance_monitor: PerformanceMonitor | None = None,
        *,
        catatonia_observer: CatatoniaObserverProtocol | None = None,
        config: FluxServiceConfig | None = None,
    ) -> None:
        cfg = config or FluxServiceConfig()
        self._persistence = persistence
        self._performance_monitor = performance_monitor
        self._environment_config = cast(
            dict[str, object],  # normalize_environment_config returns dict[str, Any]
            normalize_environment_config(cfg.environment_config or DEFAULT_ENVIRONMENT_CONFIG),
        )
        self._ticks_per_minute = max(1, cfg.ticks_per_minute)
        self._adaptive_window = max(1, cfg.adaptive_window_minutes)
        self._epsilon = 1e-6
        self._context_resolver = cfg.context_resolver
        self._now_provider = cfg.now_provider or (lambda: datetime.now(UTC))
        self._catatonia_observer = catatonia_observer
        self._lucidity_rate_overrides = (
            cfg.lucidity_rate_overrides if cfg.lucidity_rate_overrides is not None else load_lucidity_rate_overrides()
        )

        self._residuals: dict[str, float] = {}
        self._player_room_tracker: dict[str, dict[str, object]] = {}
        self._room_cache: dict[str, CachedRoom] = {}
        self._room_cache_ttl: float = 60.0

        logger.info(
            "PassiveLucidityFluxService initialized",
            ticks_per_minute=self._ticks_per_minute,
            adaptive_window_minutes=self._adaptive_window,
            room_cache_ttl=self._room_cache_ttl,
        )

    async def _build_room_cache(self, players: list[Player]) -> dict[str, FluxRoom]:
        """Build room cache for all players."""
        room_cache: dict[str, FluxRoom] = {}
        if self._persistence is not None:
            unique_room_ids = {player.current_room_id for player in players}
            for room_id in unique_room_ids:
                room = await self._get_room_cached(room_id)
                if room is not None:
                    room_cache[room_id] = room
        return room_cache

    async def _process_single_player(self, ctx: PlayerFluxCtx) -> tuple[str, LucidityUpdateResult | None]:
        """Process a single player's passive flux."""
        player = ctx.player
        if player is None:
            return "", None
        player_id_uuid = uuid.UUID(str(player.player_id))
        player_id_str = str(player_id_uuid)
        room_id = player.current_room_id
        context = await self._resolve_context_async(player, ctx.timestamp, ctx.room_cache.get(room_id))
        base_flux = context.base_flux
        companion_flux = self._companion_modifier(player, ctx.players, ctx.lucidity_records)
        total_flux = self._apply_adaptive_resistance(player_id_str, room_id, base_flux + companion_flux)
        delta = self._apply_residual(player_id_str, total_flux)
        if abs(delta) > 5 or abs(total_flux) > 5:
            logger.warning(
                "Large flux or delta calculated for player",
                player_id=player_id_str,
                room_id=room_id,
                base_flux=base_flux,
                companion_flux=companion_flux,
                total_flux_after_adaptive=total_flux,
                delta=delta,
                source=context.source,
            )
        if not delta:
            return player_id_str, None
        await handle_hallucination_triggers(
            player_id_uuid,
            player_id_str,
            room_id,
            cast(dict[str, object], cast(object, ctx.lucidity_records)),
            ctx.session,
        )
        result = await ctx.lucidity_service.apply_lucidity_adjustment(
            player_id_uuid,
            delta,
            reason_code="passive_flux",
            metadata={
                "context_tags": list(context.tags),
                "source": context.source,
                "base_flux": base_flux,
                "companion_flux": companion_flux,
                "total_flux": total_flux,
                "tick_count": ctx.tick_count,
                **context.metadata,
            },
        )
        return player_id_str, result

    async def _commit_flux_adjustments(self, session: AsyncSession, adjustments: list[LucidityUpdateResult]) -> None:
        if not adjustments:
            return
        await session.commit()
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

    async def _evaluate_players_tick(
        self, session: AsyncSession, players: list[Player], tick_base: PlayerFluxCtx
    ) -> tuple[set[str], list[LucidityUpdateResult]]:
        processed: set[str] = set()
        adjustments: list[LucidityUpdateResult] = []
        for player in players:
            processed.add(str(uuid.UUID(str(player.player_id))))
            _pid, result = await self._process_single_player(
                PlayerFluxCtx(
                    player,
                    tick_base.players,
                    tick_base.lucidity_records,
                    tick_base.room_cache,
                    tick_base.timestamp,
                    tick_base.tick_count,
                    tick_base.lucidity_service,
                    session,
                )
            )
            if result is not None:
                adjustments.append(result)
        return processed, adjustments

    async def process_tick(  # pylint: disable=too-many-locals  # Reason: Tick processing requires many intermediate variables
        self, session: AsyncSession, tick_count: int, *, now: datetime | None = None
    ) -> dict[str, object]:
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
        lucidity_service = LucidityService(session, catatonia_observer=self._catatonia_observer)

        try:
            all_players = await self._load_players(session)
            players = self._filter_active_players(all_players, timestamp)
            lucidity_records = await self._load_lucidity_records(session)
            room_cache = await self._build_room_cache(players)
            processed_player_ids, adjustments = await self._evaluate_players_tick(
                session,
                players,
                PlayerFluxCtx(
                    None, players, lucidity_records, room_cache, timestamp, tick_count, lucidity_service, session
                ),
            )
            await self._commit_flux_adjustments(session, adjustments)
            self._prune_trackers(processed_player_ids)

            duration_ms = (time.perf_counter() - evaluation_start) * 1000
            self._emit_telemetry(duration_ms, len(players), len(adjustments), True)

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

    def get_flux_runtime_status(self) -> dict[str, object]:
        """Snapshot of scheduler state for ops and tests."""
        return {
            "ticks_per_minute": self._ticks_per_minute,
            "adaptive_window_minutes": self._adaptive_window,
            "tracked_players": len(self._player_room_tracker),
            "residual_count": len(self._residuals),
            "room_cache_size": len(self._room_cache),
            "room_cache_ttl": self._room_cache_ttl,
        }

    def _should_process_tick(self, tick_count: int) -> bool:
        return self._ticks_per_minute <= 1 or not tick_count % self._ticks_per_minute

    async def _get_room_cached(self, room_id: str) -> FluxRoom | None:
        """Get room from cache or fetch from database with TTL management."""
        current_time = time.time()

        if room_id in self._room_cache:
            cached_entry = self._room_cache[room_id]
            if current_time - cached_entry.timestamp < self._room_cache_ttl:
                # Cast: CachedRoom.room is untyped; persistence stores Room matching FluxRoom.
                return cast(FluxRoom, cached_entry.room)

        if self._persistence is not None:
            try:
                room = self._persistence.get_room_by_id(room_id)
                if room is not None:
                    typed_room = cast(FluxRoom, room)
                    self._room_cache[room_id] = CachedRoom(room=typed_room, timestamp=current_time)
                    return typed_room
                return room
            except (DatabaseError, SQLAlchemyError) as exc:  # pragma: no cover - defensive logging
                logger.warning(
                    "Failed to fetch room for caching",
                    room_id=room_id,
                    error=str(exc),
                )
                return None
        return None

    async def _load_players(self, session: AsyncSession) -> Sequence[Player]:
        """Load players from database."""
        stmt: Select[tuple[Player]] = select(Player)
        result = await session.execute(stmt)
        return result.scalars().all()

    def _parse_last_active(self, last_active_raw: datetime | str | None) -> datetime | None:  # pylint: disable=too-many-return-statements  # Reason: Last active parsing requires multiple return statements
        """Parse last_active from various formats."""
        if last_active_raw is None:
            return None

        if isinstance(last_active_raw, datetime):
            return last_active_raw

        if isinstance(last_active_raw, str):
            try:
                last_active_str = last_active_raw.strip()
                if last_active_str.endswith("Z"):
                    return datetime.fromisoformat(last_active_str[:-1] + "+00:00")
                if "+" in last_active_str or "-" in last_active_str[-6:]:
                    return datetime.fromisoformat(last_active_str)
                return datetime.fromisoformat(last_active_str).replace(tzinfo=UTC)
            except (ValueError, AttributeError):
                return None

        return None  # type: ignore[unreachable]  # Reason: Defensive programming fallback

    def _normalize_datetime_timezone(self, dt: datetime | None) -> datetime | None:
        """Normalize datetime to timezone-aware UTC."""
        if dt and dt.tzinfo is None:
            return dt.replace(tzinfo=UTC)
        return dt

    def _is_player_active(
        self, player: Player, last_active: datetime | None, active_threshold: datetime, timestamp: datetime
    ) -> bool:
        """Check if player is active based on last_active and created_at."""
        from datetime import timedelta

        if last_active:
            is_recently_active = last_active >= active_threshold
        else:
            is_recently_active = False

        is_recently_created = False
        if hasattr(player, "created_at") and player.created_at is not None:
            created_at_raw = player.created_at
            created_at = self._normalize_datetime_timezone(created_at_raw)
            if created_at:
                is_recently_created = created_at >= timestamp - timedelta(hours=1)

        return is_recently_active or is_recently_created

    def _filter_active_players(self, players: Sequence[Player], timestamp: datetime) -> list[Player]:
        """Filter players to only those active in the last 5 minutes."""
        from datetime import timedelta

        active_threshold = timestamp - timedelta(minutes=5)
        active_players = []

        for player in players:
            last_active_raw: datetime | str | None = cast(datetime | str | None, player.last_active)

            if last_active_raw is None:
                active_players.append(player)
                continue

            last_active = self._parse_last_active(last_active_raw)
            if last_active is None:
                active_players.append(player)
                continue

            last_active = self._normalize_datetime_timezone(last_active)

            if self._is_player_active(player, last_active, active_threshold, timestamp):
                active_players.append(player)

        return active_players

    async def _load_lucidity_records(self, session: AsyncSession) -> dict[str, PlayerLucidity]:
        stmt: Select[tuple[PlayerLucidity]] = select(PlayerLucidity)
        result = await session.execute(stmt)
        records = result.scalars().all()
        return {str(record.player_id): record for record in records}

    def _lookup_base_flux_for_room(self, room: FluxRoom, period: str) -> tuple[float, str]:
        """Look up base_flux and profile_source from room overrides. Returns (base_flux, profile_source)."""
        default = _as_float(self._environment_config["default"])
        room_overrides = _profile_map(self._environment_config["room_overrides"])
        subzone_overrides = _profile_map(self._environment_config["sub_zone_overrides"])
        environment_defaults = _profile_map(self._environment_config["environment_defaults"])

        room_id = _as_str_attr(room.id)
        sub_zone = _as_str_attr(room.sub_zone)
        zone = _as_str_attr(room.zone)
        environment = _as_str_attr(room.environment)

        if room_id in room_overrides:
            return lookup_profile(room_overrides[room_id], period, default), f"room:{room_id}"
        if sub_zone in subzone_overrides:
            return lookup_profile(subzone_overrides[sub_zone], period, default), f"sub_zone:{sub_zone}"
        if zone in subzone_overrides:
            return lookup_profile(subzone_overrides[zone], period, default), f"zone:{zone}"
        if environment in environment_defaults:
            return lookup_profile(environment_defaults[environment], period, default), f"environment:{environment}"
        return default, "default"

    async def _resolve_context_async(
        self, player: Player, timestamp: datetime, room: FluxRoom | None = None
    ) -> PassiveFluxContext:
        """Resolve environmental context for passive flux evaluation using cached room."""
        if self._context_resolver is not None:
            return self._context_resolver(player, timestamp)

        period = period_label(timestamp)
        base_flux = _as_float(self._environment_config["default"])
        profile_source = "default"
        tags: set[str] = set()
        metadata: dict[str, object] = {"room_id": str(player.current_room_id)}

        if room is not None:
            tags.add(_as_str_attr(room.environment))
            metadata["zone"] = _as_str_attr(room.zone)
            metadata["sub_zone"] = _as_str_attr(room.sub_zone)
            base_flux, profile_source = self._lookup_base_flux_for_room(room, period)

            override_flux, override_source = self._lookup_world_override_flux(room)
            if override_flux is not None:
                base_flux = override_flux
                profile_source = override_source or profile_source
                metadata["lucidity_rate_override"] = True
        else:
            metadata["zone"] = None
            metadata["sub_zone"] = None

        return PassiveFluxContext(base_flux=base_flux, tags=frozenset(tags), source=profile_source, metadata=metadata)

    def _get_room_for_context(self, player: Player) -> FluxRoom | None:
        """Fetch room for context resolution. Returns None if persistence unavailable or fetch fails."""
        if self._persistence is None:
            return None
        try:
            return cast(FluxRoom, self._persistence.get_room_by_id(str(player.current_room_id)))
        except (DatabaseError, SQLAlchemyError) as exc:  # pragma: no cover - defensive logging
            logger.warning(
                "Failed to resolve room for passive flux",
                player_id=player.player_id,
                room_id=str(player.current_room_id),
                error=str(exc),
            )
            return None

    def _resolve_context(self, player: Player, timestamp: datetime) -> PassiveFluxContext:
        """Resolve context synchronously (legacy path)."""
        if self._context_resolver is not None:
            return self._context_resolver(player, timestamp)

        room = self._get_room_for_context(player)
        period = period_label(timestamp)
        profile_source = "default"
        base_flux = _as_float(self._environment_config["default"])
        tags: set[str] = set()
        metadata: dict[str, object] = {"room_id": str(player.current_room_id)}

        if room is not None:
            tags.add(room.environment)
            metadata["zone"] = room.zone
            metadata["sub_zone"] = room.sub_zone
            base_flux, profile_source = self._lookup_base_flux_for_room(room, period)

            override_flux, override_source = self._lookup_world_override_flux(room)
            if override_flux is not None:
                base_flux = override_flux
                profile_source = override_source or profile_source
                metadata["lucidity_rate_override"] = True
        else:
            metadata["zone"] = None
            metadata["sub_zone"] = None

        return PassiveFluxContext(base_flux=base_flux, tags=frozenset(tags), source=profile_source, metadata=metadata)

    def _count_companion_tiers(
        self, companions: Sequence[Player], lucidity_records: dict[str, PlayerLucidity]
    ) -> tuple[int, bool]:
        """Count lucid companions and whether any destabilizing companion is present. Returns (lucid_count, has_destabilizing)."""
        lucid_companions = 0
        has_destabilizing = False
        for companion in companions:
            record = lucidity_records.get(companion.player_id)
            tier = record.current_tier if record else "lucid"
            if tier in {"lucid", "uneasy"}:
                lucid_companions += 1
            if tier in {"deranged", "catatonic"}:
                has_destabilizing = True
        return lucid_companions, has_destabilizing

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

        lucid_companions, has_destabilizing = self._count_companion_tiers(companions, lucidity_records)
        companion_flux = min(lucid_companions * 0.1, 0.3)
        if has_destabilizing:
            companion_flux += -0.2
        return companion_flux

    def _apply_adaptive_resistance(self, player_id: str, room_id: str, flux: float) -> float:
        tracker = self._player_room_tracker.get(player_id)
        if tracker is None or tracker["room_id"] != room_id:
            self._player_room_tracker[player_id] = {"room_id": room_id, "minutes": 1}
            return flux

        minutes_raw = tracker.get("minutes")
        minutes = minutes_raw if isinstance(minutes_raw, int) else 0
        tracker["minutes"] = minutes + 1

        if flux >= 0:
            return flux

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

    def _emit_telemetry(  # pylint: disable=too-many-arguments  # Reason: Telemetry emission requires many parameters
        self,
        duration_ms: float,
        evaluated_players: int,
        applied_adjustments: int,
        success: bool,
        error: str | None = None,
    ) -> None:
        if self._performance_monitor is not None:
            metadata: dict[str, object] = {
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

    def _lookup_world_override_flux(self, room: FluxRoom) -> tuple[float | None, str | None]:
        if not self._lucidity_rate_overrides:
            return None, None

        plane = _as_str_attr(room.plane)
        zone = _as_str_attr(room.zone)
        sub_zone = _as_str_attr(room.sub_zone)
        keys = [
            build_override_key(plane, zone, sub_zone),
            build_override_key(plane, zone, None),
            build_override_key(plane, None, None),
        ]
        sources = [
            f"lucidity_rule:{plane}/{zone}/{sub_zone}",
            f"lucidity_rule:{plane}/{zone}",
            f"lucidity_rule:{plane}",
        ]

        for key, source in zip(keys, sources, strict=False):
            flux = self._lucidity_rate_overrides.get(key)
            if flux is not None:
                return flux, source
        return None, None


# Public name expected by package __init__ and callers
PassiveLucidityFluxService = LucidityFluxService
