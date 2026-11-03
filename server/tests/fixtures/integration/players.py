"""A real user and player for integration tests that drive the player registry against PostgreSQL."""

from __future__ import annotations

import uuid

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.models.player import Player
from server.models.user import User


async def create_test_player(
    session_factory: async_sessionmaker[AsyncSession], user_id: uuid.UUID, *, stats: dict[str, object] | None = None
) -> uuid.UUID:
    """Insert a user with this id and one player for it; the player's id."""
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"test_{user_id}@example.com",
                username=f"testuser_{str(user_id)[:8]}",
                display_name=f"Test User {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        player = Player(
            player_id=str(player_id),
            user_id=str(user_id),
            name=f"testplayer_{str(player_id)[:8]}",
            current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
        )
        if stats is not None:
            player.set_stats(stats)
        session.add(player)
        await session.commit()
    return player_id


async def delete_test_user(session_factory: async_sessionmaker[AsyncSession], user_id: uuid.UUID) -> None:
    """Delete the user; it cascades to their players and every player-keyed row."""
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()
