"""Tests for catatonia transitions within the lucidity service."""

from __future__ import annotations

import uuid
from unittest.mock import ANY, MagicMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import LucidityService


@pytest.fixture
async def session_factory():
    """Create a PostgreSQL session factory for tests."""

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


async def create_player(
    session: AsyncSession,
    *,
    name: str,
    lucidity: int = 100,
    tier: str = "lucid",
) -> Player:
    """Create a player and associated lucidity record for testing."""

    player_id = str(uuid.uuid4())
    # Add unique suffix to username to avoid conflicts in parallel test runs
    unique_suffix = str(uuid.uuid4())[:8]
    unique_username = f"{name}-{unique_suffix}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.org",
        username=unique_username,
        display_name=unique_username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=unique_username,  # Use unique username to avoid duplicate key violations
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
    )
    lucidity_record = PlayerLucidity(
        player_id=player_id,
        current_lcd=lucidity,
        current_tier=tier,
    )
    session.add_all([user, player, lucidity_record])
    await session.flush()
    return player


@pytest.mark.asyncio
async def test_catatonia_entry_sets_timestamp_and_notifies(session_factory):
    """Ensure entering catatonia stamps the record and notifies observers."""

    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, name="victim", lucidity=5, tier="deranged")
        observer = MagicMock()
        service = LucidityService(session, catatonia_observer=observer)

        result = await service.apply_lucidity_adjustment(
            player.player_id,
            -10,
            reason_code="eldritch_cascade",
            metadata={"source": "unit_test"},
        )
        await session.commit()

        refreshed = await session.get(PlayerLucidity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_tier == "catatonic"
        assert refreshed.catatonia_entered_at is not None

        observer.on_catatonia_entered.assert_called_once_with(
            player_id=player.player_id,
            entered_at=ANY,
            current_lcd=result.new_lcd,
        )
        observer.on_catatonia_cleared.assert_not_called()


@pytest.mark.asyncio
async def test_catatonia_clearance_resets_timestamp_and_notifies(session_factory):
    """Ensure recovering from catatonia clears timestamp and notifies observers."""

    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, name="victim", lucidity=5, tier="deranged")
        # Commit player creation to ensure foreign key constraints are satisfied
        await session.commit()

        observer = MagicMock()
        service = LucidityService(session, catatonia_observer=observer)

        await service.apply_lucidity_adjustment(player.player_id, -15, reason_code="shock")
        await session.commit()

        observer.reset_mock()

        await service.apply_lucidity_adjustment(player.player_id, 20, reason_code="rescue_ritual")
        await session.commit()

        refreshed = await session.get(PlayerLucidity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_tier != "catatonic"
        assert refreshed.catatonia_entered_at is None

        observer.on_catatonia_cleared.assert_called_once_with(
            player_id=player.player_id,
            resolved_at=ANY,
        )


@pytest.mark.asyncio
async def test_catatonia_failover_notifies_when_san_bottoms_out(session_factory):
    """Ensure observers are notified when LCD hits the absolute floor."""

    session_maker = session_factory
    async with session_maker() as session:
        player = await create_player(session, name="victim", lucidity=0, tier="catatonic")
        observer = MagicMock()
        service = LucidityService(session, catatonia_observer=observer)

        await service.apply_lucidity_adjustment(player.player_id, -200, reason_code="void_gaze")
        await session.commit()

        refreshed = await session.get(PlayerLucidity, player.player_id)
        assert refreshed is not None
        assert refreshed.current_lcd == -100

        observer.on_sanitarium_failover.assert_called_once_with(
            player_id=player.player_id,
            current_lcd=-100,
        )
