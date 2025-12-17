"""
Tests for FastAPI Users configuration.

This module tests the UserManager, authentication backends,
and user management functionality.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import Request
from fastapi_users.exceptions import InvalidID

from server.auth.users import (
    UserManager,
    get_auth_backend,
    get_current_user_with_logging,
    get_username_auth_backend,
)
from server.models.user import User


class TestUserManager:
    """Test UserManager functionality."""

    def test_hash_password_uses_argon2(self):
        """Test that UserManager uses Argon2 for password hashing."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        password = "test_password_123"
        hashed = manager._hash_password(password)

        # Should be an Argon2 hash
        assert hashed.startswith("$argon2id$")
        assert len(hashed) > 50  # Argon2 hashes are long

    def test_verify_password_uses_argon2(self):
        """Test that UserManager uses Argon2 for password verification."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        password = "test_password_123"
        hashed = manager._hash_password(password)

        # Verify password
        assert manager._verify_password(password, hashed) is True
        assert manager._verify_password("wrong_password", hashed) is False

    @pytest.mark.asyncio
    async def test_on_after_register_logs_info(self):
        """Test on_after_register logs user registration."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        user = Mock(spec=User)
        user.username = "testuser"
        user.email = "test@example.com"
        user.is_verified = False

        with patch("server.auth.users.logger.info") as mock_info:
            await manager.on_after_register(user, None)
            mock_info.assert_called_once()
            call_args = mock_info.call_args
            assert "User has registered" in str(call_args) or "username" in str(call_args)

    @pytest.mark.asyncio
    async def test_on_after_register_auto_verifies_bogus_email(self):
        """Test on_after_register auto-verifies bogus emails."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        user = Mock(spec=User)
        user.username = "testuser"
        user.email = "test@wolfshade.org"  # Bogus email
        user.is_verified = False

        with patch("server.auth.users.is_bogus_email", return_value=True):
            with patch("server.auth.users.logger.info") as mock_info:
                await manager.on_after_register(user, None)
                assert user.is_verified is True
                # Should log auto-verification
                assert mock_info.call_count >= 1

    @pytest.mark.asyncio
    async def test_on_after_register_does_not_verify_non_bogus_email(self):
        """Test on_after_register does not verify non-bogus emails."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        user = Mock(spec=User)
        user.username = "testuser"
        user.email = "test@example.com"  # Real email
        user.is_verified = False

        with patch("server.auth.users.is_bogus_email", return_value=False):
            await manager.on_after_register(user, None)
            assert user.is_verified is False

    @pytest.mark.asyncio
    async def test_on_after_register_handles_none_email(self):
        """Test on_after_register handles None email."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        user = Mock(spec=User)
        user.username = "testuser"
        user.email = None
        user.is_verified = False

        # Should not raise error
        await manager.on_after_register(user, None)
        assert user.is_verified is False

    @pytest.mark.asyncio
    async def test_on_after_forgot_password_logs_info(self):
        """Test on_after_forgot_password logs info."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        user = Mock(spec=User)
        user.username = "testuser"
        token = "reset-token-123"

        with patch("server.auth.users.logger.info") as mock_info:
            await manager.on_after_forgot_password(user, token, None)
            mock_info.assert_called_once()
            call_args = mock_info.call_args
            assert "forgot" in str(call_args).lower() or "reset_token" in str(call_args)

    @pytest.mark.asyncio
    async def test_on_after_request_verify_logs_info(self):
        """Test on_after_request_verify logs info."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        user = Mock(spec=User)
        user.username = "testuser"
        token = "verify-token-123"

        with patch("server.auth.users.logger.info") as mock_info:
            await manager.on_after_request_verify(user, token, None)
            mock_info.assert_called_once()
            call_args = mock_info.call_args
            assert "verification" in str(call_args).lower() or "verification_token" in str(call_args)

    def test_parse_id_with_uuid(self):
        """Test parse_id with UUID instance."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        test_uuid = uuid.uuid4()
        result = manager.parse_id(test_uuid)
        assert result == test_uuid
        assert isinstance(result, uuid.UUID)

    def test_parse_id_with_string(self):
        """Test parse_id with string UUID."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        test_uuid = uuid.uuid4()
        result = manager.parse_id(str(test_uuid))
        assert result == test_uuid
        assert isinstance(result, uuid.UUID)

    def test_parse_id_with_invalid_string(self):
        """Test parse_id raises InvalidID for invalid string."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        with pytest.raises(InvalidID):
            manager.parse_id("not-a-valid-uuid")

    def test_parse_id_with_invalid_type(self):
        """Test parse_id raises InvalidID for invalid type."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        with pytest.raises(InvalidID):
            manager.parse_id(12345)  # Integer is not a valid UUID

    def test_parse_id_with_none(self):
        """Test parse_id raises InvalidID for None."""
        mock_user_db = Mock()
        manager = UserManager(mock_user_db)

        with pytest.raises(InvalidID):
            manager.parse_id(None)


class TestAuthBackend:
    """Test authentication backend configuration."""

    def test_get_auth_backend_returns_backend(self):
        """Test get_auth_backend returns AuthenticationBackend."""
        backend = get_auth_backend()
        assert backend is not None
        assert backend.name == "jwt"
        assert backend.transport is not None
        assert backend.get_strategy is not None

    def test_get_username_auth_backend_returns_backend(self):
        """Test get_username_auth_backend returns UsernameAuthenticationBackend."""
        backend = get_username_auth_backend()
        assert backend is not None
        assert backend.name == "jwt"
        assert isinstance(backend, type(get_auth_backend()))  # Should be same type


class TestGetCurrentUserWithLogging:
    """Test get_current_user_with_logging functionality."""

    @pytest.mark.asyncio
    async def test_get_current_user_with_logging_success(self):
        """Test get_current_user_with_logging with successful authentication."""
        mock_user = Mock(spec=User)
        mock_user.username = "testuser"
        mock_user.id = uuid.uuid4()

        mock_request = Mock(spec=Request)
        mock_request.headers = {"Authorization": "Bearer token123"}

        mock_logger = Mock()
        mock_logger.debug = Mock()
        mock_logger.info = Mock()
        mock_logger.warning = Mock()
        mock_logger.error = Mock()

        with patch("server.auth.users.get_current_user", new_callable=AsyncMock, return_value=mock_user):
            with patch("server.auth.users.logger", mock_logger):
                logging_func = get_current_user_with_logging()
                # Extract the actual function from Depends wrapper
                actual_func = logging_func.dependency
                result = await actual_func(mock_request)

                assert result == mock_user
                mock_logger.debug.assert_called()
                mock_logger.info.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_current_user_with_logging_no_user(self):
        """Test get_current_user_with_logging when no user is returned."""
        mock_request = Mock(spec=Request)
        mock_request.headers = {"Authorization": "Bearer invalid_token"}

        mock_logger = Mock()
        mock_logger.debug = Mock()
        mock_logger.warning = Mock()

        with patch("server.auth.users.get_current_user", new_callable=AsyncMock, return_value=None):
            with patch("server.auth.users.logger", mock_logger):
                logging_func = get_current_user_with_logging()
                actual_func = logging_func.dependency
                result = await actual_func(mock_request)

                assert result is None
                mock_logger.debug.assert_called()
                mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_current_user_with_logging_exception(self):
        """Test get_current_user_with_logging handles exceptions."""
        mock_request = Mock(spec=Request)
        mock_request.headers = {"Authorization": "Bearer token"}

        mock_logger = Mock()
        mock_logger.debug = Mock()
        mock_logger.error = Mock()

        with patch("server.auth.users.get_current_user", new_callable=AsyncMock, side_effect=ValueError("Auth error")):
            with patch("server.auth.users.logger", mock_logger):
                logging_func = get_current_user_with_logging()
                actual_func = logging_func.dependency
                result = await actual_func(mock_request)

                assert result is None
                mock_logger.error.assert_called_once()
                mock_logger.debug.assert_called()

    @pytest.mark.asyncio
    async def test_get_current_user_with_logging_no_request(self):
        """Test get_current_user_with_logging with None request."""
        mock_logger = Mock()
        mock_logger.debug = Mock()

        with patch("server.auth.users.get_current_user", new_callable=AsyncMock, return_value=None):
            with patch("server.auth.users.logger", mock_logger):
                logging_func = get_current_user_with_logging()
                actual_func = logging_func.dependency
                result = await actual_func(None)

                assert result is None
                # Should handle None request gracefully
                mock_logger.debug.assert_called()

    @pytest.mark.asyncio
    async def test_get_current_user_with_logging_long_auth_header(self):
        """Test get_current_user_with_logging truncates long auth headers."""
        mock_request = Mock(spec=Request)
        long_token = "Bearer " + "x" * 100  # Very long token
        mock_request.headers = {"Authorization": long_token}

        mock_logger = Mock()
        mock_logger.debug = Mock()

        with patch("server.auth.users.get_current_user", new_callable=AsyncMock, return_value=None):
            with patch("server.auth.users.logger", mock_logger):
                logging_func = get_current_user_with_logging()
                actual_func = logging_func.dependency
                await actual_func(mock_request)

                # Check that auth header was truncated in log
                call_args = mock_logger.debug.call_args_list
                assert len(call_args) > 0
                # Should have truncated the header - check the kwargs passed to debug
                assert any(
                    "..." in str(call.kwargs.get("auth_preview", "")) for call in call_args if hasattr(call, "kwargs")
                )
