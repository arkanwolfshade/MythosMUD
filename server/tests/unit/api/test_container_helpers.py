"""
Unit tests for container API helper functions.

Tests validation, rate limiting, and utility functions for container operations.
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import Request, status

from server.api.container_helpers import (
    apply_rate_limiting_for_close_container,
    apply_rate_limiting_for_loot_all,
    apply_rate_limiting_for_open_container,
    apply_rate_limiting_for_transfer,
    create_error_context,
    execute_transfer,
    get_container_service,
    get_player_id_from_user,
    handle_container_service_error,
    validate_user_for_close_container,
    validate_user_for_loot_all,
    validate_user_for_open_container,
    validate_user_for_transfer,
)
from server.api.container_models import TransferContainerRequest
from server.error_types import ErrorMessages
from server.exceptions import LoggedHTTPException, RateLimitError
from server.models.user import User
from server.services.container_service import ContainerService, ContainerServiceError


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
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    user.username = "testuser"
    return user


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = AsyncMock()
    return persistence


class TestCreateErrorContext:
    """Test create_error_context function."""

    def test_create_error_context_with_user(self, mock_request, mock_user):
        """Test create_error_context includes user information."""
        context = create_error_context(mock_request, mock_user, operation="test", key="value")
        assert context.metadata["operation"] == "test"
        assert context.metadata["key"] == "value"
        assert context.user_id == str(mock_user.id)

    def test_create_error_context_no_user(self, mock_request):
        """Test create_error_context handles None user."""
        # Ensure mock_request.state doesn't have user_id to test None user case
        if hasattr(mock_request.state, "user_id"):
            delattr(mock_request.state, "user_id")
        context = create_error_context(mock_request, None, operation="test")
        assert context.metadata["operation"] == "test"
        # When current_user is None, user_id should not be set from current_user
        # (it might be set from request.state, but that's a different code path)
        # The key is that create_error_context doesn't set it when current_user is None
        assert context.user_id is None or not hasattr(context, "user_id")

    def test_create_error_context_no_request(self, mock_user):
        """Test create_error_context handles None request."""
        context = create_error_context(None, mock_user, operation="test")
        assert context.metadata["operation"] == "test"


class TestGetPlayerIdFromUser:
    """Test get_player_id_from_user function."""

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_success(self, mock_user, mock_persistence):
        """Test get_player_id_from_user returns player ID."""
        player_id = uuid.uuid4()
        mock_player = MagicMock()
        mock_player.player_id = player_id
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=mock_player)
        result = await get_player_id_from_user(mock_user, mock_persistence)
        assert result == player_id

    @pytest.mark.asyncio
    async def test_get_player_id_from_user_not_found(self, mock_user, mock_persistence):
        """Test get_player_id_from_user raises exception when player not found."""
        mock_persistence.get_player_by_user_id = AsyncMock(return_value=None)
        with pytest.raises(LoggedHTTPException) as exc_info:
            await get_player_id_from_user(mock_user, mock_persistence)
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND


class TestGetContainerService:
    """Test get_container_service function."""

    def test_get_container_service_returns_service(self, mock_persistence):
        """Test get_container_service returns ContainerService instance."""
        service = get_container_service(mock_persistence)
        assert isinstance(service, ContainerService)
        assert service.persistence == mock_persistence


class TestValidateUserForOpenContainer:
    """Test validate_user_for_open_container function."""

    def test_validate_user_for_open_container_success(self, mock_user, mock_request):
        """Test validate_user_for_open_container passes with valid user."""
        # Should not raise
        validate_user_for_open_container(mock_user, mock_request)

    def test_validate_user_for_open_container_no_user(self, mock_request):
        """Test validate_user_for_open_container raises exception for None user."""
        with pytest.raises(LoggedHTTPException) as exc_info:
            validate_user_for_open_container(None, mock_request)
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED
        assert ErrorMessages.AUTHENTICATION_REQUIRED in exc_info.value.detail


class TestApplyRateLimitingForOpenContainer:
    """Test apply_rate_limiting_for_open_container function."""

    def test_apply_rate_limiting_for_open_container_success(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_open_container passes when allowed."""
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            # Should not raise
            apply_rate_limiting_for_open_container(mock_user, mock_request)

    def test_apply_rate_limiting_for_open_container_exceeded(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_open_container raises exception when rate limited."""
        rate_limit_error = RateLimitError("Rate limit exceeded", retry_after=5)
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = rate_limit_error
            with pytest.raises(LoggedHTTPException) as exc_info:
                apply_rate_limiting_for_open_container(mock_user, mock_request)
            assert exc_info.value.status_code == status.HTTP_429_TOO_MANY_REQUESTS


class TestValidateUserForTransfer:
    """Test validate_user_for_transfer function."""

    def test_validate_user_for_transfer_success(self, mock_user, mock_request):
        """Test validate_user_for_transfer passes with valid user."""
        validate_user_for_transfer(mock_user, mock_request)

    def test_validate_user_for_transfer_no_user(self, mock_request):
        """Test validate_user_for_transfer raises exception for None user."""
        with pytest.raises(LoggedHTTPException) as exc_info:
            validate_user_for_transfer(None, mock_request)
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED


class TestApplyRateLimitingForTransfer:
    """Test apply_rate_limiting_for_transfer function."""

    def test_apply_rate_limiting_for_transfer_success(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_transfer passes when allowed."""
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            apply_rate_limiting_for_transfer(mock_user, mock_request)

    def test_apply_rate_limiting_for_transfer_exceeded(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_transfer raises exception when rate limited."""
        rate_limit_error = RateLimitError("Rate limit exceeded", retry_after=5)
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = rate_limit_error
            with pytest.raises(LoggedHTTPException) as exc_info:
                apply_rate_limiting_for_transfer(mock_user, mock_request)
            assert exc_info.value.status_code == status.HTTP_429_TOO_MANY_REQUESTS


class TestExecuteTransfer:
    """Test execute_transfer function."""

    @pytest.mark.asyncio
    async def test_execute_transfer_to_container(self, mock_persistence):
        """Test execute_transfer calls transfer_to_container for to_container direction."""
        container_service = ContainerService(persistence=mock_persistence)
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        expected_result = {"status": "transferred"}
        with patch.object(
            container_service, "transfer_to_container", new_callable=AsyncMock, return_value=expected_result
        ) as mock_transfer:
            result = await execute_transfer(container_service, request_data, player_id)
            assert result == expected_result
            mock_transfer.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_execute_transfer_to_player(self, mock_persistence):
        """Test execute_transfer calls transfer_from_container for to_player direction."""
        container_service = ContainerService(persistence=mock_persistence)
        player_id = uuid.uuid4()
        container_id = uuid.uuid4()
        request_data = TransferContainerRequest(
            container_id=container_id,
            mutation_token="token",
            direction="to_player",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        expected_result = {"status": "transferred"}
        with patch.object(
            container_service, "transfer_from_container", new_callable=AsyncMock, return_value=expected_result
        ) as mock_transfer:
            result = await execute_transfer(container_service, request_data, player_id)
            assert result == expected_result
            mock_transfer.assert_awaited_once()


class TestHandleContainerServiceError:
    """Test handle_container_service_error function."""

    def test_handle_container_service_error_stale_token(self, mock_request, mock_user):
        """Test handle_container_service_error returns 412 for stale token."""
        error = ContainerServiceError("Stale mutation token")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_invalid_stack(self, mock_request, mock_user):
        """Test handle_container_service_error returns 400 for invalid stack."""
        error = ContainerServiceError("Invalid item stack")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST

    def test_handle_container_service_error_generic(self, mock_request, mock_user):
        """Test handle_container_service_error returns 500 for generic error."""
        error = ContainerServiceError("Generic service error")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    def test_handle_container_service_error_with_request_data(self, mock_request, mock_user):
        """Test handle_container_service_error uses request_data.container_id when provided."""
        error = ContainerServiceError("Error")
        request_data = TransferContainerRequest(
            container_id=uuid.uuid4(),
            mutation_token="token",
            direction="to_container",
            stack={"item_id": str(uuid.uuid4())},
            quantity=1,
        )
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, request_data=request_data)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestValidateUserForCloseContainer:
    """Test validate_user_for_close_container function."""

    def test_validate_user_for_close_container_success(self, mock_user, mock_request):
        """Test validate_user_for_close_container passes with valid user."""
        validate_user_for_close_container(mock_user, mock_request)

    def test_validate_user_for_close_container_no_user(self, mock_request):
        """Test validate_user_for_close_container raises exception for None user."""
        with pytest.raises(LoggedHTTPException) as exc_info:
            validate_user_for_close_container(None, mock_request)
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED


class TestApplyRateLimitingForCloseContainer:
    """Test apply_rate_limiting_for_close_container function."""

    def test_apply_rate_limiting_for_close_container_success(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_close_container passes when allowed."""
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            apply_rate_limiting_for_close_container(mock_user, mock_request)

    def test_apply_rate_limiting_for_close_container_exceeded(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_close_container raises exception when rate limited."""
        rate_limit_error = RateLimitError("Rate limit exceeded", retry_after=5)
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = rate_limit_error
            with pytest.raises(LoggedHTTPException) as exc_info:
                apply_rate_limiting_for_close_container(mock_user, mock_request)
            assert exc_info.value.status_code == status.HTTP_429_TOO_MANY_REQUESTS


class TestValidateUserForLootAll:
    """Test validate_user_for_loot_all function."""

    def test_validate_user_for_loot_all_success(self, mock_user, mock_request):
        """Test validate_user_for_loot_all passes with valid user."""
        validate_user_for_loot_all(mock_user, mock_request)

    def test_validate_user_for_loot_all_no_user(self, mock_request):
        """Test validate_user_for_loot_all raises exception for None user."""
        with pytest.raises(LoggedHTTPException) as exc_info:
            validate_user_for_loot_all(None, mock_request)
        assert exc_info.value.status_code == status.HTTP_401_UNAUTHORIZED


class TestApplyRateLimitingForLootAll:
    """Test apply_rate_limiting_for_loot_all function."""

    def test_apply_rate_limiting_for_loot_all_success(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_loot_all passes when allowed."""
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.return_value = None
            apply_rate_limiting_for_loot_all(mock_user, mock_request)

    def test_apply_rate_limiting_for_loot_all_exceeded(self, mock_user, mock_request):
        """Test apply_rate_limiting_for_loot_all raises exception when rate limited."""
        rate_limit_error = RateLimitError("Rate limit exceeded", retry_after=5)
        with patch("server.api.container_helpers.container_rate_limiter") as mock_limiter:
            mock_limiter.enforce_rate_limit.side_effect = rate_limit_error
            with pytest.raises(LoggedHTTPException) as exc_info:
                apply_rate_limiting_for_loot_all(mock_user, mock_request)
            assert exc_info.value.status_code == status.HTTP_429_TOO_MANY_REQUESTS
