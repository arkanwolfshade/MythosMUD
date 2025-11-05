"""Pytest configuration for integration tests.

These tests involve full system integration with real databases, NATS messaging,
WebSocket connections, and complex service interactions. They typically have
20+ second setup times and are marked as slow to exclude from the fast test suite.
"""

import pytest

# Mark all tests in this directory as slow
# Integration tests involve full system setup with real dependencies
# and are not suitable for rapid feedback during development
pytestmark = pytest.mark.slow
