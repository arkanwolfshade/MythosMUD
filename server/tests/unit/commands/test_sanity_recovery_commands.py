"""Tests for sanity recovery command handlers."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from types import SimpleNamespace

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from server.commands.sanity_recovery_commands import handle_pray_command
from server.models.base import Base
from server.models.player import Player
from server.models.sanity import PlayerSanity, SanityCooldown
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


async def _create_player(session: AsyncSession, *, player_name: str, room_id: str, san: int = 50) -> Player:
    user = User(
        id=str(uuid.uuid4()),
        email=f"{player_name}@example.com",
        username=player_name,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    player = Player(
        player_id=f"player-{uuid.uuid4()}",
        user_id=user.id,
        name=player_name,
        current_room_id=room_id,
    )
    session.add_all([user, player])
    session.add(
        PlayerSanity(
            player_id=player.player_id,
            current_san=san,
            current_tier="lucid" if san >= 70 else "uneasy",
        )
    )
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
async def test_pray_command_success(session_factory, monkeypatch):
    async with session_factory() as session:
        player = await _create_player(
            session, player_name="arkham_scholar", room_id="earth_arkhamcity_sanctuary_room_core_001", san=42
        )

    async def session_gen():
        async with session_factory() as session:
            yield session

    monkeypatch.setattr(
        "server.commands.sanity_recovery_commands.get_async_session",
        lambda: session_gen(),
    )

    persistence = FakePersistence(player)
    request = _build_request(persistence)
    current_user = {"username": player.name}

    response = await handle_pray_command({}, current_user, request, None, player.name)
    assert "Stability shifts" in response["result"]

    async with session_factory() as session:
        sanity = await session.get(PlayerSanity, player.player_id)
        assert sanity is not None
        assert sanity.current_san == 50
        cooldown = (
            await session.execute(
                select(SanityCooldown).where(
                    SanityCooldown.player_id == player.player_id, SanityCooldown.action_code == "pray"
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
            session, player_name="arkham_scholar", room_id="earth_arkhamcity_sanctuary_room_core_001", san=30
        )

    async def session_gen():
        async with session_factory() as session:
            yield session

    monkeypatch.setattr(
        "server.commands.sanity_recovery_commands.get_async_session",
        lambda: session_gen(),
    )

    persistence = FakePersistence(player)
    request = _build_request(persistence)
    current_user = {"username": player.name}

    await handle_pray_command({}, current_user, request, None, player.name)

    # Invoke again during cooldown
    cooldown_response = await handle_pray_command({}, current_user, request, None, player.name)
    assert "cooling" in cooldown_response["result"] or "resonating" in cooldown_response["result"]
