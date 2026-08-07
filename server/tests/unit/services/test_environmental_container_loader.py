"""Unit tests for EnvironmentalContainerLoader (room JSON -> container models)."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.exceptions import ValidationError
from server.models.container import ContainerLockState
from server.services.environmental_container_loader import EnvironmentalContainerLoader


def test_environmental_loader_requires_persistence() -> None:
    with pytest.raises(ValueError, match="persistence"):
        _ = EnvironmentalContainerLoader()


def test_load_container_from_room_json_none_when_missing() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    assert loader.load_container_from_room_json({}, "room-a") is None


def test_load_container_from_room_json_disabled() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {"id": "room-a", "container": {"enabled": False}}
    assert loader.load_container_from_room_json(room_json, "room-a") is None


def test_load_container_from_room_json_success() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {
        "id": "room-a",
        "container": {
            "capacity_slots": 10,
            "lock_state": "locked",
            "key_item_id": "key-1",
            "allowed_roles": ["investigator"],
        },
    }
    container = loader.load_container_from_room_json(room_json, "room-a")
    assert container is not None
    assert container.capacity_slots == 10
    assert container.lock_state == ContainerLockState.LOCKED
    assert container.metadata["key_item_id"] == "key-1"


def test_load_container_from_room_json_invalid_capacity() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {"id": "room-a", "container": {"capacity_slots": 99}}
    with pytest.raises(ValidationError):
        _ = loader.load_container_from_room_json(room_json, "room-a")


def test_load_container_from_room_json_invalid_lock_state() -> None:
    loader = EnvironmentalContainerLoader(persistence=MagicMock())
    room_json = {"id": "room-a", "container": {"lock_state": "broken"}}
    with pytest.raises(ValidationError):
        _ = loader.load_container_from_room_json(room_json, "room-a")


@pytest.mark.asyncio
async def test_migrate_room_container_existing() -> None:
    existing_id = uuid.uuid4()
    persistence = MagicMock()
    persistence.get_containers_by_room_id = AsyncMock(
        return_value=[{"source_type": "environment", "container_id": str(existing_id)}]
    )
    create_container: AsyncMock = AsyncMock()
    persistence.create_container = create_container
    loader = EnvironmentalContainerLoader(persistence=persistence)
    room_json = {"id": "room-a", "container": {"capacity_slots": 5}}
    result = await loader.migrate_room_container_to_postgresql(room_json, "room-a")
    assert result == existing_id
    create_container.assert_not_called()


@pytest.mark.asyncio
async def test_migrate_room_container_creates_new() -> None:
    persistence = MagicMock()
    persistence.get_containers_by_room_id = AsyncMock(return_value=[])
    new_id = uuid.uuid4()
    persistence.create_container = AsyncMock(return_value={"container_id": str(new_id)})
    loader = EnvironmentalContainerLoader(persistence=persistence)
    room_json = {"id": "room-a", "container": {"capacity_slots": 5}}
    result = await loader.migrate_room_container_to_postgresql(room_json, "room-a")
    assert result == new_id


@pytest.mark.asyncio
async def test_load_containers_for_room_filters_environment() -> None:
    persistence = MagicMock()
    container_id = uuid.uuid4()
    persistence.get_containers_by_room_id = AsyncMock(
        return_value=[
            {
                "container_id": str(container_id),
                "source_type": "environment",
                "capacity_slots": 5,
                "room_id": "room-a",
                "lock_state": "unlocked",
                "items": [],
                "metadata": {},
            },
            {"container_id": str(uuid.uuid4()), "source_type": "corpse", "capacity_slots": 3},
        ]
    )
    loader = EnvironmentalContainerLoader(persistence=persistence)
    containers = await loader.load_containers_for_room("room-a")
    assert len(containers) == 1
    assert containers[0].container_id == container_id
