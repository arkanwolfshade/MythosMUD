"""Unit tests for authentication endpoints (registration)."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from sqlalchemy.exc import IntegrityError

from server.auth.endpoints import UserCreate, register_user
from server.exceptions import LoggedHTTPException
from server.models.user import User

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names match fixture names


@pytest.mark.asyncio
async def test_register_user_shutdown_pending(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration when server is shutting down."""
    user_create = UserCreate(
        username="testuser",
        password="testpass123",
    )

    mock_invite_manager = MagicMock()

    # Mock is_shutdown_pending to return True
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )

    assert exc_info.value.status_code == 503


@pytest.mark.asyncio
async def test_register_user_duplicate_username(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with duplicate username."""
    user_create = UserCreate(
        username="existing_user",
        password="testpass123",
    )

    # Mock existing user
    existing_user = User(
        id=str(uuid.uuid4()),
        username="existing_user",
        email="existing@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=existing_user)
    mock_session.execute = AsyncMock(return_value=result_mock)

    mock_invite_manager = MagicMock()

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )

    assert exc_info.value.status_code == 400
    assert "Username already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_integrity_error(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with IntegrityError."""
    user_create = UserCreate(
        username="testuser",
        password="testpass123",
    )

    # Mock IntegrityError
    integrity_error = IntegrityError("statement", "params", Exception("duplicate key value violates unique constraint"))
    integrity_error.orig = Exception("duplicate key value violates unique constraint")

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)
    add: MagicMock = MagicMock(side_effect=integrity_error)
    mock_session.add = add

    mock_invite_manager = MagicMock()

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                _ = await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )

    assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_register_user_success(mock_request: MagicMock, mock_session: MagicMock):
    """Test successful user registration."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    # Create mock invite manager with properly configured AsyncMock
    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    validate_invite_mock = AsyncMock(return_value=mock_invite)
    mock_invite_manager.validate_invite = validate_invite_mock

    # Mock session.execute to return None (no existing user)
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    execute_mock = AsyncMock(return_value=result_mock)
    mock_session.execute = execute_mock

    # Mock user creation - register_user creates User directly, not via UserManager
    new_user = User(
        id=str(uuid.uuid4()),
        username="newuser",
        email="newuser@wolfshade.org",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=False,
    )
    new_user.created_at = datetime.now(UTC).replace(tzinfo=None)
    new_user.updated_at = datetime.now(UTC).replace(tzinfo=None)
    refresh_mock = AsyncMock()
    mock_session.refresh = refresh_mock

    # Mock async_persistence with properly configured AsyncMocks
    mock_async_persistence = MagicMock()
    get_players_mock = AsyncMock(return_value=[])
    get_profession_mock = AsyncMock(return_value=None)
    mock_async_persistence.get_active_players_by_user_id = get_players_mock
    mock_async_persistence.get_profession_by_id = get_profession_mock

    # Ensure commit mock is properly configured
    commit_mock = AsyncMock()
    mock_session.commit = commit_mock

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                    # register_user creates User directly, so we need to mock session.add to set the user
                    def mock_add(_user: object) -> None:
                        # Simulate user being added and committed
                        # Parameter prefixed with _ to indicate intentionally unused
                        pass

                    mock_session.add = MagicMock(side_effect=mock_add)

                    response = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

                    # Verify async mocks were called (this ensures they're properly awaited)
                    validate_invite_mock.assert_awaited_once()
                    execute_mock.assert_awaited()
                    commit_mock.assert_awaited()
                    refresh_mock.assert_awaited()

                    assert response.access_token == "test_token"
                    assert isinstance(response.user_id, str)


@pytest.mark.asyncio
async def test_register_user_no_email(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration without email (should generate one)."""

    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code=None,
    )

    mock_invite_manager = MagicMock()

    # Mock session.execute to return None (no existing user)
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)

    mock_session.refresh = AsyncMock()

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                    mock_session.add = MagicMock()

                    response = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

                    # Should generate email
                    assert user_create.email == "newuser@wolfshade.org"
                    assert response.access_token == "test_token"


@pytest.mark.asyncio
async def test_register_user_invite_validation_failure(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration when invite validation fails."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="invalid_invite",
    )

    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(
        side_effect=LoggedHTTPException(
            status_code=400,
            detail="Invalid invite code",
            context=None,
        )
    )

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )

        assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_register_user_email_constraint_violation(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with email constraint violation."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
    )

    mock_invite_manager = MagicMock()

    # Mock IntegrityError with email constraint
    orig_exception = Exception("duplicate key value violates unique constraint users_email_key")
    integrity_error = IntegrityError("statement", "params", orig_exception)

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)
    add: MagicMock = MagicMock(side_effect=integrity_error)
    mock_session.add = add

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                _ = await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )

    assert exc_info.value.status_code == 400
    assert "Email already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_invite_marking_success(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with successful invite marking."""

    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(return_value=mock_invite)

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)

    # Mock session.execute to return result for user lookup, then success for invite update
    mock_execute_result = MagicMock()
    execute: AsyncMock = AsyncMock(
        side_effect=[
            result_mock,  # First call for user lookup
            mock_execute_result,  # Second call for invite update
        ]
    )
    mock_session.execute = execute

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                    mock_session.add = MagicMock()
                    mock_session.commit = AsyncMock()
                    mock_session.refresh = AsyncMock()

                    response = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

                    assert response.access_token == "test_token"
                    # Verify invite update was attempted
                    assert execute.call_count >= 2


@pytest.mark.asyncio
async def test_register_user_invite_marking_failure(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration when invite marking fails (should still succeed)."""

    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(return_value=mock_invite)

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)

    # Mock session.execute for invite update to raise error
    from sqlalchemy.exc import SQLAlchemyError

    mock_session.execute = AsyncMock(
        side_effect=[
            result_mock,  # First call for user lookup
            SQLAlchemyError("DB error", None, None),  # Second call for invite update
        ]
    )

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                    # Mock session.add and commit to succeed
                    mock_session.add = MagicMock()
                    mock_session.commit = AsyncMock()
                    mock_session.refresh = AsyncMock()

                    # Should still succeed even if invite marking fails
                    response = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

                    assert response.access_token == "test_token"


@pytest.mark.asyncio
async def test_register_user_unexpected_exception(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with unexpected exception."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
    )

    mock_invite_manager = MagicMock()

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)
    add: MagicMock = MagicMock(side_effect=RuntimeError("Unexpected error"))
    mock_session.add = add

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            # Should re-raise the exception
            with pytest.raises(RuntimeError, match="Unexpected error"):
                _ = await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )


@pytest.mark.asyncio
async def test_register_user_username_constraint_violation(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with username constraint violation."""
    user_create = UserCreate(
        username="existinguser",
        password="testpass123",
    )

    mock_invite_manager = MagicMock()

    # Mock IntegrityError with username constraint
    orig_exception = Exception("duplicate key value violates unique constraint users_username_key")
    integrity_error = IntegrityError("statement", "params", orig_exception)

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)
    add: MagicMock = MagicMock(side_effect=integrity_error)
    mock_session.add = add

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                _ = await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )

    assert exc_info.value.status_code == 400
    assert "Username already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_generic_constraint_violation(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with generic constraint violation."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
    )

    mock_invite_manager = MagicMock()

    # Mock IntegrityError with generic constraint
    orig_exception = Exception("duplicate key value violates unique constraint")
    integrity_error = IntegrityError("statement", "params", orig_exception)

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)
    add: MagicMock = MagicMock(side_effect=integrity_error)
    mock_session.add = add

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                _ = await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )

    assert exc_info.value.status_code == 400
    assert "already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_password_validation_empty():
    """Test registration with empty password (should be rejected by Pydantic)."""
    # This should be caught by Pydantic validation before reaching the endpoint
    from pydantic import ValidationError

    with pytest.raises(ValidationError):  # Pydantic validation error
        _ = UserCreate(
            username="newuser",
            password="",  # Empty password
        )


@pytest.mark.asyncio
async def test_register_user_password_validation_whitespace():
    """Test registration with whitespace-only password (should be rejected by Pydantic)."""
    # This should be caught by Pydantic validation before reaching the endpoint
    from pydantic import ValidationError

    with pytest.raises(ValidationError):  # Pydantic validation error
        _ = UserCreate(
            username="newuser",
            password="   ",  # Whitespace-only password
        )
