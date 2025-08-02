"""
Test configuration and fixtures for MythosMUD server tests.

This module sets up environment variables and provides common fixtures
for all tests in the MythosMUD server.
"""

import os

import pytest


def pytest_configure(config):
    """Configure pytest with environment variables for tests."""
    # Set required environment variables for tests
    os.environ.setdefault("MYTHOSMUD_SECRET_KEY", "your-super-secret-key-here-change-this-in-production")
    os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///../../data/players/players.db")
    os.environ.setdefault("TEST_DATABASE_URL", "sqlite+aiosqlite:///./tests/data/test_players.db")


@pytest.fixture(scope="session")
def test_env_vars():
    """Provide test environment variables."""
    return {
        "MYTHOSMUD_SECRET_KEY": "your-super-secret-key-here-change-this-in-production",
        "DATABASE_URL": "sqlite+aiosqlite:///../../data/players/players.db",
        "TEST_DATABASE_URL": "sqlite+aiosqlite:///./tests/data/test_players.db",
    }
