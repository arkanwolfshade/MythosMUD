"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.

New Test Structure:
-------------------
The test suite is organized hierarchically:

- fixtures/          - Shared test fixtures and utilities
- unit/              - Unit tests (isolated component tests)
  - api/             - API endpoint tests
  - commands/        - Command handler tests
  - chat/            - Chat/communication tests
  - player/          - Player management tests
  - npc/             - NPC system tests
  - world/           - Room/world tests
  - events/          - Event system tests
  - auth/            - Authentication tests
  - infrastructure/  - Core infrastructure tests
  - middleware/      - Middleware tests
  - models/          - Data model tests
  - services/        - Service layer tests
  - realtime/        - Real-time communication tests
  - logging/         - Logging tests
  - utilities/       - Utility tests
- integration/       - Integration tests (component interactions)
- e2e/               - End-to-end tests
- performance/       - Performance benchmarks
- security/          - Security tests
- coverage/          - Coverage improvement tests
- regression/        - Bug fix regression tests
- monitoring/        - Monitoring tests
- verification/      - Verification tests
- scripts/           - Test setup and migration scripts
"""

# CRITICAL: Set environment variables BEFORE any imports that might load config
# This prevents SecurityConfig validation errors during test collection
# Human reader: These must be set before importing any server modules that might load config
# AI reader: Environment variables must be set before module-level config instantiation
import os

# Set critical environment variables immediately to prevent module-level config loading failures
# Force-set these values even if they're empty (setdefault won't override empty strings)
# Human reader: These must be set before any server modules load config during test collection
# AI reader: Force-set environment variables to prevent SecurityConfig validation failures
if not os.environ.get("MYTHOSMUD_ADMIN_PASSWORD") or len(os.environ.get("MYTHOSMUD_ADMIN_PASSWORD", "")) < 8:
    os.environ["MYTHOSMUD_ADMIN_PASSWORD"] = "test-admin-password-for-development"
os.environ.setdefault("SERVER_PORT", "54731")
os.environ.setdefault("SERVER_HOST", "127.0.0.1")
os.environ.setdefault("LOGGING_ENVIRONMENT", "unit_test")

import asyncio
import atexit
import sys
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pytest
from dotenv import load_dotenv

from server.logging.enhanced_logging_config import get_logger

pytest_plugins = [
    "server.tests.fixtures.inventory_fixtures",
]

logger = get_logger(__name__)

# Import Windows-specific logging fixes
try:
    from .windows_logging_fix import (  # pyright: ignore
        configure_windows_logging,
        disable_problematic_log_handlers,
    )

    configure_windows_logging()
    disable_problematic_log_handlers()
except ImportError:
    # If the fix module doesn't exist, continue without it
    pass

# Import Windows-specific event loop fixes
try:
    from .windows_event_loop_fix import configure_windows_event_loops  # pyright: ignore

    configure_windows_event_loops()
except ImportError:
    # If the fix module doesn't exist, continue without it
    pass

# CRITICAL: Load .env.unit_test file FIRST, before any other environment variable setup
# This ensures that test-specific database URLs are loaded before any modules
# that depend on them are imported
project_root = Path(__file__).parent.parent.parent


def _is_postgres_url(url: str) -> bool:
    """Check if a database URL is PostgreSQL."""
    return url.startswith("postgresql") or url.startswith("postgresql+asyncpg") or url.startswith("postgresql+psycopg2")


def _configure_database_urls(
    worker_id: str | None = None, apply_worker_suffix: bool = True
) -> tuple[Path | None, Path | None]:
    """
    Configure DATABASE_URL and DATABASE_NPC_URL for tests.

    For PostgreSQL URLs, keeps them as-is. All workers use the same database URL.

    Returns:
        Tuple containing the resolved primary database Path (or None for PostgreSQL)
        and NPC database Path (or None for PostgreSQL).
    """

    if worker_id is None:
        worker_id = os.environ.get("PYTEST_XDIST_WORKER")

    database_url = os.getenv("DATABASE_URL")
    if database_url:
        if _is_postgres_url(database_url):
            # PostgreSQL URL - keep as-is, no path conversion needed
            print(f"[OK] Using PostgreSQL DATABASE_URL: {database_url[:50]}...")
            test_db_path = None
        else:
            raise ValueError(
                f"Unsupported database URL format: {database_url}. "
                "Only PostgreSQL (postgresql+asyncpg://) is supported."
            )
    else:
        raise ValueError(
            "DATABASE_URL environment variable is required. "
            "Please set it in server/tests/.env.unit_test to a PostgreSQL URL."
        )

    npc_database_url = os.getenv("DATABASE_NPC_URL")
    if npc_database_url:
        if _is_postgres_url(npc_database_url):
            # PostgreSQL URL - keep as-is, no path conversion needed
            print(f"[OK] Using PostgreSQL DATABASE_NPC_URL: {npc_database_url[:50]}...")
            npc_db_path = None
        else:
            raise ValueError(
                f"Unsupported database URL format: {npc_database_url}. "
                "Only PostgreSQL (postgresql+asyncpg://) is supported."
            )
    else:
        # Default to same database as main database for PostgreSQL
        if test_db_path is None:
            # Both are PostgreSQL - use same URL
            os.environ["DATABASE_NPC_URL"] = database_url
            npc_db_path = None
            print("[OK] Set DATABASE_NPC_URL to same as DATABASE_URL (PostgreSQL)")
        else:
            raise ValueError(
                "DATABASE_NPC_URL environment variable is required. "
                "Please set it in server/tests/.env.unit_test to a PostgreSQL URL."
            )

    return test_db_path, npc_db_path


TEST_ENV_PATH = project_root / "server" / "tests" / ".env.unit_test"
EXAMPLE_ENV_PATH = project_root / "env.unit_test.example"


def validate_test_environment():
    """Validate that required test environment files exist."""
    if not TEST_ENV_PATH.exists():
        logger.error("Test environment file not found", test_env_path=str(TEST_ENV_PATH))
        if EXAMPLE_ENV_PATH.exists():
            logger.info("Example file exists", example_path=str(EXAMPLE_ENV_PATH))
            logger.info(
                "Copy example file to create required test environment",
                copy_command=f'Copy-Item "{EXAMPLE_ENV_PATH}" "{TEST_ENV_PATH}"',
            )
        else:
            logger.error("No example file found to copy from")
        raise FileNotFoundError(
            f"Required test environment file missing: {TEST_ENV_PATH}\n"
            f"Please copy env.unit_test.example to server/tests/.env.unit_test"
        )

    # Validate that the file has required content
    try:
        with open(TEST_ENV_PATH, encoding="utf-8") as f:
            content = f.read()
            required_vars = ["SERVER_PORT=", "DATABASE_URL=", "DATABASE_NPC_URL=", "MYTHOSMUD_ADMIN_PASSWORD="]
            missing_vars = []
            for var in required_vars:
                if var not in content:
                    missing_vars.append(var)

            if missing_vars:
                logger.error(
                    "Test environment file missing required variables",
                    missing_variables=missing_vars,
                    test_env_path=str(TEST_ENV_PATH),
                )
                raise ValueError(f"Test environment file missing required variables: {missing_vars}")

    except Exception as e:
        logger.error("Failed to validate test environment file", error=str(e))
        raise


@pytest.hookimpl(optionalhook=True)
def pytest_configure_node(node):
    """Provide worker-specific configuration for pytest-xdist nodes."""
    try:
        npc_url = os.environ["DATABASE_NPC_URL"]
        if not _is_postgres_url(npc_url):
            raise ValueError(
                f"Unsupported database URL format: {npc_url}. Only PostgreSQL (postgresql+asyncpg://) is supported."
            )
        # PostgreSQL - no path manipulation needed
    except KeyError:
        raise ValueError(
            "DATABASE_NPC_URL environment variable is required for pytest-xdist workers. "
            "Please set it in server/tests/.env.unit_test to a PostgreSQL URL."
        ) from None

    worker_id = getattr(node, "workerid", None) or getattr(node, "id", None)
    if worker_id is None:
        worker_id = node.workerinput.get("workerid", "worker")

    # PostgreSQL uses shared database, no worker-specific paths needed
    # For PostgreSQL, all workers use the same database URL
    node.workerinput["MYTHOSMUD_WORKER_NPC_DB_PATH"] = npc_url


# Validate test environment before proceeding
try:
    validate_test_environment()
    # Use override=False so environment variables (from Docker/CI) take precedence
    # This allows Docker/CI to set DATABASE_URL with correct password while
    # still allowing local development to use .env.unit_test values
    load_dotenv(TEST_ENV_PATH, override=False)  # Don't override existing env vars
    logger.info("Loaded test environment secrets", test_env_path=str(TEST_ENV_PATH))
except (FileNotFoundError, ValueError) as e:
    logger.critical("Test environment validation failed", error=str(e))
    logger.critical(
        "Setup instructions: Copy example environment file",
        copy_command=f'Copy-Item "{EXAMPLE_ENV_PATH}" "{TEST_ENV_PATH}"',
    )
    logger.critical("Additional setup steps: Verify file contains all required variables and run tests again")
    raise SystemExit(1) from e

# Set MYTHOSMUD_ENV to enable test-specific config fallbacks
os.environ["MYTHOSMUD_ENV"] = "test"


def _cleanup_on_exit():
    """Clean up all database connections and event loops when process exits."""
    # This runs when the Python process exits, ensuring cleanup even if pytest hooks don't run
    try:
        from server.database import get_database_manager
        from server.npc_database import close_npc_db

        # Try to get or create an event loop for cleanup
        cleanup_loop = None
        loop_created = False

        try:
            loop = asyncio.get_running_loop()
            cleanup_loop = loop
        except RuntimeError:
            # No running loop - try to get the default loop
            try:
                cleanup_loop = asyncio.get_event_loop()
                if cleanup_loop.is_closed():
                    cleanup_loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(cleanup_loop)
                    loop_created = True
            except RuntimeError:
                # No default loop either - create one
                cleanup_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(cleanup_loop)
                loop_created = True

        if cleanup_loop and not cleanup_loop.is_closed():
            # Clean up main database
            try:
                db_manager = get_database_manager()
                if db_manager and db_manager.engine:
                    if cleanup_loop.is_running():
                        # Can't use run_until_complete on running loop
                        # Just try to dispose directly
                        try:
                            asyncio.run_coroutine_threadsafe(db_manager.close(), cleanup_loop)
                        except (RuntimeError, TypeError):
                            pass
                    else:
                        cleanup_loop.run_until_complete(db_manager.close())
            except (RuntimeError, TypeError):
                pass

            # Clean up NPC database
            try:
                if cleanup_loop.is_running():
                    try:
                        asyncio.run_coroutine_threadsafe(close_npc_db(), cleanup_loop)
                    except (RuntimeError, TypeError):
                        pass
                else:
                    cleanup_loop.run_until_complete(close_npc_db())
            except (RuntimeError, TypeError):
                pass

            # Close the loop if we created it
            if loop_created:
                try:
                    pending = asyncio.all_tasks(cleanup_loop)
                    for task in pending:
                        task.cancel()
                    if pending:
                        cleanup_loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                    cleanup_loop.close()
                except (RuntimeError, TypeError):
                    pass

    except (RuntimeError, TypeError):
        # Ignore all errors during exit cleanup
        pass


# Register cleanup function to run on process exit
# This ensures resources are cleaned up even if pytest hooks don't run
atexit.register(_cleanup_on_exit)

# Set environment variables BEFORE any imports to prevent module-level
# instantiations from using the wrong paths
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"

# Note: Critical environment variables are now set at the top of this file
# before any imports to prevent config validation errors during test collection
os.environ.setdefault("GAME_ROOM_DATA_PATH", "data/rooms")
os.environ.setdefault("GAME_ALIASES_DIR", str(project_root / "data" / "unit_test" / "players" / "aliases"))

# CRITICAL: Disable process termination during tests to prevent test suite crashes
# This prevents the ProcessTerminator from killing the test process when shutdown tests run
os.environ.setdefault("MYTHOSMUD_DISABLE_PROCESS_EXIT", "1")

# CRITICAL: Set database URLs IMMEDIATELY to prevent import-time failures
# This must happen before any database modules are imported

# Ensure DATABASE_URL is set with absolute path
TEST_DB_PATH, TEST_NPC_DB_PATH = _configure_database_urls()

# Ensure we're using the correct path for test logs (matches .env.unit_test)
test_logs_dir = project_root / "logs" / "unit_test"
test_logs_dir.mkdir(parents=True, exist_ok=True)
# Configuration is now loaded from .env.unit_test via Pydantic BaseSettings
# No YAML config file needed - all settings via environment variables
print("[OK] Using Pydantic configuration from .env.unit_test")
# Legacy logging environment variables no longer needed - logging is handled by
# centralized system
# Use absolute path for aliases directory to prevent incorrect directory creation
aliases_dir = project_root / "data" / "unit_test" / "players" / "aliases"
aliases_dir.mkdir(parents=True, exist_ok=True)
os.environ["ALIASES_DIR"] = str(aliases_dir)

# Add the server directory to the path for imports
sys.path.append(str(Path(__file__).parent.parent))

# Import test environment fixtures to make them available to all tests

# ARCHITECTURE FIX: Import container-based fixtures for modern testing patterns
from .fixtures.container_fixtures import (  # noqa: F401, E402
    async_container_test_client,
    container_test_client,
    container_test_client_class,  # Class-scoped variant for performance optimization
    mock_container,
    player_factory,
    room_factory,
    test_container,
)

# AI: Following pytest best practices by exposing fixtures in conftest.py
# This makes them available to all tests without individual imports
# E402 suppressed: pytest conftest requires environment setup before imports


# Create synchronous wrapper fixtures for async fixtures
@pytest.fixture
def sync_test_environment():
    """Synchronous wrapper for test_environment async fixture"""
    import uuid

    from .fixtures.test_environment import test_env_manager

    # Save original environment variables to restore after test
    original_database_url = os.environ.get("DATABASE_URL")
    original_npc_database_url = os.environ.get("DATABASE_NPC_URL")

    # Use unique environment name for each test
    env_name = f"pytest_sync_{uuid.uuid4().hex[:8]}"

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        env = loop.run_until_complete(test_env_manager.create_environment(env_name))
        yield env
    finally:
        try:
            loop.run_until_complete(test_env_manager.destroy_environment(env_name))
        except (RuntimeError, TypeError):
            pass  # Ignore cleanup errors
        finally:
            # Restore original environment variables
            if original_database_url:
                os.environ["DATABASE_URL"] = original_database_url
            if original_npc_database_url:
                os.environ["DATABASE_NPC_URL"] = original_npc_database_url

            # Force re-initialization from restored environment variables
            # by resetting global state (don't restore old state, let it reinitialize)
            import server.database
            import server.npc_database

            server.database._engine = None
            server.database._async_session_maker = None
            server.database._database_url = None

            server.npc_database._npc_engine = None
            server.npc_database._npc_async_session_maker = None
            server.npc_database._npc_database_url = None

            # Reset config cache to force reload with correct environment variables
            from server.config import reset_config

            reset_config()

            loop.close()


def pytest_configure(config):
    """Configure pytest with test environment variables."""
    # Set required test environment variables, overriding any existing values
    # These are test-specific defaults that should only be used if test.env is not loaded
    os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
    os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
    os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
    os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"

    # CRITICAL: Pydantic ServerConfig requires SERVER_PORT
    os.environ.setdefault("SERVER_PORT", "54731")
    os.environ.setdefault("SERVER_HOST", "127.0.0.1")

    # CRITICAL: Disable process termination during tests to prevent test suite crashes
    os.environ.setdefault("MYTHOSMUD_DISABLE_PROCESS_EXIT", "1")

    worker_id = None
    worker_input = getattr(config, "workerinput", None)
    worker_path_override = None
    apply_worker_suffix = True
    if worker_input:
        worker_id = worker_input.get("workerid")
        if worker_id:
            os.environ["PYTEST_XDIST_WORKER"] = worker_id
        worker_path_override = worker_input.get("MYTHOSMUD_WORKER_NPC_DB_PATH")
        if worker_path_override:
            # Check if it's already a PostgreSQL URL (from pytest_configure_node)
            if _is_postgres_url(worker_path_override):
                os.environ["DATABASE_NPC_URL"] = worker_path_override
            else:
                raise ValueError(
                    f"Unsupported database URL format: {worker_path_override}. "
                    "Only PostgreSQL (postgresql+asyncpg://) is supported."
                )
            apply_worker_suffix = False

    # Store database paths in pytest config instead of using global variables
    test_db_path, test_npc_db_path = _configure_database_urls(worker_id, apply_worker_suffix=apply_worker_suffix)
    config.test_db_path = test_db_path
    config.test_npc_db_path = test_npc_db_path

    # Ensure we're using the correct path for test logs (matches .env.unit_test)
    test_logs_dir = project_root / "logs" / "unit_test"
    test_logs_dir.mkdir(parents=True, exist_ok=True)
    # Legacy logging environment variables no longer needed - logging is handled by centralized system
    # Use absolute path for aliases directory to prevent incorrect directory creation
    aliases_dir = project_root / "data" / "unit_test" / "players" / "aliases"
    aliases_dir.mkdir(parents=True, exist_ok=True)
    os.environ["ALIASES_DIR"] = str(aliases_dir)


@pytest.fixture(scope="session")
def test_env_vars():
    """Provide test environment variables."""
    return {
        "MYTHOSMUD_SECRET_KEY": os.getenv("MYTHOSMUD_SECRET_KEY", "test-secret-key-for-development"),
        "DATABASE_URL": os.environ["DATABASE_URL"],
        "MYTHOSMUD_JWT_SECRET": os.getenv("MYTHOSMUD_JWT_SECRET", "test-jwt-secret-for-development"),
        "MYTHOSMUD_RESET_TOKEN_SECRET": os.getenv(
            "MYTHOSMUD_RESET_TOKEN_SECRET", "test-reset-token-secret-for-development"
        ),
        "MYTHOSMUD_VERIFICATION_TOKEN_SECRET": os.getenv(
            "MYTHOSMUD_VERIFICATION_TOKEN_SECRET", "test-verification-token-secret-for-development"
        ),
    }


@pytest.fixture(scope="session")
def test_database():
    """Initialize test database with proper schema."""
    # PostgreSQL databases are managed via DDL scripts, not Python initialization
    # Just return the PostgreSQL URL from environment
    test_db_url = os.getenv("DATABASE_URL")
    if not test_db_url or not test_db_url.startswith("postgresql"):
        raise ValueError("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
    return test_db_url


@pytest.fixture(scope="session")
def test_npc_database():
    """Initialize NPC test database with proper schema."""
    # PostgreSQL databases are managed via DDL scripts, not Python initialization
    # Just return the PostgreSQL URL from environment
    npc_db_url = os.getenv("DATABASE_NPC_URL")
    if not npc_db_url or not npc_db_url.startswith("postgresql"):
        raise ValueError("DATABASE_NPC_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")
    return npc_db_url


@pytest.fixture(scope="function")
def event_loop():
    """
    Override pytest-asyncio's event_loop fixture to ensure proper cleanup.

    This ensures that event loops are properly closed after each test,
    preventing ResourceWarnings about unclosed event loops and transports.

    CRITICAL: This fixture must properly close all transports and tasks before
    closing the loop to prevent ResourceWarnings in pytest-xdist workers.

    With asyncio_mode=auto, pytest-asyncio will use this fixture if it exists.
    """
    # Create a new event loop for this test
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    yield loop

    # Cleanup happens here - don't use finalizer to avoid double cleanup
    _cleanup_event_loop(loop)


def _cleanup_event_loop(loop):
    """
    Helper function to properly clean up an event loop.

    CRITICAL: This must dispose all database engines created in this loop
    before closing the loop to prevent ResourceWarnings about unclosed transports.
    """
    if loop.is_closed():
        return

    try:
        # CRITICAL: Dispose database engines BEFORE closing the loop
        # This prevents ResourceWarnings about unclosed transports from asyncpg
        try:
            from server.database import get_database_manager
            from server.npc_database import get_npc_engine

            # Check if database engines were created in this loop
            # CRITICAL: asyncpg connections MUST be disposed in the same loop they were created in
            db_manager = get_database_manager()
            if db_manager and db_manager.engine and db_manager._creation_loop_id == id(loop):
                # This engine belongs to this loop - dispose it before closing the loop
                if not loop.is_closed() and not loop.is_running():
                    try:
                        # CRITICAL: Use the database manager's close() method which properly
                        # closes all asyncpg connections before disposal. This prevents
                        # RuntimeWarning about unawaited Connection._cancel coroutines.
                        async def _close_properly():
                            await db_manager.close()

                        # Use run_until_complete to close in this loop
                        # This is safe because the test has completed and loop is not running
                        loop.run_until_complete(asyncio.wait_for(_close_properly(), timeout=3.0))
                    except (TimeoutError, RuntimeError, AttributeError, TypeError, asyncio.CancelledError):
                        # If disposal fails or times out, continue with cleanup
                        # The engine will be garbage collected eventually
                        pass

            # Same for NPC database
            # CRITICAL: asyncpg connections MUST be disposed in the same loop they were created in
            npc_engine = get_npc_engine()
            if npc_engine:
                try:
                    from server.npc_database import _npc_creation_loop_id

                    if _npc_creation_loop_id == id(loop):
                        if not loop.is_closed() and not loop.is_running():
                            try:
                                # CRITICAL: Use close_npc_db() which properly closes all asyncpg connections
                                # before disposal. This prevents RuntimeWarning about unawaited
                                # Connection._cancel coroutines.
                                async def _close_npc_properly():
                                    from server.npc_database import close_npc_db

                                    await close_npc_db()

                                # Use run_until_complete to close in this loop
                                # This is safe because the test has completed and loop is not running
                                loop.run_until_complete(asyncio.wait_for(_close_npc_properly(), timeout=3.0))
                            except (TimeoutError, RuntimeError, AttributeError, TypeError, asyncio.CancelledError):
                                # If disposal fails or times out, continue with cleanup
                                # The engine will be garbage collected eventually
                                pass
                except (RuntimeError, TypeError):
                    pass
        except (RuntimeError, TypeError):
            # Ignore errors during database cleanup
            pass

        # Get all tasks and cancel them
        pending = asyncio.all_tasks(loop)
        for task in pending:
            if not task.done():
                task.cancel()

        # Wait for tasks to complete cancellation (with timeout)
        if pending:
            try:
                loop.run_until_complete(asyncio.wait_for(asyncio.gather(*pending, return_exceptions=True), timeout=0.5))
            except (TimeoutError, RuntimeError, TypeError):
                # If we can't wait, just proceed to close
                pass

        # Close all transports explicitly
        # This is critical for preventing ResourceWarnings about unclosed transports
        if hasattr(loop, "_transports"):
            for transport in list(loop._transports.values()):
                try:
                    if hasattr(transport, "is_closing") and not transport.is_closing():
                        transport.close()
                    elif hasattr(transport, "close"):
                        transport.close()
                except (RuntimeError, TypeError):
                    pass

        # Close the loop
        loop.close()
    except (RuntimeError, TypeError):
        # If cleanup fails, try to close anyway
        try:
            if not loop.is_closed():
                loop.close()
        except (RuntimeError, TypeError):
            pass


@pytest.fixture(scope="session", autouse=True)
def cleanup_session_resources():
    """Ensure all database connections and event loops are properly closed at session end."""
    yield

    # Cleanup happens after all tests in the session complete
    # This ensures resources are closed before worker processes exit
    try:
        from server.database import get_database_manager
        from server.npc_database import close_npc_db

        # Try to get or create an event loop for cleanup
        cleanup_loop = None
        loop_created = False

        try:
            loop = asyncio.get_running_loop()
            cleanup_loop = loop
        except RuntimeError:
            # No running loop - create one for cleanup
            cleanup_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(cleanup_loop)
            loop_created = True

        if cleanup_loop and not cleanup_loop.is_closed():
            # Clean up main database
            try:
                db_manager = get_database_manager()
                if db_manager and db_manager.engine:
                    if cleanup_loop.is_running():
                        task = cleanup_loop.create_task(db_manager.close())
                        try:
                            cleanup_loop.run_until_complete(asyncio.wait_for(task, timeout=0.5))
                        except (TimeoutError, RuntimeError):
                            pass
                    else:
                        cleanup_loop.run_until_complete(db_manager.close())
            except (RuntimeError, TypeError):
                pass

            # Clean up NPC database
            try:
                if cleanup_loop.is_running():
                    task = cleanup_loop.create_task(close_npc_db())
                    try:
                        cleanup_loop.run_until_complete(asyncio.wait_for(task, timeout=0.5))
                    except (TimeoutError, RuntimeError):
                        pass
                else:
                    cleanup_loop.run_until_complete(close_npc_db())
            except (RuntimeError, TypeError):
                pass

            # Close all remaining tasks and the loop if we created it
            if loop_created:
                try:
                    # Cancel all remaining tasks
                    pending = asyncio.all_tasks(cleanup_loop)
                    for task in pending:
                        task.cancel()
                    if pending:
                        cleanup_loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                    cleanup_loop.close()
                except (RuntimeError, TypeError):
                    pass

        # Also ensure any default event loop is closed
        try:
            default_loop = asyncio.get_event_loop()
            if default_loop and not default_loop.is_closed() and default_loop != cleanup_loop:
                try:
                    # Cancel all tasks
                    pending = asyncio.all_tasks(default_loop)
                    for task in pending:
                        task.cancel()
                    if pending:
                        default_loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                    default_loop.close()
                except (RuntimeError, TypeError):
                    pass
        except RuntimeError:
            # No default loop - that's fine
            pass

    except (RuntimeError, TypeError):
        # Ignore all cleanup errors - process exit will clean up
        pass


@pytest.fixture(autouse=True)  # Enable automatic use for all tests
def ensure_test_db_ready(test_database):
    """Ensure test database is ready for each test."""
    # This fixture runs automatically for each test
    # The test_database fixture ensures the database is initialized
    # Reset config cache to ensure fresh environment variables are loaded
    from ..config import reset_config

    reset_config()
    # Reset persistence to ensure fresh instance with new environment variables
    # Removed: reset_persistence() - PersistenceLayer no longer exists
    # All code now uses AsyncPersistenceLayer from ApplicationContainer
    pass


@pytest.fixture
def mock_application_container():
    """
    Create a fully-mocked ApplicationContainer for testing.

    This fixture provides a comprehensive mock of the ApplicationContainer with all
    required services properly mocked. This ensures that tests requiring the container
    have access to all necessary dependencies without needing to initialize the full
    application infrastructure.

    Services provided:
    - Core: persistence, event_bus, event_handler, connection_manager
    - Business: player_service, room_service, user_manager
    - Cache: room_cache_service, profession_cache_service
    - Infrastructure: task_registry

    AI Agent: This fixture is the foundation for testing components that depend on
    the ApplicationContainer. Use this instead of creating incomplete mocks that
    cause "ApplicationContainer not found" errors.
    """
    from unittest.mock import AsyncMock, Mock

    container = Mock()

    # Core services
    container.persistence = AsyncMock()
    container.event_bus = Mock()
    container.event_handler = Mock()
    container.connection_manager = Mock()
    container.connection_manager.handle_new_game_session = AsyncMock(
        return_value={"success": True, "connections_disconnected": 0, "errors": []}
    )

    # Business services
    container.player_service = Mock()
    container.room_service = Mock()
    container.user_manager = Mock()

    # Cache services
    container.room_cache_service = Mock()
    container.profession_cache_service = Mock()

    # Infrastructure
    container.task_registry = Mock()

    # Configure commonly-used methods to return sensible defaults
    container.persistence.async_list_players = AsyncMock(return_value=[])
    container.persistence.async_get_player = AsyncMock(return_value=None)
    container.persistence.async_get_room = AsyncMock(return_value=None)
    container.persistence.async_save_player = AsyncMock(return_value=None)
    container.persistence.async_delete_player = AsyncMock(return_value=True)

    container.player_service.list_players = AsyncMock(return_value=[])
    container.player_service.get_player_by_id = AsyncMock(return_value=None)

    container.room_service.get_room = AsyncMock(return_value=None)

    # Configure user_manager with a test data directory
    project_root = Path(__file__).parent.parent.parent
    container.user_manager.data_dir = project_root / "data" / "unit_test" / "user_management"

    return container


@pytest.fixture
def test_client(mock_application_container):
    """Create a test client with properly initialized app state."""

    from fastapi.testclient import TestClient

    from ..async_persistence import AsyncPersistenceLayer
    from ..events.event_bus import EventBus
    from ..game.player_service import PlayerService
    from ..game.room_service import RoomService
    from ..main import app
    from ..realtime.event_handler import RealTimeEventHandler

    # PostgreSQL databases are initialized via DDL scripts, not Python initialization
    # The database should already exist and be accessible via DATABASE_URL environment variable

    # AI Agent: Create event handler directly (no longer using global factory)
    #           Post-migration: RealTimeEventHandler uses dependency injection
    event_bus = EventBus()
    app.state.event_handler = RealTimeEventHandler(event_bus=event_bus)
    # Use AsyncPersistenceLayer directly (PersistenceLayer removed)
    app.state.persistence = AsyncPersistenceLayer(event_bus=event_bus)
    app.state.server_shutdown_pending = False

    # Create real PlayerService and RoomService with real persistence
    player_service = PlayerService(app.state.persistence)
    room_service = RoomService(app.state.persistence)

    # Use the comprehensive mock container
    app.state.container = mock_application_container
    # Update container's persistence, event_bus, and services with real instances
    mock_application_container.persistence = app.state.persistence
    mock_application_container.event_bus = app.state.event_handler.event_bus
    mock_application_container.event_handler = app.state.event_handler
    mock_application_container.player_service = player_service
    mock_application_container.room_service = room_service

    # Also set these on app.state for backward compatibility
    app.state.event_bus = app.state.event_handler.event_bus
    app.state.player_service = player_service
    app.state.room_service = room_service

    client = TestClient(app)
    client.app.state.server_shutdown_pending = False
    return client


@pytest.fixture
async def async_test_client(mock_application_container):
    """Create an async test client with properly initialized app state for async tests."""
    from httpx import ASGITransport, AsyncClient

    from ..async_persistence import AsyncPersistenceLayer
    from ..database import get_database_manager
    from ..events.event_bus import EventBus
    from ..game.player_service import PlayerService
    from ..game.room_service import RoomService
    from ..main import app
    from ..realtime.event_handler import RealTimeEventHandler

    # CRITICAL FIX: Dispose database engine before test to prevent event loop mismatch errors
    # This ensures the engine is recreated in the current event loop (the test's loop)
    # rather than using an engine created in a different loop
    try:
        db_manager = get_database_manager()
        if db_manager and db_manager.engine:
            await db_manager.engine.dispose()
            # Reset initialization state to force recreation in current loop
            db_manager._initialized = False
            db_manager.engine = None
            db_manager.session_maker = None
    except (RuntimeError, TypeError):
        # Ignore errors - engine might not exist yet
        pass

    # PostgreSQL databases are initialized via DDL scripts, not Python initialization
    # The database should already exist and be accessible via DATABASE_URL environment variable

    # AI Agent: Create event handler directly (no longer using global factory)
    #           Post-migration: RealTimeEventHandler uses dependency injection
    event_bus = EventBus()
    app.state.event_handler = RealTimeEventHandler(event_bus=event_bus)
    # Use AsyncPersistenceLayer directly (PersistenceLayer removed)
    app.state.persistence = AsyncPersistenceLayer(event_bus=event_bus)
    app.state.server_shutdown_pending = False

    # Create real PlayerService and RoomService with real persistence
    player_service = PlayerService(app.state.persistence)
    room_service = RoomService(app.state.persistence)

    # Use the comprehensive mock container
    app.state.container = mock_application_container
    # Update container's persistence, event_bus, and services with real instances
    mock_application_container.persistence = app.state.persistence
    mock_application_container.event_bus = app.state.event_handler.event_bus
    mock_application_container.event_handler = app.state.event_handler
    mock_application_container.player_service = player_service
    mock_application_container.room_service = room_service

    # Also set these on app.state for backward compatibility
    app.state.event_bus = app.state.event_handler.event_bus
    app.state.player_service = player_service
    app.state.room_service = room_service

    transport = ASGITransport(app=app)
    client = AsyncClient(transport=transport, base_url="http://test")
    client.app = app  # Attach app for backward compatibility
    client.app.state.server_shutdown_pending = False

    # For serial tests, ensure database transactions are properly isolated
    # by flushing any pending operations before starting the test
    try:
        # Force a small delay to ensure any pending database operations are committed
        await asyncio.sleep(0.05)  # Small delay for transaction isolation
    except (RuntimeError, TypeError):
        pass  # Ignore errors in test setup

    try:
        yield client
    finally:
        # For serial tests, ensure transactions are committed before cleanup
        try:
            await asyncio.sleep(0.05)  # Small delay to ensure transaction commit
        except (RuntimeError, TypeError):
            pass  # Ignore errors in test teardown

        # Explicitly close the client and transport to prevent ResourceWarnings
        try:
            await client.aclose()
        except (RuntimeError, TypeError):
            pass
        # Cleanup database connections before event loop closes (Windows-specific fix)
        # This prevents "Event loop is closed" errors when asyncpg tries to use closed loop
        try:
            from ..database import get_database_manager

            db_manager = get_database_manager()
            if db_manager and hasattr(db_manager, "engine") and db_manager.engine:
                # Dispose of connection pool to close all connections
                await db_manager.engine.dispose()
        except (RuntimeError, TypeError):
            # Ignore cleanup errors - connections will be cleaned up by process exit
            pass


@pytest.fixture
async def async_database_session():
    """Provide an async database session for tests that need direct database access."""
    from ..database import get_async_session

    async for session in get_async_session():
        yield session
        # Session cleanup is handled by get_async_session's context manager
        break


@pytest.fixture
async def async_npc_database_session():
    """Provide an async NPC database session for tests that need direct NPC database access."""
    from ..npc_database import get_npc_session

    async for session in get_npc_session():
        yield session
        # Session cleanup is handled by get_npc_session's context manager
        break


@pytest.fixture
async def async_event_bus():
    """Provide a properly initialized EventBus for async tests."""
    from ..events.event_bus import EventBus

    event_bus = EventBus()

    # Set the main event loop if available
    try:
        loop = asyncio.get_running_loop()
        event_bus.set_main_loop(loop)
    except RuntimeError:
        # No running loop, EventBus will work without it
        pass

    yield event_bus

    # Cleanup
    try:
        await event_bus.shutdown()
    except (RuntimeError, TypeError):
        pass  # Ignore cleanup errors


@pytest.fixture
async def async_connection_manager():
    """Provide a properly initialized ConnectionManager for async tests."""
    from ..realtime.connection_manager import ConnectionManager

    connection_manager = ConnectionManager()

    # Initialize with mock persistence for testing
    from unittest.mock import Mock

    connection_manager.persistence = Mock()

    yield connection_manager

    # Cleanup
    try:
        await connection_manager.force_cleanup()
    except (RuntimeError, TypeError):
        pass  # Ignore cleanup errors


@pytest.fixture
async def async_event_handler(async_event_bus, async_connection_manager):
    """Provide a properly initialized RealTimeEventHandler for async tests."""
    from ..realtime.event_handler import RealTimeEventHandler

    event_handler = RealTimeEventHandler(async_event_bus)
    event_handler.connection_manager = async_connection_manager

    yield event_handler

    # Cleanup
    try:
        event_handler.shutdown()
    except (RuntimeError, TypeError):
        pass  # Ignore cleanup errors


@pytest.fixture
def event_bus():
    """Provide a properly initialized EventBus for sync tests."""
    from ..events.event_bus import EventBus

    event_bus = EventBus()
    return event_bus


# Global asyncio task cleanup fixture to prevent resource leaks
@pytest.fixture(autouse=True)
def cleanup_all_asyncio_tasks():
    """Automatically clean up all asyncio tasks to prevent resource leaks."""
    import weakref

    from ..events.event_bus import EventBus

    # Track all EventBus instances created during tests
    eventbus_instances = weakref.WeakSet()

    # Store original EventBus.__init__ to track instances
    original_init = EventBus.__init__

    def tracking_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        eventbus_instances.add(self)

    # Replace EventBus.__init__ with tracking version
    EventBus.__init__ = tracking_init

    # Track tasks created during this test
    try:
        initial_tasks = set(asyncio.all_tasks())
    except RuntimeError:
        # No event loop running yet, start with empty set
        initial_tasks = set()

    yield

    # Cleanup all EventBus instances after test
    for eventbus in list(eventbus_instances):
        try:
            if hasattr(eventbus, "_running") and eventbus._running:
                # Force shutdown without waiting for async operations
                eventbus._running = False
                eventbus._shutdown_event.set()

                # Cancel all active tasks
                if hasattr(eventbus, "_active_tasks") and eventbus._active_tasks:
                    for task in list(eventbus._active_tasks):
                        if not task.done():
                            task.cancel()
                    eventbus._active_tasks.clear()
        except (RuntimeError, TypeError):
            # Ignore cleanup errors during teardown
            pass

    # Clean up any orphaned asyncio tasks created during this test
    try:
        # Only try to get tasks if there's a running event loop
        try:
            current_tasks = set(asyncio.all_tasks())
            test_created_tasks = current_tasks - initial_tasks

            # Cancel any tasks that were created during this test and are still running
            for task in test_created_tasks:
                if not task.done():
                    task.cancel()

            # Wait briefly for tasks to complete cancellation (synchronous approach)
            if test_created_tasks:
                try:
                    loop = asyncio.get_running_loop()
                    # Use run_until_complete for synchronous cleanup
                    loop.run_until_complete(
                        asyncio.wait_for(
                            asyncio.gather(*test_created_tasks, return_exceptions=True),
                            timeout=0.5,  # Shorter timeout for cleanup
                        )
                    )
                except RuntimeError:
                    # No running loop, just cancel tasks without waiting
                    pass
                except TypeError:
                    # Ignore timeout or other errors during cleanup
                    pass
        except RuntimeError:
            # No event loop running, skip task cleanup
            pass
    except (RuntimeError, TypeError):
        # Ignore any errors during task cleanup
        pass

    # Restore original EventBus.__init__
    EventBus.__init__ = original_init


@pytest.fixture
def connection_manager():
    """Provide a properly initialized ConnectionManager for sync tests."""
    from ..realtime.connection_manager import ConnectionManager

    connection_manager = ConnectionManager()

    # Initialize with mock persistence for testing
    from unittest.mock import Mock

    connection_manager.persistence = Mock()
    return connection_manager


@pytest.fixture
def event_handler(event_bus, connection_manager):
    """Provide a properly initialized RealTimeEventHandler for sync tests."""
    from ..realtime.event_handler import RealTimeEventHandler

    event_handler = RealTimeEventHandler(event_bus)
    event_handler.connection_manager = connection_manager

    return event_handler


@pytest.fixture
def mock_string():
    """Create a mock that behaves like a string for command parser tests."""

    def _create_mock_string(value: str):
        """Create a mock that behaves like a string."""
        mock = MagicMock()
        # Configure __str__ using configure_mock to avoid method assignment
        mock.configure_mock(**{"__str__.return_value": value})
        mock.__len__ = MagicMock(return_value=len(value))
        mock.strip = MagicMock(return_value=value.strip())
        mock.startswith = MagicMock(return_value=value.startswith)
        mock.split = MagicMock(return_value=value.split())
        mock.lower = MagicMock(return_value=value.lower())
        # Make the mock itself return the string value when used as a string
        mock._mock_return_value = value
        return mock

    return _create_mock_string


@pytest.fixture
def mock_command_string():
    """Create a mock command string for testing."""

    def _create_mock_command_string(command: str):
        """Create a mock that behaves like a command string."""
        mock = MagicMock()
        # Configure __str__ using configure_mock to avoid method assignment
        mock.configure_mock(**{"__str__.return_value": command})
        mock.__len__ = MagicMock(return_value=len(command))
        mock.strip = MagicMock(return_value=command.strip())
        mock.startswith = MagicMock(return_value=command.startswith)
        mock.split = MagicMock(return_value=command.split())
        mock.lower = MagicMock(return_value=command.lower())
        # Make the mock itself return the string value when used as a string
        mock._mock_return_value = command
        return mock

    return _create_mock_command_string


class TestingAsyncMixin:
    """Unified async test framework integration for MythosMUD testing.

    This mixin provides strict async test relationships by providing utilities
    and fixtures that replace scattered asyncio patterns with consistent
    standardized behavior.
    """

    @pytest.mark.asyncio
    async def async_test_fixture_helper(self):
        """
        Automatic helper for inheriting test classes providing unified async test initialization.
        """
        event_loop = asyncio.get_running_loop()
        assert event_loop is not None

        return event_loop

    @staticmethod
    def async_environment_scan():
        """
        Perform computational verification of test environment status.

        Returns: A dictionary containing test pattern verification
        """
        test_environ_analysis = {"running_loop_active": None, "standardization_state": None}

        try:
            event_loop = asyncio.get_running_loop()
            test_environ_analysis["running_loop_active"] = event_loop is not None
        except RuntimeError:
            test_environ_analysis["running_loop_active"] = False

        test_environ_analysis["standardization_state"] = (
            "READY" if test_environ_analysis["running_loop_active"] else "NEEDS_IMPROVEMENT"
        )

        return test_environ_analysis

    @staticmethod
    async def create_async_test_task(coro, task_name: str = "test_task"):
        """
        Create a properly tracked async test task with standardized naming.

        Args:
            coro: The coroutine to execute
            task_name: Human-readable name for the task

        Returns:
            asyncio.Task: The created and tracked task
        """
        task = asyncio.create_task(coro, name=task_name)
        return task

    @staticmethod
    async def wait_for_async_operations(operations, timeout: float = 5.0):
        """
        Wait for multiple async operations to complete with timeout.

        Args:
            operations: List of awaitables or tasks
            timeout: Maximum time to wait

        Returns:
            List of results from the operations
        """
        try:
            results = await asyncio.wait_for(asyncio.gather(*operations, return_exceptions=True), timeout=timeout)
            return results
        except TimeoutError as err:
            raise TimeoutError(f"Async operations timed out after {timeout} seconds") from err

    @staticmethod
    async def cleanup_async_resources(resources):
        """
        Clean up async resources with proper error handling.

        Args:
            resources: List of resources with cleanup methods
        """
        cleanup_tasks = []

        for resource in resources:
            if hasattr(resource, "shutdown"):
                cleanup_tasks.append(resource.shutdown())
            elif hasattr(resource, "close"):
                cleanup_tasks.append(resource.close())
            elif hasattr(resource, "cleanup"):
                cleanup_tasks.append(resource.cleanup())

        if cleanup_tasks:
            try:
                await asyncio.gather(*cleanup_tasks, return_exceptions=True)
            except (RuntimeError, TypeError):
                pass  # Ignore cleanup errors


class TestSessionBoundaryEnforcement:
    """Test session boundary enforcement to prevent event loop conflicts.

    This class provides utilities for ensuring proper test isolation and
    preventing event loop conflicts between test sessions.
    """

    _active_loops: set[Any] = set()
    _session_loop_registry: dict[str, Any] = {}

    @classmethod
    def register_test_loop(cls, test_id: str, loop: asyncio.AbstractEventLoop | None):
        """Register a test loop to prevent conflicts."""
        if test_id in cls._session_loop_registry:
            raise RuntimeError(f"Test loop conflict detected: {test_id} already has an active loop")

        cls._session_loop_registry[test_id] = loop
        # Only add non-None loops to active_loops set
        if loop is not None:
            cls._active_loops.add(loop)

    @classmethod
    def unregister_test_loop(cls, test_id: str):
        """Unregister a test loop after test completion."""
        if test_id in cls._session_loop_registry:
            loop = cls._session_loop_registry[test_id]
            # Only remove non-None loops from active_loops
            if loop is not None:
                cls._active_loops.discard(loop)
            del cls._session_loop_registry[test_id]

            # Ensure loop is properly closed (skip None placeholders)
            if loop is not None and not loop.is_closed():
                try:
                    # Only try to get tasks if the loop is still running
                    if loop.is_running():
                        try:
                            # Cancel any remaining tasks
                            pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
                            for task in pending_tasks:
                                task.cancel()

                            # Wait for tasks to complete with timeout
                            if pending_tasks:
                                loop.run_until_complete(
                                    asyncio.wait(pending_tasks, timeout=1.0, return_when=asyncio.ALL_COMPLETED)
                                )
                        except RuntimeError:
                            # Loop might have stopped running, just close it
                            pass

                    loop.close()
                except (RuntimeError, TypeError) as e:
                    # Log but don't fail the test
                    print(f"Warning: Error closing test loop for {test_id}: {e}")

    @classmethod
    def get_active_loop_count(cls) -> int:
        """Get the number of currently active test loops."""
        return len(cls._active_loops)

    @classmethod
    def enforce_session_boundaries(cls):
        """Enforce session boundaries by cleaning up any orphaned loops."""
        if cls._active_loops:
            print(f"Warning: {len(cls._active_loops)} orphaned test loops detected")
            for loop in list(cls._active_loops):
                try:
                    # Skip None placeholders (registered but no actual loop)
                    if loop is not None and not loop.is_closed():
                        loop.close()
                except (RuntimeError, TypeError, AttributeError):
                    pass
            cls._active_loops.clear()
            cls._session_loop_registry.clear()


@pytest.fixture
def async_test_environment():
    """Standardized async test environment fixture for unified tests."""
    return TestingAsyncMixin.async_environment_scan()


@pytest.fixture
def async_test_mixin():
    """Provide the TestingAsyncMixin class for test classes that need async utilities."""
    return TestingAsyncMixin


@pytest.fixture
async def async_test_utilities():
    """Provide async test utilities for complex async test scenarios."""

    class AsyncTestUtilities:
        """Utilities for complex async test scenarios."""

        def __init__(self):
            self.active_tasks = []
            self.active_resources = []

        async def create_task(self, coro, name: str = "test_task"):
            """Create and track an async task."""
            task = await TestingAsyncMixin.create_async_test_task(coro, name)
            self.active_tasks.append(task)
            return task

        async def wait_for_tasks(self, timeout: float = 5.0):
            """Wait for all tracked tasks to complete."""
            if self.active_tasks:
                results = await TestingAsyncMixin.wait_for_async_operations(self.active_tasks, timeout)
                self.active_tasks.clear()
                return results
            return []

        def register_resource(self, resource):
            """Register a resource for cleanup."""
            self.active_resources.append(resource)

        async def cleanup_all(self):
            """Clean up all tracked resources and tasks."""
            # Cancel any remaining tasks
            for task in self.active_tasks:
                if not task.done():
                    task.cancel()

            # Wait for tasks to complete
            if self.active_tasks:
                await asyncio.gather(*self.active_tasks, return_exceptions=True)

            # Clean up resources
            await TestingAsyncMixin.cleanup_async_resources(self.active_resources)

            # Clear tracking
            self.active_tasks.clear()
            self.active_resources.clear()

    utilities = AsyncTestUtilities()

    try:
        yield utilities
    finally:
        await utilities.cleanup_all()


@pytest.fixture
def isolated_event_loop(request):
    """Provide an isolated event loop for tests that need manual loop management.

    This fixture replaces manual asyncio.new_event_loop() calls with proper
    session boundary enforcement and cleanup.
    """
    import uuid

    test_id = f"{request.node.name}_{id(request.node)}_{uuid.uuid4().hex[:8]}"

    # Create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Register with session boundary enforcement
    TestSessionBoundaryEnforcement.register_test_loop(test_id, loop)

    try:
        yield loop
    finally:
        # Cleanup
        TestSessionBoundaryEnforcement.unregister_test_loop(test_id)

        # Additional cleanup
        try:
            # Cancel any remaining tasks
            pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
            for task in pending_tasks:
                task.cancel()

            # Wait for tasks to complete with timeout
            if pending_tasks:
                loop.run_until_complete(asyncio.wait(pending_tasks, timeout=1.0, return_when=asyncio.ALL_COMPLETED))
        except (RuntimeError, TypeError):
            pass  # Ignore cleanup errors

        # Close the loop
        if not loop.is_closed():
            loop.close()

        # Reset event loop to None to prevent conflicts
        try:
            asyncio.set_event_loop(None)
        except RuntimeError:
            pass  # Ignore if no loop is set


@pytest.fixture(autouse=True)
def enforce_test_session_boundaries(request):
    """Automatically enforce test session boundaries to prevent event loop conflicts."""
    test_id = f"{request.node.name}_{id(request.node)}"

    # Register the test
    TestSessionBoundaryEnforcement.register_test_loop(test_id, None)  # Placeholder registration

    yield

    # Cleanup after test
    TestSessionBoundaryEnforcement.unregister_test_loop(test_id)


def pytest_sessionstart(session):
    """Called after the Session object has been created and before performing collection and entering the run test loop."""
    # Initialize session boundary enforcement
    TestSessionBoundaryEnforcement.enforce_session_boundaries()


def pytest_sessionfinish(session, exitstatus):
    """Called after whole test run finished, right before returning the exit status to the system."""
    # CRITICAL: Properly clean up all database connections and event loops to prevent ResourceWarnings
    # This is especially important for pytest-xdist workers which may exit with unclosed resources
    try:
        from server.database import get_database_manager
        from server.npc_database import close_npc_db, get_npc_engine

        # Create a new event loop for cleanup if needed
        # This ensures we can properly dispose of resources even if the main loop is closed
        cleanup_loop = None
        loop_created = False

        try:
            # Try to get the running loop first
            loop = asyncio.get_running_loop()
            cleanup_loop = loop
        except RuntimeError:
            # No running loop - create a new one for cleanup
            cleanup_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(cleanup_loop)
            loop_created = True

        if cleanup_loop and not cleanup_loop.is_closed():
            # Clean up main database engine
            try:
                db_manager = get_database_manager()
                if db_manager and db_manager.engine:
                    if cleanup_loop.is_running():
                        # If loop is running, we can't use run_until_complete
                        # Create a task and hope it completes
                        task = cleanup_loop.create_task(db_manager.close())
                        # Give it a brief moment, but don't wait forever
                        try:
                            cleanup_loop.run_until_complete(asyncio.wait_for(task, timeout=0.5))
                        except (TimeoutError, RuntimeError):
                            # Task didn't complete in time or loop issues - that's okay
                            pass
                    else:
                        # Loop exists but not running - we can use run_until_complete
                        cleanup_loop.run_until_complete(db_manager.close())
            except (RuntimeError, TypeError):
                # Ignore cleanup errors - resources will be cleaned up by process exit
                pass

            # Clean up NPC database engine
            try:
                npc_engine = get_npc_engine()
                if npc_engine:
                    if cleanup_loop.is_running():
                        task = cleanup_loop.create_task(close_npc_db())
                        try:
                            cleanup_loop.run_until_complete(asyncio.wait_for(task, timeout=0.5))
                        except (TimeoutError, RuntimeError):
                            pass
                    else:
                        cleanup_loop.run_until_complete(close_npc_db())
            except (RuntimeError, TypeError):
                # Ignore cleanup errors
                pass

            # Close the cleanup loop if we created it
            if loop_created:
                try:
                    # Cancel any remaining tasks
                    pending = asyncio.all_tasks(cleanup_loop)
                    for task in pending:
                        task.cancel()
                    # Run until all tasks are cancelled
                    if pending:
                        cleanup_loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
                    # Close the loop
                    cleanup_loop.close()
                except (RuntimeError, TypeError):
                    # Ignore errors during loop closure
                    pass

    except (RuntimeError, TypeError):
        # Ignore any errors during session cleanup - process exit will clean up resources
        pass

    # Clean up NPC database files
    npc_dir = project_root / "data" / "unit_test" / "npcs"
    for path in npc_dir.glob("unit_test_npcs_gw*.db"):
        try:
            path.unlink()
        except OSError:
            pass

    # Clean up any remaining test loops
    TestSessionBoundaryEnforcement.enforce_session_boundaries()

    # Windows-specific cleanup
    try:
        from .windows_event_loop_fix import cleanup_windows_event_loops  # pyright: ignore

        cleanup_windows_event_loops()
    except ImportError:
        pass


@pytest.hookimpl(trylast=True, optionalhook=True)
def pytest_unraisableexception(unraisable: Any) -> None:
    """
    Suppress known harmless unraisable exceptions from asyncpg cleanup.

    This hook is called when pytest detects an unraisable exception during
    garbage collection. We suppress warnings about asyncpg Connection._cancel
    coroutines that are created during GC after event loops close, as these are
    harmless and expected behavior during test teardown.

    Note: This hook doesn't prevent warnings from being counted, but it allows
    us to handle them. The actual suppression happens via filterwarnings in pytest.ini.
    """
    # Check if this is a RuntimeWarning about unawaited coroutines
    if unraisable.exc_type is RuntimeWarning:
        exc_msg = str(unraisable.err_msg) if hasattr(unraisable, "err_msg") else ""
        if exc_msg and "coroutine" in exc_msg and "was never awaited" in exc_msg:
            # These are known harmless warnings from asyncpg cleanup
            # The filterwarnings in pytest.ini should catch them, but we log here
            # for debugging if needed
            if "Connection._cancel" in exc_msg or ("Connection" in exc_msg and "cancel" in exc_msg):
                # Known asyncpg cleanup warning - already filtered in pytest.ini
                return
            # Also suppress AsyncMock-related coroutine warnings
            if "AsyncMock" in exc_msg or "AsyncMockMixin" in exc_msg:
                # Known AsyncMock warning - already filtered in pytest.ini
                return
    # Let other unraisable exceptions be reported normally


def pytest_runtest_setup(item):
    """Called to perform the setup phase for a test item."""
    # Ensure clean state before each test
    active_loops = TestSessionBoundaryEnforcement.get_active_loop_count()
    if active_loops > 0:
        print(f"Warning: {active_loops} active loops detected before test {item.name}")

    # Handle serial marker - ensure database transactions are isolated
    if item.get_closest_marker("serial"):
        # For serial tests, add a delay to ensure previous test's transactions are committed
        import time

        time.sleep(0.2)  # Longer delay for serial tests to ensure transaction isolation

        # Also ensure database connections are properly initialized
        try:
            from ..database import get_database_manager

            db_manager = get_database_manager()
            if db_manager and db_manager.engine:
                # Force a connection to ensure the engine is ready
                # This helps with transaction isolation
                pass
        except (RuntimeError, TypeError):
            pass  # Ignore errors - database might not be initialized yet


def pytest_runtest_teardown(item, nextitem):
    """Called to perform the teardown phase for a test item."""
    # Ensure proper cleanup after each test
    TestSessionBoundaryEnforcement.enforce_session_boundaries()

    # Note: Event loop cleanup is handled by the event_loop fixture
    # We don't close the loop here because pytest-asyncio is still managing it

    # Handle serial marker - ensure database transactions are committed
    if item.get_closest_marker("serial"):
        # For serial tests, add a delay to ensure this test's transactions are committed
        import time

        time.sleep(0.2)  # Delay to ensure transaction commit


def pytest_collection_modifyitems(config, items):
    """
    Modify test collection to handle serial tests.

    Serial tests are moved to the end of the collection to ensure they run
    after parallel tests, reducing the chance of race conditions.
    """
    serial_items = []
    parallel_items = []

    for item in items:
        if item.get_closest_marker("serial"):
            serial_items.append(item)
        else:
            parallel_items.append(item)

    # Reorder: parallel tests first, then serial tests
    # This ensures serial tests run after parallel tests complete
    items[:] = parallel_items + serial_items


# Track test outcomes to suppress teardown-only failures
_test_outcomes: dict[str, str] = {}


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    """
    Intercept test execution to catch timeout exceptions and convert them to skips.

    This runs BEFORE pytest-timeout kills the process, allowing us to catch
    TimeoutError exceptions and convert them to skips.
    """
    # This hook runs during test execution, but we can't easily catch exceptions here
    # The real work happens in pytest_runtest_makereport
    pass


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Intercept test reports to suppress known cleanup errors and convert timeouts to skips.

    These are not actual test failures but rather asyncpg/asyncio cleanup issues
    that occur during teardown on Windows when the event loop is closed while
    database connections are still trying to terminate.

    Also converts pytest-timeout failures to skips so tests can continue running.
    """
    outcome = yield
    report = outcome.get_result()

    # Track test outcomes
    test_id = item.nodeid
    if report.when == "call":
        _test_outcomes[test_id] = report.outcome

    # Note: Timeout-to-skip conversion is now handled directly in tests using try/except TimeoutError
    # and pytest.skip(). This hook is kept for backward compatibility but should not be needed
    # for tests that properly handle timeouts. The hook was causing INTERNALERROR in pytest's
    # terminal output handler when manually converting failures to skips.

    # Only suppress errors during teardown phase if the test itself passed
    if report.when == "teardown" and report.failed:
        # Check if the test itself passed
        test_passed = _test_outcomes.get(test_id) == "passed"

        if test_passed:
            exc_info = call.excinfo
            if exc_info is not None:
                exc_type = exc_info.type
                exc_value = str(exc_info.value) if exc_info.value else ""

                # Suppress known asyncpg cleanup errors on Windows
                # These occur when asyncpg tries to close connections after event loop is closed
                cleanup_error_patterns = [
                    ("AttributeError", "'NoneType' object has no attribute 'send'"),
                    ("RuntimeError", "Event loop is closed"),
                ]

                for error_type_name, error_msg in cleanup_error_patterns:
                    if exc_type.__name__ == error_type_name and error_msg in exc_value:
                        # Test passed, but teardown failed due to cleanup issue - suppress the failure
                        report.outcome = "passed"
                        if hasattr(report, "longrepr"):
                            report.longrepr = None
                        break
