"""
Integration tests: moving and sitting are registry units (ADR-029 step 7a), against a real database.

Before this step a move and a posture change each loaded the player, changed one field, and saved the whole row, so
one could put back what the other had just written. Now each commits only its own column or stats key under the
player's lock.
"""

import asyncio
import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import UUID

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.movement_service import MovementService
from server.game.player_registry import PlayerRegistry, RegistrySettings, SessionFactory
from server.models.player import Player
from server.models.user import User
from server.services.player_position_service import PlayerPositionService, SupportsPlayerPersistence

TO_ROOM_ID = "earth_arkhamcity_sanitarium_room_hallway_001"


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> tuple[UUID, UUID, str]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    name = f"mover_{str(player_id)[:8]}"
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"mover_{user_id}@example.com",
                username=f"mover_{str(user_id)[:8]}",
                display_name=f"Mover {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=name))
        await session.commit()
    return player_id, user_id, name


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_move_racing_a_posture_change_loses_neither(session_factory: async_sessionmaker[AsyncSession]) -> None:
    player_id, user_id, name = await _create_player(session_factory)
    # As in production for now: no idle TTL, so every unit loads the player fresh from the database.
    registry = PlayerRegistry(cast(SessionFactory, session_factory), settings=RegistrySettings(idle_ttl_seconds=0))
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    try:
        stored = await persistence.get_player_by_id(player_id)
        assert stored is not None
        from_room_id = str(stored.current_room_id)
        from_room, to_room = MagicMock(), MagicMock()
        from_room.configure_mock(id=from_room_id, has_player=MagicMock(return_value=True))
        to_room.configure_mock(id=TO_ROOM_ID)
        rooms = {from_room_id: from_room, TO_ROOM_ID: to_room}
        persistence.get_room_by_id = MagicMock(side_effect=rooms.get)
        movement = MovementService(async_persistence=persistence, player_registry=registry)
        posture = PlayerPositionService(
            cast(SupportsPlayerPersistence, cast(object, persistence)), None, None, registry
        )

        with (
            patch.object(movement, "_validate_movement", new=AsyncMock(return_value=True)),
            patch("server.game.movement_service.get_movement_monitor"),
        ):
            moved, sat = await asyncio.gather(
                movement.move_player(player_id, from_room_id, TO_ROOM_ID),
                posture.change_position(name, "sitting"),
            )

        assert moved is True and sat["success"] is True
        player = await registry.get(player_id)
        assert player is not None
        assert player.row.current_room_id == TO_ROOM_ID
        assert player.row.stats["position"] == "sitting"
    finally:
        await _cleanup(session_factory, player_id, user_id)
