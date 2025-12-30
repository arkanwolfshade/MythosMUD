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
    1. Create prerequisites (user, player) in a single transaction
    2. Service creates the lucidity record (defaults to 100 LCD, "lucid" tier)
    3. Service adjusts the lucidity
    4. Changes are persisted and verified

    CRITICAL: All database operations happen within a single session/transaction
    to avoid foreign key constraint violations with NullPool connections.
    """
    async with session_factory() as session:
        # Create user and player - prerequisites for lucidity record
        # These must be committed before the service can create PlayerLucidity
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

        # CRITICAL: With NullPool and pytest-xdist parallel execution, committing
        # the player separately can cause visibility issues. The service's
        # get_or_create_player_lucidity() does a flush() which requires the player
        # to exist for the foreign key constraint.
        #
        # Strategy: Keep user and player in the same transaction context as the
        # service operations. We flush them to ensure they're in the database,
        # but don't commit until after the service operations complete.
        # This ensures the foreign key constraint is satisfied because everything
        # happens in one transaction.
        session.add_all([user, player])
        await session.flush()  # Flush to ensure objects are in the database for FK checks
        # DO NOT commit here - keep everything in the same transaction

        # Now use the service - it will create the lucidity record if it doesn't exist
        # Default initial state: current_lcd=100, current_tier="lucid"
        # The player is now committed and in the session, so the foreign key constraint will be satisfied
        service = LucidityService(session)
        delta = -60  # Adjust from 100 to 40, which should change tier from "lucid" to "uneasy"
        expected_new_lcd = 100 + delta  # 40

        result = await service.apply_lucidity_adjustment(
            player_id=player_id,
            delta=delta,
            reason_code="test_adjustment",
        )

        # Verify the service result
        # Service creates record with defaults: previous_lcd=100, previous_tier="lucid"
        assert result.previous_lcd == 100
        assert result.previous_tier == "lucid"
        assert result.new_lcd == expected_new_lcd
        assert result.new_tier == "uneasy"  # 40 LCD is in the "uneasy" tier range

        # Verify the record exists in the session before commit
        # This confirms the service created it successfully
        from sqlalchemy import select

        pre_commit_stmt = select(PlayerLucidity).where(PlayerLucidity.player_id == player_id)
        pre_commit_result = await session.execute(pre_commit_stmt)
        pre_commit_record = pre_commit_result.scalar_one_or_none()
        assert pre_commit_record is not None, "PlayerLucidity should exist in session before commit"
        assert pre_commit_record.current_lcd == expected_new_lcd

        # Commit the service's modifications (creates PlayerLucidity record and adjustment log)
        # All operations (user, player, lucidity record) are in the same transaction
        # The service has already done flush(), so commit() will persist everything
        try:
            await session.commit()
        except Exception as e:
            pytest.fail(f"Commit failed with error: {type(e).__name__}: {e}")

        # Verify persistence by reading the record back from the database
        # Use a fresh session to ensure we're reading committed data
        # This is necessary with NullPool where the same session might not see committed data
        from server.services.lucidity_service import LucidityRepository

        async with session_factory() as verify_session:
            verify_repo = LucidityRepository(verify_session)
            fetched = await verify_repo.get_player_lucidity(player_id)

            assert fetched is not None, (
                f"PlayerLucidity record should exist after commit. "
                f"Pre-commit check passed (record existed), but post-commit check failed. "
                f"This suggests the commit did not persist the record. "
                f"Player ID: {player_id}"
            )
            assert fetched.current_lcd == expected_new_lcd
            assert fetched.current_tier == result.new_tier
