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

import asyncio
import os
import sys
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock
from urllib.parse import urlparse

import pytest
from dotenv import load_dotenv

from server.logging.enhanced_logging_config import get_logger

pytest_plugins = [
    "server.tests.fixtures.inventory_fixtures",
]

logger = get_logger(__name__)

# Import Windows-specific logging fixes
try:
    from .windows_logging_fix import configure_windows_logging, disable_problematic_log_handlers

    configure_windows_logging()
    disable_problematic_log_handlers()
except ImportError:
    # If the fix module doesn't exist, continue without it
    pass

# Import Windows-specific event loop fixes
try:
    from .windows_event_loop_fix import configure_windows_event_loops

    configure_windows_event_loops()
except ImportError:
    # If the fix module doesn't exist, continue without it
    pass

# CRITICAL: Load .env.unit_test file FIRST, before any other environment variable setup
# This ensures that test-specific database URLs are loaded before any modules
# that depend on them are imported
project_root = Path(__file__).parent.parent.parent


def _sqlite_url_to_path(url: str) -> Path:
    """
    Convert a sqlite+aiosqlite URL to a Path object.

    Args:
        url: Database URL in sqlite+aiosqlite format.

    Returns:
        Absolute Path corresponding to the database file.
    """

    if not url.startswith("sqlite+aiosqlite:///"):
        raise ValueError(f"Unsupported sqlite URL format: {url}")

    parsed = urlparse(url)
    # urlparse preserves the absolute portion in parsed.path
    path_str = parsed.path

    # On Windows, urlparse will keep the drive letter in the path (e.g. /E:/path)
    if path_str.startswith("/") and len(path_str) > 2 and path_str[2] == ":":
        path_str = path_str[1:]

    path = Path(path_str)
    if path.is_absolute():
        project_root_resolved = project_root.resolve()
        path_str_normalized = str(path).replace("\\", "/")
        project_root_str = str(project_root_resolved).replace("\\", "/")

        if path_str_normalized.startswith(project_root_str):
            path = path.resolve()
        elif len(path.parts) > 1 and path.parts[1] in {"data", "logs"}:
            rel_from_root = Path(*path.parts[1:])
            path = (project_root_resolved / rel_from_root).resolve()
        else:
            path = path.resolve()
    else:
        path = (project_root / path).resolve()

    return path


def _is_postgres_url(url: str) -> bool:
    """Check if a database URL is PostgreSQL."""
    return url.startswith("postgresql") or url.startswith("postgresql+asyncpg") or url.startswith("postgresql+psycopg2")


def _configure_database_urls(
    worker_id: str | None = None, apply_worker_suffix: bool = True
) -> tuple[Path | None, Path | None]:
    """
    Configure DATABASE_URL and DATABASE_NPC_URL for tests.

    For PostgreSQL URLs, keeps them as-is. For SQLite URLs, converts to absolute paths
    and adds worker-specific suffixes for NPC databases when pytest-xdist is active.

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
        with open(TEST_ENV_PATH) as f:
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
        base_npc_path = None
    except KeyError:
        raise ValueError(
            "DATABASE_NPC_URL environment variable is required for pytest-xdist workers. "
            "Please set it in server/tests/.env.unit_test to a PostgreSQL URL."
        ) from None

    worker_id = getattr(node, "workerid", None) or getattr(node, "id", None)
    if worker_id is None:
        worker_id = node.workerinput.get("workerid", "worker")

    # PostgreSQL uses shared database, no worker-specific paths needed
    if base_npc_path is None:
        # For PostgreSQL, all workers use the same database URL
        node.workerinput["MYTHOSMUD_WORKER_NPC_DB_PATH"] = npc_url
    else:
        # SQLite path manipulation (should not reach here with PostgreSQL-only)
        worker_path = base_npc_path.with_name(f"{base_npc_path.stem}_{worker_id}{base_npc_path.suffix}")
        node.workerinput["MYTHOSMUD_WORKER_NPC_DB_PATH"] = str(worker_path)


# Validate test environment before proceeding
try:
    validate_test_environment()
    load_dotenv(TEST_ENV_PATH, override=True)  # Force override existing values
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

# Set environment variables BEFORE any imports to prevent module-level
# instantiations from using the wrong paths
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"

# CRITICAL: Pydantic ServerConfig requires SERVER_PORT - set at module level
# This must happen BEFORE any server modules are imported during collection
os.environ.setdefault("SERVER_PORT", "54731")
os.environ.setdefault("SERVER_HOST", "127.0.0.1")
os.environ.setdefault("MYTHOSMUD_ADMIN_PASSWORD", "test-admin-password-for-development")
os.environ.setdefault("LOGGING_ENVIRONMENT", "unit_test")
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
        except Exception:
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
            os.environ["DATABASE_NPC_URL"] = f"sqlite+aiosqlite:///{worker_path_override}"
            apply_worker_suffix = False

    global TEST_DB_PATH, TEST_NPC_DB_PATH
    TEST_DB_PATH, TEST_NPC_DB_PATH = _configure_database_urls(worker_id, apply_worker_suffix=apply_worker_suffix)

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
    from server.tests.scripts.init_test_db import init_test_database

    # Initialize the test database
    init_test_database()

    # Return the database path from environment variable
    test_db_url = os.getenv("DATABASE_URL")
    return str(_sqlite_url_to_path(test_db_url))


@pytest.fixture(scope="session")
def test_npc_database():
    """Initialize NPC test database with proper schema."""
    import os
    import time

    # Get the NPC test database path
    from server.tests.scripts.init_npc_test_db import init_npc_test_database

    npc_test_db_path = TEST_NPC_DB_PATH

    # Always recreate worker-scoped NPC databases to guarantee consistent schema
    if npc_test_db_path.exists():
        for attempt in range(3):
            try:
                os.unlink(npc_test_db_path)
                break
            except PermissionError:
                if attempt < 2:
                    time.sleep(0.1)
                else:
                    raise

    init_npc_test_database()

    try:
        yield str(npc_test_db_path)
    finally:
        if npc_test_db_path.exists():
            try:
                os.unlink(npc_test_db_path)
            except PermissionError:
                pass


@pytest.fixture(autouse=True)  # Enable automatic use for all tests
def ensure_test_db_ready(test_database):
    """Ensure test database is ready for each test."""
    # This fixture runs automatically for each test
    # The test_database fixture ensures the database is initialized
    # Reset persistence to ensure fresh instance with new environment variables
    from ..persistence import reset_persistence

    reset_persistence()
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
    from pathlib import Path
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

    from ..events.event_bus import EventBus
    from ..game.player_service import PlayerService
    from ..main import app
    from ..persistence import get_persistence, reset_persistence
    from ..realtime.event_handler import RealTimeEventHandler
    from .scripts.init_test_db import init_test_database

    # Reset persistence to ensure fresh state
    reset_persistence()

    # Initialize the test database to ensure it exists and is accessible
    init_test_database()

    # AI Agent: Create event handler directly (no longer using global factory)
    #           Post-migration: RealTimeEventHandler uses dependency injection
    event_bus = EventBus()
    app.state.event_handler = RealTimeEventHandler(event_bus=event_bus)
    app.state.persistence = get_persistence(event_bus=event_bus)
    app.state.server_shutdown_pending = False

    # Create real PlayerService with real persistence
    player_service = PlayerService(app.state.persistence)

    # Use the comprehensive mock container
    app.state.container = mock_application_container
    # Update container's persistence, event_bus, and player_service with real instances
    mock_application_container.persistence = app.state.persistence
    mock_application_container.event_bus = app.state.event_handler.event_bus
    mock_application_container.event_handler = app.state.event_handler
    mock_application_container.player_service = player_service

    # Also set these on app.state for backward compatibility
    app.state.event_bus = app.state.event_handler.event_bus
    app.state.player_service = player_service

    client = TestClient(app)
    client.app.state.server_shutdown_pending = False
    return client


@pytest.fixture
async def async_test_client():
    """Create an async test client with properly initialized app state for async tests."""
    from httpx import AsyncClient

    from ..events.event_bus import EventBus
    from ..main import app
    from ..persistence import get_persistence, reset_persistence
    from ..realtime.event_handler import RealTimeEventHandler
    from .scripts.init_test_db import init_test_database

    # Reset persistence to ensure fresh state
    reset_persistence()

    # Initialize the test database to ensure it exists and is accessible
    init_test_database()

    # AI Agent: Create event handler directly (no longer using global factory)
    #           Post-migration: RealTimeEventHandler uses dependency injection
    event_bus = EventBus()
    app.state.event_handler = RealTimeEventHandler(event_bus=event_bus)
    app.state.persistence = get_persistence(event_bus=event_bus)
    app.state.server_shutdown_pending = False

    async with AsyncClient(app=app, base_url="http://test") as client:
        client.app.state.server_shutdown_pending = False
        yield client


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
    except Exception:
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
    except Exception:
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
    except Exception:
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
    import asyncio
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
        except Exception:
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
                except Exception:
                    # Ignore timeout or other errors during cleanup
                    pass
        except RuntimeError:
            # No event loop running, skip task cleanup
            pass
    except Exception:
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
            except Exception:
                pass  # Ignore cleanup errors


class TestSessionBoundaryEnforcement:
    """Test session boundary enforcement to prevent event loop conflicts.

    This class provides utilities for ensuring proper test isolation and
    preventing event loop conflicts between test sessions.
    """

    _active_loops: set[Any] = set()
    _session_loop_registry: dict[str, Any] = {}

    @classmethod
    def register_test_loop(cls, test_id: str, loop: asyncio.AbstractEventLoop):
        """Register a test loop to prevent conflicts."""
        if test_id in cls._session_loop_registry:
            raise RuntimeError(f"Test loop conflict detected: {test_id} already has an active loop")

        cls._session_loop_registry[test_id] = loop
        cls._active_loops.add(loop)

    @classmethod
    def unregister_test_loop(cls, test_id: str):
        """Unregister a test loop after test completion."""
        if test_id in cls._session_loop_registry:
            loop = cls._session_loop_registry[test_id]
            cls._active_loops.discard(loop)
            del cls._session_loop_registry[test_id]

            # Ensure loop is properly closed
            if not loop.is_closed():
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
                except Exception as e:
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
                    if not loop.is_closed():
                        loop.close()
                except Exception:
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
        except Exception:
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
        from .windows_event_loop_fix import cleanup_windows_event_loops

        cleanup_windows_event_loops()
    except ImportError:
        pass


def pytest_runtest_setup(item):
    """Called to perform the setup phase for a test item."""
    # Ensure clean state before each test
    active_loops = TestSessionBoundaryEnforcement.get_active_loop_count()
    if active_loops > 0:
        print(f"Warning: {active_loops} active loops detected before test {item.name}")


def pytest_runtest_teardown(item, nextitem):
    """Called to perform the teardown phase for a test item."""
    # Ensure proper cleanup after each test
    TestSessionBoundaryEnforcement.enforce_session_boundaries()
