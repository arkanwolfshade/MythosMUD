"""
Integration test for DP on the player registry (ADR-029 step 6a), against real PostgreSQL.

A PlayerHealthService change and a death or respawn are sync units: they commit before the call returns, writing only
the stats keys and columns they changed. A removed stats key (the respawn's death room) is removed from the stored
jsonb. And a legacy full-row save of a copy loaded before those changes (``upsert_player``) can no longer write the
old DP or the death room back.
"""

import uuid
from typing import cast

import pytest
import structlog
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.constants.spawn_defaults import DEFAULT_RESPAWN_ROOM, LIMBO_ROOM_ID
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.persistence.repositories.player_repository_save import PlayerSavePreparer
from server.services.player_health_service import PlayerHealthService
from server.services.player_respawn_service import PlayerRespawnService
from server.tests.fixtures.integration.players import create_test_player, delete_test_user

STREET = "earth_arkhamcity_street_room_001"


@pytest.fixture
async def cleanup_test_user(session_factory: async_sessionmaker[AsyncSession]):
    """Yield a fresh user id; deleting it afterwards cascades to the player."""
    user_id = uuid.uuid4()
    yield user_id
    await delete_test_user(session_factory, user_id)


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


async def _row(
    session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID
) -> tuple[dict[str, object], str]:
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT stats, current_room_id FROM players WHERE player_id = :id"), {"id": str(player_id)}
            )
        ).one()
    return cast(dict[str, object], row[0]), cast(str, row[1])


async def _set_room(session_factory: async_sessionmaker[AsyncSession], player_id: uuid.UUID, room_id: str) -> None:
    async with session_factory() as session:
        _ = await session.execute(
            text("UPDATE players SET current_room_id = :room WHERE player_id = :id"),
            {"room": room_id, "id": str(player_id)},
        )
        await session.commit()


@pytest.mark.asyncio
async def test_death_and_respawn_round_trip(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    player_id = await create_test_player(session_factory, cleanup_test_user, stats={"current_dp": 5, "max_dp": 20})
    await _set_room(session_factory, player_id, STREET)
    registry = _registry(session_factory)

    change = await PlayerHealthService(registry).set_dp(player_id, -10)
    assert change.became_dead
    assert not registry.is_loaded(player_id)  # sync: committed, nothing left to sweep
    stats, _room = await _row(session_factory, player_id)
    # Not the room: make test-playwright runs this on mythos_e2e, whose live server moves the dead to limbo on any tick.
    assert (stats["current_dp"], stats["position"]) == (-10, "lying")

    respawn = PlayerRespawnService(player_registry=registry)
    assert await respawn.move_player_to_limbo(player_id, STREET) is True
    stats, room = await _row(session_factory, player_id)
    assert (room, stats["death_room_id"]) == (LIMBO_ROOM_ID, STREET)

    assert await respawn.respawn_player(player_id) is True
    stats, room = await _row(session_factory, player_id)
    assert room == DEFAULT_RESPAWN_ROOM  # the test player has no custom respawn room
    assert (stats["current_dp"], stats["position"]) == (20, "standing")
    assert "death_room_id" not in stats  # removed from the stored jsonb, not set to null


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_stale_full_row_save_keeps_the_stored_dp_and_death_room(
    session_factory: async_sessionmaker[AsyncSession], cleanup_test_user: uuid.UUID
):
    """upsert_player of a Player loaded before the registry changes keeps the registry's DP and death room."""
    player_id = await create_test_player(session_factory, cleanup_test_user, stats={"current_dp": -10, "max_dp": 20})
    await _set_room(session_factory, player_id, STREET)
    stale = await AsyncPersistenceLayer(_skip_room_cache=True).get_player_by_id(player_id)
    assert stale is not None
    registry = _registry(session_factory)
    assert await PlayerRespawnService(player_registry=registry).move_player_to_limbo(player_id, STREET) is True
    assert await PlayerRespawnService(player_registry=registry).respawn_player(player_id) is True

    stats = stale.get_stats()
    stats["current_dp"] = -3  # the stale copy's own DP: a write that bypassed the registry
    stats["death_room_id"] = STREET  # and a death room the respawn already cleared
    stats["luck"] = 7  # a stat the registry does not own yet still lands
    stale.set_stats(stats)
    preparer = PlayerSavePreparer(structlog.get_logger())
    async with session_factory() as session:
        await preparer.execute(session, preparer.prepare(stale))
        await session.commit()

    after, _room = await _row(session_factory, player_id)
    assert after["current_dp"] == 20
    assert "death_room_id" not in after
    assert after["luck"] == 7
