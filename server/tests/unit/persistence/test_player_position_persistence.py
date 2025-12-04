"""Tests verifying player position persistence across login/logout cycles."""

from __future__ import annotations

import json
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


async def initialize_database(session: AsyncSession, user_id: str | None = None) -> str:
    """Create required schema and seed data in PostgreSQL.

    Returns:
        The UUID of the created user (as string)
    """
    import uuid

    # Generate a proper UUID for user_id if not provided
    if user_id is None:
        user_uuid = uuid.uuid4()
    else:
        # If user_id is provided, try to use it as UUID, or generate new one
        try:
            user_uuid = uuid.UUID(user_id)
        except (ValueError, AttributeError):
            # If it's not a valid UUID, generate a new one
            user_uuid = uuid.uuid4()

    unique_suffix = str(user_uuid)[:8]

    # Create user with unique email and username
    user = User(
        id=str(user_uuid),
        email=f"position_test_{unique_suffix}@example.com",
        username=f"position_test_user_{unique_suffix}",
        display_name=f"position_test_user_{unique_suffix}",
        hashed_password="hashed-password",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    session.add(user)
    await session.commit()
    return str(user_uuid)


def build_player(player_id: str, user_id: str, name: str | None = None) -> Player:
    """Create a Player instance with timestamps normalized for persistence tests."""
    import json
    import uuid

    # Use unique name based on player_id if not provided
    # Player.name has unique constraint, so we need to ensure uniqueness
    if name is None:
        # Use a combination of player_id and a short UUID to ensure uniqueness
        unique_part = player_id.replace("-", "")[-12:] if len(player_id) > 12 else player_id
        name = f"PositionTester-{unique_part}-{str(uuid.uuid4())[:8]}"

    player = Player(
        player_id=player_id,
        user_id=user_id,
        name=name,
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
        status_effects=json.dumps([]),  # Ensure status_effects is set (not null)
        experience_points=0,  # Ensure experience_points is set (not null)
        level=1,  # Ensure level is set (not null)
        is_admin=0,  # Ensure is_admin is set (not null)
        profession_id=0,  # Ensure profession_id is set (not null)
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


@pytest.mark.slow
@pytest.mark.asyncio
async def test_position_persists_across_logout_login_cycle(async_session_factory):
    """Verify that player position changes persist after saving and reloading."""

    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    async with async_session_factory() as session:
        user_id = await initialize_database(session)
        await session.commit()

    persistence = PersistenceLayer(db_path=database_url)

    # Use proper UUID format for player_id (PostgreSQL requires valid UUID)
    import uuid as uuid_module

    player_id = uuid_module.uuid4()  # UUID object, not string
    player = build_player(str(player_id), user_id)  # build_player expects string

    # Initial save representing the player's first login.
    persistence.save_player(player)

    # Load the player (simulating a login) and confirm standing.
    # get_player expects UUID object
    loaded_player = persistence.get_player(player_id)
    assert loaded_player is not None, "player should load successfully after initial save"
    assert loaded_player.get_stats()["position"] == "standing"

    # Change position to sitting and persist (simulating logout).
    updated_stats = loaded_player.get_stats()
    updated_stats["position"] = "sitting"
    loaded_player.set_stats(updated_stats)
    persistence.save_player(loaded_player)

    # Reload and ensure the sitting posture persisted.
    # get_player expects UUID object
    reloaded_player = persistence.get_player(player_id)
    assert reloaded_player is not None, "player should load successfully after updating position"
    assert reloaded_player.get_stats()["position"] == "sitting"


@pytest.mark.slow
@pytest.mark.asyncio
async def test_missing_position_defaults_to_standing_on_load(async_session_factory):
    """Players with legacy stats lacking position should default to standing."""
    import uuid

    database_url = get_database_url()
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

    # Generate unique identifiers to avoid constraint violations on repeated test runs
    unique_suffix = str(uuid.uuid4())[:8]

    async with async_session_factory() as session:
        user_id = await initialize_database(session)

        # Insert legacy stats without a position field using PostgreSQL syntax
        legacy_stats_json = (
            '{"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, '
            '"wisdom": 10, "charisma": 10, "lucidity": 100, "occult_knowledge": 0, '
            '"fear": 0, "corruption": 0, "cult_affiliation": 0, "current_health": 100}'
        )
        # Parse JSON string to dict - MutableDict.as_mutable(JSONB) requires dict, not string
        legacy_stats = json.loads(legacy_stats_json)

        # Use proper UUID format for player_id
        import uuid as uuid_module

        player_id = uuid_module.uuid4()  # UUID object, not string
        # Create player with legacy stats
        # Player model expects string for player_id (UUID(as_uuid=False))
        player = Player(
            player_id=str(player_id),
            user_id=user_id,
            name=f"LegacyPlayer-{unique_suffix}",
            current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
        )
        # Set legacy stats directly
        # Testing legacy behavior where stats is assigned as dict (parsed from JSON string)
        # SQLAlchemy JSONB column with MutableDict requires dict at runtime
        player.stats = legacy_stats
        session.add(player)
        await session.commit()

    persistence = PersistenceLayer(db_path=database_url)
    # get_player expects UUID object
    rehydrated_player = persistence.get_player(player_id)

    assert rehydrated_player is not None, "legacy player should load successfully"
    assert rehydrated_player.get_stats()["position"] == "standing", "legacy player should default to standing position"
