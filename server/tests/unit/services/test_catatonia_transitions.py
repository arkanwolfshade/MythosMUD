"""Tests for catatonia transitions within the sanity service."""

from __future__ import annotations

import uuid
from unittest.mock import ANY, MagicMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from server.models.base import Base
from server.models.player import Player
from server.models.sanity import PlayerSanity
from server.models.user import User
from server.services.sanity_service import SanityService


@pytest.fixture
async def session_factory():
    """Create an in-memory SQLite session factory."""

    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        future=True,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    async with engine.begin() as conn:
        await conn.exec_driver_sql("PRAGMA foreign_keys=ON")
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def create_player(
    session: AsyncSession,
    *,
    name: str,
    sanity: int = 100,
    tier: str = "lucid",
) -> Player:
    """Create a player and associated sanity record for testing."""

    player_id = f"player-{uuid.uuid4()}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.org",
        username=name,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=name,
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
    )
    sanity_record = PlayerSanity(
        player_id=player_id,
        current_san=sanity,
        current_tier=tier,
    )
    session.add_all([user, player, sanity_record])
    await session.flush()
    return player


@pytest.mark.asyncio
async def test_catatonia_entry_sets_timestamp_and_notifies(session_factory):
    """Ensure entering catatonia stamps the record and notifies observers."""

    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, name="victim", sanity=5, tier="deranged")
        observer = MagicMock()
        service = SanityService(session, catatonia_observer=observer)

        result = await service.apply_sanity_adjustment(
            player.player_id,
            -10,
            reason_code="eldritch_cascade",
            metadata={"source": "unit_test"},
        )
        await session.commit()

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_tier == "catatonic"
        assert refreshed.catatonia_entered_at is not None

        observer.on_catatonia_entered.assert_called_once_with(
            player_id=player.player_id,
            entered_at=ANY,
            current_san=result.new_san,
        )
        observer.on_catatonia_cleared.assert_not_called()


@pytest.mark.asyncio
async def test_catatonia_clearance_resets_timestamp_and_notifies(session_factory):
    """Ensure recovering from catatonia clears timestamp and notifies observers."""

    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, name="victim", sanity=5, tier="deranged")
        observer = MagicMock()
        service = SanityService(session, catatonia_observer=observer)

        await service.apply_sanity_adjustment(player.player_id, -15, reason_code="shock")
        await session.commit()

        observer.reset_mock()

        await service.apply_sanity_adjustment(player.player_id, 20, reason_code="rescue_ritual")
        await session.commit()

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_tier != "catatonic"
        assert refreshed.catatonia_entered_at is None

        observer.on_catatonia_cleared.assert_called_once_with(
            player_id=player.player_id,
            resolved_at=ANY,
        )


@pytest.mark.asyncio
async def test_catatonia_failover_notifies_when_san_bottoms_out(session_factory):
    """Ensure observers are notified when SAN hits the absolute floor."""

    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, name="victim", sanity=0, tier="catatonic")
        observer = MagicMock()
        service = SanityService(session, catatonia_observer=observer)

        await service.apply_sanity_adjustment(player.player_id, -200, reason_code="void_gaze")
        await session.commit()

        refreshed = await session.get(PlayerSanity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_san == -100

        observer.on_sanitarium_failover.assert_called_once_with(
            player_id=player.player_id,
            current_san=-100,
        )
