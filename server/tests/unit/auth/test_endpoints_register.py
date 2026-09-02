"""Unit tests for authentication endpoints (registration)."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from server.auth.endpoints import UserCreate, UserUpdate, register_user
from server.exceptions import LoggedHTTPException
from server.models.user import User

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names match fixture names


def test_user_create_rejects_unknown_field() -> None:
    """#755: UserCreate now inherits SecureBaseModel - extra fields must be rejected."""
    with pytest.raises(ValidationError):
        _ = UserCreate.model_validate(
            {
                "username": "testuser",
                "password": "testpass123",
                "invite_code": "valid_invite",
                "unexpected_field": "nope",
            }
        )


def test_user_update_rejects_unknown_field() -> None:
    """
    #755: UserUpdate now also inherits SecureBaseModel alongside fastapi_users'
    BaseUserUpdate - assert the multiple-inheritance model_config merge holds.
    """
    with pytest.raises(ValidationError):
        _ = UserUpdate.model_validate({"username": "newname", "unexpected_field": "nope"})


def _mock_invite_manager() -> MagicMock:
    """A MagicMock invite manager whose validate_invite awaits to a truthy invite."""
    manager = MagicMock()
    manager.validate_invite = AsyncMock(return_value=MagicMock())
    return manager


@pytest.mark.asyncio
async def test_register_user_shutdown_pending(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration when server is shutting down."""
    user_create = UserCreate(
        username="testuser",
        password="testpass123",
        invite_code="valid_invite",
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
        invite_code="valid_invite",
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

    mock_invite_manager = _mock_invite_manager()

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
        invite_code="valid_invite",
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

    mock_invite_manager = _mock_invite_manager()

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
    """Test successful user registration, including the atomic invite claim."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    validate_invite_mock = AsyncMock(return_value=mock_invite)
    mock_invite_manager.validate_invite = validate_invite_mock

    from sqlalchemy.engine import Result

    # execute() call order: reserve_invite (AUTH), username-existence lookup, capture_invite (CAPTURE).
    reserve_result = MagicMock(spec=Result)
    reserve_result.scalar_one = MagicMock(return_value=True)
    lookup_result = MagicMock(spec=Result)
    lookup_result.scalar_one_or_none = MagicMock(return_value=None)
    claim_result = MagicMock(spec=Result)
    claim_result.scalar_one = MagicMock(return_value=True)
    execute_mock = AsyncMock(side_effect=[reserve_result, lookup_result, claim_result])
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

    # Mock async_persistence with properly configured AsyncMocks
    mock_async_persistence = MagicMock()
    get_players_mock = AsyncMock(return_value=[])
    get_profession_mock = AsyncMock(return_value=None)
    mock_async_persistence.get_active_players_by_user_id = get_players_mock
    mock_async_persistence.get_profession_by_id = get_profession_mock

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch(
                "server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True
            ):
                with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                    # register_user creates User directly, so we need to mock session.add to set the user
                    def mock_add(_user: object) -> None:
                        # Simulate user being added (id populated by flush())
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
                    assert execute_mock.await_count == 3
                    mock_session.flush.assert_awaited_once()
                    mock_session.commit.assert_awaited()
                    mock_session.refresh.assert_awaited()

                    assert response.access_token == "test_token"
                    assert isinstance(response.user_id, str)


@pytest.mark.asyncio
async def test_register_user_no_email(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration without email (should generate one).

    Previously this test constructed invite_code=None and asserted success - it was live proof
    of #733's bypass. It now requires a valid invite code (the bypass itself is asserted against
    separately in test_register_user_invite_code_missing); its actual purpose, auto-generated
    email, is preserved below.
    """
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite_manager = _mock_invite_manager()

    from sqlalchemy.engine import Result

    reserve_result = MagicMock(spec=Result)
    reserve_result.scalar_one = MagicMock(return_value=True)
    lookup_result = MagicMock(spec=Result)
    lookup_result.scalar_one_or_none = MagicMock(return_value=None)
    claim_result = MagicMock(spec=Result)
    claim_result.scalar_one = MagicMock(return_value=True)
    mock_session.execute = AsyncMock(side_effect=[reserve_result, lookup_result, claim_result])

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch(
                "server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True
            ):
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
        invite_code="valid_invite",
    )

    mock_invite_manager = _mock_invite_manager()

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
async def test_register_user_invite_claim_success(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration where the invite claim (mark_invite_used) succeeds."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(return_value=mock_invite)

    from sqlalchemy.engine import Result

    reserve_result = MagicMock(spec=Result)
    reserve_result.scalar_one = MagicMock(return_value=True)
    lookup_result = MagicMock(spec=Result)
    lookup_result.scalar_one_or_none = MagicMock(return_value=None)
    claim_result = MagicMock(spec=Result)
    claim_result.scalar_one = MagicMock(return_value=True)
    execute = AsyncMock(side_effect=[reserve_result, lookup_result, claim_result])
    mock_session.execute = execute

    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch(
                "server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True
            ):
                with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                    mock_session.add = MagicMock()

                    response = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

                    assert response.access_token == "test_token"
                    # Verify the claim (mark_invite_used) was attempted
                    assert execute.call_count == 3
                    mock_session.commit.assert_awaited()


@pytest.mark.asyncio
async def test_register_user_capture_rejected_rolls_back(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration when capture_invite returns False after a successful reserve.

    Defense-in-depth path: with _reserve_invite's lock held, this should be unreachable in
    practice, but it must still reject (400) and not commit the user if the contract is ever
    violated, rather than silently succeeding.
    """
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(return_value=mock_invite)

    from sqlalchemy.engine import Result

    reserve_result = MagicMock(spec=Result)
    reserve_result.scalar_one = MagicMock(return_value=True)
    lookup_result = MagicMock(spec=Result)
    lookup_result.scalar_one_or_none = MagicMock(return_value=None)
    claim_result = MagicMock(spec=Result)
    claim_result.scalar_one = MagicMock(return_value=False)
    mock_session.execute = AsyncMock(side_effect=[reserve_result, lookup_result, claim_result])

    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch(
                "server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True
            ):
                mock_session.add = MagicMock()

                with pytest.raises(LoggedHTTPException) as exc_info:
                    _ = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

    assert exc_info.value.status_code == 400
    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_register_user_capture_error_rolls_back(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration when capture_invite itself errors (SQLAlchemyError).

    Fixes #733's swallowed-error bypass: previously this error was caught and logged, and
    registration succeeded anyway, leaving a committed user against an unclaimed invite. It
    must now propagate so the caller (get_async_session) rolls the user back.
    """
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite = MagicMock()
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(return_value=mock_invite)

    from sqlalchemy.engine import Result

    reserve_result = MagicMock(spec=Result)
    reserve_result.scalar_one = MagicMock(return_value=True)
    lookup_result = MagicMock(spec=Result)
    lookup_result.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(
        side_effect=[reserve_result, lookup_result, SQLAlchemyError("DB error", None, None)]
    )

    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch(
                "server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True
            ):
                mock_session.add = MagicMock()

                with pytest.raises(SQLAlchemyError):
                    _ = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )

    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_register_user_reserve_rejected(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration rejected when reserve_invite (AUTH) sees the code as unreservable.

    This is the authoritative concurrent-reuse guard: it must reject before any user object is
    built (no username lookup, no session.add) and must not commit.
    """
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="already_used",
    )

    mock_invite_manager = _mock_invite_manager()

    from sqlalchemy.engine import Result

    reserve_result = MagicMock(spec=Result)
    reserve_result.scalar_one = MagicMock(return_value=False)
    mock_session.execute = AsyncMock(return_value=reserve_result)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )

    assert exc_info.value.status_code == 400
    mock_session.execute.assert_awaited_once()  # reserve_invite only - no username lookup reached
    mock_session.commit.assert_not_awaited()


@pytest.mark.asyncio
async def test_register_user_unexpected_exception(mock_request: MagicMock, mock_session: MagicMock):
    """Test registration with unexpected exception."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )

    mock_invite_manager = _mock_invite_manager()

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
        invite_code="valid_invite",
    )

    mock_invite_manager = _mock_invite_manager()

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
        invite_code="valid_invite",
    )

    mock_invite_manager = _mock_invite_manager()

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
    with pytest.raises(ValidationError):  # Pydantic validation error
        _ = UserCreate(
            username="newuser",
            password="",  # Empty password
            invite_code="valid_invite",
        )


@pytest.mark.asyncio
async def test_register_user_password_validation_whitespace():
    """Test registration with whitespace-only password (should be rejected by Pydantic)."""
    # This should be caught by Pydantic validation before reaching the endpoint
    with pytest.raises(ValidationError):  # Pydantic validation error
        _ = UserCreate(
            username="newuser",
            password="   ",  # Whitespace-only password
            invite_code="valid_invite",
        )


@pytest.mark.asyncio
async def test_register_user_invite_code_missing():
    """Test registration with no invite_code at all is rejected by Pydantic (#733).

    This is the exact shape of #733: the field must be required, not optional-with-None-default,
    so a caller cannot omit it entirely and reach the handler. Uses model_validate() on a plain
    dict (mirroring FastAPI's parsing of an incoming JSON body) rather than a keyword UserCreate(...)
    call, since the latter is a field genuinely missing from the wire payload - a static
    "missing argument" call wouldn't compile against UserCreate's own generated __init__ and
    wouldn't reflect what an actual malicious/malformed request looks like.
    """
    with pytest.raises(ValidationError):
        _ = UserCreate.model_validate({"username": "newuser", "password": "testpass123"})


@pytest.mark.asyncio
async def test_register_user_invite_code_blank():
    """Test registration with a whitespace-only invite_code is rejected by Pydantic (#733)."""
    with pytest.raises(ValidationError):
        _ = UserCreate(
            username="newuser",
            password="testpass123",
            invite_code="   ",
        )
