"""Tests for the lucidity service adjustment and liability logic."""

from __future__ import annotations

import uuid
from datetime import datetime

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import (
    LucidityService,
    decode_liabilities,
    resolve_tier,
)


@pytest.fixture
async def session_factory():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL for this test.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    yield session_maker

    # Clean up tables after tests
    # Handle foreign key dependencies by dropping with CASCADE
    try:
        async with engine.begin() as conn:
            from sqlalchemy import text

            try:
                # Try normal drop_all first
                await conn.run_sync(Base.metadata.drop_all)
            except (SQLAlchemyError, OSError, RuntimeError, ConnectionError, TimeoutError):
                # If that fails due to foreign key constraints or connection issues, use CASCADE
                # Get all table names and drop them with CASCADE
                result = await conn.execute(
                    text(
                        """
                    SELECT tablename FROM pg_tables
                    WHERE schemaname = 'public'
                    """
                    )
                )
                tables = [row[0] for row in result.fetchall()]
                for table in tables:
                    try:
                        await conn.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE'))
                    except (SQLAlchemyError, OSError, RuntimeError, ConnectionError, TimeoutError):
                        # Ignore errors for tables that don't exist or are already dropped
                        pass
                    except Exception:  # pylint: disable=broad-exception-caught
                        # Catch any other unexpected exceptions during individual table drops
                        # (e.g., from mocks or asyncpg specifics) to ensure robust test teardown
                        pass
            except Exception:  # pylint: disable=broad-exception-caught
                # Catch any other unexpected exceptions during drop_all (e.g., from mocks or asyncpg specifics)
                # This ensures robust test teardown even in inconsistent database states
                pass
    except (SQLAlchemyError, OSError, RuntimeError, ConnectionError, TimeoutError):
        # Ignore teardown errors - test database may be in inconsistent state
        pass
    except Exception:  # pylint: disable=broad-exception-caught
        # Catch any other unexpected exceptions during teardown (e.g., from mocks or asyncpg specifics)
        # This ensures robust test teardown even in inconsistent database states
        pass
    finally:
        await engine.dispose()


@pytest.fixture
async def db_session(session_factory):
    async with session_factory() as session:
        yield session


@pytest.fixture
def lucidity_service(db_session):
    return LucidityService(db_session)


def test_decode_liabilities():
    """Test liability JSON decoding into structured list."""
    # None/Empty = no liabilities
    assert decode_liabilities(None) == []
    assert decode_liabilities("") == []

    # Valid JSON list of liability objects
    payload = '[{"code": "night_frayed_reflexes", "stacks": 2}]'
    decoded = decode_liabilities(payload)
    assert len(decoded) == 1
    assert decoded[0]["code"] == "night_frayed_reflexes"
    assert decoded[0]["stacks"] == 2

    # Malformed JSON
    assert decode_liabilities("invalid-json") == []


def test_resolve_tier():
    """Test lucidity tier label derivation based on LCD thresholds."""
    assert resolve_tier(100) == "lucid"
    assert resolve_tier(70) == "lucid"
    assert resolve_tier(69) == "uneasy"
    assert resolve_tier(40) == "uneasy"
    assert resolve_tier(39) == "fractured"
    assert resolve_tier(20) == "fractured"
    assert resolve_tier(19) == "deranged"
    assert resolve_tier(1) == "deranged"
    assert resolve_tier(0) == "catatonic"
    assert resolve_tier(-10) == "catatonic"


@pytest.mark.asyncio
@pytest.mark.serial  # Mark as serial to prevent deadlocks during parallel execution
async def test_get_player_lucidity_state(db_session, lucidity_service):
    """Test retrieving full lucidity record for a player."""
    # Create User first (required for Player foreign key)
    user_id = uuid.uuid4()
    user = User(
        id=user_id,
        username=f"testuser_{user_id.hex[:8]}",
        email=f"test_{user_id.hex[:8]}@test.example.com",
        hashed_password="test_password_hash",
        is_active=True,
        is_superuser=False,
        is_verified=True,
        display_name=f"testuser_{user_id.hex[:8]}",
        is_admin=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db_session.add(user)
    await db_session.flush()

    # Create Player (required for PlayerLucidity foreign key)
    player_id = uuid.uuid4()
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name=f"TestPlayer_{player_id.hex[:8]}",
        current_room_id="limbo_death_void_limbo_death_void",
        experience_points=0,
        level=1,
        is_admin=0,
        profession_id=1,
        created_at=datetime.now(),
        last_active=datetime.now(),
        stats={"current_dp": 100, "max_dp": 100},
        status_effects="[]",
        inventory="[]",
    )
    db_session.add(player)
    await db_session.flush()

    # 65 lucidity = uneasy tier
    # liabilities stored as JSON string
    liabilities_json = '[{"code": "night_frayed_reflexes", "stacks": 1}]'
    db_session.add(
        PlayerLucidity(player_id=player_id, current_lcd=65, liabilities=liabilities_json, current_tier="uneasy")
    )
    await db_session.commit()

    record = await lucidity_service.get_player_lucidity(player_id)

    assert record.current_lcd == 65
    assert record.current_tier == "uneasy"
    decoded = decode_liabilities(record.liabilities)
    assert len(decoded) == 1
    assert decoded[0]["code"] == "night_frayed_reflexes"


@pytest.mark.asyncio
async def test_catatonic_state_enforced(db_session, lucidity_service):
    """Test that catatonic state is correctly reflected in the record."""
    # Create User first (required for Player foreign key)
    user_id = uuid.uuid4()
    user = User(
        id=user_id,
        username=f"testuser_{user_id.hex[:8]}",
        email=f"test_{user_id.hex[:8]}@test.example.com",
        hashed_password="test_password_hash",
        is_active=True,
        is_superuser=False,
        is_verified=True,
        display_name=f"testuser_{user_id.hex[:8]}",
        is_admin=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db_session.add(user)
    await db_session.flush()

    # Create Player (required for PlayerLucidity foreign key)
    player_id = uuid.uuid4()
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name=f"TestPlayer_{player_id.hex[:8]}",
        current_room_id="limbo_death_void_limbo_death_void",
        experience_points=0,
        level=1,
        is_admin=0,
        profession_id=1,
        created_at=datetime.now(),
        last_active=datetime.now(),
        stats={"current_dp": 100, "max_dp": 100},
        status_effects="[]",
        inventory="[]",
    )
    db_session.add(player)
    await db_session.flush()

    # Entered at timestamp indicates active catatonia
    from datetime import UTC

    entered_at = datetime.now(UTC).replace(tzinfo=None)
    db_session.add(
        PlayerLucidity(player_id=player_id, current_lcd=0, current_tier="catatonic", catatonia_entered_at=entered_at)
    )
    await db_session.commit()

    record = await lucidity_service.get_player_lucidity(player_id)

    assert record.current_lcd == 0
    assert record.current_tier == "catatonic"
    # Compare datetimes ignoring timezone (database may return with or without tzinfo)
    assert record.catatonia_entered_at is not None
    assert record.catatonia_entered_at.replace(tzinfo=None) == entered_at.replace(tzinfo=None)
