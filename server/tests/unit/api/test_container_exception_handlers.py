"""
Unit tests for container exception handlers.

Tests exception handling and HTTP status code mapping for container operations.
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import uuid
from unittest.mock import MagicMock, Mock, patch

import pytest
from fastapi import Request, status

from server.api.container_exception_handlers import (
    handle_close_container_exceptions,
    handle_loot_all_exceptions,
    handle_open_container_exceptions,
    handle_transfer_items_exceptions,
)
from server.exceptions import LoggedHTTPException
from server.models.user import User
from server.services.container_service import (
    ContainerAccessDeniedError,
    ContainerCapacityError,
    ContainerLockedError,
    ContainerNotFoundError,
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
    user = MagicMock(spec=User)
    user.id = uuid.uuid4()
    user.username = "testuser"
    return user


@pytest.fixture
def container_id():
    """Create a test container ID."""
    return uuid.uuid4()


class TestHandleOpenContainerExceptions:
    """Test handle_open_container_exceptions function."""

    def test_handle_open_container_exceptions_not_found(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions returns 404 for ContainerNotFoundError."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND
        assert "not found" in exc_info.value.detail.lower()

    def test_handle_open_container_exceptions_locked(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions returns 423 for ContainerLockedError."""
        error = ContainerLockedError("Container is locked")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_423_LOCKED
        assert "locked" in exc_info.value.detail.lower()

    def test_handle_open_container_exceptions_access_denied(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions returns 403 for ContainerAccessDeniedError."""
        error = ContainerAccessDeniedError("Access denied")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN
        assert "denied" in exc_info.value.detail.lower()

    def test_handle_open_container_exceptions_already_open(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions returns 409 for already open error."""
        error = ContainerServiceError("Container is already open")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_409_CONFLICT
        assert "already" in exc_info.value.detail.lower()

    def test_handle_open_container_exceptions_service_error(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions returns 500 for generic ContainerServiceError."""
        error = ContainerServiceError("Service error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    def test_handle_open_container_exceptions_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions returns 500 for generic exceptions."""
        error = ValueError("Unexpected error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestHandleTransferItemsExceptions:
    """Test handle_transfer_items_exceptions function."""

    def test_handle_transfer_items_exceptions_not_found(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 404 for ContainerNotFoundError."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND

    def test_handle_transfer_items_exceptions_capacity_error(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 409 for ContainerCapacityError."""
        error = ContainerCapacityError("Capacity exceeded")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_409_CONFLICT

    def test_handle_transfer_items_exceptions_access_denied(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 403 for ContainerAccessDeniedError."""
        error = ContainerAccessDeniedError("Access denied")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN

    def test_handle_transfer_items_exceptions_stale_token(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 412 for stale mutation token."""
        error = ContainerServiceError("Stale mutation token")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED
        assert "stale" in exc_info.value.detail.lower()

    def test_handle_transfer_items_exceptions_invalid_stack(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 400 for invalid stack."""
        error = ContainerServiceError("Invalid item stack")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST

    def test_handle_transfer_items_exceptions_service_error(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 500 for generic ContainerServiceError."""
        error = ContainerServiceError("Service error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    def test_handle_transfer_items_exceptions_validation_error(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 400 for ValidationError."""
        from server.exceptions import ValidationError as MythosValidationError

        error = MythosValidationError("Invalid field value")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST

    def test_handle_transfer_items_exceptions_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions returns 500 for generic exceptions."""
        error = ValueError("Unexpected error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestHandleCloseContainerExceptions:
    """Test handle_close_container_exceptions function."""

    def test_handle_close_container_exceptions_not_found(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions returns 404 for ContainerNotFoundError."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND

    def test_handle_close_container_exceptions_invalid_token(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions returns 400 for invalid token."""
        error = ContainerServiceError("Invalid mutation token")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST

    def test_handle_close_container_exceptions_service_error(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions returns 500 for generic ContainerServiceError."""
        error = ContainerServiceError("Service error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    def test_handle_close_container_exceptions_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions returns 500 for generic exceptions."""
        error = ValueError("Unexpected error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestHandleLootAllExceptions:
    """Test handle_loot_all_exceptions function."""

    def test_handle_loot_all_exceptions_not_found(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions returns 404 for ContainerNotFoundError."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_404_NOT_FOUND

    def test_handle_loot_all_exceptions_locked(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions returns 423 for ContainerLockedError."""
        error = ContainerLockedError("Container is locked")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_423_LOCKED

    def test_handle_loot_all_exceptions_access_denied(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions returns 403 for ContainerAccessDeniedError."""
        error = ContainerAccessDeniedError("Access denied")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN

    def test_handle_loot_all_exceptions_capacity_error(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions returns 409 for ContainerCapacityError."""
        error = ContainerCapacityError("Capacity exceeded")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_409_CONFLICT

    def test_handle_loot_all_exceptions_service_error(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions returns 500 for ContainerServiceError."""
        error = ContainerServiceError("Service error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

    def test_handle_loot_all_exceptions_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions returns 500 for generic exceptions."""
        error = ValueError("Unexpected error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


class TestHandleOpenContainerExceptionsEdgeCases:
    """Additional edge case tests for handle_open_container_exceptions."""

    def test_handle_open_container_exceptions_already_open_variant(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions detects 'already' in error message."""
        error = ContainerServiceError("Container already opened")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_409_CONFLICT

    def test_handle_open_container_exceptions_open_keyword(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions detects 'open' in error message."""
        error = ContainerServiceError("Container is open")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_409_CONFLICT


class TestHandleTransferItemsExceptionsEdgeCases:
    """Additional edge case tests for handle_transfer_items_exceptions."""

    def test_handle_transfer_items_exceptions_mutation_token_error(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions detects mutation token error."""
        error = ContainerServiceError("Invalid mutation token")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_transfer_items_exceptions_token_keyword(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions detects 'token' in error message."""
        error = ContainerServiceError("Token expired")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_transfer_items_exceptions_invalid_keyword(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions detects 'invalid' in error message."""
        error = ContainerServiceError("Invalid operation")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST

    def test_handle_transfer_items_exceptions_stack_keyword(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions detects 'stack' in error message."""
        error = ContainerServiceError("Stack not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST


class TestHandleCloseContainerExceptionsEdgeCases:
    """Additional edge case tests for handle_close_container_exceptions."""

    def test_handle_close_container_exceptions_invalid_keyword(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions detects 'invalid' in error message."""
        error = ContainerServiceError("Invalid operation")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST

    def test_handle_close_container_exceptions_token_keyword(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions detects 'token' in error message."""
        error = ContainerServiceError("Token mismatch")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST


class TestExceptionHandlerLoggerCalls:
    """Test that logger calls are made correctly in exception handlers."""

    def test_handle_open_container_exceptions_logs_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions logs generic errors."""
        error = ValueError("Unexpected error")
        with (
            patch("server.api.container_exception_handlers.logger") as mock_logger,
            pytest.raises(LoggedHTTPException),
        ):
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Unexpected error opening container" in call_args[0][0]
            assert call_args[1]["error"] == "Unexpected error"
            assert call_args[1]["exc_info"] is True

    def test_handle_transfer_items_exceptions_logs_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions logs generic errors."""
        error = RuntimeError("Unexpected error")
        with (
            patch("server.api.container_exception_handlers.logger") as mock_logger,
            pytest.raises(LoggedHTTPException),
        ):
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Unexpected error transferring items" in call_args[0][0]
            assert call_args[1]["error"] == "Unexpected error"
            assert call_args[1]["exc_info"] is True

    def test_handle_close_container_exceptions_logs_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions logs generic errors."""
        error = KeyError("Unexpected error")
        with (
            patch("server.api.container_exception_handlers.logger") as mock_logger,
            pytest.raises(LoggedHTTPException),
        ):
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Unexpected error closing container" in call_args[0][0]
            assert call_args[1]["error"] == "Unexpected error"
            assert call_args[1]["exc_info"] is True

    def test_handle_loot_all_exceptions_logs_generic_error(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions logs generic errors without exc_info."""
        error = TypeError("Unexpected error")
        with (
            patch("server.api.container_exception_handlers.logger") as mock_logger,
            pytest.raises(LoggedHTTPException),
        ):
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Unexpected error in loot-all" in call_args[0][0]
            assert call_args[1]["error"] == "Unexpected error"
            # Note: loot_all handler uses error=str(e) instead of exc_info=True
            assert "exc_info" not in call_args[1]


class TestExceptionHandlerContext:
    """Test that error context is properly created and passed."""

    def test_handle_open_container_exceptions_includes_context(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions includes error context."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.context is not None
        assert exc_info.value.context.metadata.get("container_id") == str(container_id)
        assert exc_info.value.context.metadata.get("operation") == "open_container"

    def test_handle_transfer_items_exceptions_includes_context(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions includes error context."""
        error = ContainerCapacityError("Capacity exceeded")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.context is not None
        assert exc_info.value.context.metadata.get("container_id") == str(container_id)
        assert exc_info.value.context.metadata.get("operation") == "transfer_items"

    def test_handle_close_container_exceptions_includes_context(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions includes error context."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.context is not None
        assert exc_info.value.context.metadata.get("container_id") == str(container_id)
        assert exc_info.value.context.metadata.get("operation") == "close_container"

    def test_handle_loot_all_exceptions_includes_context(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions includes error context."""
        error = ContainerLockedError("Container is locked")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.context is not None
        assert exc_info.value.context.metadata.get("container_id") == str(container_id)
        assert exc_info.value.context.metadata.get("operation") == "loot_all"


class TestExceptionChaining:
    """Test that exceptions are properly chained."""

    def test_handle_open_container_exceptions_chains_exception(self, mock_request, mock_user, container_id):
        """Test handle_open_container_exceptions chains original exception."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_open_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.__cause__ is error

    def test_handle_transfer_items_exceptions_chains_exception(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions chains original exception."""
        error = ContainerCapacityError("Capacity exceeded")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.__cause__ is error

    def test_handle_close_container_exceptions_chains_exception(self, mock_request, mock_user, container_id):
        """Test handle_close_container_exceptions chains original exception."""
        error = ContainerNotFoundError("Container not found")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_close_container_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.__cause__ is error

    def test_handle_loot_all_exceptions_chains_exception(self, mock_request, mock_user, container_id):
        """Test handle_loot_all_exceptions chains original exception."""
        error = ContainerLockedError("Container is locked")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_loot_all_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.__cause__ is error


class TestTransferItemsExceptionsMutationKeyword:
    """Test handle_transfer_items_exceptions detects 'mutation' keyword."""

    def test_handle_transfer_items_exceptions_mutation_keyword(self, mock_request, mock_user, container_id):
        """Test handle_transfer_items_exceptions detects 'mutation' in error message."""
        error = ContainerServiceError("Mutation guard failed")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_transfer_items_exceptions(error, mock_request, mock_user, container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED
        assert "stale" in exc_info.value.detail.lower() or "token" in exc_info.value.detail.lower()
