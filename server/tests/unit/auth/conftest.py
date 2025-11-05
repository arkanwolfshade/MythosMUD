"""Pytest configuration for authentication tests.

These tests involve FastAPI app creation with full middleware stack,
database initialization, and Argon2 password hashing. They typically have
20+ second setup times and are marked as slow to exclude from the fast test suite.
"""

import pytest

# Mark all tests in this directory as slow
# Auth tests involve heavy FastAPI app setup, database initialization,
# and time-intensive password hashing operations - not suitable for rapid feedback
pytestmark = pytest.mark.slow
