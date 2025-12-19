"""Tests for the active lucidity adjustment service."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy import select
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

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture
async def db_session(session_factory):
    async with session_factory() as session:
        yield session


@pytest.fixture
def lucidity_service(db_session):
    return LucidityService(db_session)


@pytest.mark.asyncio
async def test_adjust_lucidity_increases_total(db_session, lucidity_service):
    """Test that adjusting lucidity increases the total properly."""
    # Create test user and player
    user = User(
        id=str(uuid.uuid4()), email="test@example.com", hashed_password="pw", is_active=True, username="testuser"
    )
    db_session.add(user)
    await db_session.flush()

    player = Player(player_id=str(uuid.uuid4()), user_id=user.id, name="TestPlayer")
    db_session.add(player)
    await db_session.flush()

    # Create initial lucidity record
    lucidity = PlayerLucidity(player_id=player.player_id, current_lcd=50, current_tier="uneasy")
    db_session.add(lucidity)
    await db_session.commit()

    # Adjust lucidity
    await lucidity_service.apply_lucidity_adjustment(uuid.UUID(player.player_id), 10, reason_code="test_adj")

    # Verify update
    updated_lucidity = await db_session.get(PlayerLucidity, player.player_id)
    assert updated_lucidity.current_lcd == 60


@pytest.mark.asyncio
async def test_adjust_lucidity_caps_at_max(db_session, lucidity_service):
    """Test that lucidity doesn't exceed 100."""
    player_id = uuid.uuid4()
    lucidity = PlayerLucidity(player_id=str(player_id), current_lcd=95, current_tier="lucid")
    db_session.add(lucidity)
    await db_session.commit()

    await lucidity_service.apply_lucidity_adjustment(player_id, 10, reason_code="test_cap")

    updated_lucidity = await db_session.get(PlayerLucidity, str(player_id))
    assert updated_lucidity.current_lcd == 100


@pytest.mark.asyncio
async def test_adjust_lucidity_caps_at_min(db_session, lucidity_service):
    """Test that lucidity doesn't drop below -100."""
    player_id = uuid.uuid4()
    lucidity = PlayerLucidity(player_id=str(player_id), current_lcd=-95, current_tier="catatonic")
    db_session.add(lucidity)
    await db_session.commit()

    await lucidity_service.apply_lucidity_adjustment(player_id, -10, reason_code="test_floor")

    updated_lucidity = await db_session.get(PlayerLucidity, str(player_id))
    assert updated_lucidity.current_lcd == -100


@pytest.mark.asyncio
async def test_cooldown_management(db_session, lucidity_service):
    """Test that cooldowns can be set and retrieved."""
    player_id = uuid.uuid4()

    # Set a future cooldown
    expiry = datetime.now(UTC) + timedelta(minutes=5)
    await lucidity_service.set_cooldown(player_id, "test_action", expiry)
    await db_session.commit()

    # Retrieve cooldown
    cooldown = await lucidity_service.get_cooldown(player_id, "test_action")
    assert cooldown is not None
    # Compare naive datetimes for PostgreSQL compatibility
    assert cooldown.cooldown_expires_at.replace(tzinfo=None) == expiry.replace(tzinfo=None)


@pytest.mark.asyncio
async def test_adjust_lucidity_logging(db_session, lucidity_service):
    """Test that lucidity adjustments are properly logged in LucidityAdjustmentLog."""
    from server.models.lucidity import LucidityAdjustmentLog

    player_id = uuid.uuid4()
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
