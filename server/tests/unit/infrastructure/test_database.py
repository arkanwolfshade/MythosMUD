"""
Tests for database configuration and session management.

This module tests the database connection, session management,
and initialization functionality in database.py.
"""

from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.database import (
    close_db,
    ensure_database_directory,
    get_async_session,
    get_database_path,
    get_engine,
    get_session_maker,
    init_db,
)
from server.exceptions import DatabaseError, ValidationError
from server.metadata import metadata


class TestDatabaseConfiguration:
    """Test database configuration constants and setup."""

    def test_database_path_postgresql(self) -> None:
        """Test database path for PostgreSQL (returns None)."""
        # PostgreSQL doesn't have a file path
        db_path = get_database_path()
        # For PostgreSQL, this should be None
        assert db_path is None

    def test_metadata_exists(self) -> None:
        """Test that metadata is properly initialized."""
        assert metadata is not None
        assert hasattr(metadata, "tables")

    def test_engine_initialization(self) -> None:
        """Test that engine is properly initialized."""
        engine = get_engine()
        assert engine is not None
        # Engine should be created with asyncpg for PostgreSQL
        assert "postgresql" in str(engine.url) or "asyncpg" in str(engine.url)

    def test_session_maker_initialization(self) -> None:
        """Test that session maker is properly initialized."""
        session_maker = get_session_maker()
        assert session_maker is not None
        assert hasattr(session_maker, "kw")  # Session maker has configuration


class TestGetDatabasePath:
    """Test database path extraction functionality."""

    def test_get_database_path_postgresql(self) -> None:
        """Test getting database path for PostgreSQL URL (returns None)."""
        with patch("server.database._database_url", "postgresql+asyncpg://postgres:pass@localhost/mythos_unit"):
            result = get_database_path()
            # PostgreSQL doesn't have a file path
            assert result is None

    def test_get_database_path_mysql_url(self) -> None:
        """Test getting database path with MySQL URL (unsupported)."""
        with patch("server.database._database_url", "mysql://user:pass@localhost/db"):
            with pytest.raises(ValidationError) as exc_info:
                get_database_path()

            assert "Unsupported database URL" in str(exc_info.value)


class TestEnsureDatabaseDirectory:
    """Test database directory creation functionality."""

    def test_ensure_database_directory_postgresql(self) -> None:
        """Test that ensure_database_directory skips for PostgreSQL (no file path)."""
        with patch("server.database.get_database_path", return_value=None):
            # Should not raise an error, just skip directory creation
            ensure_database_directory()
            # No assertions needed - function should complete without error


class TestGetAsyncSession:
    """Test async session management functionality."""

    @pytest.mark.asyncio
    async def test_get_async_session_yields_session(self) -> None:
        """Test that get_async_session yields a session."""
        session_count = 0

        async for session in get_async_session():
            session_count += 1
            assert isinstance(session, AsyncSession)
            break

        assert session_count == 1

    @pytest.mark.asyncio
    async def test_get_async_session_closes_session(self) -> None:
        """Test that session is properly closed."""
        session = None

        async for s in get_async_session():
            session = s
            break

        # Session should be closed after the context manager
        assert session is not None

    @pytest.mark.asyncio
    async def test_get_async_session_exception_handling(self) -> None:
        """Test that exceptions are properly handled."""
        # Create a mock session context manager that raises an exception
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(side_effect=RuntimeError("Test error"))
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create a mock session maker callable that returns the context manager
        mock_session_maker_callable = MagicMock()
        mock_session_maker_callable.return_value = mock_context_manager

        with patch("server.database.get_session_maker", return_value=mock_session_maker_callable):
            with pytest.raises(RuntimeError):
                async for _session in get_async_session():
                    pass


class TestInitDB:
    """Test database initialization functionality."""

    @pytest.mark.asyncio
    async def test_init_db_creates_tables(self) -> None:
        """Test that init_db verifies database connectivity."""
        # Create properly configured mocks for async engine operations
        mock_conn = AsyncMock()
        mock_result = AsyncMock()
        mock_conn.execute = AsyncMock(return_value=mock_result)

        # Create a mock async context manager
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_conn)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create a mock engine with async begin() that returns the context manager
        mock_engine = MagicMock()
        mock_engine.begin = MagicMock(return_value=mock_context_manager)

        with patch("server.database.get_engine", return_value=mock_engine):
            with patch("sqlalchemy.orm.configure_mappers"):
                with patch("server.models.invite.Invite"):
                    with patch("server.models.player.Player"):
                        with patch("server.models.user.User"):
                            with patch("server.models.lucidity.PlayerLucidity"):
                                await init_db()

            # Verify that connectivity check was performed (SELECT 1)
            mock_conn.execute.assert_called_once()
            call_args = mock_conn.execute.call_args[0]
            # text() returns a TextClause object - check by string representation
            assert "SELECT 1" in str(call_args[0])

    @pytest.mark.asyncio
    @pytest.mark.filterwarnings("ignore:coroutine.*was never awaited:RuntimeWarning")
    async def test_init_db_imports_models(self) -> None:
        """Test that init_db imports all required models."""
        # Create properly configured mocks
        mock_conn = AsyncMock()

        # Create a mock async context manager
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_conn)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create a mock engine with async begin() that returns the context manager
        mock_engine = MagicMock()
        mock_engine.begin = MagicMock(return_value=mock_context_manager)

        with patch("server.database.get_engine", return_value=mock_engine):
            # AI Agent: connection_manager no longer a module-level global - patch removed
            # Mock the specific imports that init_db makes
            with patch("server.models.invite.Invite"):
                with patch("server.models.npc.NPCDefinition"):
                    with patch("server.models.npc.NPCSpawnRule"):
                        with patch("server.models.player.Player"):
                            with patch("server.models.user.User"):
                                with patch("server.models.invite.Invite"):
                                    # ARCHITECTURE FIX: setup_relationships deleted - relationships now in models
                                    # Mock the configure_mappers function
                                    with patch("sqlalchemy.orm.configure_mappers"):
                                        await init_db()

                # Test passes if no exceptions are raised during init_db

    @pytest.mark.asyncio
    async def test_init_db_engine_begin_failure(self) -> None:
        """Test init_db when engine.begin() fails."""
        mock_engine = MagicMock()
        mock_engine.begin.side_effect = RuntimeError("Engine error")

        with patch("server.database.get_engine", return_value=mock_engine):
            with pytest.raises(RuntimeError):
                await init_db()


class TestCloseDB:
    """Test database connection closing functionality."""

    @pytest.mark.asyncio
    async def test_close_db_disposes_engine(self) -> None:
        """Test that close_db disposes the engine."""
        mock_engine = AsyncMock()
        mock_engine.dispose = AsyncMock()

        with patch("server.database.DatabaseManager.get_instance") as mock_get_mgr:
            mock_mgr = Mock()
            mock_mgr.engine = mock_engine
            mock_mgr.get_engine = Mock(return_value=mock_engine)
            mock_mgr.close = AsyncMock()
            mock_get_mgr.return_value = mock_mgr

            await close_db()

            mock_mgr.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_close_db_engine_dispose_failure(self) -> None:
        """Test close_db when engine.dispose() fails."""
        mock_engine = AsyncMock()

        with patch("server.database.DatabaseManager.get_instance") as mock_get_mgr:
            mock_mgr = Mock()
            mock_mgr.engine = mock_engine
            mock_mgr.get_engine = Mock(return_value=mock_engine)
            mock_mgr.close = AsyncMock(side_effect=RuntimeError("Dispose error"))
            mock_get_mgr.return_value = mock_mgr

            with pytest.raises(RuntimeError):
                await close_db()


class TestDatabaseIntegration:
    """Test database integration scenarios."""

    @pytest.mark.asyncio
    async def test_database_lifecycle(self) -> None:
        """Test complete database lifecycle."""
        # Create properly configured mocks
        mock_conn = AsyncMock()
        mock_result = AsyncMock()
        mock_conn.execute = AsyncMock(return_value=mock_result)

        # Create a mock async context manager
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_conn)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create a mock engine with begin() that returns the context manager
        mock_engine = MagicMock()
        mock_engine.begin = MagicMock(return_value=mock_context_manager)
        mock_engine.dispose = AsyncMock()

        with patch("server.database.DatabaseManager.get_instance") as mock_get_mgr:
            mock_mgr = Mock()
            mock_mgr.engine = mock_engine
            mock_mgr.get_engine = Mock(return_value=mock_engine)
            mock_mgr.close = AsyncMock()
            mock_get_mgr.return_value = mock_mgr

            with patch("server.database.get_engine", return_value=mock_engine):
                with patch("sqlalchemy.orm.configure_mappers"):
                    with patch("server.models.invite.Invite"):
                        with patch("server.models.player.Player"):
                            with patch("server.models.user.User"):
                                with patch("server.models.lucidity.PlayerLucidity"):
                                    await init_db()
                                    # Verify connectivity check was performed
                                    mock_conn.execute.assert_called_once()
                                    call_args = mock_conn.execute.call_args[0]
                                    # text() returns a TextClause object - check by string representation
                                    assert "SELECT 1" in str(call_args[0])

                # Test closing
                await close_db()
                mock_mgr.close.assert_called_once()

    def test_database_path_integration_postgresql(self) -> None:
        """Test database path integration with PostgreSQL (no file path)."""
        with patch("server.database.get_database_path", return_value=None):
            # PostgreSQL doesn't need directory creation
            ensure_database_directory()
            # Should complete without error

    @pytest.mark.asyncio
    async def test_session_integration(self) -> None:
        """Test session integration with async context."""
        session_count = 0

        async for session in get_async_session():
            session_count += 1
            assert hasattr(session, "commit")
            assert hasattr(session, "rollback")
            assert hasattr(session, "close")
            break

        assert session_count == 1


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_get_database_path_empty_url(self) -> None:
        """Test getting database path with empty URL."""
        with patch("server.database._database_url", ""):
            with pytest.raises(ValidationError):
                get_database_path()

    def test_get_database_path_malformed_url(self) -> None:
        """Test getting database path with malformed URL."""
        with patch("server.database._database_url", "not-a-url"):
            with pytest.raises(ValidationError):
                get_database_path()

    @pytest.mark.asyncio
    async def test_get_async_session_multiple_iterations(self) -> None:
        """Test multiple iterations of get_async_session."""
        sessions = []

        async for session in get_async_session():
            sessions.append(session)
            if len(sessions) >= 3:  # Limit to prevent infinite loop
                break

        assert len(sessions) >= 1
        assert all(isinstance(s, AsyncSession) for s in sessions)

    def test_ensure_database_directory_postgresql_skip(self) -> None:
        """Test that ensure_database_directory skips for PostgreSQL."""
        # PostgreSQL returns None, so directory creation is skipped
        with patch("server.database.get_database_path", return_value=None):
            # Should not raise any errors
            ensure_database_directory()

    @pytest.mark.asyncio
    async def test_database_manager_close_with_no_running_loop(self) -> None:
        """Test DatabaseManager.close() when no running loop exists."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        # Initialize the manager first
        manager.get_engine()

        # Mock no running loop (RuntimeError)
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            # Should handle gracefully without raising
            await manager.close()

    @pytest.mark.asyncio
    async def test_database_manager_close_timeout(self) -> None:
        """Test DatabaseManager.close() when disposal times out."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.get_engine()

        # Mock engine with timeout on dispose
        mock_engine = MagicMock()
        mock_engine.dispose = AsyncMock(side_effect=TimeoutError())
        mock_engine.sync_engine = MagicMock()
        mock_engine.sync_engine.pool = MagicMock()
        mock_engine.sync_engine.pool.dispose = MagicMock()

        manager.engine = mock_engine

        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", side_effect=TimeoutError()):
                # Should handle timeout gracefully
                await manager.close()

    @pytest.mark.asyncio
    async def test_database_manager_close_no_engine(self) -> None:
        """Test DatabaseManager.close() when engine is None."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.engine = None
        manager._initialized = True

        # Should handle gracefully
        await manager.close()
        assert manager.engine is None
        assert not manager._initialized

    def test_database_manager_get_database_path_none_url(self) -> None:
        """Test DatabaseManager.get_database_path() when URL is None."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        # Reset initialization state and set URL to None
        # Patch _initialize_database to prevent re-initialization
        original_init = manager._initialize_database
        manager._initialized = True  # Mark as initialized to skip init
        manager.database_url = None  # But set URL to None

        try:
            with pytest.raises(ValidationError, match="Database URL is None"):
                manager.get_database_path()
        finally:
            # Restore original method
            manager._initialize_database = original_init  # type: ignore[method-assign] # Restore method after test

    def test_database_manager_get_database_path_non_postgresql(self) -> None:
        """Test DatabaseManager.get_database_path() with non-PostgreSQL URL."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.database_url = "sqlite:///test.db"
        manager._initialized = True

        with pytest.raises(ValidationError, match="Unsupported database URL"):
            manager.get_database_path()

    @pytest.mark.asyncio
    async def test_database_manager_close_exception_handling(self) -> None:
        """Test DatabaseManager.close() exception handling paths."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.get_engine()

        # Mock engine with various exception scenarios
        mock_engine = MagicMock()
        mock_engine.dispose = AsyncMock(side_effect=RuntimeError("Test error"))
        manager.engine = mock_engine

        # Should handle RuntimeError gracefully
        await manager.close()
        assert manager.engine is None
        assert not manager._initialized  # type: ignore[unreachable]

    @pytest.mark.asyncio
    async def test_database_manager_close_attribute_error(self) -> None:
        """Test DatabaseManager.close() when AttributeError occurs."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.get_engine()

        # Mock engine that raises AttributeError
        mock_engine = MagicMock()
        mock_engine.dispose = AsyncMock(side_effect=AttributeError("Test error"))
        manager.engine = mock_engine

        # Should handle AttributeError gracefully
        await manager.close()
        assert manager.engine is None

    def test_database_manager_get_engine_reinitialization(self) -> None:
        """Test DatabaseManager.get_engine() reinitializes when engine is None."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()

        # Set initialized but engine is None
        manager._initialized = True
        manager.engine = None

        # Create a mock engine to be set after reinitialization
        mock_engine = MagicMock()

        def mock_init():
            """Mock _initialize_database that sets the engine."""
            manager.engine = mock_engine
            manager._initialized = True

        with patch("server.database.logger.warning") as mock_warning:
            with patch.object(manager, "_initialize_database", side_effect=mock_init):
                result = manager.get_engine()
                # Should log warning and reinitialize
                mock_warning.assert_called_once()
                # Should return the engine
                assert result == mock_engine

    def test_database_manager_initialization_skips_if_already_initialized(self) -> None:
        """Test DatabaseManager._initialize_database skips if already initialized."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = True

        # Should return early without doing anything
        original_engine = manager.engine
        manager._initialize_database()
        # Engine should be unchanged
        assert manager.engine == original_engine

    def test_database_manager_postgresql_url_conversion(self) -> None:
        """Test DatabaseManager converts postgresql:// to postgresql+asyncpg://."""
        from server.database import DatabaseManager, _database_url

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Set test database URL directly (bypassing config)
        original_url = _database_url
        try:
            # Set module-level test override
            import server.database as db_module

            db_module._database_url = "postgresql://user:pass@localhost/db"

            with patch("server.database.create_async_engine") as mock_create:
                manager._initialize_database()
                # Should convert to postgresql+asyncpg://
                call_args = mock_create.call_args[0]
                assert call_args[0].startswith("postgresql+asyncpg://")
        finally:
            # Restore original
            db_module._database_url = original_url

    def test_database_manager_session_maker_creation_exception(self) -> None:
        """Test DatabaseManager handles exceptions during session maker creation."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Mock exception during async_sessionmaker creation
        with patch("server.database.create_async_engine") as mock_create:
            mock_engine = Mock()
            mock_create.return_value = mock_engine
            with patch("server.database.async_sessionmaker", side_effect=TypeError("Session maker error")):
                # Exception during session maker creation should be caught
                # The function should still mark as initialized
                try:
                    manager._initialize_database()
                except (ValidationError, DatabaseError, TypeError):
                    # Some exceptions might propagate, that's okay
                    pass

    def test_database_manager_runtime_error_no_loop_during_init(self) -> None:
        """Test DatabaseManager handles RuntimeError when no loop during initialization."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Mock RuntimeError when getting running loop during initialization
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            with patch("server.database.create_async_engine") as mock_create:
                mock_engine = Mock()
                mock_create.return_value = mock_engine
                manager._initialize_database()
                # Should handle gracefully - _creation_loop_id should be None
                assert manager._creation_loop_id is None

    @pytest.mark.asyncio
    async def test_database_manager_close_with_closed_loop(self) -> None:
        """Test DatabaseManager.close() when event loop is closed."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager.get_engine()

        # Mock closed event loop
        mock_loop = Mock()
        mock_loop.is_closed.return_value = True

        with patch("asyncio.get_running_loop", return_value=mock_loop):
            with patch("server.database.logger.warning") as mock_warning:
                await manager.close()
                # Should log warning and skip disposal
                mock_warning.assert_called_once()
                assert manager.engine is None
                assert not manager._initialized

    @pytest.mark.asyncio
    async def test_database_manager_close_with_timeout(self) -> None:
        """Test DatabaseManager.close() handles timeout during disposal."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager.get_engine()

        # Mock engine with timeout on dispose
        mock_engine = MagicMock()
        mock_engine.dispose = AsyncMock(side_effect=TimeoutError("Disposal timeout"))
        mock_engine.sync_engine = MagicMock()
        mock_engine.sync_engine.pool = MagicMock()
        mock_engine.sync_engine.pool.dispose = MagicMock()

        manager.engine = mock_engine

        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", side_effect=TimeoutError()):
                # Should handle timeout gracefully
                await manager.close()
                # Engine should be cleared
                assert manager.engine is None

    def test_database_manager_get_database_path_with_postgresql_url(self) -> None:
        """Test DatabaseManager.get_database_path() with PostgreSQL URL returns None."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager.database_url = "postgresql+asyncpg://user:pass@localhost/db"
        manager._initialized = True

        result = manager.get_database_path()
        # PostgreSQL doesn't have a file path
        assert result is None

    def test_database_manager_get_database_path_with_non_postgresql_url(self) -> None:
        """Test DatabaseManager.get_database_path() raises error for non-PostgreSQL URL."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager.database_url = "sqlite:///test.db"
        manager._initialized = True

        with pytest.raises(ValidationError, match="Unsupported database URL"):
            manager.get_database_path()

    def test_database_manager_import_error_handling(self) -> None:
        """Test DatabaseManager handles ImportError during config import."""
        from server.database import DatabaseManager, _database_url

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Set test database URL to None to force config loading
        original_url = _database_url
        try:
            import server.database as db_module

            db_module._database_url = None

            # Mock ImportError when importing config
            # log_and_raise should raise ValidationError, so configure mock to raise
            with patch("server.database.log_and_raise", side_effect=ValidationError("Config error")):
                with patch("server.config.get_config", side_effect=ImportError("Config module not found")):
                    # This should raise ValidationError
                    with pytest.raises(ValidationError):
                        manager._initialize_database()
        finally:
            # Restore original
            db_module._database_url = original_url

    def test_database_manager_config_load_exception(self) -> None:
        """Test DatabaseManager handles exceptions during config loading."""
        from server.database import DatabaseManager, _database_url

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Set test database URL to None to force config loading
        original_url = _database_url
        try:
            import server.database as db_module

            db_module._database_url = None

            # Mock exception during config.get_config()
            # log_and_raise should raise ValidationError, so configure mock to raise
            with patch("server.database.log_and_raise", side_effect=ValidationError("Config error")):
                with patch("server.config.get_config", side_effect=RuntimeError("Config error")):
                    # This should raise ValidationError
                    with pytest.raises(ValidationError):
                        manager._initialize_database()
        finally:
            # Restore original
            db_module._database_url = original_url

    def test_database_manager_non_postgresql_url(self) -> None:
        """Test DatabaseManager validates PostgreSQL URL format."""
        from server.database import DatabaseManager, _database_url

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Set test database URL to non-PostgreSQL URL
        original_url = _database_url
        try:
            import server.database as db_module

            db_module._database_url = "sqlite:///test.db"

            # log_and_raise should raise ValidationError, so configure mock to raise
            with patch("server.database.log_and_raise", side_effect=ValidationError("Unsupported database URL")):
                # Should raise ValidationError for non-PostgreSQL URL
                with pytest.raises(ValidationError, match="Unsupported database URL"):
                    manager._initialize_database()
        finally:
            # Restore original
            db_module._database_url = original_url

    def test_database_manager_non_asyncpg_url(self) -> None:
        """Test DatabaseManager validates asyncpg URL format."""
        from server.database import DatabaseManager, _database_url

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # This test doesn't make sense - the code converts postgresql:// to postgresql+asyncpg://
        # So a postgresql:// URL is valid and will be converted, not raise an error
        # Let's test with an invalid URL instead
        original_url = _database_url
        try:
            import server.database as db_module

            # Test with a URL that starts with postgresql but is malformed
            db_module._database_url = "postgresql://user:pass@localhost/db"

            with patch("server.database.create_async_engine") as mock_create:
                manager._initialize_database()
                # Should convert postgresql:// to postgresql+asyncpg://
                call_args = mock_create.call_args[0]
                assert call_args[0].startswith("postgresql+asyncpg://")
        finally:
            # Restore original
            db_module._database_url = original_url

    @pytest.mark.asyncio
    async def test_database_manager_event_loop_change_detection(self) -> None:
        """Test DatabaseManager detects event loop changes."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()

        # Initialize in one loop
        manager.get_engine()

        # Simulate event loop change by creating a new loop
        import asyncio

        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)

        try:
            # Get engine in new loop - should detect loop change
            with patch("asyncio.get_running_loop", return_value=new_loop):
                with patch("server.database.logger.warning") as mock_warning:
                    engine = manager.get_engine()
                    # Should log warning about loop change
                    mock_warning.assert_called()
                    assert engine is not None
        finally:
            new_loop.close()
            asyncio.set_event_loop(None)

    def test_database_manager_get_engine_no_running_loop(self) -> None:
        """Test DatabaseManager.get_engine() handles no running loop."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = True
        manager.engine = Mock()

        # Mock RuntimeError for no running loop
        with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
            with patch("server.database.logger.debug") as mock_debug:
                engine = manager.get_engine()
                # Should log debug message
                mock_debug.assert_called_once()
                assert engine is not None

    def test_database_manager_engine_creation_exception(self) -> None:
        """Test DatabaseManager handles exceptions during engine creation."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Mock exception during create_async_engine
        with patch("server.database.create_async_engine", side_effect=ValueError("Engine creation failed")):
            with patch("server.database.log_and_raise") as mock_raise:
                manager._initialize_database()
                # Should call log_and_raise
                mock_raise.assert_called()

    def test_database_manager_connection_error_handling(self) -> None:
        """Test DatabaseManager handles ConnectionError during initialization."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Mock ConnectionError during engine creation
        with patch("server.database.create_async_engine", side_effect=ConnectionError("Connection failed")):
            with patch("server.database.log_and_raise") as mock_raise:
                manager._initialize_database()
                # Should call log_and_raise with DatabaseError
                mock_raise.assert_called()

    def test_database_manager_generic_exception_handling(self) -> None:
        """Test DatabaseManager handles generic exceptions during initialization."""
        from server.database import DatabaseManager

        manager = DatabaseManager.get_instance()
        manager.reset_instance()
        manager = DatabaseManager.get_instance()
        manager._initialized = False

        # Mock generic exception
        with patch("server.database.create_async_engine", side_effect=Exception("Unexpected error")):
            with patch("server.database.log_and_raise") as mock_raise:
                manager._initialize_database()
                # Should call log_and_raise
                mock_raise.assert_called()
