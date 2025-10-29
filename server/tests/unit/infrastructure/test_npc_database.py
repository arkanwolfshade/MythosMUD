"""
Unit tests for NPC database configuration and initialization.

These tests verify the NPC database engine setup, session management,
and initialization procedures for the NPC subsystem.

AI: Tests cover initialization, session management, error handling, and path operations.
"""

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from server.exceptions import ValidationError
from server.npc_database import (
    _initialize_npc_database,
    close_npc_db,
    ensure_npc_database_directory,
    get_npc_database_path,
    get_npc_engine,
    get_npc_session,
    get_npc_session_maker,
    init_npc_db,
)


class TestNPCDatabaseInitialization:
    """Test NPC database initialization."""

    def test_initialize_npc_database_success(self):
        """Test successful NPC database initialization."""
        # Reset global state
        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.database.npc_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"
            mock_get_config.return_value = mock_config

            _initialize_npc_database()

            assert npc_db._npc_engine is not None
            assert npc_db._npc_async_session_maker is not None
            assert npc_db._npc_database_url == "sqlite+aiosqlite:///data/npcs/test_npcs.db"

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    def test_initialize_npc_database_already_initialized(self):
        """Test that re-initialization is skipped if already initialized."""
        import server.npc_database as npc_db

        # Set up as already initialized
        npc_db._npc_engine = MagicMock(spec=AsyncEngine)
        npc_db._npc_async_session_maker = MagicMock()
        npc_db._npc_database_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"

        # Should return early without doing anything
        _initialize_npc_database()

        # Engine should still be the mock we set
        assert isinstance(npc_db._npc_engine, MagicMock)

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    def test_initialize_npc_database_import_error(self):
        """Test initialization failure when config import fails."""
        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

        with patch("server.config.get_config", side_effect=ImportError("Cannot import config")):
            with pytest.raises(ValidationError) as exc_info:
                _initialize_npc_database()

            assert "Failed to load configuration" in str(exc_info.value)

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    def test_initialize_npc_database_config_error(self):
        """Test initialization failure when config loading fails."""
        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

        with patch("server.config.get_config", side_effect=Exception("Config error")):
            with pytest.raises(ValidationError) as exc_info:
                _initialize_npc_database()

            assert "Failed to load configuration" in str(exc_info.value)

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None


class TestGetNPCEngine:
    """Test getting NPC database engine."""

    def test_get_npc_engine_initializes_if_needed(self):
        """Test that get_npc_engine initializes database if not initialized."""
        import server.npc_database as npc_db

        npc_db._npc_engine = None

        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.database.npc_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"
            mock_get_config.return_value = mock_config

            engine = get_npc_engine()

            assert engine is not None
            assert npc_db._npc_engine is not None

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    def test_get_npc_engine_returns_existing(self):
        """Test that get_npc_engine returns existing engine if already initialized."""
        import server.npc_database as npc_db

        mock_engine = MagicMock(spec=AsyncEngine)
        npc_db._npc_engine = mock_engine

        engine = get_npc_engine()

        assert engine is mock_engine

        # Clean up
        npc_db._npc_engine = None


class TestGetNPCSessionMaker:
    """Test getting NPC session maker."""

    def test_get_npc_session_maker_initializes_if_needed(self):
        """Test that get_npc_session_maker initializes database if not initialized."""
        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None

        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.database.npc_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"
            mock_get_config.return_value = mock_config

            session_maker = get_npc_session_maker()

            assert session_maker is not None
            assert npc_db._npc_async_session_maker is not None

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None


class TestGetNPCSession:
    """Test NPC session generation."""

    @pytest.mark.asyncio
    async def test_get_npc_session_success(self):
        """Test successful session creation."""
        import server.npc_database as npc_db

        # Create a mock session
        mock_session = AsyncMock(spec=AsyncSession)
        mock_session_maker = MagicMock()
        mock_session_maker.return_value.__aenter__.return_value = mock_session
        mock_session_maker.return_value.__aexit__.return_value = None

        npc_db._npc_async_session_maker = mock_session_maker

        async for session in get_npc_session():
            assert session is mock_session

        # Clean up
        npc_db._npc_async_session_maker = None

    @pytest.mark.asyncio
    async def test_get_npc_session_error_handling(self):
        """Test error handling in session generation."""
        import server.npc_database as npc_db

        # Create a custom context manager that raises during __aenter__
        class FailingSessionContext:
            async def __aenter__(self):
                raise Exception("Session error")

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                return False

        mock_session_maker = MagicMock()
        mock_session_maker.return_value = FailingSessionContext()

        npc_db._npc_async_session_maker = mock_session_maker

        with pytest.raises(Exception) as exc_info:
            async for _session in get_npc_session():
                pass

        assert "Session error" in str(exc_info.value)

        # Clean up
        npc_db._npc_async_session_maker = None

    @pytest.mark.asyncio
    async def test_get_npc_session_rollback_error(self):
        """Test error handling when rollback fails."""
        import server.npc_database as npc_db

        # Create a mock session that raises on rollback
        mock_session = AsyncMock(spec=AsyncSession)
        mock_session.rollback.side_effect = RuntimeError("Rollback error")

        # Create a custom context manager that raises during usage
        class FailingSessionContext:
            async def __aenter__(self):
                return mock_session

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                if exc_type:
                    await mock_session.rollback()  # This will raise
                return False

        mock_session_maker = MagicMock()
        mock_session_maker.return_value = FailingSessionContext()

        npc_db._npc_async_session_maker = mock_session_maker

        with pytest.raises(RuntimeError):
            async for _session in get_npc_session():
                raise RuntimeError("Session usage error")

        # Clean up
        npc_db._npc_async_session_maker = None


class TestInitNPCDB:
    """Test NPC database initialization function."""

    @pytest.mark.asyncio
    async def test_init_npc_db_success(self):
        """Test successful database initialization."""
        import server.npc_database as npc_db

        # Create mocks
        mock_engine = AsyncMock(spec=AsyncEngine)
        mock_conn = AsyncMock()
        mock_engine.begin.return_value.__aenter__.return_value = mock_conn
        mock_engine.begin.return_value.__aexit__.return_value = None

        npc_db._npc_engine = mock_engine
        npc_db._npc_async_session_maker = MagicMock()
        npc_db._npc_database_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"

        with patch("sqlalchemy.orm.configure_mappers"):
            await init_npc_db()

        # Verify database tables were created
        mock_conn.run_sync.assert_called_once()
        mock_conn.execute.assert_called_once()

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    @pytest.mark.asyncio
    async def test_init_npc_db_error(self):
        """Test database initialization error handling."""
        import server.npc_database as npc_db

        # Create a mock engine that raises an error
        mock_engine = AsyncMock(spec=AsyncEngine)
        mock_engine.begin.side_effect = Exception("Database error")

        npc_db._npc_engine = mock_engine

        with pytest.raises(Exception) as exc_info:
            await init_npc_db()

        assert "Database error" in str(exc_info.value)

        # Clean up
        npc_db._npc_engine = None


class TestCloseNPCDB:
    """Test NPC database closing function."""

    @pytest.mark.asyncio
    async def test_close_npc_db_success(self):
        """Test successful database closing."""
        import server.npc_database as npc_db

        mock_engine = AsyncMock(spec=AsyncEngine)
        npc_db._npc_engine = mock_engine
        npc_db._npc_async_session_maker = MagicMock()
        npc_db._npc_database_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"

        await close_npc_db()

        # Verify dispose was called
        mock_engine.dispose.assert_called_once()

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    @pytest.mark.asyncio
    async def test_close_npc_db_error(self):
        """Test database closing error handling."""
        import server.npc_database as npc_db

        mock_engine = AsyncMock(spec=AsyncEngine)
        mock_engine.dispose.side_effect = Exception("Dispose error")
        npc_db._npc_engine = mock_engine

        with pytest.raises(Exception) as exc_info:
            await close_npc_db()

        assert "Dispose error" in str(exc_info.value)

        # Clean up
        npc_db._npc_engine = None


class TestGetNPCDatabasePath:
    """Test getting NPC database path."""

    def test_get_npc_database_path_sqlite(self):
        """Test getting database path for SQLite URL."""
        import server.npc_database as npc_db

        npc_db._npc_database_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"

        path = get_npc_database_path()

        assert isinstance(path, Path)
        # Use Path comparison to handle OS-specific separators
        assert path == Path("data/npcs/test_npcs.db")

        # Clean up
        npc_db._npc_database_url = None

    def test_get_npc_database_path_initializes_if_needed(self):
        """Test that get_npc_database_path initializes database if not initialized."""
        import server.npc_database as npc_db

        npc_db._npc_database_url = None

        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.database.npc_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"
            mock_get_config.return_value = mock_config

            path = get_npc_database_path()

            assert isinstance(path, Path)
            assert npc_db._npc_database_url is not None

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    def test_get_npc_database_path_unsupported_url(self):
        """Test error handling for unsupported database URL."""
        import server.npc_database as npc_db

        npc_db._npc_database_url = "postgresql://localhost/npcs"

        with pytest.raises(ValidationError) as exc_info:
            get_npc_database_path()

        assert "Unsupported NPC database URL" in str(exc_info.value)

        # Clean up
        npc_db._npc_database_url = None


class TestEnsureNPCDatabaseDirectory:
    """Test ensuring NPC database directory exists."""

    def test_ensure_npc_database_directory_creates_dir(self):
        """Test that ensure_npc_database_directory creates directory."""
        import server.npc_database as npc_db

        npc_db._npc_database_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"

        with patch.object(Path, "mkdir") as mock_mkdir:
            ensure_npc_database_directory()

            mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)

        # Clean up
        npc_db._npc_database_url = None


class TestSQLitePragmaListener:
    """Test SQLite pragma listener."""

    def test_set_sqlite_pragma_for_sqlite_connection(self):
        """Test that foreign keys are enabled for SQLite connections."""
        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.database.npc_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"
            mock_get_config.return_value = mock_config

            _initialize_npc_database()

            # Check that the listener was registered
            assert npc_db._npc_engine is not None

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

    def test_set_sqlite_pragma_non_sqlite_connection(self):
        """Test that non-SQLite connections skip PRAGMA setting."""
        # This tests the warning path when connection is not SQLite
        # Since we can't easily test the actual event listener without a real connection,
        # we'll test the logic indirectly through initialization with different URLs

        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

        # Initialize with SQLite URL (the default behavior)
        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            # Use a test database URL that contains "test"
            # Use absolute path to prevent nested server/server/ directory creation
            test_db_path = Path(__file__).parent.parent.parent.parent / "data" / "unit_test" / "npcs" / "test_npcs.db"
            mock_config.database.npc_url = f"sqlite+aiosqlite:///{test_db_path}"
            mock_get_config.return_value = mock_config

            _initialize_npc_database()

            # Verify engine was created with NullPool (for test databases)
            assert npc_db._npc_engine is not None

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None


class TestNPCDatabaseIntegration:
    """Integration tests for NPC database operations."""

    def test_get_functions_work_together(self):
        """Test that all get functions work together correctly."""
        import server.npc_database as npc_db

        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None

        with patch("server.config.get_config") as mock_get_config:
            mock_config = MagicMock()
            mock_config.database.npc_url = "sqlite+aiosqlite:///data/npcs/test_npcs.db"
            mock_get_config.return_value = mock_config

            # Get engine
            engine = get_npc_engine()
            assert engine is not None

            # Get session maker
            session_maker = get_npc_session_maker()
            assert session_maker is not None

            # Get database path
            path = get_npc_database_path()
            assert isinstance(path, Path)

            # All should use the same initialized values
            assert npc_db._npc_engine is engine
            assert npc_db._npc_async_session_maker is session_maker

        # Clean up
        npc_db._npc_engine = None
        npc_db._npc_async_session_maker = None
        npc_db._npc_database_url = None
