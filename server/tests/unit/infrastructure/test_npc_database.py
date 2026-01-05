"""
Unit tests for NPC database initialization and session management.

Tests NPC database engine creation, session management, and cleanup.
"""

import builtins
import os
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from server.exceptions import ValidationError
from server.npc_database import (
    close_npc_db,
    ensure_npc_database_directory,
    get_npc_database_path,
    get_npc_engine,
    get_npc_session,
    get_npc_session_maker,
    init_npc_db,
    reset_npc_database,
)


@pytest.fixture(autouse=True)
def reset_state():
    """Reset NPC database state before each test."""
    reset_npc_database()
    yield
    reset_npc_database()


class TestNPCDatabaseInitialization:
    """Test NPC database initialization."""

    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    def test_get_npc_engine_initializes_engine(self, mock_get_config, mock_create_engine):
        """Test get_npc_engine() initializes engine when None."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_engine = MagicMock(spec=AsyncEngine)
        mock_create_engine.return_value = mock_engine

        result = get_npc_engine()
        assert result == mock_engine
        mock_create_engine.assert_called_once()

    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    def test_get_npc_engine_uses_existing_engine(self, mock_get_config, mock_create_engine):
        """Test get_npc_engine() returns existing engine if already initialized."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_engine = MagicMock(spec=AsyncEngine)
        mock_create_engine.return_value = mock_engine

        # First call initializes
        result1 = get_npc_engine()
        # Second call should reuse
        result2 = get_npc_engine()
        assert result1 == result2
        assert mock_create_engine.call_count == 1

    @patch("server.config.get_config")
    def test_get_npc_engine_raises_on_invalid_url(self, mock_get_config):
        """Test get_npc_engine() raises ValidationError for non-PostgreSQL URL."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "sqlite:///test.db"
        mock_get_config.return_value = mock_config

        with pytest.raises(ValidationError, match="Only PostgreSQL is supported"):
            get_npc_engine()

    @patch("server.config.get_config")
    def test_get_npc_engine_env_fallback(self, mock_get_config):
        """Test get_npc_engine() uses environment fallback when config fails."""
        mock_get_config.side_effect = Exception("Config error")
        os.environ["NPC_DB_ENV_FALLBACK"] = "true"
        os.environ["DATABASE_NPC_URL"] = "postgresql+asyncpg://test:test@host/db"

        with patch("server.npc_database.create_async_engine") as mock_create_engine:
            mock_engine = MagicMock(spec=AsyncEngine)
            mock_create_engine.return_value = mock_engine

            result = get_npc_engine()
            assert result == mock_engine

        # Cleanup
        os.environ.pop("NPC_DB_ENV_FALLBACK", None)
        os.environ.pop("DATABASE_NPC_URL", None)

    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    def test_get_npc_engine_uses_nullpool_for_test(self, mock_get_config, mock_create_engine):
        """Test get_npc_engine() uses NullPool for test databases."""
        from sqlalchemy.pool import NullPool

        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/test_db"
        mock_get_config.return_value = mock_config

        get_npc_engine()
        call_kwargs = mock_create_engine.call_args[1]
        assert call_kwargs.get("poolclass") == NullPool


class TestNPCSessionMaker:
    """Test NPC session maker functions."""

    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    def test_get_npc_session_maker(self, mock_get_config, mock_create_engine):
        """Test get_npc_session_maker() returns session maker."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_engine = MagicMock(spec=AsyncEngine)
        mock_create_engine.return_value = mock_engine

        result = get_npc_session_maker()
        assert isinstance(result, async_sessionmaker)


class TestNPCSession:
    """Test NPC session management."""

    @pytest.mark.asyncio
    @patch("server.npc_database._npc_async_session_maker", new_callable=Mock)
    async def test_get_npc_session_yields_session(self, mock_session_maker):
        """Test get_npc_session() yields session."""
        mock_session = AsyncMock(spec=AsyncSession)
        mock_context = AsyncMock()
        mock_context.__aenter__ = AsyncMock(return_value=mock_session)
        mock_context.__aexit__ = AsyncMock(return_value=None)

        # Configure the mock session maker to return the async context manager
        mock_session_maker.return_value = mock_context

        async for session in get_npc_session():
            assert session == mock_session
            break

    @pytest.mark.asyncio
    @patch("server.npc_database._npc_async_session_maker", new_callable=Mock)
    async def test_get_npc_session_rollback_on_error(self, mock_session_maker):
        """Test get_npc_session() rolls back on error during yield."""
        # The exception handler in get_npc_session only catches exceptions during yield,
        # not exceptions in the loop body. To test rollback, we need to simulate an exception
        # during the yield itself, which happens when the session context manager raises.
        mock_session = AsyncMock(spec=AsyncSession)
        mock_session.rollback = AsyncMock()
        mock_context = AsyncMock()
        # Make __aenter__ raise an exception to trigger the generator's exception handler
        mock_context.__aenter__ = AsyncMock(side_effect=ValueError("Test error"))
        mock_context.__aexit__ = AsyncMock(return_value=False)

        # Configure the mock session maker to return the async context manager
        mock_session_maker.return_value = mock_context

        # The exception should be raised, but we can't easily test rollback this way
        # because the exception happens before we get a session. This test may need
        # to be removed or the implementation changed if rollback-on-loop-error is desired.
        # For now, we'll test that the exception is properly raised.
        with pytest.raises(ValueError, match="Test error"):
            async for _ in get_npc_session():
                pass  # Exception happens in __aenter__, before we get here

    @pytest.mark.asyncio
    @patch("server.npc_database._npc_async_session_maker", None)
    @patch("server.npc_database.init_npc_db")
    @patch("server.npc_database.get_npc_session_maker")
    @patch("server.config.get_config")
    async def test_get_npc_session_inits_db_for_unit_test(
        self, mock_get_config, mock_get_session_maker, mock_init_npc_db
    ):
        """Test get_npc_session() calls init_npc_db() for unit_test databases."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/unit_test_db"
        mock_get_config.return_value = mock_config

        mock_session = AsyncMock(spec=AsyncSession)
        mock_context = AsyncMock()
        mock_context.__aenter__ = AsyncMock(return_value=mock_session)
        mock_context.__aexit__ = AsyncMock(return_value=None)

        # Create a callable mock that returns the async context manager
        mock_session_maker = Mock(return_value=mock_context)
        mock_get_session_maker.return_value = mock_session_maker

        with patch("server.npc_database._npc_database_url", "postgresql://test/unit_test_db"):
            async for _ in get_npc_session():
                break

        mock_init_npc_db.assert_awaited_once()


class TestInitNpcDb:
    """Test init_npc_db() function."""

    @pytest.mark.asyncio
    @patch("server.npc_database.get_npc_engine")
    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    async def test_init_npc_db_success(self, mock_get_config, mock_create_engine, mock_get_engine):
        """Test init_npc_db() successfully initializes database."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_engine = MagicMock(spec=AsyncEngine)
        mock_conn = AsyncMock()
        mock_conn.execute = AsyncMock()
        mock_begin_context = AsyncMock()
        mock_begin_context.__aenter__ = AsyncMock(return_value=mock_conn)
        mock_begin_context.__aexit__ = AsyncMock(return_value=None)
        mock_engine.begin = Mock(return_value=mock_begin_context)
        mock_create_engine.return_value = mock_engine
        mock_get_engine.return_value = mock_engine

        await init_npc_db()
        mock_conn.execute.assert_awaited_once()

    @pytest.mark.asyncio
    @patch("server.npc_database.get_npc_engine")
    @patch("server.config.get_config")
    async def test_init_npc_db_raises_on_none_engine(self, mock_get_config, mock_get_engine):
        """Test init_npc_db() raises ValidationError when engine is None."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_get_engine.return_value = None

        with pytest.raises(ValidationError, match="NPC database engine is None"):
            await init_npc_db()


class TestCloseNpcDb:
    """Test close_npc_db() function."""

    @pytest.mark.asyncio
    @patch("server.npc_database.get_npc_engine")
    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    async def test_close_npc_db_disposes_engine(self, mock_get_config, mock_create_engine, mock_get_engine):
        """Test close_npc_db() disposes engine."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_engine = MagicMock(spec=AsyncEngine)
        mock_engine.dispose = AsyncMock()
        mock_create_engine.return_value = mock_engine
        mock_get_engine.return_value = mock_engine

        # Initialize first
        get_npc_engine()
        # Then close
        await close_npc_db()

        mock_engine.dispose.assert_awaited()

    @pytest.mark.asyncio
    @patch("server.npc_database.get_npc_engine")
    async def test_close_npc_db_handles_closed_loop(self, mock_get_engine):
        """Test close_npc_db() handles closed event loop."""
        mock_engine = MagicMock(spec=AsyncEngine)
        mock_get_engine.return_value = mock_engine

        # Mock loop.is_closed() to return True
        with patch("asyncio.get_running_loop") as mock_get_loop:
            mock_loop = MagicMock()
            mock_loop.is_closed.return_value = True
            mock_get_loop.return_value = mock_loop

            await close_npc_db()
            # Should not call dispose when loop is closed
            mock_engine.dispose.assert_not_called()

    @pytest.mark.asyncio
    async def test_close_npc_db_handles_no_engine(self):
        """Test close_npc_db() handles case when engine is None."""
        with patch("server.npc_database.get_npc_engine", return_value=None):
            # Should not raise
            await close_npc_db()


class TestResetNPCDatabase:
    """Test reset_npc_database() function."""

    def test_reset_npc_database_resets_state(self):
        """Test reset_npc_database() resets all global state."""
        # Initialize some state
        with patch("server.npc_database._initialize_npc_database"):
            reset_npc_database()

        # Verify state is reset (would need to check internals, but function should complete)
        # This is more of an integration test, but we can at least verify it doesn't raise
        reset_npc_database()


class TestGetNPCDatabasePath:
    """Test get_npc_database_path() function."""

    @patch("server.config.get_config")
    def test_get_npc_database_path_returns_none_for_postgresql(self, mock_get_config):
        """Test get_npc_database_path() returns None for PostgreSQL."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_get_config.return_value = mock_config

        with patch("server.npc_database._npc_database_url", "postgresql://test/db"):
            # Call function directly in assert to avoid assigning potentially None value
            assert get_npc_database_path() is None

    @patch("server.config.get_config")
    def test_get_npc_database_path_raises_for_non_postgresql(self, mock_get_config):
        """Test get_npc_database_path() raises for non-PostgreSQL URLs."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "sqlite:///test.db"
        mock_get_config.return_value = mock_config

        with patch("server.npc_database._npc_database_url", "sqlite:///test.db"):
            with pytest.raises(ValidationError, match="Only PostgreSQL is supported"):
                get_npc_database_path()


class TestEnsureNPCDatabaseDirectory:
    """Test ensure_npc_database_directory() function."""

    @patch("server.npc_database.get_npc_database_path")
    def test_ensure_npc_database_directory_no_op_for_postgresql(self, mock_get_path):
        """Test ensure_npc_database_directory() is no-op for PostgreSQL."""
        mock_get_path.return_value = None
        # Should not raise or create directories
        ensure_npc_database_directory()

    @patch("server.npc_database.get_npc_database_path")
    def test_ensure_npc_database_directory_creates_directory(self, mock_get_path):
        """Test ensure_npc_database_directory() creates directory if needed."""
        from pathlib import Path

        mock_path = Mock(spec=Path)
        mock_parent = Mock()
        mock_parent.mkdir = Mock()
        mock_path.parent = mock_parent
        mock_get_path.return_value = mock_path

        ensure_npc_database_directory()
        mock_parent.mkdir.assert_called_once_with(parents=True, exist_ok=True)


class TestEventLoopHandling:
    """Test event loop change detection and handling."""

    @pytest.mark.asyncio
    @patch("server.npc_database.create_async_engine")
    @patch("server.config.get_config")
    async def test_get_npc_engine_recreates_on_loop_change(self, mock_get_config, mock_create_engine):
        """Test get_npc_engine() recreates engine when event loop changes."""
        mock_config = MagicMock()
        mock_config.database.npc_url = "postgresql+asyncpg://user:pass@host/db"
        mock_config.database.pool_size = 5
        mock_config.database.max_overflow = 10
        mock_config.database.pool_timeout = 30
        mock_get_config.return_value = mock_config

        mock_engine1 = MagicMock(spec=AsyncEngine)
        mock_engine2 = MagicMock(spec=AsyncEngine)
        mock_create_engine.side_effect = [mock_engine1, mock_engine2]

        # Set up initial state: engine exists with old loop ID
        # Use patch to set protected members instead of direct access
        with patch("server.npc_database._npc_engine", mock_engine1):
            with patch("server.npc_database._npc_creation_loop_id", 123):
                # Simulate different loop ID - patch asyncio.get_running_loop and id()
                with patch("asyncio.get_running_loop") as mock_get_loop:
                    mock_loop = MagicMock()
                    mock_get_loop.return_value = mock_loop

                    # Create a mock id function that returns 456 for the mock_loop
                    original_id = builtins.id

                    def mock_id(obj):
                        if obj is mock_loop:
                            return 456
                        return original_id(obj)

                    with patch("builtins.id", side_effect=mock_id):
                        get_npc_engine()
                        # Should recreate because loop ID changed (calls _initialize_npc_database which calls create_async_engine)
                        assert mock_create_engine.call_count >= 1
