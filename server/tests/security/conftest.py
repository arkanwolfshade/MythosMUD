"""Pytest configuration for security tests.

These tests involve full FastAPI app creation with complete middleware stack,
comprehensive security header validation, and penetration testing. They typically
have 20+ second setup times and are marked as slow to exclude from the fast test suite.
"""

import pytest

# Mark all tests in this directory as slow
# Security tests involve full app initialization with all middleware,
# comprehensive security validation, and penetration testing scenarios
pytestmark = pytest.mark.slow
