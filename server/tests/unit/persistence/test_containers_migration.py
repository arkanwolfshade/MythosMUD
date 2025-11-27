"""
Migration tests ensuring containers table is created correctly.

As documented in the restricted archives of Miskatonic University, the container
system requires careful validation to ensure proper storage of investigator
artifacts and forbidden artifacts.
"""

from __future__ import annotations

import json
import uuid
from contextlib import asynccontextmanager
from datetime import UTC, datetime, timedelta

import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def _use_async_session():
    """
    Context manager helper to properly handle async session generator lifecycle.

    This helper ensures the generator completes cleanup properly before
    test teardown, preventing "orphaned test loops" warnings and event
    loop closure errors that occur with asyncpg on Windows.

    CRITICAL: Forces database engine recreation for the current event loop
    to prevent "Task got Future attached to a different loop" errors.

    Usage:
        async with _use_async_session() as session:
            # Use session here
            await session.execute(...)
    """
    import asyncio

    from server.database import get_async_session, get_database_manager

    # CRITICAL: Ensure database engine is recreated for the current event loop
    # This prevents "Task got Future attached to a different loop" errors
    # when tests run in parallel or event loops change between test collection and execution
    try:
        # Verify we're in a running event loop (get_running_loop() raises if not)
        asyncio.get_running_loop()
        db_manager = get_database_manager()
        # Force engine recreation check by calling get_engine() which checks loop ID
        # This ensures the engine is bound to the current test's event loop
        _ = db_manager.get_engine()
    except RuntimeError:
        # No running loop yet - that's okay, engine will be created when needed
        pass

    gen = get_async_session()
    session = None
    try:
        # Get the session from the generator
        session = await anext(gen)
        yield session
    finally:
        # Explicitly close session first to ensure all operations complete
        # and connections are returned to the pool before generator cleanup
        if session is not None:
            try:
                # Commit/rollback any pending transaction before closing
                if hasattr(session, "in_transaction") and session.in_transaction():
                    await session.rollback()
                # Close the session to return connection to pool
                await session.close()
            except (RuntimeError, AttributeError, Exception):
                # Ignore errors if session is already closed or event loop is closed
                # This is expected behavior with asyncpg on Windows when running in parallel
                pass
        # Then close the generator
        try:
            await gen.aclose()
        except (StopAsyncIteration, RuntimeError, GeneratorExit, AttributeError):
            # Ignore cleanup errors - expected when event loop is closing
            # or generator is already closed
            pass


@pytest.mark.asyncio
async def test_containers_table_exists():
    """Test that containers table exists after migration."""
    async with _use_async_session() as session:
        # Check if table exists
        result = await session.execute(
            text("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_name = 'containers'
        )
    """)
        )
        table_exists = result.scalar()
        assert table_exists, "containers table should exist after migration"


@pytest.mark.asyncio
async def test_containers_table_schema():
    """Test that containers table has correct schema."""
    async with _use_async_session() as session:
        # Get column information
        result = await session.execute(
            text("""
            SELECT column_name, data_type, is_nullable, column_default
            FROM information_schema.columns
            WHERE table_schema = 'public'
            AND table_name = 'containers'
            ORDER BY ordinal_position
        """)
        )
        columns = {
            row[0]: {"type": row[1], "nullable": row[2] == "YES", "default": row[3]} for row in result.fetchall()
        }

        # Verify required columns exist
        assert "container_instance_id" in columns
        assert columns["container_instance_id"]["type"] in ("uuid", "USER-DEFINED")
        assert not columns["container_instance_id"]["nullable"]

        assert "source_type" in columns
        assert columns["source_type"]["type"] in ("text", "character varying")
        assert not columns["source_type"]["nullable"]

        assert "owner_id" in columns
        assert columns["owner_id"]["type"] in ("uuid", "USER-DEFINED")
        assert columns["owner_id"]["nullable"]

        assert "room_id" in columns
        assert columns["room_id"]["type"] in ("character varying", "varchar", "text")
        assert columns["room_id"]["nullable"]

        assert "entity_id" in columns
        assert columns["entity_id"]["type"] in ("uuid", "USER-DEFINED")
        assert columns["entity_id"]["nullable"]

        assert "lock_state" in columns
        assert columns["lock_state"]["type"] in ("text", "character varying")
        assert not columns["lock_state"]["nullable"]
        assert "unlocked" in (columns["lock_state"]["default"] or "")

        assert "capacity_slots" in columns
        assert columns["capacity_slots"]["type"] in ("integer", "int4")
        assert not columns["capacity_slots"]["nullable"]

        assert "weight_limit" in columns
        assert columns["weight_limit"]["type"] in ("integer", "int4")
        assert columns["weight_limit"]["nullable"]

        assert "decay_at" in columns
        assert columns["decay_at"]["type"] in ("timestamp with time zone", "timestamptz")
        assert columns["decay_at"]["nullable"]

        assert "allowed_roles" in columns
        assert columns["allowed_roles"]["type"] in ("jsonb", "USER-DEFINED")
        assert columns["allowed_roles"]["nullable"]

        assert "items_json" in columns
        assert columns["items_json"]["type"] in ("jsonb", "USER-DEFINED")
        assert not columns["items_json"]["nullable"]

        assert "metadata_json" in columns
        assert columns["metadata_json"]["type"] in ("jsonb", "USER-DEFINED")
        assert columns["metadata_json"]["nullable"]

        assert "created_at" in columns
        assert "updated_at" in columns


@pytest.mark.asyncio
async def test_containers_table_indexes():
    """Test that containers table has required indexes."""
    async with _use_async_session() as session:
        result = await session.execute(
            text("""
            SELECT indexname
            FROM pg_indexes
            WHERE schemaname = 'public'
            AND tablename = 'containers'
        """)
        )
        indexes = {row[0] for row in result.fetchall()}

        # Verify required indexes exist
        assert "containers_pkey" in indexes, "Primary key index should exist"
        assert "idx_containers_room_id" in indexes, "Room ID index should exist"
        assert "idx_containers_entity_id" in indexes, "Entity ID index should exist"
        assert "idx_containers_owner_id" in indexes, "Owner ID index should exist"
        assert "idx_containers_source_type" in indexes, "Source type index should exist"
        assert "idx_containers_decay_at" in indexes, "Decay timestamp index should exist"


@pytest.mark.asyncio
async def test_containers_table_constraints():
    """Test that containers table has correct constraints."""
    # Check CHECK constraints
    async with _use_async_session() as session:
        result = await session.execute(
            text("""
            SELECT conname, pg_get_constraintdef(oid) as definition
            FROM pg_constraint
            WHERE conrelid = 'public.containers'::regclass
            AND contype = 'c'
        """)
        )
        check_constraints = {row[0]: row[1] for row in result.fetchall()}

        # Verify source_type constraint
        source_type_constraint = next((defn for name, defn in check_constraints.items() if "source_type" in defn), None)
        assert source_type_constraint is not None, "source_type CHECK constraint should exist"
        assert "environment" in source_type_constraint
        assert "equipment" in source_type_constraint
        assert "corpse" in source_type_constraint

        # Verify lock_state constraint
        lock_state_constraint = next((defn for name, defn in check_constraints.items() if "lock_state" in defn), None)
        assert lock_state_constraint is not None, "lock_state CHECK constraint should exist"

        # Verify capacity_slots constraint
        capacity_constraint = next((defn for name, defn in check_constraints.items() if "capacity_slots" in defn), None)
        assert capacity_constraint is not None, "capacity_slots CHECK constraint should exist"


@pytest.mark.asyncio
async def test_containers_table_insert_environment():
    """Test inserting an environmental container."""
    async with _use_async_session() as session:
        container_id = uuid.uuid4()
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"

        await session.execute(
            text("""
            INSERT INTO containers (
                container_instance_id, source_type, room_id,
                capacity_slots, items_json
            ) VALUES (
                :container_id, 'environment', :room_id,
                8, '[]'::jsonb
            )
        """),
            {"container_id": container_id, "room_id": room_id},
        )
        await session.commit()

        # Verify insertion
        result = await session.execute(
            text("SELECT * FROM containers WHERE container_instance_id = :container_id"),
            {"container_id": container_id},
        )
        row = result.fetchone()
        assert row is not None, "Container should be inserted"
        assert row.source_type == "environment"
        assert row.room_id == room_id
        assert row.capacity_slots == 8
        assert row.items_json == []


@pytest.mark.asyncio
async def test_containers_table_insert_corpse():
    """Test inserting a corpse container with decay timestamp."""
    async with _use_async_session() as session:
        container_id = uuid.uuid4()
        owner_id = uuid.uuid4()
        room_id = "earth_arkhamcity_sanitarium_room_foyer_001"
        decay_at = datetime.now(UTC) + timedelta(hours=1)

        # Get or create minimal test profession (required for players)
        # Test Profession with id=1 should already exist, but ensure it does
        await session.execute(
            text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects, is_available)
                VALUES (1, 'Test Profession', 'Test profession for migration tests', 'Test flavor', '{}', '{}', true)
                ON CONFLICT (id) DO UPDATE SET name = professions.name
            """),
        )
        profession_id = 1  # Use known profession_id

        # Create a minimal test player to satisfy foreign key constraint
        # These migration tests only verify schema, not full application logic
        user_id = uuid.uuid4()
        # Use unique username/email to avoid conflicts
        username = f"test_player_{user_id.hex[:8]}"
        email = f"test_{user_id.hex[:8]}@example.com"
        await session.execute(
            text("""
                INSERT INTO users (id, username, email, hashed_password, display_name, is_active, is_superuser, is_verified, is_admin, created_at, updated_at)
                VALUES (:user_id, :username, :email, 'dummy_hash', 'TestPlayer', true, false, false, false, NOW(), NOW())
                ON CONFLICT DO NOTHING
            """),
            {"user_id": user_id, "username": username, "email": email},
        )
        # For migration tests, we need minimal test players
        # Use unique names to avoid conflicts
        player_name = f"TestPlayer_{owner_id.hex[:8]}"
        await session.execute(
            text("""
                INSERT INTO players (player_id, user_id, name, inventory, status_effects, current_room_id, experience_points, level, is_admin, profession_id, created_at, last_active)
                VALUES (:player_id, :user_id, :player_name, '[]', '[]', 'earth_arkhamcity_sanitarium_room_foyer_001', 0, 1, 0, :profession_id, NOW(), NOW())
                ON CONFLICT DO NOTHING
            """),
            {"player_id": owner_id, "user_id": user_id, "player_name": player_name, "profession_id": profession_id},
        )

        await session.execute(
            text("""
                INSERT INTO containers (
                    container_instance_id, source_type, owner_id, room_id,
                    capacity_slots, decay_at, items_json
                ) VALUES (
                    :container_id, 'corpse', :owner_id, :room_id,
                    20, :decay_at, '[]'::jsonb
                )
            """),
            {
                "container_id": container_id,
                "owner_id": owner_id,
                "room_id": room_id,
                "decay_at": decay_at,
            },
        )
        await session.commit()

        # Verify insertion
        result = await session.execute(
            text("SELECT * FROM containers WHERE container_instance_id = :container_id"),
            {"container_id": container_id},
        )
        row = result.fetchone()
        assert row is not None, "Corpse container should be inserted"
        assert row.source_type == "corpse"
        assert str(row.owner_id) == str(owner_id)
        assert row.room_id == room_id
        assert row.decay_at is not None


@pytest.mark.asyncio
async def test_containers_table_insert_equipment():
    """Test inserting a wearable equipment container."""
    async with _use_async_session() as session:
        container_id = uuid.uuid4()
        entity_id = uuid.uuid4()

        # Get or create minimal test profession (required for players)
        # Test Profession with id=1 should already exist, but ensure it does
        await session.execute(
            text("""
                INSERT INTO professions (id, name, description, flavor_text, stat_requirements, mechanical_effects, is_available)
                VALUES (1, 'Test Profession', 'Test profession for migration tests', 'Test flavor', '{}', '{}', true)
                ON CONFLICT (id) DO UPDATE SET name = professions.name
            """),
        )
        profession_id = 1  # Use known profession_id

        # Create a minimal test player to satisfy foreign key constraint
        # These migration tests only verify schema, not full application logic
        user_id = uuid.uuid4()
        # Use unique username/email to avoid conflicts
        username = f"test_entity_{user_id.hex[:8]}"
        email = f"test_entity_{user_id.hex[:8]}@example.com"
        await session.execute(
            text("""
                INSERT INTO users (id, username, email, hashed_password, display_name, is_active, is_superuser, is_verified, is_admin, created_at, updated_at)
                VALUES (:user_id, :username, :email, 'dummy_hash', 'TestEntity', true, false, false, false, NOW(), NOW())
                ON CONFLICT DO NOTHING
            """),
            {"user_id": user_id, "username": username, "email": email},
        )
        # For migration tests, we need minimal test players
        # Use unique names to avoid conflicts
        player_name = f"TestEntity_{entity_id.hex[:8]}"
        await session.execute(
            text("""
                INSERT INTO players (player_id, user_id, name, inventory, status_effects, current_room_id, experience_points, level, is_admin, profession_id, created_at, last_active)
                VALUES (:player_id, :user_id, :player_name, '[]', '[]', 'earth_arkhamcity_sanitarium_room_foyer_001', 0, 1, 0, :profession_id, NOW(), NOW())
                ON CONFLICT DO NOTHING
            """),
            {"player_id": entity_id, "user_id": user_id, "player_name": player_name, "profession_id": profession_id},
        )

        await session.execute(
            text("""
                INSERT INTO containers (
                    container_instance_id, source_type, entity_id,
                    capacity_slots, items_json
                ) VALUES (
                    :container_id, 'equipment', :entity_id,
                    10, '[]'::jsonb
                )
            """),
            {"container_id": container_id, "entity_id": entity_id},
        )
        await session.commit()

        # Verify insertion
        result = await session.execute(
            text("SELECT * FROM containers WHERE container_instance_id = :container_id"),
            {"container_id": container_id},
        )
        row = result.fetchone()
        assert row is not None, "Equipment container should be inserted"
        assert row.source_type == "equipment"
        assert str(row.entity_id) == str(entity_id)


@pytest.mark.asyncio
async def test_containers_table_jsonb_items():
    """Test that items_json can store InventoryStack arrays."""
    async with _use_async_session() as session:
        container_id = uuid.uuid4()
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

        await session.execute(
            text("""
                INSERT INTO containers (
                    container_instance_id, source_type, room_id,
                    capacity_slots, items_json
                ) VALUES (
                    :container_id, 'environment', :room_id,
                    8, cast(:items_json as jsonb)
                )
            """),
            {
                "container_id": container_id,
                "room_id": "earth_arkhamcity_sanitarium_room_foyer_001",
                "items_json": json.dumps(items),
            },
        )
        await session.commit()

        # Verify JSONB storage and retrieval
        result = await session.execute(
            text("SELECT items_json FROM containers WHERE container_instance_id = :container_id"),
            {"container_id": container_id},
        )
        row = result.fetchone()
        assert row is not None
        retrieved_items = row.items_json
        assert len(retrieved_items) == 2
        assert retrieved_items[0]["item_id"] == "elder_sign"
        assert retrieved_items[1]["item_id"] == "tome_of_forbidden_knowledge"


@pytest.mark.asyncio
async def test_containers_table_defaults():
    """Test that containers table uses correct default values."""
    async with _use_async_session() as session:
        container_id = uuid.uuid4()

        await session.execute(
            text("""
                INSERT INTO containers (
                    container_instance_id, source_type, capacity_slots
                ) VALUES (
                    :container_id, 'environment', 8
                )
            """),
            {"container_id": container_id},
        )
        await session.commit()

        # Verify defaults
        result = await session.execute(
            text("SELECT * FROM containers WHERE container_instance_id = :container_id"),
            {"container_id": container_id},
        )
        row = result.fetchone()
        assert row is not None
        assert row.lock_state == "unlocked"
        assert row.items_json == []
        assert row.created_at is not None
        assert row.updated_at is not None


@pytest.mark.asyncio
async def test_containers_table_constraint_violations():
    """Test that constraints properly reject invalid data."""
    container_id = uuid.uuid4()

    # Test invalid source_type
    async with _use_async_session() as session1:
        with pytest.raises(IntegrityError):
            await session1.execute(
                text("""
                    INSERT INTO containers (
                        container_instance_id, source_type, capacity_slots
                    ) VALUES (
                        :container_id, 'invalid_type', 8
                    )
                """),
                {"container_id": container_id},
            )
            await session1.commit()

    # Test invalid capacity_slots (too high)
    container_id2 = uuid.uuid4()
    async with _use_async_session() as session2:
        with pytest.raises(IntegrityError):
            await session2.execute(
                text("""
                    INSERT INTO containers (
                        container_instance_id, source_type, capacity_slots
                    ) VALUES (
                        :container_id, 'environment', 25
                    )
                """),
                {"container_id": container_id2},
            )
            await session2.commit()

    # Test invalid capacity_slots (zero)
    container_id3 = uuid.uuid4()
    async with _use_async_session() as session3:
        with pytest.raises(IntegrityError):
            await session3.execute(
                text("""
                    INSERT INTO containers (
                        container_instance_id, source_type, capacity_slots
                    ) VALUES (
                        :container_id, 'environment', 0
                    )
                """),
                {"container_id": container_id3},
            )
            await session3.commit()
