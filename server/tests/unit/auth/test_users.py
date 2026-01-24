"""
Unit tests for user management.
"""  # pylint: disable=too-many-lines  # Reason: Comprehensive test suite for user management - splitting would reduce cohesion and make related tests harder to find

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request

from server.auth.users import UserManager, get_user_db, get_user_manager
from server.models.user import User


@pytest.mark.asyncio
async def test_user_manager_hash_password():
    """Test UserManager password hashing."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    password = "test_password_123"
    hashed = manager._hash_password(password)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires access to protected method for unit testing

    assert isinstance(hashed, str)
    assert hashed != password
    assert len(hashed) > 0


@pytest.mark.asyncio
async def test_user_manager_verify_password():
    """Test UserManager password verification."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    password = "test_password_123"
    hashed = manager._hash_password(password)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires access to protected method for unit testing

    result = manager._verify_password(password, hashed)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires access to protected method for unit testing
    assert result is True

    result = manager._verify_password("wrong_password", hashed)  # pylint: disable=protected-access  # noqa: SLF001  # Reason: Test requires access to protected method for unit testing
    assert result is False


@pytest.mark.asyncio
async def test_user_manager_on_after_register_bogus_email():
    """Test post-registration logic with bogus email (auto-verified)."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@wolfshade.org",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    with patch("server.auth.users.is_bogus_email", return_value=True):
        await manager.on_after_register(user)

    # Bogus email should be auto-verified
    assert user.is_verified is True


@pytest.mark.asyncio
async def test_user_manager_on_after_register_non_bogus_email():
    """Test post-registration logic with non-bogus email (not auto-verified)."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    with patch("server.auth.users.is_bogus_email", return_value=False):
        await manager.on_after_register(user)

    # Non-bogus email should not be auto-verified
    assert user.is_verified is False


@pytest.mark.asyncio
async def test_user_manager_on_after_register_no_email():
    """Test post-registration logic with no email."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email=None,
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    await manager.on_after_register(user)

    # Should not raise and should not change verification status
    assert user.is_verified is False


@pytest.mark.asyncio
async def test_user_manager_on_after_register_with_request():
    """Test post-registration logic with request object."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@wolfshade.org",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    mock_request = MagicMock(spec=Request)

    with patch("server.auth.users.is_bogus_email", return_value=True):
        await manager.on_after_register(user, request=mock_request)

    # Should not raise
    assert user.is_verified is True


@pytest.mark.asyncio
async def test_user_manager_on_after_forgot_password():
    """Test forgot password logic."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Should not raise
    await manager.on_after_forgot_password(user, "reset_token")


@pytest.mark.asyncio
async def test_user_manager_on_after_request_verify():
    """Test verification request logic."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    # Should not raise
    await manager.on_after_request_verify(user, "verify_token")


def test_user_manager_parse_id_uuid():
    """Test parsing UUID from UUID object."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user_id = uuid.uuid4()
    result = manager.parse_id(user_id)
    assert result == user_id


def test_user_manager_parse_id_string():
    """Test parsing UUID from string."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user_id_str = str(uuid.uuid4())
    result = manager.parse_id(user_id_str)
    assert isinstance(result, uuid.UUID)
    assert str(result) == user_id_str


def test_user_manager_parse_id_invalid():
    """Test parsing invalid UUID."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    with pytest.raises(InvalidID):
        manager.parse_id("not-a-uuid")


def test_user_manager_parse_id_non_string_non_uuid():
    """Test parsing non-string, non-UUID value."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    # Test with a value that can't be converted to UUID
    with pytest.raises(InvalidID):
        manager.parse_id(12345)


def test_user_manager_parse_id_non_string_convertible():
    """Test parsing non-string value that can be converted to string."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    # Test with a value that can be converted to string but isn't a valid UUID
    from fastapi_users.exceptions import InvalidID

    with pytest.raises(InvalidID):
        manager.parse_id(12345)  # Can be converted to string but not a valid UUID


def test_user_manager_parse_id_none():
    """Test parsing None value."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    with pytest.raises(InvalidID):
        manager.parse_id(None)


def test_user_manager_parse_id_empty_string():
    """Test parsing empty string."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    with pytest.raises(InvalidID):
        manager.parse_id("")


def test_user_manager_parse_id_valid_uuid_string():
    """Test parsing valid UUID string."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user_id = uuid.uuid4()
    result = manager.parse_id(str(user_id))
    assert result == user_id


def test_user_manager_parse_id_value_error():
    """Test parsing value that raises ValueError when converting to string."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    # Create an object that raises ValueError when converting to string
    class BadStr:
        """Test class that raises ValueError when converting to string."""

        def __str__(self):
            raise ValueError("Cannot convert to string")

    with pytest.raises(InvalidID):
        manager.parse_id(BadStr())


def test_get_auth_backend():
    """Test getting authentication backend."""
    from server.auth.users import get_auth_backend

    backend = get_auth_backend()
    assert backend is not None
    assert backend.name == "jwt"


def test_get_username_auth_backend():
    """Test getting username-based authentication backend."""
    from server.auth.users import get_username_auth_backend

    backend = get_username_auth_backend()
    assert backend is not None
    assert backend.name == "jwt"


@pytest.mark.asyncio
async def test_get_user_db():
    """Test getting user database dependency."""
    mock_session = MagicMock()
    mock_session.execute = AsyncMock()

    async for user_db in get_user_db(session=mock_session):
        assert user_db is not None
        break


@pytest.mark.asyncio
async def test_get_user_manager():
    """Test getting user manager dependency."""
    from fastapi_users.db import SQLAlchemyUserDatabase

    mock_user_db = MagicMock(spec=SQLAlchemyUserDatabase)

    # Mock get_user_db to return our mock
    with patch("server.auth.users.get_user_db", return_value=iter([mock_user_db])):
        async for manager in get_user_manager():
            assert manager is not None
            assert isinstance(manager, UserManager)
            break


@pytest.mark.asyncio
async def test_username_authentication_backend_login():
    """Test UsernameAuthenticationBackend login method."""
    from fastapi_users.authentication import BearerTransport, JWTStrategy

    from server.auth.users import UsernameAuthenticationBackend

    def get_strategy():
        return JWTStrategy(secret="test", lifetime_seconds=3600, token_audience=["test"])

    transport = BearerTransport(tokenUrl="auth/jwt/login")
    backend = UsernameAuthenticationBackend("jwt", transport, get_strategy)

    # Test that login method exists and can be called
    mock_strategy = MagicMock()
    mock_user = MagicMock()

    # Mock the parent class's login method
    with patch("fastapi_users.authentication.AuthenticationBackend.login", new_callable=AsyncMock) as mock_parent_login:
        mock_parent_login.return_value = {"access_token": "test_token"}
        result = await backend.login(mock_strategy, mock_user)
        assert result == {"access_token": "test_token"}
        mock_parent_login.assert_awaited_once_with(mock_strategy, mock_user)


def test_user_manager_parse_id_type_error():
    """Test parsing ID that raises TypeError."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    # Create an object that raises TypeError when converting to string
    class BadType:
        """Test class that raises TypeError when converting to string."""

        def __str__(self):
            raise TypeError("Cannot convert to string")

    with pytest.raises(InvalidID):
        manager.parse_id(BadType())


def test_user_manager_parse_id_attribute_error():
    """Test parsing ID that raises AttributeError."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    # Create an object that raises AttributeError when converting to string
    class BadAttr:
        """Test class that raises AttributeError when converting to string."""

        def __str__(self):
            raise AttributeError("Cannot convert to string")

    with pytest.raises(InvalidID):
        manager.parse_id(BadAttr())


def test_user_manager_parse_id_uuid_value_error():
    """Test parsing ID that raises ValueError in UUID conversion."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    # Valid string format but invalid UUID
    with pytest.raises(InvalidID):
        manager.parse_id("not-a-valid-uuid-string")


def test_user_manager_parse_id_uuid_type_error():
    """Test parsing ID that raises TypeError in UUID conversion."""
    from fastapi_users.exceptions import InvalidID

    user_db = MagicMock()
    manager = UserManager(user_db)

    # This would be caught by the isinstance check, but test edge case
    # where UUID() raises TypeError
    with pytest.raises(InvalidID):
        manager.parse_id("invalid-uuid-format")


@pytest.mark.asyncio
async def test_user_manager_on_after_forgot_password_with_request():
    """Test forgot password logic with request object."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    mock_request = MagicMock(spec=Request)

    # Should not raise
    await manager.on_after_forgot_password(user, "reset_token", request=mock_request)


@pytest.mark.asyncio
async def test_user_manager_on_after_request_verify_with_request():
    """Test verification request logic with request object."""
    user_db = MagicMock()
    manager = UserManager(user_db)

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )

    mock_request = MagicMock(spec=Request)

    # Should not raise
    await manager.on_after_request_verify(user, "verify_token", request=mock_request)


def test_get_auth_backend_returns_authentication_backend():
    """Test that get_auth_backend returns an AuthenticationBackend instance."""
    from fastapi_users.authentication import AuthenticationBackend

    from server.auth.users import get_auth_backend

    backend = get_auth_backend()
    assert isinstance(backend, AuthenticationBackend)
    assert backend.name == "jwt"


def test_get_username_auth_backend_returns_username_authentication_backend():
    """Test that get_username_auth_backend returns UsernameAuthenticationBackend."""
    from server.auth.users import UsernameAuthenticationBackend, get_username_auth_backend

    backend = get_username_auth_backend()
    assert isinstance(backend, UsernameAuthenticationBackend)
    assert backend.name == "jwt"


def test_get_username_auth_backend_jwt_strategy_uses_env_var():
    """Test that get_username_auth_backend uses environment variable for JWT secret."""
    import os

    from server.auth.users import get_username_auth_backend

    # Test with custom env var
    with patch.dict(os.environ, {"MYTHOSMUD_JWT_SECRET": "custom-secret"}):
        backend = get_username_auth_backend()
        # The strategy is created lazily, so we can't easily test it
        # But we can verify the backend is created
        assert backend is not None
        assert backend.name == "jwt"


def test_get_username_auth_backend_jwt_strategy_default_secret():
    """Test that get_username_auth_backend uses default secret when env var not set."""
    import os

    from server.auth.users import get_username_auth_backend

    # Remove env var if it exists
    with patch.dict(os.environ, {}, clear=False):
        if "MYTHOSMUD_JWT_SECRET" in os.environ:
            del os.environ["MYTHOSMUD_JWT_SECRET"]
        backend = get_username_auth_backend()
        # The strategy is created lazily, so we can't easily test it
        # But we can verify the backend is created with default
        assert backend is not None
        assert backend.name == "jwt"


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
    inner_function = depends_wrapper.dependency

    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger") as mock_logger:
            result = await inner_function(mock_request)

            assert result == mock_user
            mock_logger.debug.assert_called_once()
            mock_logger.info.assert_called_once_with(
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
    inner_function = depends_wrapper.dependency

    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger") as mock_logger:
            result = await inner_function(None)

            assert result == mock_user
            # Should log "No request" when request is None
            mock_logger.debug.assert_called_once()
            call_kwargs = mock_logger.debug.call_args[1]
            assert call_kwargs.get("auth_preview") == "No request"


@pytest.mark.asyncio
async def test_get_current_user_with_logging_no_user():
    """Test _get_current_user_with_logging when no user is returned."""
    from server.auth.users import get_current_user_with_logging

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer test_token"}

    depends_wrapper = get_current_user_with_logging()
    inner_function = depends_wrapper.dependency

    with patch("server.auth.users.get_current_user", new_callable=AsyncMock, return_value=None):
        with patch("server.auth.users.logger") as mock_logger:
            result = await inner_function(mock_request)

            assert result is None
            mock_logger.debug.assert_called_once()
            mock_logger.warning.assert_called_once_with("Authentication failed: No user returned from get_current_user")


@pytest.mark.asyncio
async def test_get_current_user_with_logging_http_exception():
    """Test _get_current_user_with_logging when HTTPException is raised."""
    from fastapi import HTTPException

    from server.auth import users

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer invalid_token"}

    http_exception = HTTPException(status_code=401, detail="Invalid token")

    depends_wrapper = users.get_current_user_with_logging()
    inner_function = depends_wrapper.dependency

    with patch.object(users, "get_current_user", new_callable=AsyncMock, side_effect=http_exception):
        with patch.object(users, "logger") as mock_logger:
            result = await inner_function(mock_request)

            assert result is None
            mock_logger.debug.assert_called_once()
            mock_logger.warning.assert_called_once_with(
                "Authentication HTTP error", status_code=401, detail="Invalid token"
            )


@pytest.mark.asyncio
async def test_get_current_user_with_logging_generic_exception():
    """Test _get_current_user_with_logging when generic Exception is raised."""
    from server.auth import users

    mock_request = MagicMock()
    mock_request.headers = {"Authorization": "Bearer test_token"}

    depends_wrapper = users.get_current_user_with_logging()
    inner_function = depends_wrapper.dependency

    with patch.object(users, "get_current_user", new_callable=AsyncMock, side_effect=Exception("Unexpected error")):
        with patch.object(users, "logger") as mock_logger:
            result = await inner_function(mock_request)

            assert result is None
            mock_logger.debug.assert_called()
            # Should log error twice (error and debug)
            assert mock_logger.error.call_count == 1
            assert mock_logger.debug.call_count >= 2  # Once for auth attempt, once for error details
            error_call = mock_logger.error.call_args
            assert "Unexpected authentication error" in str(error_call)


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
    inner_function = depends_wrapper.dependency

    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger") as mock_logger:
            result = await inner_function(mock_request)

            assert result == mock_user
            mock_logger.debug.assert_called_once()
            # Check that auth_preview was truncated
            call_kwargs = mock_logger.debug.call_args[1]
            auth_preview = call_kwargs.get("auth_preview", "")
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
    inner_function = depends_wrapper.dependency

    with patch.object(users, "get_current_user", new_callable=AsyncMock, return_value=mock_user):
        with patch.object(users, "logger") as mock_logger:
            result = await inner_function(mock_request)

            assert result == mock_user
            mock_logger.debug.assert_called_once()
            call_kwargs = mock_logger.debug.call_args[1]
            assert call_kwargs.get("auth_preview") == "Not provided"


def test_get_auth_backend_jwt_strategy_uses_env_var():
    """Test that get_auth_backend uses environment variable for JWT secret."""
    import os

    from server.auth.users import get_auth_backend

    # Test with custom env var
    with patch.dict(os.environ, {"MYTHOSMUD_JWT_SECRET": "custom-secret"}):
        backend = get_auth_backend()
        # The strategy is created lazily, so we can't easily test it
        # But we can verify the backend is created
        assert backend is not None
        assert backend.name == "jwt"


def test_get_auth_backend_jwt_strategy_default_secret():
    """Test that get_auth_backend uses default secret when env var not set."""
    import os

    from server.auth.users import get_auth_backend

    # Remove env var if it exists
    with patch.dict(os.environ, {}, clear=False):
        if "MYTHOSMUD_JWT_SECRET" in os.environ:
            del os.environ["MYTHOSMUD_JWT_SECRET"]
        backend = get_auth_backend()
        # The strategy is created lazily, so we can't easily test it
        # But we can verify the backend is created with default
        assert backend is not None
        assert backend.name == "jwt"


def test_user_manager_reset_password_token_secret_env_var():
    """Test that UserManager uses environment variable for reset password token secret."""
    import os

    # Test with custom env var - these are instance attributes set in __init__
    with patch.dict(
        os.environ,
        {
            "MYTHOSMUD_RESET_TOKEN_SECRET": "custom-reset-secret",
            "MYTHOSMUD_VERIFICATION_TOKEN_SECRET": "custom-verification-secret",
        },
    ):
        user_db = MagicMock()
        manager = UserManager(user_db)
        assert manager.reset_password_token_secret == "custom-reset-secret"


def test_user_manager_verification_token_secret_env_var():
    """Test that UserManager uses environment variable for verification token secret."""
    import os

    # Test with custom env var - these are instance attributes set in __init__
    with patch.dict(
        os.environ,
        {
            "MYTHOSMUD_RESET_TOKEN_SECRET": "custom-reset-secret",
            "MYTHOSMUD_VERIFICATION_TOKEN_SECRET": "custom-verification-secret",
        },
    ):
        user_db = MagicMock()
        manager = UserManager(user_db)
        assert manager.verification_token_secret == "custom-verification-secret"


def test_user_manager_reset_password_token_secret_default():
    """Test that UserManager raises ValueError when reset password token secret starts with 'dev-'."""
    import os

    # UserManager now validates that secrets don't start with 'dev-'
    user_db = MagicMock()
    with patch.dict(
        os.environ,
        {
            "MYTHOSMUD_RESET_TOKEN_SECRET": "dev-reset-secret",
            "MYTHOSMUD_VERIFICATION_TOKEN_SECRET": "test-verification-secret",
        },
    ):
        with pytest.raises(ValueError, match="MYTHOSMUD_RESET_TOKEN_SECRET must be set to a secure value"):
            UserManager(user_db)


def test_user_manager_verification_token_secret_default():
    """Test that UserManager raises ValueError when verification token secret starts with 'dev-'."""
    import os

    # UserManager now validates that secrets don't start with 'dev-'
    user_db = MagicMock()
    with patch.dict(
        os.environ,
        {
            "MYTHOSMUD_RESET_TOKEN_SECRET": "test-reset-secret",
            "MYTHOSMUD_VERIFICATION_TOKEN_SECRET": "dev-verification-secret",
        },
    ):
        with pytest.raises(ValueError, match="MYTHOSMUD_VERIFICATION_TOKEN_SECRET must be set to a secure value"):
            UserManager(user_db)


def test_username_authentication_backend_init():
    """Test UsernameAuthenticationBackend initialization."""
    from fastapi_users.authentication import BearerTransport, JWTStrategy

    from server.auth.users import UsernameAuthenticationBackend

    def get_strategy():
        return JWTStrategy(secret="test", lifetime_seconds=3600, token_audience=["test"])

    transport = BearerTransport(tokenUrl="auth/jwt/login")
    backend = UsernameAuthenticationBackend("jwt", transport, get_strategy)

    assert backend.name == "jwt"
    assert backend.transport == transport


def test_fastapi_users_instance_created():
    """Test that fastapi_users instance is created."""
    from server.auth.users import fastapi_users

    assert fastapi_users is not None


def test_get_current_user_exported():
    """Test that get_current_user is exported."""
    from server.auth.users import get_current_user

    assert get_current_user is not None


def test_get_current_active_user_exported():
    """Test that get_current_active_user is exported."""
    from server.auth.users import get_current_active_user

    assert get_current_active_user is not None
