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

# Set environment variables BEFORE any imports to prevent module-level
# instantiations from using the wrong paths
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"
# Get the project root (two levels up from this file)
project_root = Path(__file__).parent.parent.parent
# Use absolute path to ensure database is created in the correct location
test_db_path = project_root / "server" / "tests" / "data" / "players" / "test_players.db"
test_db_path.parent.mkdir(parents=True, exist_ok=True)
os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{test_db_path}"
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

# Load test environment variables from .env.test file
TEST_ENV_PATH = Path(__file__).parent.parent.parent / ".env.test"
if TEST_ENV_PATH.exists():
    load_dotenv(TEST_ENV_PATH, override=True)  # Force override existing values
    print(f"✓ Loaded test environment from {TEST_ENV_PATH}")
else:
    print(f"⚠️  Test environment file not found at {TEST_ENV_PATH}")
    print("Using default test environment variables")


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
    # Use absolute path to ensure database is created in the correct location
    test_db_path = project_root / "server" / "tests" / "data" / "players" / "test_players.db"
    test_db_path.parent.mkdir(parents=True, exist_ok=True)
    os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{test_db_path}"
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
        return test_db_url.replace("sqlite+aiosqlite:///", "")
    else:
        raise ValueError(f"Unsupported database URL format: {test_db_url}")


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
