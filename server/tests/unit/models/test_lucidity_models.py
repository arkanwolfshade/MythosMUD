"""Unit tests for lucidity persistence models."""

from __future__ import annotations

import uuid
from datetime import datetime

import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from server.models.base import Base
from server.models.lucidity import (
    LucidityAdjustmentLog,
    LucidityCooldown,
    LucidityExposureState,
    PlayerLucidity,
)
from server.models.player import Player
from server.models.user import User


def build_engine():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
    # Convert async URL to sync URL for create_engine
    sync_url = database_url.replace("+asyncpg", "")
    engine = create_engine(sync_url, future=True)
    # PostgreSQL always enforces foreign keys - no PRAGMA needed
    return engine


def create_user_and_player(session: Session, player_id: str, username: str) -> Player:
    """Create a basic user/player pair for lucidity testing."""
    user = User(
        id=str(uuid.uuid4()),
        email=f"{username}@example.com",
        username=username,
        display_name=username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=player_id,
        user_id=user.id,
        name=username.capitalize(),
    )
    session.add_all([user, player])
    session.flush()
    return player


@pytest.mark.serial  # Mark as serial to prevent database table creation conflicts in parallel execution
@pytest.mark.xdist_group(name="serial_lucidity_tests")  # Force serial execution with pytest-xdist
def test_player_lucidity_defaults_and_constraints():
    engine = build_engine()
    Base.metadata.create_all(engine)

    try:
        # Generate unique identifiers to avoid constraint violations on repeated test runs
        player_id = str(uuid.uuid4())  # Use proper UUID format for PostgreSQL
        unique_suffix = str(uuid.uuid4())[:8]
        username = f"arkhamite-{unique_suffix}"

        with Session(engine) as session:
            player = create_user_and_player(session, player_id, username)

            player_lucidity = PlayerLucidity()
            player.lucidity = player_lucidity
            session.commit()

            persisted = session.get(PlayerLucidity, player_id)
            assert persisted is not None
            assert persisted.current_lcd == 100
            assert persisted.current_tier == "lucid"
            assert persisted.liabilities == "[]"

            persisted.current_lcd = -25
            persisted.current_tier = "uneasy"
            session.commit()

            persisted.current_lcd = 120
            with pytest.raises(IntegrityError):
                session.flush()
            session.rollback()

            persisted.current_tier = "eldritch"
            with pytest.raises(IntegrityError):
                session.flush()
            session.rollback()

            # Use a valid UUID format that doesn't exist in the database (for foreign key constraint test)
            nonexistent_player_id = str(uuid.uuid4())
            rogue_lucidity = PlayerLucidity(player_id=nonexistent_player_id)
            session.add(rogue_lucidity)
            with pytest.raises(IntegrityError):
                session.flush()
            session.rollback()
    finally:
        # Clean up tables
        try:
            Base.metadata.drop_all(engine)
        except Exception:  # pylint: disable=broad-except
            # Ignore cleanup errors - tables may already be dropped or in use
            pass
        engine.dispose()


def test_lucidity_relationships_cascade():
    engine = build_engine()
    Base.metadata.create_all(engine)

    # Generate unique identifiers to avoid constraint violations on repeated test runs
    player_id = str(uuid.uuid4())  # Use proper UUID format for PostgreSQL
    unique_suffix = str(uuid.uuid4())[:8]
    username = f"miskatonic-{unique_suffix}"

    with Session(engine) as session:
        player = create_user_and_player(session, player_id, username)

        player.lucidity = PlayerLucidity(current_lcd=88, current_tier="uneasy")
        player.lucidity_adjustments.append(
            LucidityAdjustmentLog(
                delta=-12,
                reason_code="eldritch_whispers",
                metadata_payload='{"source":"library"}',
            )
        )
        player.lucidity_exposures.append(LucidityExposureState(entity_archetype="star_vampire", encounter_count=3))
        player.lucidity_cooldowns.append(
            LucidityCooldown(
                action_code="pray",
                cooldown_expires_at=datetime.fromisoformat("2099-01-01T00:00:00"),
            )
        )

        session.commit()

        session.delete(player)
        session.commit()

        # Check that only our test player's records were deleted (filter by player_id)
        lucidity_rows = session.execute(select(PlayerLucidity).where(PlayerLucidity.player_id == player_id)).all()
        adjustment_rows = session.execute(
            select(LucidityAdjustmentLog).where(LucidityAdjustmentLog.player_id == player_id)
        ).all()
        exposure_rows = session.execute(
            select(LucidityExposureState).where(LucidityExposureState.player_id == player_id)
        ).all()
        cooldown_rows = session.execute(select(LucidityCooldown).where(LucidityCooldown.player_id == player_id)).all()

        assert not lucidity_rows, f"PlayerLucidity records for {player_id} should be deleted"
        assert not adjustment_rows, f"LucidityAdjustmentLog records for {player_id} should be deleted"
        assert not exposure_rows, f"LucidityExposureState records for {player_id} should be deleted"
        assert not cooldown_rows, f"LucidityCooldown records for {player_id} should be deleted"
