"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.
"""

import os
import sys
from pathlib import Path

import pytest

# Add the server directory to the path for imports
sys.path.append(str(Path(__file__).parent.parent))


def pytest_configure(config):
    """Configure pytest with environment variables for tests."""
    # Set required environment variables for tests
    os.environ.setdefault("MYTHOSMUD_SECRET_KEY", "test-secret-key-for-development")
    os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///data/players/players.db")
    os.environ.setdefault("TEST_DATABASE_URL", "sqlite+aiosqlite:///server/tests/data/test_players.db")


@pytest.fixture(scope="session")
def test_env_vars():
    """Provide test environment variables."""
    return {
        "MYTHOSMUD_SECRET_KEY": "test-secret-key-for-development",
        "DATABASE_URL": "sqlite+aiosqlite:///data/players/players.db",
        "TEST_DATABASE_URL": ("sqlite+aiosqlite:///server/tests/data/test_players.db"),
    }


@pytest.fixture(scope="session")
def test_database():
    """Initialize test database with proper schema."""
    from server.tests.init_test_db import init_test_database

    # Initialize the test database
    init_test_database()

    # Return the database path for tests that need it
    return "server/tests/data/test_players.db"


@pytest.fixture(autouse=True)
def ensure_test_db_ready(test_database):
    """Ensure test database is ready for each test."""
    # This fixture runs automatically for each test
    # The test_database fixture ensures the database is initialized
    pass
