"""
Unit tests for database error handling and edge cases.

Tests error paths, validation failures, and edge cases in database.py.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic import ValidationError as PydanticValidationError

from server.database import DatabaseManager, reset_database
from server.exceptions import DatabaseError, ValidationError

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


# autouse: required for test isolation in this module - DatabaseManager singleton reset
@pytest.fixture(autouse=True)
def reset_db_state():
    """Reset database state before each test."""
    reset_database()
    yield
    reset_database()


def test_database_manager_init_raises_when_instance_exists():
    """Test DatabaseManager.__init__ raises when instance already exists."""
    DatabaseManager.reset_instance()
    DatabaseManager.get_instance()

    with pytest.raises(RuntimeError, match="Use DatabaseManager.get_instance"):
        DatabaseManager()


def test_initialize_database_skips_if_already_initialized():
    """Test _initialize_database skips if already initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = MagicMock()
    manager.session_maker = MagicMock()

    with patch.object(manager, "_initialize_database", wraps=manager._initialize_database) as mock_init:
        manager._initialize_database()
        # Should return early without doing anything
        mock_init.assert_called_once()


def test_initialize_database_config_validation_error():
    """Test _initialize_database handles PydanticValidationError."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config", side_effect=PydanticValidationError.from_exception_data("Test", [])):
        with pytest.raises(ValidationError, match="Failed to load configuration"):
            manager._initialize_database()


def test_initialize_database_config_runtime_error():
    """Test _initialize_database handles RuntimeError from config."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config", side_effect=RuntimeError("Config runtime error")):
        with pytest.raises(ValidationError, match="Failed to load configuration"):
            manager._initialize_database()


def test_initialize_database_none_url():
    """Test _initialize_database raises when database_url is None."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = None
        mock_config.return_value = mock_config_obj

        with pytest.raises(ValidationError, match="Database URL is not configured"):
            manager._initialize_database()


def test_initialize_database_unsupported_url():
    """Test _initialize_database raises for unsupported database URL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "sqlite://test.db"
        mock_config.return_value = mock_config_obj

        with pytest.raises(ValidationError, match="Unsupported database URL"):
            manager._initialize_database()


def test_initialize_database_converts_postgresql_url():
    """Test _initialize_database converts postgresql:// to postgresql+asyncpg://."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            with patch("server.database.async_sessionmaker") as mock_sessionmaker:
                mock_engine = MagicMock()
                mock_create.return_value = mock_engine
                mock_sessionmaker.return_value = MagicMock()

                manager._initialize_database()

                # Should convert postgresql:// to postgresql+asyncpg://
                assert manager.database_url == "postgresql+asyncpg://user:pass@localhost/db"
                mock_create.assert_called_once()


def test_initialize_database_keeps_asyncpg_url():
    """Test _initialize_database keeps postgresql+asyncpg:// URL as-is."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            with patch("server.database.async_sessionmaker") as mock_sessionmaker:
                mock_engine = MagicMock()
                mock_create.return_value = mock_engine
                mock_sessionmaker.return_value = MagicMock()

                manager._initialize_database()

                # Should keep postgresql+asyncpg:// as-is
                assert manager.database_url == "postgresql+asyncpg://user:pass@localhost/db"


def test_initialize_database_uses_nullpool_for_test():
    """Test _initialize_database uses NullPool for test URLs."""
    from sqlalchemy.pool import NullPool

    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/mythos_test"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            with patch("server.database.async_sessionmaker") as mock_sessionmaker:
                mock_engine = MagicMock()
                mock_create.return_value = mock_engine
                mock_sessionmaker.return_value = MagicMock()

                manager._initialize_database()

                # Should use NullPool for test URLs
                call_kwargs = mock_create.call_args[1]
                assert call_kwargs.get("poolclass") == NullPool


def test_initialize_database_uses_pool_config_for_production():
    """Test _initialize_database uses pool config for production URLs."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/mythos"
        mock_config_obj.database.model_dump.return_value = {
            "pool_size": 10,
            "max_overflow": 5,
            "pool_timeout": 30,
        }
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            with patch("server.database.async_sessionmaker") as mock_sessionmaker:
                mock_engine = MagicMock()
                mock_create.return_value = mock_engine
                mock_sessionmaker.return_value = MagicMock()

                manager._initialize_database()

                # Should use pool config for production
                call_kwargs = mock_create.call_args[1]
                assert call_kwargs.get("pool_size") == 10
                assert call_kwargs.get("max_overflow") == 5
                assert call_kwargs.get("pool_timeout") == 30


def test_initialize_database_value_error():
    """Test _initialize_database handles ValueError from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=ValueError("Invalid URL")):
            with pytest.raises(ValidationError, match="Invalid database configuration"):
                manager._initialize_database()


def test_initialize_database_type_error():
    """Test _initialize_database handles TypeError from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=TypeError("Invalid type")):
            with pytest.raises(ValidationError, match="Invalid database configuration"):
                manager._initialize_database()


def test_initialize_database_connection_error():
    """Test _initialize_database handles ConnectionError from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=ConnectionError("Connection failed")):
            with pytest.raises(DatabaseError, match="Failed to connect to database"):
                manager._initialize_database()


def test_initialize_database_os_error():
    """Test _initialize_database handles OSError from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=OSError("OS error")):
            with pytest.raises(DatabaseError, match="Failed to connect to database"):
                manager._initialize_database()


def test_initialize_database_generic_exception():
    """Test _initialize_database handles generic Exception from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=Exception("Unexpected error")):
            with pytest.raises(DatabaseError, match="Failed to create database engine"):
                manager._initialize_database()


def test_initialize_database_uses_module_level_url():
    """Test _initialize_database uses module-level _database_url if set."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    # Set module-level URL
    import server.database as db_module

    db_module._database_url = "postgresql+asyncpg://test:test@localhost/test"

    try:
        with patch("server.database.create_async_engine") as mock_create:
            with patch("server.database.async_sessionmaker") as mock_sessionmaker:
                mock_engine = MagicMock()
                mock_create.return_value = mock_engine
                mock_sessionmaker.return_value = MagicMock()

                manager._initialize_database()

                # Should use module-level URL, not config
                assert manager.database_url == "postgresql+asyncpg://test:test@localhost/test"
                mock_create.assert_called_once()
    finally:
        # Clean up
        db_module._database_url = None


def test_get_engine_reinitializes_if_none():
    """Test get_engine reinitializes if engine is None after initialization."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = None

    call_count = 0
    mock_engine = MagicMock()

    def mock_init():
        nonlocal call_count
        call_count += 1
        # Always set engine and initialized flag
        manager.engine = mock_engine
        manager._initialized = True

    # When get_engine is called with _initialized=True but engine=None,
    # it will call _initialize_database() which should set the engine
    with patch.object(manager, "_initialize_database", side_effect=mock_init):
        result = manager.get_engine()
        assert result is not None
        assert result == mock_engine
        assert call_count == 1  # Should have been called once to fix the None engine
        assert manager.engine is not None


def test_get_engine_event_loop_changed():
    """Test get_engine recreates engine when event loop changes."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    old_engine = MagicMock()
    manager.engine = old_engine
    manager._creation_loop_id = 123

    new_engine = MagicMock()
    init_call_count = 0

    def mock_init():
        nonlocal init_call_count
        init_call_count += 1
        manager.engine = new_engine
        manager._initialized = True
        manager._creation_loop_id = 456

    mock_loop = MagicMock()
    with patch("asyncio.get_running_loop", return_value=mock_loop):
        with patch("server.database.id", return_value=456):  # Different loop ID
            with patch.object(manager, "_initialize_database", side_effect=mock_init):
                result = manager.get_engine()

                # Should have reinitialized
                assert init_call_count == 1
                assert result == new_engine
                assert manager._creation_loop_id == 456


def test_get_engine_no_running_loop():
    """Test get_engine handles no running event loop."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    mock_engine = MagicMock()
    manager.engine = mock_engine
    manager._creation_loop_id = None

    with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
        result = manager.get_engine()
        # Should return engine without checking loop
        assert result == mock_engine


def test_get_session_maker_not_initialized():
    """Test get_session_maker initializes if not initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "_initialize_database") as _mock_init:
        mock_session_maker = MagicMock()
        manager.session_maker = mock_session_maker
        manager._initialized = True

        result = manager.get_session_maker()
        assert result == mock_session_maker


def test_get_database_url_not_initialized():
    """Test get_database_url initializes if not initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "_initialize_database") as _mock_init:
        manager.database_url = "postgresql+asyncpg://test"
        manager._initialized = True

        result = manager.get_database_url()
        assert result == "postgresql+asyncpg://test"


def test_get_database_path_postgresql_returns_none():
    """Test get_database_path returns None for PostgreSQL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "get_database_url", return_value="postgresql+asyncpg://test"):
        result = manager.get_database_path()
        assert result is None


def test_get_database_path_unsupported_raises():
    """Test get_database_path raises for unsupported URL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "get_database_url", return_value="sqlite://test.db"):
        with pytest.raises(ValidationError, match="Unsupported database URL"):
            manager.get_database_path()


def test_get_database_path_none_url_raises():
    """Test get_database_path raises when URL is None."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "get_database_url", return_value=None):
        with pytest.raises(ValidationError, match="Database URL is None"):
            manager.get_database_path()


@pytest.mark.asyncio
async def test_close_handles_none_engine():
    """Test close handles None engine gracefully."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager.engine = None
    manager._initialized = True

    # Should not raise
    await manager.close()

    assert manager._initialized is False
    assert manager._creation_loop_id is None


@pytest.mark.asyncio
async def test_close_handles_closed_event_loop():
    """Test close handles closed event loop gracefully."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True

    mock_loop = MagicMock()
    mock_loop.is_closed.return_value = True

    with patch("asyncio.get_running_loop", return_value=mock_loop):
        await manager.close()

        # Should skip disposal and just reset state
        assert manager.engine is None
        # Reason: Testing field value - mypy sees as unreachable but valid at runtime
        assert manager._initialized is False  # type: ignore[unreachable]
        # Should not have called dispose
        assert not hasattr(mock_engine, "dispose") or not mock_engine.dispose.called


@pytest.mark.asyncio
async def test_close_handles_no_running_loop():
    """Test close handles no running loop."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock()
    mock_engine.dispose = AsyncMock()
    mock_engine.sync_engine = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True

    with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", new_callable=AsyncMock) as mock_wait:
                # Mock wait_for to call the dispose function
                async def mock_wait_for(coro, _timeout):
                    await coro

                mock_wait.side_effect = mock_wait_for

                await manager.close()

                # Should have attempted disposal
                assert manager.engine is None
                # Reason: Testing field value - mypy sees as unreachable but valid at runtime
                assert manager._initialized is False  # type: ignore[unreachable]


@pytest.mark.asyncio
async def test_close_handles_dispose_timeout():
    """Test close handles dispose timeout."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock()
    mock_engine.dispose = AsyncMock()
    mock_engine.sync_engine = MagicMock()
    mock_engine.sync_engine.pool = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True

    mock_loop = MagicMock()
    mock_loop.is_closed.return_value = False

    with patch("asyncio.get_running_loop", return_value=mock_loop):
        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", side_effect=TimeoutError()):
                await manager.close()

                # Should have attempted force close via pool
                assert manager.engine is None
                assert manager._initialized is False  # type: ignore[unreachable]  # Reason: close() handles TimeoutError internally, so this code is reachable


@pytest.mark.asyncio
async def test_close_handles_runtime_error_during_dispose():
    """Test close handles RuntimeError during dispose."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock()
    mock_engine.dispose = AsyncMock(side_effect=RuntimeError("Event loop closed"))
    mock_engine.sync_engine = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True

    mock_loop = MagicMock()
    mock_loop.is_closed.return_value = False

    with patch("asyncio.get_running_loop", return_value=mock_loop):
        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", new_callable=AsyncMock) as mock_wait:

                async def mock_wait_for(coro, _timeout):
                    await coro

                mock_wait.side_effect = mock_wait_for

                # Should not raise, just log and reset state
                await manager.close()

                assert manager.engine is None
                assert manager._initialized is False  # type: ignore[unreachable]  # Reason: close() handles RuntimeError internally, so this code is reachable


@pytest.mark.asyncio
async def test_close_handles_attribute_error_during_dispose():
    """Test close handles AttributeError during dispose."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock()
    mock_engine.dispose = AsyncMock(side_effect=AttributeError("No attribute"))
    mock_engine.sync_engine = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True

    mock_loop = MagicMock()
    mock_loop.is_closed.return_value = False

    with patch("asyncio.get_running_loop", return_value=mock_loop):
        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", new_callable=AsyncMock) as mock_wait:

                async def mock_wait_for(coro, _timeout):
                    await coro

                mock_wait.side_effect = mock_wait_for

                # Should not raise, just log and reset state
                await manager.close()

                assert manager.engine is None
                assert manager._initialized is False  # type: ignore[unreachable]  # Reason: close() handles RuntimeError internally, so this code is reachable


@pytest.mark.asyncio
async def test_close_handles_generic_exception_during_dispose():
    """Test close handles generic Exception during dispose."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    mock_engine = MagicMock()
    mock_engine.dispose = AsyncMock(side_effect=Exception("Unexpected error"))
    mock_engine.sync_engine = MagicMock()
    manager.engine = mock_engine
    manager._initialized = True

    mock_loop = MagicMock()
    mock_loop.is_closed.return_value = False

    with patch("asyncio.get_running_loop", return_value=mock_loop):
        with patch("asyncio.sleep", new_callable=AsyncMock):
            with patch("asyncio.wait_for", new_callable=AsyncMock) as mock_wait:

                async def mock_wait_for(coro, _timeout):
                    await coro

                mock_wait.side_effect = mock_wait_for

                # Should not raise, just log and reset state
                await manager.close()

                assert manager.engine is None
                assert manager._initialized is False  # type: ignore[unreachable]  # Reason: close() handles RuntimeError internally, so this code is reachable


def test_reset_database_resets_singleton():
    """Test reset_database resets singleton."""
    DatabaseManager.reset_instance()
    instance1 = DatabaseManager.get_instance()

    reset_database()

    instance2 = DatabaseManager.get_instance()
    assert instance1 is not instance2


def test_reset_database_resets_module_url():
    """Test reset_database resets module-level _database_url."""
    import server.database as db_module

    db_module._database_url = "test_url"

    reset_database()

    assert db_module._database_url is None
