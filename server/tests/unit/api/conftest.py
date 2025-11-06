"""Pytest configuration for API endpoint tests.

These tests involve FastAPI TestClient with full app initialization including
middleware stack, database connections, and ApplicationContainer. They are marked
as slow to exclude from the fast test suite.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow marker to all tests in this directory only."""
    marked_count = 0
    for item in items:
        # Only mark tests that are actually in this directory
        if "tests/unit/api" in str(item.fspath) or "tests\\unit\\api" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
            marked_count += 1
    if marked_count > 0:
        print(f"DEBUG: Marked {marked_count} API tests as slow")
