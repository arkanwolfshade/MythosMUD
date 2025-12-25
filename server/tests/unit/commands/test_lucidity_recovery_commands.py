"""Tests for lucidity recovery command handlers."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from types import SimpleNamespace

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.commands.lucidity_recovery_commands import handle_pray_command
from server.models.base import Base
from server.models.lucidity import LucidityCooldown, PlayerLucidity
from server.models.player import Player
from server.models.user import User


@pytest.fixture
async def session_factory():
    import os

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
    engine = create_async_engine(database_url, future=True)
    async with engine.begin() as conn:
        # PostgreSQL always enforces foreign keys - no PRAGMA needed
        await conn.run_sync(Base.metadata.create_all)
    maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    try:
        yield maker
    finally:
        await engine.dispose()


async def _create_player(session: AsyncSession, *, player_name: str, room_id: str, LCD: int = 50) -> Player:
    # Use unique identifiers to avoid IntegrityError in parallel test runs
    unique_suffix = uuid.uuid4().hex[:8]
    unique_username = f"{player_name}_{unique_suffix}"
    unique_email = f"{player_name}_{unique_suffix}@example.com"
    unique_player_name = f"{player_name}_{unique_suffix}"

    user = User(
        id=str(uuid.uuid4()),
        email=unique_email,
        username=unique_username,
        display_name=unique_username,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=str(uuid.uuid4()),
        user_id=user.id,
        name=unique_player_name,
        current_room_id=room_id,
    )
    session.add_all([user, player])
    await session.flush()  # Flush to get player_id available for foreign key
    # Create PlayerLucidity - player_id is stored as string UUID in DB (UUID(as_uuid=False))
    # The service queries using uuid.UUID object, and SQLAlchemy handles the string/UUID conversion
    # Ensure we use the player_id string directly (it's already a string from uuid.uuid4())
    player_lucidity = PlayerLucidity(
        player_id=player.player_id,  # String UUID - SQLAlchemy will convert when querying
        current_lcd=LCD,
        current_tier="lucid" if LCD >= 70 else "uneasy",
    )
    session.add(player_lucidity)
    await session.commit()
    return player


class FakePersistence:
    """Minimal in-memory persistence stub for command tests."""

    def __init__(self, player):
        self._player = player

    def get_player_by_name(self, name: str):
        if name == self._player.name:
            return self._player
        return None


def _build_request(persistence) -> SimpleNamespace:
    return SimpleNamespace(app=SimpleNamespace(state=SimpleNamespace(persistence=persistence)))


@pytest.mark.asyncio
@pytest.mark.serial  # Worker crash in parallel execution - likely due to database session isolation issues
async def test_pray_command_success(session_factory, monkeypatch):
    async with session_factory() as session:
        player = await _create_player(
            session, player_name="arkham_scholar", room_id="earth_arkhamcity_LCDctuary_room_core_001", LCD=42
        )

    async def session_gen():
        async with session_factory() as session:
            yield session

    monkeypatch.setattr(
        "server.commands.lucidity_recovery_commands.get_async_session",
        lambda: session_gen(),
    )

    persistence = FakePersistence(player)
    request = _build_request(persistence)
    current_user = {"username": player.name}

    response = await handle_pray_command({}, current_user, request, None, player.name)
    assert "Stability shifts" in response["result"]

    async with session_factory() as session:
        lucidity = await session.get(PlayerLucidity, player.player_id)
        assert lucidity is not None
        assert lucidity.current_lcd == 50
        cooldown = (
            await session.execute(
                select(LucidityCooldown).where(
                    LucidityCooldown.player_id == player.player_id, LucidityCooldown.action_code == "pray"
                )
            )
        ).scalar_one()
        expiry = cooldown.cooldown_expires_at
        assert expiry is not None
        expiry_dt = expiry.replace(tzinfo=UTC)
        remaining = (expiry_dt - datetime.now(UTC)).total_seconds() / 60
        assert 10 <= remaining <= 16


@pytest.mark.asyncio
async def test_pray_command_respects_cooldown(session_factory, monkeypatch):
    async with session_factory() as session:
        player = await _create_player(
            session, player_name="arkham_scholar", room_id="earth_arkhamcity_LCDctuary_room_core_001", LCD=30
        )

    async def session_gen():
        async with session_factory() as session:
            yield session

    monkeypatch.setattr(
        "server.commands.lucidity_recovery_commands.get_async_session",
        lambda: session_gen(),
    )

    persistence = FakePersistence(player)
    request = _build_request(persistence)
    current_user = {"username": player.name}

    await handle_pray_command({}, current_user, request, None, player.name)

    # Invoke again during cooldown
    cooldown_response = await handle_pray_command({}, current_user, request, None, player.name)
    assert "cooling" in cooldown_response["result"] or "resonating" in cooldown_response["result"]
