"""Unit tests for login profession lookup paths."""

import uuid
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.auth.endpoints import LoginRequest, login_user
from server.models.user import User

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard for unit testing
# pylint: disable=redefined-outer-name  # Reason: pytest fixture parameter names match fixture names


@pytest.mark.asyncio
async def test_login_user_profession_lookup_success(mock_request: MagicMock, mock_session: MagicMock):
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
async def test_login_user_profession_lookup_error(mock_request: MagicMock, mock_session: MagicMock):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

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

                # Should still succeed, just without profession name
                assert response.access_token == "test_token"
                assert len(response.characters) == 1
                assert response.characters[0].name == "TestCharacter"
                assert response.characters[0].profession_name is None


@pytest.mark.asyncio
async def test_login_user_profession_lookup_none(mock_request: MagicMock, mock_session: MagicMock):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

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
                assert response.characters[0].profession_name is None


@pytest.mark.asyncio
async def test_login_user_player_no_profession_id(mock_request: MagicMock, mock_session: MagicMock):
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
    result_mock.scalar_one_or_none = MagicMock(return_value=user.id)
    mock_session.execute = AsyncMock(return_value=result_mock)
    # _find_user_by_username (#633) resolves the id via SQL, then fetches the mapped entity.
    mock_session.get = AsyncMock(return_value=user)

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
                assert response.characters[0].profession_name is None
