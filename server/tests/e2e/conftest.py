"""Pytest configuration for end-to-end tests.

These tests involve full system testing with running server and client services,
real WebSocket connections, and complete user workflows. They are marked as both
'slow' and 'e2e' to exclude them from fast test suites.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow and e2e markers to all tests in this directory only."""
    for item in items:
        # Only mark tests that are actually in this directory
        if "tests/e2e" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
            item.add_marker(pytest.mark.e2e)
