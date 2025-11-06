"""Pytest configuration for service layer tests.

Service tests that use full FastAPI TestClient and app initialization
are marked as slow to exclude from fast test suite.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow marker to all tests in this directory only."""
    marked_count = 0
    for item in items:
        if "tests/unit/services" in str(item.fspath) or "tests\\unit\\services" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
            marked_count += 1
    if marked_count > 0:
        print(f"DEBUG: Marked {marked_count} service tests as slow")
