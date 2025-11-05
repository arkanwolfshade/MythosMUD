"""Pytest configuration for real-time communication tests.

Real-time WebSocket and SSE tests require full FastAPI app initialization with middleware,
persistence layers, and connection managers. These are marked as slow.
"""

import pytest


def pytest_collection_modifyitems(items):
    """Add slow marker to all tests in this directory only."""
    marked_count = 0
    for item in items:
        if "tests/unit/realtime" in str(item.fspath) or "tests\\unit\\realtime" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
            marked_count += 1
    if marked_count > 0:
        print(f"DEBUG: Marked {marked_count} realtime tests as slow")
