"""
Integration test: a full-row player write never undoes a soft delete.

A copy of the player loaded before the delete committed (a 10 Hz MP-regen save, or a registry aggregate) used to
write is_deleted=false back over it, so a deleted character came back on the character list. save_player's
player_is_deleted guard is check-then-act and cannot close that window; upsert_player and update_player_row must.
"""

import uuid
from typing import cast
from uuid import UUID

import pytest
import structlog
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.player_registry import PlayerRegistry, SessionFactory
from server.models.player import Player
from server.models.user import User
from server.persistence.repositories.player_repository_save import PlayerSavePreparer


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"undelete_{user_id}@example.com",
                username=f"undelete_{str(user_id)[:8]}",
                display_name=f"Undelete {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"undelete_{str(player_id)[:8]}"))
        await session.commit()
    return player_id, user_id


async def _is_deleted(session_factory: async_sessionmaker[AsyncSession], player_id: UUID) -> tuple[bool, object]:
    async with session_factory() as session:
        row = (
            await session.execute(
                text("SELECT is_deleted, deleted_at FROM players WHERE player_id = :id"), {"id": str(player_id)}
            )
        ).one()
    return bool(cast(object, row[0])), cast(object, row[1])


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_upsert_of_a_copy_loaded_before_the_delete_keeps_it_deleted(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """upsert_player of a Player loaded before the delete leaves is_deleted and deleted_at as the delete set them."""
    player_id, user_id = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    try:
        stale = await persistence.get_player_by_id(player_id)
        assert stale is not None and not stale.is_deleted
        assert await persistence.soft_delete_player(player_id)
        deleted_at = (await _is_deleted(session_factory, player_id))[1]

        # The upsert save_player runs once its guard has (already) passed: the delete landed in between.
        preparer = PlayerSavePreparer(structlog.get_logger())
        async with session_factory() as session:
            await preparer.execute(session, preparer.prepare(stale))
            await session.commit()

        assert await _is_deleted(session_factory, player_id) == (True, deleted_at)
    finally:
        await _cleanup(session_factory, player_id, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_registry_write_of_an_aggregate_loaded_before_the_delete_keeps_it_deleted(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """update_player_row from a registry unit that spans the delete leaves the character deleted."""
    player_id, user_id = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    registry = PlayerRegistry(cast(SessionFactory, session_factory))
    try:
        async with registry.mutate(player_id, sync=True) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            assert await persistence.soft_delete_player(player_id)
            player.row.set_stat("magic_points", 3)  # dirty: the unit writes update_player_row on exit

        is_deleted, deleted_at = await _is_deleted(session_factory, player_id)
        assert is_deleted and deleted_at is not None
    finally:
        await _cleanup(session_factory, player_id, user_id)
