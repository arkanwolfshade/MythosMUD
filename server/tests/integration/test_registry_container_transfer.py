"""
Integration test: a container transfer is one player-registry transaction against the real database (ADR-029 step 4b).

The unit tests fake the database; this proves the real pieces fit: the registry's session runs
write_container_items_async inside its own transaction (no commit of its own), next to update_player_inventory,
and a failure anywhere in that transaction leaves both the player and the container as they were.
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
from server.game.player_registry import DbSession, PlayerRegistry, SessionFactory
from server.models.player import Player
from server.models.user import User
from server.services.bank_service import get_or_create_bank_box
from server.services.container_service import ContainerService
from server.services.container_service_transfer_to import container_items_write
from server.services.inventory_service import InventoryStack

# Any existing prototype works as the moved item; this chest prototype is seeded by migration.
ITEM_PROTOTYPE_ID = "furniture.sanitarium.lost_and_found_chest"


def _stack() -> dict[str, object]:
    return {
        "item_id": ITEM_PROTOTYPE_ID,
        "prototype_id": ITEM_PROTOTYPE_ID,
        "item_instance_id": f"xfer-test-{uuid.uuid4().hex[:8]}",
        "item_name": "Keepsake",
        "slot_type": "backpack",
        "quantity": 1,
    }


async def _create_player(
    session_factory: async_sessionmaker[AsyncSession], carried: list[dict[str, object]]
) -> tuple[UUID, UUID]:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"xfer_{user_id}@example.com",
                username=f"xfer_{str(user_id)[:8]}",
                display_name=f"Xfer {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(
            Player(
                player_id=str(player_id),
                user_id=str(user_id),
                name=f"xfer_{str(player_id)[:8]}",
                inventory=json.dumps(carried),
            )
        )
        await session.commit()
    return player_id, user_id


async def _carried(session_factory: async_sessionmaker[AsyncSession], player_id: UUID) -> list[dict[str, object]]:
    async with session_factory() as session:
        raw = cast(
            object,
            (
                await session.execute(
                    text("SELECT inventory FROM players WHERE player_id = :id"), {"id": str(player_id)}
                )
            ).scalar_one(),
        )
    return cast(list[dict[str, object]], json.loads(str(raw)))


async def _box_items(persistence: AsyncPersistenceLayer, owner_id: UUID) -> list[Mapping[str, object]]:
    box = await persistence.get_bank_container(owner_id)
    assert box is not None
    return cast(list[Mapping[str, object]], box["items_json"])


async def _cleanup(session_factory: async_sessionmaker[AsyncSession], player_id: UUID, user_id: UUID) -> None:
    async with session_factory() as session:
        _ = await session.execute(text("DELETE FROM containers WHERE owner_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM item_instances WHERE item_instance_id LIKE 'xfer-test-%'"))
        _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
        _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_deposit_and_withdraw_commit_the_player_and_the_box_together(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    keepsake = _stack()
    player_id, user_id = await _create_player(session_factory, [keepsake])
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    registry = PlayerRegistry(cast(SessionFactory, session_factory))
    service = ContainerService(persistence=persistence)
    try:
        box_id = UUID(str((await get_or_create_bank_box(persistence, player_id))["container_id"]))
        token = service.register_open_session(box_id, player_id)

        _ = await service.transfer_to_container(
            box_id,
            player_id,
            token,
            cast(InventoryStack, cast(object, {"item_instance_id": keepsake["item_instance_id"]})),
            None,
            registry=registry,
        )
        assert await _carried(session_factory, player_id) == []
        assert [item["item_instance_id"] for item in await _box_items(persistence, player_id)] == [
            keepsake["item_instance_id"]
        ]

        _ = await service.transfer_from_container(
            box_id,
            player_id,
            token,
            cast(InventoryStack, cast(object, {"item_instance_id": keepsake["item_instance_id"]})),
            None,
            registry=registry,
        )
        assert [item["item_instance_id"] for item in await _carried(session_factory, player_id)] == [
            keepsake["item_instance_id"]
        ]
        assert await _box_items(persistence, player_id) == []
    finally:
        await _cleanup(session_factory, player_id, user_id)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_a_failure_late_in_the_transaction_rolls_back_both_the_player_and_the_box(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    keepsake = _stack()
    player_id, user_id = await _create_player(session_factory, [keepsake])
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    registry = PlayerRegistry(cast(SessionFactory, session_factory))

    async def fail(session: DbSession) -> None:
        _ = await session.execute(text("SELECT no_such_function()"))

    try:
        box_id = UUID(str((await get_or_create_bank_box(persistence, player_id))["container_id"]))
        with pytest.raises(Exception, match="no_such_function"):
            async with registry.mutate(player_id, containers=[box_id]) as player:
                player.inventory.set_carried([])
                registry.write_container(
                    box_id, container_items_write(box_id, [cast(InventoryStack, cast(object, keepsake))])
                )
                registry.write_container(box_id, fail)

        assert [item["item_instance_id"] for item in await _carried(session_factory, player_id)] == [
            keepsake["item_instance_id"]
        ]
        assert await _box_items(persistence, player_id) == []
    finally:
        await _cleanup(session_factory, player_id, user_id)
