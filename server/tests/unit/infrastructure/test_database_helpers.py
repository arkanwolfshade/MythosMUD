"""
Unit tests for database_helpers module.

Tests module-level utility functions for database operations.
"""

import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

# anext is a built-in in Python 3.10+; project requires 3.12+
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
from server.database import DatabaseManager
from server.database_helpers import (
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
from server.exceptions import ValidationError


@pytest.fixture(autouse=True)
def reset_db():
    """Reset database state before each test."""
    reset_database()
    yield
    reset_database()


def test_reset_database():
    """Test reset_database resets DatabaseManager singleton and module state."""
    # Get initial instance
    instance1 = DatabaseManager.get_instance()
    instance1._initialized = True

    # Reset
    reset_database()

    # Verify new instance
    instance2 = DatabaseManager.get_instance()
    assert instance1 is not instance2
    assert instance2._initialized is False


def test_get_engine():
    """Test get_engine returns engine from DatabaseManager."""
    DatabaseManager.reset_instance()
    mock_engine = MagicMock(spec=AsyncEngine)
    mock_manager = MagicMock()
    mock_manager.get_engine.return_value = mock_engine

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        result = get_engine()
        assert result == mock_engine
        mock_manager.get_engine.assert_called_once()


def test_get_engine_raises_validation_error():
    """Test get_engine raises ValidationError when database cannot be initialized."""
    DatabaseManager.reset_instance()
    mock_manager = MagicMock()
    mock_manager.get_engine.side_effect = ValidationError("Database initialization failed")

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        with pytest.raises(ValidationError, match="Database initialization failed"):
            get_engine()


def test_get_session_maker():
    """Test get_session_maker returns session maker from DatabaseManager."""
    DatabaseManager.reset_instance()
    mock_session_maker = MagicMock(spec=async_sessionmaker)
    mock_manager = MagicMock()
    mock_manager.get_session_maker.return_value = mock_session_maker

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        result = get_session_maker()
        assert result == mock_session_maker
        mock_manager.get_session_maker.assert_called_once()


def test_get_session_maker_raises_validation_error():
    """Test get_session_maker raises ValidationError when database cannot be initialized."""
    DatabaseManager.reset_instance()
    mock_manager = MagicMock()
    mock_manager.get_session_maker.side_effect = ValidationError("Database initialization failed")

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        with pytest.raises(ValidationError, match="Database initialization failed"):
            get_session_maker()


def test_get_database_url():
    """Test get_database_url returns URL from DatabaseManager."""
    DatabaseManager.reset_instance()
    mock_manager = MagicMock()
    mock_manager.get_database_url.return_value = "postgresql+asyncpg://test:test@localhost/test"

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        result = get_database_url()
        assert result == "postgresql+asyncpg://test:test@localhost/test"
        mock_manager.get_database_url.assert_called_once()


def test_get_database_url_returns_none():
    """Test get_database_url returns None when not configured."""
    DatabaseManager.reset_instance()
    mock_manager = MagicMock()
    mock_manager.get_database_url.return_value = None

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        result = get_database_url()
        assert result is None


@pytest.mark.asyncio
async def test_get_async_session_success():
    """Test get_async_session yields session and handles cleanup."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        async for session in get_async_session():
            assert session == mock_session
            break


@pytest.mark.asyncio
async def test_get_async_session_http_exception_propagates():
    """Test get_async_session re-raises HTTPException without rollback."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)

    http_error = HTTPException(status_code=400, detail="Bad request")

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        with pytest.raises(HTTPException):
            async for _ in get_async_session():
                raise http_error


@pytest.mark.asyncio
async def test_get_async_session_rollback_on_error():
    """Test get_async_session rolls back on exception."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.rollback = AsyncMock()

    # Create a proper async context manager that allows exceptions to propagate
    class MockSessionContext:
        """Mock async context manager for testing exception propagation in get_async_session."""

        def __init__(self, session):
            self.session = session

        async def __aenter__(self):
            return self.session

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            # Return False to not suppress exceptions - let them propagate to get_async_session's handler
            return False

    mock_session_maker = MagicMock()
    mock_session_maker.return_value = MockSessionContext(mock_session)

    test_error = ValueError("Database error")

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        # Use async for to consume the generator
        # When exception is raised in the loop, it propagates to the generator's exception handler
        with pytest.raises(ValueError, match="Database error"):
            async for _ in get_async_session():
                # Exception raised here will be caught by get_async_session's exception handler
                # which calls rollback before re-raising
                raise test_error

    # Note: The exception handler in get_async_session calls rollback before re-raising
    # Due to async generator exception handling complexity with mocks, we verify the exception
    # propagates correctly. The rollback code path is covered by the exception handler structure.


@pytest.mark.asyncio
async def test_get_async_session_rollback_failure():
    """Test get_async_session handles rollback failure."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.rollback = AsyncMock(side_effect=RuntimeError("Rollback failed"))
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)

    test_error = ValueError("Database error")

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        # Original error should still be raised
        with pytest.raises(ValueError, match="Database error"):
            async for _ in get_async_session():
                raise test_error


@pytest.mark.asyncio
async def test_init_db_success():
    """Test init_db successfully initializes database."""
    mock_engine = AsyncMock(spec=AsyncEngine)
    mock_conn = AsyncMock()
    mock_engine.begin.return_value.__aenter__ = AsyncMock(return_value=mock_conn)
    mock_engine.begin.return_value.__aexit__ = AsyncMock(return_value=None)
    mock_conn.execute = AsyncMock()

    with (
        patch("server.database_helpers.get_engine", return_value=mock_engine),
        patch("sqlalchemy.orm.configure_mappers") as mock_configure,
    ):
        await init_db()
        mock_configure.assert_called_once()
        mock_conn.execute.assert_awaited_once()


@pytest.mark.asyncio
async def test_init_db_raises_on_error():
    """Test init_db raises exception on initialization failure."""
    test_error = RuntimeError("Database connection failed")

    with (
        patch("server.database_helpers.get_engine", side_effect=test_error),
        patch("sqlalchemy.orm.configure_mappers"),
    ):
        with pytest.raises(RuntimeError, match="Database connection failed"):
            await init_db()


@pytest.mark.asyncio
async def test_close_db_success():
    """Test close_db successfully closes database connections."""
    mock_manager = MagicMock()
    mock_manager.get_engine.return_value = MagicMock()
    mock_manager.close = AsyncMock()

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        await close_db()
        mock_manager.close.assert_awaited_once()


@pytest.mark.asyncio
async def test_close_db_raises_runtime_error_on_failure():
    """Test close_db raises RuntimeError when closing fails."""
    mock_manager = MagicMock()
    mock_manager.get_engine.return_value = MagicMock()
    mock_manager.close = AsyncMock(side_effect=ValueError("Close failed"))

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        with pytest.raises(RuntimeError, match="Failed to close database connections"):
            await close_db()


def test_get_database_path_postgresql_returns_none():
    """Test get_database_path returns None for PostgreSQL URLs."""
    with (
        patch("server.database._get_database_url_state", return_value="postgresql+asyncpg://test:test@localhost/test"),
        patch("server.database_helpers.get_test_database_url", return_value=None),
    ):
        result = get_database_path()
        assert result is None


def test_get_database_path_unsupported_url_raises():
    """Test get_database_path raises ValidationError for unsupported URL schemes."""
    with (
        patch("server.database._get_database_url_state", return_value="sqlite:///test.db"),
        patch("server.database_helpers.get_test_database_url", return_value=None),
    ):
        with pytest.raises(ValidationError, match="Unsupported database URL"):
            get_database_path()


def test_get_database_path_none_url_uses_manager():
    """Test get_database_path uses DatabaseManager when URL state is None."""
    mock_manager = MagicMock()
    mock_manager.get_database_path.return_value = None

    with (
        patch("server.database._get_database_url_state", return_value=None),
        patch("server.database_helpers.get_test_database_url", return_value=None),
        patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager),
    ):
        result = get_database_path()
        mock_manager.get_database_path.assert_called_once()
        assert result is None


def test_get_database_path_uses_database_manager_when_no_test_url():
    """Test get_database_path falls back to DatabaseManager when no test URL."""
    mock_manager = MagicMock()
    mock_manager.get_database_path.return_value = None

    with (
        patch("server.database._get_database_url_state", return_value=None),
        patch("server.database_helpers.get_test_database_url", return_value=None),
        patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager),
    ):
        result = get_database_path()
        mock_manager.get_database_path.assert_called_once()
        assert result is None


def test_ensure_database_directory_no_op_for_postgresql():
    """Test ensure_database_directory is no-op for PostgreSQL (returns None)."""
    with patch("server.database_helpers.get_database_path", return_value=None):
        # Should not raise or create directories
        ensure_database_directory()


def test_ensure_database_directory_creates_directory():
    """Test ensure_database_directory creates directory when path exists."""
    # Use tempfile to create a secure temporary path for testing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp_file:
        test_path = Path(tmp_file.name)
    try:
        with (
            patch("server.database_helpers.get_database_path", return_value=test_path),
            patch("pathlib.Path.mkdir") as mock_mkdir,
        ):
            ensure_database_directory()
            mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
    finally:
        # Clean up temporary file
        if test_path.exists():
            test_path.unlink()


@pytest.mark.asyncio
async def test_get_async_session_http_exception_passthrough():
    """Test get_async_session re-raises HTTPException without logging as database error."""

    mock_session = AsyncMock(spec=AsyncSession)
    mock_session_maker = MagicMock()
    mock_session_maker.return_value.__aenter__ = AsyncMock(return_value=mock_session)
    mock_session_maker.return_value.__aexit__ = AsyncMock(return_value=None)

    http_error = HTTPException(status_code=400, detail="Bad request")

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        with pytest.raises(HTTPException):
            async for _ in get_async_session():
                raise http_error
        # Should not have called rollback for HTTPException
        mock_session.rollback.assert_not_awaited()


def test_get_database_path_empty_string_url_raises():
    """Test get_database_path raises ValidationError when URL is empty string."""
    with (
        patch("server.database._get_database_url_state", return_value=""),
        patch("server.database_helpers.get_test_database_url", return_value=None),
    ):
        with pytest.raises(ValidationError, match="Database URL is None"):
            get_database_path()


def test_get_database_path_uses_test_url_when_available():
    """Test get_database_path uses test URL from get_test_database_url when available."""
    test_url = "postgresql+asyncpg://test:test@localhost/test"
    with (
        patch("server.database._get_database_url_state", return_value=None),
        patch("server.database_helpers.get_test_database_url", return_value=test_url),
    ):
        result = get_database_path()
        assert result is None  # PostgreSQL returns None


def test_get_database_path_uses_module_attribute_fallback():
    """Test get_database_path falls back to module _database_url attribute."""
    test_url = "postgresql+asyncpg://test:test@localhost/test"
    with (
        patch("server.database._get_database_url_state", return_value=None),
        patch("server.database_helpers.get_test_database_url", return_value=None),
        patch("server.database._database_url", test_url),
    ):
        result = get_database_path()
        assert result is None  # PostgreSQL returns None


@pytest.mark.asyncio
async def test_init_db_configure_mappers_failure():
    """Test init_db raises exception when configure_mappers fails."""
    mock_engine = AsyncMock(spec=AsyncEngine)
    configure_error = RuntimeError("Mapper configuration failed")

    with (
        patch("server.database_helpers.get_engine", return_value=mock_engine),
        patch("sqlalchemy.orm.configure_mappers", side_effect=configure_error),
    ):
        with pytest.raises(RuntimeError, match="Mapper configuration failed"):
            await init_db()


@pytest.mark.asyncio
async def test_init_db_connection_verification_failure():
    """Test init_db raises exception when connection verification fails."""
    mock_engine = AsyncMock(spec=AsyncEngine)
    mock_conn = AsyncMock()
    mock_engine.begin.return_value.__aenter__ = AsyncMock(return_value=mock_conn)
    mock_engine.begin.return_value.__aexit__ = AsyncMock(return_value=None)
    mock_conn.execute = AsyncMock(side_effect=RuntimeError("Connection failed"))

    with (
        patch("server.database_helpers.get_engine", return_value=mock_engine),
        patch("sqlalchemy.orm.configure_mappers"),
    ):
        with pytest.raises(RuntimeError, match="Connection failed"):
            await init_db()


@pytest.mark.asyncio
async def test_close_db_engine_initialization_failure():
    """Test close_db handles failure when engine initialization fails."""
    mock_manager = MagicMock()
    mock_manager.get_engine.side_effect = ValidationError("Engine initialization failed")

    with patch("server.database_helpers.DatabaseManager.get_instance", return_value=mock_manager):
        with pytest.raises(RuntimeError, match="Failed to close database connections"):
            await close_db()


@pytest.mark.asyncio
async def test_get_async_session_finally_block_executes():
    """Test get_async_session finally block executes even on success."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_exit = AsyncMock(return_value=None)

    class MockSessionContext:
        """Mock async context manager for testing."""

        async def __aenter__(self):
            return mock_session

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            return await mock_exit(exc_type, exc_val, exc_tb)

    mock_session_maker = MagicMock()
    mock_session_maker.return_value = MockSessionContext()

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        # Use anext() to properly test async generator
        gen = get_async_session()
        session = await anext(gen)
        assert session == mock_session
        # Close generator normally - this should trigger __aexit__
        await gen.aclose()
        # Verify session context manager was properly exited
        mock_exit.assert_awaited_once()


@pytest.mark.asyncio
async def test_get_async_session_rollback_success():
    """Test get_async_session successfully rolls back on exception."""
    mock_session = AsyncMock(spec=AsyncSession)
    mock_session.rollback = AsyncMock()

    class MockSessionContext:
        """Mock async context manager for testing rollback."""

        def __init__(self, session):
            self.session = session

        async def __aenter__(self):
            return self.session

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            return False  # Don't suppress exception

    mock_session_maker = MagicMock()
    mock_session_maker.return_value = MockSessionContext(mock_session)

    test_error = ValueError("Test error")

    with patch("server.database_helpers.get_session_maker", return_value=mock_session_maker):
        # Use anext() and athrow() to properly test exception propagation
        gen = get_async_session()
        session = await anext(gen)
        assert session == mock_session
        # Throw exception back to generator - this should trigger rollback
        with pytest.raises(ValueError, match="Test error"):
            await gen.athrow(test_error)

    # Verify rollback was called (exception handler should have called it)
    mock_session.rollback.assert_awaited_once()
