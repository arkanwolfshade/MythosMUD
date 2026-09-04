"""Pytest fixtures for auth unit tests."""

from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import Request

from server.auth.token_epoch import set_auth_epoch


# autouse: required for test isolation in this module - token generation needs an epoch
@pytest.fixture(autouse=True)
def set_auth_epoch_for_tests():
    """Set auth epoch so token generation and validation work in tests (no real server lifespan)."""
    set_auth_epoch("test-epoch-for-unit-tests")
    yield
    # Reset so other test modules don't rely on this epoch
    set_auth_epoch("test-epoch-for-unit-tests")


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    app.state = MagicMock()
    request = MagicMock(spec=Request)
    request.app = app
    return request


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.execute = AsyncMock()
    # _find_user_by_username (#633) resolves an id via SQL then fetches the mapped ORM entity via
    # session.get() to preserve identity-map tracking -- tests that mock the login lookup must
    # override this to return the user; see server/auth/endpoints.py.
    session.get = AsyncMock()
    session.add = MagicMock()
    session.flush = AsyncMock()
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    return session
