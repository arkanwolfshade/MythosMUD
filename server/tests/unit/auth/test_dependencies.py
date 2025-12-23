"""
Tests for authentication dependencies.

This module tests dependency injection functions for
authentication and authorization.
"""

import uuid
from unittest.mock import AsyncMock, Mock

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


class TestGetCurrentSuperuser:
    """Test get_current_superuser dependency."""

    @pytest.mark.asyncio
    async def test_get_current_superuser_with_superuser(self) -> None:
        """Test get_current_superuser returns superuser."""
        mock_user = Mock(spec=User)
        mock_user.is_superuser = True

        result = await get_current_superuser(current_user=mock_user)
        assert result == mock_user

    @pytest.mark.asyncio
    async def test_get_current_superuser_with_non_superuser(self) -> None:
        """Test get_current_superuser raises 403 for non-superuser."""
        mock_user = Mock(spec=User)
        mock_user.is_superuser = False

        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_current_superuser(current_user=mock_user)

        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
        assert "privileges" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_get_current_superuser_exception_details(self) -> None:
        """Test get_current_superuser exception contains correct details."""
        mock_user = Mock(spec=User)
        mock_user.is_superuser = False

        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_current_superuser(current_user=mock_user)

        exception = exc_info.value
        assert exception.status_code == status.HTTP_403_FORBIDDEN
        assert exception.detail == "The user doesn't have enough privileges"


class TestGetCurrentVerifiedUser:
    """Test get_current_verified_user dependency."""

    @pytest.mark.asyncio
    async def test_get_current_verified_user_with_verified_user(self) -> None:
        """Test get_current_verified_user returns verified user."""
        mock_user = Mock(spec=User)
        mock_user.is_verified = True

        result = await get_current_verified_user(current_user=mock_user)
        assert result == mock_user

    @pytest.mark.asyncio
    async def test_get_current_verified_user_with_unverified_user(self) -> None:
        """Test get_current_verified_user raises 403 for unverified user."""
        mock_user = Mock(spec=User)
        mock_user.is_verified = False

        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_current_verified_user(current_user=mock_user)

        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
        assert "not verified" in exc_info.value.detail.lower()

    @pytest.mark.asyncio
    async def test_get_current_verified_user_exception_details(self) -> None:
        """Test get_current_verified_user exception contains correct details."""
        mock_user = Mock(spec=User)
        mock_user.is_verified = False

        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_current_verified_user(current_user=mock_user)

        exception = exc_info.value
        assert exception.status_code == status.HTTP_403_FORBIDDEN
        assert exception.detail == "The user is not verified"


class TestRequireInviteCode:
    """Test require_invite_code dependency."""

    @pytest.mark.asyncio
    async def test_require_invite_code_with_valid_code(self) -> None:
        """Test require_invite_code succeeds with valid invite code."""
        mock_invite_manager = Mock()
        mock_invite_manager.validate_invite = AsyncMock(return_value=Mock())

        # Should not raise exception
        await require_invite_code("valid-code-123", invite_manager=mock_invite_manager)
        mock_invite_manager.validate_invite.assert_called_once_with("valid-code-123")

    @pytest.mark.asyncio
    async def test_require_invite_code_with_logged_http_exception(self) -> None:
        """Test require_invite_code re-raises LoggedHTTPException."""
        mock_invite_manager = Mock()
        logged_exception = LoggedHTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid invite code",
            context=None,
        )
        mock_invite_manager.validate_invite = AsyncMock(side_effect=logged_exception)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await require_invite_code("invalid-code", invite_manager=mock_invite_manager)

        assert exc_info.value == logged_exception
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        # Verify the exception is re-raised, not wrapped
        assert exc_info.value.detail == "Invalid invite code"

    @pytest.mark.asyncio
    async def test_require_invite_code_with_generic_exception(self) -> None:
        """Test require_invite_code converts generic exception to LoggedHTTPException."""
        mock_invite_manager = Mock()
        generic_exception = ValueError("Some validation error")
        mock_invite_manager.validate_invite = AsyncMock(side_effect=generic_exception)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await require_invite_code("bad-code", invite_manager=mock_invite_manager)

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        assert "Invalid or expired invite code" in exc_info.value.detail
        assert exc_info.value.__cause__ == generic_exception

    @pytest.mark.asyncio
    async def test_require_invite_code_with_different_exception_types(self) -> None:
        """Test require_invite_code handles various exception types."""
        exception_types = [RuntimeError("Runtime error"), KeyError("key"), TypeError("type error")]
        for exception_type in exception_types:
            mock_invite_manager = Mock()
            mock_invite_manager.validate_invite = AsyncMock(side_effect=exception_type)

            with pytest.raises(LoggedHTTPException) as exc_info:
                await require_invite_code("test-code", invite_manager=mock_invite_manager)

            assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
            assert "Invalid or expired invite code" in exc_info.value.detail
            assert exc_info.value.__cause__ == exception_type

    @pytest.mark.asyncio
    async def test_require_invite_code_with_empty_string(self) -> None:
        """Test require_invite_code with empty invite code string."""
        mock_invite_manager = Mock()
        mock_invite_manager.validate_invite = AsyncMock(side_effect=ValueError("Invalid code"))

        with pytest.raises(LoggedHTTPException) as exc_info:
            await require_invite_code("", invite_manager=mock_invite_manager)

        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
        mock_invite_manager.validate_invite.assert_called_once_with("")


class TestGetOptionalCurrentUser:
    """Test get_optional_current_user dependency."""

    @pytest.mark.asyncio
    async def test_get_optional_current_user_with_user(self) -> None:
        """Test get_optional_current_user returns user when authenticated."""
        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"

        result = await get_optional_current_user(current_user=mock_user)
        assert result == mock_user
        assert result is not None
        assert result.id == mock_user.id

    @pytest.mark.asyncio
    async def test_get_optional_current_user_with_none(self) -> None:
        """Test get_optional_current_user returns None when not authenticated."""
        result = await get_optional_current_user(current_user=None)
        assert result is None

    @pytest.mark.asyncio
    async def test_get_optional_current_user_preserves_user_attributes(self) -> None:
        """Test get_optional_current_user preserves all user attributes."""
        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "test@example.com"
        mock_user.is_superuser = True
        mock_user.is_verified = True

        result = await get_optional_current_user(current_user=mock_user)
        assert result == mock_user
        assert result.username == "testuser"
        assert result.email == "test@example.com"
        assert result.is_superuser is True
        assert result.is_verified is True
