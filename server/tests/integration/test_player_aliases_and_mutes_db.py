"""
Integration tests for DB-backed player aliases (#680) and mutes (#681).

Drives AliasStorage / PlayerMuteRepository / UserManager against mythos_unit through the real
procedures in db/procedures/player_aliases.sql and player_mutes.sql.
"""

import uuid
from collections.abc import AsyncGenerator
from dataclasses import dataclass, replace
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.alias_storage import MAX_ALIASES_PER_PLAYER, AliasStorage
from server.persistence.repositories.player_mute_repository import PlayerMute, PlayerMuteRepository
from server.services.user_manager import UserManager


@dataclass(frozen=True)
class _Players:
    muter_id: uuid.UUID
    muter_name: str
    target_id: uuid.UUID
    target_name: str


@pytest.fixture
async def players(
    session_factory: async_sessionmaker[AsyncSession], monkeypatch: pytest.MonkeyPatch
) -> AsyncGenerator[_Players, None]:
    """Two fresh players; storage classes are pointed at the integration session factory."""
    monkeypatch.setattr("server.alias_storage.get_session_maker", lambda: session_factory)
    monkeypatch.setattr(
        "server.persistence.repositories.player_mute_repository.get_session_maker", lambda: session_factory
    )
    suffix = uuid.uuid4().hex[:8]
    user_id = uuid.uuid4()
    p = _Players(uuid.uuid4(), f"Muter{suffix}", uuid.uuid4(), f"Target{suffix}")
    async with session_factory() as session:
        _ = await session.execute(
            text(
                """
                INSERT INTO users (id, email, username, display_name, hashed_password,
                                   is_active, is_superuser, is_verified, created_at, updated_at)
                VALUES (:id, :email, :username, :username, 'x', true, false, true, now(), now())
                """
            ),
            {"id": user_id, "email": f"{suffix}@alias-mute.test", "username": f"am{suffix}"},
        )
        for player_id, name in ((p.muter_id, p.muter_name), (p.target_id, p.target_name)):
            _ = await session.execute(
                text("INSERT INTO players (player_id, user_id, name) VALUES (:pid, :uid, :name)"),
                {"pid": player_id, "uid": user_id, "name": name},
            )
        await session.commit()
    yield p
    async with session_factory() as session:
        # users -> players -> player_aliases / player_mutes all cascade
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_id})
        await session.commit()


@pytest.mark.asyncio
async def test_alias_crud_round_trip(players: _Players) -> None:
    storage = AliasStorage()
    name = players.muter_name

    created = await storage.create_alias(name, "sit", "/sit")
    assert created is not None
    assert created.command == "/sit"

    # Case-insensitive player and alias names; re-creating replaces the command in place
    replaced = await storage.create_alias(name.upper(), "SIT", "/sit down")
    assert replaced is not None
    assert replaced.id == created.id

    aliases = await storage.get_player_aliases(name.lower())
    assert [(a.name, a.command) for a in aliases] == [("SIT", "/sit down")]
    fetched = await storage.get_alias(name, "sIt")
    assert fetched is not None
    assert fetched.command == "/sit down"

    assert await storage.remove_alias(name, "sit") is True
    assert await storage.remove_alias(name, "sit") is False
    assert await storage.get_alias(name, "sit") is None


@pytest.mark.asyncio
async def test_aliases_are_per_player_and_deleted_by_id(players: _Players) -> None:
    storage = AliasStorage()
    assert await storage.create_alias(players.muter_name, "go", "north") is not None

    assert await storage.get_player_aliases(players.target_name) == []
    assert await storage.delete_player_aliases_by_id(str(players.muter_id)) is True
    assert await storage.get_player_aliases(players.muter_name) == []


@pytest.mark.asyncio
async def test_alias_rejected_for_unknown_player_and_over_limit(players: _Players) -> None:
    storage = AliasStorage()
    assert await storage.create_alias(f"Nobody{uuid.uuid4().hex[:6]}", "x", "look") is None

    for i in range(MAX_ALIASES_PER_PLAYER):
        assert await storage.create_alias(players.muter_name, f"a{i}", "look") is not None
    assert await storage.create_alias(players.muter_name, "overflow", "look") is None


@pytest.mark.asyncio
async def test_mute_repository_upsert_replaces_and_filters_expired(players: _Players) -> None:
    repo = PlayerMuteRepository()
    now = datetime.now(UTC)
    base = PlayerMute(
        mute_type="player",
        muter_id=players.muter_id,
        muter_name=players.muter_name,
        target_id=players.target_id,
        target_name=players.target_name,
        channel=None,
        reason="spam",
        muted_at=now,
        expires_at=None,
    )
    await repo.upsert(base)
    await repo.upsert(replace(base, reason="again", expires_at=now + timedelta(minutes=5)))
    await repo.upsert(
        replace(base, mute_type="global", muted_at=now - timedelta(minutes=10), expires_at=now - timedelta(minutes=1))
    )

    mine = [m for m in await repo.load_active() if m.muter_id == players.muter_id]
    assert [(m.mute_type, m.reason) for m in mine] == [("player", "again")]

    assert await repo.delete("player", players.muter_id, players.target_id, None) is True
    assert await repo.delete("player", players.muter_id, players.target_id, None) is False


@pytest.mark.asyncio
async def test_global_mute_survives_restart_without_muter_online(players: _Players) -> None:
    """Regression: global mutes used to live in the muter's JSON file and vanished unless it was loaded."""
    first = UserManager()
    assert await first.mute_global(
        players.muter_id, players.muter_name, players.target_id, players.target_name, 30, "spam"
    )
    assert await first.mute_player(players.muter_id, players.muter_name, players.target_id, players.target_name)
    assert await first.mute_channel(players.muter_id, players.muter_name, "ooc")

    restarted = UserManager()
    _ = await restarted.load_all_mutes()
    assert restarted.is_globally_muted(players.target_id)
    assert restarted.is_player_muted(players.muter_id, players.target_id)
    assert restarted.is_channel_muted(players.muter_id, "ooc")

    assert await restarted.unmute_global(players.muter_id, players.muter_name, players.target_id, players.target_name)
    after_unmute = UserManager()
    _ = await after_unmute.load_all_mutes()
    assert not after_unmute.is_globally_muted(players.target_id)
    assert after_unmute.is_player_muted(players.muter_id, players.target_id)
