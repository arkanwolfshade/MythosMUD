"""Tests for the active lucidity adjustment service."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import LucidityService


@pytest.fixture
async def session_factory():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL for this test.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # PostgreSQL always enforces foreign keys - no PRAGMA needed
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
            except (SQLAlchemyError, OSError, RuntimeError, ConnectionError) as e:
                # Catch specific database and connection errors
                # If that fails due to foreign key constraints, use CASCADE
                error_msg = str(e).lower()
                if "dependent" not in error_msg and "constraint" not in error_msg:
                    # Re-raise if it's not a foreign key constraint issue
                    raise
                # Fall through to CASCADE drop logic for foreign key constraint errors
            except Exception:  # pylint: disable=broad-exception-caught
                # Catch any other unexpected exceptions (e.g., asyncpg.exceptions.DependentObjectsStillExistError)
                # This is necessary for test teardown to handle all possible database errors gracefully
                pass
            # If drop_all failed, use CASCADE to drop tables individually
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
                except Exception:  # pylint: disable=broad-exception-caught
                    # Ignore errors for tables that don't exist or are already dropped
                    # This is necessary for test teardown robustness
                    pass
    except (SQLAlchemyError, OSError, RuntimeError, ConnectionError, TimeoutError):
        # Catch specific database and connection errors during teardown
        # Ignore teardown errors - test database may be in inconsistent state
        pass
    except Exception:  # pylint: disable=broad-exception-caught
        # Catch any other unexpected exceptions during teardown
        # This is necessary for test teardown to handle all possible errors gracefully
        # Test database may be in inconsistent state, so we ignore all teardown errors
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


@pytest.mark.asyncio
@pytest.mark.serial  # Mark as serial to prevent deadlocks during parallel execution
@pytest.mark.xdist_group(name="serial_lucidity_tests")  # Force serial execution with pytest-xdist
async def test_adjust_lucidity_caps_at_min(db_session, lucidity_service):
    """Test that lucidity doesn't drop below -100."""
    # Create test user and player first (required for foreign key constraint)
    # Use unique username to avoid conflicts with other tests
    unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{unique_username}@example.com",
        hashed_password="pw",
        is_active=True,
        username=unique_username,
    )
    db_session.add(user)
    await db_session.flush()

    player_id = uuid.uuid4()
    # Use unique player name to avoid conflicts in parallel test execution
    unique_player_name = f"TestPlayer_{uuid.uuid4().hex[:8]}"
    player = Player(player_id=str(player_id), user_id=user.id, name=unique_player_name)
    db_session.add(player)
    await db_session.flush()

    lucidity = PlayerLucidity(player_id=str(player_id), current_lcd=-95, current_tier="catatonic")
    db_session.add(lucidity)
    await db_session.commit()

    await lucidity_service.apply_lucidity_adjustment(player_id, -10, reason_code="test_floor")

    updated_lucidity = await db_session.get(PlayerLucidity, str(player_id))
    assert updated_lucidity.current_lcd == -100


@pytest.mark.asyncio
async def test_cooldown_management(db_session, lucidity_service):
    """Test that cooldowns can be set and retrieved."""
    # Create test user and player first (required for foreign key constraint)
    # Use unique username to avoid conflicts with other tests
    unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{unique_username}@example.com",
        hashed_password="pw",
        is_active=True,
        username=unique_username,
    )
    db_session.add(user)
    await db_session.flush()

    player_id = uuid.uuid4()
    # Use unique player name to avoid conflicts in parallel test execution
    unique_player_name = f"TestPlayer_{uuid.uuid4().hex[:8]}"
    player = Player(player_id=str(player_id), user_id=user.id, name=unique_player_name)
    db_session.add(player)
    await db_session.flush()

    # Set a future cooldown - use naive datetime for PostgreSQL compatibility
    expiry = datetime.now(UTC).replace(tzinfo=None) + timedelta(minutes=5)
    await lucidity_service.set_cooldown(player_id, "test_action", expiry)
    await db_session.commit()

    # Retrieve cooldown
    cooldown = await lucidity_service.get_cooldown(player_id, "test_action")
    assert cooldown is not None
    # Compare naive datetimes for PostgreSQL compatibility
    assert cooldown.cooldown_expires_at.replace(tzinfo=None) == expiry.replace(tzinfo=None)


@pytest.mark.asyncio
@pytest.mark.serial  # Mark as serial to prevent deadlocks during parallel execution
@pytest.mark.xdist_group(name="serial_lucidity_tests")  # Force serial execution with pytest-xdist
async def test_adjust_lucidity_logging(db_session, lucidity_service):
    """Test that lucidity adjustments are properly logged in LucidityAdjustmentLog."""
    from server.models.lucidity import LucidityAdjustmentLog

    # Create test user and player first (required for foreign key constraint)
    # Use unique username to avoid conflicts with other tests
    unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
    user = User(
        id=str(uuid.uuid4()),
        email=f"{unique_username}@example.com",
        hashed_password="pw",
        is_active=True,
        username=unique_username,
    )
    db_session.add(user)
    await db_session.flush()

    player_id = uuid.uuid4()
    # Use unique player name to avoid conflicts in parallel test execution
    unique_player_name = f"TestPlayer_{uuid.uuid4().hex[:8]}"
    player = Player(player_id=str(player_id), user_id=user.id, name=unique_player_name)
    db_session.add(player)
    await db_session.flush()

    lucidity = PlayerLucidity(player_id=str(player_id), current_lcd=50, current_tier="uneasy")
    db_session.add(lucidity)
    await db_session.commit()

    reason = "test_logging"
    await lucidity_service.apply_lucidity_adjustment(player_id, 15, reason_code=reason)

    # Check logs
    result = await db_session.execute(
        select(LucidityAdjustmentLog).where(LucidityAdjustmentLog.player_id == str(player_id))
    )
    logs = result.scalars().all()

    assert len(logs) == 1
    assert logs[0].delta == 15
    assert logs[0].reason_code == reason
