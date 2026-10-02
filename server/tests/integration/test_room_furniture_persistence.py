"""
Integration test: room furniture sync against the real persistence layer.

The loader's unit tests use a fake persistence; this drives sync_room_furniture through
AsyncPersistenceLayer and the real create_container / update_container / set_container_capacity
procedures, proving a furniture container is created once, refreshed from its prototype in place,
and never duplicated on restart.
"""

import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.game.items.models import ItemPrototypeModel
from server.game.items.prototype_registry import PrototypeRegistry
from server.models.room import Room
from server.services.room_furniture_loader import sync_room_furniture

CHEST_ID = "furniture.test.integration_chest"


def _registry(name: str, capacity: int) -> PrototypeRegistry:
    prototype = ItemPrototypeModel.model_validate(
        {
            "prototype_id": CHEST_ID,
            "name": name,
            "short_description": "a test chest",
            "long_description": "A chest that exists only for this test.",
            "item_type": "container",
            "weight": 1.0,
            "base_value": 0,
            "durability": None,
            "flags": [],
            "wear_slots": [],
            "stacking_rules": {},
            "usage_restrictions": {},
            "effect_components": [],
            "metadata": {"container": {"capacity_slots": capacity}},
            "tags": [],
        }
    )
    return PrototypeRegistry({CHEST_ID: prototype}, [])


@pytest.mark.asyncio
async def test_furniture_container_created_once_then_refreshed_in_place(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    room_id = f"test_furniture_room_{uuid.uuid4().hex[:12]}"
    room = Room({"id": room_id, "attributes": {"furniture": [{"prototype_id": CHEST_ID, "role": "lost_and_found"}]}})
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    try:
        assert await sync_room_furniture([room], _registry("Test Chest", 50), persistence) == 1
        [created] = await persistence.get_containers_by_room_id(room_id)
        assert created["source_type"] == "environment"
        assert created["capacity_slots"] == 50
        assert created["metadata_json"] == {"name": "Test Chest", "prototype_id": CHEST_ID, "role": "lost_and_found"}

        # Restart with a resized, renamed prototype: same row, refreshed (beyond the old 20-slot cap).
        assert await sync_room_furniture([room], _registry("Renamed Chest", 200), persistence) == 1
        [refreshed] = await persistence.get_containers_by_room_id(room_id)
        assert refreshed["container_id"] == created["container_id"]
        assert refreshed["capacity_slots"] == 200
        assert refreshed["metadata_json"] == {
            "name": "Renamed Chest",
            "prototype_id": CHEST_ID,
            "role": "lost_and_found",
        }

        # A plain restart changes nothing and never duplicates the row.
        assert await sync_room_furniture([room], _registry("Renamed Chest", 200), persistence) == 1
        assert len(await persistence.get_containers_by_room_id(room_id)) == 1
    finally:
        async with session_factory() as session:
            _ = await session.execute(text("DELETE FROM containers WHERE room_id = :room_id"), {"room_id": room_id})
            await session.commit()
