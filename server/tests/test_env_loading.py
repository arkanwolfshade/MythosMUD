"""
Test environment variable loading for tests.

This module tests that environment variables are properly loaded
from the test.env file during test execution.
"""

import os


def test_environment_variables_loaded():
    """Test that all required environment variables are loaded from test.env."""
    assert os.getenv("MYTHOSMUD_SECRET_KEY") is not None
    assert os.getenv("DATABASE_URL") is not None
    assert os.getenv("MYTHOSMUD_JWT_SECRET") is not None
    assert os.getenv("MYTHOSMUD_RESET_TOKEN_SECRET") is not None
    assert os.getenv("MYTHOSMUD_VERIFICATION_TOKEN_SECRET") is not None

    # Verify we have test-specific values
    assert "test" in os.getenv("MYTHOSMUD_SECRET_KEY", "").lower()
    assert "test" in os.getenv("MYTHOSMUD_JWT_SECRET", "").lower()
    assert "test" in os.getenv("MYTHOSMUD_RESET_TOKEN_SECRET", "").lower()
    assert "test" in os.getenv("MYTHOSMUD_VERIFICATION_TOKEN_SECRET", "").lower()


def test_database_url_is_test_specific():
    """Test that DATABASE_URL points to test database."""
    database_url = os.getenv("DATABASE_URL")
    assert database_url is not None
    assert database_url.startswith("sqlite+aiosqlite:///")
    assert "test" in database_url or "tests" in database_url


def test_environment_file_loading():
    """Test that test.env file is properly loaded by conftest.py."""
    # This test verifies that the conftest.py is loading the test.env file
    # by checking that we have test-specific values
    secret_key = os.getenv("MYTHOSMUD_SECRET_KEY", "")
    assert "test-secret-key-for-development" in secret_key
