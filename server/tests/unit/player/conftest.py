"""Pytest configuration for player tests.

Player tests that use full FastAPI TestClient and app initialization
are marked as slow to exclude from fast test suite.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow marker to all tests in this directory only."""
    marked_count = 0
    for item in items:
        if "tests/unit/player" in str(item.fspath) or "tests\\unit\\player" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
            marked_count += 1
    if marked_count > 0:
        print(f"DEBUG: Marked {marked_count} player tests as slow")
