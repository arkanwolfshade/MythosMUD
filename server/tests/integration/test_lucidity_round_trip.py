"""
Integration test for lucidity service round-trip.
"""

import uuid

import pytest

from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import LucidityService


@pytest.mark.asyncio
@pytest.mark.serial  # Ensure this runs serially to avoid event loop conflicts
async def test_lucidity_adjustment_round_trip(session_factory):
    """
    Test that LucidityService can adjust lucidity and persist changes.

    CRITICAL: This test is marked as serial to ensure it runs sequentially
    and avoids Windows event loop issues with asyncpg.
    """
    async with session_factory() as session:
        # Create user and player
        user_id = str(uuid.uuid4())
        player_id = str(uuid.uuid4())

        user = User(
            id=user_id,
            email=f"test_{user_id}@example.com",
            username=f"testuser_{user_id[:8]}",
            display_name=f"Test User {user_id[:8]}",
            hashed_password="hashed",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        player = Player(
            player_id=player_id,
            user_id=user_id,
            name=f"testplayer_{player_id[:8]}",
            current_room_id="earth_arkhamcity_intersection_derby_high",
        )

        # Create all entities in the same transaction to ensure foreign key constraints
        # are satisfied and all records are visible to queries within the same session
        user = User(
            id=user_id,
            email=f"test_{user_id}@example.com",
            username=f"testuser_{user_id[:8]}",
            display_name=f"Test User {user_id[:8]}",
            hashed_password="hashed",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        player = Player(
            player_id=player_id,
            user_id=user_id,
            name=f"testplayer_{player_id[:8]}",
            current_room_id="earth_arkhamcity_intersection_derby_high",
        )
        lucidity_record = PlayerLucidity(
            player_id=player_id,
            current_lcd=50,
            current_tier="uneasy",
        )
        
        # Add all entities and flush to make them visible within the same transaction
        # This ensures get_or_create_player_lucidity will find the existing record
        session.add_all([user, player, lucidity_record])
        await session.flush()  # Flush to make records visible to queries in same session

        # Apply adjustment
        service = LucidityService(session)
        result = await service.apply_lucidity_adjustment(
            player_id=uuid.UUID(player_id),
            delta=-10,
            reason_code="test_adjustment",
        )

        await session.commit()

        # Verify result
        assert result.previous_lcd == 50
        assert result.new_lcd == 40

        # Re-read from database
        refreshed = await session.get(PlayerLucidity, player_id)
        assert refreshed is not None
        assert refreshed.current_lcd == 40
        assert refreshed.current_tier == result.new_tier
