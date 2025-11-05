"""Pytest configuration for end-to-end tests.

These tests involve full system testing with running server and client services,
real WebSocket connections, and complete user workflows. They are marked as both
'slow' and 'e2e' to exclude them from fast test suites.
"""

import pytest

# Mark all tests in this directory as both slow and e2e
# E2E tests require running server/client and test complete workflows
pytestmark = [pytest.mark.slow, pytest.mark.e2e]
