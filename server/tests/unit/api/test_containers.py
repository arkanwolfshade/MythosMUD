"""
Unit tests for container API endpoints.

Tests open, transfer, close, and loot-all container operations.
"""
# pylint: disable=redefined-outer-name  # Reason: Pytest fixtures are injected as function parameters, which pylint incorrectly flags as redefining names from outer scope, this is standard pytest usage
# Pytest fixtures are injected as function parameters, which triggers
# "redefined-outer-name" warnings. This is standard pytest pattern.
# pylint: disable=too-many-lines  # Reason: Test file exceeds 550 lines but contains comprehensive test coverage for container API, splitting would reduce cohesion

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request
from pydantic import ValidationError

# Lazy imports to avoid circular import issues
# Import inside functions that need them to avoid triggering circular import chain
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
        """Test create_error_context() creates context."""
        # Lazy import to avoid circular import
        from server.api.container_helpers import (
            create_error_context,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        context = create_error_context(mock_request, mock_user, operation="test")
        assert context["user_id"] == str(mock_user.id)
        assert context["operation"] == "test"

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_success(self, mock_user, mock_persistence):
        """Test get_player_id_from_user() returns player ID."""
        # Lazy import to avoid circular import
        from server.api.container_helpers import (
            get_player_id_from_user,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        mock_player = MagicMock()
        mock_player.player_id = uuid.uuid4()
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)

        result = await get_player_id_from_user(mock_user, mock_persistence)
        assert result == mock_player.player_id

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_not_found(self, mock_user, mock_persistence):
        """Test get_player_id_from_user() raises when player not found."""
        # Lazy import to avoid circular import
        from server.api.container_helpers import (
            get_player_id_from_user,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        mock_persistence.get_player_by_user_id = AsyncMock(return_value=None)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_player_id_from_user(mock_user, mock_persistence)
        assert exc_info.value.status_code == 404

    def test_get_container_service_with_persistence(self, mock_persistence):
        """Test get_container_service() with provided persistence."""
        # Lazy import to avoid circular import
        from server.api.container_helpers import (
            get_container_service,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        service = get_container_service(persistence=mock_persistence)
        assert isinstance(service, ContainerService)

    def test_get_container_service_from_request(self, mock_request, mock_persistence):
        """Test get_container_service() gets persistence from request."""
        # Lazy import to avoid circular import
        from server.api.container_helpers import (
            get_container_service,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        # Function now requires persistence parameter directly
        service = get_container_service(persistence=mock_persistence)
        assert isinstance(service, ContainerService)

    def test_get_container_service_raises_without_args(self):
        """Test get_container_service() raises when persistence not provided."""
        # Lazy import to avoid circular import
        from server.api.container_helpers import (
            get_container_service,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        with pytest.raises(TypeError, match="missing 1 required positional argument"):
            # Reason: Intentionally calling without required argument to test error handling
            get_container_service()  # type: ignore[call-arg]


class TestOpenContainer:
    """Test open_container() endpoint."""

    @pytest.mark.asyncio
    async def test_open_container_not_authenticated(self, mock_request):
        """Test open_container() requires authentication."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import open_container  # noqa: E402
        from server.api.container_models import (
            OpenContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = OpenContainerRequest(container_id=uuid.uuid4())
        with pytest.raises(LoggedHTTPException) as exc_info:
            await open_container(
                request_data=request_data,
                request=mock_request,
                # Reason: Intentionally passing None to test unauthenticated scenario
                current_user=None,  # type: ignore[arg-type]
                persistence=AsyncMock(),
                connection_manager=MagicMock(),
            )
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_open_container_rate_limit(self, mock_request, mock_user):
        """Test open_container() enforces rate limiting."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import open_container  # noqa: E402
        from server.api.container_models import (
            OpenContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = OpenContainerRequest(container_id=uuid.uuid4())
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await open_container(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=AsyncMock(),
                    connection_manager=MagicMock(),
                )
            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_open_container_success(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test open_container() successfully opens container."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import open_container  # noqa: E402
        from server.api.container_models import (
            OpenContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()
        mock_result = {
            "container": {"container_id": str(container_id), "room_id": None},
            "mutation_token": "token123",
        }

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_persistence.get_container = AsyncMock(
            return_value={"container_id": str(container_id), "room_id": None, "items": []}
        )
        mock_persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
        mock_container_service.open_container = AsyncMock(return_value=mock_result)
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            # Patch where it's imported and used
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with patch(
                    "server.api.container_endpoints_basic.emit_container_opened_events", new_callable=AsyncMock
                ) as mock_emit:
                    mock_emit.return_value = None
                    result = await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                    assert result.container is not None
                    assert result.mutation_token is not None

    @pytest.mark.asyncio
    async def test_open_container_not_found(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test open_container() handles ContainerNotFoundError."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import open_container  # noqa: E402
        from server.api.container_models import (
            OpenContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_persistence.get_container = AsyncMock(return_value=None)
        mock_container_service.open_container = AsyncMock(side_effect=ContainerNotFoundError("Not found"))
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            # Patch where it's imported and used
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_open_container_locked(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test open_container() handles ContainerLockedError."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import open_container  # noqa: E402
        from server.api.container_models import (
            OpenContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_persistence.get_container = AsyncMock(
            return_value={"container_id": str(container_id), "room_id": None, "items": []}
        )
        mock_persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
        mock_container_service.open_container = AsyncMock(side_effect=ContainerLockedError("Locked"))
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                assert exc_info.value.status_code == 423

    @pytest.mark.asyncio
    async def test_open_container_access_denied(
        self, mock_request, mock_user, mock_persistence, mock_container_service
    ):
        """Test open_container() handles ContainerAccessDeniedError."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import open_container  # noqa: E402
        from server.api.container_models import (
            OpenContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = OpenContainerRequest(container_id=container_id)
        player_id = uuid.uuid4()

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_persistence.get_container = AsyncMock(
            return_value={"container_id": str(container_id), "room_id": None, "items": []}
        )
        mock_persistence.get_player_by_id = AsyncMock(return_value=MagicMock())
        mock_container_service.open_container = AsyncMock(side_effect=ContainerAccessDeniedError("Access denied"))
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await open_container(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                assert exc_info.value.status_code == 403


class TestTransferItems:
    """Test transfer_items() endpoint."""

    @pytest.mark.asyncio
    async def test_transfer_items_not_authenticated(self, mock_request):
        """Test transfer_items() requires authentication."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import transfer_items  # noqa: E402
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

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
                # Reason: Intentionally passing None to test unauthenticated scenario
                current_user=None,  # type: ignore[arg-type]
                persistence=AsyncMock(),
                connection_manager=MagicMock(),
            )
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_transfer_items_rate_limit(self, mock_request, mock_user):
        """Test transfer_items() enforces rate limiting."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import transfer_items  # noqa: E402
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = TransferContainerRequest(
            container_id=uuid.uuid4(),
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await transfer_items(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=AsyncMock(),
                    connection_manager=MagicMock(),
                )
            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_transfer_items_to_container(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test transfer_items() transfers to container."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import transfer_items  # noqa: E402
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()
        from typing import Any

        mock_result: dict[str, Any] = {"container": {}, "player_inventory": []}

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_container_service.transfer_to_container = AsyncMock(return_value=mock_result)
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with patch("server.api.container_endpoints_basic.emit_transfer_event", new_callable=AsyncMock):
                    result = await transfer_items(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                    assert result.container is not None
                mock_container_service.transfer_to_container.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_items_to_player(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test transfer_items() transfers to player."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import transfer_items  # noqa: E402
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_player",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()
        from typing import Any

        mock_result: dict[str, Any] = {"container": {}, "player_inventory": []}

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_container_service.transfer_from_container = AsyncMock(return_value=mock_result)
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with patch("server.api.container_endpoints_basic.emit_transfer_event", new_callable=AsyncMock):
                    result = await transfer_items(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                    assert result.container is not None
                    mock_container_service.transfer_from_container.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_transfer_items_capacity_error(
        self, mock_request, mock_user, mock_persistence, mock_container_service
    ):
        """Test transfer_items() handles ContainerCapacityError."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import transfer_items  # noqa: E402
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_container_service.transfer_to_container = AsyncMock(
            side_effect=ContainerCapacityError("Capacity exceeded")
        )
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await transfer_items(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                assert exc_info.value.status_code == 409

    @pytest.mark.asyncio
    async def test_transfer_items_stale_token(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test transfer_items() handles stale mutation token."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import transfer_items  # noqa: E402
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        player_id = uuid.uuid4()

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_container_service.transfer_to_container = AsyncMock(
            side_effect=ContainerServiceError("Stale mutation token")
        )
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                with pytest.raises(LoggedHTTPException) as exc_info:
                    await transfer_items(
                        request_data=request_data,
                        request=mock_request,
                        current_user=mock_user,
                        persistence=mock_persistence,
                        connection_manager=MagicMock(),
                    )
                assert exc_info.value.status_code == 412


class TestCloseContainer:
    """Test close_container() endpoint."""

    @pytest.mark.asyncio
    async def test_close_container_not_authenticated(self, mock_request):
        """Test close_container() requires authentication."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import close_container  # noqa: E402
        from server.api.container_models import (
            CloseContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = CloseContainerRequest(container_id=uuid.uuid4(), mutation_token="token")
        with pytest.raises(LoggedHTTPException) as exc_info:
            await close_container(
                request_data=request_data,
                request=mock_request,
                # Reason: Intentionally passing None to test unauthenticated scenario
                current_user=None,  # type: ignore[arg-type]
                persistence=AsyncMock(),
                connection_manager=MagicMock(),
            )
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_close_container_rate_limit(self, mock_request, mock_user):
        """Test close_container() enforces rate limiting."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import close_container  # noqa: E402
        from server.api.container_models import (
            CloseContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        request_data = CloseContainerRequest(container_id=uuid.uuid4(), mutation_token="token")
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = RateLimitError("Rate limit exceeded", retry_after=60)
            with pytest.raises(LoggedHTTPException) as exc_info:
                await close_container(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=AsyncMock(),
                    connection_manager=MagicMock(),
                )
            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_close_container_success(self, mock_request, mock_user, mock_persistence, mock_container_service):
        """Test close_container() successfully closes container."""
        # Lazy import to avoid circular import
        from server.api.container_endpoints_basic import close_container  # noqa: E402
        from server.api.container_models import (
            CloseContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

        container_id = uuid.uuid4()
        request_data = CloseContainerRequest(container_id=container_id, mutation_token="token")
        player_id = uuid.uuid4()

        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        mock_persistence.get_container = AsyncMock(
            return_value={"container_id": str(container_id), "room_id": None, "items": []}
        )
        mock_container_service.close_container = AsyncMock()
        mock_request.app.state.persistence = mock_persistence

        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            with patch(
                "server.api.container_endpoints_basic.get_container_service", return_value=mock_container_service
            ):
                result = await close_container(
                    request_data=request_data,
                    request=mock_request,
                    current_user=mock_user,
                    persistence=mock_persistence,
                    connection_manager=MagicMock(),
                )
                assert result.status == "closed"
                mock_container_service.close_container.assert_awaited_once()


class TestRequestModels:
    """Test request model validation."""

    def test_transfer_container_request_direction_validation(self):
        """Test TransferContainerRequest validates direction."""
        # Lazy import to avoid circular import
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

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
        # Lazy import to avoid circular import
        from server.api.container_models import (
            TransferContainerRequest,  # noqa: E402  # Reason: Lazy import inside function to avoid circular import chain during module initialization
        )

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
