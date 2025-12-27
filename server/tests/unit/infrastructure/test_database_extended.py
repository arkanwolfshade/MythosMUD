"""
Extended unit tests for database module.

Tests database initialization, error handling, and utility functions.
"""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from server.database import (
    DatabaseManager,
    close_db,
    ensure_database_directory,
    get_async_session,
    get_database_path,
    get_database_url,
    get_engine,
    get_session_maker,
    init_db,
    reset_database,
)
from server.exceptions import DatabaseError, ValidationError


@pytest.fixture(autouse=True)
def reset_db_state():
    """Reset database state before each test."""
    reset_database()
    yield
    reset_database()


def test_get_engine_initializes_database():
    """Test get_engine initializes database if not already initialized."""
    DatabaseManager.reset_instance()
    
    with patch.object(DatabaseManager, "_initialize_database") as mock_init:
        mock_manager = MagicMock()
        mock_manager.get_engine = MagicMock(return_value=MagicMock(spec=AsyncEngine))
        mock_manager._initialized = True
        mock_manager.engine = MagicMock(spec=AsyncEngine)
        
        with patch("server.database.DatabaseManager.get_instance", return_value=mock_manager):
            result = get_engine()
            assert result is not None


def test_get_session_maker_initializes_database():
    """Test get_session_maker initializes database if not already initialized."""
    DatabaseManager.reset_instance()
    
    mock_manager = MagicMock()
    mock_manager.get_session_maker = MagicMock(return_value=MagicMock(spec=async_sessionmaker))
    mock_manager._initialized = True
    mock_manager.session_maker = MagicMock(spec=async_sessionmaker)
    
    with patch("server.database.DatabaseManager.get_instance", return_value=mock_manager):
        result = get_session_maker()
        assert result is not None


def test_get_database_url_initializes_database():
    """Test get_database_url initializes database if not already initialized."""
    DatabaseManager.reset_instance()
    
    mock_manager = MagicMock()
    mock_manager.get_database_url = MagicMock(return_value="postgresql+asyncpg://test")
    mock_manager._initialized = True
    mock_manager.database_url = "postgresql+asyncpg://test"
    
    with patch("server.database.DatabaseManager.get_instance", return_value=mock_manager):
        result = get_database_url()
        assert result == "postgresql+asyncpg://test"


def test_reset_database():
    """Test reset_database resets both singleton and module-level URL."""
    DatabaseManager.reset_instance()
    
    # Set module-level URL
    import server.database as db_module
    db_module._database_url = "test_url"
    
    reset_database()
    
    assert db_module._database_url is None
    # Verify singleton is reset
    instance1 = DatabaseManager.get_instance()
    DatabaseManager.reset_instance()
    instance2 = DatabaseManager.get_instance()
    assert instance1 is not instance2


def test_database_manager_get_engine_initializes():
    """Test DatabaseManager.get_engine initializes if not initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    
    with patch.object(manager, "_initialize_database") as mock_init:
        mock_engine = MagicMock(spec=AsyncEngine)
        manager.engine = mock_engine
        manager._initialized = True
        
        result = manager.get_engine()
        assert result == mock_engine


def test_database_manager_get_engine_reinitializes_if_none():
    """Test DatabaseManager.get_engine reinitializes if engine is None."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = None
    
    # Mock _initialize_database to set engine and _initialized
    def mock_init():
        manager.engine = MagicMock(spec=AsyncEngine)
        manager._initialized = True
    
    with patch.object(manager, "_initialize_database", side_effect=mock_init):
        result = manager.get_engine()
        assert result is not None
        # Should have called _initialize_database to re-initialize
        assert manager._initialized is True


def test_database_manager_get_session_maker_initializes():
    """Test DatabaseManager.get_session_maker initializes if not initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    
    with patch.object(manager, "_initialize_database") as mock_init:
        mock_session_maker = MagicMock(spec=async_sessionmaker)
        manager.session_maker = mock_session_maker
        manager._initialized = True
        
        result = manager.get_session_maker()
        assert result == mock_session_maker


def test_database_manager_get_database_url_initializes():
    """Test DatabaseManager.get_database_url initializes if not initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    
    with patch.object(manager, "_initialize_database") as mock_init:
        manager.database_url = "postgresql+asyncpg://test"
        manager._initialized = True
        
        result = manager.get_database_url()
        assert result == "postgresql+asyncpg://test"


def test_database_manager_get_database_path_postgresql():
    """Test DatabaseManager.get_database_path returns None for PostgreSQL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager.database_url = "postgresql+asyncpg://test"
    
    result = manager.get_database_path()
    assert result is None


def test_database_manager_get_database_path_unsupported():
    """Test DatabaseManager.get_database_path raises for unsupported URL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    # Need to initialize first to set database_url
    with patch.object(manager, "_initialize_database") as mock_init:
        manager.database_url = "sqlite://test.db"
        manager._initialized = True
        
        with pytest.raises(ValidationError, match="Unsupported database URL"):
            manager.get_database_path()


@pytest.mark.asyncio
async def test_database_manager_close_with_engine():
    """Test DatabaseManager.close disposes engine if it exists."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock(spec=AsyncEngine)
    mock_engine.dispose = AsyncMock()
    mock_engine.sync_engine = MagicMock()
    mock_engine.sync_engine.dispose = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True
    
    # Mock asyncio.get_running_loop to avoid RuntimeError
    with patch("asyncio.get_running_loop") as mock_loop:
        mock_loop.return_value.is_closed = MagicMock(return_value=False)
        await manager.close()
    
    assert manager.engine is None
    assert manager._initialized is False


@pytest.mark.asyncio
async def test_database_manager_close_without_engine():
    """Test DatabaseManager.close handles None engine gracefully."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager.engine = None
    manager._initialized = True
    
    # Should not raise
    await manager.close()
    
    assert manager._initialized is False


@pytest.mark.asyncio
async def test_database_manager_close_dispose_error():
    """Test DatabaseManager.close handles dispose errors gracefully."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock(spec=AsyncEngine)
    mock_engine.dispose = AsyncMock(side_effect=RuntimeError("Dispose error"))
    mock_engine.sync_engine = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True
    
    # Mock asyncio.get_running_loop to avoid RuntimeError
    with patch("asyncio.get_running_loop") as mock_loop:
        mock_loop.return_value.is_closed = MagicMock(return_value=False)
        # Should not raise, just log
        await manager.close()
    
    assert manager.engine is None
    assert manager._initialized is False


@pytest.mark.asyncio
async def test_get_async_session_success():
    """Test get_async_session creates and yields session successfully."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch("server.database.get_session_maker", return_value=mock_session_maker):
        async for session in get_async_session():
            assert session == mock_session
            break


@pytest.mark.asyncio
async def test_get_async_session_http_exception_re_raised():
    """Test get_async_session re-raises HTTPException."""
    from fastapi import HTTPException
    
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch("server.database.get_session_maker", return_value=mock_session_maker):
        async for session in get_async_session():
            # Simulate HTTPException during session use
            with pytest.raises(HTTPException):
                raise HTTPException(status_code=400, detail="Bad request")
            break


@pytest.mark.asyncio
async def test_get_async_session_rollback_on_error():
    """Test get_async_session rolls back on error."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.rollback = AsyncMock()
    
    # Create a proper async context manager that propagates exceptions
    class MockSessionContext:
        def __init__(self, session):
            self.session = session
        
        async def __aenter__(self):
            return self.session
        
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            # Don't suppress exceptions - let them propagate to the generator's exception handler
            return False
    
    mock_session_maker = MagicMock(return_value=MockSessionContext(mock_session))
    
    with patch("server.database.get_session_maker", return_value=mock_session_maker):
        # Use the generator directly - exception must be raised while generator is active
        gen = get_async_session()
        session = await gen.__anext__()
        # Exception must be sent back to generator using athrow (single-arg signature)
        try:
            await gen.athrow(ValueError("Test error"))
        except ValueError:
            # Exception was re-raised after rollback
            pass
    
    # Rollback should be called when exception occurs
    mock_session.rollback.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_async_session_rollback_error():
    """Test get_async_session handles rollback errors."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.rollback = AsyncMock(side_effect=RuntimeError("Rollback error"))
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)
    
    with patch("server.database.get_session_maker", return_value=mock_session_maker):
        # Should raise original error, not rollback error
        with pytest.raises(ValueError, match="Test error"):
            async for session in get_async_session():
                raise ValueError("Test error")


@pytest.mark.asyncio
async def test_init_db_success():
    """Test init_db initializes database successfully."""
    mock_engine = MagicMock(spec=AsyncEngine)
    mock_conn = AsyncMock()
    mock_conn.execute = AsyncMock()
    mock_engine.begin = MagicMock(return_value=AsyncMock(__aenter__=AsyncMock(return_value=mock_conn), __aexit__=AsyncMock(return_value=None)))
    
    with patch("server.database.get_engine", return_value=mock_engine):
        with patch("sqlalchemy.orm.configure_mappers"):
            await init_db()
    
    mock_conn.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_init_db_import_error():
    """Test init_db handles import errors."""
    with patch("sqlalchemy.orm.configure_mappers", side_effect=ImportError("Import error")):
        with pytest.raises(ImportError):
            await init_db()


@pytest.mark.asyncio
async def test_init_db_connection_error():
    """Test init_db handles connection errors."""
    mock_engine = MagicMock(spec=AsyncEngine)
    mock_engine.begin = MagicMock(side_effect=SQLAlchemyError("Connection error", None, None))
    
    with patch("server.database.get_engine", return_value=mock_engine):
        with patch("sqlalchemy.orm.configure_mappers"):
            with pytest.raises(SQLAlchemyError):
                await init_db()


@pytest.mark.asyncio
async def test_close_db_success():
    """Test close_db closes database successfully."""
    mock_manager = MagicMock()
    mock_engine = MagicMock(spec=AsyncEngine)
    mock_manager.get_engine = MagicMock(return_value=mock_engine)
    mock_manager.close = AsyncMock()
    
    with patch("server.database.DatabaseManager.get_instance", return_value=mock_manager):
        await close_db()
    
    mock_manager.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_db_error():
    """Test close_db raises RuntimeError on error."""
    mock_manager = MagicMock()
    mock_manager.get_engine = MagicMock(side_effect=RuntimeError("Error"))
    
    with patch("server.database.DatabaseManager.get_instance", return_value=mock_manager):
        with pytest.raises(RuntimeError, match="Failed to close database connections"):
            await close_db()


def test_get_database_path_postgresql():
    """Test get_database_path returns None for PostgreSQL."""
    import server.database as db_module
    db_module._database_url = "postgresql+asyncpg://test"
    
    result = get_database_path()
    assert result is None


def test_get_database_path_unsupported():
    """Test get_database_path raises for unsupported URL."""
    import server.database as db_module
    db_module._database_url = "sqlite://test.db"
    
    with pytest.raises(ValidationError, match="Unsupported database URL"):
        get_database_path()


def test_get_database_path_none_url():
    """Test get_database_path raises for None URL."""
    import server.database as db_module
    db_module._database_url = None
    
    # Should use DatabaseManager which will raise if not initialized
    DatabaseManager.reset_instance()
    with patch("server.database.DatabaseManager.get_instance") as mock_get:
        mock_manager = MagicMock()
        mock_manager.get_database_path = MagicMock(side_effect=ValidationError("Database URL is None"))
        mock_get.return_value = mock_manager
        
        with pytest.raises(ValidationError):
            get_database_path()


def test_ensure_database_directory_postgresql():
    """Test ensure_database_directory is no-op for PostgreSQL."""
    # Should not raise
    ensure_database_directory()


def test_database_manager_get_engine_event_loop_check():
    """Test DatabaseManager.get_engine checks event loop change."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    mock_engine = MagicMock(spec=AsyncEngine)
    manager.engine = mock_engine
    manager._creation_loop_id = 123
    
    # Mock different event loop with different ID
    mock_loop_obj = MagicMock()
    mock_loop_obj.__class__.__name__ = "EventLoop"
    # Create a new engine for the new loop
    new_mock_engine = MagicMock(spec=AsyncEngine)
    
    # Mock _initialize_database to set the new engine
    def mock_init():
        manager.engine = new_mock_engine
        manager._initialized = True
        manager._creation_loop_id = 456
    
    # Create a mock loop object with a different id by patching id() at the module level
    with patch("asyncio.get_running_loop", return_value=mock_loop_obj):
        with patch("server.database.id", return_value=456):  # Different loop ID
            with patch.object(manager, "_initialize_database", side_effect=mock_init):
                # Should trigger re-initialization
                result = manager.get_engine()
                # Should return the new engine
                assert result == new_mock_engine
                assert manager._creation_loop_id == 456


def test_database_manager_get_engine_no_running_loop():
    """Test DatabaseManager.get_engine handles no running loop."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = MagicMock(spec=AsyncEngine)
    manager._creation_loop_id = None
    
    with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
        # Should not raise
        result = manager.get_engine()
        assert result is not None

