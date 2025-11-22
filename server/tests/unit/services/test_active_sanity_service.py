"""Tests for the active sanity adjustment service."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.player import Player
from server.models.sanity import PlayerSanity, SanityCooldown
from server.models.user import User


@pytest.fixture
async def session_factory():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL for this test.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # PostgreSQL always enforces foreign keys - no PRAGMA needed
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def create_player(session: AsyncSession, *, room_id: str, sanity: int = 100, tier: str = "lucid") -> Player:
    player_id = str(uuid.uuid4())
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.com",
        username=player_id,
        display_name=player_id,
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
async def test_encounter_loss_first_and_repeat(session_factory):
    async with session_factory() as session:
        player = await create_player(session, room_id="earth_arkhamcity_downtown_room_curwen_st_017")
        from server.services.active_sanity_service import ActiveSanityService

        fixed_now = datetime(2025, 1, 1, 12, 0, tzinfo=UTC)
        service = ActiveSanityService(session, now_provider=lambda: fixed_now)

        first = await service.apply_encounter_sanity_loss(
            player_id=player.player_id,
            entity_archetype="disturbing_ghoul",
            category="disturbing",
            location_id="earth_arkhamcity_downtown_room_curwen_st_017",
        )
        assert first.delta == -6

        repeat = await service.apply_encounter_sanity_loss(
            player_id=player.player_id,
            entity_archetype="disturbing_ghoul",
            category="disturbing",
            location_id="earth_arkhamcity_downtown_room_curwen_st_017",
        )
        assert repeat.delta == -2

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_san == 92


@pytest.mark.asyncio
async def test_encounter_acclimation_reduces_loss(session_factory):
    async with session_factory() as session:
        player = await create_player(session, room_id="earth_arkhamcity_downtown_room_curwen_st_017", sanity=100)
        from server.services.active_sanity_service import ActiveSanityService

        service = ActiveSanityService(session, now_provider=lambda: datetime.now(UTC))

        deltas = []
        for _ in range(6):
            result = await service.apply_encounter_sanity_loss(
                player_id=player.player_id,
                entity_archetype="cosmic_outer_god",
                category="cosmic",
                location_id="earth_arkhamcity_downtown_room_curwen_st_017",
            )
            deltas.append(result.delta)

        assert deltas[0] == -20  # first-time
        assert deltas[1] == -10  # repeat
        assert deltas[-1] == -5  # acclimated half-loss

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_san == 100 + sum(deltas)


@pytest.mark.asyncio
async def test_recovery_action_pray_sets_cooldown(session_factory):
    async with session_factory() as session:
        player = await create_player(session, room_id="earth_arkhamcity_sanitarium_room_foyer_001", sanity=40)
        from server.services.active_sanity_service import ActiveSanityService

        now = datetime(2025, 1, 1, 18, 0, tzinfo=UTC)
        service = ActiveSanityService(session, now_provider=lambda: now)

        result = await service.perform_recovery_action(
            player_id=player.player_id,
            action_code="pray",
            location_id="earth_arkhamcity_sanitarium_room_foyer_001",
        )
        assert result.delta == 8

        cooldown = (
            await session.execute(
                select(SanityCooldown).where(
                    SanityCooldown.player_id == player.player_id, SanityCooldown.action_code == "pray"
                )
            )
        ).scalar_one()
        stored_expiry = cooldown.cooldown_expires_at
        assert stored_expiry is not None
        assert stored_expiry.replace(tzinfo=UTC) == now + timedelta(minutes=15)

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_san == 48


@pytest.mark.asyncio
async def test_recovery_action_respects_cooldown(session_factory):
    async with session_factory() as session:
        player = await create_player(session, room_id="earth_arkhamcity_sanitarium_room_foyer_001", sanity=70)
        from server.services.active_sanity_service import ActiveSanityService, SanityActionOnCooldownError

        now = datetime(2025, 3, 15, 9, 0, tzinfo=UTC)
        service = ActiveSanityService(session, now_provider=lambda: now)

        await service.perform_recovery_action(
            player_id=player.player_id,
            action_code="pray",
            location_id="earth_arkhamcity_sanitarium_room_foyer_001",
        )

        with pytest.raises(SanityActionOnCooldownError):
            await service.perform_recovery_action(
                player_id=player.player_id,
                action_code="pray",
                location_id="earth_arkhamcity_sanitarium_room_foyer_001",
            )
