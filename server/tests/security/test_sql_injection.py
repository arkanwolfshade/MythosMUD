"""
Security tests for SQL injection prevention.

These tests verify that all database operations use parameterized queries
and are protected against SQL injection attacks.
"""

import json
import os
import uuid
from datetime import datetime
from typing import cast

import pytest

from server.exceptions import DatabaseError, ValidationError
from server.models.player import Player
from server.persistence import PersistenceLayer, get_persistence, reset_persistence


class TestSQLInjectionPrevention:
    """Test SQL injection prevention in database operations."""

    @pytest.fixture(autouse=True)
    def cleanup_players(self, persistence):
        """Clean up test players after each test."""
        # Clean up any existing player for test_user_id before test runs
        try:
            test_user_id = getattr(persistence, "_test_user_id", None)
            if test_user_id:
                # Delete any existing player for this user_id (user_id has unique constraint)
                from uuid import UUID

                try:
                    # Try to get player by user_id (if such method exists) or find by name patterns
                    # Since we can't easily query by user_id, we'll clean up after test
                    pass
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception:
            pass  # Ignore cleanup errors

        yield

        # Clean up test players after test completes
        try:
            test_user_id = getattr(persistence, "_test_user_id", None)
            if test_user_id:
                # Delete test players for this user by trying common test names
                # or by getting player by user_id if possible
                from uuid import UUID

                try:
                    # Try to find player by user_id - we'll need to query the database directly
                    # For now, try to delete by common test player names
                    for name_pattern in ["TestPlayer", "TestPlayer2", "SafePlayer", "TestPlayer3", "ErrorPlayer"]:
                        player = persistence.get_player_by_name(name_pattern)
                        if player:
                            try:
                                player_id_uuid = (
                                    UUID(str(player.player_id))
                                    if isinstance(player.player_id, str)
                                    else player.player_id
                                )
                                persistence.delete_player(player_id_uuid)
                                break  # Found and deleted one, that's enough
                            except Exception:
                                pass  # Ignore cleanup errors
                except Exception:
                    pass  # Ignore cleanup errors
        except Exception:
            pass  # Ignore cleanup errors

    @pytest.fixture
    def persistence(self):
        """Create a persistence layer instance for testing."""
        # Reset persistence to ensure clean state
        reset_persistence()

        # Use PostgreSQL from environment - SQLite is no longer supported
        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            pytest.skip("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")

        # Get persistence instance (uses singleton pattern)
        persistence_instance = get_persistence()

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
                        except Exception as e:
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
                            except Exception as e2:
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
                else:
                    pytest.skip("Could not find or create a test user - database may be empty or schema mismatch")
                break

        # Run async function to create test user
        import asyncio

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        loop.run_until_complete(create_test_user())

        # Clean up any existing test players for this user before tests run
        test_user_id = getattr(persistence_instance, "_test_user_id", None)
        if test_user_id:
            try:
                # Try to find and delete any existing test players
                from sqlalchemy import text

                from server.database import get_async_session

                async def cleanup_existing_players():
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

                loop.run_until_complete(cleanup_existing_players())
            except Exception:
                pass  # Ignore cleanup errors

        return persistence_instance

    def test_update_player_stat_field_whitelist_validation(self, persistence: PersistenceLayer):
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
            stats={"current_health": 100, "max_health": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        persistence.save_player(player)

        # Test valid field names (only fields that are in stats JSONB)
        # Note: experience_points is NOT in stats JSONB - it's a separate INTEGER column
        valid_fields = [
            "current_health",
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
            persistence.update_player_stat_field(player_id_uuid, field_name, 10, "test")

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
                persistence.update_player_stat_field(player_id_uuid, field_name, 10, "test")

    def test_update_player_stat_field_parameterized_query(self, persistence: PersistenceLayer):
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
            stats={"current_health": 100, "max_health": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        persistence.save_player(player)

        # Attempt SQL injection via delta parameter
        # The delta is parameterized, so this should be safe
        # (field_name is already validated by whitelist)
        malicious_delta = "10; DROP TABLE players; --"

        # This should fail with a type error, not execute SQL
        # malicious_delta is a string, but update_player_stat_field expects int | float
        with pytest.raises((TypeError, ValueError)):
            from uuid import UUID

            player_id_uuid = UUID(str(player.player_id))
            persistence.update_player_stat_field(
                player_id_uuid,
                "current_health",
                cast(int | float, malicious_delta),  # Intentionally passing wrong type to test type checking
                "test",
            )

    def test_get_player_by_name_parameterized(self, persistence: PersistenceLayer):
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
            stats={"current_health": 100, "max_health": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        persistence.save_player(player)

        # Attempt SQL injection via name parameter
        malicious_names = [
            "SafePlayer'; DROP TABLE players; --",
            "SafePlayer' OR '1'='1",
            "SafePlayer' UNION SELECT * FROM users; --",
        ]

        for malicious_name in malicious_names:
            # Should return None (player not found), not execute malicious SQL
            result = persistence.get_player_by_name(malicious_name)
            assert result is None, f"SQL injection attempt should not find player: {malicious_name}"

        # Valid name should still work
        result = persistence.get_player_by_name("SafePlayer")
        assert result is not None
        assert result.name == "SafePlayer"

    def test_get_player_by_id_parameterized(self, persistence: PersistenceLayer):
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
            stats={"current_health": 100, "max_health": 100},  # JSONB accepts dict directly
            status_effects=json.dumps([]),
            inventory=json.dumps([]),
        )
        persistence.save_player(player)

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
                result = persistence.get_player(uuid_obj)
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

        result = persistence.get_player(UUID(test_player_id))
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

    def test_player_name_validation(self, persistence: PersistenceLayer):
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
                persistence.save_player(player)
                # If it succeeds, verify the name was sanitized
                saved_player = persistence.get_player_by_name(malicious_name)
                if saved_player:
                    # Name should be sanitized, not contain SQL
                    assert "DROP" not in saved_player.name
                    assert "DELETE" not in saved_player.name
                    assert ";" not in saved_player.name
            except (DatabaseError, ValidationError):
                # Validation error is acceptable - prevents injection
                pass
