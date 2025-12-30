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
        # Keep player_id as UUID throughout - only convert to string when Player model requires it
        user_id = uuid.uuid4()
        player_id = uuid.uuid4()

        user = User(
            id=str(user_id),
            email=f"test_{user_id}@example.com",
            username=f"testuser_{str(user_id)[:8]}",
            display_name=f"Test User {str(user_id)[:8]}",
            hashed_password="hashed",
            is_active=True,
            is_superuser=False,
            is_verified=True,
        )
        # Player model expects player_id as string (Mapped[str]) even though DB stores UUID
        player = Player(
            player_id=str(player_id),
            user_id=str(user_id),
            name=f"testplayer_{str(player_id)[:8]}",
            current_room_id="earth_arkhamcity_intersection_derby_high",
        )
        # PlayerLucidity model expects player_id as UUID (Mapped[uuid.UUID])
        lucidity_record = PlayerLucidity(
            player_id=player_id,
            current_lcd=50,
            current_tier="uneasy",
        )

        # Add entities one at a time and commit to ensure they're persisted
        # This avoids event loop issues with asyncpg when using add_all + flush
        session.add(user)
        await session.commit()

        session.add(player)
        await session.commit()

        session.add(lucidity_record)
        await session.commit()

        # Apply adjustment - service expects UUID
        service = LucidityService(session)
        result = await service.apply_lucidity_adjustment(
            player_id=player_id,
            delta=-10,
            reason_code="test_adjustment",
        )

        await session.commit()

        # Verify result
        assert result.previous_lcd == 50
        assert result.new_lcd == 40

        # Re-read from database - PlayerLucidity uses UUID as primary key
        refreshed = await session.get(PlayerLucidity, player_id)
        assert refreshed is not None
        assert refreshed.current_lcd == 40
        assert refreshed.current_tier == result.new_tier
