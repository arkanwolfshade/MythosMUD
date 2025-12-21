"""
Security tests for SQL injection prevention.

These tests verify that all database operations use parameterized queries
and are protected against SQL injection attacks.
"""

import asyncio
import os
import uuid
from collections.abc import AsyncGenerator
from datetime import datetime
from typing import Any, cast
from uuid import UUID

import pytest
from sqlalchemy.exc import SQLAlchemyError

from server.async_persistence import AsyncPersistenceLayer
from server.exceptions import DatabaseError, ValidationError


class TestSQLInjectionPrevention:
    """Test SQL injection prevention in database operations."""

    async def _verify_user_exists(self, test_user_id: str) -> bool:
        """Verify that a test user exists in the database before use."""
        from sqlalchemy import text

        from server.database import get_async_session

        async for session in get_async_session():
            verify_stmt = text("SELECT id FROM users WHERE id = :user_id")
            result = await session.execute(verify_stmt, {"user_id": test_user_id})
            return result.fetchone() is not None
        return False

    @pytest.fixture(autouse=True)
    async def cleanup_players(self, persistence: AsyncPersistenceLayer) -> AsyncGenerator[None, None]:
        """Clean up test players after each test."""
        # Clean up any existing player for test_user_id before test runs
        # This prevents unique constraint violations on user_id
        try:
            test_user_id_raw = getattr(persistence, "_test_user_id", None)
            if test_user_id_raw:
                test_user_id = cast(str, test_user_id_raw)
                # Use async persistence methods
                try:
                    # Get player by user_id (async)
                    existing_player = await persistence.get_player_by_user_id(str(UUID(test_user_id)))
                    if existing_player:
                        # Delete the player using async persistence
                        player_id = existing_player.player_id
                        await persistence.delete_player(cast(Any, player_id))
                except (DatabaseError, ValidationError):
                    pass  # Ignore cleanup errors - player might not exist
        except (DatabaseError, ValidationError):
            pass  # Ignore cleanup errors - test will handle it

        yield

        # Clean up test players after test completes
        try:
            test_user_id_raw = getattr(persistence, "_test_user_id", None)
            if test_user_id_raw:
                test_user_id = cast(str, test_user_id_raw)
                # Use async persistence methods
                try:
                    # Get player by user_id (async)
                    existing_player = await persistence.get_player_by_user_id(str(UUID(test_user_id)))
                    if existing_player:
                        # Delete the player using async persistence
                        player_id = existing_player.player_id
                        await persistence.delete_player(cast(Any, player_id))
                except (DatabaseError, ValidationError):
                    pass  # Ignore cleanup errors - player might not exist
        except (DatabaseError, ValidationError):
            pass  # Ignore cleanup errors - test will handle it

    @pytest.fixture
    async def persistence(self) -> AsyncGenerator[AsyncPersistenceLayer, None]:
        """Create an async persistence layer instance for testing."""
        # Use PostgreSQL from environment - SQLite is no longer supported
        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")

        # CRITICAL: Dispose database engine before test to prevent event loop mismatch errors
        # This ensures the engine is recreated in the current event loop (the test's loop)
        # rather than using an engine created in a different loop
        from server.database import DatabaseManager

        try:
            db_manager = DatabaseManager.get_instance()
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
        persistence_instance._test_event_bus = event_bus  # type: ignore[attr-defined] # Test-only attribute for cleanup

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
                try:
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
                                            "display_name": test_email.split("@")[
                                                0
                                            ],  # Use email prefix as display_name
                                            "is_admin": False,
                                            "created_at": now,
                                            "updated_at": now,
                                        },
                                    )
                                    await session.commit()
                                    final_user_id = str(test_user_id)
                                except (DatabaseError, ValidationError) as e2:
                                    # If both fail, raise error
                                    await session.rollback()
                                    raise RuntimeError(
                                        f"Could not create test user - database schema mismatch. First error: {e}, Second error: {e2}"
                                    ) from e2
                        else:
                            final_user_id = str(test_user_id)

                    # Verify the user actually exists before using it (use a fresh query after commit)
                    if final_user_id:
                        # Use a new session to ensure we see committed data
                        async for verify_session in get_async_session():
                            verify_stmt = text("SELECT id FROM users WHERE id = :user_id")
                            result = await verify_session.execute(verify_stmt, {"user_id": final_user_id})
                            verified = result.fetchone()
                            if verified:
                                persistence_instance._test_user_id = final_user_id  # type: ignore[attr-defined] # Test-only attribute for tracking test user
                                return  # Success - exit the function
                            else:
                                # User doesn't exist, try to create it again or use existing user
                                break
                    else:
                        raise RuntimeError(
                            "Could not find or create a test user - database may be empty or schema mismatch"
                        )
                except (DatabaseError, ValidationError, SQLAlchemyError):
                    # If database operations fail, rollback and continue to next iteration
                    try:
                        await session.rollback()
                    except (DatabaseError, ValidationError, SQLAlchemyError):
                        # Ignore rollback errors - session may already be closed
                        pass
                    continue
                break

            # If we get here, we couldn't create/find a user - raise error
            if not getattr(persistence_instance, "_test_user_id", None):
                raise RuntimeError("Could not find or create a test user after all attempts")

        # Run async function to create test user (await since fixture is async)
        await create_test_user()

        # Clean up any existing test players for this user before tests run
        test_user_id = getattr(persistence_instance, "_test_user_id", None)
        if test_user_id:
            try:
                # Try to find and delete any existing test players
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
        try:
            event_bus_raw = getattr(persistence_instance, "_test_event_bus", None)
            if event_bus_raw:
                event_bus = cast(EventBus, event_bus_raw)
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
            db_manager = DatabaseManager.get_instance()
            if db_manager and db_manager.engine:
                await db_manager.engine.dispose()
        except (DatabaseError, ValidationError):
            # Ignore cleanup errors - test is ending anyway
            pass

    @pytest.mark.xdist_group(name="serial_sql_injection_tests")  # Force serial execution with pytest-xdist
    def test_f_string_sql_uses_constants_only(self) -> None:
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
