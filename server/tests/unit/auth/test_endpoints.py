"""
Unit tests for authentication endpoints.
"""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import Request
from sqlalchemy.exc import IntegrityError

from server.auth.endpoints import LoginRequest, UserCreate, login_user, register_user
from server.exceptions import LoggedHTTPException
from server.models.user import User


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    app.state = MagicMock()
    request = MagicMock(spec=Request)
    request.app = app
    return request


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.execute = AsyncMock()
    session.add = MagicMock()
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    return session


@pytest.fixture
def mock_session():
    """Create a mock async session."""
    session = MagicMock()
    session.execute = AsyncMock()
    session.add = MagicMock()
    session.commit = AsyncMock()
    session.refresh = AsyncMock()
    return session


@pytest.mark.asyncio
async def test_register_user_shutdown_pending(mock_request, mock_session):
    """Test registration when server is shutting down."""
    user_create = UserCreate(
        username="testuser",
        password="testpass123",
    )

    mock_invite_manager = MagicMock()

    # Mock is_shutdown_pending to return True
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )

    assert exc_info.value.status_code == 503


@pytest.mark.asyncio
async def test_register_user_duplicate_username(mock_request, mock_session):
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
            await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )

    assert exc_info.value.status_code == 400
    assert "Username already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_integrity_error(mock_request, mock_session):
    """Test registration with IntegrityError."""
    user_create = UserCreate(
        username="testuser",
        password="testpass123",
    )

    # Mock IntegrityError
    integrity_error = IntegrityError("statement", "params", "orig")
    integrity_error.orig = Exception("duplicate key value violates unique constraint")

    from sqlalchemy.engine import Result

    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock
    mock_session.add.side_effect = integrity_error

    mock_invite_manager = MagicMock()

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )

    assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_login_user_success(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)

    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])  # No characters
    mock_async_persistence.get_profession_by_id = AsyncMock(return_value=None)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth_utils.verify_password", return_value=True):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                    # Mock user_manager.authenticate to return the user
                    mock_user_manager.authenticate = AsyncMock(return_value=user)

                    response = await login_user(
                        request=login_request,
                        http_request=mock_request,
                        user_manager=mock_user_manager,
                        session=mock_session,
                    )

    assert response.access_token == "test_token"
    assert response.user_id == str(user.id)


@pytest.mark.asyncio
async def test_login_user_invalid_credentials(mock_request, mock_session):
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

    mock_user_manager = MagicMock()
    mock_user_manager.get_by_username = AsyncMock(return_value=user)

    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth_utils.verify_password", return_value=False):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )

    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_not_found(mock_request, mock_session):
    """Test login with non-existent user."""
    login_request = LoginRequest(username="nonexistent", password="testpass123")
    
    mock_user_manager = MagicMock()
    mock_user_manager.get_by_username = AsyncMock(return_value=None)
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
    
    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_register_user_success(mock_request, mock_session):
    """Test successful user registration."""
    from datetime import datetime, UTC
    
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="valid_invite",
    )
    
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(return_value=MagicMock())
    
    # Mock session.execute to return None (no existing user)
    from sqlalchemy.engine import Result
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
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
    mock_session.refresh = AsyncMock()
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])
    mock_async_persistence.get_profession_by_id = AsyncMock(return_value=None)
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                    # register_user creates User directly, so we need to mock session.add to set the user
                    def mock_add(user):
                        # Simulate user being added and committed
                        pass
                    mock_session.add = MagicMock(side_effect=mock_add)
                    
                    response = await register_user(
                        user_create=user_create,
                        request=mock_request,
                        invite_manager=mock_invite_manager,
                        session=mock_session,
                    )
                    
                    assert response.access_token == "test_token"
                    assert isinstance(response.user_id, str)


@pytest.mark.asyncio
async def test_register_user_no_email(mock_request, mock_session):
    """Test registration without email (should generate one)."""
    from datetime import datetime, UTC
    
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
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
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
async def test_register_user_invite_validation_failure(mock_request, mock_session):
    """Test registration when invite validation fails."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
        invite_code="invalid_invite",
    )
    
    mock_invite_manager = MagicMock()
    mock_invite_manager.validate_invite = AsyncMock(side_effect=LoggedHTTPException(
        status_code=400,
        detail="Invalid invite code",
        context=None,
    ))
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await register_user(
                user_create=user_create,
                request=mock_request,
                invite_manager=mock_invite_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_login_user_shutdown_pending(mock_request, mock_session):
    """Test login when server is shutting down."""
    login_request = LoginRequest(username="testuser", password="testpass123")
    
    mock_user_manager = MagicMock()
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=True):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 503


@pytest.mark.asyncio
async def test_login_user_no_email(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_id_mismatch(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=different_user)  # Returns different user
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )
            
            assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_generic_exception(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(side_effect=RuntimeError("Unexpected error"))
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_with_characters(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
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
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                response = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )
                
                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0]["name"] == "TestCharacter"
                assert response.characters[0]["profession_name"] == "Investigator"


@pytest.mark.asyncio
async def test_login_user_profession_lookup_success(mock_request, mock_session):
    """Test login when profession lookup succeeds."""
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
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
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                response = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )
                
                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0]["name"] == "TestCharacter"
                assert response.characters[0]["profession_name"] == "Investigator"


@pytest.mark.asyncio
async def test_login_user_profession_lookup_error(mock_request, mock_session):
    """Test login when profession lookup fails."""
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=user)
    
    # Mock player with profession_id but profession lookup fails
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestCharacter"
    mock_player.profession_id = 1
    mock_player.level = 5
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])
    # Code catches SQLAlchemyError, so raise that instead of generic Exception
    from sqlalchemy.exc import SQLAlchemyError
    mock_async_persistence.get_profession_by_id = AsyncMock(side_effect=SQLAlchemyError("DB error", None, None))
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                response = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )
                
                # Should still succeed, just without profession name
                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0]["name"] == "TestCharacter"
                assert response.characters[0]["profession_name"] is None


@pytest.mark.asyncio
async def test_login_user_profession_lookup_none(mock_request, mock_session):
    """Test login when profession lookup returns None."""
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=user)
    
    # Mock player with profession_id but profession lookup returns None
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestCharacter"
    mock_player.profession_id = 1
    mock_player.level = 5
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])
    mock_async_persistence.get_profession_by_id = AsyncMock(return_value=None)
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                response = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )
                
                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0]["name"] == "TestCharacter"
                assert response.characters[0]["profession_name"] is None


@pytest.mark.asyncio
async def test_login_user_player_no_profession_id(mock_request, mock_session):
    """Test login when player has no profession_id."""
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=user)
    
    # Mock player without profession_id
    # CharacterInfo requires profession_id to be int, so we use 0 for None
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_player.name = "TestCharacter"
    mock_player.profession_id = 0  # Use 0 instead of None to match CharacterInfo schema
    mock_player.level = 5
    mock_player.created_at = datetime.now(UTC).replace(tzinfo=None)
    mock_player.last_active = datetime.now(UTC).replace(tzinfo=None)
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[mock_player])
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
            with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
                response = await login_user(
                    request=login_request,
                    http_request=mock_request,
                    user_manager=mock_user_manager,
                    session=mock_session,
                )
                
                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0]["name"] == "TestCharacter"
                assert response.characters[0]["profession_name"] is None


@pytest.mark.asyncio
async def test_get_current_user_info(mock_request, mock_session):
    """Test getting current user info."""
    from server.auth.endpoints import get_current_user_info
    
    user = User(
        id=str(uuid.uuid4()),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    
    response = await get_current_user_info(current_user=user)
    # Function returns a dict, not an object
    assert isinstance(response, dict)
    assert response["id"] == str(user.id)
    assert response["username"] == user.username
    assert response["email"] == user.email
    assert response["is_superuser"] == user.is_superuser


@pytest.mark.asyncio
async def test_list_invites(mock_request, mock_session):
    """Test listing invites."""
    from server.auth.endpoints import list_invites
    from datetime import datetime, UTC
    
    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    mock_invite.id = uuid.uuid4()
    mock_invite.invite_code = "test_invite"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    mock_invite_manager.list_invites = AsyncMock(return_value=[mock_invite])
    
    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    
    # _current_user is injected via Depends, so we pass it as a parameter
    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )
    
    assert len(response) == 1
    assert response[0]["invite_code"] == "test_invite"
    mock_invite_manager.list_invites.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_invite(mock_request, mock_session):
    """Test creating an invite."""
    from server.auth.endpoints import create_invite
    from datetime import datetime, UTC
    
    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    # InviteRead expects id as string
    invite_id = uuid.uuid4()
    mock_invite.id = str(invite_id)  # Must be string for InviteRead
    mock_invite.invite_code = "new_invite"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    mock_invite_manager.create_invite = AsyncMock(return_value=mock_invite)
    
    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    
    # _current_user is injected via Depends, so we pass it as a parameter
    response = await create_invite(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )
    
    # Function returns a dict (model_dump())
    assert isinstance(response, dict)
    assert response["invite_code"] == "new_invite"
    mock_invite_manager.create_invite.assert_awaited_once()


@pytest.mark.asyncio
async def test_register_user_email_constraint_violation(mock_request, mock_session):
    """Test registration with email constraint violation."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
    )
    
    mock_invite_manager = MagicMock()
    
    # Mock IntegrityError with email constraint
    integrity_error = IntegrityError("statement", "params", "orig")
    integrity_error.orig = Exception("duplicate key value violates unique constraint users_email_key")
    
    from sqlalchemy.engine import Result
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock
    mock_session.add.side_effect = integrity_error
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )
    
    assert exc_info.value.status_code == 400
    assert "Email already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_invite_marking_success(mock_request, mock_session):
    """Test registration with successful invite marking."""
    from datetime import datetime, UTC
    
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
    mock_session.execute = AsyncMock(side_effect=[
        result_mock,  # First call for user lookup
        mock_execute_result,  # Second call for invite update
    ])
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
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
                    assert mock_session.execute.call_count >= 2


@pytest.mark.asyncio
async def test_register_user_invite_marking_failure(mock_request, mock_session):
    """Test registration when invite marking fails (should still succeed)."""
    from datetime import datetime, UTC
    
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
    mock_session.execute = AsyncMock(side_effect=[
        result_mock,  # First call for user lookup
        SQLAlchemyError("DB error", None, None),  # Second call for invite update
    ])
    
    # Mock async_persistence
    mock_async_persistence = MagicMock()
    mock_async_persistence.get_active_players_by_user_id = AsyncMock(return_value=[])
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with patch("server.async_persistence.get_async_persistence", return_value=mock_async_persistence):
                with patch("fastapi_users.jwt.generate_jwt", return_value="test_token"):
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
async def test_register_user_unexpected_exception(mock_request, mock_session):
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
    mock_session.add.side_effect = RuntimeError("Unexpected error")
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            # Should re-raise the exception
            with pytest.raises(RuntimeError, match="Unexpected error"):
                await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )


@pytest.mark.asyncio
async def test_register_user_username_constraint_violation(mock_request, mock_session):
    """Test registration with username constraint violation."""
    user_create = UserCreate(
        username="existinguser",
        password="testpass123",
    )
    
    mock_invite_manager = MagicMock()
    
    # Mock IntegrityError with username constraint
    integrity_error = IntegrityError("statement", "params", "orig")
    integrity_error.orig = Exception("duplicate key value violates unique constraint users_username_key")
    
    from sqlalchemy.engine import Result
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock
    mock_session.add.side_effect = integrity_error
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )
    
    assert exc_info.value.status_code == 400
    assert "Username already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_generic_constraint_violation(mock_request, mock_session):
    """Test registration with generic constraint violation."""
    user_create = UserCreate(
        username="newuser",
        password="testpass123",
    )
    
    mock_invite_manager = MagicMock()
    
    # Mock IntegrityError with generic constraint
    integrity_error = IntegrityError("statement", "params", "orig")
    integrity_error.orig = Exception("duplicate key value violates unique constraint")
    
    from sqlalchemy.engine import Result
    result_mock = MagicMock(spec=Result)
    result_mock.scalar_one_or_none = MagicMock(return_value=None)
    mock_session.execute.return_value = result_mock
    mock_session.add.side_effect = integrity_error
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with patch("server.auth.argon2_utils.hash_password", return_value="hashed"):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await register_user(
                    user_create=user_create,
                    request=mock_request,
                    invite_manager=mock_invite_manager,
                    session=mock_session,
                )
    
    assert exc_info.value.status_code == 400
    assert "already exists" in exc_info.value.detail


@pytest.mark.asyncio
async def test_register_user_password_validation_empty(mock_request, mock_session):
    """Test registration with empty password (should be rejected by Pydantic)."""
    # This should be caught by Pydantic validation before reaching the endpoint
    with pytest.raises(Exception):  # Pydantic validation error
        UserCreate(
            username="newuser",
            password="",  # Empty password
        )


@pytest.mark.asyncio
async def test_register_user_password_validation_whitespace(mock_request, mock_session):
    """Test registration with whitespace-only password (should be rejected by Pydantic)."""
    # This should be caught by Pydantic validation before reaching the endpoint
    with pytest.raises(Exception):  # Pydantic validation error
        UserCreate(
            username="newuser",
            password="   ",  # Whitespace-only password
        )


@pytest.mark.asyncio
async def test_login_user_authenticate_returns_none(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(return_value=None)  # Returns None
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_authenticate_raises_exception(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(side_effect=ValueError("Auth error"))
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(LoggedHTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_login_user_http_exception_re_raised(mock_request, mock_session):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user)
    mock_session.execute = AsyncMock(return_value=result_mock)
    
    mock_user_manager = MagicMock()
    mock_user_manager.authenticate = AsyncMock(side_effect=HTTPException(status_code=400, detail="Bad request"))
    
    with patch("server.commands.admin_shutdown_command.is_shutdown_pending", return_value=False):
        with pytest.raises(HTTPException) as exc_info:
            await login_user(
                request=login_request,
                http_request=mock_request,
                user_manager=mock_user_manager,
                session=mock_session,
            )
        
        assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_list_invites_empty_list(mock_request, mock_session):
    """Test listing invites when list is empty."""
    from server.auth.endpoints import list_invites
    
    mock_invite_manager = MagicMock()
    mock_invite_manager.list_invites = AsyncMock(return_value=[])
    
    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    
    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )
    
    assert response == []
    mock_invite_manager.list_invites.assert_awaited_once()


@pytest.mark.asyncio
async def test_list_invites_with_used_invite(mock_request, mock_session):
    """Test listing invites with a used invite."""
    from server.auth.endpoints import list_invites
    from datetime import datetime, UTC
    
    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    mock_invite.id = uuid.uuid4()
    mock_invite.invite_code = "used_invite"
    mock_invite.is_active = False
    mock_invite.used_by_user_id = uuid.uuid4()
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    mock_invite_manager.list_invites = AsyncMock(return_value=[mock_invite])
    
    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    
    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )
    
    assert len(response) == 1
    assert response[0]["is_active"] is False
    assert response[0]["used_by_user_id"] is not None


@pytest.mark.asyncio
async def test_list_invites_with_expired_invite(mock_request, mock_session):
    """Test listing invites with an expired invite."""
    from server.auth.endpoints import list_invites
    from datetime import datetime, UTC, timedelta
    
    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    mock_invite.id = uuid.uuid4()
    mock_invite.invite_code = "expired_invite"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC) - timedelta(days=10)
    mock_invite.expires_at = datetime.now(UTC) - timedelta(days=1)  # Expired
    mock_invite_manager.list_invites = AsyncMock(return_value=[mock_invite])
    
    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    
    response = await list_invites(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )
    
    assert len(response) == 1
    assert response[0]["invite_code"] == "expired_invite"
    assert response[0]["expires_at"] is not None


@pytest.mark.asyncio
async def test_create_invite_success(mock_request, mock_session):
    """Test creating an invite successfully."""
    from server.auth.endpoints import create_invite
    from datetime import datetime, UTC
    
    mock_invite_manager = MagicMock()
    mock_invite = MagicMock()
    invite_id = uuid.uuid4()
    mock_invite.id = str(invite_id)
    mock_invite.invite_code = "new_invite_code"
    mock_invite.is_active = True
    mock_invite.used_by_user_id = None
    mock_invite.created_at = datetime.now(UTC)
    mock_invite.expires_at = datetime.now(UTC)
    mock_invite_manager.create_invite = AsyncMock(return_value=mock_invite)
    
    admin_user = User(
        id=str(uuid.uuid4()),
        username="admin",
        email="admin@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    
    response = await create_invite(
        _current_user=admin_user,
        invite_manager=mock_invite_manager,
    )
    
    assert isinstance(response, dict)
    assert response["invite_code"] == "new_invite_code"
    assert response["is_active"] is True
    mock_invite_manager.create_invite.assert_awaited_once()
