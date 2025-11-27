"""
Tests for container persistence operations.

As documented in the restricted archives of Miskatonic University, container
persistence requires thorough testing to ensure proper storage and retrieval
of investigator artifacts.
"""

from __future__ import annotations

import uuid
from collections.abc import Iterator
from datetime import UTC, datetime, timedelta
from uuid import UUID

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
def sample_player_id(persistence) -> Iterator[uuid.UUID]:
    """Create a test player in the database and return its UUID."""
    import os
    from datetime import UTC, datetime

    import psycopg2

    from server.models.player import Player

    # Create a test user first
    user_id = uuid.uuid4()
    player_id = uuid.uuid4()

    # Create user using direct database connection with autocommit
    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL")

    url = database_url.replace("postgresql+psycopg2://", "postgresql://").replace(
        "postgresql+asyncpg://", "postgresql://"
    )
    conn = psycopg2.connect(url)
    conn.autocommit = True  # Enable autocommit for user creation
    cursor = conn.cursor()
    try:
        now = datetime.now(UTC).replace(tzinfo=None)
        cursor.execute(
            """
            INSERT INTO users (id, email, username, display_name, hashed_password, is_active, is_superuser, is_verified, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
            """,
            (
                str(user_id),
                f"test-{player_id}@example.com",
                f"testuser-{player_id}",
                f"Test User {player_id}",
                "hashed_password",
                True,
                False,
                True,
                now,
                now,
            ),
        )
    finally:
        cursor.close()
        conn.close()

    # Create player using persistence layer
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name=f"TestPlayer-{player_id}",
        current_room_id="earth_arkhamcity_sanitarium_room_foyer_001",
        level=1,
        experience_points=0,
        profession_id=0,
        inventory="[]",
        status_effects="[]",
        created_at=now,
        last_active=now,
    )
    persistence.save_player(player)

    yield player_id

    # Cleanup: delete test player and user
    try:
        persistence.delete_player(player_id)
        # Delete user using direct connection
        conn = psycopg2.connect(url)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (str(user_id),))
        cursor.close()
        conn.close()
    except Exception:
        pass  # Ignore cleanup errors


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
        assert container["items"] == []
        assert "container_id" in container

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
        # owner_id should be converted to string by to_dict()
        assert str(container["owner_id"]) == str(sample_player_id)
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
        # entity_id should be converted to string by to_dict()
        assert str(container["entity_id"]) == str(sample_player_id)
        assert container["room_id"] is None

    def test_create_container_with_items(self, persistence, sample_room_id: str):
        """Test creating a container with initial items."""
        # Use item prototype IDs that exist in the database
        # These must match actual prototype_ids from item_prototypes table
        items = [
            {
                "item_id": "equipment.accessory.phosphor_charm",
                "item_name": "Phosphor Charm",
                "slot_type": "backpack",
                "quantity": 1,
            },
            {
                "item_id": "equipment.off_hand.mirror_ward_tome",
                "item_name": "Mirror Ward Tome",
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
        assert len(container["items"]) == 2
        assert container["items"][0]["item_id"] == "equipment.accessory.phosphor_charm"
        assert container["items"][1]["item_id"] == "equipment.off_hand.mirror_ward_tome"

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
        # container_id should be a string from to_dict(), but handle both cases
        container_id = (
            created["container_id"]
            if isinstance(created["container_id"], uuid.UUID)
            else uuid.UUID(created["container_id"])
        )

        # Retrieve container
        retrieved = persistence.get_container(container_id)

        assert retrieved is not None
        assert retrieved["container_id"] == created["container_id"]
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
        # Convert container_ids to strings for comparison (to_dict() returns strings)
        container_ids = {
            str(c["container_id"]) if isinstance(c["container_id"], UUID) else c["container_id"] for c in containers
        }
        container1_id = (
            str(container1["container_id"])
            if isinstance(container1["container_id"], UUID)
            else container1["container_id"]
        )
        container2_id = (
            str(container2["container_id"])
            if isinstance(container2["container_id"], UUID)
            else container2["container_id"]
        )
        assert container1_id in container_ids
        assert container2_id in container_ids

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
        # Convert container_ids to strings for comparison (to_dict() returns strings)
        container_ids = {
            str(c["container_id"]) if isinstance(c["container_id"], UUID) else c["container_id"] for c in containers
        }
        container1_id = (
            str(container1["container_id"])
            if isinstance(container1["container_id"], UUID)
            else container1["container_id"]
        )
        container2_id = (
            str(container2["container_id"])
            if isinstance(container2["container_id"], UUID)
            else container2["container_id"]
        )
        assert container1_id in container_ids
        assert container2_id in container_ids


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
        # container_id should be a string from to_dict(), but handle both cases
        container_id = (
            created["container_id"]
            if isinstance(created["container_id"], uuid.UUID)
            else uuid.UUID(created["container_id"])
        )

        # Update items - use item prototype ID that exists in database
        new_items = [
            {
                "item_id": "equipment.accessory.phosphor_charm",
                "item_instance_id": "equipment.accessory.phosphor_charm",  # Add item_instance_id for foreign key
                "item_name": "Phosphor Charm",
                "slot_type": "backpack",
                "quantity": 1,
            },
        ]

        updated = persistence.update_container(container_id, items_json=new_items)

        assert updated is not None
        assert len(updated["items"]) == 1
        assert updated["items"][0]["item_id"] == "equipment.accessory.phosphor_charm"

    def test_update_container_lock_state(self, persistence, sample_room_id: str):
        """Test updating container lock state."""
        # Create container
        created = persistence.create_container(
            source_type="environment",
            room_id=sample_room_id,
            capacity_slots=8,
            lock_state="unlocked",
        )
        # container_id should be a string from to_dict(), but handle both cases
        container_id = (
            created["container_id"]
            if isinstance(created["container_id"], uuid.UUID)
            else uuid.UUID(created["container_id"])
        )

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
        # container_id should be a string from to_dict(), but handle both cases
        container_id = (
            created["container_id"]
            if isinstance(created["container_id"], uuid.UUID)
            else uuid.UUID(created["container_id"])
        )

        # Update metadata
        new_metadata = {"key_item_id": "arkham_library_key", "requires_key": True}
        updated = persistence.update_container(container_id, metadata_json=new_metadata)

        assert updated is not None
        assert updated["metadata"]["key_item_id"] == "arkham_library_key"
        assert updated["metadata"]["requires_key"] is True

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
        # container_id should be a string from to_dict(), but handle both cases
        container_id = (
            created["container_id"]
            if isinstance(created["container_id"], uuid.UUID)
            else uuid.UUID(created["container_id"])
        )

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
        # container_id should be a string from to_dict(), but handle both cases
        container_id = (
            created["container_id"]
            if isinstance(created["container_id"], uuid.UUID)
            else uuid.UUID(created["container_id"])
        )

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
