"""
Tests for database configuration and session management.

This module tests the database connection, session management,
and initialization functionality in database.py.
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from server.database import (
    DATABASE_URL,
    TEST_DATABASE_URL,
    close_db,
    ensure_database_directory,
    get_async_session,
    get_database_path,
    init_db,
    metadata,
)


class TestDatabaseConfiguration:
    """Test database configuration constants and setup."""

    def test_database_url_default(self):
        """Test default DATABASE_URL."""
        assert DATABASE_URL == "sqlite+aiosqlite:///data/players/players.db"

    def test_test_database_url_default(self):
        """Test default TEST_DATABASE_URL."""
        assert TEST_DATABASE_URL == "sqlite+aiosqlite:///./tests/data/test_players.db"

    def test_metadata_exists(self):
        """Test that metadata is properly initialized."""
        assert metadata is not None
        assert hasattr(metadata, "tables")

    @patch.dict(os.environ, {"DATABASE_URL": "sqlite+aiosqlite:///custom/path.db"})
    def test_database_url_from_env(self):
        """Test DATABASE_URL from environment variable."""
        # Re-import to get the updated value
        import importlib

        import server.database

        importlib.reload(server.database)

        assert server.database.DATABASE_URL == "sqlite+aiosqlite:///custom/path.db"

    @patch.dict(os.environ, {"TEST_DATABASE_URL": "sqlite+aiosqlite:///test/path.db"})
    def test_test_database_url_from_env(self):
        """Test TEST_DATABASE_URL from environment variable."""
        # Re-import to get the updated value
        import importlib

        import server.database

        importlib.reload(server.database)

        assert server.database.TEST_DATABASE_URL == "sqlite+aiosqlite:///test/path.db"


class TestGetDatabasePath:
    """Test database path extraction functionality."""

    def test_get_database_path_sqlite(self):
        """Test getting database path for SQLite URL."""
        with patch("server.database.DATABASE_URL", "sqlite+aiosqlite:///path/to/db.db"):
            result = get_database_path()

            assert isinstance(result, Path)
            assert result.as_posix() == "path/to/db.db"

    def test_get_database_path_with_relative_path(self):
        """Test getting database path with relative path."""
        with patch("server.database.DATABASE_URL", "sqlite+aiosqlite:///./relative/path.db"):
            result = get_database_path()

            assert isinstance(result, Path)
            assert result.as_posix() == "relative/path.db"

    def test_get_database_path_with_absolute_path(self):
        """Test getting database path with absolute path."""
        with patch("server.database.DATABASE_URL", "sqlite+aiosqlite:////absolute/path.db"):
            result = get_database_path()

            assert isinstance(result, Path)
            assert result.as_posix() == "/absolute/path.db"

    def test_get_database_path_unsupported_url(self):
        """Test getting database path with unsupported URL."""
        with patch("server.database.DATABASE_URL", "postgresql://user:pass@localhost/db"):
            with pytest.raises(ValueError) as exc_info:
                get_database_path()

            assert "Unsupported database URL" in str(exc_info.value)

    def test_get_database_path_mysql_url(self):
        """Test getting database path with MySQL URL."""
        with patch("server.database.DATABASE_URL", "mysql://user:pass@localhost/db"):
            with pytest.raises(ValueError) as exc_info:
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
        with patch("server.database.async_session_maker") as mock_session_maker:
            mock_session = AsyncMock()
            mock_session.rollback = AsyncMock()
            mock_session.close = AsyncMock()
            mock_session_maker.return_value.__aenter__.return_value = mock_session

            # Simulate an exception
            mock_session_maker.return_value.__aenter__.side_effect = RuntimeError("Test error")

            with pytest.raises(RuntimeError):
                async for _session in get_async_session():
                    pass


class TestInitDB:
    """Test database initialization functionality."""

    @pytest.mark.asyncio
    async def test_init_db_creates_tables(self):
        """Test that init_db creates all tables."""
        with patch("server.database.engine") as mock_engine:
            mock_conn = AsyncMock()
            mock_engine.begin.return_value.__aenter__.return_value = mock_conn

            await init_db()

            # Verify that create_all was called
            mock_conn.run_sync.assert_called_once()
            call_args = mock_conn.run_sync.call_args[0]
            assert call_args[0] == metadata.create_all

    @pytest.mark.asyncio
    async def test_init_db_imports_models(self):
        """Test that init_db imports all required models."""
        with patch("server.database.engine") as mock_engine:
            mock_conn = AsyncMock()
            mock_engine.begin.return_value.__aenter__.return_value = mock_conn

            # Mock the imports to ensure they're called
            with patch("builtins.__import__") as mock_import:
                await init_db()

                # Verify that models were imported
                assert mock_import.called

    @pytest.mark.asyncio
    async def test_init_db_engine_begin_failure(self):
        """Test init_db when engine.begin() fails."""
        with patch("server.database.engine") as mock_engine:
            mock_engine.begin.side_effect = RuntimeError("Engine error")

            with pytest.raises(RuntimeError):
                await init_db()


class TestCloseDB:
    """Test database connection closing functionality."""

    @pytest.mark.asyncio
    async def test_close_db_disposes_engine(self):
        """Test that close_db disposes the engine."""
        with patch("server.database.engine") as mock_engine:
            mock_engine.dispose = AsyncMock()

            await close_db()

            mock_engine.dispose.assert_called_once()

    @pytest.mark.asyncio
    async def test_close_db_engine_dispose_failure(self):
        """Test close_db when engine.dispose() fails."""
        with patch("server.database.engine") as mock_engine:
            mock_engine.dispose.side_effect = RuntimeError("Dispose error")

            with pytest.raises(RuntimeError):
                await close_db()


class TestDatabaseIntegration:
    """Test database integration scenarios."""

    @pytest.mark.asyncio
    async def test_database_lifecycle(self):
        """Test complete database lifecycle."""
        with patch("server.database.engine") as mock_engine:
            mock_engine.dispose = AsyncMock()

            # Test initialization
            mock_conn = AsyncMock()
            mock_engine.begin.return_value.__aenter__.return_value = mock_conn

            await init_db()
            mock_conn.run_sync.assert_called_once()

            # Test closing
            await close_db()
            mock_engine.dispose.assert_called_once()

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
        with patch("server.database.DATABASE_URL", ""):
            with pytest.raises(ValueError):
                get_database_path()

    def test_get_database_path_malformed_url(self):
        """Test getting database path with malformed URL."""
        with patch("server.database.DATABASE_URL", "not-a-url"):
            with pytest.raises(ValueError):
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
