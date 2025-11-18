"""Tests verifying player position persistence across login/logout cycles."""

from __future__ import annotations

from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.database import get_database_url
from server.models.base import Base
from server.models.player import Player
from server.models.user import User
from server.persistence import PersistenceLayer


@pytest.fixture
async def async_session_factory():
    """Create an async session factory for database setup."""
    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # Create tables
        await conn.run_sync(Base.metadata.create_all)

    factory = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield factory
    finally:
        await engine.dispose()


async def initialize_database(session: AsyncSession, user_id: str = "test-user-position") -> None:
    """Create required schema and seed data in PostgreSQL."""
    import uuid

    # Generate unique suffix from user_id or create new one
    unique_suffix = user_id.split("-")[-1] if "-" in user_id else str(uuid.uuid4())[:8]

    # Create user with unique email and username
    user = User(
        id=user_id,
        email=f"position_test_{unique_suffix}@example.com",
        username=f"position_test_user_{unique_suffix}",
        hashed_password="hashed-password",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    session.add(user)
    await session.commit()


def build_player(player_id: str, user_id: str) -> Player:
    """Create a Player instance with timestamps normalized for persistence tests."""
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name="PositionTester",
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
    )
    now = datetime.now(UTC).replace(tzinfo=None)
    player.created_at = now  # type: ignore[assignment]
    player.last_active = now  # type: ignore[assignment]
    return player


def test_player_stats_include_position_by_default():
    """Ensure newly constructed Player stats include a standing position."""
    player = build_player("player-default-position", "user-default-position")
    stats = player.get_stats()

    assert "position" in stats, "position field should be present in default stats"
    assert stats["position"] == "standing", "default position should be standing"


@pytest.mark.asyncio
async def test_position_persists_across_logout_login_cycle(async_session_factory):
    """Verify that player position changes persist after saving and reloading."""
    import uuid

    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    # Generate unique identifiers to avoid constraint violations on repeated test runs
    unique_suffix = str(uuid.uuid4())[:8]
    user_id = f"position-user-{unique_suffix}"

    async with async_session_factory() as session:
        await initialize_database(session, user_id=user_id)
        await session.commit()

    persistence = PersistenceLayer(db_path=database_url)

    player_id = f"position-player-{unique_suffix}"
    player = build_player(player_id, user_id)

    # Initial save representing the player's first login.
    persistence.save_player(player)

    # Load the player (simulating a login) and confirm standing.
    loaded_player = persistence.get_player(player_id)
    assert loaded_player is not None, "player should load successfully after initial save"
    assert loaded_player.get_stats()["position"] == "standing"

    # Change position to sitting and persist (simulating logout).
    updated_stats = loaded_player.get_stats()
    updated_stats["position"] = "sitting"
    loaded_player.set_stats(updated_stats)
    persistence.save_player(loaded_player)

    # Reload and ensure the sitting posture persisted.
    reloaded_player = persistence.get_player(player_id)
    assert reloaded_player is not None, "player should load successfully after updating position"
    assert reloaded_player.get_stats()["position"] == "sitting"


@pytest.mark.asyncio
async def test_missing_position_defaults_to_standing_on_load(async_session_factory):
    """Players with legacy stats lacking position should default to standing."""
    import uuid

    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    # Generate unique identifiers to avoid constraint violations on repeated test runs
    unique_suffix = str(uuid.uuid4())[:8]
    user_id = f"legacy-position-user-{unique_suffix}"

    async with async_session_factory() as session:
        await initialize_database(session, user_id=user_id)

        # Insert legacy stats without a position field using PostgreSQL syntax
        legacy_stats = (
            '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, '
            '"wisdom": 10, "charisma": 10, "sanity": 100, "occult_knowledge": 0, '
            '"fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100}'
        )

        player_id = f"legacy-player-{unique_suffix}"
        # Create player with legacy stats
        player = Player(
            player_id=player_id,
            user_id=user_id,
            name=f"LegacyPlayer-{unique_suffix}",
            current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
        )
        # Set legacy stats directly
        player.stats = legacy_stats
        session.add(player)
        await session.commit()

    persistence = PersistenceLayer(db_path=database_url)
    rehydrated_player = persistence.get_player(player_id)

    assert rehydrated_player is not None, "legacy player should load successfully"
    assert rehydrated_player.get_stats()["position"] == "standing", "legacy player should default to standing position"
