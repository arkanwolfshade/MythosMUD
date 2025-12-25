"""
Tests for Container API endpoints and models.

This module tests the container API request/response models and endpoint logic
for the unified container system covering environmental props, wearable gear,
and corpse storage.

AI Agent: Tests for container API models covering validation, field constraints,
         and request model structure. Created for fresh session execution.
"""


# pylint: disable=redefined-outer-name,too-many-lines
# Justification: pytest fixtures redefine names, comprehensive endpoint tests require many lines

from unittest.mock import AsyncMock, Mock, patch
from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError

from server.exceptions import LoggedHTTPException, RateLimitError
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
    ContainerService,
    ContainerServiceError,
)


# Note: These imports will trigger bcrypt in same session as other tests
# Run in fresh terminal: uv run pytest server/tests/unit/api/test_containers.py -v
@pytest.fixture
def containers_module():
    """Lazily import containers module."""
    from server.api import containers

    return containers


@pytest.fixture
def sample_container_id():
    """Provide sample container UUID."""
    return uuid4()


class TestOpenContainerRequest:
    """Test OpenContainerRequest model validation."""

    def test_valid_open_container_request(self, containers_module, sample_container_id):
        """Test valid open container request."""
        request = containers_module.OpenContainerRequest(container_id=sample_container_id)

        assert request.container_id == sample_container_id
        assert isinstance(request.container_id, UUID)

    def test_open_container_request_requires_container_id(self, containers_module):
        """Test open container request requires container_id."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.OpenContainerRequest()

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("container_id",) for error in errors)

    def test_open_container_request_validates_uuid_format(self, containers_module):
        """Test container_id must be valid UUID."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.OpenContainerRequest(container_id="not-a-uuid")

        errors = exc_info.value.errors()
        assert any("uuid" in str(error).lower() for error in errors)


class TestTransferContainerRequest:
    """Test TransferContainerRequest model validation."""

    def test_valid_transfer_to_container(self, containers_module, sample_container_id):
        """Test valid transfer to container request."""
        request = containers_module.TransferContainerRequest(
            container_id=sample_container_id,
            mutation_token="token123",
            direction="to_container",
            stack={"item_id": "sword01", "quantity": 1},
            quantity=1,
        )

        assert request.container_id == sample_container_id
        assert request.direction == "to_container"
        assert request.quantity == 1

    def test_valid_transfer_to_player(self, containers_module, sample_container_id):
        """Test valid transfer to player request."""
        request = containers_module.TransferContainerRequest(
            container_id=sample_container_id,
            mutation_token="token456",
            direction="to_player",
            stack={"item_id": "potion01"},
            quantity=2,
        )

        assert request.direction == "to_player"
        assert request.quantity == 2

    def test_transfer_direction_validation_rejects_invalid(self, containers_module, sample_container_id):
        """Test direction field validates allowed values."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.TransferContainerRequest(
                container_id=sample_container_id,
                mutation_token="token",
                direction="invalid_direction",
                stack={},
                quantity=1,
            )

        assert any("direction must be" in str(error).lower() for error in exc_info.value.errors())

    def test_transfer_quantity_must_be_positive(self, containers_module, sample_container_id):
        """Test quantity must be >= 1."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.TransferContainerRequest(
                container_id=sample_container_id,
                mutation_token="token",
                direction="to_container",
                stack={},
                quantity=0,
            )

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("quantity",) for error in errors)

    def test_transfer_requires_all_fields(self, containers_module):
        """Test all required fields must be provided."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.TransferContainerRequest(container_id=uuid4())

        # Should have errors for missing required fields
        errors = exc_info.value.errors()
        field_names = {error["loc"][0] for error in errors}
        assert "mutation_token" in field_names or "direction" in field_names


class TestCloseContainerRequest:
    """Test CloseContainerRequest model validation."""

    def test_valid_close_container_request(self, containers_module, sample_container_id):
        """Test valid close container request."""
        request = containers_module.CloseContainerRequest(container_id=sample_container_id, mutation_token="token789")

        assert request.container_id == sample_container_id
        assert request.mutation_token == "token789"

    def test_close_container_requires_mutation_token(self, containers_module, sample_container_id):
        """Test mutation_token is required."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.CloseContainerRequest(container_id=sample_container_id)

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("mutation_token",) for error in errors)


class TestLootAllRequest:
    """Test LootAllRequest model validation."""

    def test_valid_loot_all_request(self, containers_module, sample_container_id):
        """Test valid loot all request."""
        request = containers_module.LootAllRequest(container_id=sample_container_id, mutation_token="loot_token")

        assert request.container_id == sample_container_id
        assert request.mutation_token == "loot_token"

    def test_loot_all_requires_container_id(self, containers_module):
        """Test container_id is required."""
        with pytest.raises(ValidationError) as exc_info:
            containers_module.LootAllRequest(mutation_token="token")

        errors = exc_info.value.errors()
        assert any(error["loc"] == ("container_id",) for error in errors)


class TestContainerRateLimiting:
    """Test container rate limiting configuration."""

    def test_rate_limiter_exists(self, containers_module):
        """Test container rate limiter is configured."""
        assert hasattr(containers_module, "container_rate_limiter")
        assert containers_module.container_rate_limiter is not None

    def test_rate_limiter_has_correct_limits(self, containers_module):
        """Test rate limiter configured with correct limits."""
        limiter = containers_module.container_rate_limiter
        assert limiter.max_requests == 20
        assert limiter.window_seconds == 60


# Helper fixtures for endpoint testing
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
    request.app.state.persistence = Mock()
    request.app.state.connection_manager = Mock()
    return request


@pytest.fixture
def mock_player_id():
    """Mock player ID for testing."""
    return uuid4()


@pytest.fixture
def sample_container_data(sample_container_id):
    """Sample container data for testing."""
    return {
        "container_id": str(sample_container_id),
        "source_type": "environment",
        "room_id": "test_room_001",
        "items": [],
        "capacity_slots": 10,
        "lock_state": "unlocked",
    }


@pytest.fixture
def mock_persistence(mock_player_id, sample_container_id, sample_container_data):
    """Mock persistence layer for testing."""
    persistence = AsyncMock()
    player = Mock()
    player.player_id = mock_player_id
    persistence.get_player_by_user_id = AsyncMock(return_value=player)
    persistence.get_container = AsyncMock(return_value=sample_container_data)
    return persistence


@pytest.fixture
def mock_container_service():
    """Mock ContainerService for testing."""
    service = Mock(spec=ContainerService)
    service.open_container = AsyncMock()
    service.transfer_to_container = AsyncMock()
    service.transfer_from_container = AsyncMock()
    service.close_container = AsyncMock()
    return service


class TestOpenContainerEndpoint:
    """Test open_container endpoint."""

    @pytest.mark.asyncio
    async def test_open_container_success(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test successful container opening."""
        mock_request.app.state.persistence = mock_persistence

        # Setup container service mock
        mock_container_service = Mock()
        result_data = {
            "container": {
                "container_id": str(sample_container_id),
                "source_type": "environmental",
                "room_id": "test_room_001",
                "items": [],
            },
            "mutation_token": "test_token_123",
        }
        mock_container_service.open_container = AsyncMock(return_value=result_data)

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(
                containers_module, "_get_player_id_from_user", return_value=mock_player_id
            ) as mock_get_player:
                with patch.object(containers_module, "emit_container_opened", new_callable=AsyncMock):
                    with patch.object(containers_module, "emit_container_opened_to_room", new_callable=AsyncMock):
                        request_data = containers_module.OpenContainerRequest(container_id=sample_container_id)
                        result = await containers_module.open_container(
                            request_data=request_data, request=mock_request, current_user=mock_current_user
                        )

                        assert result == result_data
                        mock_container_service.open_container.assert_called_once_with(
                            sample_container_id, mock_player_id
                        )
                        mock_get_player.assert_called_once()

    @pytest.mark.asyncio
    async def test_open_container_no_user(self, containers_module, mock_request, sample_container_id):
        """Test open_container raises error when no user."""
        request_data = containers_module.OpenContainerRequest(container_id=sample_container_id)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await containers_module.open_container(request_data=request_data, request=mock_request, current_user=None)

        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_open_container_rate_limit(
        self, containers_module, mock_current_user, mock_request, sample_container_id
    ):
        """Test open_container handles rate limiting."""
        request_data = containers_module.OpenContainerRequest(container_id=sample_container_id)

        with patch.object(
            containers_module.container_rate_limiter,
            "enforce_rate_limit",
            side_effect=RateLimitError("Rate limit", retry_after=60),
        ):
            with pytest.raises(LoggedHTTPException) as exc_info:
                await containers_module.open_container(
                    request_data=request_data, request=mock_request, current_user=mock_current_user
                )

            assert exc_info.value.status_code == 429

    @pytest.mark.asyncio
    async def test_open_container_not_found(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test open_container handles container not found."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        mock_container_service.open_container = AsyncMock(side_effect=ContainerNotFoundError("Not found"))

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.OpenContainerRequest(container_id=sample_container_id)

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.open_container(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_open_container_locked(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test open_container handles locked container."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        mock_container_service.open_container = AsyncMock(side_effect=ContainerLockedError("Locked"))

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.OpenContainerRequest(container_id=sample_container_id)

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.open_container(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 423

    @pytest.mark.asyncio
    async def test_open_container_access_denied(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test open_container handles access denied."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        mock_container_service.open_container = AsyncMock(side_effect=ContainerAccessDeniedError("Access denied"))

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.OpenContainerRequest(container_id=sample_container_id)

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.open_container(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 403


class TestTransferItemsEndpoint:
    """Test transfer_items endpoint."""

    @pytest.mark.asyncio
    async def test_transfer_to_container_success(
        self,
        containers_module,
        mock_current_user,
        mock_request,
        mock_player_id,
        sample_container_id,
        mock_persistence,
    ):
        """Test successful transfer to container."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        result_data = {
            "container": {"container_id": str(sample_container_id), "items": []},
            "player_inventory": [],
        }
        mock_container_service.transfer_to_container = AsyncMock(return_value=result_data)

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                with patch.object(containers_module, "emit_container_updated", new_callable=AsyncMock):
                    request_data = containers_module.TransferContainerRequest(
                        container_id=sample_container_id,
                        mutation_token="test_token",
                        direction="to_container",
                        stack={"item_id": "sword01"},
                        quantity=1,
                    )
                    result = await containers_module.transfer_items(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                    assert result == result_data

    @pytest.mark.asyncio
    async def test_transfer_to_player_success(
        self,
        containers_module,
        mock_current_user,
        mock_request,
        mock_player_id,
        sample_container_id,
        mock_persistence,
    ):
        """Test successful transfer to player."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        result_data = {
            "container": {"container_id": str(sample_container_id), "items": []},
            "player_inventory": [],
        }
        mock_container_service.transfer_from_container = AsyncMock(return_value=result_data)

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                with patch.object(containers_module, "emit_container_updated", new_callable=AsyncMock):
                    request_data = containers_module.TransferContainerRequest(
                        container_id=sample_container_id,
                        mutation_token="test_token",
                        direction="to_player",
                        stack={"item_id": "sword01"},
                        quantity=1,
                    )
                    result = await containers_module.transfer_items(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                    assert result == result_data

    @pytest.mark.asyncio
    async def test_transfer_capacity_exceeded(
        self,
        containers_module,
        mock_current_user,
        mock_request,
        mock_player_id,
        sample_container_id,
        mock_persistence,
    ):
        """Test transfer handles capacity exceeded."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        mock_container_service.transfer_to_container = AsyncMock(side_effect=ContainerCapacityError("Full"))

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.TransferContainerRequest(
                    container_id=sample_container_id,
                    mutation_token="test_token",
                    direction="to_container",
                    stack={"item_id": "sword01"},
                    quantity=1,
                )

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.transfer_items(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 409

    @pytest.mark.asyncio
    async def test_transfer_stale_token(
        self,
        containers_module,
        mock_current_user,
        mock_request,
        mock_player_id,
        sample_container_id,
        mock_persistence,
    ):
        """Test transfer handles stale mutation token."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        mock_container_service.transfer_to_container = AsyncMock(
            side_effect=ContainerServiceError("stale mutation token")
        )

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.TransferContainerRequest(
                    container_id=sample_container_id,
                    mutation_token="stale_token",
                    direction="to_container",
                    stack={"item_id": "sword01"},
                    quantity=1,
                )

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.transfer_items(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 412


class TestCloseContainerEndpoint:
    """Test close_container endpoint."""

    @pytest.mark.asyncio
    async def test_close_container_success(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test successful container closing."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_container = Mock(return_value={"room_id": "test_room"})

        mock_container_service = Mock()
        mock_container_service.close_container = AsyncMock()

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                with patch.object(containers_module, "emit_container_closed", new_callable=AsyncMock):
                    request_data = containers_module.CloseContainerRequest(
                        container_id=sample_container_id, mutation_token="test_token"
                    )
                    result = await containers_module.close_container(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                    assert result == {"status": "closed"}
                    mock_container_service.close_container.assert_called_once()

    @pytest.mark.asyncio
    async def test_close_container_not_found(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test close_container handles container not found."""
        mock_request.app.state.persistence = mock_persistence

        mock_container_service = Mock()
        mock_container_service.close_container = AsyncMock(side_effect=ContainerNotFoundError("Not found"))

        with patch.object(containers_module, "_get_container_service", return_value=mock_container_service):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.CloseContainerRequest(
                    container_id=sample_container_id, mutation_token="test_token"
                )

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.close_container(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 404


class TestLootAllEndpoint:
    """Test loot_all_items endpoint."""

    @pytest.mark.asyncio
    async def test_loot_all_container_not_found_simple(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test loot_all handles container not found (simplified test avoiding async/sync inconsistency)."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_container = AsyncMock(return_value=None)

        with patch.object(containers_module, "_get_container_service"):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.LootAllRequest(
                    container_id=sample_container_id, mutation_token="test_token"
                )

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.loot_all_items(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_loot_all_container_not_found(
        self, containers_module, mock_current_user, mock_request, mock_player_id, sample_container_id, mock_persistence
    ):
        """Test loot_all handles container not found."""
        mock_request.app.state.persistence = mock_persistence
        mock_persistence.get_container = AsyncMock(return_value=None)

        with patch.object(containers_module, "_get_container_service"):
            with patch.object(containers_module, "_get_player_id_from_user", return_value=mock_player_id):
                request_data = containers_module.LootAllRequest(
                    container_id=sample_container_id, mutation_token="test_token"
                )

                with pytest.raises(LoggedHTTPException) as exc_info:
                    await containers_module.loot_all_items(
                        request_data=request_data, request=mock_request, current_user=mock_current_user
                    )

                assert exc_info.value.status_code == 404


class TestHelperFunctions:
    """Test helper functions in containers module."""

    def test_create_error_context(self, containers_module, mock_request, mock_current_user):
        """Test _create_error_context helper function."""
        context = containers_module._create_error_context(
            mock_request, mock_current_user, operation="test", extra="data"
        )

        assert context is not None
        assert hasattr(context, "metadata")
        assert context.metadata.get("operation") == "test"
        assert context.metadata.get("extra") == "data"

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_success(
        self, containers_module, mock_current_user, mock_persistence, mock_player_id
    ):
        """Test _get_player_id_from_user returns player ID."""
        player = Mock()
        player.player_id = mock_player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=player)

        result = await containers_module._get_player_id_from_user(mock_current_user, mock_persistence)

        assert result == mock_player_id

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_not_found(self, containers_module, mock_current_user, mock_persistence):
        """Test _get_player_id_from_user raises error when player not found."""
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=None)

        with pytest.raises(LoggedHTTPException) as exc_info:
            await containers_module._get_player_id_from_user(mock_current_user, mock_persistence)

        assert exc_info.value.status_code == 404

    def test_get_container_service_with_persistence(self, containers_module, mock_persistence):
        """Test _get_container_service with persistence provided."""
        service = containers_module._get_container_service(persistence=mock_persistence)

        # Verify service is created (can't check exact type due to mocking)
        assert service is not None
        assert hasattr(service, "persistence")

    def test_get_container_service_with_request(self, containers_module, mock_request, mock_persistence):
        """Test _get_container_service with request provided."""
        mock_request.app.state.persistence = mock_persistence

        service = containers_module._get_container_service(request=mock_request)

        # Verify service is created (can't check exact type due to mocking)
        assert service is not None
        assert hasattr(service, "persistence")

    def test_get_container_service_error_when_none(self, containers_module):
        """Test _get_container_service raises error when neither provided."""
        with pytest.raises(ValueError):
            containers_module._get_container_service()
