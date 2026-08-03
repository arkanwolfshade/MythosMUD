"""Unit tests for ContainerRepository."""

from __future__ import annotations

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.persistence.container_create_params import ContainerCreateParams
from server.persistence.container_data import ContainerData, ContainerDataCore, ContainerDataExtras
from server.persistence.repositories.container_repository import ContainerRepository, _container_data_to_dict

CONTAINER_ID = uuid.UUID("aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa")


def _sample_container_data() -> ContainerData:
    now = datetime.now(UTC)
    return ContainerData(
        ContainerDataCore(
            container_instance_id=CONTAINER_ID,
            source_type="room",
            owner_id=None,
            room_id="room_001",
            entity_id=None,
            lock_state="unlocked",
            capacity_slots=10,
        ),
        ContainerDataExtras(
            weight_limit=100.0,
            decay_at=None,
            allowed_roles=[],
            items_json=[{"item_id": "x"}],
            metadata_json={"label": "chest"},
            created_at=now,
            updated_at=now,
        ),
    )


def test_container_data_to_dict_renames_keys() -> None:
    result = _container_data_to_dict(_sample_container_data())
    assert "items_json" in result
    assert "metadata_json" in result


@pytest.fixture
def repo() -> ContainerRepository:
    return ContainerRepository()


@pytest.mark.asyncio
async def test_create_container(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)
    params = ContainerCreateParams(
        owner_id=None,
        room_id="room_001",
        entity_id=None,
        lock_state="unlocked",
        capacity_slots=10,
        weight_limit=100.0,
        decay_at=None,
        allowed_roles=[],
        items_json=[],
        metadata_json={},
    )

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.create_container_async",
            new_callable=AsyncMock,
            return_value=_sample_container_data(),
        ),
    ):
        result = await repo.create_container("room", params)

    assert result["container_id"] == str(CONTAINER_ID)


@pytest.mark.asyncio
async def test_get_container_found(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.get_container_async",
            new_callable=AsyncMock,
            return_value=_sample_container_data(),
        ),
    ):
        result = await repo.get_container(CONTAINER_ID)

    assert result is not None
    assert result["room_id"] == "room_001"


@pytest.mark.asyncio
async def test_get_container_not_found(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.get_container_async",
            new_callable=AsyncMock,
            return_value=None,
        ),
    ):
        assert await repo.get_container(CONTAINER_ID) is None


@pytest.mark.asyncio
async def test_get_containers_by_room_id(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.get_containers_by_room_id_async",
            new_callable=AsyncMock,
            return_value=[_sample_container_data()],
        ),
    ):
        results = await repo.get_containers_by_room_id("room_001")

    assert len(results) == 1


@pytest.mark.asyncio
async def test_get_containers_by_entity_id(repo: ContainerRepository) -> None:
    entity_id = uuid.UUID("bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb")
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.get_containers_by_entity_id_async",
            new_callable=AsyncMock,
            return_value=[_sample_container_data()],
        ),
    ):
        results = await repo.get_containers_by_entity_id(entity_id)

    assert len(results) == 1


@pytest.mark.asyncio
async def test_update_container(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.update_container_async",
            new_callable=AsyncMock,
            return_value=_sample_container_data(),
        ),
    ):
        result = await repo.update_container(CONTAINER_ID, lock_state="locked")

    assert result is not None


@pytest.mark.asyncio
async def test_get_decayed_containers(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.get_decayed_containers_async",
            new_callable=AsyncMock,
            return_value=[],
        ),
    ):
        assert await repo.get_decayed_containers() == []


@pytest.mark.asyncio
async def test_delete_container(repo: ContainerRepository) -> None:
    mock_session = AsyncMock()
    mock_session.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session.__aexit__ = AsyncMock(return_value=None)

    with (
        patch(
            "server.persistence.repositories.container_repository.get_session_maker",
            return_value=MagicMock(return_value=mock_session),
        ),
        patch(
            "server.persistence.repositories.container_repository.delete_container_async",
            new_callable=AsyncMock,
            return_value=True,
        ),
    ):
        assert await repo.delete_container(CONTAINER_ID) is True
