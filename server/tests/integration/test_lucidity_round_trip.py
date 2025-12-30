"""
Integration test for lucidity service round-trip.

Tests that LucidityService can find or create a lucidity record,
apply adjustments, and persist changes correctly.
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

    This test verifies the full round-trip:
    1. Create prerequisites (user, player)
    2. Create initial lucidity record
    3. Service finds and adjusts the record
    4. Changes are persisted
    """
    async with session_factory() as session:
        # Create user and player - prerequisites for lucidity record
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

        # Create user and player first, commit to satisfy foreign key constraints
        session.add_all([user, player])
        await session.commit()

        # Create lucidity record with known initial state
        # PlayerLucidity model expects player_id as UUID (Mapped[uuid.UUID])
        initial_lcd = 50
        lucidity_record = PlayerLucidity(
            player_id=player_id,
            current_lcd=initial_lcd,
            current_tier="uneasy",
        )
        session.add(lucidity_record)
        await session.commit()

        # Now use the service to adjust the lucidity
        # The service will query for the record and should find the committed one
        service = LucidityService(session)
        delta = -10
        expected_new_lcd = initial_lcd + delta

        result = await service.apply_lucidity_adjustment(
            player_id=player_id,
            delta=delta,
            reason_code="test_adjustment",
        )

        # Verify the service result
        assert result.previous_lcd == initial_lcd
        assert result.new_lcd == expected_new_lcd

        # Commit the service's modifications
        await session.commit()

        # Verify persistence by reading the record back from the database
        # Use a fresh query to ensure we're reading committed data
        fetched = await session.get(PlayerLucidity, player_id)
        assert fetched is not None
        assert fetched.current_lcd == expected_new_lcd
        assert fetched.current_tier == result.new_tier
