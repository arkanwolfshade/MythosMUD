"""
Integration test for lucidity-based LCDitarium respawn.

This test verifies the complete flow:
1. Player lucidity reaches -100 via PassiveLucidityFluxService
2. CatatoniaRegistry failover callback is triggered
3. Player is moved to limbo and respawned at LCDitarium

This test reproduces the bug where players at -100 lucidity are not respawning.
"""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.catatonia_registry import CatatoniaRegistry
from server.services.passive_lucidity_flux_service import PassiveLucidityFluxService
from server.services.player_respawn_service import PlayerRespawnService


@pytest.fixture
async def session_factory():
    """Create a PostgreSQL session factory for tests."""

    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL for this test.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def create_test_player(
    session: AsyncSession,
    *,
    name: str,
    lucidity: int = 100,
    tier: str = "lucid",
    room_id: str = "earth_arkhamcity_downtown_room_derby_st_001",
) -> Player:
    """Create a player and associated lucidity record for testing."""

    player_id = str(uuid.uuid4())
    unique_name = f"{name}-{uuid.uuid4().hex[:8]}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_id}@example.org",
        username=unique_name,
        display_name=unique_name,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=unique_name,
        current_room_id=room_id,
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
async def test_lucidity_respawn_flow_when_lucidity_hits_minus_100(session_factory):
    """
    Test complete respawn flow when lucidity reaches -100.

    This test reproduces the reported bug where players at -100 lucidity
    are not respawning at the LCDitarium.

    NOTE: This test directly uses lucidityService to apply a delta that will
    cross the -100 threshold, bypassing the flux calculation which may not
    work correctly with mocked persistence.
    """
    session_maker = session_factory
    async with session_maker() as session:
        # Create player with lucidity at -99 (just above threshold)
        player = await create_test_player(
            session,
            name="test_victim",
            lucidity=-99,
            tier="catatonic",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
        )
        await session.commit()

        # Track failover callback calls
        failover_calls = []

        async def failover_callback(player_id: str, current_lcd: int) -> None:
            """Track failover callback invocations."""
            failover_calls.append({"player_id": player_id, "current_lcd": current_lcd})
            # Note: In production, the failover callback uses container.database_manager
            # to get a completely independent session. In tests, we need to wait for
            # the lucidity service transaction to complete before attempting respawn.
            import asyncio

            await asyncio.sleep(0.2)  # Allow lucidity service transaction to complete

            # Actually perform the respawn using a fresh session
            # In production, this would use container.database_manager.get_session_maker()
            # For the test, we'll use the session factory to create a new session
            # Convert string player_id to UUID for type safety
            player_id_uuid = uuid.UUID(player_id)
            async with session_maker() as respawn_session:
                respawn_service = PlayerRespawnService()
                await respawn_service.move_player_to_limbo(player_id_uuid, "catatonia_failover", respawn_session)
                await respawn_service.respawn_player(player_id_uuid, respawn_session)

        # Get session maker for failover callback to use
        from server.database import get_database_manager

        db_manager = get_database_manager()
        session_maker = db_manager.get_session_maker()

        # Create catatonia registry with failover callback
        registry = CatatoniaRegistry(failover_callback=failover_callback)

        # Use lucidityService directly to apply a -1 delta that will cross the threshold
        # This bypasses the flux calculation and tests the core failover logic
        from server.services.lucidity_service import lucidityService

        lucidity_service = lucidityService(session, catatonia_observer=registry)

        # Apply -1 lucidity loss (should push from -99 to -100 and trigger failover)
        await lucidity_service.apply_lucidity_adjustment(
            player.player_id,
            -1,
            reason_code="test_crossing_threshold",
        )

        await session.commit()

        # Wait for failover callback to complete (it runs as a background task)
        import asyncio

        await asyncio.sleep(0.5)  # Give failover callback time to execute

        # Refresh player from database
        await session.refresh(player)
        refreshed_lucidity = await session.get(PlayerLucidity, player.player_id)

        # VERIFICATION: Check if failover was triggered
        assert len(failover_calls) > 0, "Failover callback should have been called when lucidity reached -100"
        assert failover_calls[0]["player_id"] == player.player_id
        assert failover_calls[0]["current_lcd"] == -100

        # VERIFICATION: Check if player was respawned at LCDitarium
        assert player.current_room_id == "earth_arkhamcity_LCDitarium_room_foyer_001", (
            f"Player should be at LCDitarium, but is at {player.current_room_id}"
        )

        # VERIFICATION: Check if lucidity is clamped at -100
        assert refreshed_lucidity is not None
        assert refreshed_lucidity.current_lcd == -100


@pytest.mark.asyncio
async def test_lucidity_respawn_flow_from_high_lucidity_to_minus_100(session_factory):
    """
    Test respawn flow when lucidity drops from high value directly to -100.

    This tests the scenario where a massive lucidity loss (like the bug reported earlier)
    causes lucidity to drop from 100 to -100 in one tick.
    """
    session_maker = session_factory
    async with session_maker() as session:
        # Create player with high lucidity
        player = await create_test_player(
            session,
            name="test_victim_2",
            lucidity=100,
            tier="lucid",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
        )
        await session.commit()

        failover_calls = []

        async def failover_callback(player_id: str, current_lcd: int) -> None:
            """Track failover callback invocations."""
            failover_calls.append({"player_id": player_id, "current_lcd": current_lcd})
            # Note: In production, the failover callback uses container.database_manager
            # to get a completely independent session. In tests, we need to wait for
            # the lucidity service transaction to complete before attempting respawn.
            import asyncio

            await asyncio.sleep(0.2)  # Allow lucidity service transaction to complete

            # Actually perform the respawn using a fresh session
            # In production, this would use container.database_manager.get_session_maker()
            # For the test, we'll use the session factory to create a new session
            # Convert string player_id to UUID for type safety
            player_id_uuid = uuid.UUID(player_id)
            async with session_maker() as respawn_session:
                respawn_service = PlayerRespawnService()
                await respawn_service.move_player_to_limbo(player_id_uuid, "catatonia_failover", respawn_session)
                await respawn_service.respawn_player(player_id_uuid, respawn_session)

        # Get session maker for failover callback to use
        from server.database import get_database_manager

        db_manager = get_database_manager()
        session_maker = db_manager.get_session_maker()

        registry = CatatoniaRegistry(failover_callback=failover_callback)

        persistence = MagicMock()
        persistence.get_player = MagicMock(return_value=player)
        persistence.get_room = MagicMock(return_value=MagicMock(plane="earth", zone="arkhamcity", sub_zone="downtown"))

        # Manually apply a massive lucidity loss that would push to -100
        # We'll use the lucidity service directly to simulate this
        from server.services.lucidity_service import lucidityService

        lucidity_service = lucidityService(session, catatonia_observer=registry)
        # Apply -200 lucidity loss (should clamp to -100)
        await lucidity_service.apply_lucidity_adjustment(
            player.player_id,
            -200,
            reason_code="test_massive_loss",
        )
        await session.commit()

        # Wait for failover callback to complete (it runs as a background task)
        import asyncio

        await asyncio.sleep(0.5)  # Give failover callback time to execute

        # Refresh player
        await session.refresh(player)

        # VERIFICATION: Failover should have been triggered
        assert len(failover_calls) > 0, "Failover callback should have been called"
        assert failover_calls[0]["current_lcd"] == -100

        # VERIFICATION: Player should be at LCDitarium
        assert player.current_room_id == "earth_arkhamcity_LCDitarium_room_foyer_001", (
            f"Player should be at LCDitarium, but is at {player.current_room_id}"
        )


@pytest.mark.asyncio
async def test_lucidity_respawn_flow_without_observer(session_factory):
    """
    Test that respawn does NOT happen when catatonia_observer is None.

    This verifies that the observer is required for the respawn flow.
    """
    session_maker = session_factory
    async with session_maker() as session:
        player = await create_test_player(
            session,
            name="test_victim_3",
            lucidity=-99,
            tier="catatonic",
            room_id="earth_arkhamcity_downtown_room_derby_st_001",
        )
        await session.commit()

        original_room = player.current_room_id

        # Create flux service WITHOUT catatonia observer
        persistence = MagicMock()
        persistence.get_player = MagicMock(return_value=player)
        persistence.get_room = MagicMock(return_value=MagicMock(plane="earth", zone="arkhamcity", sub_zone="downtown"))

        flux_service = PassiveLucidityFluxService(
            persistence=persistence,
            catatonia_observer=None,  # No observer!
        )

        # Process tick
        await flux_service.process_tick(tick_count=1, session=session, now=None)
        await session.commit()

        # Refresh player
        await session.refresh(player)

        # VERIFICATION: Player should NOT have moved (no observer = no respawn)
        assert player.current_room_id == original_room, "Player should not have moved without observer"


@pytest.mark.asyncio
async def test_lucidity_respawn_flow_condition_check(session_factory):
    """
    Test that the condition `new_LCD <= -100 and previous_LCD > -100` works correctly.

    This verifies the exact condition that triggers respawn.
    """
    session_maker = session_factory
    async with session_maker() as session:
        # Test case 1: Player already at -100 (should NOT trigger again)
        player1 = await create_test_player(
            session,
            name="test_already_at_minus_100",
            lucidity=-100,
            tier="catatonic",
        )
        await session.commit()

        failover_calls_1 = []

        async def failover_callback_1(player_id: str, current_lcd: int) -> None:
            failover_calls_1.append({"player_id": player_id, "current_lcd": current_lcd})

        registry1 = CatatoniaRegistry(failover_callback=failover_callback_1)

        from server.services.lucidity_service import lucidityService

        lucidity_service1 = lucidityService(session, catatonia_observer=registry1)
        # Try to apply more lucidity loss (should stay at -100)
        await lucidity_service1.apply_lucidity_adjustment(player1.player_id, -10, reason_code="test")
        await session.commit()

        # VERIFICATION: Should NOT trigger failover (already at -100)
        assert len(failover_calls_1) == 0, "Failover should not trigger if already at -100"

        # Test case 2: Player at -99, apply -1 (should trigger)
        player2 = await create_test_player(
            session,
            name="test_crossing_threshold",
            lucidity=-99,
            tier="catatonic",
        )
        await session.commit()

        failover_calls_2 = []

        async def failover_callback_2(player_id: str, current_lcd: int) -> None:
            failover_calls_2.append({"player_id": player_id, "current_lcd": current_lcd})

        registry2 = CatatoniaRegistry(failover_callback=failover_callback_2)

        lucidity_service2 = lucidityService(session, catatonia_observer=registry2)
        # Apply -1 lucidity loss (should cross threshold)
        await lucidity_service2.apply_lucidity_adjustment(player2.player_id, -1, reason_code="test")
        await session.commit()

        # VERIFICATION: Should trigger failover (crossing from -99 to -100)
        assert len(failover_calls_2) > 0, "Failover should trigger when crossing -100 threshold"
        assert failover_calls_2[0]["current_lcd"] == -100
