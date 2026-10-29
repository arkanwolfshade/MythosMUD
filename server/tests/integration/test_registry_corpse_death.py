"""
Integration test: a death's corpse transfer is one player-registry transaction against the real database (ADR-029
step 4c-ii).

The unit tests fake the database; this proves the real pieces fit: the registry's session runs the create_container
procedure and the corpse's items, the worn-container delete and update_player_inventory in one transaction, and a
failure anywhere in it leaves the player, their worn container and the room as they were (no corpse).
"""

import json
import uuid
from collections.abc import Mapping
from typing import cast
from uuid import UUID

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.player_registry import PlayerRegistry, SessionFactory
from server.models.player import Player
from server.models.user import User
from server.persistence.container_create_params import ContainerCreateParams
from server.services.corpse_lifecycle_service import CorpseLifecycleService, CorpseServiceError

# Any existing prototype works as the item; this chest prototype is seeded by migration.
ITEM_PROTOTYPE_ID = "furniture.sanitarium.lost_and_found_chest"
ROOM_ID = "earth_arkhamcity_sanitarium_room_foyer_001"


def _stack(name: str, slot_type: str = "backpack") -> dict[str, object]:
    return {
        "item_id": ITEM_PROTOTYPE_ID,
        "prototype_id": ITEM_PROTOTYPE_ID,
        "item_instance_id": f"death-test-{name}-{uuid.uuid4().hex[:8]}",
        "item_name": name,
        "slot_type": slot_type,
        "quantity": 1,
    }


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"death_{user_id}@example.com",
                username=f"death_{str(user_id)[:8]}",
                display_name=f"Death {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"death_{str(player_id)[:8]}"))
        await session.commit()
    return player_id, user_id


async def _dress(
    registry: PlayerRegistry, persistence: AsyncPersistenceLayer, player_id: UUID
) -> tuple[dict[str, object], dict[str, object], dict[str, object], UUID]:
    """Carry a keepsake, wear a backpack holding a coin (its own equipment-container row). Returns all three + row."""
    keepsake, pack, coin = _stack("keepsake"), _stack("backpack", "back"), _stack("coin")
    async with registry.mutate(player_id) as player:  # pylint: disable=contextmanager-generator-missing-cleanup  # Reason: @asynccontextmanager always drives this generator to completion; pylint cannot see through the wrapper
        player.inventory.replace([keepsake], {"back": pack})
    worn = await persistence.create_container(
        "equipment",
        ContainerCreateParams(
            entity_id=player_id,
            capacity_slots=8,
            items_json=[coin],
            metadata_json={"item_instance_id": pack["item_instance_id"], "item_name": "Backpack"},
        ),
    )
    return keepsake, pack, coin, UUID(str(worn["container_id"]))


async def _saved_inventory(
    session_factory: async_sessionmaker[AsyncSession], player_id: UUID
) -> tuple[list[dict[str, object]], dict[str, object]]:
    async with session_factory() as session:
        row = (
            await session.execute(
                text(
                    "SELECT p.inventory, pi.equipped_json FROM players p"
                    + " JOIN player_inventories pi ON pi.player_id = p.player_id WHERE p.player_id = :id"
                ),
                {"id": str(player_id)},
            )
        ).one()
    carried = cast(list[dict[str, object]], json.loads(str(cast(object, row[0]))))
    equipped = cast(dict[str, object], json.loads(str(cast(object, row[1]))))
    return carried, equipped


async def _corpses(persistence: AsyncPersistenceLayer, player_id: UUID) -> list[Mapping[str, object]]:
    rows = await persistence.get_containers_by_room_id(ROOM_ID)
    return [row for row in rows if row.get("source_type") == "corpse" and row.get("owner_id") == str(player_id)]


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(
            text("DELETE FROM containers WHERE owner_id = :id OR entity_id = :id"), {"id": str(player_id)}
        )
        _ = await session.execute(text("DELETE FROM item_instances WHERE item_instance_id LIKE 'death-test-%'"))
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_death_moves_carried_and_worn_gear_onto_a_corpse_in_one_transaction(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player_id, user_id = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    registry = PlayerRegistry(cast(SessionFactory, session_factory))
    try:
        keepsake, pack, coin, worn_id = await _dress(registry, persistence, player_id)

        corpse = await CorpseLifecycleService(persistence=persistence, player_registry=registry).create_corpse_on_death(
            player_id, ROOM_ID
        )

        assert await _saved_inventory(session_factory, player_id) == ([], {})
        assert await persistence.get_container(worn_id) is None  # folded into the backpack's stack, then deleted
        [stored] = await _corpses(persistence, player_id)
        assert stored["container_id"] == str(corpse.container_id)  # the procedure's id, set on the returned corpse
        items = cast(list[Mapping[str, object]], stored["items_json"])
        assert [item["item_instance_id"] for item in items] == [keepsake["item_instance_id"], pack["item_instance_id"]]
        inner = cast(Mapping[str, object], items[1]["inner_container"])
        assert [item["item_instance_id"] for item in cast(list[Mapping[str, object]], inner["items"])] == [
            coin["item_instance_id"]
        ]
    finally:
        await _cleanup(session_factory, player_id, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_failure_late_in_the_death_rolls_back_the_corpse_and_keeps_the_player_dressed(
    session_factory: async_sessionmaker[AsyncSession],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    player_id, user_id = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    registry = PlayerRegistry(cast(SessionFactory, session_factory))
    try:
        keepsake, pack, _coin, worn_id = await _dress(registry, persistence, player_id)

        async def fail(_session: AsyncSession, _container_id: UUID) -> None:
            raise RuntimeError("database went away mid-death")

        # The worn-container delete runs after the corpse's create in the same transaction.
        monkeypatch.setattr("server.services.corpse_lifecycle_service.delete_container_in_transaction_async", fail)
        with pytest.raises(CorpseServiceError):
            _ = await CorpseLifecycleService(persistence=persistence, player_registry=registry).create_corpse_on_death(
                player_id, ROOM_ID
            )

        assert await _saved_inventory(session_factory, player_id) == ([keepsake], {"back": pack})
        assert await persistence.get_container(worn_id) is not None
        assert await _corpses(persistence, player_id) == []
        # The in-memory player rolled back too, so the next unit still sees the gear.
        live = registry.peek(player_id)
        assert live is not None and [dict(stack) for stack in live.inventory.carried] == [keepsake]
    finally:
        await _cleanup(session_factory, player_id, user_id)
