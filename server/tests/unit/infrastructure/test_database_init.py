"""
Unit tests for database initialization and error handling.

Tests the _initialize_database method and various initialization error paths.
"""

from unittest.mock import MagicMock, patch

import pytest

from server.database import DatabaseManager, ValidationError, reset_database
from server.exceptions import DatabaseError


@pytest.fixture(autouse=True)
def reset_db():
    """Reset database state before each test."""
    reset_database()
    yield
    reset_database()


def test_initialize_database_skip_if_already_initialized():
    """Test _initialize_database skips if already initialized."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = MagicMock()

    # Should return early without calling config
    with patch("server.config.get_config") as mock_config:
        manager._initialize_database()
        mock_config.assert_not_called()


def test_initialize_database_uses_module_level_url():
    """Test _initialize_database uses module-level _database_url if set."""
    import server.database as db_module

    DatabaseManager.reset_instance()
    db_module._database_url = "postgresql+asyncpg://test:test@localhost/test"

    manager = DatabaseManager.get_instance()

    with patch("server.database.create_async_engine") as mock_create:
        mock_engine = MagicMock()
        mock_create.return_value = mock_engine

        manager._initialize_database()

        assert manager.database_url == "postgresql+asyncpg://test:test@localhost/test"
        mock_create.assert_called_once()


def test_initialize_database_import_error():
    """Test _initialize_database handles ImportError from config."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config", side_effect=ImportError("Config import failed")):
        with pytest.raises(ValidationError, match="Failed to load configuration"):
            manager._initialize_database()


def test_initialize_database_config_validation_error():
    """Test _initialize_database handles PydanticValidationError."""
    from pydantic import ValidationError as PydanticValidationError

    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    # Create a simple PydanticValidationError by instantiating it directly
    # This simulates a validation error from Pydantic
    try:
        # Try to create an error by attempting invalid validation
        # This is a workaround since PydanticValidationError is complex to construct
        raise PydanticValidationError.from_exception_data(
            "AppConfig",
            [
                {
                    "type": "value_error",
                    "loc": ("database", "url"),
                    "msg": "Field required",
                    "input": {},
                    "ctx": {"error": "Field required"},
                }
            ],
        )
    except PydanticValidationError as e:
        pydantic_error = e

    with patch("server.config.get_config", side_effect=pydantic_error):
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
    """Test _initialize_database raises for non-PostgreSQL URL."""
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
            mock_engine = MagicMock()
            mock_create.return_value = mock_engine

            manager._initialize_database()

            assert manager.database_url == "postgresql+asyncpg://user:pass@localhost/db"


def test_initialize_database_keeps_asyncpg_url():
    """Test _initialize_database keeps postgresql+asyncpg:// URL as-is."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/db"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            mock_engine = MagicMock()
            mock_create.return_value = mock_engine

            manager._initialize_database()

            assert manager.database_url == "postgresql+asyncpg://user:pass@localhost/db"


def test_initialize_database_uses_nullpool_for_test():
    """Test _initialize_database uses NullPool for test URLs."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://test:test@localhost/mythos_test"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            from sqlalchemy.pool import NullPool

            mock_engine = MagicMock()
            mock_create.return_value = mock_engine

            manager._initialize_database()

            # Verify NullPool was used
            call_kwargs = mock_create.call_args[1]
            assert call_kwargs["poolclass"] == NullPool


def test_initialize_database_uses_pool_config_for_production():
    """Test _initialize_database uses pool config for production URLs."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://user:pass@localhost/prod"
        mock_config_obj.database.model_dump.return_value = {
            "pool_size": 10,
            "max_overflow": 20,
            "pool_timeout": 30,
        }
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            mock_engine = MagicMock()
            mock_create.return_value = mock_engine

            manager._initialize_database()

            # Verify pool config was used
            call_kwargs = mock_create.call_args[1]
            assert call_kwargs["pool_size"] == 10
            assert call_kwargs["max_overflow"] == 20
            assert call_kwargs["pool_timeout"] == 30
            assert "poolclass" not in call_kwargs  # Uses default AsyncAdaptedQueuePool


def test_initialize_database_value_error():
    """Test _initialize_database handles ValueError from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://test"
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
        mock_config_obj.database.url = "postgresql+asyncpg://test"
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
        mock_config_obj.database.url = "postgresql+asyncpg://test"
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
        mock_config_obj.database.url = "postgresql+asyncpg://test"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=OSError("Network error")):
            with pytest.raises(DatabaseError, match="Failed to connect to database"):
                manager._initialize_database()


def test_initialize_database_generic_exception():
    """Test _initialize_database handles generic Exception from create_async_engine."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://test"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine", side_effect=Exception("Unexpected error")):
            with pytest.raises(DatabaseError, match="Failed to create database engine"):
                manager._initialize_database()


def test_initialize_database_sets_creation_loop_id():
    """Test _initialize_database sets _creation_loop_id when loop is running."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://test"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            mock_engine = MagicMock()
            mock_create.return_value = mock_engine

            mock_loop = MagicMock()
            with patch("asyncio.get_running_loop", return_value=mock_loop):
                with patch("server.database.id", return_value=12345):
                    manager._initialize_database()

                    assert manager._creation_loop_id == 12345


def test_initialize_database_sets_creation_loop_id_none():
    """Test _initialize_database sets _creation_loop_id to None when no loop."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch("server.config.get_config") as mock_config:
        mock_config_obj = MagicMock()
        mock_config_obj.database.url = "postgresql+asyncpg://test"
        mock_config.return_value = mock_config_obj

        with patch("server.database.create_async_engine") as mock_create:
            mock_engine = MagicMock()
            mock_create.return_value = mock_engine

            with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
                manager._initialize_database()

                assert manager._creation_loop_id is None


def test_get_engine_reinitializes_if_none():
    """Test get_engine reinitializes if engine is None after initialization."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = None

    with patch.object(manager, "_initialize_database") as mock_init:

        def set_engine():
            manager.engine = MagicMock()
            manager._initialized = True

        mock_init.side_effect = set_engine

        result = manager.get_engine()

        assert result is not None
        assert mock_init.call_count == 1


def test_get_engine_handles_no_running_loop():
    """Test get_engine handles RuntimeError when no running loop."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()
    manager._initialized = True
    manager.engine = MagicMock()
    manager._creation_loop_id = None

    with patch("asyncio.get_running_loop", side_effect=RuntimeError("No running loop")):
        result = manager.get_engine()

        assert result is not None


def test_get_database_path_postgresql_returns_none():
    """Test get_database_path returns None for PostgreSQL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "_initialize_database"):
        manager.database_url = "postgresql+asyncpg://test"
        manager._initialized = True

        result = manager.get_database_path()

        assert result is None


def test_get_database_path_unsupported_raises():
    """Test get_database_path raises for unsupported URL."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "_initialize_database"):
        manager.database_url = "sqlite://test.db"
        manager._initialized = True

        with pytest.raises(ValidationError, match="Unsupported database URL"):
            manager.get_database_path()


def test_get_database_path_none_url_raises():
    """Test get_database_path raises when database_url is None."""
    DatabaseManager.reset_instance()
    manager = DatabaseManager.get_instance()

    with patch.object(manager, "_initialize_database"):
        manager.database_url = None
        manager._initialized = True

        with pytest.raises(ValidationError, match="Database URL is None"):
            manager.get_database_path()


def test_get_database_path_module_level_none():
    """Test get_database_path handles module-level empty URL."""
    import server.database as db_module

    DatabaseManager.reset_instance()
    # Set to empty string to trigger "Database URL is None" error
    db_module._database_url = ""

    with pytest.raises(ValidationError, match="Database URL is not configured"):
        from server.database import get_database_path

        get_database_path()


def test_get_database_path_module_level_postgresql():
    """Test get_database_path returns None for module-level PostgreSQL URL."""
    import server.database as db_module

    DatabaseManager.reset_instance()
    db_module._database_url = "postgresql+asyncpg://test"

    from server.database import get_database_path

    result = get_database_path()

    assert result is None


def test_get_database_path_module_level_unsupported():
    """Test get_database_path raises for module-level unsupported URL."""
    import server.database as db_module

    DatabaseManager.reset_instance()
    db_module._database_url = "sqlite://test.db"

    with pytest.raises(ValidationError, match="Unsupported database URL"):
        from server.database import get_database_path

        get_database_path()


def test_reset_database_resets_module_url():
    """Test reset_database resets module-level _database_url."""
    import server.database as db_module

    db_module._database_url = "test_url"
    reset_database()

    assert db_module._database_url is None


def test_reset_database_resets_singleton():
    """Test reset_database resets DatabaseManager singleton."""
    instance1 = DatabaseManager.get_instance()
    reset_database()
    instance2 = DatabaseManager.get_instance()

    assert instance1 is not instance2
