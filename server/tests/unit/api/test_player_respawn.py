"""
Tests for Player Respawn API endpoints.

This module tests the player respawn API endpoints for handling player
resurrection after death and delirium recovery.
"""


# pylint: disable=redefined-outer-name
# Justification: pytest fixtures redefine names

from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.exceptions import LoggedHTTPException, ValidationError


@pytest.fixture
def player_respawn_module():
    """Lazily import player_respawn module."""
    from server.api import player_respawn

    return player_respawn


@pytest.fixture
def mock_current_user():
    """Mock authenticated user for testing."""
    user = Mock()
    user.id = uuid4()
    user.username = "testuser"
    return user


@pytest.fixture
def mock_request():
    """Mock FastAPI request object."""
    request = Mock()
    request.app = Mock()
    request.app.state = Mock()
    request.app.state.player_respawn_service = Mock()
    request.app.state.persistence = AsyncMock()
    return request


@pytest.fixture
def mock_player_service():
    """Mock PlayerService for testing."""
    service = Mock()
    service.respawn_player_from_delirium_by_user_id = AsyncMock()
    service.respawn_player_by_user_id = AsyncMock()
    return service


@pytest.fixture
def mock_async_session():
    """Mock async database session."""
    session = AsyncMock()
    session.__aenter__ = AsyncMock(return_value=session)
    session.__aexit__ = AsyncMock(return_value=None)
    return session


async def async_generator_mock(sessions):
    """Helper to create async generator from list of sessions."""
    for session in sessions:
        yield session


class TestRespawnPlayerFromDelirium:
    """Test respawn_player_from_delirium endpoint."""

    @pytest.mark.asyncio
    async def test_respawn_player_from_delirium_success(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test successful respawn from delirium."""
        expected_result = {
            "player": {"player_id": str(uuid4()), "lucidity": 10},
            "room": {"room_id": "sanitarium_room"},
        }
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(return_value=expected_result)

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            result = await player_respawn_module.respawn_player_from_delirium(
                request=mock_request, current_user=mock_current_user, player_service=mock_player_service
            )

            assert result == expected_result
            mock_player_service.respawn_player_from_delirium_by_user_id.assert_called_once()

    @pytest.mark.asyncio
    async def test_respawn_player_from_delirium_player_not_found(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn raises 404 when player not found."""
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(
            side_effect=ValidationError("Player not found")
        )

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player_from_delirium(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_respawn_player_from_delirium_not_delirious(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn raises 403 when player is not delirious."""
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(
            side_effect=ValidationError("Player must be delirious")
        )

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player_from_delirium(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 403
            assert "delirious" in str(exc_info.value.detail).lower()

    @pytest.mark.asyncio
    async def test_respawn_player_from_delirium_generic_error(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn handles generic ValidationError."""
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(
            side_effect=ValidationError("Generic validation error")
        )

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player_from_delirium(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_respawn_player_from_delirium_exception(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn handles unexpected exceptions."""
        mock_player_service.respawn_player_from_delirium_by_user_id = AsyncMock(side_effect=Exception("Unexpected error"))

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player_from_delirium(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 500


class TestRespawnPlayer:
    """Test respawn_player endpoint."""

    @pytest.mark.asyncio
    async def test_respawn_player_success(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test successful player respawn."""
        expected_result = {
            "player": {"player_id": str(uuid4()), "dp": 100},
            "room": {"room_id": "respawn_room"},
        }
        mock_player_service.respawn_player_by_user_id = AsyncMock(return_value=expected_result)

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            result = await player_respawn_module.respawn_player(
                request=mock_request, current_user=mock_current_user, player_service=mock_player_service
            )

            assert result == expected_result
            mock_player_service.respawn_player_by_user_id.assert_called_once()

    @pytest.mark.asyncio
    async def test_respawn_player_not_found(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn raises 404 when player not found."""
        mock_player_service.respawn_player_by_user_id = AsyncMock(side_effect=ValidationError("Player not found"))

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_respawn_player_not_dead(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn raises 403 when player is not dead."""
        mock_player_service.respawn_player_by_user_id = AsyncMock(side_effect=ValidationError("Player must be dead"))

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 403
            assert "dead" in str(exc_info.value.detail).lower()

    @pytest.mark.asyncio
    async def test_respawn_player_generic_validation_error(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn handles generic ValidationError."""
        mock_player_service.respawn_player_by_user_id = AsyncMock(side_effect=ValidationError("Generic error"))

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_respawn_player_exception(
        self, player_respawn_module, mock_current_user, mock_request, mock_player_service, mock_async_session
    ):
        """Test respawn handles unexpected exceptions."""
        mock_player_service.respawn_player_by_user_id = AsyncMock(side_effect=Exception("Unexpected error"))

        with patch("server.database.get_async_session") as mock_get_session:
            # get_async_session() returns an async generator, so we need to mock it properly
            async def mock_async_gen():
                yield mock_async_session
            mock_get_session.return_value = mock_async_gen()
            with pytest.raises(LoggedHTTPException) as exc_info:
                await player_respawn_module.respawn_player(
                    request=mock_request, current_user=mock_current_user, player_service=mock_player_service
                )

            assert exc_info.value.status_code == 500
