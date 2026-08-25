"""Unit tests for authentication endpoints (login)."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.auth.endpoints import LoginRequest, login_user
from server.exceptions import LoggedHTTPException
from server.models.user import User

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names match fixture names


@pytest.mark.asyncio
async def test_login_user_success(mock_request: MagicMock, mock_session: MagicMock):
    """Test successful user login."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    mock_user_manager = MagicMock()
    mock_user_manager.get_by_username = AsyncMock(return_value=user)

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])  # No characters
    mock_async_persistence.get_profession_by_id = AsyncMock(return_value=None)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth_utils.verify_password", return_value=True):
            with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                with patch(
                    "server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True
                ):
                    # Mock user_manager.authenticate to return the user
                    mock_user_manager.authenticate = AsyncMock(return_value=user)

                    # Mock container with async_persistence
                    mock_container = MagicMock()
                    mock_container.async_persistence = mock_async_persistence

                    response = await login_user(
                        request=login_request,
                        http_request=mock_request,
                        user_manager=mock_user_manager,
                        session=mock_session,
                        container=mock_container,
                    )

    assert response.access_token == "test_token"
    assert response.user_id == str(user.id)


@pytest.mark.asyncio
async def test_login_user_invalid_credentials(mock_request: MagicMock, mock_session: MagicMock):
    """Test login with invalid credentials."""
    login_request = LoginRequest(username="testuser", password="wrongpass")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=None)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_not_found(mock_request: MagicMock, mock_session: MagicMock):
    """Test login with non-existent user."""
    login_request = LoginRequest(username="nonexistent", password="testpass123")

    mock_user_manager = MagicMock()
    mock_user_manager.get_by_username = AsyncMock(return_value=None)

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_shutdown_pending(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when server is shutting down."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    mock_user_manager = MagicMock()

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 503


@pytest.mark.asyncio
async def test_login_user_no_email(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when user has no email."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email=None,  # No email
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_id_mismatch(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when authenticated user ID doesn't match."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    different_user = User(
        id=str(uuid.uuid4()),  # Different ID
        username="otheruser",
        email="other@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=different_user)  # Returns different user

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True):
            with pytest.raises(LoggedHTTPException) as exc_info:
                _ = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                    container=MagicMock(),
                )

            assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_generic_exception(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when a generic exception occurs."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(side_effect=RuntimeError("Unexpected error"))

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_with_characters(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when user has active characters."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=user)

    # Mock player with profession
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestCharacter"
    mock_player.profession_id = 1
    mock_player.level = 5
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)

    mock_profession = MagicMock()
    mock_profession.name = "Investigator"

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])
    mock_async_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence, create=True):
            with patch("server.auth.endpoints._generate_jwt_token", return_value="test_token"):
                # Mock container with async_persistence
                mock_container = MagicMock()
                mock_container.async_persistence = mock_async_persistence

                response = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                    container=mock_container,
                )

                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0].name == "TestCharacter"
                assert response.characters[0].profession_name == "Investigator"


@pytest.mark.asyncio
async def test_login_user_authenticate_returns_none(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when authenticate returns None."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=None)  # Returns None

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_authenticate_raises_exception(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when authenticate raises an exception."""
    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(side_effect=ValueError("Auth error"))

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_http_exception_re_raised(mock_request: MagicMock, mock_session: MagicMock):
    """Test login when HTTPException is raised (should be re-raised)."""
    from fastapi import HTTPException

    login_request = LoginRequest(username="testuser", password="testpass123")

    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )

    # Mock session.execute to return the user
    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(side_effect=HTTPException(status_code=400, detail="Bad request"))

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(HTTPException) as exc_info:
            _ = await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
                container=MagicMock(),
            )

        assert exc_info.value.status_code == 400
