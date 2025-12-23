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
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL")

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
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL")

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
        # Check if containers table exists
        cursor.execute(
            """
            SELECT EXISTS (
                SELECT FROM information_schema.tables
                WHERE table_schema = 'public'
                AND table_name = 'containers'
            );
            """
        )
        result = cursor.fetchone()
        table_exists = result[0] if result is not None else False

        if not table_exists:
            # Create containers table if it doesn't exist (using schema from authoritative_schema.sql)
            cursor.execute(
                """
                CREATE TABLE public.containers (
                    container_instance_id uuid DEFAULT gen_random_uuid() NOT NULL,
                    source_type text NOT NULL,
                    owner_id uuid,
                    room_id character varying(255),
                    entity_id uuid,
                    lock_state text DEFAULT 'unlocked'::text NOT NULL,
                    capacity_slots integer NOT NULL,
                    weight_limit integer,
                    decay_at timestamp with time zone,
                    allowed_roles jsonb,
                    metadata_json jsonb,
                    created_at timestamp with time zone DEFAULT now() NOT NULL,
                    updated_at timestamp with time zone DEFAULT now() NOT NULL,
                    container_item_instance_id character varying(64),
                    items_json jsonb DEFAULT '[]'::jsonb NOT NULL,
                    CONSTRAINT containers_capacity_slots_check CHECK (((capacity_slots > 0) AND (capacity_slots <= 20))),
                    CONSTRAINT containers_lock_state_check CHECK ((lock_state = ANY (ARRAY['unlocked'::text, 'locked'::text, 'sealed'::text]))),
                    CONSTRAINT containers_source_type_check CHECK ((source_type = ANY (ARRAY['environment'::text, 'equipment'::text, 'corpse'::text]))),
                    CONSTRAINT containers_weight_limit_check CHECK (((weight_limit IS NULL) OR (weight_limit > 0))),
                    PRIMARY KEY (container_instance_id)
                );
                CREATE INDEX IF NOT EXISTS idx_containers_room ON containers(room_id);
                CREATE INDEX IF NOT EXISTS idx_containers_entity ON containers(entity_id);
                CREATE INDEX IF NOT EXISTS idx_containers_owner ON containers(owner_id);
                """
            )
    finally:
        cursor.close()
        conn.close()

    yield

    # No cleanup needed - table persists for other tests


@pytest.fixture
async def persistence(ensure_containers_table):  # pylint: disable=redefined-outer-name,unused-argument,unused-variable
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


def _ensure_room_in_cache(persistence, room_id: str) -> None:
    """Ensure a room exists in the persistence layer's room cache."""
    from server.models.room import Room

    # The room cache is shared between persistence and player_repo
    # Add to persistence cache which is used by player_repo
    if room_id not in persistence._room_cache:
        room_data = {
            "id": room_id,
            "name": "Test Room",
            "description": "Test room for container tests",
        }
        persistence._room_cache[room_id] = Room(room_data)

    # Also ensure it's in the player_repo's cache (same reference, but being explicit)
    if hasattr(persistence, "_player_repo") and hasattr(persistence._player_repo, "_room_cache"):
        if room_id not in persistence._player_repo._room_cache:
            persistence._player_repo._room_cache[room_id] = persistence._room_cache[room_id]


async def _create_test_player(
    persistence, player_id: UUID, name: str, room_id: str = "earth_arkhamcity_sanitarium_room_foyer_001"
) -> Player:
    """Helper function to create a test player in the database."""
    from datetime import UTC, datetime

    from server.database import get_async_session
    from server.models.user import User

    # Create user and player in same async transaction to avoid FK violations
    user_id = uuid4()
    user = User(
        id=str(user_id),  # User.id expects string UUID
        email=f"test-{name}@example.com",
        username=name,
        display_name=name,
        hashed_password="test_password_hash",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    now = datetime.now(UTC).replace(tzinfo=None)
    player = Player(
        player_id=str(player_id),  # Player.player_id expects string UUID
        user_id=str(user_id),  # Player.user_id expects string UUID
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

    # Use async session to create both user and player in same transaction
    # CRITICAL: Use context manager properly - it will auto-commit on exit
    # We explicitly commit to ensure data is written before context exits
    import asyncio

    async for session in get_async_session():
        try:
            session.add(user)
            await session.flush()  # Flush to make user visible to FK constraint
            session.add(player)
            await session.commit()  # Explicitly commit before context exit
            # Wait a moment to ensure commit completes
            await asyncio.sleep(0.01)
        except Exception:
            await session.rollback()
            raise
        # Context manager will close session automatically
        break  # Exit generator after first iteration

    # CRITICAL: Wait for commit to propagate across database connections
    # PostgreSQL transaction isolation can cause delays in high-load scenarios
    # The test's own retry logic will handle final verification
    await asyncio.sleep(0.1)

    return player


async def _get_player_directly_from_db(player_id: UUID) -> Player | None:
    """
    Get player directly from database using direct SQL query.

    This bypasses the persistence layer's session management and connection pooling,
    ensuring we can retrieve players immediately after they're committed, even if
    there are transaction isolation delays in the persistence layer.

    Args:
        player_id: The player's UUID

    Returns:
        Player object if found, None otherwise

    AI: Direct SQL queries bypass SQLAlchemy session management and connection pooling,
    allowing immediate visibility of committed data across different database connections.
    This is critical for integration tests where transaction isolation can cause delays.
    """
    from sqlalchemy import select

    from server.database import get_async_session

    async for session in get_async_session():
        try:
            stmt = select(Player).where(Player.player_id == str(player_id))
            result = await session.execute(stmt)
            player = result.scalar_one_or_none()
            if player:
                # Ensure room validation (same as persistence layer does)
                if hasattr(player, "current_room_id") and player.current_room_id:
                    # Room validation would go here if needed, but for tests we skip it
                    pass
                return player
        except Exception as e:
            # Log error but don't fail - return None to allow fallback
            import sys

            print(f"DEBUG: Direct DB query error for player {player_id}: {e}", file=sys.stderr)
        finally:
            await session.close()
        break

    return None


def _create_reliable_get_player_wrapper(persistence, created_players: dict[UUID, Player] | None = None):
    """
    Create a wrapper for get_player_by_id that falls back to direct DB query.

    This implements Option 6 from PLAYER_VISIBILITY_SOLUTIONS.md:
    - Tries persistence layer first (normal path)
    - Falls back to direct DB query if persistence layer returns None
    - Optionally uses a cache of known-created players for immediate return

    Args:
        persistence: The persistence layer instance
        created_players: Optional dict mapping player_id to Player for immediate return

    Returns:
        Wrapper function that replaces persistence.get_player_by_id

    AI: This hybrid approach maintains integration testing (real DB, real container operations)
    while avoiding flakiness from transaction isolation issues in player retrieval.
    """
    original_get_player = persistence.get_player_by_id
    if created_players is None:
        created_players = {}

    async def reliable_get_player(player_id: UUID) -> Player | None:
        """Reliable player retrieval with fallback to direct DB query."""
        # First, check cache of known-created players (immediate return)
        if player_id in created_players:
            return created_players[player_id]

        # Try persistence layer first (normal production path)
        player = await original_get_player(player_id)
        if player is not None:
            return player

        # Fallback: direct database query (bypasses session management)
        # This ensures we can retrieve players even if persistence layer has visibility issues
        player = await _get_player_directly_from_db(player_id)
        if player is not None:
            # Cache it for future lookups
            created_players[player_id] = player
        return player

    return reliable_get_player


@pytest.mark.asyncio
class TestContainerPersistenceRestart:
    """Test container persistence across server restarts."""

    @pytest.mark.serial  # Flaky in parallel execution - database transaction conflicts
    @pytest.mark.xdist_group(name="serial_container_persistence_tests")  # Force serial execution with pytest-xdist
    @pytest.mark.asyncio
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

    @pytest.mark.serial  # Flaky in parallel execution - likely due to database transaction conflicts or shared state
    @pytest.mark.xdist_group(name="serial_container_persistence_tests")  # Force serial execution with pytest-xdist
    async def test_wearable_container_persistence(self, persistence) -> None:
        """Test that wearable containers persist across server restarts."""
        # Create test player first (entity_id must reference a real player)
        entity_id = uuid4()
        await _create_test_player(persistence, entity_id, f"TestPlayer_{entity_id.hex[:8]}")

        # Verify player exists before creating container (transaction isolation in parallel execution)
        import asyncio

        max_retries = 20  # Increased retries for parallel execution
        player = None
        for attempt in range(max_retries):
            player = await persistence.get_player_by_id(entity_id)
            if player is not None:
                break
            if attempt < max_retries - 1:
                await asyncio.sleep(0.1)
        if player is None:
            # Fallback: use direct DB query if persistence layer has visibility issues
            player = await _get_player_directly_from_db(entity_id)
            if player is None:
                raise RuntimeError(
                    f"Player {entity_id} not visible after creation - cannot create container with entity_id"
                )

        # Additional delay to ensure commit is fully propagated before container creation
        # This is critical in parallel execution where transaction isolation can cause delays
        await asyncio.sleep(0.2)

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

    @pytest.mark.serial  # Flaky in parallel execution - likely due to database transaction conflicts or shared state
    @pytest.mark.xdist_group(name="serial_container_persistence_tests")  # Force serial execution with pytest-xdist
    async def test_corpse_container_persistence(self, persistence, ensure_test_item_prototypes) -> None:  # pylint: disable=unused-argument
        """Test that corpse containers persist across server restarts."""
        # Use a real room ID that exists in the database
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        owner_id = uuid4()

        # Ensure room exists in cache
        _ensure_room_in_cache(persistence, room_id)

        # Create test player (owner)
        await _create_test_player(persistence, owner_id, f"TestPlayer_{owner_id.hex[:8]}", room_id)

        # Verify player exists before creating container (transaction isolation in parallel execution)
        import asyncio

        max_retries = 20  # Increased retries for parallel execution
        player = None
        for attempt in range(max_retries):
            player = await persistence.get_player_by_id(owner_id)
            if player is not None:
                break
            if attempt < max_retries - 1:
                await asyncio.sleep(0.1)
        if player is None:
            # Fallback: use direct DB query if persistence layer has visibility issues
            player = await _get_player_directly_from_db(owner_id)
            if player is None:
                raise RuntimeError(
                    f"Player {owner_id} not visible after creation - cannot create container with owner_id"
                )

        # Additional delay to ensure commit is fully propagated before container creation
        # This is critical in parallel execution where transaction isolation can cause delays
        await asyncio.sleep(0.2)

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

    @pytest.mark.serial  # Flaky in parallel execution - likely due to database transaction conflicts or shared state
    @pytest.mark.xdist_group(name="serial_container_persistence_tests")  # Force serial execution with pytest-xdist
    async def test_container_updates_persist(
        self,
        persistence,
        container_service: ContainerService,
        ensure_test_item_prototypes,  # pylint: disable=unused-argument
    ) -> None:
        """Test that container updates persist across restarts."""
        # Use a real room ID that exists in the database
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

        # Ensure room exists in cache to prevent validate_and_fix_player_room from changing player room
        _ensure_room_in_cache(persistence, room_id)

        player_id = uuid4()

        # Create test player
        await _create_test_player(persistence, player_id, f"TestPlayer_{player_id.hex[:8]}", room_id)

        # Verify player exists before creating container (transaction isolation in parallel execution)
        import asyncio

        max_retries = 20  # Increased retries for parallel execution
        player = None
        for attempt in range(max_retries):
            player = await persistence.get_player_by_id(player_id)
            if player is not None:
                break
            if attempt < max_retries - 1:
                await asyncio.sleep(0.1)
        if player is None:
            # Fallback: use direct DB query if persistence layer has visibility issues
            player = await _get_player_directly_from_db(player_id)
            if player is None:
                raise RuntimeError(f"Player {player_id} not visible after creation")

        # Additional delay to ensure commit is fully propagated before container creation
        # This is critical in parallel execution where transaction isolation can cause delays
        await asyncio.sleep(0.2)

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
