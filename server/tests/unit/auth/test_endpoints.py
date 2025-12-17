"""
Tests for authentication endpoints.

This module tests the registration, login, and authentication endpoints.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from server.auth.endpoints import (
    LoginRequest,
    LoginResponse,
    UserCreate,
    create_invite,
    get_current_user_info,
    list_invites,
    login_user,
    register_user,
)
from server.exceptions import LoggedHTTPException
from server.models.user import User


class TestUserCreate:
    """Test UserCreate schema."""

    def test_user_create_valid(self):
        """Test UserCreate with valid data."""
        user_create = UserCreate(username="testuser", password="password123", email="test@example.com")
        assert user_create.username == "testuser"
        assert user_create.password == "password123"
        assert user_create.email == "test@example.com"

    def test_user_create_password_empty(self):
        """Test UserCreate rejects empty password."""
        with pytest.raises(ValueError, match="Password cannot be empty"):
            UserCreate(username="testuser", password="", email="test@example.com")

    def test_user_create_password_whitespace_only(self):
        """Test UserCreate rejects whitespace-only password."""
        with pytest.raises(ValueError, match="Password cannot be empty"):
            UserCreate(username="testuser", password="   ", email="test@example.com")


class TestLoginRequest:
    """Test LoginRequest schema."""

    def test_login_request_valid(self):
        """Test LoginRequest with valid data."""
        login_req = LoginRequest(username="testuser", password="password123")
        assert login_req.username == "testuser"
        assert login_req.password == "password123"


class TestRegisterUser:
    """Test register_user endpoint."""

    @pytest.mark.asyncio
    async def test_register_user_success(self):
        """Test successful user registration."""
        user_create = UserCreate(username="newuser", password="password123", email="test@example.com")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)
        mock_session.commit = AsyncMock()
        mock_session.refresh = AsyncMock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "newuser"

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed_password"):
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                    with patch("server.auth.endpoints.User", return_value=mock_user):
                        with patch("server.auth.endpoints.logger.info") as mock_info:
                            with patch("server.auth.endpoints.logger.debug") as mock_debug:
                                result = await register_user(user_create, mock_request, Mock(), Mock(), mock_session)

                                assert isinstance(result, LoginResponse)
                                assert result.access_token == "test_token"
                                assert result.has_character is False
                                # Should log successful registration
                                assert any(
                                    "User registered successfully" in str(call) for call in mock_info.call_args_list
                                )
                                assert any("Registration successful" in str(call) for call in mock_info.call_args_list)
                                # Should log JWT debug messages
                                assert any("JWT token generated" in str(call) for call in mock_debug.call_args_list)

    @pytest.mark.asyncio
    async def test_register_user_with_invite_success(self):
        """Test register_user successfully marks invite as used."""
        user_create = UserCreate(
            username="newuser", password="password123", email="test@example.com", invite_code="INVITE-123"
        )
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_invite = Mock()
        mock_invite_manager = Mock()
        mock_invite_manager.validate_invite = AsyncMock(return_value=mock_invite)

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)
        mock_session.execute = AsyncMock(return_value=mock_result)
        mock_session.commit = AsyncMock()
        mock_session.refresh = AsyncMock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "newuser"

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed_password"):
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                    with patch("server.auth.endpoints.User", return_value=mock_user):
                        with patch("server.auth.endpoints.logger.info") as mock_info:
                            result = await register_user(
                                user_create, mock_request, mock_invite_manager, Mock(), mock_session
                            )

                            assert isinstance(result, LoginResponse)
                            # Should log invite marking success
                            assert any("Invite marked as used" in str(call) for call in mock_info.call_args_list)

    @pytest.mark.asyncio
    async def test_register_user_shutdown_pending(self):
        """Test register_user raises exception when server is shutting down."""
        user_create = UserCreate(username="newuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
            with patch(
                "server.commands.admin_shutdown_command.get_shutdown_blocking_message",
                return_value="Server shutting down",
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await register_user(user_create, mock_request, Mock(), Mock(), Mock())

                assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_register_user_username_exists(self):
        """Test register_user raises exception when username already exists."""
        user_create = UserCreate(username="existinguser", password="password123", email="existing@example.com")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_existing_user = Mock(spec=User)
        mock_result = Mock()
        mock_result.scalar_one_or_none = AsyncMock(return_value=mock_existing_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await register_user(user_create, mock_request, Mock(), Mock(), mock_session)

                assert exc_info.value.status_code == 400
                assert "Username already exists" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_register_user_generates_email(self):
        """Test register_user generates email when not provided."""
        user_create = UserCreate(username="newuser", password="password123", email="")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)
        mock_session.commit = AsyncMock()
        mock_session.refresh = AsyncMock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "newuser"

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed_password"):
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                    with patch("server.auth.endpoints.User", return_value=mock_user):
                        with patch("server.auth.endpoints.logger.info") as mock_info:
                            result = await register_user(user_create, mock_request, Mock(), Mock(), mock_session)

                            assert isinstance(result, LoginResponse)
                            # Should log email generation
                            assert any("Generated simple bogus email" in str(call) for call in mock_info.call_args_list)

    @pytest.mark.asyncio
    async def test_register_user_integrity_error_username(self):
        """Test register_user handles IntegrityError for duplicate username."""
        user_create = UserCreate(username="duplicateuser", password="password123", email="dup@example.com")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)
        mock_session.commit = AsyncMock(side_effect=IntegrityError("statement", "params", "orig"))
        mock_session.commit.side_effect.orig = Exception("users_username_key")

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed_password"):
                with patch("server.auth.endpoints.User", return_value=Mock()):
                    with pytest.raises(LoggedHTTPException) as exc_info:
                        await register_user(user_create, mock_request, Mock(), Mock(), mock_session)

                        assert exc_info.value.status_code == 400
                        assert "Username already exists" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_register_user_integrity_error_email(self):
        """Test register_user handles IntegrityError for duplicate email."""
        user_create = UserCreate(username="newuser", password="password123", email="duplicate@example.com")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)
        mock_integrity_error = IntegrityError("statement", "params", "orig")
        mock_integrity_error.orig = Exception("users_email_key")
        mock_session.commit = AsyncMock(side_effect=mock_integrity_error)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("server.auth.argon2_utils.hash_password", return_value="hashed_password"):
                with patch("server.auth.endpoints.User", return_value=Mock()):
                    with pytest.raises(LoggedHTTPException) as exc_info:
                        await register_user(user_create, mock_request, Mock(), Mock(), mock_session)

                        assert exc_info.value.status_code == 400
                        assert "Email already exists" in exc_info.value.detail


class TestLoginUser:
    """Test login_user endpoint."""

    @pytest.mark.asyncio
    async def test_login_user_success(self):
        """Test successful user login."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_user)

        mock_persistence = Mock()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=None)
        mock_request.app.state.container.persistence = mock_persistence

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_persistence):
                    result = await login_user(login_req, mock_request, mock_user_manager, mock_session)

                    assert isinstance(result, LoginResponse)
                    assert result.access_token == "test_token"
                    assert result.user_id == str(mock_user.id)
                    assert result.has_character is False

    @pytest.mark.asyncio
    async def test_login_user_shutdown_pending(self):
        """Test login_user raises exception when server is shutting down."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
            with patch(
                "server.commands.admin_shutdown_command.get_shutdown_blocking_message",
                return_value="Server shutting down",
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await login_user(login_req, mock_request, Mock(), Mock())

                    assert exc_info.value.status_code == 503

    @pytest.mark.asyncio
    async def test_login_user_not_found(self):
        """Test login_user raises exception when user not found."""
        login_req = LoginRequest(username="nonexistent", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=None)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await login_user(login_req, mock_request, Mock(), mock_session)

                assert exc_info.value.status_code == 401
                assert "Invalid credentials" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_login_user_no_email(self):
        """Test login_user raises exception when user has no email."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = None

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await login_user(login_req, mock_request, Mock(), mock_session)

                assert exc_info.value.status_code == 401
                assert "Invalid credentials" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_login_user_authentication_failed(self):
        """Test login_user raises exception when authentication fails."""
        login_req = LoginRequest(username="testuser", password="wrongpassword")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=None)  # Authentication failed

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            mock_context = Mock()
            mock_context.metadata = {}
            with patch("server.auth.endpoints.create_context_from_request", return_value=mock_context):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await login_user(login_req, mock_request, mock_user_manager, mock_session)

                    assert exc_info.value.status_code == 401
                    assert "Invalid credentials" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_login_user_generic_exception(self):
        """Test login_user handles generic exceptions during authentication."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(side_effect=ValueError("Unexpected error"))

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            mock_context = Mock()
            mock_context.metadata = {}
            with patch("server.auth.endpoints.create_context_from_request", return_value=mock_context):
                with patch("server.auth.endpoints.logger.error") as mock_error:
                    with pytest.raises(LoggedHTTPException) as exc_info:
                        await login_user(login_req, mock_request, mock_user_manager, mock_session)

                        assert exc_info.value.status_code == 401
                        assert "Invalid credentials" in exc_info.value.detail
                        mock_error.assert_called_once()

    @pytest.mark.asyncio
    async def test_login_user_session_management_success(self):
        """Test login_user handles session management when user has character."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.container = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_user)

        mock_player = Mock()
        mock_player.name = "TestCharacter"
        mock_player.player_id = uuid.uuid4()

        mock_persistence = Mock()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        mock_connection_manager = Mock()
        mock_connection_manager.handle_new_game_session = AsyncMock(
            return_value={"success": True, "connections_disconnected": 2}
        )
        mock_request.app.state.container.connection_manager = mock_connection_manager
        mock_request.app.state.container.persistence = mock_persistence

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_persistence):
                    with patch("server.auth.endpoints.logger.info") as mock_info:
                        result = await login_user(login_req, mock_request, mock_user_manager, mock_session)

                        assert isinstance(result, LoginResponse)
                        assert result.has_character is True
                        # Should log session management success
                        assert any(
                            "Disconnected existing connections" in str(call) for call in mock_info.call_args_list
                        )

    @pytest.mark.asyncio
    async def test_login_user_session_management_failure(self):
        """Test login_user handles session management failure."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.container = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_user)

        mock_player = Mock()
        mock_player.name = "TestCharacter"
        mock_player.player_id = uuid.uuid4()

        mock_persistence = Mock()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        mock_connection_manager = Mock()
        mock_connection_manager.handle_new_game_session = AsyncMock(
            return_value={"success": False, "errors": ["Connection error"]}
        )
        mock_request.app.state.container.connection_manager = mock_connection_manager
        mock_request.app.state.container.persistence = mock_persistence

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_persistence):
                    with patch("server.auth.endpoints.logger.warning") as mock_warning:
                        result = await login_user(login_req, mock_request, mock_user_manager, mock_session)

                        assert isinstance(result, LoginResponse)
                        assert result.has_character is True
                        # Should log session management failure
                        mock_warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_login_user_id_mismatch(self):
        """Test login_user raises exception when user ID mismatch."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_authenticated_user = Mock(spec=User)
        mock_authenticated_user.id = uuid.uuid4()  # Different ID

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_authenticated_user)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await login_user(login_req, mock_request, mock_user_manager, mock_session)

                assert exc_info.value.status_code == 401
                assert "Invalid credentials" in exc_info.value.detail

    @pytest.mark.asyncio
    async def test_login_user_with_character(self):
        """Test login_user returns has_character=True when player exists."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()
        mock_request.app.state.container = Mock()
        mock_request.app.state.container.connection_manager = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)  # scalar_one_or_none is synchronous
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_user)

        mock_player = Mock()
        mock_player.name = "TestCharacter"
        mock_player.player_id = uuid.uuid4()

        mock_persistence = Mock()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_request.app.state.container.persistence = mock_persistence

        mock_connection_manager = Mock()
        mock_connection_manager.handle_new_game_session = AsyncMock(
            return_value={"success": True, "connections_disconnected": 0}
        )
        mock_request.app.state.container.connection_manager = mock_connection_manager

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_persistence):
                    with patch("server.auth.endpoints.logger.info") as mock_info:
                        result = await login_user(login_req, mock_request, mock_user_manager, mock_session)

                        assert isinstance(result, LoginResponse)
                        assert result.has_character is True
                        assert result.character_name == "TestCharacter"
                        # Should log login successful
                        assert any("Login successful" in str(call) for call in mock_info.call_args_list)

    @pytest.mark.asyncio
    async def test_login_user_without_character(self):
        """Test login_user returns has_character=False when player doesn't exist."""
        login_req = LoginRequest(username="testuser", password="password123")
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = Mock()

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.username = "testuser"
        mock_user.email = "testuser@example.com"

        mock_session = AsyncMock(spec=AsyncSession)
        mock_result = Mock()
        mock_result.scalar_one_or_none = Mock(return_value=mock_user)
        mock_session.execute = AsyncMock(return_value=mock_result)

        mock_user_manager = Mock()
        mock_user_manager.authenticate = AsyncMock(return_value=mock_user)

        mock_persistence = Mock()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=None)

        with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_persistence):
                    with patch("server.auth.endpoints.logger.info") as mock_info:
                        result = await login_user(login_req, mock_request, mock_user_manager, mock_session)

                        assert isinstance(result, LoginResponse)
                        assert result.has_character is False
                        assert result.character_name is None
                        # Should log login successful
                        assert any("Login successful" in str(call) for call in mock_info.call_args_list)


class TestGetCurrentUserInfo:
    """Test get_current_user_info endpoint."""

    @pytest.mark.asyncio
    async def test_get_current_user_info_success(self):
        """Test get_current_user_info returns user information."""

        mock_user = Mock(spec=User)
        mock_user.id = uuid.uuid4()
        mock_user.email = "test@example.com"
        mock_user.username = "testuser"
        mock_user.is_superuser = False

        result = await get_current_user_info(current_user=mock_user)

        assert result["id"] == str(mock_user.id)
        assert result["email"] == "test@example.com"
        assert result["username"] == "testuser"
        assert result["is_superuser"] is False


class TestListInvites:
    """Test list_invites endpoint."""

    @pytest.mark.asyncio
    async def test_list_invites_success(self):
        """Test list_invites returns list of invites."""

        mock_user = Mock(spec=User)
        mock_user.is_superuser = True

        mock_invite1 = Mock()
        mock_invite1.id = str(uuid.uuid4())  # InviteRead expects string ID
        mock_invite1.invite_code = "INVITE-123"
        mock_invite1.is_active = True
        mock_invite1.used_by_user_id = None
        mock_invite1.expires_at = None
        mock_invite1.created_at = datetime.now(UTC).replace(tzinfo=None)

        mock_invite2 = Mock()
        mock_invite2.id = str(uuid.uuid4())  # InviteRead expects string ID
        mock_invite2.invite_code = "INVITE-456"
        mock_invite2.is_active = False
        mock_invite2.used_by_user_id = str(uuid.uuid4())
        mock_invite2.expires_at = datetime.now(UTC).replace(tzinfo=None)
        mock_invite2.created_at = datetime.now(UTC).replace(tzinfo=None)

        mock_invite_manager = Mock()
        mock_invite_manager.list_invites = AsyncMock(return_value=[mock_invite1, mock_invite2])

        result = await list_invites(current_user=mock_user, invite_manager=mock_invite_manager)

        assert len(result) == 2
        assert result[0]["invite_code"] == "INVITE-123"
        assert result[1]["invite_code"] == "INVITE-456"


class TestCreateInvite:
    """Test create_invite endpoint."""

    @pytest.mark.asyncio
    async def test_create_invite_success(self):
        """Test create_invite creates and returns invite."""

        mock_user = Mock(spec=User)
        mock_user.is_superuser = True

        mock_invite = Mock()
        mock_invite.id = str(uuid.uuid4())  # InviteRead expects string ID
        mock_invite.invite_code = "NEW-INVITE"
        mock_invite.is_active = True
        mock_invite.used_by_user_id = None
        mock_invite.expires_at = None
        mock_invite.created_at = datetime.now(UTC).replace(tzinfo=None)

        mock_invite_manager = Mock()
        mock_invite_manager.create_invite = AsyncMock(return_value=mock_invite)

        result = await create_invite(current_user=mock_user, invite_manager=mock_invite_manager)

        assert result["invite_code"] == "NEW-INVITE"
        assert result["is_active"] is True
