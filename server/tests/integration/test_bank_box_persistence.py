"""
Integration test: bank deposit boxes against the real persistence layer and database (#977).

The unit tests use a fake persistence; this proves the pieces the migration/schema add really work:
the 'bank' source type, the get_bank_container procedure, one box per owner (unique index), stacks
persisting in order and never being trimmed, and a box outliving its deleted owner as an unreachable
orphan (containers.owner_id is ON DELETE SET NULL).
"""

import uuid
from typing import cast
from uuid import UUID

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.exceptions import DatabaseError
from server.models.player import Player
from server.models.user import User
from server.persistence.container_create_params import ContainerCreateParams
from server.services.bank_service import BANK_BOX_CAPACITY, forward_to_bank_box, get_or_create_bank_box

# Any existing prototype works as the deposited item; this chest prototype is seeded by migration.
ITEM_PROTOTYPE_ID = "furniture.sanitarium.lost_and_found_chest"


def _stack(label: str) -> dict[str, object]:
    return {
        "item_id": ITEM_PROTOTYPE_ID,
        "item_instance_id": f"bank-test-{label}-{uuid.uuid4().hex[:8]}",
        "item_name": label,
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
                email=f"bank_{user_id}@example.com",
                username=f"bank_{str(user_id)[:8]}",
                display_name=f"Bank {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"bank_{str(player_id)[:8]}"))
        await session.commit()
    return player_id, user_id


async def _cleanup(
    session_factory: async_sessionmaker[AsyncSession], players: list[tuple[UUID, UUID]], box_ids: list[str]
) -> None:
    async with session_factory() as session:
        for box_id in box_ids:
            _ = await session.execute(
                text("DELETE FROM containers WHERE container_instance_id = CAST(:id AS uuid)"), {"id": box_id}
            )
        _ = await session.execute(text("DELETE FROM item_instances WHERE item_instance_id LIKE 'bank-test-%'"))
        for player_id, user_id in players:
            _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player_id)})
            _ = await session.execute(text("DELETE FROM users WHERE id = :id"), {"id": str(user_id)})
        await session.commit()


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_box_is_created_once_and_stacks_persist_in_order_without_trimming(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player = await _create_player(session_factory)
    owner_id = player[0]
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    first, second, third = _stack("first"), _stack("second"), _stack("third")
    box_ids: list[str] = []
    try:
        box = await get_or_create_bank_box(persistence, owner_id)
        box_ids.append(str(box["container_id"]))
        again = await get_or_create_bank_box(persistence, owner_id)

        assert again["container_id"] == box["container_id"]
        assert box["source_type"] == "bank"
        assert box["owner_id"] == str(owner_id)
        assert box["room_id"] is None
        assert box["capacity_slots"] == BANK_BOX_CAPACITY

        # Shrink the box below what we are about to put in: forwarded items must still all be kept.
        _ = await persistence.update_container(UUID(str(box["container_id"])), capacity_slots=2)
        await forward_to_bank_box(persistence, owner_id, [first])
        await forward_to_bank_box(persistence, owner_id, [second, third])

        stored = await persistence.get_bank_container(owner_id)
        assert stored is not None
        held = cast(list[dict[str, object]], stored["items_json"])
        assert [stack["item_instance_id"] for stack in held] == [
            first["item_instance_id"],
            second["item_instance_id"],
            third["item_instance_id"],
        ]
        assert stored["capacity_slots"] == 2  # 3 stacks in a 2-slot box
    finally:
        await _cleanup(session_factory, [player], box_ids)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_each_owner_has_their_own_box_and_the_database_allows_only_one_each(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    alice, bob = await _create_player(session_factory), await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    box_ids: list[str] = []
    try:
        alice_box = await get_or_create_bank_box(persistence, alice[0])
        bob_box = await get_or_create_bank_box(persistence, bob[0])
        box_ids += [str(alice_box["container_id"]), str(bob_box["container_id"])]

        assert alice_box["container_id"] != bob_box["container_id"]
        assert await persistence.get_bank_container(uuid.uuid4()) is None  # a stranger has no box
        # uq_containers_bank_owner: even bypassing get-or-create, a second box for the same owner is refused.
        with pytest.raises(DatabaseError):
            _ = await persistence.create_container(
                "bank", ContainerCreateParams(owner_id=alice[0], capacity_slots=BANK_BOX_CAPACITY)
            )
    finally:
        await _cleanup(session_factory, [alice, bob], box_ids)


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_deleting_the_owner_leaves_an_orphaned_box_nobody_can_look_up(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    box = await get_or_create_bank_box(persistence, player[0])
    try:
        await forward_to_bank_box(persistence, player[0], [_stack("keepsake")])
        async with session_factory() as session:
            _ = await session.execute(text("DELETE FROM players WHERE player_id = :id"), {"id": str(player[0])})
            await session.commit()

        assert await persistence.get_bank_container(player[0]) is None
        orphan = await persistence.get_container(UUID(str(box["container_id"])))
        assert orphan is not None  # the contents survive for an admin to recover
        assert orphan["owner_id"] is None
    finally:
        await _cleanup(session_factory, [player], [str(box["container_id"])])
