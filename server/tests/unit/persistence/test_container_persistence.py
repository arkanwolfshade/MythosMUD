"""
Tests for container persistence operations.

As documented in the restricted archives of Miskatonic University, container
persistence requires thorough testing to ensure proper storage and retrieval
of investigator artifacts.
"""

from __future__ import annotations

import uuid
from datetime import UTC, datetime, timedelta

import pytest

from server.exceptions import ValidationError
from server.logging.enhanced_logging_config import get_logger
from server.persistence import get_persistence

logger = get_logger(__name__)


@pytest.fixture
def persistence():
    """Create a persistence layer instance for testing."""
    return get_persistence()


@pytest.fixture
def sample_player_id() -> uuid.UUID:
    """Generate a sample player UUID for testing."""
    return uuid.uuid4()


@pytest.fixture
def sample_room_id() -> str:
    """Return a sample room ID for testing."""
    return "earth_arkhamcity_sanitarium_room_foyer_001"


class TestCreateContainer:
    """Test container creation operations."""

    def test_create_environment_container(self, persistence, sample_room_id: str):
        """Test creating an environmental container."""
        container = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )

        assert container is not None
        assert container["source_type"] == "environment"
        assert container["room_id"] == sample_room_id
        assert container["capacity_slots"] == 8
        assert container["lock_state"] == "unlocked"
        assert container["items_json"] == []
        assert "container_instance_id" in container

    def test_create_corpse_container(self, persistence, sample_player_id: uuid.UUID, sample_room_id: str):
        """Test creating a corpse container with decay timestamp."""
        decay_at = datetime.now(UTC) + timedelta(hours=1)

        container = persistence.create_container(
            source_type="corpse",
            owner_id=sample_player_id,
            room_id=sample_room_id,
            capacity_slots=20,
            decay_at=decay_at,
        )

        assert container is not None
        assert container["source_type"] == "corpse"
        assert container["owner_id"] == str(sample_player_id)
        assert container["room_id"] == sample_room_id
        assert container["decay_at"] is not None

    def test_create_equipment_container(self, persistence, sample_player_id: uuid.UUID):
        """Test creating a wearable equipment container."""
        container = persistence.create_container(
            source_type="equipment",
            entity_id=sample_player_id,
            capacity_slots=10,
        )

        assert container is not None
        assert container["source_type"] == "equipment"
        assert container["entity_id"] == str(sample_player_id)
        assert container["room_id"] is None

    def test_create_container_with_items(self, persistence, sample_room_id: str):
        """Test creating a container with initial items."""
        items = [
            {
                "item_id": "elder_sign",
                "item_name": "Elder Sign",
                "slot_type": "backpack",
                "quantity": 1,
            },
            {
                "item_id": "tome_of_forbidden_knowledge",
                "item_name": "Tome of Forbidden Knowledge",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        container = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
            items_json=items,
        )

        assert container is not None
        assert len(container["items_json"]) == 2
        assert container["items_json"][0]["item_id"] == "elder_sign"
        assert container["items_json"][1]["item_id"] == "tome_of_forbidden_knowledge"

    def test_create_container_invalid_source_type(self, persistence):
        """Test that invalid source_type is rejected."""
        with pytest.raises(ValidationError):
            persistence.create_container(
                source_type="invalid_type",
                room_id="test_room",
                capacity_slots=8,
            )

    def test_create_container_invalid_capacity(self, persistence):
        """Test that invalid capacity_slots is rejected."""
        with pytest.raises(ValidationError):
            persistence.create_container(
                source_type="environment",
                room_id="test_room",
                capacity_slots=25,  # Too high
            )

        with pytest.raises(ValidationError):
            persistence.create_container(
                source_type="environment",
                room_id="test_room",
                capacity_slots=0,  # Too low
            )

    def test_create_container_invalid_lock_state(self, persistence):
        """Test that invalid lock_state is rejected."""
        with pytest.raises(ValidationError):
            persistence.create_container(
                source_type="environment",
                room_id="test_room",
                capacity_slots=8,
                lock_state="invalid_state",
            )


class TestGetContainer:
    """Test container retrieval operations."""

    def test_get_container_by_id(self, persistence, sample_room_id: str):
        """Test retrieving a container by ID."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )
        container_id = uuid.UUID(created["container_instance_id"])

        # Retrieve container
        retrieved = persistence.get_container(container_id)

        assert retrieved is not None
        assert retrieved["container_instance_id"] == created["container_instance_id"]
        assert retrieved["source_type"] == "environment"
        assert retrieved["room_id"] == sample_room_id

    def test_get_nonexistent_container(self, persistence):
        """Test retrieving a non-existent container."""
        container_id = uuid.uuid4()
        retrieved = persistence.get_container(container_id)
        assert retrieved is None

    def test_get_containers_by_room_id(self, persistence, sample_room_id: str):
        """Test retrieving all containers in a room."""
        # Create multiple containers in the same room
        container1 = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )
        container2 = persistence.create_container(
            source_type="corpse",
            room_id=sample_room_id,
            capacity_slots=20,
        )

        # Retrieve containers
        containers = persistence.get_containers_by_room_id(sample_room_id)

        assert len(containers) >= 2
        container_ids = {c["container_instance_id"] for c in containers}
        assert container1["container_instance_id"] in container_ids
        assert container2["container_instance_id"] in container_ids

    def test_get_containers_by_entity_id(self, persistence, sample_player_id: uuid.UUID):
        """Test retrieving all containers owned by an entity."""
        # Create multiple containers for the same entity
        container1 = persistence.create_container(
            source_type="equipment",
            entity_id=sample_player_id,
            capacity_slots=10,
        )
        container2 = persistence.create_container(
            source_type="equipment",
            entity_id=sample_player_id,
            capacity_slots=15,
        )

        # Retrieve containers
        containers = persistence.get_containers_by_entity_id(sample_player_id)

        assert len(containers) >= 2
        container_ids = {c["container_instance_id"] for c in containers}
        assert container1["container_instance_id"] in container_ids
        assert container2["container_instance_id"] in container_ids


class TestUpdateContainer:
    """Test container update operations."""

    def test_update_container_items(self, persistence, sample_room_id: str):
        """Test updating container items."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )
        container_id = uuid.UUID(created["container_instance_id"])

        # Update items
        new_items = [
            {
                "item_id": "elder_sign",
                "item_name": "Elder Sign",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        updated = persistence.update_container(container_id, items_json=new_items)

        assert updated is not None
        assert len(updated["items_json"]) == 1
        assert updated["items_json"][0]["item_id"] == "elder_sign"

    def test_update_container_lock_state(self, persistence, sample_room_id: str):
        """Test updating container lock state."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state="unlocked",
        )
        container_id = uuid.UUID(created["container_instance_id"])

        # Update lock state
        updated = persistence.update_container(container_id, lock_state="locked")

        assert updated is not None
        assert updated["lock_state"] == "locked"

    def test_update_container_metadata(self, persistence, sample_room_id: str):
        """Test updating container metadata."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )
        container_id = uuid.UUID(created["container_instance_id"])

        # Update metadata
        new_metadata = {"key_item_id": "arkham_library_key", "requires_key": True}
        updated = persistence.update_container(container_id, metadata_json=new_metadata)

        assert updated is not None
        assert updated["metadata_json"]["key_item_id"] == "arkham_library_key"
        assert updated["metadata_json"]["requires_key"] is True

    def test_update_nonexistent_container(self, persistence):
        """Test updating a non-existent container."""
        container_id = uuid.uuid4()
        updated = persistence.update_container(container_id, lock_state="locked")
        assert updated is None

    def test_update_container_invalid_lock_state(self, persistence, sample_room_id: str):
        """Test that invalid lock_state is rejected during update."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )
        container_id = uuid.UUID(created["container_instance_id"])

        # Try to update with invalid lock state
        with pytest.raises(ValidationError):
            persistence.update_container(container_id, lock_state="invalid_state")


class TestDeleteContainer:
    """Test container deletion operations."""

    def test_delete_container(self, persistence, sample_room_id: str):
        """Test deleting a container."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
        )
        container_id = uuid.UUID(created["container_instance_id"])

        # Delete container
        deleted = persistence.delete_container(container_id)
        assert deleted is True

        # Verify container is gone
        retrieved = persistence.get_container(container_id)
        assert retrieved is None

    def test_delete_nonexistent_container(self, persistence):
        """Test deleting a non-existent container."""
        container_id = uuid.uuid4()
        deleted = persistence.delete_container(container_id)
        assert deleted is False
