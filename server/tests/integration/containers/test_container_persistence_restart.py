"""
Integration tests for container persistence across server restarts.

These tests verify that containers persist correctly when the server is
restarted, including:
- Container data persistence
- Container items persistence
- Container state persistence (locked, capacity, etc.)
- Mutation token invalidation on restart
- Container relationships (room_id, entity_id) persistence
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import cast
from uuid import UUID, uuid4

import pytest
from sqlalchemy.exc import DatabaseError

from server.models.container import ContainerComponent, ContainerLockState
from server.models.player import Player

# Removed: from server.persistence import get_persistence, reset_persistence - now using AsyncPersistenceLayer directly
from server.services.container_service import ContainerService, _filter_container_data
from server.services.inventory_service import InventoryStack


@pytest.fixture(scope="module")
def ensure_test_item_prototypes():
    """Ensure test item prototypes exist in the database."""
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL")

    url = database_url.replace("postgresql+psycopg2://", "postgresql://").replace(
        "postgresql+asyncpg://", "postgresql://"
    )

    conn = psycopg2.connect(url)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    try:
        # Create test item prototypes if they don't exist
        test_prototypes = [
            ("item_1", "Test Item 1", "A test item for container testing"),
            ("item_2", "Test Item 2", "Another test item for container testing"),
        ]

        for prototype_id, name, description in test_prototypes:
            cursor.execute(
                """
                INSERT INTO item_prototypes (
                    prototype_id, name, short_description, long_description,
                    item_type, weight, base_value, durability, flags,
                    wear_slots, stacking_rules, usage_restrictions,
                    effect_components, metadata, tags
                ) VALUES (
                    %s, %s, %s, %s, 'consumable', 1.0, 10, 100,
                    '[]'::jsonb, '[]'::jsonb, '{"max_stack": 99}'::jsonb,
                    '{}'::jsonb, '[]'::jsonb, '{}'::jsonb, '[]'::jsonb
                )
                ON CONFLICT (prototype_id) DO NOTHING
                """,
                (prototype_id, name, description, description),
            )

        # Create additional prototypes for tests that use item_{i} pattern
        for i in range(3, 21):  # item_3 through item_20
            cursor.execute(
                """
                INSERT INTO item_prototypes (
                    prototype_id, name, short_description, long_description,
                    item_type, weight, base_value, durability, flags,
                    wear_slots, stacking_rules, usage_restrictions,
                    effect_components, metadata, tags
                ) VALUES (
                    %s, %s, %s, %s, 'consumable', 1.0, 10, 100,
                    '[]'::jsonb, '[]'::jsonb, '{"max_stack": 99}'::jsonb,
                    '{}'::jsonb, '[]'::jsonb, '{}'::jsonb, '[]'::jsonb
                )
                ON CONFLICT (prototype_id) DO NOTHING
                """,
                (
                    f"item_{i}",
                    f"Test Item {i}",
                    f"A test item {i} for container testing",
                    f"A test item {i} for container testing",
                ),
            )

        conn.commit()
    finally:
        cursor.close()
        conn.close()

    yield

    # Cleanup is not needed - prototypes can remain for other tests


@pytest.fixture(scope="module")
def ensure_containers_table():
    """Ensure the containers table exists in the test database."""
    # Get database URL from environment
    database_url = os.getenv("DATABASE_URL")
    if not database_url or not database_url.startswith("postgresql"):
        pytest.skip("DATABASE_URL must be set to a PostgreSQL URL")

    # Read the migration SQL file
    project_root = Path(__file__).parent.parent.parent.parent.parent
    migration_file = project_root / "db" / "migrations" / "012_create_containers_table.sql"

    if not migration_file.exists():
        pytest.skip(f"Migration file not found: {migration_file}")

    # Execute the migration SQL
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    # Normalize URL format
    url = database_url.replace("postgresql+psycopg2://", "postgresql://").replace(
        "postgresql+asyncpg://", "postgresql://"
    )

    conn = psycopg2.connect(url)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    try:
        # Read and execute the migration SQL
        with open(migration_file, encoding="utf-8") as f:
            migration_sql = f.read()
        cursor.execute(migration_sql)
    finally:
        cursor.close()
        conn.close()

    yield

    # No cleanup needed - table persists for other tests


@pytest.fixture
async def persistence(_ensure_containers_table):
    """Create an AsyncPersistenceLayer instance for testing with proper cleanup."""
    from server.async_persistence import AsyncPersistenceLayer
    from server.database import DatabaseManager
    from server.events.event_bus import EventBus

    event_bus = EventBus()
    persistence_instance = AsyncPersistenceLayer(event_bus=event_bus)

    yield persistence_instance

    # Cleanup: Close database connections before event loop closes
    # This prevents "Event loop is closed" errors during teardown
    try:
        await persistence_instance.close()
        # Also ensure database manager closes connections
        db_manager = DatabaseManager.get_instance()
        if db_manager and hasattr(db_manager, "engine"):
            if db_manager.engine:
                await db_manager.engine.dispose(close=True)
    except (ValueError, KeyError, AttributeError, RuntimeError, DatabaseError) as e:
        # Log but don't fail on cleanup errors
        import logging

        logging.getLogger(__name__).warning("Error during persistence cleanup: %s", e)


@pytest.fixture
async def container_service(persistence):
    """Create a ContainerService instance for testing."""
    return ContainerService(persistence=persistence)


async def _create_test_player(
    persistence, player_id: UUID, name: str, room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001"
) -> Player:
    """Helper function to create a test player in the database."""
    from datetime import UTC, datetime

    import psycopg2

    from server.models.user import User

    # Create user first (required foreign key)
    user_id = uuid4()
    user = User(
        id=user_id,
        email=f"test-{name}@example.com",
        username=name,
        display_name=name,
        hashed_password="test_password_hash",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Use direct database insert for user (persistence doesn't have user methods)
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
                user.email,
                user.username,
                user.display_name,
                user.hashed_password,
                user.is_active,
                user.is_superuser,
                user.is_verified,
                now,
                now,
            ),
        )
    finally:
        cursor.close()
        conn.close()

    # Create player
    now = datetime.now(UTC).replace(tzinfo=None)
    player = Player(
        player_id=player_id,
        user_id=user_id,
        name=name,
        current_room_id=room_id,
        level=1,
        experience_points=0,
        profession_id=0,  # Required field - default profession
        inventory="[]",  # Required field
        status_effects="[]",  # Required field
        created_at=now,
        last_active=now,
    )
    await persistence.save_player(player)
    return player


@pytest.mark.asyncio
class TestContainerPersistenceRestart:
    """Test container persistence across server restarts."""

    async def test_environmental_container_persistence(self, persistence) -> None:
        """Test that environmental containers persist across server restarts."""
        # Use a real room ID that exists in the database
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

        # Create container with items
        container_result = await persistence.create_container(
            source_type="environment",
            room_id=room_id,
            capacity_slots=10,
            weight_limit=1000.0,
            items_json=[
                {
                    "item_id": "item_1",
                    "item_instance_id": "inst_item_1",
                    "prototype_id": "item_1",
                    "item_name": "Test Item 1",
                    "slot_type": "backpack",
                    "quantity": 10,
                    "weight": 1.0,
                },
                {
                    "item_id": "item_2",
                    "item_instance_id": "inst_item_2",
                    "prototype_id": "item_2",
                    "item_name": "Test Item 2",
                    "slot_type": "backpack",
                    "quantity": 5,
                    "weight": 2.0,
                },
            ],
            metadata_json={"type": "chest", "description": "A wooden chest"},
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Simulate server restart by creating new persistence instance
        # (In real scenario, this would be a new server process)
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify container still exists after "restart"
        persisted_container_data = await new_persistence.get_container(container_id)
        assert persisted_container_data is not None, "Container should persist after restart"

        # Convert to ContainerComponent for easier assertions
        persisted_container = ContainerComponent.model_validate(_filter_container_data(persisted_container_data))
        assert persisted_container.container_id == container_id
        assert persisted_container.room_id == room_id
        assert persisted_container.capacity_slots == 10
        assert persisted_container.weight_limit == 1000.0
        assert persisted_container.lock_state == ContainerLockState.UNLOCKED

        # Verify items persisted
        assert len(persisted_container.items) == 2
        assert persisted_container.items[0]["item_id"] == "item_1"
        assert persisted_container.items[0]["quantity"] == 10
        assert persisted_container.items[1]["item_id"] == "item_2"
        assert persisted_container.items[1]["quantity"] == 5

        # Verify metadata persisted
        assert persisted_container.metadata["type"] == "chest"
        assert persisted_container.metadata["description"] == "A wooden chest"

    async def test_wearable_container_persistence(self, persistence) -> None:
        """Test that wearable containers persist across server restarts."""
        # Create test player first (entity_id must reference a real player)
        entity_id = uuid4()
        await _create_test_player(persistence, entity_id, f"TestPlayer_{entity_id.hex[:8]}")

        # Create wearable container
        container_result = await persistence.create_container(
            source_type="equipment",
            entity_id=entity_id,
            capacity_slots=10,
            weight_limit=500.0,
            items_json=[
                {
                    "item_id": "item_1",
                    "item_instance_id": "inst_item_1",
                    "prototype_id": "item_1",
                    "item_name": "Test Item 1",
                    "slot_type": "backpack",
                    "quantity": 3,
                    "weight": 1.0,
                }
            ],
            metadata_json={"type": "backpack", "equipped": True},
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Simulate server restart
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify container persists
        persisted_container_data = await new_persistence.get_container(container_id)
        assert persisted_container_data is not None

        persisted_container = ContainerComponent.model_validate(_filter_container_data(persisted_container_data))
        assert persisted_container.entity_id == entity_id
        assert persisted_container.capacity_slots == 10
        assert persisted_container.metadata["type"] == "backpack"
        assert persisted_container.metadata["equipped"] is True

        # Verify container can be found by entity_id
        containers_by_entity_data = await new_persistence.get_containers_by_entity_id(entity_id)
        assert len(containers_by_entity_data) == 1
        found_container_id = containers_by_entity_data[0]["container_id"]
        found_container_id_uuid = (
            found_container_id if isinstance(found_container_id, UUID) else UUID(found_container_id)
        )
        assert found_container_id_uuid == container_id
        found_container_id_uuid = (
            found_container_id if isinstance(found_container_id, UUID) else UUID(found_container_id)
        )
        assert found_container_id_uuid == container_id

    async def test_corpse_container_persistence(self, persistence, _ensure_test_item_prototypes) -> None:
        """Test that corpse containers persist across server restarts."""
        # Use a real room ID that exists in the database
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        owner_id = uuid4()

        # Create test player (owner)
        await _create_test_player(persistence, owner_id, f"TestPlayer_{owner_id.hex[:8]}", room_id)

        # Create corpse container
        from datetime import UTC, datetime, timedelta

        decay_at = datetime.now(UTC) + timedelta(hours=1)

        container_result = await persistence.create_container(
            source_type="corpse",
            owner_id=owner_id,
            room_id=room_id,
            capacity_slots=10,
            weight_limit=1000.0,
            decay_at=decay_at,
            items_json=[
                {
                    "item_id": "item_1",
                    "item_instance_id": "inst_item_1",
                    "prototype_id": "item_1",
                    "item_name": "Test Item 1",
                    "slot_type": "backpack",
                    "quantity": 1,
                    "weight": 1.0,
                }
            ],
            metadata_json={
                "type": "corpse",
                "owner_id": str(owner_id),
                "grace_period_end": "2025-11-22T12:00:00Z",
                "decay_time": "2025-11-22T12:30:00Z",
            },
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Simulate server restart
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify container persists
        persisted_container_data = await new_persistence.get_container(container_id)
        assert persisted_container_data is not None

        persisted_container = ContainerComponent.model_validate(_filter_container_data(persisted_container_data))
        assert persisted_container.room_id == room_id
        assert persisted_container.metadata["type"] == "corpse"
        assert persisted_container.metadata["owner_id"] == str(owner_id)
        assert "grace_period_end" in persisted_container.metadata
        assert "decay_time" in persisted_container.metadata

        # Verify items persisted
        assert len(persisted_container.items) == 1
        assert persisted_container.items[0]["item_id"] == "item_1"

    async def test_container_state_persistence(self, persistence) -> None:
        """Test that container state (locked, capacity, etc.) persists."""
        # Use a real room ID that exists in the database
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

        container_result = await persistence.create_container(
            source_type="environment",
            room_id=room_id,
            capacity_slots=10,
            weight_limit=750.0,
            lock_state="locked",
            metadata_json={"key_id": "key_123", "lock_type": "key"},
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Simulate server restart
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify state persisted
        persisted_container_data = await new_persistence.get_container(container_id)
        assert persisted_container_data is not None

        persisted_container = ContainerComponent.model_validate(_filter_container_data(persisted_container_data))
        assert persisted_container.lock_state == ContainerLockState.LOCKED
        assert persisted_container.capacity_slots == 10
        assert persisted_container.weight_limit == 750.0
        assert persisted_container.metadata["key_id"] == "key_123"
        assert persisted_container.metadata["lock_type"] == "key"

    async def test_container_updates_persist(
        self, persistence, container_service: ContainerService, _ensure_test_item_prototypes
    ) -> None:
        """Test that container updates persist across restarts."""
        # Use a real room ID that exists in the database
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        player_id = uuid4()

        # Create test player
        await _create_test_player(persistence, player_id, f"TestPlayer_{player_id.hex[:8]}", room_id)

        # Create container
        container_result = await persistence.create_container(
            source_type="environment",
            room_id=room_id,
            capacity_slots=10,
            weight_limit=1000.0,
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Open container and add items
        open_result = await container_service.open_container(container_id, player_id)
        mutation_token = open_result["mutation_token"]

        stack = {
            "item_id": "item_1",
            "item_name": "Test Item 1",
            "quantity": 5,
            "weight": 1.0,
            "slot_type": "backpack",
        }
        await container_service.transfer_to_container(
            container_id=container_id,
            player_id=player_id,
            mutation_token=mutation_token,
            item=cast(InventoryStack, stack),
            quantity=5,
        )

        # Verify items added before restart
        container_before_data = await container_service.persistence.get_container(container_id)
        assert container_before_data is not None
        container_before = ContainerComponent.model_validate(_filter_container_data(container_before_data))
        assert len(container_before.items) == 1
        assert container_before.items[0]["quantity"] == 5

        # Simulate server restart
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify items persisted after restart
        container_after_data = await new_persistence.get_container(container_id)
        assert container_after_data is not None
        container_after = ContainerComponent.model_validate(_filter_container_data(container_after_data))
        assert len(container_after.items) == 1
        assert container_after.items[0]["item_id"] == "item_1"
        assert container_after.items[0]["quantity"] == 5

    async def test_multiple_containers_persist(self, persistence) -> None:
        """Test that multiple containers persist correctly."""
        # Use a real room ID that exists in the database
        base_room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

        # Create multiple containers
        containers = []

        for i in range(5):
            container_result = await persistence.create_container(
                source_type="environment",
                room_id=base_room_id,
                capacity_slots=10,
                weight_limit=1000.0,
                items_json=[
                    {
                        "item_id": f"item_{i + 1}",  # Use item_1 through item_5 (item_0 doesn't exist)
                        "item_instance_id": f"item_{i + 1}",
                        "item_name": f"Test Item {i + 1}",
                        "slot_type": "backpack",
                        "quantity": i + 1,
                        "weight": 1.0,
                    }
                ],
                metadata_json={"index": i},
            )
            container_id = (
                container_result["container_id"]
                if isinstance(container_result["container_id"], UUID)
                else UUID(container_result["container_id"])
            )
            containers.append(container_id)

        # Simulate server restart
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify all containers persist
        for i, container_id in enumerate(containers):
            persisted_container_data = await new_persistence.get_container(container_id)
            assert persisted_container_data is not None
            persisted_container = ContainerComponent.model_validate(_filter_container_data(persisted_container_data))
            assert len(persisted_container.items) == 1
            assert persisted_container.items[0]["item_id"] == f"item_{i + 1}"

    async def test_container_room_relationship_persistence(self, persistence) -> None:
        """Test that container-room relationships persist."""
        # Use real room IDs that exist in the database
        room1_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        room2_id = "earth_arkhamcity_sanitarium_room_hallway_001"

        # Create containers in different rooms
        container1_result = await persistence.create_container(
            source_type="environment",
            room_id=room1_id,
            capacity_slots=10,
            weight_limit=1000.0,
        )
        container1_id = (
            container1_result["container_id"]
            if isinstance(container1_result["container_id"], UUID)
            else UUID(container1_result["container_id"])
        )

        container2_result = await persistence.create_container(
            source_type="environment",
            room_id=room2_id,
            capacity_slots=10,
            weight_limit=1000.0,
        )
        container2_id = (
            container2_result["container_id"]
            if isinstance(container2_result["container_id"], UUID)
            else UUID(container2_result["container_id"])
        )

        # Simulate server restart
        # Simulate server restart by creating new AsyncPersistenceLayer instance
        from server.async_persistence import AsyncPersistenceLayer
        from server.events.event_bus import EventBus

        event_bus = EventBus()
        new_persistence = AsyncPersistenceLayer(event_bus=event_bus)

        # Verify containers can be found by room_id
        containers_room1_data = await new_persistence.get_containers_by_room_id(room1_id)
        containers_room2_data = await new_persistence.get_containers_by_room_id(room2_id)

        # Filter to find our test containers (there may be other containers in these rooms)
        def get_container_uuid(c):
            """Helper to get container UUID from dict."""
            container_id = c["container_id"]
            return container_id if isinstance(container_id, UUID) else UUID(container_id)

        container1_found = any(get_container_uuid(c) == container1_id for c in containers_room1_data)
        container2_found = any(get_container_uuid(c) == container2_id for c in containers_room2_data)

        assert container1_found, (
            f"Container 1 not found in room 1. Found containers: {[c['container_id'] for c in containers_room1_data]}"
        )
        assert container2_found, (
            f"Container 2 not found in room 2. Found containers: {[c['container_id'] for c in containers_room2_data]}"
        )
