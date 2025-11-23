"""
Tests for environmental container loading from JSON and PostgreSQL.

As documented in the restricted archives of Miskatonic University, environmental
container integration requires careful testing to ensure proper loading from
JSON definitions into PostgreSQL and subsequent retrieval.
"""

from __future__ import annotations

import uuid
from unittest.mock import MagicMock

import pytest

from server.models.container import ContainerLockState, ContainerSourceType
from server.services.environmental_container_loader import EnvironmentalContainerLoader


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def sample_room_id():
    """Return a sample room ID."""
    return "earth_arkhamcity_sanitarium_room_foyer_001"


@pytest.fixture
def sample_room_json_with_container(sample_room_id):
    """Create a sample room JSON with container definition."""
    return {
        "id": sample_room_id,
        "name": "Main Foyer",
        "description": "A grand entrance hall.",
        "plane": "earth",
        "zone": "arkhamcity",
        "sub_zone": "sanitarium",
        "environment": "indoors",
        "exits": {
            "east": "earth_arkhamcity_sanitarium_room_hallway_001",
        },
        "container": {
            "enabled": True,
            "capacity_slots": 8,
            "lock_state": "locked",
            "key_item_id": "arkham_library_key",
            "weight_limit": 50,
            "allowed_roles": ["admin", "librarian"],
        },
    }


@pytest.fixture
def sample_room_json_without_container(sample_room_id):
    """Create a sample room JSON without container definition."""
    return {
        "id": sample_room_id,
        "name": "Main Foyer",
        "description": "A grand entrance hall.",
        "plane": "earth",
        "zone": "arkhamcity",
        "sub_zone": "sanitarium",
        "environment": "indoors",
        "exits": {
            "east": "earth_arkhamcity_sanitarium_room_hallway_001",
        },
    }


class TestContainerLoadingFromJSON:
    """Test loading containers from room JSON definitions."""

    def test_load_container_from_room_json(self, mock_persistence, sample_room_json_with_container, sample_room_id):
        """Test loading a container from room JSON definition."""
        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        container = loader.load_container_from_room_json(sample_room_json_with_container, sample_room_id)

        assert container is not None
        assert container.source_type == ContainerSourceType.ENVIRONMENT
        assert container.room_id == sample_room_id
        assert container.capacity_slots == 8
        assert container.lock_state == ContainerLockState.LOCKED
        assert container.weight_limit == 50
        assert container.allowed_roles == ["admin", "librarian"]
        assert container.metadata.get("key_item_id") == "arkham_library_key"

    def test_load_container_from_room_json_minimal(self, mock_persistence, sample_room_id):
        """Test loading a container with minimal configuration."""
        room_json = {
            "id": sample_room_id,
            "name": "Test Room",
            "description": "A test room.",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "test",
            "exits": {},
            "container": {
                "enabled": True,
            },
        }

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        container = loader.load_container_from_room_json(room_json, sample_room_id)

        assert container is not None
        assert container.source_type == ContainerSourceType.ENVIRONMENT
        assert container.room_id == sample_room_id
        assert container.capacity_slots == 20  # Default
        assert container.lock_state == ContainerLockState.UNLOCKED  # Default

    def test_load_container_disabled(self, mock_persistence, sample_room_id):
        """Test that disabled containers are not loaded."""
        room_json = {
            "id": sample_room_id,
            "name": "Test Room",
            "description": "A test room.",
            "plane": "earth",
            "zone": "arkhamcity",
            "sub_zone": "test",
            "exits": {},
            "container": {
                "enabled": False,
            },
        }

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        container = loader.load_container_from_room_json(room_json, sample_room_id)

        assert container is None

    def test_load_container_missing_block(self, mock_persistence, sample_room_json_without_container, sample_room_id):
        """Test that rooms without container blocks return None."""
        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        container = loader.load_container_from_room_json(sample_room_json_without_container, sample_room_id)

        assert container is None


class TestContainerMigrationToPostgreSQL:
    """Test migrating containers from JSON to PostgreSQL."""

    def test_migrate_room_container_to_postgresql(
        self, mock_persistence, sample_room_json_with_container, sample_room_id
    ):
        """Test migrating a container from room JSON to PostgreSQL."""
        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        # Mock container creation
        mock_persistence.create_container.return_value = {
            "container_instance_id": str(uuid.uuid4()),
        }

        container_id = loader.migrate_room_container_to_postgresql(sample_room_json_with_container, sample_room_id)

        assert container_id is not None
        mock_persistence.create_container.assert_called_once()

        # Verify call arguments
        call_args = mock_persistence.create_container.call_args
        assert call_args.kwargs["source_type"] == "environment"
        assert call_args.kwargs["room_id"] == sample_room_id
        assert call_args.kwargs["capacity_slots"] == 8
        assert call_args.kwargs["lock_state"] == "locked"

    def test_migrate_room_container_already_exists(
        self, mock_persistence, sample_room_json_with_container, sample_room_id
    ):
        """Test that existing containers are not recreated."""
        # Mock existing container
        existing_container_id = uuid.uuid4()
        mock_persistence.get_containers_by_room_id.return_value = [
            {
                "container_instance_id": str(existing_container_id),
                "source_type": "environment",
                "room_id": sample_room_id,
            },
        ]

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        container_id = loader.migrate_room_container_to_postgresql(sample_room_json_with_container, sample_room_id)

        assert container_id == existing_container_id
        # Should not create a new container
        mock_persistence.create_container.assert_not_called()

    def test_migrate_room_without_container(self, mock_persistence, sample_room_json_without_container, sample_room_id):
        """Test migrating a room without a container."""
        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        container_id = loader.migrate_room_container_to_postgresql(sample_room_json_without_container, sample_room_id)

        assert container_id is None
        mock_persistence.create_container.assert_not_called()


class TestContainerLoadingFromPostgreSQL:
    """Test loading containers from PostgreSQL when loading rooms."""

    def test_load_containers_for_room(self, mock_persistence, sample_room_id):
        """Test loading containers for a room from PostgreSQL."""
        # Mock container data
        container_data = {
            "container_instance_id": str(uuid.uuid4()),
            "source_type": "environment",
            "room_id": sample_room_id,
            "capacity_slots": 8,
            "lock_state": "locked",
            "items_json": [],
            "metadata_json": {"key_item_id": "arkham_library_key"},
        }

        mock_persistence.get_containers_by_room_id.return_value = [container_data]

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        containers = loader.load_containers_for_room(sample_room_id)

        assert len(containers) == 1
        assert containers[0].source_type == ContainerSourceType.ENVIRONMENT
        assert containers[0].room_id == sample_room_id

    def test_load_containers_for_room_none_found(self, mock_persistence, sample_room_id):
        """Test loading containers when none exist."""
        mock_persistence.get_containers_by_room_id.return_value = []

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        containers = loader.load_containers_for_room(sample_room_id)

        assert len(containers) == 0

    def test_load_containers_for_room_multiple(self, mock_persistence, sample_room_id):
        """Test loading multiple containers for a room."""
        container_data_1 = {
            "container_instance_id": str(uuid.uuid4()),
            "source_type": "environment",
            "room_id": sample_room_id,
            "capacity_slots": 8,
            "lock_state": "unlocked",
            "items_json": [],
            "metadata_json": {},
        }

        container_data_2 = {
            "container_instance_id": str(uuid.uuid4()),
            "source_type": "environment",
            "room_id": sample_room_id,
            "capacity_slots": 12,
            "lock_state": "locked",
            "items_json": [],
            "metadata_json": {},
        }

        mock_persistence.get_containers_by_room_id.return_value = [container_data_1, container_data_2]

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        containers = loader.load_containers_for_room(sample_room_id)

        assert len(containers) == 2


class TestRoomContainerIntegration:
    """Test integration of containers with room loading."""

    def test_room_with_container_includes_containers(self, mock_persistence, sample_room_id):
        """Test that rooms loaded from database include their containers."""
        # Mock container data
        container_data = {
            "container_instance_id": str(uuid.uuid4()),
            "source_type": "environment",
            "room_id": sample_room_id,
            "capacity_slots": 8,
            "lock_state": "unlocked",
            "items_json": [],
            "metadata_json": {},
        }

        mock_persistence.get_containers_by_room_id.return_value = [container_data]

        loader = EnvironmentalContainerLoader(persistence=mock_persistence)

        # Load containers for room
        containers = loader.load_containers_for_room(sample_room_id)

        # Verify containers are loaded
        assert len(containers) == 1
        assert containers[0].room_id == sample_room_id
