"""Pytest configuration for authentication tests.

These tests involve FastAPI app creation with full middleware stack,
database initialization, and Argon2 password hashing. They typically have
20+ second setup times and are marked as slow to exclude from the fast test suite.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow marker to all tests in this directory only."""
    for item in items:
        # Only mark tests that are actually in this directory
        if "tests/unit/auth" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
