"""
Integration tests: fear, occult knowledge and admin-set stats are written by the registry (ADR-029 step 8c).

They used to be an atomic SQL update (``update_player_stat_field``) and a whole-row ``save_player``. Against a real
database these pin that the registry's units reach the stored ``stats``, and that a ``save_player`` of a copy loaded
before a fear or occult change cannot write the old value back.
"""

import uuid
from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.container.bundles.combat import make_stat_adjuster
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory


@pytest.fixture
async def player_row(session_factory: async_sessionmaker[AsyncSession]):
    """Create a user and a player row with the schema's default stats. Yields player_id."""
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    username = f"stat_test_{uuid.uuid4().hex[:8]}"
    async with session_factory() as session:
        _ = await session.execute(
            text(
                "INSERT INTO users (id, username, display_name, email, hashed_password, is_active) "
                + "VALUES (:id, :username, :username, :email, 'hashed', true)"
            ),
            {"id": user_id, "username": username, "email": f"{username}@example.com"},
        )
        _ = await session.execute(
            text("INSERT INTO players (player_id, user_id, name) VALUES (:player_id, :user_id, :name)"),
            {"player_id": player_id, "user_id": user_id, "name": username},
        )
        await session.commit()
    yield player_id
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": user_id})
        await session.commit()


async def _stat(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID, key: str) -> object:
    """One ``stats`` key as stored, or None."""
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT stats -> :key FROM players WHERE player_id = :id"), {"key": key, "id": str(player_id)}
            )
        ).one()
    return cast(object, row[0])


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    """No idle TTL, so every unit loads the player fresh from the database."""
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


@pytest.mark.asyncio
async def test_fear_and_occult_knowledge_add_up_in_the_database(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    adjust = make_stat_adjuster(_registry(session_factory))

    await adjust(player_row, "fear", 3, "test")
    await adjust(player_row, "fear", 2, "test")
    await adjust(player_row, "occult_knowledge", 7, "test")

    assert await _stat(session_factory, player_row, "fear") == 5
    assert await _stat(session_factory, player_row, "occult_knowledge") == 7


@pytest.mark.asyncio
async def test_a_single_stat_unit_writes_only_its_key(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID
) -> None:
    """What admin set stat now does for a generic stat: one ``stats`` key, merged, nothing else touched."""
    registry = _registry(session_factory)
    dp_before = await _stat(session_factory, player_row, "current_dp")

    async with registry.mutate(player_row, sync=True) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
        player.row.set_stat("strength", 77, sync=True)

    assert await _stat(session_factory, player_row, "strength") == 77
    assert await _stat(session_factory, player_row, "current_dp") == dp_before


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
@pytest.mark.parametrize("key", ["fear", "occult_knowledge"])
async def test_a_save_of_a_copy_loaded_before_the_change_keeps_it(
    session_factory: async_sessionmaker[AsyncSession], player_row: uuid.UUID, key: str
) -> None:
    """upsert_player used to write the loaded copy's value back: now only the registry writes fear and occult."""
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    stale_copy = await persistence.get_player_by_id(player_row)  # loaded before the change
    assert stale_copy is not None

    await make_stat_adjuster(_registry(session_factory))(player_row, key, 4, "test")
    await persistence.save_player(stale_copy)

    assert await _stat(session_factory, player_row, key) == 4
