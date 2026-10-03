"""
Integration test: lost-and-found deposits against the real persistence layer.

The flush service's unit tests use a fake persistence; this proves floor-drop stacks really
persist into an environment container through update_container (item instances included), in
order, with the oldest stacks evicted once the chest is full.
"""

import uuid
from typing import cast

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.persistence.container_create_params import ContainerCreateParams
from server.services.instance_flush_service import LOST_AND_FOUND_ROLE, deposit_in_lost_and_found

# Any existing prototype works as the dropped item; the chest prototype is seeded by migration.
ITEM_PROTOTYPE_ID = "furniture.sanitarium.lost_and_found_chest"


def _stack(label: str) -> dict[str, object]:
    return {
        "item_id": ITEM_PROTOTYPE_ID,
        "item_instance_id": f"lf-test-{label}-{uuid.uuid4().hex[:8]}",
        "item_name": label,
        "slot_type": "backpack",
        "quantity": 1,
    }


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_deposit_persists_stacks_in_order_and_evicts_oldest(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    room_id = f"test_lost_and_found_{uuid.uuid4().hex[:12]}"
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    _ = await persistence.create_container(
        "environment",
        ContainerCreateParams(
            room_id=room_id,
            capacity_slots=2,
            metadata_json={"name": "Test Chest", "role": LOST_AND_FOUND_ROLE},
        ),
    )
    first, second, third = _stack("first"), _stack("second"), _stack("third")
    try:
        await deposit_in_lost_and_found(persistence, room_id, [first])
        await deposit_in_lost_and_found(persistence, room_id, [second, third])

        [chest] = await persistence.get_containers_by_room_id(room_id)
        held = cast(list[dict[str, object]], chest["items_json"])
        held_ids = [stack["item_instance_id"] for stack in held]
        assert held_ids == [second["item_instance_id"], third["item_instance_id"]]
    finally:
        async with session_factory() as session:
            _ = await session.execute(text("DELETE FROM containers WHERE room_id = :room_id"), {"room_id": room_id})
            _ = await session.execute(
                text("DELETE FROM item_instances WHERE item_instance_id LIKE 'lf-test-%'"),
            )
            await session.commit()
