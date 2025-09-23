"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.
"""

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
    print(f"✓ Loaded test environment from {TEST_ENV_PATH}")
else:
    print(f"⚠️  Test environment file not found at {TEST_ENV_PATH}")
    print("Using default test environment variables")

# Set environment variables BEFORE any imports to prevent module-level
# instantiations from using the wrong paths
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"

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
        print(f"✓ Converted DATABASE_URL to absolute path: {os.environ['DATABASE_URL']}")
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
        print(f"✓ Converted NPC_DATABASE_URL to absolute path: {os.environ['NPC_DATABASE_URL']}")
else:
    # Use absolute path to ensure NPC database is created in the correct location
    test_npc_db_path = project_root / "server" / "tests" / "data" / "npcs" / "test_npcs.db"
    test_npc_db_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ["NPC_DATABASE_URL"] = f"sqlite+aiosqlite:///{test_npc_db_path}"

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
    import asyncio
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
            print(f"✓ Converted DATABASE_URL to absolute path: {os.environ['DATABASE_URL']}")
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
            print(f"✓ Converted NPC_DATABASE_URL to absolute path: {os.environ['NPC_DATABASE_URL']}")
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
    import asyncio

    from server.npc_database import init_npc_database
    from server.tests.init_npc_test_db import init_npc_test_database

    # Initialize the NPC test database
    init_npc_test_database()

    # Also initialize the NPC database through the main initialization function
    # This ensures the SQLAlchemy metadata is properly set up
    asyncio.run(init_npc_database())

    # Return the NPC database path
    from pathlib import Path

    npc_test_db_path = Path(__file__).parent / "data" / "npcs" / "test_npcs.db"
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
