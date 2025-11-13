"""Tests for passive SAN flux service."""

from __future__ import annotations

import math
import uuid
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.player import Player
from server.models.sanity import PlayerSanity
from server.models.user import User
from server.services.passive_sanity_flux_service import (
    PassiveFluxContext,
    PassiveSanityFluxService,
)


@pytest.fixture
async def session_factory():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", future=True)
    async with engine.begin() as conn:
        await conn.exec_driver_sql("PRAGMA foreign_keys=ON")
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def _create_player(session: AsyncSession, *, room_id: str, sanity: int = 100, tier: str = "lucid") -> Player:
    player_id = f"player-{uuid.uuid4()}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.com",
        username=player_id,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=player_id,
        current_room_id=room_id,
    )
    session.add_all([user, player])
    session.add(
        PlayerSanity(
            player_id=player_id,
            current_san=sanity,
            current_tier=tier,
        )
    )
    await session.flush()
    return player


@pytest.mark.asyncio
async def test_positive_flux_accumulates_and_applies(session_factory):
    async with session_factory() as session:
        player = await _create_player(session, room_id="earth_sunlit_garden", sanity=90)

        flux_service = PassiveSanityFluxService(
            persistence=None,
            ticks_per_minute=1,
            context_resolver=lambda _player, _now: PassiveFluxContext(base_flux=0.6, source="test"),
        )

        result = await flux_service.process_tick(session, tick_count=1, now=datetime.now(UTC))
        assert result["adjustments"] == 0  # residual below threshold

        result = await flux_service.process_tick(session, tick_count=2, now=datetime.now(UTC))
        assert result["adjustments"] == 1

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        await session.refresh(refreshed)
        assert refreshed is not None
        assert refreshed.current_san == 91
        assert math.isclose(flux_service._residuals[player.player_id], 0.2, rel_tol=1e-6)


@pytest.mark.asyncio
async def test_negative_flux_respects_adaptive_resistance(session_factory):
    async with session_factory() as session:
        player = await _create_player(session, room_id="earth_haunted_chapel")

        flux_service = PassiveSanityFluxService(
            persistence=None,
            ticks_per_minute=1,
            adaptive_window_minutes=2,
            context_resolver=lambda _player, _now: PassiveFluxContext(base_flux=-1.0, source="drain"),
        )

        tick_time = datetime.now(UTC)
        total_ticks = 6
        for tick in range(1, total_ticks + 1):
            await flux_service.process_tick(session, tick_count=tick, now=tick_time + timedelta(minutes=tick))

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        await session.refresh(refreshed)
        assert refreshed is not None

        # Without adaptive resistance we'd lose 6 SAN; ensure we lost less.
        assert refreshed.current_san > 94
        assert refreshed.current_san < 100


@pytest.mark.asyncio
async def test_companion_bonus_accumulates(session_factory):
    async with session_factory() as session:
        player = await _create_player(session, room_id="earth_campus_quad", sanity=60, tier="uneasy")
        await _create_player(session, room_id="earth_campus_quad", sanity=100, tier="lucid")

        flux_service = PassiveSanityFluxService(
            persistence=None,
            ticks_per_minute=1,
            context_resolver=lambda _player, _now: PassiveFluxContext(base_flux=0.0, source="companions"),
        )

        start_time = datetime.now(UTC)
        for tick in range(1, 11):
            await flux_service.process_tick(session, tick_count=tick, now=start_time + timedelta(minutes=tick))

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        await session.refresh(refreshed)
        assert refreshed is not None
        companion_residual = flux_service._residuals.get(player.player_id, 0.0)
        assert abs(companion_residual) < 1e-5
        assert refreshed.current_san >= 61  # companion support created net gain
