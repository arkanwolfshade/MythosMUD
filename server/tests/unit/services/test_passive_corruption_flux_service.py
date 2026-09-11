"""Unit tests for PassiveCorruptionFluxService (#815 PR-5)."""

# pyright: reportAny=false
# TEST_MOCK: MagicMock/AsyncMock attribute and call chains resolve to Any throughout this file,
# mirroring test_corruption_service.py's identical, already-baselined pattern for mock-typing
# noise -- this file is new, so it has no baseline entry of its own for the same, otherwise
# unavoidable mock-typing noise.
# pyright: reportPrivateUsage=false
# TEST_MOCK: deliberately exercises PassiveCorruptionFluxService's private helpers directly --
# same house style as test_aggro_threat.py and every other private-method-testing suite here.

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.corruption import CorruptionTier
from server.services.corruption_service import CorruptionUpdateResult
from server.services.passive_corruption_flux.config import CorruptionFluxServiceConfig, CorruptionOverride
from server.services.passive_corruption_flux.service import FluxRoom, PassiveCorruptionFluxService


def test_package_reexports_public_surface() -> None:
    """The package __init__ re-exports CachedRoom/PassiveCorruptionFluxContext/Service."""
    from server.services.passive_corruption_flux import (
        CachedRoom,
        PassiveCorruptionFluxContext,
    )
    from server.services.passive_corruption_flux import (
        PassiveCorruptionFluxService as ReexportedService,
    )

    assert ReexportedService is PassiveCorruptionFluxService
    assert PassiveCorruptionFluxContext(target=0.0, rate=0.0).target == 0.0
    assert CachedRoom(room=object(), timestamp=0.0).timestamp == 0.0


def _make_service(
    ticks_per_minute: int = 1, corruption_overrides: dict[str, CorruptionOverride] | None = None
) -> PassiveCorruptionFluxService:
    config = CorruptionFluxServiceConfig(
        ticks_per_minute=ticks_per_minute, corruption_overrides=corruption_overrides or {}
    )
    return PassiveCorruptionFluxService(config=config)


def _room(
    room_id: str = "room-1",
    sub_zone: str = "",
    zone: str = "",
    plane: str = "earth",
    environment: str = "",
    attributes: dict[str, object] | None = None,
) -> FluxRoom:
    room = MagicMock()
    room.id = room_id
    room.sub_zone = sub_zone
    room.zone = zone
    room.plane = plane
    room.environment = environment
    room.attributes = attributes or {}
    return room


def _player(corruption: int = 0, room_id: str = "room-1") -> MagicMock:
    player = MagicMock()
    player.current_room_id = room_id
    player.get_stats = MagicMock(return_value={"corruption": corruption})
    return player


def test_should_process_tick() -> None:
    svc = _make_service(ticks_per_minute=2)
    assert svc._should_process_tick(0) is True
    assert svc._should_process_tick(1) is False
    assert svc._should_process_tick(2) is True


def test_lookup_target_room_attribute_takes_precedence() -> None:
    svc = _make_service()
    room = _room(attributes={"corruption": 90.0})
    target, source = svc._lookup_target_for_room(room, "day")
    assert target == 90.0
    assert source == "room:room-1"


def test_lookup_rate_and_target_environment_defaults() -> None:
    svc = _make_service()
    room = _room(environment="eldritch")
    rate, rate_source = svc._lookup_rate_for_room(room, "day")
    target, target_source = svc._lookup_target_for_room(room, "day")
    assert rate == 0.03
    assert rate_source == "environment:eldritch"
    assert target == 80.0
    assert target_source == "environment:eldritch"


def test_lookup_rate_night_profile_differs_from_day() -> None:
    svc = _make_service()
    room = _room(environment="haunted")
    day_rate, _ = svc._lookup_rate_for_room(room, "day")
    night_rate, _ = svc._lookup_rate_for_room(room, "night")
    assert day_rate == 0.02
    assert night_rate == 0.04


def test_lookup_db_override_wins_over_static_config() -> None:
    """A DB override still applies when the room authored neither rate nor target itself."""
    svc = _make_service(corruption_overrides={"earth|arkham|downtown": CorruptionOverride(rate=0.5, target=99.0)})
    room = _room(plane="earth", zone="arkham", sub_zone="downtown", environment="eldritch")
    ctx = svc._resolve_context(room, datetime.now(UTC))
    assert ctx.rate == 0.5
    assert ctx.target == 99.0
    assert ctx.source == "db_override"


def test_room_attribute_rate_wins_over_environment_default() -> None:
    svc = _make_service()
    room = _room(environment="eldritch", attributes={"corruption_rate": 0.10})
    rate, source = svc._lookup_rate_for_room(room, "day")
    assert rate == 0.10
    assert source == "room:room-1"


def test_room_attribute_rate_wins_over_db_override() -> None:
    """#824: a room's own attributes.corruption_rate must not be clobbered by a broader
    zone-level special_rules override -- 'most specific wins' applies to rate, not just target.
    (`ctx.source` isn't asserted here: it's a single label that _resolve_context aliases to
    whichever of rate/target last matched a non-default branch, so with the room authoring only a
    rate and the DB override supplying the target, `source` ends up describing the target's
    provenance -- the numeric rate value is the real invariant under test.)"""
    svc = _make_service(corruption_overrides={"earth|arkham|downtown": CorruptionOverride(rate=0.5, target=99.0)})
    room = _room(plane="earth", zone="arkham", sub_zone="downtown", attributes={"corruption_rate": 0.10})
    ctx = svc._resolve_context(room, datetime.now(UTC))
    assert ctx.rate == 0.10


def test_room_attribute_target_wins_over_db_override() -> None:
    """#824: a room's own attributes.corruption (target) must not be clobbered by a broader
    zone-level special_rules corruption_target -- this is what makes a consecrated room with
    target 0 sit safely inside a zone that authors a broadly-corrupting zone-level target."""
    svc = _make_service(corruption_overrides={"earth|arkham|downtown": CorruptionOverride(rate=0.5, target=99.0)})
    room = _room(plane="earth", zone="arkham", sub_zone="downtown", attributes={"corruption": 0})
    ctx = svc._resolve_context(room, datetime.now(UTC))
    assert ctx.target == 0.0
    assert ctx.rate == 0.5  # rate still falls through to the DB override -- room authored no rate
    assert ctx.source == "db_override"


def test_room_authoring_only_rate_still_inherits_db_target() -> None:
    svc = _make_service(corruption_overrides={"earth|arkham|downtown": CorruptionOverride(rate=0.5, target=99.0)})
    room = _room(plane="earth", zone="arkham", sub_zone="downtown", attributes={"corruption_rate": 0.10})
    ctx = svc._resolve_context(room, datetime.now(UTC))
    assert ctx.rate == 0.10
    assert ctx.target == 99.0


def test_signed_flux_direction_derived_from_current_vs_target() -> None:
    assert PassiveCorruptionFluxService._signed_flux_toward_target(10, 80.0, 0.05) == 0.05
    assert PassiveCorruptionFluxService._signed_flux_toward_target(90, 10.0, 0.05) == -0.05
    assert PassiveCorruptionFluxService._signed_flux_toward_target(50, 50.0, 0.05) == 0.0


def test_apply_residual_accumulates_then_emits_delta() -> None:
    svc = _make_service()
    player_id = str(uuid.uuid4())
    assert svc._apply_residual(player_id, 0.4) == 0
    assert svc._apply_residual(player_id, 0.4) == 0
    assert svc._apply_residual(player_id, 0.4) == 1


def test_bound_delta_caps_rise_at_room_target() -> None:
    svc = _make_service()
    # current 78, raw_delta +5 would overshoot the room's target of 80.
    assert svc._bound_delta(78, 5, target=80.0) == 2


def test_bound_delta_floors_fall_at_current_tier_bottom() -> None:
    svc = _make_service()
    # current 30 is MARKED (tier floor 25); a big downward delta must not cross below 25.
    assert svc._bound_delta(30, -10, target=0.0) == -5


def test_tier_floor_boundaries() -> None:
    assert PassiveCorruptionFluxService._tier_floor(0) == 0
    assert PassiveCorruptionFluxService._tier_floor(10) == 1
    assert PassiveCorruptionFluxService._tier_floor(30) == 25
    assert PassiveCorruptionFluxService._tier_floor(60) == 50
    assert PassiveCorruptionFluxService._tier_floor(90) == 75


@pytest.mark.asyncio
async def test_process_tick_for_player_applies_bounded_rising_delta() -> None:
    """A pure player lingering in a corrupt room converges upward, capped at the room's target."""
    svc = _make_service(ticks_per_minute=1)
    player_id = uuid.uuid4()
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock(return_value=_player(corruption=0))
    persistence.get_room_by_id = MagicMock(return_value=_room(attributes={"corruption": 80.0}))
    svc._persistence = persistence

    with (
        # Force the residual bank to emit a delta of +1 on the first tick.
        patch.object(svc, "_apply_residual", return_value=1),
        patch(
            "server.services.passive_corruption_flux.service.CorruptionService.apply_corruption_adjustment",
            new_callable=AsyncMock,
            return_value=CorruptionUpdateResult(
                player_id=player_id,
                previous_value=0,
                new_value=1,
                previous_tier=CorruptionTier.PURE,
                new_tier=CorruptionTier.TOUCHED,
                delta=1,
            ),
        ) as adjust,
    ):
        result = await svc.process_tick_for_player(player_id, tick_count=0)

    assert result["delta"] == 1
    adjust.assert_awaited_once()
    assert adjust.await_args is not None
    assert adjust.await_args.kwargs["reason_code"] == "room_flux"


@pytest.mark.asyncio
async def test_process_tick_for_player_skipped_off_cadence() -> None:
    svc = _make_service(ticks_per_minute=6)
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock()
    svc._persistence = persistence

    result = await svc.process_tick_for_player(uuid.uuid4(), tick_count=1)

    assert result == {"delta": 0}
    persistence.get_player_by_id.assert_not_awaited()


@pytest.mark.asyncio
async def test_process_tick_for_player_no_persistence_is_noop() -> None:
    svc = _make_service(ticks_per_minute=1)
    result = await svc.process_tick_for_player(uuid.uuid4(), tick_count=0)
    assert result == {"delta": 0}


@pytest.mark.asyncio
async def test_process_tick_for_player_zero_delta_skips_write() -> None:
    svc = _make_service(ticks_per_minute=1)
    persistence = MagicMock()
    # Room target equals current value -> zero signed flux -> zero residual delta -> no write.
    persistence.get_player_by_id = AsyncMock(return_value=_player(corruption=50))
    persistence.get_room_by_id = MagicMock(return_value=_room(attributes={"corruption": 50.0}))
    svc._persistence = persistence

    with patch(
        "server.services.passive_corruption_flux.service.CorruptionService.apply_corruption_adjustment",
        new_callable=AsyncMock,
    ) as adjust:
        result = await svc.process_tick_for_player(uuid.uuid4(), tick_count=0)

    assert result == {"delta": 0}
    adjust.assert_not_awaited()


@pytest.mark.asyncio
async def test_innsmouth_pier_converges_upward_and_clamps_at_its_own_ceiling() -> None:
    """#824 (PR-C): models the real Innsmouth Waterfront Pier as authored in the DML --
    attributes.corruption: 65 on the room, corruption_rate: 0.05 + corruption_target: 40 on the
    earth/innsmouth zone's special_rules -- and confirms the room's own target (65) wins over the
    broader zone target (40) per PR-A's room-beats-zone precedence, that a lingering player
    converges upward, and that the ceiling clamps exactly at 65 rather than continuing to rise."""
    svc = _make_service(
        ticks_per_minute=1,
        corruption_overrides={"earth|innsmouth|waterfront": CorruptionOverride(rate=0.05, target=40.0)},
    )
    room = _room(
        room_id="earth_innsmouth_waterfront_room_waterfront_001",
        plane="earth",
        zone="innsmouth",
        sub_zone="waterfront",
        environment="outdoors",
        attributes={"corruption": 65},
    )
    persistence = MagicMock()
    persistence.get_room_by_id = MagicMock(return_value=room)

    # A player seeded just below the ceiling should rise into it and stop; one further tick with
    # a real signed_flux/residual/bound pipeline (no mocked _apply_residual here) confirms the
    # ceiling holds rather than merely asserting the isolated _bound_delta unit in isolation.
    persistence.get_player_by_id = AsyncMock(return_value=_player(corruption=64))
    svc._persistence = persistence

    with patch(
        "server.services.passive_corruption_flux.service.CorruptionService.apply_corruption_adjustment",
        new_callable=AsyncMock,
        return_value=CorruptionUpdateResult(
            player_id=uuid.uuid4(),
            previous_value=64,
            new_value=65,
            previous_tier=CorruptionTier.MARKED,
            new_tier=CorruptionTier.MARKED,
            delta=1,
        ),
    ) as adjust:
        player_id = uuid.uuid4()
        # Force enough banked residual to emit a delta this tick without waiting out 0.05's real
        # ~20-tick cadence -- the cadence itself is covered by test_apply_residual_accumulates_*.
        with patch.object(svc, "_apply_residual", return_value=1):
            result = await svc.process_tick_for_player(player_id, tick_count=0)

    assert result["delta"] == 1
    assert result["new_value"] == 65
    adjust.assert_awaited_once()
    assert adjust.await_args is not None
    assert adjust.await_args.args[1] == 1  # actual_delta clamped to +1, not overshooting past 65
    assert adjust.await_args.kwargs["metadata"]["target"] == 65.0  # room wins over the zone's 40
