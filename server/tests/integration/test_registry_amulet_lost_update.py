"""
Integration test: the amulet lost update (ADR-029 step 4c-iii, the bug that started the player registry).

e2e logs 2026-10-26 15:15:23: the status-effect tick loaded the player, a `get amulet` pickup committed 3 carried
items, then the tick saved its copy, loaded before the pickup, with save_player, and every later tick re-wrote 2.
The amulet was gone. Inventory is now written only by the registry, so a save_player of a stale copy keeps its own
columns (DP here) and leaves the carried and equipped stacks alone.
"""

import json
import uuid
from typing import cast
from uuid import UUID

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.player_registry import PlayerRegistry, SessionFactory
from server.models.player import Player
from server.models.user import User

ITEM_PROTOTYPE_ID = "furniture.sanitarium.lost_and_found_chest"


def _stack(name: str) -> dict[str, object]:
    return {
        "item_id": ITEM_PROTOTYPE_ID,
        "prototype_id": ITEM_PROTOTYPE_ID,
        "item_instance_id": f"amulet-test-{name}-{uuid.uuid4().hex[:8]}",
        "item_name": name,
        "slot_type": "backpack",
        "quantity": 1,
    }


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"amulet_{user_id}@example.com",
                username=f"amulet_{str(user_id)[:8]}",
                display_name=f"Amulet {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"amulet_{str(player_id)[:8]}"))
        await session.commit()
    return player_id, user_id


async def _saved(
    session_factory: async_sessionmaker[AsyncSession], player_id: UUID
) -> tuple[list[dict[str, object]], list[dict[str, object]], dict[str, object], dict[str, object]]:
    """Both carried copies, the equipped stacks and the stats, as stored."""
    async with session_factory() as session:
        row = (
            await session.execute(
                text(
                    "SELECT p.inventory, pi.inventory_json, pi.equipped_json, p.stats FROM players p"
                    + " JOIN player_inventories pi ON pi.player_id = p.player_id WHERE p.player_id = :id"
                ),
                {"id": str(player_id)},
            )
        ).one()
    stats = cast(object, row[3])
    return (
        cast(list[dict[str, object]], json.loads(str(cast(object, row[0])))),
        cast(list[dict[str, object]], json.loads(str(cast(object, row[1])))),
        cast(dict[str, object], json.loads(str(cast(object, row[2])))),
        cast(dict[str, object], stats if isinstance(stats, dict) else json.loads(str(stats))),
    )


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_tick_save_of_a_copy_loaded_before_a_pickup_keeps_the_amulet(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """The 15:15:23 sequence: tick load, registry pickup, tick save. The pickup and the tick's heal both survive."""
    player_id, user_id = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    registry = PlayerRegistry(cast(SessionFactory, session_factory))
    try:
        lantern, coin, amulet = _stack("lantern"), _stack("coin"), _stack("amulet")
        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            player.inventory.replace([lantern, coin], {})

        tick_copy = await persistence.get_player_by_id(player_id)  # the tick's load: 2 carried items
        assert tick_copy is not None and len(tick_copy.get_inventory()) == 2

        async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
            player.inventory.set_carried([lantern, coin, amulet])  # `get amulet`

        stats = tick_copy.get_stats()
        stats["current_dp"] = 42  # heal_player
        tick_copy.set_stats(stats)
        await persistence.save_player(tick_copy)

        carried, carried_json, equipped, saved_stats = await _saved(session_factory, player_id)
        ids = [lantern["item_instance_id"], coin["item_instance_id"], amulet["item_instance_id"]]
        assert [stack["item_instance_id"] for stack in carried] == ids
        assert [stack["item_instance_id"] for stack in carried_json] == ids
        assert equipped == {}
        assert saved_stats["current_dp"] == 42  # the tick's own column still saved
    finally:
        await _cleanup(session_factory, player_id, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_save_player_still_writes_a_new_players_starting_inventory(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    """Character creation inserts through save_player, so the insert keeps writing both inventory copies."""
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"amulet_{user_id}@example.com",
                username=f"amulet_{str(user_id)[:8]}",
                display_name=f"Amulet {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.commit()
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    try:
        candle = _stack("candle")
        new_player = Player(player_id=str(player_id), user_id=str(user_id), name=f"amulet_{str(player_id)[:8]}")
        new_player.set_inventory([candle])
        await persistence.save_player(new_player)

        carried, carried_json, equipped, _stats = await _saved(session_factory, player_id)
        assert [stack["item_instance_id"] for stack in carried] == [candle["item_instance_id"]]
        assert [stack["item_instance_id"] for stack in carried_json] == [candle["item_instance_id"]]
        assert equipped == {}
    finally:
        await _cleanup(session_factory, player_id, user_id)
