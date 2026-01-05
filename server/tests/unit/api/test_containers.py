"""
Unit tests for container API endpoints.

Tests open, transfer, close, and loot-all container operations.
"""
# pylint: disable=redefined-outer-name
# Pytest fixtures are injected as function parameters, which triggers
# "redefined-outer-name" warnings. This is standard pytest pattern.

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request
from pydantic import ValidationError

from server.api.containers import (
    CloseContainerRequest,
    OpenContainerRequest,
    TransferContainerRequest,
    _create_error_context,
    _get_container_service,
    _get_player_id_from_user,
    close_container,
    open_container,
    transfer_items,
)
from server.exceptions import LoggedHTTPException, RateLimitError
from server.models.user import User
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
)


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    request = Mock(spec=Request)
    request.app = MagicMock()
    request.app.state = MagicMock()
    return request


@pytest.fixture
def mock_user():
    """Create a mock user."""
    user = User(
        id=uuid.uuid4(),
        username="testuser",
        email="test@example.com",
        hashed_password="hashed",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    return user


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


@pytest.fixture
def mock_container_service():
    """Create a mock container service."""
    service = MagicMock(spec=ContainerService)
    return service


class TestHelperFunctions:
    """Test helper functions."""

    def test_create_error_context(self, mock_request, mock_user):
        """Test _create_error_context() creates context."""
        context = _create_error_context(mock_request, mock_user, operation="test")
        assert context.user_id == str(mock_user.id)
        assert context.metadata["operation"] == "test"

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_success(self, mock_user, mock_persistence):
        """Test _get_player_id_from_user() returns player ID."""
        mock_player = MagicMock()
        mock_player.player_id = uuid.uuid4()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        result = await _get_player_id_from_user(mock_user, mock_persistence)
        assert result == mock_player.player_id

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_not_found(self, mock_user, mock_persistence):
        """Test _get_player_id_from_user() raises when player not found."""
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=None)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await _get_player_id_from_user(mock_user, mock_persistence)
        assert exc_info.value.status_code == 404

    def test_get_container_service_with_persistence(self, mock_persistence):
        """Test _get_container_service() with provided persistence."""
        service = _get_container_service(persistence=mock_persistence)
        assert isinstance(service, ContainerService)

    def test_get_container_service_from_request(self, mock_request, mock_persistence):
        """Test _get_container_service() gets persistence from request."""
        mock_request.app.state.persistence = mock_persistence
        service = _get_container_service(request=mock_request)
        assert isinstance(service, ContainerService)

    def test_get_container_service_raises_without_args(self):
        """Test _get_container_service() raises when neither persistence nor request provided."""
        with pytest.raises(ValueError, match="Either persistence or request must be provided"):
            _get_container_service()


class TestOpenContainer:
    """Test open_container() endpoint."""

    @pytest.mark.asyncio
    async def test_open_container_not_authenticated(self, mock_request):
        """Test open_container() requires authentication."""
        request_data = OpenContainerRequest(container_id=uuid.uuid4())
        with pytest.raises(LoggedHTTPException) as exc_info:
            await open_container(
                request_data=request_data,
                request=mock_request,
                current_user=None,
            )
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_open_container_rate_limit(self, mock_request, mock_user):
        """Test open_container() enforces rate limiting."""
        request_data = OpenContainerRequest(container_id=uuid.uuid4())
        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await open_container(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                )
            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_open_container_success(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test open_container() successfully opens container."""
        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()
        mock_result = {
            "container": {"container_id": str(container_id), "room_id": None},
            "mutation_token": "token123",
        }

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.open_container = AsyncMock(return_value=mock_result)
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                with patch("server.api.containers.emit_container_opened", new_callable=AsyncMock):
                    result = await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                    )
                    assert "container" in result
                    assert "mutation_token" in result

    @pytest.mark.asyncio
    async def test_open_container_not_found(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test open_container() handles ContainerNotFoundError."""
        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.open_container = AsyncMock(side_effect=ContainerNotFoundError("Not found"))
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                    )
                assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_open_container_locked(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test open_container() handles ContainerLockedError."""
        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.open_container = AsyncMock(side_effect=ContainerLockedError("Locked"))
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                    )
                assert exc_info.value.status_code == 423

    @pytest.mark.asyncio
    async def test_open_container_access_denied(
        self, mock_request, mock_user, mock_persistence, mock_container_service
    ):
        """Test open_container() handles ContainerAccessDeniedError."""
        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.open_container = AsyncMock(side_effect=ContainerAccessDeniedError("Access denied"))
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                    )
                assert exc_info.value.status_code == 403


class TestTransferItems:
    """Test transfer_items() endpoint."""

    @pytest.mark.asyncio
    async def test_transfer_items_not_authenticated(self, mock_request):
        """Test transfer_items() requires authentication."""
        request_data = TransferContainerRequest(
            container_id=uuid.uuid4(),
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        with pytest.raises(LoggedHTTPException) as exc_info:
            await transfer_items(
                request_data=request_data,
                request=mock_request,
                current_user=None,
            )
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_transfer_items_rate_limit(self, mock_request, mock_user):
        """Test transfer_items() enforces rate limiting."""
        request_data = TransferContainerRequest(
            container_id=uuid.uuid4(),
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await transfer_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                )
            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_transfer_items_to_container(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test transfer_items() transfers to container."""
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()
        mock_result = {"container": {}, "player_inventory": []}

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.transfer_to_container = AsyncMock(return_value=mock_result)
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                result = await transfer_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                )
                assert "container" in result
                mock_container_service.transfer_to_container.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_items_to_player(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test transfer_items() transfers to player."""
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_player",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()
        mock_result = {"container": {}, "player_inventory": []}

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.transfer_from_container = AsyncMock(return_value=mock_result)
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                result = await transfer_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                )
                assert "container" in result
                mock_container_service.transfer_from_container.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_items_capacity_error(
        self, mock_request, mock_user, mock_persistence, mock_container_service
    ):
        """Test transfer_items() handles ContainerCapacityError."""
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.transfer_to_container = AsyncMock(
            side_effect=ContainerCapacityError("Capacity exceeded")
        )
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await transfer_items(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                    )
                assert exc_info.value.status_code == 409

    @pytest.mark.asyncio
    async def test_transfer_items_stale_token(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test transfer_items() handles stale mutation token."""
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.transfer_to_container = AsyncMock(
            side_effect=ContainerServiceError("Stale mutation token")
        )
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await transfer_items(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                    )
                assert exc_info.value.status_code == 412


class TestCloseContainer:
    """Test close_container() endpoint."""

    @pytest.mark.asyncio
    async def test_close_container_not_authenticated(self, mock_request):
        """Test close_container() requires authentication."""
        request_data = CloseContainerRequest(container_id=uuid.uuid4(), mutation_token="token")
        with pytest.raises(LoggedHTTPException) as exc_info:
            await close_container(
                request_data=request_data,
                request=mock_request,
                current_user=None,
            )
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_close_container_rate_limit(self, mock_request, mock_user):
        """Test close_container() enforces rate limiting."""
        request_data = CloseContainerRequest(container_id=uuid.uuid4(), mutation_token="token")
        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await close_container(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                )
            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_close_container_success(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test close_container() successfully closes container."""
        container_id = uuid.uuid4()
        request_data = CloseContainerRequest(container_id=container_id, mutation_token="token")
        player_id = uuid.uuid4()

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=MagicMock(player_id=player_id))
        mock_container_service.close_container = AsyncMock()
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.containers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch("server.api.containers._get_container_service", return_value=mock_container_service):
                result = await close_container(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                )
                assert result["status"] == "closed"
                mock_container_service.close_container.assert_awaited_once()


class TestRequestModels:
    """Test request model validation."""

    def test_transfer_container_request_direction_validation(self):
        """Test TransferContainerRequest validates direction."""
        # Valid direction
        request = TransferContainerRequest(
            container_id=uuid.uuid4(),
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        assert request.direction == "to_container"

        # Invalid direction
        with pytest.raises(ValueError, match="direction must be"):
            TransferContainerRequest(
                container_id=uuid.uuid4(),
                mutation_token="token",
                direction="invalid",
                stack={"item_id": str(uuid.uuid4())},
                quantity=1,
            )

    def test_transfer_container_request_quantity_validation(self):
        """Test TransferContainerRequest validates quantity."""
        # Valid quantity
        request = TransferContainerRequest(
            container_id=uuid.uuid4(),
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=5,
        )
        assert request.quantity == 5

        # Invalid quantity (less than 1)
        with pytest.raises(ValidationError):  # Pydantic validation error
            TransferContainerRequest(
                container_id=uuid.uuid4(),
                mutation_token="token",
                direction="to_container",
                stack={"item_id": str(uuid.uuid4())},
                quantity=0,
            )
