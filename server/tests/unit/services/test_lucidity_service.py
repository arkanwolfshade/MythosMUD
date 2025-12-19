"""Tests for the lucidity service adjustment and liability logic."""

from __future__ import annotations

import uuid

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.models.base import Base
from server.models.lucidity import PlayerLucidity
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
async def test_get_player_lucidity_state(db_session, lucidity_service):
    """Test retrieving full lucidity record for a player."""
    player_id = uuid.uuid4()
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
    player_id = uuid.uuid4()
    # Entered at timestamp indicates active catatonia
    from datetime import UTC, datetime

    entered_at = datetime.now(UTC).replace(tzinfo=None)
    db_session.add(
        PlayerLucidity(player_id=player_id, current_lcd=0, current_tier="catatonic", catatonia_entered_at=entered_at)
    )
    await db_session.commit()

    record = await lucidity_service.get_player_lucidity(player_id)

    assert record.current_lcd == 0
    assert record.current_tier == "catatonic"
    assert record.catatonia_entered_at == entered_at
