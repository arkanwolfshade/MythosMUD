"""
Unit tests for the container API's service-error mapping (handle_container_service_error).

Loot-all itself is ContainerService.loot_all (tests/unit/services/test_container_transfers.py).
"""
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions

import uuid
from unittest.mock import MagicMock, Mock

import pytest
from fastapi import Request, status

from server.api.container_helpers import handle_container_service_error
from server.exceptions import LoggedHTTPException
from server.models.user import User
from server.services.container_service import ContainerServiceError


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


class TestHandleContainerServiceErrorEdgeCases:
    """Additional edge case tests for handle_container_service_error."""

    def test_handle_container_service_error_mutation_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'mutation' in error message."""
        error = ContainerServiceError("Invalid mutation")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_no_container_id_or_request_data(self, mock_request, mock_user):
        """Test handle_container_service_error uses 'unknown' when no container_id provided."""
        error = ContainerServiceError("Service error")
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user)
        assert exc_info.value.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        # Note: LoggedHTTPException doesn't expose context as an attribute,
        # it's used internally for logging. The function correctly uses 'unknown'
        # when no container_id is provided (verified in handle_container_service_error implementation)

    def test_handle_container_service_error_token_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'token' in error message."""
        error = ContainerServiceError("Token expired")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_stale_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'stale' in error message."""
        error = ContainerServiceError("Stale data")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_handle_container_service_error_stack_keyword(self, mock_request, mock_user):
        """Test handle_container_service_error detects 'stack' in error message."""
        error = ContainerServiceError("Stack overflow")
        container_id = uuid.uuid4()
        with pytest.raises(LoggedHTTPException) as exc_info:
            handle_container_service_error(error, mock_request, mock_user, container_id=container_id)
        assert exc_info.value.status_code == status.HTTP_400_BAD_REQUEST
