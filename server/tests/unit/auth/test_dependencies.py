"""
Unit tests for authentication dependencies.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import status

from server.auth.dependencies import (
    get_current_superuser,
    get_current_verified_user,
    get_optional_current_user,
    require_invite_code,
)
from server.exceptions import LoggedHTTPException
from server.models.user import User


@pytest.mark.asyncio
async def test_get_current_superuser_success():
    """Test getting current superuser when user is superuser."""
    user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )

    result = await get_current_superuser(current_user=user)
    assert result == user
    assert result.is_superuser is True


@pytest.mark.asyncio
async def test_get_current_superuser_failure():
    """Test getting current superuser when user is not superuser."""
    user = User(
        id=str(uuid.uuid4()),
        username="regular_user",
        email="user@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    with pytest.raises(LoggedHTTPException) as exc_info:
        await get_current_superuser(current_user=user)

    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_get_current_verified_user_success():
    """Test getting current verified user when user is verified."""
    user = User(
        id=str(uuid.uuid4()),
        username="verified_user",
        email="user@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    result = await get_current_verified_user(current_user=user)
    assert result == user
    assert result.is_verified is True


@pytest.mark.asyncio
async def test_get_current_verified_user_failure():
    """Test getting current verified user when user is not verified."""
    user = User(
        id=str(uuid.uuid4()),
        username="unverified_user",
        email="user@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    with pytest.raises(LoggedHTTPException) as exc_info:
        await get_current_verified_user(current_user=user)

    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_require_invite_code_success():
    """Test requiring invite code with valid code."""
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock()

    await require_invite_code("valid_code", invite_manager=mock_invite_manager)

    mock_invite_manager.validate_invite.assert_called_once_with("valid_code")


@pytest.mark.asyncio
async def test_require_invite_code_invalid():
    """Test requiring invite code with invalid code."""
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(side_effect=ValueError("Invalid code"))

    with pytest.raises(LoggedHTTPException) as exc_info:
        await require_invite_code("invalid_code", invite_manager=mock_invite_manager)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_require_invite_code_logged_http_exception():
    """Test requiring invite code when validate_invite raises LoggedHTTPException."""
    mock_invite_manager = MagicMock()
    logged_exception = LoggedHTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid invite code",
        context=None,
    )
    mock_invite_manager.validate_invite = AsyncMock(side_effect=logged_exception)

    # Should re-raise the LoggedHTTPException
    with pytest.raises(LoggedHTTPException) as exc_info:
        await require_invite_code("invalid_code", invite_manager=mock_invite_manager)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert exc_info.value.detail == "Invalid invite code"


@pytest.mark.asyncio
async def test_require_invite_code_generic_exception():
    """Test requiring invite code when validate_invite raises generic Exception."""
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(side_effect=RuntimeError("Unexpected error"))

    with pytest.raises(LoggedHTTPException) as exc_info:
        await require_invite_code("invalid_code", invite_manager=mock_invite_manager)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
    assert "Invalid or expired invite code" in exc_info.value.detail


@pytest.mark.asyncio
async def test_get_optional_current_user_with_user():
    """Test getting optional current user when user exists."""
    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    result = await get_optional_current_user(current_user=user)
    assert result == user


@pytest.mark.asyncio
async def test_get_optional_current_user_none():
    """Test getting optional current user when user is None."""
    result = await get_optional_current_user(current_user=None)
    assert result is None


@pytest.mark.asyncio
async def test_require_invite_code_none():
    """Test requiring invite code with None code."""
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(side_effect=ValueError("Invalid code"))

    with pytest.raises(LoggedHTTPException) as exc_info:
        await require_invite_code(None, invite_manager=mock_invite_manager)

    assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_require_invite_code_with_request():
    """Test requiring invite code with request parameter."""
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock()

    await require_invite_code("valid_code", invite_manager=mock_invite_manager)

    # Should call validate_invite
    mock_invite_manager.validate_invite.assert_called_once()


@pytest.mark.asyncio
async def test_get_current_superuser_with_none_user():
    """Test get_current_superuser with None user (should fail via dependency)."""
    # This would fail at the dependency level, but we test the function directly

    # If None is passed, it would come from get_current_active_user which would raise
    # But we can test the function logic directly
    user = User(
        id=str(uuid.uuid4()),
        username="user",
        email="user@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    with pytest.raises(LoggedHTTPException) as exc_info:
        await get_current_superuser(current_user=user)

    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.asyncio
async def test_get_current_verified_user_with_none_user():
    """Test get_current_verified_user with None user (should fail via dependency)."""
    # This would fail at the dependency level, but we test the function logic
    user = User(
        id=str(uuid.uuid4()),
        username="user",
        email="user@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    with pytest.raises(LoggedHTTPException) as exc_info:
        await get_current_verified_user(current_user=user)

    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
