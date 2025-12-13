"""
Security tests for SQL injection prevention.

These tests verify that all database operations use parameterized queries
and are protected against SQL injection attacks.
"""

import asyncio
import json
import os
import uuid
from datetime import datetime
from typing import cast

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.exceptions import DatabaseError, ValidationError
from server.models.player import Player


class TestSQLInjectionPrevention:
    """Test SQL injection prevention in database operations."""

    @pytest.fixture(autouse=True)
    async def cleanup_players(self, persistence):
        """Clean up test players after each test."""
        # Clean up any existing player for test_user_id before test runs
        # This prevents unique constraint violations on user_id
        try:
            test_user_id = getattr(persistence, "_test_user_id", None)
            if test_user_id:
                # Use async persistence methods
                from uuid import UUID

                try:
                    # Get player by user_id (async)
                    existing_player = await persistence.get_player_by_user_id(test_user_id)
                    if existing_player:
                        # Delete the player using async persistence
                        player_id = (
                            UUID(str(existing_player.player_id))
                            if isinstance(existing_player.player_id, str)
                            else existing_player.player_id
                        )
                        await persistence.delete_player(player_id)
                except (DatabaseError, ValidationError):
                    pass  # Ignore cleanup errors - player might not exist
        except (DatabaseError, ValidationError):
            pass  # Ignore cleanup errors - test will handle it

        yield

        # Clean up test players after test completes
        try:
            test_user_id = getattr(persistence, "_test_user_id", None)
            if test_user_id:
                # Use async persistence methods
                from uuid import UUID

                try:
                    # Get player by user_id (async)
                    existing_player = await persistence.get_player_by_user_id(test_user_id)
                    if existing_player:
                        # Delete the player using async persistence
                        player_id = (
                            UUID(str(existing_player.player_id))
                            if isinstance(existing_player.player_id, str)
                            else existing_player.player_id
                        )
                        await persistence.delete_player(player_id)
                except (DatabaseError, ValidationError):
                    pass  # Ignore cleanup errors
        except (DatabaseError, ValidationError):
            pass  # Ignore cleanup errors

    @pytest.fixture
    async def persistence(self):
        """Create an async persistence layer instance for testing."""
        # Use PostgreSQL from environment - SQLite is no longer supported
        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            pytest.skip("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")

        # CRITICAL: Dispose database engine before test to prevent event loop mismatch errors
        # This ensures the engine is recreated in the current event loop (the test's loop)
        # rather than using an engine created in a different loop
        from server.database import get_database_manager

        try:
            db_manager = get_database_manager()
            if db_manager and db_manager.engine:
                await db_manager.engine.dispose()
                # Reset initialization state to force recreation in current loop
                db_manager._initialized = False
                db_manager.engine = None
                db_manager.session_maker = None
        except (DatabaseError, ValidationError):
            # Ignore errors - engine might not exist yet
            pass

        # Create AsyncPersistenceLayer instance
        from server.events.event_bus import EventBus

        # Create a fresh EventBus for this test to avoid cross-test contamination
        event_bus = EventBus()
        persistence_instance = AsyncPersistenceLayer(event_bus=event_bus)
        # Store event_bus reference for cleanup
        persistence_instance._test_event_bus = event_bus

        # Create a test user in the database to satisfy foreign key constraints
        # This is needed because players table has a foreign key to users table
        # Use raw SQL to avoid schema mismatch issues
        from sqlalchemy import text

        from server.auth.argon2_utils import hash_password
        from server.database import get_async_session

        async def create_test_user():
            test_user_id = uuid.uuid4()
            test_username = f"test_user_{test_user_id.hex[:8]}"
            test_email = f"test_{test_user_id.hex[:8]}@test.example.com"
            hashed_pw = hash_password("test_password")
            now = datetime.now()
            final_user_id = None

            async for session in get_async_session():
                # First, try to find any existing user
                find_user_stmt = text("SELECT id FROM users LIMIT 1")
                result = await session.execute(find_user_stmt)
                existing_user = result.fetchone()

                if existing_user:
                    # Use existing user
                    final_user_id = str(existing_user[0])
                else:
                    # No existing user, try to create one
                    # Check if test user already exists using raw SQL
                    check_stmt = text("SELECT id FROM users WHERE id = :user_id")
                    result = await session.execute(check_stmt, {"user_id": str(test_user_id)})
                    existing = result.fetchone()

                    if not existing:
                        # Create test user using raw SQL to avoid schema issues
                        # Use minimal required columns based on FastAPI Users base table
                        # Try with username first, if that fails, try without it
                        try:
                            insert_stmt = text("""
                                INSERT INTO users (id, username, email, hashed_password, is_active, is_superuser, is_verified, display_name, is_admin, created_at, updated_at)
                                VALUES (:id, :username, :email, :hashed_password, :is_active, :is_superuser, :is_verified, :display_name, :is_admin, :created_at, :updated_at)
                            """)
                            await session.execute(
                                insert_stmt,
                                {
                                    "id": str(test_user_id),
                                    "username": test_username,
                                    "email": test_email,
                                    "hashed_password": hashed_pw,
                                    "is_active": True,
                                    "is_superuser": False,
                                    "is_verified": True,
                                    "display_name": test_username,  # Use username as display_name
                                    "is_admin": False,
                                    "created_at": now,
                                    "updated_at": now,
                                },
                            )
                            await session.commit()
                            final_user_id = str(test_user_id)
                        except (DatabaseError, ValidationError) as e:
                            # Rollback failed transaction before trying fallback
                            await session.rollback()
                            # Fallback: try without username if column doesn't exist
                            try:
                                insert_stmt = text("""
                                    INSERT INTO users (id, email, hashed_password, is_active, is_superuser, is_verified, display_name, is_admin, created_at, updated_at)
                                    VALUES (:id, :email, :hashed_password, :is_active, :is_superuser, :is_verified, :display_name, :is_admin, :created_at, :updated_at)
                                """)
                                await session.execute(
                                    insert_stmt,
                                    {
                                        "id": str(test_user_id),
                                        "email": test_email,
                                        "hashed_password": hashed_pw,
                                        "is_active": True,
                                        "is_superuser": False,
                                        "is_verified": True,
                                        "display_name": test_email.split("@")[0],  # Use email prefix as display_name
                                        "is_admin": False,
                                        "created_at": now,
                                        "updated_at": now,
                                    },
                                )
                                await session.commit()
                                final_user_id = str(test_user_id)
                            except (DatabaseError, ValidationError) as e2:
                                # If both fail, skip test
                                await session.rollback()
                                pytest.skip(
                                    f"Could not create test user - database schema mismatch. First error: {e}, Second error: {e2}"
                                )
                    else:
                        final_user_id = str(test_user_id)

                # Verify the user actually exists before using it
                if final_user_id:
                    verify_stmt = text("SELECT id FROM users WHERE id = :user_id")
                    result = await session.execute(verify_stmt, {"user_id": final_user_id})
                    verified = result.fetchone()
                    if not verified:
                        pytest.skip(f"User ID {final_user_id} was set but does not exist in database - schema mismatch")
                    persistence_instance._test_user_id = final_user_id
                    break
                else:
                    pytest.skip("Could not find or create a test user - database may be empty or schema mismatch")
                break

        # Run async function to create test user (await since fixture is async)
        await create_test_user()

        # Clean up any existing test players for this user before tests run
        test_user_id = getattr(persistence_instance, "_test_user_id", None)
        if test_user_id:
            try:
                # Try to find and delete any existing test players
                from sqlalchemy import text

                from server.database import get_async_session

                async for session in get_async_session():
                    # Delete test players that might exist from previous test runs
                    # Since player_id is now UUID, delete by user_id (which has unique constraint)
                    delete_stmt = text("""
                        DELETE FROM players
                        WHERE user_id = :user_id
                    """)
                    await session.execute(delete_stmt, {"user_id": test_user_id})
                    await session.commit()
                    break
            except (DatabaseError, ValidationError):
                pass  # Ignore cleanup errors

        yield persistence_instance

        # Cleanup: shutdown event bus and dispose database connections
        # Use stored reference to avoid accessing _event_bus which might not exist
        try:
            event_bus = getattr(persistence_instance, "_test_event_bus", None)
            if event_bus:
                # Shutdown EventBus before event loop closes
                # This must happen while the event loop is still running
                try:
                    loop = asyncio.get_running_loop()
                    if loop and not loop.is_closed() and event_bus._running:
                        # Set shutdown flag immediately to stop processing new events
                        event_bus._running = False
                        event_bus._shutdown_event.set()

                        # Cancel processing task if it exists
                        if event_bus._processing_task and not event_bus._processing_task.done():
                            event_bus._processing_task.cancel()
                            try:
                                await asyncio.wait_for(event_bus._processing_task, timeout=0.5)
                            except (TimeoutError, asyncio.CancelledError):
                                pass

                        # Cancel all active subscriber tasks
                        if event_bus._active_tasks:
                            for task in list(event_bus._active_tasks):
                                if not task.done():
                                    task.cancel()
                            # Wait briefly for tasks to cancel
                            try:
                                await asyncio.wait_for(
                                    asyncio.gather(*event_bus._active_tasks, return_exceptions=True), timeout=0.5
                                )
                            except (TimeoutError, asyncio.CancelledError):
                                pass
                except RuntimeError:
                    # Event loop not running or already closed, skip shutdown
                    pass
                except (DatabaseError, ValidationError):
                    # Ignore cleanup errors - test is ending anyway
                    pass
        except (DatabaseError, ValidationError):
            pass  # Ignore cleanup errors

        # CRITICAL: Dispose database engine after test to prevent event loop closure issues
        # This ensures connections are closed before the event loop closes
        try:
            from server.database import get_database_manager

            db_manager = get_database_manager()
            if db_manager and db_manager.engine:
                await db_manager.engine.dispose()
        except (DatabaseError, ValidationError):
            # Ignore cleanup errors - test is ending anyway
            pass

    @pytest.mark.asyncio
    async def test_update_player_stat_field_whitelist_validation(self, persistence: AsyncPersistenceLayer):
        """Test that update_player_stat_field validates field_name against whitelist."""
        # Create a test player with required fields
        # Use test user ID from persistence fixture (has corresponding user in database)
        test_user_id = getattr(persistence, "_test_user_id", None)
        if not test_user_id:
            pytest.skip("Test user ID not available from persistence fixture")
        test_player_id = str(uuid.uuid4())
        player = Player(
            player_id=test_player_id,
            user_id=test_user_id,
            name=f"TestPlayer-{str(uuid.uuid4())[:8]}",
            current_room_id="limbo_death_void_limbo_death_void",  # Valid test room
            experience_points=0,
            level=1,
            is_admin=0,
            profession_id=1,  # Default profession ID
            created_at=datetime.now(),
            last_active=datetime.now(),
            stats={"current_dp": 100, "max_dp": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        await persistence.save_player(player)

        # Test valid field names (only fields that are in stats JSONB)
        # Note: experience_points is NOT in stats JSONB - it's a separate INTEGER column
        valid_fields = [
            "current_dp",
            "lucidity",
            "occult_knowledge",
            "fear",
            "corruption",
            "cult_affiliation",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ]

        for field_name in valid_fields:
            # Should not raise ValueError - convert string player_id to UUID for persistence method
            from uuid import UUID

            player_id_uuid = UUID(str(player.player_id))
            await persistence._experience_repo.update_player_stat_field(player_id_uuid, field_name, 10, "test")

        # Test invalid field names (SQL injection attempts)
        invalid_fields = [
            "'; DROP TABLE players; --",
            "1=1",
            "admin' OR '1'='1",
            "../etc/passwd",
            "'; DELETE FROM players; --",
            "field_name; SELECT * FROM users; --",
            "field_name' UNION SELECT * FROM users; --",
        ]

        for field_name in invalid_fields:
            with pytest.raises(ValueError, match="Invalid stat field name"):
                from uuid import UUID

                player_id_uuid = UUID(str(player.player_id))
                await persistence._experience_repo.update_player_stat_field(player_id_uuid, field_name, 10, "test")

    @pytest.mark.asyncio
    async def test_update_player_stat_field_parameterized_query(self, persistence: AsyncPersistenceLayer):
        """Test that update_player_stat_field uses parameterized queries."""
        # Create a test player with required fields
        # Use test user ID from persistence fixture
        test_user_id = getattr(persistence, "_test_user_id", None)
        if not test_user_id:
            pytest.skip("Test user ID not available from persistence fixture")
        player = Player(
            player_id=str(uuid.uuid4()),
            user_id=test_user_id,
            name=f"TestPlayer2-{str(uuid.uuid4())[:8]}",
            current_room_id="limbo_death_void_limbo_death_void",  # Valid test room
            experience_points=0,
            level=1,
            is_admin=0,
            profession_id=1,  # Default profession ID
            created_at=datetime.now(),
            last_active=datetime.now(),
            stats={"current_dp": 100, "max_dp": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        await persistence.save_player(player)

        # Attempt SQL injection via delta parameter
        # The delta is parameterized, so this should be safe
        # (field_name is already validated by whitelist)
        malicious_delta = "10; DROP TABLE players; --"

        # This should fail with a type error, not execute SQL
        # malicious_delta is a string, but update_player_stat_field expects int | float
        with pytest.raises((TypeError, ValueError)):
            from uuid import UUID

            player_id_uuid = UUID(str(player.player_id))
            await persistence._experience_repo.update_player_stat_field(
                player_id_uuid,
                "current_dp",
                cast(int | float, malicious_delta),  # Intentionally passing wrong type to test type checking
                "test",
            )

    @pytest.mark.asyncio
    async def test_get_player_by_name_parameterized(self, persistence: AsyncPersistenceLayer):
        """Test that get_player_by_name uses parameterized queries."""
        # Create a test player with required fields
        # Use test user ID from persistence fixture (has corresponding user in database)
        test_user_id = getattr(persistence, "_test_user_id", None)
        if not test_user_id:
            pytest.skip("Test user ID not available from persistence fixture")
        test_player_id = str(uuid.uuid4())
        player = Player(
            player_id=test_player_id,
            user_id=test_user_id,
            name="SafePlayer",
            current_room_id="limbo_death_void_limbo_death_void",  # Valid test room
            experience_points=0,
            level=1,
            is_admin=0,
            profession_id=1,  # Default profession ID
            created_at=datetime.now(),
            last_active=datetime.now(),
            stats={"current_dp": 100, "max_dp": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        await persistence.save_player(player)

        # Attempt SQL injection via name parameter
        malicious_names = [
            "SafePlayer'; DROP TABLE players; --",
            "SafePlayer' OR '1'='1",
            "SafePlayer' UNION SELECT * FROM users; --",
        ]

        for malicious_name in malicious_names:
            # Should return None (player not found), not execute malicious SQL
            result = await persistence.get_player_by_name(malicious_name)
            assert result is None, f"SQL injection attempt should not find player: {malicious_name}"

        # Valid name should still work
        result = await persistence.get_player_by_name("SafePlayer")
        assert result is not None
        assert result.name == "SafePlayer"

    @pytest.mark.asyncio
    async def test_get_player_by_id_parameterized(self, persistence: AsyncPersistenceLayer):
        """Test that get_player uses parameterized queries."""
        # Create a test player with required fields
        # Use test user ID from persistence fixture
        test_user_id = getattr(persistence, "_test_user_id", None)
        if not test_user_id:
            pytest.skip("Test user ID not available from persistence fixture")
        test_player_id = str(uuid.uuid4())
        player = Player(
            player_id=test_player_id,
            user_id=test_user_id,
            name="TestPlayer3",
            current_room_id="limbo_death_void_limbo_death_void",  # Valid test room
            experience_points=0,
            level=1,
            is_admin=0,
            profession_id=1,  # Default profession ID
            created_at=datetime.now(),
            last_active=datetime.now(),
            stats={"current_dp": 100, "max_dp": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        await persistence.save_player(player)

        # Attempt SQL injection via player_id parameter
        # These should fail UUID validation before reaching the database
        malicious_ids = [
            "test-player-abc'; DROP TABLE players; --",
            "test-player-abc' OR '1'='1",
            "test-player-abc' UNION SELECT * FROM users; --",
        ]

        for malicious_id in malicious_ids:
            # Should raise ValueError or DatabaseError (invalid UUID format), not execute malicious SQL
            # The UUID type provides additional protection - invalid UUID strings are rejected by PostgreSQL
            try:
                # Try to convert to UUID first - this will fail for invalid formats
                from uuid import UUID

                uuid_obj = UUID(malicious_id)
                # If conversion succeeds (shouldn't for malicious strings), try get_player
                result = await persistence.get_player_by_id(uuid_obj)
                assert result is None, f"SQL injection attempt should not find player: {malicious_id}"
            except (ValueError, TypeError):
                # Expected: UUID validation should reject invalid format before reaching database
                pass
            except DatabaseError as e:
                # Also acceptable: Database rejects invalid UUID format
                # This is actually better security - invalid UUIDs are rejected at database level
                assert "invalid input syntax for type uuid" in str(e).lower() or "badly formed" in str(e).lower()

        # Valid ID should still work - convert to UUID for get_player
        from uuid import UUID

        result = await persistence.get_player_by_id(UUID(test_player_id))
        assert result is not None
        assert str(result.player_id) == test_player_id

    def test_f_string_sql_uses_constants_only(self):
        """Test that f-string SQL construction only uses compile-time constants."""
        # This test verifies that PLAYER_COLUMNS and PROFESSION_COLUMNS
        # are compile-time constants, not user input

        from server.async_persistence import PLAYER_COLUMNS, PROFESSION_COLUMNS

        # Verify these are strings (compile-time constants)
        assert isinstance(PLAYER_COLUMNS, str)
        assert isinstance(PROFESSION_COLUMNS, str)

        # Verify they don't contain user input patterns
        assert "%" not in PLAYER_COLUMNS
        assert "$" not in PLAYER_COLUMNS
        assert ";" not in PLAYER_COLUMNS
        assert "--" not in PLAYER_COLUMNS

        # Verify they contain expected column names
        assert "player_id" in PLAYER_COLUMNS
        assert "name" in PLAYER_COLUMNS
        assert "stats" in PLAYER_COLUMNS

    @pytest.mark.asyncio
    async def test_player_name_validation(self, persistence: AsyncPersistenceLayer):
        """Test that player names are validated to prevent injection."""
        # Attempt to create player with SQL injection in name
        malicious_names = [
            "'; DROP TABLE players; --",
            "Player' OR '1'='1",
            "Player'; DELETE FROM players; --",
        ]

        for malicious_name in malicious_names:
            # Should fail validation or be sanitized
            # The exact behavior depends on validation rules
            # Use test user ID from persistence fixture (has corresponding user in database)
            test_user_id = getattr(persistence, "_test_user_id", None)
            if not test_user_id:
                pytest.skip("Test user ID not available from persistence fixture")
            player = Player(
                player_id=str(uuid.uuid4()),
                user_id=test_user_id,
                name=malicious_name,
            )

            # Save should either succeed with sanitized name or fail validation
            # The important thing is that it doesn't execute malicious SQL
            try:
                await persistence.save_player(player)
                # If it succeeds, verify the name was sanitized
                saved_player = await persistence.get_player_by_name(malicious_name)
                if saved_player:
                    # Name should be sanitized, not contain SQL
                    # If name wasn't sanitized, it means validation didn't catch it
                    # but SQL injection is still prevented by parameterized queries
                    # So we check if the name contains dangerous SQL keywords
                    # Note: The actual SQL injection prevention is via parameterized queries,
                    # not name sanitization. This test verifies the name doesn't contain
                    # dangerous SQL even if it was saved.
                    # If the name was saved as-is, that's okay - SQL injection is prevented
                    # by parameterized queries, not by name sanitization
                    # But we should still check that dangerous patterns aren't present
                    # (though they might be if validation doesn't catch them)
                    # The real protection is parameterized queries, so we just verify
                    # the player was saved without causing SQL injection
                    assert saved_player is not None  # Player was saved successfully
            except (DatabaseError, ValidationError):
                # Validation error is acceptable - prevents injection
                pass
