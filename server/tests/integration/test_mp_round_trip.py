"""
Integration test for MP on the player registry (ADR-029 step 6b), against real PostgreSQL.

A PlayerMpService change commits before the call returns, writing only ``magic_points`` (and removing the old
``_mp_fractional``). A legacy full-row save of a copy loaded before the change (``upsert_player``) can no longer write
the old MP back.
"""

import uuid
from typing import cast

import pytest
import structlog
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.persistence.repositories.player_repository_save import PlayerSavePreparer
from server.services.player_mp_service import PlayerMpService
from server.tests.fixtures.integration.players import create_test_player, delete_test_user

STATS: dict[str, object] = {"current_dp": 20, "max_dp": 20, "magic_points": 5, "max_magic_points": 10}


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id; deleting it afterwards cascades to the player."""
    user_id = uuid.uuid4()
    yield user_id
    await delete_test_user(session_factory, user_id)


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


async def _stats(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID) -> dict[str, object]:
    async with session_factory() as session:
        row = (
            await session.execute(text("SELECT stats FROM players WHERE player_id = :id"), {"id": str(player_id)})
        ).one()
    return cast(dict[str, object], row[0])


@pytest.mark.asyncio
async def test_mp_round_trip(session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID):
    player_id = await create_test_player(session_factory, cleanup_test_user, stats={**STATS, "_mp_fractional": 0.4})
    registry = _registry(session_factory)

    _ = await PlayerMpService(registry).spend(player_id, 3)

    assert not registry.is_loaded(player_id)  # sync: committed, nothing left to sweep
    assert await _stats(session_factory, player_id) == {**STATS, "magic_points": 2}  # the old fraction is gone

    _ = await PlayerMpService(registry).restore(player_id, 50)
    assert (await _stats(session_factory, player_id))["magic_points"] == 10


@pytest.mark.asyncio
async def test_a_drain_moves_mp_between_two_players(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    """Power Drain's write: one transaction across both players' rows."""
    other_user = uuid.uuid4()
    target = await create_test_player(session_factory, cleanup_test_user, stats=dict(STATS))
    caster = await create_test_player(session_factory, other_user, stats=dict(STATS))
    try:
        lost, received = await PlayerMpService(_registry(session_factory)).drain(target, caster, 4)

        assert (lost.new_mp, received.new_mp) == (1, 9)
        assert (await _stats(session_factory, target))["magic_points"] == 1
        assert (await _stats(session_factory, caster))["magic_points"] == 9
    finally:
        await delete_test_user(session_factory, other_user)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_stale_full_row_save_keeps_the_stored_mp(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    """upsert_player of a Player loaded before an MP change keeps the new MP; its other stats land."""
    player_id = await create_test_player(session_factory, cleanup_test_user, stats=dict(STATS))
    stale = await AsyncPersistenceLayer(_skip_room_cache=True).get_player_by_id(player_id)
    assert stale is not None

    _ = await PlayerMpService(_registry(session_factory)).spend(player_id, 3)

    stats = stale.get_stats()
    stats["magic_points"] = 9  # the stale copy's own MP: a write that bypassed the registry
    stats["luck"] = 7  # a stat the registry does not own yet still lands
    stale.set_stats(stats)
    preparer = PlayerSavePreparer(structlog.get_logger())
    async with session_factory() as session:
        await preparer.execute(session, preparer.prepare(stale))
        await session.commit()

    after = await _stats(session_factory, player_id)
    assert after["magic_points"] == 2
    assert after["luck"] == 7
