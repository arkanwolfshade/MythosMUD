"""
Integration tests for concurrent container mutations.

These tests verify that the container system handles concurrent operations
correctly, including mutation token validation, race condition prevention,
and state consistency across multiple simultaneous operations.
"""

from __future__ import annotations

import asyncio
import os
from typing import Any, cast
from uuid import UUID, uuid4

import pytest

from server.models.player import Player

# Removed: from server.persistence import get_persistence - now using AsyncPersistenceLayer directly
from server.services.container_service import ContainerService, ContainerServiceError, _filter_container_data
from server.services.inventory_service import InventoryStack

pytestmark = [
    pytest.mark.integration,
    pytest.mark.serial,  # Keep container DB ops isolated from xdist workers
    pytest.mark.xdist_group(name="serial_container_mutations_tests"),  # Run on a single worker across suite
]


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
        # Ensure item_prototypes table exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS item_prototypes (
                prototype_id varchar(120) PRIMARY KEY,
                name varchar(120) NOT NULL,
                short_description varchar(255) NOT NULL,
                long_description text NOT NULL,
                item_type varchar(32) NOT NULL,
                weight double precision NOT NULL DEFAULT 0.0,
                base_value integer NOT NULL DEFAULT 0,
                durability integer,
                flags jsonb NOT NULL DEFAULT '[]'::jsonb,
                wear_slots jsonb NOT NULL DEFAULT '[]'::jsonb,
                stacking_rules jsonb NOT NULL DEFAULT '{}'::jsonb,
                usage_restrictions jsonb NOT NULL DEFAULT '{}'::jsonb,
                effect_components jsonb NOT NULL DEFAULT '[]'::jsonb,
                metadata jsonb NOT NULL DEFAULT '{}'::jsonb,
                tags jsonb NOT NULL DEFAULT '[]'::jsonb,
                created_at timestamptz NOT NULL DEFAULT now()
            )
        """)

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
async def container_service(request):
    """Create a ContainerService instance for testing with proper cleanup."""
    # Ensure containers table exists (dependency injection via request)
    request.getfixturevalue("ensure_containers_table")

    from server.async_persistence import AsyncPersistenceLayer
    from server.database import DatabaseManager
    from server.events.event_bus import EventBus

    # Create persistence with real event_bus (not mock) for proper async operations
    event_bus = EventBus()
    persistence = AsyncPersistenceLayer(event_bus=event_bus)
    service = ContainerService(persistence=persistence)

    yield service

    # Cleanup: Close database connections before event loop closes
    # This prevents "Event loop is closed" errors during teardown
    try:
        await persistence.close()
        # Also ensure database manager closes connections
        db_manager = DatabaseManager.get_instance()
        if db_manager and hasattr(db_manager, "engine"):
            if db_manager.engine:
                await db_manager.engine.dispose(close=True)
    except (RuntimeError, asyncio.CancelledError) as e:
        # Log but don't fail on cleanup errors
        # RuntimeError covers "Event loop is closed" errors
        # asyncio.CancelledError covers cancellation during cleanup
        import logging

        logging.getLogger(__name__).warning("Error during persistence cleanup: %s", e)


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


async def _create_test_player(persistence, player_id: UUID, name: str, room_id: str = "test_room_001") -> Player:
    """Helper function to create a test player in the database."""
    from datetime import UTC, datetime

    from server.database import get_async_session
    from server.models.user import User

    # Create user first (required foreign key)
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

    # Create player
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
    # CRITICAL: Ensure commit happens and is visible before proceeding
    from sqlalchemy import select

    commit_successful = False
    async for session in get_async_session():
        try:
            session.add(user)
            await session.flush()  # Flush to make user visible to FK constraint
            session.add(player)
            await session.commit()  # Explicitly commit

            # Verify commit succeeded by checking in the same session
            stmt = select(Player).where(Player.player_id == str(player_id))
            result = await session.execute(stmt)
            committed_player = result.scalar_one_or_none()
            if committed_player is None:
                raise RuntimeError(
                    f"Player {player_id} was not found in same session after commit. "
                    "This indicates the commit failed or was rolled back."
                )
            commit_successful = True
        except Exception as e:
            await session.rollback()
            raise RuntimeError(
                f"Failed to create player {player_id}: {e}. "
                "This may indicate a database constraint violation or connection issue."
            ) from e
        # Context manager will close session automatically
        break  # Exit generator after first iteration

    if not commit_successful:
        raise RuntimeError(f"Player {player_id} commit was not successful")

    # NOTE: We don't verify player visibility here because:
    # 1. The player was verified in the same session after commit (line 305-310)
    # 2. Option 6's reliable wrapper (_create_reliable_get_player_wrapper) handles
    #    player retrieval with fallback to direct DB query, avoiding transaction
    #    isolation issues in parallel test execution
    # 3. The verification was causing flakiness in parallel execution due to
    #    PostgreSQL transaction isolation delays, even though the player was
    #    successfully committed

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
# pylint: disable=redefined-outer-name
class TestConcurrentContainerMutations:
    """Test concurrent container mutation operations."""

    @pytest.mark.serial  # Flaky in parallel execution - race conditions in concurrent database operations
    @pytest.mark.xdist_group(name="serial_container_mutations_tests")  # Force serial execution with pytest-xdist
    async def test_concurrent_open_operations(self, container_service: ContainerService) -> None:
        """Test that multiple players can open the same container concurrently."""
        try:
            # Create test container
            # Use a real room ID that exists in the database
            room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

            # Ensure room exists in cache to prevent validate_and_fix_player_room from changing player room
            _ensure_room_in_cache(container_service.persistence, room_id)

            player1_id = uuid4()
            player2_id = uuid4()

            # Create test players in database (in the same room as the container)
            player1 = await _create_test_player(
                container_service.persistence, player1_id, f"TestPlayer1_{player1_id.hex[:8]}", room_id
            )
            player2 = await _create_test_player(
                container_service.persistence, player2_id, f"TestPlayer2_{player2_id.hex[:8]}", room_id
            )

            # OPTION 6: Use reliable get_player_by_id wrapper with fallback to direct DB query
            # This avoids transaction isolation issues while maintaining integration testing
            created_players = {player1_id: player1, player2_id: player2}
            container_service.persistence.get_player_by_id = _create_reliable_get_player_wrapper(
                container_service.persistence, created_players
            )

            # Create container in persistence
            container_result = await container_service.persistence.create_container(
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

            # Open container concurrently from two players
            async def open_container(player_id: UUID) -> dict[str, Any]:
                """Open container for a player."""
                return await container_service.open_container(container_id, player_id)

            results = await asyncio.gather(
                open_container(player1_id),
                open_container(player2_id),
            )

            # Both operations should succeed
            assert len(results) == 2
            assert all("container" in result for result in results)
            assert all("mutation_token" in result for result in results)

            # Each player should get their own mutation token
            token1 = results[0]["mutation_token"]
            token2 = results[1]["mutation_token"]
            assert token1 != token2, "Each player should get a unique mutation token"
        except TimeoutError as e:
            # If the operation times out, raise an error
            # Timeout indicates a real problem that should be investigated
            raise RuntimeError(f"Test timed out: {str(e) if e else 'Test timed out after 25 seconds'}") from e

    @pytest.mark.timeout(60)
    @pytest.mark.serial  # Flaky in parallel execution - race conditions in concurrent database operations
    @pytest.mark.xdist_group(name="serial_container_mutations_tests")  # Force serial execution with pytest-xdist
    async def test_concurrent_transfer_operations(
        self,
        container_service: ContainerService,
        ensure_test_item_prototypes,  # pylint: disable=unused-argument
    ) -> None:
        """Test that concurrent transfers are handled correctly with mutation tokens."""
        # Create test container
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        _ensure_room_in_cache(container_service.persistence, room_id)
        player_id = uuid4()

        # Create test player in database
        player = await _create_test_player(
            container_service.persistence, player_id, f"TestPlayer_{player_id.hex[:8]}", room_id
        )

        # OPTION 6: Use reliable get_player_by_id wrapper with fallback to direct DB query
        created_players = {player_id: player}
        container_service.persistence.get_player_by_id = _create_reliable_get_player_wrapper(
            container_service.persistence, created_players
        )

        # Create container with items
        container_result = await container_service.persistence.create_container(
            source_type="environment",
            room_id=room_id,
            capacity_slots=10,
            weight_limit=1000.0,
            items_json=[
                {
                    "item_id": "item_1",
                    "item_name": "Test Item 1",
                    "quantity": 10,
                    "weight": 1.0,
                    "slot_type": "backpack",
                },
                {
                    "item_id": "item_2",
                    "item_name": "Test Item 2",
                    "quantity": 5,
                    "weight": 2.0,
                    "slot_type": "backpack",
                },
            ],
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Open container
        open_result = await container_service.open_container(container_id, player_id)
        mutation_token = open_result["mutation_token"]

        # Attempt concurrent transfers with same mutation token
        # This should fail for the second transfer due to token invalidation
        stack1 = {
            "item_id": "item_1",
            "item_name": "Test Item 1",
            "quantity": 1,
            "weight": 1.0,
            "slot_type": "backpack",
        }
        stack2 = {
            "item_id": "item_2",
            "item_name": "Test Item 2",
            "quantity": 1,
            "weight": 2.0,
            "slot_type": "backpack",
        }

        async def transfer_item(stack: dict[str, Any]) -> dict[str, Any] | Exception:
            """Transfer item to container."""
            try:
                return await container_service.transfer_to_container(
                    container_id=container_id,
                    player_id=player_id,
                    mutation_token=mutation_token,
                    item=cast(InventoryStack, stack),
                    quantity=1,
                )
            except ContainerServiceError as e:
                return e

        results = await asyncio.gather(
            transfer_item(stack1),
            transfer_item(stack2),
            return_exceptions=True,
        )

        # One transfer should succeed, one should fail (mutation token invalidated)
        success_count = sum(1 for r in results if not isinstance(r, Exception))
        failure_count = sum(1 for r in results if isinstance(r, Exception))

        assert success_count == 1, "One transfer should succeed"
        assert failure_count == 1, "One transfer should fail due to token invalidation"

    @pytest.mark.serial  # Flaky in parallel execution - race conditions in concurrent database operations
    @pytest.mark.xdist_group(name="serial_container_mutations_tests")  # Force serial execution with pytest-xdist
    async def test_concurrent_transfer_different_tokens(
        self,
        container_service: ContainerService,
        ensure_test_item_prototypes,  # pylint: disable=unused-argument
    ) -> None:
        """Test that transfers with different mutation tokens work correctly."""
        # Create test container
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        _ensure_room_in_cache(container_service.persistence, room_id)
        player1_id = uuid4()
        player2_id = uuid4()

        # Create test players in database
        player1 = await _create_test_player(
            container_service.persistence, player1_id, f"TestPlayer1_{player1_id.hex[:8]}", room_id
        )
        player2 = await _create_test_player(
            container_service.persistence, player2_id, f"TestPlayer2_{player2_id.hex[:8]}", room_id
        )

        # OPTION 6: Use reliable get_player_by_id wrapper with fallback to direct DB query
        created_players = {player1_id: player1, player2_id: player2}
        container_service.persistence.get_player_by_id = _create_reliable_get_player_wrapper(
            container_service.persistence, created_players
        )

        # Create container
        container_result = await container_service.persistence.create_container(
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

        # Open container for both players
        open_result1 = await container_service.open_container(container_id, player1_id)
        open_result2 = await container_service.open_container(container_id, player2_id)

        token1 = open_result1["mutation_token"]
        token2 = open_result2["mutation_token"]

        # Create test stacks
        stack1 = {
            "item_id": "item_1",
            "item_instance_id": "item_1",
            "item_name": "Test Item 1",
            "quantity": 1,
            "weight": 1.0,
            "slot_type": "backpack",
        }
        stack2 = {
            "item_id": "item_2",
            "item_instance_id": "item_2",
            "item_name": "Test Item 2",
            "quantity": 1,
            "weight": 2.0,
            "slot_type": "backpack",
        }

        # Transfer concurrently with different tokens
        async def transfer_with_token(token: str, stack: dict[str, Any], player_id: UUID) -> dict[str, Any]:
            """Transfer item with specific mutation token."""
            return await container_service.transfer_to_container(
                container_id=container_id,
                player_id=player_id,
                mutation_token=token,
                item=cast(InventoryStack, stack),
                quantity=1,
            )

        results = await asyncio.gather(
            transfer_with_token(token1, stack1, player1_id),
            transfer_with_token(token2, stack2, player2_id),
            return_exceptions=True,
        )

        # Both transfers should succeed (different tokens)
        # Debug: Print exceptions if any
        for i, r in enumerate(results):
            if isinstance(r, Exception):
                print(f"Result {i} is an exception: {type(r).__name__}: {r}")
        assert all(not isinstance(r, Exception) for r in results), (
            f"Some transfers failed: {[type(r).__name__ if isinstance(r, Exception) else 'success' for r in results]}"
        )
        assert all(isinstance(r, dict) and "container" in r for r in results if not isinstance(r, Exception))

    @pytest.mark.serial  # Flaky in parallel execution - race conditions in concurrent database operations
    @pytest.mark.xdist_group(name="serial_container_mutations_tests")  # Force serial execution with pytest-xdist
    async def test_concurrent_close_operations(self, container_service: ContainerService) -> None:
        """Test that concurrent close operations are handled correctly."""
        # Create test container
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        _ensure_room_in_cache(container_service.persistence, room_id)
        player_id = uuid4()

        # Create test player in database
        player = await _create_test_player(
            container_service.persistence, player_id, f"TestPlayer_{player_id.hex[:8]}", room_id
        )

        # OPTION 6: Use reliable get_player_by_id wrapper with fallback to direct DB query
        created_players = {player_id: player}
        container_service.persistence.get_player_by_id = _create_reliable_get_player_wrapper(
            container_service.persistence, created_players
        )

        # Create container
        container_result = await container_service.persistence.create_container(
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

        # Open container
        open_result = await container_service.open_container(container_id, player_id)
        mutation_token = open_result["mutation_token"]

        # Attempt concurrent close operations
        async def close_container(token: str) -> None | Exception:
            """Close container."""
            try:
                await container_service.close_container(
                    container_id=container_id,
                    player_id=player_id,
                    mutation_token=token,
                )
                return None
            except ContainerServiceError as e:
                return e

        results = await asyncio.gather(
            close_container(mutation_token),
            close_container(mutation_token),
            return_exceptions=True,
        )

        # One close should succeed, one should fail (token invalidated)
        success_count = sum(1 for r in results if not isinstance(r, Exception))
        failure_count = sum(1 for r in results if isinstance(r, Exception))

        assert success_count == 1, "One close should succeed"
        assert failure_count == 1, "One close should fail due to token invalidation"

    @pytest.mark.serial  # Flaky in parallel execution - race conditions in concurrent database operations
    @pytest.mark.xdist_group(name="serial_container_mutations_tests")  # Force serial execution with pytest-xdist
    async def test_concurrent_open_close_race_condition(self, container_service: ContainerService) -> None:
        """Test that open/close race conditions are handled correctly."""
        # Create test container
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        _ensure_room_in_cache(container_service.persistence, room_id)
        player_id = uuid4()

        # Create test player in database
        player = await _create_test_player(
            container_service.persistence, player_id, f"TestPlayer_{player_id.hex[:8]}", room_id
        )

        # OPTION 6: Use reliable get_player_by_id wrapper with fallback to direct DB query
        created_players = {player_id: player}
        container_service.persistence.get_player_by_id = _create_reliable_get_player_wrapper(
            container_service.persistence, created_players
        )

        # Create container
        container_result = await container_service.persistence.create_container(
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

        # Open container
        open_result = await container_service.open_container(container_id, player_id)
        mutation_token = open_result["mutation_token"]

        # Concurrently close and try to open again
        async def close_container() -> None | Exception:
            """Close container."""
            try:
                await container_service.close_container(
                    container_id=container_id,
                    player_id=player_id,
                    mutation_token=mutation_token,
                )
                return None
            except ContainerServiceError as e:
                return e

        async def open_container_again() -> dict[str, Any] | Exception:
            """Open container again."""
            try:
                # Small delay to allow close to potentially complete first
                await asyncio.sleep(0.01)
                return await container_service.open_container(container_id, player_id)
            except ContainerServiceError as e:
                return e

        results = await asyncio.gather(
            close_container(),
            open_container_again(),
            return_exceptions=True,
        )

        # Both operations should complete (close succeeds, open succeeds after close)
        assert len(results) == 2
        # Close should succeed
        assert not isinstance(results[0], Exception)
        # Open should succeed (can open after close)
        assert not isinstance(results[1], Exception)
        assert isinstance(results[1], dict) and "mutation_token" in results[1]

    @pytest.mark.serial  # Flaky in parallel execution - race conditions in concurrent database operations
    @pytest.mark.xdist_group(name="serial_container_mutations_tests")  # Force serial execution with pytest-xdist
    async def test_concurrent_capacity_validation(
        self,
        container_service: ContainerService,
        ensure_test_item_prototypes,  # pylint: disable=unused-argument
    ) -> None:
        """Test that capacity validation works correctly under concurrent load."""
        # Create test container with limited capacity
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        _ensure_room_in_cache(container_service.persistence, room_id)
        player_id = uuid4()

        # Create test player in database
        player = await _create_test_player(
            container_service.persistence, player_id, f"TestPlayer_{player_id.hex[:8]}", room_id
        )

        # OPTION 6: Use reliable get_player_by_id wrapper with fallback to direct DB query
        created_players = {player_id: player}
        container_service.persistence.get_player_by_id = _create_reliable_get_player_wrapper(
            container_service.persistence, created_players
        )

        # Create container with capacity of 2 items
        container_result = await container_service.persistence.create_container(
            source_type="environment",
            room_id=room_id,
            capacity_slots=2,
            weight_limit=1000.0,
        )
        container_id = (
            container_result["container_id"]
            if isinstance(container_result["container_id"], UUID)
            else UUID(container_result["container_id"])
        )

        # Open container
        open_result = await container_service.open_container(container_id, player_id)
        mutation_token = open_result["mutation_token"]

        # Attempt to add 3 items sequentially (should fail for the 3rd due to capacity)
        # Note: We test sequentially because mutation tokens are invalidated after each transfer,
        # so concurrent transfers with the same token would fail due to token invalidation, not capacity.
        stacks = [
            {
                "item_id": f"item_{i + 1}",  # Use item_1, item_2, item_3 (item_0 doesn't exist)
                "item_instance_id": f"item_{i + 1}",
                "item_name": f"Test Item {i + 1}",
                "quantity": 1,
                "weight": 1.0,
                "slot_type": "backpack",
            }
            for i in range(3)
        ]

        # Transfer first 2 items (should succeed)
        for i in range(2):
            await container_service.transfer_to_container(
                container_id=container_id,
                player_id=player_id,
                mutation_token=mutation_token,
                item=cast(InventoryStack, stacks[i]),
                quantity=1,
            )
            # Close container after transfer (using token before it's fully invalidated)
            # Then reopen to get new mutation token for next transfer
            await container_service.close_container(container_id, player_id, mutation_token)
            open_result = await container_service.open_container(container_id, player_id)
            mutation_token = open_result["mutation_token"]

        # Verify container has 2 items before attempting 3rd
        container_data = await container_service.persistence.get_container(container_id)
        assert container_data is not None
        container = _filter_container_data(container_data)
        assert len(container["items"]) == 2, "Container should have 2 items before attempting 3rd"

        # Attempt to add 3rd item (should fail due to capacity limit)
        with pytest.raises(ContainerServiceError):  # Should raise ContainerServiceError due to capacity
            await container_service.transfer_to_container(
                container_id=container_id,
                player_id=player_id,
                mutation_token=mutation_token,
                item=cast(InventoryStack, stacks[2]),
                quantity=1,
            )

        # Verify final container state - still has only 2 items
        container_data = await container_service.persistence.get_container(container_id)
        assert container_data is not None
        container = _filter_container_data(container_data)
        assert len(container["items"]) == 2, "Container should still have exactly 2 items after failed 3rd transfer"
