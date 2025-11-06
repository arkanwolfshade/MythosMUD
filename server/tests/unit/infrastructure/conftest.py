"""Pytest configuration for infrastructure tests.

These tests involve heavy database setup, service initialization, and integration
testing. They typically have 20+ second setup times and are marked as slow to
exclude from the fast test suite.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow marker to all tests in this directory only."""
    marked_count = 0
    for item in items:
        # Only mark tests that are actually in this directory
        if "tests/unit/infrastructure" in str(item.fspath) or "tests\\unit\\infrastructure" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
            marked_count += 1
    if marked_count > 0:
        print(f"DEBUG: Marked {marked_count} infrastructure tests as slow")
