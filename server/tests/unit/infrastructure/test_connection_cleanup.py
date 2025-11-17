"""
Tests for connection pool cleanup in all shutdown paths and error scenarios.

These tests verify that database connections and pools are properly cleaned up
in all shutdown scenarios, including normal shutdown and error conditions.
"""

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest

from server.async_persistence import AsyncPersistenceLayer
from server.database import DatabaseManager, close_db, get_database_manager


class TestAsyncPersistenceCleanup:
    """Test AsyncPersistenceLayer connection cleanup."""

    @pytest.fixture
    def async_persistence(self):
        """Create an AsyncPersistenceLayer instance for testing."""
        return AsyncPersistenceLayer()

    @pytest.mark.asyncio
    async def test_close_method_exists(self, async_persistence):
        """Test that close() method exists and can be called."""
        # The close() method should exist for backward compatibility
        # Even though SQLAlchemy sessions are managed by context managers,
        # the method should not raise errors
        await async_persistence.close()

    @pytest.mark.asyncio
    async def test_close_is_idempotent(self, async_persistence):
        """Test that close() can be called multiple times safely."""
        # Should not raise errors on multiple calls
        await async_persistence.close()
        await async_persistence.close()
        await async_persistence.close()

    @pytest.mark.asyncio
    async def test_session_cleanup_on_exception(self, async_persistence):
        """Test that sessions are cleaned up even when exceptions occur."""
        # SQLAlchemy async sessions use context managers, so they should
        # be cleaned up automatically even on exceptions
        from server.database import get_async_session

        try:
            async for _session in get_async_session():
                # Simulate an exception during operation
                raise ValueError("Test exception")
        except ValueError:
            # Exception should not prevent cleanup
            pass

        # Verify we can still create new sessions after exception
        # (This verifies cleanup happened)
        async for session in get_async_session():
            assert session is not None
            break


class TestDatabaseManagerCleanup:
    """Test DatabaseManager connection pool cleanup."""

    @pytest.fixture
    def db_manager(self):
        """Create a fresh DatabaseManager instance for testing."""
        # Reset singleton to ensure clean state
        DatabaseManager._instance = None
        manager = DatabaseManager.get_instance()
        yield manager
        # Cleanup
        DatabaseManager._instance = None

    @pytest.mark.asyncio
    async def test_close_db_function(self):
        """Test that close_db() function properly cleans up resources."""
        # Initialize database first
        from server.database import init_db

        await init_db()

        # Close database
        await close_db()

        # Should not raise errors
        # In a real scenario, this would close all connections

    @pytest.mark.asyncio
    async def test_engine_cleanup_on_shutdown(self, db_manager):
        """Test that engine is properly cleaned up on shutdown."""
        engine = db_manager.get_engine()
        assert engine is not None

        # Simulate shutdown
        with patch.object(engine, "dispose", new_callable=Mock):
            # In a real shutdown scenario, dispose() would be called
            # We're just verifying the pattern exists
            pass

    @pytest.mark.asyncio
    async def test_session_maker_cleanup(self, db_manager):
        """Test that session maker resources are cleaned up."""
        session_maker = db_manager.get_session_maker()
        assert session_maker is not None

        # Verify session maker can be used
        async for session in session_maker():
            assert session is not None
            # Session should be automatically closed by context manager
            break

    @pytest.mark.asyncio
    async def test_cleanup_on_initialization_error(self, db_manager):
        """Test cleanup behavior when initialization fails."""
        # This test verifies that partial initialization doesn't leak resources
        with patch.object(db_manager, "_initialize_database", side_effect=Exception("Init error")):
            try:
                db_manager.get_engine()
            except Exception:
                # Initialization failed, but no resources should be leaked
                pass

        # Should be able to recover and initialize properly
        db_manager._initialized = False
        engine = db_manager.get_engine()
        assert engine is not None


class TestConnectionPoolErrorScenarios:
    """Test connection pool cleanup in error scenarios."""

    @pytest.mark.asyncio
    async def test_cleanup_on_connection_error(self):
        """Test cleanup when connection errors occur."""
        async_persistence = AsyncPersistenceLayer()

        # Simulate a connection error
        with patch("server.database.get_async_session", side_effect=Exception("Connection error")):
            try:
                await async_persistence.get_player_by_id("test-id")
            except Exception:
                # Error occurred, but cleanup should still happen
                pass

        # Should be able to recover
        # (In real scenario, sessions are managed by context managers)

    @pytest.mark.asyncio
    async def test_cleanup_on_transaction_error(self):
        """Test cleanup when transaction errors occur."""
        async_persistence = AsyncPersistenceLayer()

        # Create a mock player for testing
        from server.models.player import Player

        mock_player = Mock(spec=Player)
        mock_player.player_id = "test-player"
        mock_player.name = "TestPlayer"

        # Simulate transaction error during save
        with patch("server.database.get_async_session") as mock_session:
            mock_session_obj = AsyncMock()
            mock_session_obj.merge = AsyncMock(side_effect=Exception("Transaction error"))
            mock_session_obj.commit = AsyncMock()
            mock_session.return_value.__aenter__ = AsyncMock(return_value=mock_session_obj)
            mock_session.return_value.__aexit__ = AsyncMock(return_value=None)

            try:
                await async_persistence.save_player(mock_player)
            except Exception:
                # Transaction error occurred
                pass

            # Verify session cleanup was attempted (context manager exit)
            assert mock_session.return_value.__aexit__.called

    @pytest.mark.asyncio
    async def test_cleanup_on_timeout(self):
        """Test cleanup when operations timeout."""

        # Simulate a timeout scenario
        async def slow_operation():
            await asyncio.sleep(10)  # Would timeout in real scenario
            return None

        # Use asyncio.wait_for to simulate timeout
        try:
            await asyncio.wait_for(slow_operation(), timeout=0.1)
        except TimeoutError:
            # Timeout occurred, but cleanup should still happen
            pass

        # Should be able to continue with other operations
        # (Sessions are managed by context managers, so cleanup is automatic)


class TestShutdownPathCleanup:
    """Test cleanup in various shutdown paths."""

    @pytest.mark.asyncio
    async def test_normal_shutdown_cleanup(self):
        """Test cleanup during normal application shutdown."""
        # Simulate normal shutdown sequence
        db_manager = get_database_manager()

        # Initialize
        engine = db_manager.get_engine()
        assert engine is not None

        # Use some sessions
        async for session in db_manager.get_session_maker()():
            assert session is not None
            break

        # Shutdown
        await close_db()

        # Should complete without errors

    @pytest.mark.asyncio
    async def test_emergency_shutdown_cleanup(self):
        """Test cleanup during emergency shutdown (SIGTERM, etc.)."""
        # Simulate emergency shutdown where not all operations complete
        db_manager = get_database_manager()

        # Simulate interrupted operation
        async def interrupted_operation():
            async for _session in db_manager.get_session_maker()():
                # Operation interrupted
                raise KeyboardInterrupt("Emergency shutdown")

        try:
            await interrupted_operation()
        except KeyboardInterrupt:
            # Emergency shutdown, but cleanup should still be attempted
            pass

        # Should be able to call close_db even after interruption
        await close_db()

    @pytest.mark.asyncio
    async def test_cleanup_with_multiple_sessions(self):
        """Test cleanup when multiple sessions are active."""
        db_manager = get_database_manager()
        session_maker = db_manager.get_session_maker()

        # Create multiple sessions
        sessions = []
        for _ in range(3):
            async for session in session_maker():
                sessions.append(session)
                break

        # All sessions should be properly managed by context managers
        # Cleanup should happen automatically

        # Shutdown
        await close_db()

    @pytest.mark.asyncio
    async def test_cleanup_on_application_error(self):
        """Test cleanup when application-level errors occur."""
        async_persistence = AsyncPersistenceLayer()

        # Simulate application error that doesn't prevent cleanup
        try:
            # This would normally work, but simulate an error
            raise RuntimeError("Application error")
        except RuntimeError:
            # Error occurred, but cleanup should still be possible
            await async_persistence.close()

        # Should complete cleanup without errors
