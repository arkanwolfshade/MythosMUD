"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.
"""

import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

# Set environment variables BEFORE any imports to prevent module-level instantiations
# from using the wrong paths
os.environ["MYTHOSMUD_SECRET_KEY"] = "test-secret-key-for-development"
os.environ["MYTHOSMUD_JWT_SECRET"] = "test-jwt-secret-for-development"
os.environ["MYTHOSMUD_RESET_TOKEN_SECRET"] = "test-reset-token-secret-for-development"
os.environ["MYTHOSMUD_VERIFICATION_TOKEN_SECRET"] = "test-verification-token-secret-for-development"
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
# Get the project root (two levels up from this file)
project_root = Path(__file__).parent.parent.parent
# Ensure we're using the correct path for test logs
test_logs_dir = project_root / "server" / "tests" / "logs"
test_logs_dir.mkdir(parents=True, exist_ok=True)
# Legacy logging environment variables no longer needed - logging is handled by centralized system
os.environ["ALIASES_DIR"] = "server/tests/data/players/aliases"

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
    os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///server/tests/data/players/test_players.db"
    # Get the project root (two levels up from this file)
    project_root = Path(__file__).parent.parent.parent
    # Ensure we're using the correct path for test logs
    test_logs_dir = project_root / "server" / "tests" / "logs"
    test_logs_dir.mkdir(parents=True, exist_ok=True)
    # Legacy logging environment variables no longer needed - logging is handled by centralized system


os.environ["ALIASES_DIR"] = "server/tests/data/players/aliases"


@pytest.fixture(scope="session")
def test_env_vars():
    """Provide test environment variables."""
    return {
        "MYTHOSMUD_SECRET_KEY": os.getenv("MYTHOSMUD_SECRET_KEY", "test-secret-key-for-development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite+aiosqlite:///server/tests/data/players/test_players.db"),
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
