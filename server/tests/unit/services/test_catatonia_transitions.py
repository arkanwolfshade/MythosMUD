"""Tests for catatonia transitions within the lucidity service."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import PlayerLucidity
from server.models.player import Player
from server.models.user import User
from server.services.lucidity_service import LucidityService


@pytest.fixture(name="session_factory")
async def _session_factory():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL for this test.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    yield session_maker

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest.fixture(name="db_session")
async def _db_session(session_factory):
    async with session_factory() as session:
        yield session


@pytest.fixture(name="lucidity_service")
def _lucidity_service(db_session):
    return LucidityService(db_session)


@pytest.mark.asyncio
async def test_lucidity_drop_to_zero_triggers_catatonia(db_session, lucidity_service):
    """Test that dropping lucidity to zero sets the catatonic tier and timestamp."""
    # Create test user and player
    user = User(
        id=str(uuid.uuid4()), email="catatonia@example.com", hashed_password="pw", is_active=True, username="testuser"
    )
    db_session.add(user)
    await db_session.flush()

    player = Player(player_id=str(uuid.uuid4()), user_id=user.id, name="CatatonicPlayer")
    db_session.add(player)
    await db_session.flush()

    # Create initial lucidity record (not catatonic)
    lucidity = PlayerLucidity(player_id=player.player_id, current_lcd=5, current_tier="deranged")
    db_session.add(lucidity)
    await db_session.commit()

    # Adjust lucidity to zero
    await lucidity_service.apply_lucidity_adjustment(uuid.UUID(player.player_id), -5, reason_code="test_catatonia")

    # Verify catatonic state
    updated_lucidity = await db_session.get(PlayerLucidity, player.player_id)
    assert updated_lucidity.current_lcd == 0
    assert updated_lucidity.current_tier == "catatonic"
    assert updated_lucidity.catatonia_entered_at is not None


@pytest.mark.asyncio
async def test_lucidity_recovery_clears_catatonia(db_session, lucidity_service):
    """Test that recovering lucidity from zero clears the catatonic flag."""
    # Create test user and player
    user = User(
        id=str(uuid.uuid4()),
        email="recovery@example.com",
        hashed_password="pw",
        is_active=True,
        username="recoveryuser",
    )
    db_session.add(user)
    await db_session.flush()

    player = Player(player_id=str(uuid.uuid4()), user_id=user.id, name="RecoveryPlayer")
    db_session.add(player)
    await db_session.flush()

    # Start as catatonic at 0
    entered_at = datetime.now(UTC).replace(tzinfo=None)
    lucidity = PlayerLucidity(
        player_id=player.player_id, current_lcd=0, current_tier="catatonic", catatonia_entered_at=entered_at
    )
    db_session.add(lucidity)
    await db_session.commit()

    # Adjust lucidity upwards
    await lucidity_service.apply_lucidity_adjustment(uuid.UUID(player.player_id), 1, reason_code="recovery")

    # Verify catatonic state cleared
    updated_lucidity = await db_session.get(PlayerLucidity, player.player_id)
    assert updated_lucidity.current_lcd == 1
    assert updated_lucidity.current_tier == "deranged"
    assert updated_lucidity.catatonia_entered_at is None
