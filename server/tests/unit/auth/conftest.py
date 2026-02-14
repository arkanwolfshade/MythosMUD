"""Pytest fixtures for auth unit tests."""

import pytest

from server.auth.token_epoch import set_auth_epoch


# autouse: required for test isolation in this module - token generation needs an epoch
@pytest.fixture(autouse=True)
def set_auth_epoch_for_tests():
    """Set auth epoch so token generation and validation work in tests (no real server lifespan)."""
    set_auth_epoch("test-epoch-for-unit-tests")
    yield
    # Reset so other test modules don't rely on this epoch
    set_auth_epoch("test-epoch-for-unit-tests")
