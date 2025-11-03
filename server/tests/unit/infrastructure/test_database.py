"""
Tests for database configuration and session management.

This module tests the database connection, session management,
and initialization functionality in database.py.
"""

import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, Mock, patch

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
    metadata,
)
from server.exceptions import ValidationError


class TestDatabaseConfiguration:
    """Test database configuration constants and setup."""

    def test_database_path_default(self):
        """Test default database path from configuration."""
        # The actual value set by conftest.py uses an absolute path
        # Check that it contains the expected path components (handle both Windows and Unix paths)
        # Test environment sets DATABASE_URL to data/unit_test/players/unit_test_players.db
        db_path = get_database_path()
        assert "data/unit_test/players/unit_test_players.db" in str(db_path).replace("\\", "/")

    def test_metadata_exists(self):
        """Test that metadata is properly initialized."""
        assert metadata is not None
        assert hasattr(metadata, "tables")

    def test_engine_initialization(self):
        """Test that engine is properly initialized."""
        engine = get_engine()
        assert engine is not None
        # Engine should be created with aiosqlite
        assert "aiosqlite" in str(engine.url)

    def test_session_maker_initialization(self):
        """Test that session maker is properly initialized."""
        session_maker = get_session_maker()
        assert session_maker is not None
        assert hasattr(session_maker, "kw")  # Session maker has configuration


class TestGetDatabasePath:
    """Test database path extraction functionality."""

    def test_get_database_path_sqlite(self):
        """Test getting database path for SQLite URL."""
        # Patch the private _database_url variable after initialization
        with patch("server.database._database_url", "sqlite+aiosqlite:///path/to/db.db"):
            result = get_database_path()

            assert isinstance(result, Path)
            assert result.as_posix() == "path/to/db.db"

    def test_get_database_path_with_relative_path(self):
        """Test getting database path with relative path."""
        with patch("server.database._database_url", "sqlite+aiosqlite:///./relative/path.db"):
            result = get_database_path()

            assert isinstance(result, Path)
            assert result.as_posix() == "relative/path.db"

    def test_get_database_path_with_absolute_path(self):
        """Test getting database path with absolute path."""
        with patch("server.database._database_url", "sqlite+aiosqlite:////absolute/path.db"):
            result = get_database_path()

            assert isinstance(result, Path)
            assert result.as_posix() == "/absolute/path.db"

    def test_get_database_path_unsupported_url(self):
        """Test getting database path with unsupported URL."""
        with patch("server.database._database_url", "postgresql://user:pass@localhost/db"):
            with pytest.raises(ValidationError) as exc_info:
                get_database_path()

            assert "Unsupported database URL" in str(exc_info.value)

    def test_get_database_path_mysql_url(self):
        """Test getting database path with MySQL URL."""
        with patch("server.database._database_url", "mysql://user:pass@localhost/db"):
            with pytest.raises(ValidationError) as exc_info:
                get_database_path()

            assert "Unsupported database URL" in str(exc_info.value)


class TestEnsureDatabaseDirectory:
    """Test database directory creation functionality."""

    def test_ensure_database_directory_creates_parent(self):
        """Test that database directory is created if it doesn't exist."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "nonexistent" / "subdir" / "db.db"

            with patch("server.database.get_database_path", return_value=db_path):
                ensure_database_directory()

                assert db_path.parent.exists()

    def test_ensure_database_directory_existing(self):
        """Test that database directory creation works with existing directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "existing" / "db.db"
            db_path.parent.mkdir(parents=True)

            with patch("server.database.get_database_path", return_value=db_path):
                ensure_database_directory()

                assert db_path.parent.exists()

    def test_ensure_database_directory_nested(self):
        """Test that deeply nested database directories are created."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "level1" / "level2" / "level3" / "db.db"

            with patch("server.database.get_database_path", return_value=db_path):
                ensure_database_directory()

                assert db_path.parent.exists()


class TestGetAsyncSession:
    """Test async session management functionality."""

    @pytest.mark.asyncio
    async def test_get_async_session_yields_session(self):
        """Test that get_async_session yields a session."""
        session_count = 0

        async for session in get_async_session():
            session_count += 1
            assert isinstance(session, AsyncSession)
            break

        assert session_count == 1

    @pytest.mark.asyncio
    async def test_get_async_session_closes_session(self):
        """Test that session is properly closed."""
        session = None

        async for s in get_async_session():
            session = s
            break

        # Session should be closed after the context manager
        assert session is not None

    @pytest.mark.asyncio
    async def test_get_async_session_exception_handling(self):
        """Test that exceptions are properly handled."""
        from unittest.mock import MagicMock

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
    async def test_init_db_creates_tables(self):
        """Test that init_db creates all tables."""
        from unittest.mock import MagicMock

        # Create properly configured mocks for async engine operations
        mock_conn = AsyncMock()

        # Create a mock async context manager
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_conn)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create a mock engine with async begin() that returns the context manager
        mock_engine = MagicMock()
        mock_engine.begin = MagicMock(return_value=mock_context_manager)

        with patch("server.database.get_engine", return_value=mock_engine):
            # Mock the connection manager to prevent unawaited coroutines
            with patch("server.realtime.connection_manager.connection_manager"):
                await init_db()

                # Verify that create_all was called
                mock_conn.run_sync.assert_called_once()
                call_args = mock_conn.run_sync.call_args[0]
                assert call_args[0] == metadata.create_all

    @pytest.mark.asyncio
    @pytest.mark.filterwarnings("ignore:coroutine.*was never awaited:RuntimeWarning")
    async def test_init_db_imports_models(self):
        """Test that init_db imports all required models."""
        from unittest.mock import MagicMock

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
            # Mock the global connection_manager instance to avoid creating unawaited coroutines
            with patch("server.realtime.connection_manager.connection_manager"):
                # Mock the specific imports that init_db makes
                with patch("server.models.invite.Invite"):
                    with patch("server.models.npc.NPCDefinition"):
                        with patch("server.models.npc.NPCSpawnRule"):
                            with patch("server.models.player.Player"):
                                with patch("server.models.user.User"):
                                    with patch("server.models.relationships.setup_relationships"):
                                        # Mock the configure_mappers function
                                        with patch("sqlalchemy.orm.configure_mappers"):
                                            await init_db()

                # Test passes if no exceptions are raised during init_db

    @pytest.mark.asyncio
    async def test_init_db_engine_begin_failure(self):
        """Test init_db when engine.begin() fails."""
        from unittest.mock import MagicMock

        mock_engine = MagicMock()
        mock_engine.begin.side_effect = RuntimeError("Engine error")

        with patch("server.database.get_engine", return_value=mock_engine):
            with pytest.raises(RuntimeError):
                await init_db()


class TestCloseDB:
    """Test database connection closing functionality."""

    @pytest.mark.asyncio
    async def test_close_db_disposes_engine(self):
        """Test that close_db disposes the engine."""
        mock_engine = AsyncMock()
        mock_engine.dispose = AsyncMock()

        with patch("server.database.get_database_manager") as mock_get_mgr:
            mock_mgr = Mock()
            mock_mgr.engine = mock_engine
            mock_mgr.get_engine = Mock(return_value=mock_engine)
            mock_mgr.close = AsyncMock()
            mock_get_mgr.return_value = mock_mgr

            await close_db()

            mock_mgr.close.assert_called_once()

    @pytest.mark.asyncio
    async def test_close_db_engine_dispose_failure(self):
        """Test close_db when engine.dispose() fails."""
        mock_engine = AsyncMock()

        with patch("server.database.get_database_manager") as mock_get_mgr:
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
    async def test_database_lifecycle(self):
        """Test complete database lifecycle."""
        from unittest.mock import MagicMock

        # Create properly configured mocks
        mock_conn = AsyncMock()

        # Create a mock async context manager
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_conn)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create a mock engine with begin() that returns the context manager
        mock_engine = MagicMock()
        mock_engine.begin = MagicMock(return_value=mock_context_manager)
        mock_engine.dispose = AsyncMock()

        with patch("server.database.get_database_manager") as mock_get_mgr:
            mock_mgr = Mock()
            mock_mgr.engine = mock_engine
            mock_mgr.get_engine = Mock(return_value=mock_engine)
            mock_mgr.close = AsyncMock()
            mock_get_mgr.return_value = mock_mgr

            with patch("server.database.get_engine", return_value=mock_engine):
                await init_db()
                mock_conn.run_sync.assert_called_once()

                # Test closing
                await close_db()
                mock_mgr.close.assert_called_once()

    def test_database_path_integration(self):
        """Test database path integration with directory creation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            db_path = Path(temp_dir) / "test" / "db.db"

            with patch("server.database.get_database_path", return_value=db_path):
                ensure_database_directory()

                assert db_path.parent.exists()
                assert str(db_path.parent) == str(Path(temp_dir) / "test")

    @pytest.mark.asyncio
    async def test_session_integration(self):
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

    def test_get_database_path_empty_url(self):
        """Test getting database path with empty URL."""
        with patch("server.database._database_url", ""):
            with pytest.raises(ValidationError):
                get_database_path()

    def test_get_database_path_malformed_url(self):
        """Test getting database path with malformed URL."""
        with patch("server.database._database_url", "not-a-url"):
            with pytest.raises(ValidationError):
                get_database_path()

    @pytest.mark.asyncio
    async def test_get_async_session_multiple_iterations(self):
        """Test multiple iterations of get_async_session."""
        sessions = []

        async for session in get_async_session():
            sessions.append(session)
            if len(sessions) >= 3:  # Limit to prevent infinite loop
                break

        assert len(sessions) >= 1
        assert all(isinstance(s, AsyncSession) for s in sessions)

    def test_ensure_database_directory_permissions(self):
        """Test database directory creation with permission issues."""
        with patch("pathlib.Path.mkdir") as mock_mkdir:
            mock_mkdir.side_effect = PermissionError("Permission denied")

            with pytest.raises(PermissionError):
                ensure_database_directory()
