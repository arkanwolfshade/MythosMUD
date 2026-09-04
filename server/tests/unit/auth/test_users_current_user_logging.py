"""Unit tests for get_current_user_with_logging wrapper."""

import uuid
from collections.abc import Awaitable, Callable
from typing import cast
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.models.user import User


@pytest.mark.asyncio
async def test_get_current_user_with_logging_success():
    """Test _get_current_user_with_logging with successful authentication."""

    from server.auth import users

    # Verify that Depends has the dependency attribute
    depends_wrapper = users.get_current_user_with_logging()
    assert hasattr(depends_wrapper, "dependency"), "Depends object should have dependency attribute"

    mock_user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer test_token"}

    # Get the Depends wrapper and extract the inner function
    depends_wrapper = users.get_current_user_with_logging()
    # FastAPI's Depends stores the dependency callable in the dependency attribute
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_info: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    mock_logger.info = mock_info
    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger", mock_logger):
            result = await inner_function(mock_request)

            assert result == mock_user
            mock_debug.assert_called_once()
            mock_info.assert_called_once_with(
                "Authentication successful for user", username=mock_user.username, user_id=mock_user.id
            )


@pytest.mark.asyncio
async def test_get_current_user_with_logging_no_request():
    """Test _get_current_user_with_logging when request is None."""
    from server.auth import users

    mock_user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    depends_wrapper = users.get_current_user_with_logging()
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger", mock_logger):
            result = await inner_function(None)

            assert result == mock_user
            # Should log "No request" when request is None
            mock_debug.assert_called_once()
            assert mock_debug.call_args is not None
            call_kwargs = cast(dict[str, object], mock_debug.call_args.kwargs)
            assert call_kwargs.get("auth_preview") == "No request"


@pytest.mark.asyncio
async def test_get_current_user_with_logging_no_user():
    """Test _get_current_user_with_logging when no user is returned."""
    from server.auth.users import get_current_user_with_logging

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer test_token"}

    depends_wrapper = get_current_user_with_logging()
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_warning: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    mock_logger.warning = mock_warning
    with patch("server.auth.users.get_current_user", new_callable=AsyncMock, return_value=None):
        with patch("server.auth.users.logger", mock_logger):
            result = await inner_function(mock_request)

            assert result is None
            mock_debug.assert_called_once()
            mock_warning.assert_called_once_with("Authentication failed: No user returned from get_current_user")


@pytest.mark.asyncio
async def test_get_current_user_with_logging_http_exception():
    """Test _get_current_user_with_logging when HTTPException is raised."""
    from fastapi import HTTPException

    from server.auth import users

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer invalid_token"}

    http_exception = HTTPException(status_code=401, detail="Invalid token")

    depends_wrapper = users.get_current_user_with_logging()
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_warning: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    mock_logger.warning = mock_warning
    with patch.object(users, "get_current_user", new_callable=AsyncMock, side_effect=http_exception):
        with patch.object(users, "logger", mock_logger):
            result = await inner_function(mock_request)

            assert result is None
            mock_debug.assert_called_once()
            mock_warning.assert_called_once_with("Authentication HTTP error", status_code=401, detail="Invalid token")


@pytest.mark.asyncio
async def test_get_current_user_with_logging_generic_exception():
    """Test _get_current_user_with_logging when generic Exception is raised."""
    from server.auth import users

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer test_token"}

    depends_wrapper = users.get_current_user_with_logging()
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_error: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    mock_logger.error = mock_error
    with patch.object(users, "get_current_user", new_callable=AsyncMock, side_effect=Exception("Unexpected error")):
        with patch.object(users, "logger", mock_logger):
            result = await inner_function(mock_request)

            assert result is None
            mock_debug.assert_called()
            # Should log error twice (error and debug)
            assert mock_error.call_count == 1
            assert mock_debug.call_count >= 2  # Once for auth attempt, once for error details
            assert mock_error.call_args is not None
            assert "Unexpected authentication error" in str(mock_error.call_args)


@pytest.mark.asyncio
async def test_get_current_user_with_logging_long_auth_header():
    """Test _get_current_user_with_logging with long Authorization header."""
    from server.auth import users

    mock_user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Create a very long auth header (> 50 chars)
    long_token = "a" * 100
    mock_request = MagicMock()
    mock_request.headers = {"Authorization": f"Bearer {long_token}"}

    depends_wrapper = users.get_current_user_with_logging()
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger", mock_logger):
            result = await inner_function(mock_request)

            assert result == mock_user
            mock_debug.assert_called_once()
            # Check that auth_preview was truncated
            assert mock_debug.call_args is not None
            call_kwargs = cast(dict[str, object], mock_debug.call_args.kwargs)
            auth_preview = call_kwargs.get("auth_preview", "")
            assert isinstance(auth_preview, str)
            assert len(auth_preview) <= 53  # 50 chars + "..."
            assert "..." in auth_preview


@pytest.mark.asyncio
async def test_get_current_user_with_logging_no_auth_header():
    """Test _get_current_user_with_logging when Authorization header is missing."""
    from server.auth import users

    mock_user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    mock_request = MagicMock()
    mock_request.headers = {}  # No Authorization header

    depends_wrapper = users.get_current_user_with_logging()
    dependency = depends_wrapper.dependency
    assert dependency is not None
    inner_function = cast(Callable[..., Awaitable[User | None]], dependency)

    mock_logger: MagicMock = MagicMock()
    mock_debug: MagicMock = MagicMock()
    mock_logger.debug = mock_debug
    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger", mock_logger):
            result = await inner_function(mock_request)

            assert result == mock_user
            mock_debug.assert_called_once()
            assert mock_debug.call_args is not None
            call_kwargs = cast(dict[str, object], mock_debug.call_args.kwargs)
            assert call_kwargs.get("auth_preview") == "Not provided"
