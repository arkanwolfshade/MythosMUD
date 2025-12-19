"""
Coverage tests for authentication endpoints.
Targets missing branches and error handling in server/auth/endpoints.py.
"""

import uuid
from typing import Any, cast
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import Request
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.auth.endpoints import (
    LoginRequest,
    UserCreate,
    login_user,
    register_user,
)
from server.exceptions import LoggedHTTPException
from server.models.user import User


class TestAuthEndpointsCoverage:
    """Test missing branches in auth endpoints."""

    @pytest.mark.asyncio
    async def test_register_user_invite_error(self) -> None:
        """Test register_user handles invite validation errors."""
        user_create = UserCreate(username="newuser", password="password123", invite_code="INVALID")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()

        mock_invite_manager = Mock()
        mock_invite_manager.validate_invite = AsyncMock(
            side_effect=LoggedHTTPException(status_code=400, detail="Invalid invite")
        )

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await register_user(user_create, mock_request, mock_invite_manager, Mock())

            assert exc_info.value.status_code == 400
            assert "Invalid invite" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_register_user_invite_sql_error(self) -> None:
        """Test register_user logs but doesn't fail on invite update SQL error."""
        user_create = UserCreate(username="newuser", password="password123", invite_code="VALID")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)
        mock_session.execute = AsyncMock(side_effect=[mock_result, SQLAlchemyError("Update failed")])

        mock_invite_manager = Mock()
        mock_invite_manager.validate_invite = AsyncMock(return_value=Mock())

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
                with patch("fastapi_users.jwt.generate_jwt", return_value="token"):
                    with patch("server.auth.endpoints.logger.error") as mock_error:
                        result = await register_user(user_create, mock_request, mock_invite_manager, mock_session)

                        assert result.access_token == "token"
                        # Should have logged the error but succeeded
                        assert any("Failed to mark invite as used" in str(call) for call in mock_error.call_args_list)

    @pytest.mark.asyncio
    async def test_register_user_generic_integrity_error(self) -> None:
        """Test register_user handles generic IntegrityError."""
        user_create = UserCreate(username="user", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)
        mock_session.execute = AsyncMock(return_value=mock_result)

        # IntegrityError with generic message
        mock_integrity_error = IntegrityError("statement", "params", cast(Any, "orig"))
        mock_integrity_error.orig = Exception("some_other_constraint")
        mock_session.commit = AsyncMock(side_effect=mock_integrity_error)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await register_user(user_create, mock_request, Mock(), mock_session)

                assert exc_info.value.status_code == 400
                assert "A user with this information already exists" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_register_user_unexpected_exception(self) -> None:
        """Test register_user handles unexpected exceptions."""
        user_create = UserCreate(username="user", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_session.execute = AsyncMock(side_effect=RuntimeError("Extreme failure"))

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(RuntimeError, match="Extreme failure"):
                await register_user(user_create, mock_request, Mock(), mock_session)

    @pytest.mark.asyncio
    async def test_login_user_id_mismatch(self) -> None:
        """Test login_user handles user ID mismatch (defensive)."""
        login_req = LoginRequest(username="user", password="password")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.email = "user@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        # Authenticate returns a DIFFERENT user ID
        mock_other_user = Mock(spec=User)
        mock_other_user.id = uuid.uuid4()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_other_user)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await login_user(login_req, mock_request, mock_user_manager, mock_session)

            assert exc_info.value.status_code == 401
            assert "Invalid credentials" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_login_user_profession_lookup_error(self) -> None:
        """Test login_user handles profession lookup error."""
        login_req = LoginRequest(username="user", password="password")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.email = "user@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_user)

        from datetime import UTC, datetime

        mock_player = Mock()
        mock_player.player_id = uuid.uuid4()
        mock_player.name = "TestChar"
        mock_player.profession_id = 1
        mock_player.level = 1
        mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
        mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)

        mock_persistence = Mock()
        mock_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])
        # Profession lookup raises error
        mock_persistence.get_profession_by_id = AsyncMock(side_effect=SQLAlchemyError("DB down"))

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("fastapi_users.jwt.generate_jwt", return_value="token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_persistence):
                    result = await login_user(login_req, mock_request, mock_user_manager, mock_session)

                    assert result.access_token == "token"
                    assert len(result.characters) == 1
                    assert result.characters[0]["profession_name"] is None

    @pytest.mark.asyncio
    async def test_register_user_shutdown_blocking(self) -> None:
        """Test register_user blocked by shutdown."""
        user_create = UserCreate(username="newuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
            with patch("server.commands.admin_shutdown_command.get_shutdown_blocking_message", return_value="Shutdown"):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await register_user(user_create, mock_request, Mock(), Mock())
                assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_login_user_shutdown_blocking(self) -> None:
        """Test login_user blocked by shutdown."""
        login_req = LoginRequest(username="user", password="password")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
            with patch("server.commands.admin_shutdown_command.get_shutdown_blocking_message", return_value="Shutdown"):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await login_user(login_req, mock_request, Mock(), Mock())
                assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_register_user_duplicate_email_integrity_error(self) -> None:
        """Test register_user handles duplicate email IntegrityError."""
        user_create = UserCreate(username="user", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)
        mock_session.execute = AsyncMock(return_value=mock_result)

        # IntegrityError with email constraint
        mock_integrity_error = IntegrityError("statement", "params", cast(Any, "orig"))
        mock_integrity_error.orig = Exception("users_email_key")
        mock_session.commit = AsyncMock(side_effect=mock_integrity_error)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await register_user(user_create, mock_request, Mock(), mock_session)

                assert exc_info.value.status_code == 400
                assert "Email already exists" in exc_info.value.detail
