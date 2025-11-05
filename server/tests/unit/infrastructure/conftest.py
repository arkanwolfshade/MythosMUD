"""Pytest configuration for infrastructure tests.

These tests involve heavy database setup, service initialization, and integration
testing. They typically have 20+ second setup times and are marked as slow to
exclude from the fast test suite.
"""

import pytest

# Mark all tests in this directory as slow
# Infrastructure tests involve real database setup, dependency injection,
# and comprehensive service initialization - not suitable for rapid feedback
pytestmark = pytest.mark.slow
