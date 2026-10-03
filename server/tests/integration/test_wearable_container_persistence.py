"""
Integration test: wearable containers against the real persistence layer (#951).

Every unit test of WearableContainerService mocked persistence synchronously and with pre-rename row
keys, so none noticed that equip never created a row (unawaited async create_container) and that
lookups read `metadata` where ContainerRepository returns `metadata_json`. This drives the service
through AsyncPersistenceLayer and a real database instead.
"""

import uuid
from typing import cast

import pytest
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from server.async_persistence import AsyncPersistenceLayer
from server.models.player import Player
from server.models.user import User
from server.services.wearable_container_service import WearableContainerService


async def _create_player(session_factory: async_sessionmaker[AsyncSession]) -> uuid.UUID:
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()
    async with session_factory() as session:
        session.add(
            User(
                id=str(user_id),
                email=f"wearable_{user_id}@example.com",
                username=f"wearable_{str(user_id)[:8]}",
                display_name=f"Wearable {str(user_id)[:8]}",
                hashed_password="hashed",
                is_active=True,
                is_superuser=False,
                is_verified=True,
            )
        )
        await session.flush()
        session.add(Player(player_id=str(player_id), user_id=str(user_id), name=f"wearable_{str(player_id)[:8]}"))
        await session.commit()
    return player_id


@pytest.mark.asyncio
@pytest.mark.usefixtures("fresh_database_manager")
async def test_equip_creates_one_row_reuses_it_and_unequip_reads_it_back(
    session_factory: async_sessionmaker[AsyncSession],
) -> None:
    player_id = await _create_player(session_factory)
    persistence = AsyncPersistenceLayer(_skip_room_cache=True)
    service = WearableContainerService(persistence=persistence)
    backpack: dict[str, object] = {
        "item_id": "backpack",
        "item_name": "Backpack",
        "item_instance_id": f"pack-{uuid.uuid4()}",
        "inner_container": {"capacity_slots": 8, "items": [], "lock_state": "unlocked"},
    }

    created = await service.handle_equip_wearable_container(player_id, backpack)
    reused = await service.handle_equip_wearable_container(player_id, backpack)

    assert created is not None
    assert reused == created  # matched through metadata_json.item_instance_id, not a second row
    rows = [
        row for row in await persistence.get_containers_by_entity_id(player_id) if row.get("source_type") == "equipment"
    ]
    assert len(rows) == 1
    assert str(rows[0]["container_id"]) == str(cast(object, created["container_id"]))

    unequipped = await service.handle_unequip_wearable_container(player_id, backpack)

    assert unequipped is not None
    assert unequipped["inner_container"]["capacity_slots"] == 8
    assert unequipped["inner_container"]["items"] == []
