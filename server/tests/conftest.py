"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.
"""

import asyncio
import os
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest
from dotenv import load_dotenv

# CRITICAL: Load .env.test file FIRST, before any other environment variable setup
# This ensures that test-specific database URLs are loaded before any modules
# that depend on them are imported
project_root = Path(__file__).parent.parent.parent
TEST_ENV_PATH = project_root / ".env.test"
if TEST_ENV_PATH.exists():
    load_dotenv(TEST_ENV_PATH, override=True)  # Force override existing values
    print(f"[OK] Loaded test environment from {TEST_ENV_PATH}")
else:
    print(f"[WARNING] Test environment file not found at {TEST_ENV_PATH}")
    print("Using default test environment variables")

# Set environment variables BEFORE any imports to prevent module-level
# instantiations from using the wrong paths
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"

# CRITICAL: Set database URLs IMMEDIATELY to prevent import-time failures
# This must happen before any database modules are imported

# Ensure DATABASE_URL is set with absolute path
database_url = os.getenv("DATABASE_URL")
if database_url:
    # Convert relative paths to absolute paths
    if database_url.startswith("sqlite+aiosqlite:///") and not database_url.startswith("sqlite+aiosqlite:///E:"):
        # Extract the relative path and make it absolute
        relative_path = database_url.replace("sqlite+aiosqlite:///", "")
        absolute_path = project_root / relative_path
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{absolute_path}"
        print(f"[OK] Converted DATABASE_URL to absolute path: {os.environ['DATABASE_URL']}")
else:
    # Use absolute path to ensure database is created in the correct location
    test_db_path = project_root / "server" / "tests" / "data" / "players" / "test_players.db"
    test_db_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{test_db_path}"
    print(f"[OK] Set DATABASE_URL to: {os.environ['DATABASE_URL']}")

# Ensure NPC_DATABASE_URL is set with absolute path
npc_database_url = os.getenv("NPC_DATABASE_URL")
if npc_database_url:
    # Convert relative paths to absolute paths
    if npc_database_url.startswith("sqlite+aiosqlite:///") and not npc_database_url.startswith(
        "sqlite+aiosqlite:///E:"
    ):
        # Extract the relative path and make it absolute
        relative_path = npc_database_url.replace("sqlite+aiosqlite:///", "")
        absolute_path = project_root / relative_path
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        os.environ["NPC_DATABASE_URL"] = f"sqlite+aiosqlite:///{absolute_path}"
        print(f"[OK] Converted NPC_DATABASE_URL to absolute path: {os.environ['NPC_DATABASE_URL']}")
else:
    # Use absolute path to ensure NPC database is created in the correct location
    test_npc_db_path = project_root / "server" / "tests" / "data" / "npcs" / "test_npcs.db"
    test_npc_db_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ["NPC_DATABASE_URL"] = f"sqlite+aiosqlite:///{test_npc_db_path}"
    print(f"[OK] Set NPC_DATABASE_URL to: {os.environ['NPC_DATABASE_URL']}")

# Ensure we're using the correct path for test logs
test_logs_dir = project_root / "server" / "tests" / "logs"
test_logs_dir.mkdir(parents=True, exist_ok=True)
# Set test configuration file path
test_config_path = project_root / "server" / "tests" / "test_server_config.yaml"
os.environ["MYTHOSMUD_CONFIG_PATH"] = str(test_config_path)
# Legacy logging environment variables no longer needed - logging is handled by
# centralized system
# Use absolute path for aliases directory to prevent incorrect directory creation
aliases_dir = project_root / "server" / "tests" / "data" / "players" / "aliases"
aliases_dir.mkdir(parents=True, exist_ok=True)
os.environ["ALIASES_DIR"] = str(aliases_dir)

# Add the server directory to the path for imports
sys.path.append(str(Path(__file__).parent.parent))

# Import test environment fixtures to make them available to all tests


# Create synchronous wrapper fixtures for async fixtures
@pytest.fixture
def sync_test_environment():
    """Synchronous wrapper for test_environment async fixture"""
    import uuid

    from .utils.test_environment import test_env_manager

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
        loop.close()


def pytest_configure(config):
    """Configure pytest with test environment variables."""
    # Set required test environment variables, overriding any existing values
    # These are test-specific defaults that should only be used if test.env is not loaded
    os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
    os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
    os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
    os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"

    # Get the project root (two levels up from this file)
    project_root = Path(__file__).parent.parent.parent

    # Only set DATABASE_URL if not already set by .env.test
    # Ensure DATABASE_URL is set with absolute path
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        # Convert relative paths to absolute paths
        if database_url.startswith("sqlite+aiosqlite:///") and not database_url.startswith("sqlite+aiosqlite:///E:"):
            # Extract the relative path and make it absolute
            relative_path = database_url.replace("sqlite+aiosqlite:///", "")
            absolute_path = project_root / relative_path
            absolute_path.parent.mkdir(parents=True, exist_ok=True)
            os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{absolute_path}"
            print(f"[OK] Converted DATABASE_URL to absolute path: {os.environ['DATABASE_URL']}")
    else:
        # Use absolute path to ensure database is created in the correct location
        test_db_path = project_root / "server" / "tests" / "data" / "players" / "test_players.db"
        test_db_path.parent.mkdir(parents=True, exist_ok=True)
        os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{test_db_path}"

    # Ensure NPC_DATABASE_URL is set with absolute path
    npc_database_url = os.getenv("NPC_DATABASE_URL")
    if npc_database_url:
        # Convert relative paths to absolute paths
        if npc_database_url.startswith("sqlite+aiosqlite:///") and not npc_database_url.startswith(
            "sqlite+aiosqlite:///E:"
        ):
            # Extract the relative path and make it absolute
            relative_path = npc_database_url.replace("sqlite+aiosqlite:///", "")
            absolute_path = project_root / relative_path
            absolute_path.parent.mkdir(parents=True, exist_ok=True)
            os.environ["NPC_DATABASE_URL"] = f"sqlite+aiosqlite:///{absolute_path}"
            print(f"[OK] Converted NPC_DATABASE_URL to absolute path: {os.environ['NPC_DATABASE_URL']}")
    else:
        # Use absolute path to ensure NPC database is created in the correct location
        test_npc_db_path = project_root / "server" / "tests" / "data" / "npcs" / "test_npcs.db"
        test_npc_db_path.parent.mkdir(parents=True, exist_ok=True)
        os.environ["NPC_DATABASE_URL"] = f"sqlite+aiosqlite:///{test_npc_db_path}"

    # Ensure we're using the correct path for test logs
    test_logs_dir = project_root / "server" / "tests" / "logs"
    test_logs_dir.mkdir(parents=True, exist_ok=True)
    # Legacy logging environment variables no longer needed - logging is handled by centralized system
    # Use absolute path for aliases directory to prevent incorrect directory creation
    aliases_dir = project_root / "server" / "tests" / "data" / "players" / "aliases"
    aliases_dir.mkdir(parents=True, exist_ok=True)
    os.environ["ALIASES_DIR"] = str(aliases_dir)


@pytest.fixture(scope="session")
def test_env_vars():
    """Provide test environment variables."""
    return {
        "MYTHOSMUD_SECRET_KEY": os.getenv("MYTHOSMUD_SECRET_KEY", "test-secret-key-for-development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{test_db_path}"),
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
    from server.tests.init_test_db import init_test_database

    # Initialize the test database
    init_test_database()

    # Return the database path from environment variable
    test_db_url = os.getenv("DATABASE_URL")
    if test_db_url.startswith("sqlite+aiosqlite:///"):
        db_path = test_db_url.replace("sqlite+aiosqlite:///", "")
        return db_path
    else:
        raise ValueError(f"Unsupported database URL format: {test_db_url}")


@pytest.fixture(scope="session")
def test_npc_database():
    """Initialize NPC test database with proper schema."""
    import os

    # Get the NPC test database path
    from pathlib import Path

    from server.tests.init_npc_test_db import init_npc_test_database

    npc_test_db_path = Path(__file__).parent / "data" / "npcs" / "test_npcs.db"

    # Remove existing database file to ensure clean state
    if npc_test_db_path.exists():
        os.unlink(npc_test_db_path)

    # Initialize the NPC test database with schema
    init_npc_test_database()

    # The SQLAlchemy metadata initialization will happen when the NPC database
    # module is imported and the engine is created. We don't need to call
    # init_npc_database() here as it's meant for runtime initialization.

    return str(npc_test_db_path)


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
def test_client():
    """Create a test client with properly initialized app state."""

    from fastapi.testclient import TestClient

    from ..main import app
    from ..persistence import get_persistence, reset_persistence
    from ..realtime.event_handler import get_real_time_event_handler
    from ..tests.init_test_db import init_test_database

    # Reset persistence to ensure fresh state
    reset_persistence()

    # Initialize the test database to ensure it exists and is accessible
    init_test_database()

    # Initialize the app state manually for tests
    app.state.event_handler = get_real_time_event_handler()
    app.state.persistence = get_persistence(event_bus=app.state.event_handler.event_bus)

    return TestClient(app)


@pytest.fixture
async def async_test_client():
    """Create an async test client with properly initialized app state for async tests."""
    from httpx import AsyncClient

    from ..main import app
    from ..persistence import get_persistence, reset_persistence
    from ..realtime.event_handler import get_real_time_event_handler
    from ..tests.init_test_db import init_test_database

    # Reset persistence to ensure fresh state
    reset_persistence()

    # Initialize the test database to ensure it exists and is accessible
    init_test_database()

    # Initialize the app state manually for tests
    app.state.event_handler = get_real_time_event_handler()
    app.state.persistence = get_persistence(event_bus=app.state.event_handler.event_bus)

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
async def async_database_session():
    """Provide an async database session for tests that need direct database access."""
    from ..database import get_async_session

    async for session in get_async_session():
        try:
            yield session
        finally:
            await session.close()


@pytest.fixture
async def async_npc_database_session():
    """Provide an async NPC database session for tests that need direct NPC database access."""
    from ..npc_database import get_npc_async_session

    async for session in get_npc_async_session():
        try:
            yield session
        finally:
            await session.close()


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
        mock.__str__ = MagicMock(return_value=value)
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
        mock.__str__ = MagicMock(return_value=command)
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

    _active_loops = set()
    _session_loop_registry = {}

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
                    # Cancel any remaining tasks
                    pending_tasks = [task for task in asyncio.all_tasks(loop) if not task.done()]
                    for task in pending_tasks:
                        task.cancel()

                    # Wait for tasks to complete with timeout
                    if pending_tasks:
                        loop.run_until_complete(
                            asyncio.wait(pending_tasks, timeout=1.0, return_when=asyncio.ALL_COMPLETED)
                        )

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
    # Clean up any remaining test loops
    TestSessionBoundaryEnforcement.enforce_session_boundaries()


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
