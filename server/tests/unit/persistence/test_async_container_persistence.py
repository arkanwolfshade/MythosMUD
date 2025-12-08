"""
Greenfield async unit tests for AsyncPersistenceLayer container operations.

These tests cover all container-related persistence operations using the
async persistence layer directly.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.events.event_bus import EventBus


class TestAsyncContainerPersistence:
    """Test async container persistence operations."""

    @pytest.fixture
    def event_bus(self):
        """Create an event bus for testing."""
        return EventBus()

    @pytest.fixture
    def async_persistence(self, event_bus):
        """Create an AsyncPersistenceLayer instance for testing."""
        return AsyncPersistenceLayer(event_bus=event_bus)

    @pytest.fixture
    def sample_container_data(self):
        """Create sample container data for testing."""
        return {
            "container_id": str(uuid4()),
            "source_type": "environment",
            "room_id": "earth_arkhamcity_downtown_room_derby_st_001",
            "lock_state": "unlocked",
            "capacity_slots": 20,
            "items_json": [],
            "metadata_json": {},
        }

    @pytest.mark.asyncio
    async def test_create_container(self, async_persistence, sample_container_data):
        """Test creating a container."""
        # Mock the repository create method
        async_persistence._container_repo.create_container = AsyncMock(return_value=sample_container_data)

        result = await async_persistence.create_container(
            source_type="environment",
            room_id=sample_container_data["room_id"],
            capacity_slots=20,
        )

        assert result is not None
        assert result["container_id"] == sample_container_data["container_id"]
        async_persistence._container_repo.create_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_container(self, async_persistence, sample_container_data):
        """Test getting a container by ID."""
        container_id = uuid.UUID(sample_container_data["container_id"])
        # Mock the repository get method
        async_persistence._container_repo.get_container = AsyncMock(return_value=sample_container_data)

        result = await async_persistence.get_container(container_id)

        assert result is not None
        assert result["container_id"] == sample_container_data["container_id"]
        async_persistence._container_repo.get_container.assert_called_once_with(container_id)

    @pytest.mark.asyncio
    async def test_get_container_not_exists(self, async_persistence):
        """Test getting a container that does not exist."""
        container_id = uuid4()
        # Mock the repository to return None
        async_persistence._container_repo.get_container = AsyncMock(return_value=None)

        result = await async_persistence.get_container(container_id)

        assert result is None
        async_persistence._container_repo.get_container.assert_called_once_with(container_id)

    @pytest.mark.asyncio
    async def test_get_containers_by_room_id(self, async_persistence, sample_container_data):
        """Test getting containers by room ID."""
        room_id = sample_container_data["room_id"]
        containers = [sample_container_data]
        # Mock the repository get method
        async_persistence._container_repo.get_containers_by_room_id = AsyncMock(return_value=containers)

        result = await async_persistence.get_containers_by_room_id(room_id)

        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0]["room_id"] == room_id
        async_persistence._container_repo.get_containers_by_room_id.assert_called_once_with(room_id)

    @pytest.mark.asyncio
    async def test_get_containers_by_entity_id(self, async_persistence, sample_container_data):
        """Test getting containers by entity ID."""
        entity_id = uuid4()
        containers = [sample_container_data]
        # Mock the repository get method
        async_persistence._container_repo.get_containers_by_entity_id = AsyncMock(return_value=containers)

        result = await async_persistence.get_containers_by_entity_id(entity_id)

        assert isinstance(result, list)
        assert len(result) == 1
        async_persistence._container_repo.get_containers_by_entity_id.assert_called_once_with(entity_id)

    @pytest.mark.asyncio
    async def test_update_container(self, async_persistence, sample_container_data):
        """Test updating a container."""
        container_id = uuid.UUID(sample_container_data["container_id"])
        updated_data = {**sample_container_data, "lock_state": "locked"}
        # Mock the repository update method
        async_persistence._container_repo.update_container = AsyncMock(return_value=updated_data)

        result = await async_persistence.update_container(container_id, lock_state="locked")

        assert result is not None
        assert result["lock_state"] == "locked"
        async_persistence._container_repo.update_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_decayed_containers(self, async_persistence, sample_container_data):
        """Test getting decayed containers."""
        current_time = datetime.now(UTC)
        decayed_containers = [sample_container_data]
        # Mock the repository get method
        async_persistence._container_repo.get_decayed_containers = AsyncMock(return_value=decayed_containers)

        result = await async_persistence.get_decayed_containers(current_time)

        assert isinstance(result, list)
        assert len(result) == 1
        async_persistence._container_repo.get_decayed_containers.assert_called_once_with(current_time)

    @pytest.mark.asyncio
    async def test_delete_container(self, async_persistence):
        """Test deleting a container."""
        container_id = uuid4()
        # Mock the repository delete method
        async_persistence._container_repo.delete_container = AsyncMock(return_value=True)

        result = await async_persistence.delete_container(container_id)

        assert result is True
        async_persistence._container_repo.delete_container.assert_called_once_with(container_id)
