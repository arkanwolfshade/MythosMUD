"""Unit tests for PassiveLucidityFluxService."""

import uuid
from datetime import UTC, datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.lucidity_service import LucidityUpdateResult
from server.services.passive_lucidity_flux.config import FluxServiceConfig
from server.services.passive_lucidity_flux.models import PassiveFluxContext
from server.services.passive_lucidity_flux.service import PassiveLucidityFluxService


def _make_service(**kwargs: object) -> PassiveLucidityFluxService:
    config = FluxServiceConfig(
        ticks_per_minute=2,
        adaptive_window_minutes=5,
        lucidity_rate_overrides={"earth|arkham|downtown": -0.5},
        **kwargs,
    )
    return PassiveLucidityFluxService(config=config)


def test_should_process_tick() -> None:
    svc = _make_service()
    assert svc._should_process_tick(0) is True
    assert svc._should_process_tick(1) is False
    assert svc._should_process_tick(2) is True


def test_parse_last_active_variants() -> None:
    svc = _make_service()
    assert svc._parse_last_active(None) is None
    now = datetime.now(UTC)
    assert svc._parse_last_active(now) == now
    assert svc._parse_last_active("2020-01-01T12:00:00Z") is not None
    assert svc._parse_last_active("not-a-date") is None


def test_normalize_datetime_timezone() -> None:
    svc = _make_service()
    naive = datetime(2020, 1, 1, 12, 0, 0)
    normalized = svc._normalize_datetime_timezone(naive)
    assert normalized is not None
    assert normalized.tzinfo is UTC


def test_filter_active_players_includes_recent_and_null_last_active() -> None:
    svc = _make_service()
    now = datetime.now(UTC)
    recent = MagicMock()
    recent.player_id = str(uuid.uuid4())
    recent.last_active = now.isoformat()
    recent.created_at = None
    no_last = MagicMock()
    no_last.player_id = str(uuid.uuid4())
    no_last.last_active = None
    no_last.created_at = None
    stale = MagicMock()
    stale.player_id = str(uuid.uuid4())
    stale.last_active = (now - timedelta(hours=2)).isoformat()
    stale.created_at = None
    active = svc._filter_active_players([recent, no_last, stale], now)
    assert recent in active
    assert no_last in active
    assert stale not in active


def test_apply_residual_accumulates_and_emits_delta() -> None:
    svc = _make_service()
    player_id = str(uuid.uuid4())
    assert svc._apply_residual(player_id, 0.4) == 0
    assert svc._apply_residual(player_id, 0.4) == 0
    assert svc._apply_residual(player_id, 0.4) == 1


def test_apply_adaptive_resistance_reduces_negative_flux() -> None:
    svc = _make_service()
    player_id = str(uuid.uuid4())
    room_a = "room-a"
    first = svc._apply_adaptive_resistance(player_id, room_a, -1.0)
    assert first == -1.0
    for _ in range(5):
        svc._apply_adaptive_resistance(player_id, room_a, -1.0)
    reduced = svc._apply_adaptive_resistance(player_id, room_a, -1.0)
    assert reduced > -1.0


def test_companion_modifier_with_lucid_and_destabilizing() -> None:
    svc = _make_service()
    player = MagicMock(player_id="p1", current_room_id="room-a")
    companion_lucid = MagicMock(player_id="p2", current_room_id="room-a")
    companion_deranged = MagicMock(player_id="p3", current_room_id="room-a")
    records = {
        "p2": MagicMock(current_tier="lucid"),
        "p3": MagicMock(current_tier="deranged"),
    }
    flux = svc._companion_modifier(player, [player, companion_lucid, companion_deranged], records)
    assert flux == pytest.approx(-0.1)


def test_lookup_base_flux_for_room_overrides() -> None:
    svc = _make_service()
    svc._environment_config = {
        "default": 0.0,
        "room_overrides": {"room-1": {"day": 1.0}},
        "sub_zone_overrides": {"sanitarium": {"day": -0.5}},
        "environment_defaults": {"haunted": {"day": -0.4}},
    }
    room = MagicMock(id="room-1", sub_zone="other", zone="z", environment="haunted")
    flux, source = svc._lookup_base_flux_for_room(room, "day")
    assert flux == 1.0
    assert source == "room:room-1"


def test_resolve_context_with_custom_resolver() -> None:
    def resolver(_player: object, _ts: datetime) -> PassiveFluxContext:
        return PassiveFluxContext(base_flux=0.5, source="test")

    svc = PassiveLucidityFluxService(config=FluxServiceConfig(context_resolver=resolver))
    player = MagicMock(current_room_id="room-a")
    ctx = svc._resolve_context(player, datetime.now(UTC))
    assert ctx.base_flux == 0.5
    assert ctx.source == "test"


def test_prune_trackers() -> None:
    svc = _make_service()
    svc._residuals = {"keep": 0.1, "drop": 0.2}
    svc._player_room_tracker = {"keep": {"room_id": "a", "minutes": 1}, "drop": {"room_id": "b", "minutes": 1}}
    svc._prune_trackers(["keep"])
    assert "keep" in svc._residuals
    assert "drop" not in svc._residuals


def test_emit_telemetry_records_metric() -> None:
    monitor = MagicMock()
    svc = PassiveLucidityFluxService(performance_monitor=monitor)
    svc._emit_telemetry(12.5, 3, 1, True)
    monitor.record_metric.assert_called_once()


@pytest.mark.asyncio
async def test_process_tick_skipped_when_not_due() -> None:
    svc = _make_service()
    result = await svc.process_tick(AsyncMock(), tick_count=1)
    assert result["skipped"] is True
    assert result["evaluated"] == 0


@pytest.mark.asyncio
async def test_process_tick_applies_adjustment() -> None:
    player_id = uuid.uuid4()
    player = MagicMock()
    player.player_id = str(player_id)
    player.current_room_id = "room-a"
    player.last_active = None
    player.created_at = None

    session = AsyncMock()
    players_result = MagicMock()
    players_result.scalars.return_value.all.return_value = [player]
    lucidity_result = MagicMock()
    lucidity_result.scalars.return_value.all.return_value = []
    session.execute = AsyncMock(side_effect=[players_result, lucidity_result])
    session.commit = AsyncMock()

    adjustment = LucidityUpdateResult(
        player_id=player_id,
        previous_lcd=50,
        new_lcd=49,
        previous_tier="lucid",
        new_tier="lucid",
        delta=-1,
        liabilities_added=[],
    )

    svc = _make_service(
        context_resolver=lambda _p, _t: PassiveFluxContext(base_flux=-1.2, source="test"),
    )

    with patch.object(svc, "_process_single_player", AsyncMock(return_value=(str(player_id), adjustment))):
        result = await svc.process_tick(session, tick_count=2)

    assert result["skipped"] is False
    assert result["adjustments"] == 1
    session.commit.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_room_cached_uses_persistence() -> None:
    persistence = MagicMock()
    room = MagicMock(id="room-a")
    persistence.get_room_by_id.return_value = room
    svc = PassiveLucidityFluxService(persistence=persistence)
    fetched = await svc._get_room_cached("room-a")
    assert fetched is room
    cached = await svc._get_room_cached("room-a")
    assert cached is room
    persistence.get_room_by_id.assert_called_once()


def test_lookup_base_flux_sub_zone_override() -> None:
    svc = _make_service()
    svc._environment_config = {
        "default": 0.0,
        "room_overrides": {},
        "sub_zone_overrides": {"sanitarium": {"day": -0.5}},
        "environment_defaults": {},
    }
    room = MagicMock(id="room-2", sub_zone="sanitarium", zone="z", environment="urban")
    flux, source = svc._lookup_base_flux_for_room(room, "day")
    assert flux == -0.5
    assert source == "sub_zone:sanitarium"


def test_lookup_world_override_flux() -> None:
    svc = _make_service()
    room = MagicMock(plane="earth", zone="arkham", sub_zone="downtown")
    flux, source = svc._lookup_world_override_flux(room)
    assert flux == -0.5
    assert source is not None


def test_count_companion_tiers() -> None:
    svc = _make_service()
    companion = MagicMock(player_id="p2")
    records = {"p2": MagicMock(current_tier="deranged")}
    lucid_count, has_destabilizing = svc._count_companion_tiers([companion], records)
    assert lucid_count == 0
    assert has_destabilizing is True


def test_is_player_active_recent() -> None:
    svc = _make_service()
    now = datetime.now(UTC)
    player = MagicMock(player_id="p1", last_active=(now - timedelta(minutes=2)).isoformat(), created_at=None)
    last_active = svc._parse_last_active(player.last_active)
    assert svc._is_player_active(player, last_active, now - timedelta(minutes=5), now) is True


def test_apply_adaptive_resistance_positive_flux_unchanged() -> None:
    svc = _make_service()
    player_id = str(uuid.uuid4())
    assert svc._apply_adaptive_resistance(player_id, "room-a", 0.5) == 0.5


def test_apply_residual_negative_delta() -> None:
    svc = _make_service()
    player_id = str(uuid.uuid4())
    assert svc._apply_residual(player_id, -0.4) == 0
    assert svc._apply_residual(player_id, -0.4) == 0
    assert svc._apply_residual(player_id, -0.4) == -1


def test_emit_telemetry_with_error() -> None:
    monitor = MagicMock()
    svc = PassiveLucidityFluxService(performance_monitor=monitor)
    svc._emit_telemetry(5.0, 0, 0, False, error="boom")
    monitor.record_metric.assert_called_once()


@pytest.mark.asyncio
async def test_resolve_context_async_with_room() -> None:
    svc = _make_service()
    svc._environment_config = {
        "default": 0.0,
        "room_overrides": {},
        "sub_zone_overrides": {},
        "environment_defaults": {"haunted": {"day": -0.3}},
    }
    player = MagicMock(current_room_id="room-a")
    room = MagicMock(id="room-a", environment="haunted", zone="z", sub_zone="s")
    # Fixed noon UTC so period_label is "day" (datetime.now can be night).
    day = datetime(2020, 6, 15, 12, 0, 0, tzinfo=UTC)
    ctx = await svc._resolve_context_async(player, day, room)
    assert ctx.base_flux == -0.3
    assert "haunted" in ctx.tags


@pytest.mark.asyncio
async def test_build_room_cache() -> None:
    persistence = MagicMock()
    room = MagicMock(id="room-a")
    persistence.get_room_by_id.return_value = room
    svc = PassiveLucidityFluxService(persistence=persistence)
    player = MagicMock(current_room_id="room-a")
    cache = await svc._build_room_cache([player])
    assert cache["room-a"] is room


@pytest.mark.asyncio
async def test_process_single_player_no_delta() -> None:
    svc = _make_service(context_resolver=lambda _p, _t: PassiveFluxContext(base_flux=0.0, source="test"))
    player = MagicMock(player_id=str(uuid.uuid4()), current_room_id="room-a")
    player_id_str, result = await svc._process_single_player(
        player, [player], {}, {}, datetime.now(UTC), 2, AsyncMock(), AsyncMock()
    )
    assert result is None
    assert player_id_str
