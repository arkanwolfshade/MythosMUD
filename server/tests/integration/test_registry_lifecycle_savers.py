"""
Integration tests: the connection-lifecycle savers write through the registry (ADR-029 step 8a), against a real database.

A tutorial reconnect commits the player's room and instance as one synchronous unit; logout and quit stamp
``last_active`` lazily and the sweep writes it. Neither saves the whole row any more.
"""

import uuid
from datetime import UTC, datetime, timedelta
from typing import cast
from uuid import UUID

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.game.instance_state import place_in_instance
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.models.player import Player
from server.models.user import User

ROOM = "instance_abc_earth_demo_zone_room_square_001"


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"lifecycle_{user_id}@example.com",
                username=f"life_{str(user_id)[:8]}",
                display_name=f"Life {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"life_{str(player_id)[:8]}"))
        await session.commit()
    return player_id, user_id


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


def _registry(session_factory: async_sessionmaker[AsyncSession]) -> PlayerRegistry:
    """No idle TTL, so every read loads the player fresh from the database."""
    return PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_tutorial_placement_commits_the_room_and_the_instance(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player_id, user_id = await _create_player(session_factory)
    registry = _registry(session_factory)
    try:
        copy = Player(player_id=str(player_id), name="Placed", tutorial_instance_id="instance_abc")

        await place_in_instance(registry, copy, ROOM)

        placed = await registry.get(player_id)
        assert placed is not None
        assert placed.row.current_room_id == ROOM
        assert placed.row.tutorial_instance_id == "instance_abc"
    finally:
        await _cleanup(session_factory, player_id, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_last_active_is_stamped_lazily_and_the_sweep_writes_it(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player_id, user_id = await _create_player(session_factory)
    registry = _registry(session_factory)
    stamp = datetime.now(UTC) + timedelta(days=1)  # clearly later than the row's creation time
    try:
        async with registry.mutate(player_id) as aggregate:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            aggregate.row.touch_last_active(stamp)

        assert await _stored_last_active(session_factory, player_id) != stamp  # lazy: nothing committed yet
        assert await registry.flush_dirty() == 1
        assert await _stored_last_active(session_factory, player_id) == stamp
    finally:
        await _cleanup(session_factory, player_id, user_id)


async def _stored_last_active(session_factory: async_sessionmaker[AsyncSession], player_id: UUID) -> datetime | None:
    async with session_factory() as session:
        result = await session.execute(
            text("SELECT last_active FROM players WHERE player_id = :id"), {"id": str(player_id)}
        )
        return cast(datetime | None, result.scalar_one())
