"""
Tests for standardized error responses.

This module tests the StandardizedErrorResponse class to ensure it correctly
handles all types of exceptions and returns consistent error responses
across all API endpoints.
"""

import pytest
from fastapi import HTTPException
from pydantic import ValidationError

from server.error_handlers.standardized_responses import (
    StandardizedErrorResponse,
    create_standardized_error_response,
    handle_api_error,
)
from server.error_types import ErrorType
from server.exceptions import (
    AuthenticationError,
    DatabaseError,
    ErrorContext,
    GameLogicError,
    LoggedHTTPException,
    NetworkError,
    RateLimitError,
    ResourceNotFoundError,
    create_error_context,
)
from server.exceptions import (
    ValidationError as MythosValidationError,
)
from server.models.command import SayCommand


class TestStandardizedErrorResponse:
    """Test StandardizedErrorResponse functionality."""

    def test_standardized_error_response_initialization(self):
        """Test that StandardizedErrorResponse initializes correctly."""
        handler = StandardizedErrorResponse()
        assert handler is not None
        assert handler.context is not None
        assert handler.request is None

    def test_standardized_error_response_with_request(self):
        """Test initialization with FastAPI request."""

        # Mock request object
        class MockRequest:
            def __init__(self):
                self.state = type("State", (), {})()
                self.state.user = {"id": "test_user_id"}
                self.state.session_id = "test_session"
                self.state.request_id = "test_request"
                self.url = "http://test.com/api/test"
                self.method = "POST"
                self.headers = {"user-agent": "test-agent", "content-type": "application/json"}

        mock_request = MockRequest()
        handler = StandardizedErrorResponse(request=mock_request)

        assert handler.request == mock_request
        assert handler.context.user_id == "test_user_id"
        assert handler.context.session_id == "test_session"
        assert handler.context.request_id == "test_request"

    def test_handle_mythos_validation_error(self):
        """Test handling of MythosValidationError."""
        error = MythosValidationError(
            message="Validation failed",
            context=create_error_context(user_id="test_user"),
            details={"field": "message"},
            user_friendly="Please check your input",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error)

        assert response.status_code == 422  # Unprocessable Entity
        content = response.body.decode()
        assert '"type":"validation_error"' in content
        assert '"user_friendly":"Please check your input"' in content

    def test_handle_authentication_error(self):
        """Test handling of AuthenticationError."""
        error = AuthenticationError(
            message="Authentication failed",
            context=create_error_context(user_id="test_user"),
            user_friendly="Please log in again",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error)

        assert response.status_code == 401  # Unauthorized
        content = response.body.decode()
        assert '"type":"authentication_failed"' in content
        assert '"user_friendly":"Please log in again"' in content

    def test_handle_game_logic_error(self):
        """Test handling of GameLogicError."""
        error = GameLogicError(
            message="Invalid game action",
            context=create_error_context(user_id="test_user"),
            user_friendly="You cannot perform that action",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error)

        assert response.status_code == 400  # Bad Request
        content = response.body.decode()
        assert '"type":"game_logic_error"' in content
        assert '"user_friendly":"You cannot perform that action"' in content

    def test_handle_database_error(self):
        """Test handling of DatabaseError."""
        error = DatabaseError(
            message="Database connection failed",
            context=create_error_context(user_id="test_user"),
            user_friendly="Database temporarily unavailable",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error)

        assert response.status_code == 503  # Service Unavailable
        content = response.body.decode()
        assert '"type":"database_error"' in content
        assert '"user_friendly":"Database temporarily unavailable"' in content

    def test_handle_resource_not_found_error(self):
        """Test handling of ResourceNotFoundError."""
        error = ResourceNotFoundError(
            message="Player not found",
            context=create_error_context(user_id="test_user"),
            user_friendly="Player does not exist",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error)

        assert response.status_code == 404  # Not Found
        content = response.body.decode()
        assert '"type":"resource_not_found"' in content
        assert '"user_friendly":"Player does not exist"' in content

    def test_handle_pydantic_validation_error(self):
        """Test handling of Pydantic ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            SayCommand()  # Missing required message field

        validation_error = exc_info.value
        handler = StandardizedErrorResponse()

        response = handler.handle_exception(validation_error)

        assert response.status_code == 422  # Unprocessable Entity
        content = response.body.decode()
        assert '"type":"missing_required_field"' in content
        assert '"user_friendly"' in content

    def test_handle_logged_http_exception(self):
        """Test handling of LoggedHTTPException."""
        exception = LoggedHTTPException(
            status_code=404, detail="Resource not found", context=create_error_context(user_id="test_user")
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(exception)

        assert response.status_code == 404
        content = response.body.decode()
        assert '"type":"resource_not_found"' in content
        assert '"message":"Resource not found"' in content

    def test_handle_http_exception(self):
        """Test handling of standard HTTPException."""
        exception = HTTPException(status_code=400, detail="Bad request")

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(exception)

        assert response.status_code == 400
        content = response.body.decode()
        assert '"type":"invalid_input"' in content
        assert '"message":"Bad request"' in content

    def test_handle_generic_exception(self):
        """Test handling of generic exceptions."""
        exception = ValueError("Generic error")

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(exception)

        assert response.status_code == 500  # Internal Server Error
        content = response.body.decode()
        assert '"type":"internal_error"' in content
        assert '"user_friendly":"An internal error occurred"' in content

    def test_handle_exception_with_details(self):
        """Test handling exceptions with detailed information."""
        error = MythosValidationError(
            message="Validation failed",
            context=create_error_context(user_id="test_user"),
            details={"field": "message", "value": "invalid"},
            user_friendly="Please check your input",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error, include_details=True)

        assert response.status_code == 422
        content = response.body.decode()
        assert '"field":"message"' in content
        assert '"context"' in content

    def test_handle_exception_websocket_response(self):
        """Test handling exceptions with WebSocket response type."""
        error = MythosValidationError(
            message="Validation failed",
            context=create_error_context(user_id="test_user"),
            user_friendly="Please check your input",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error, response_type="websocket")

        assert response.status_code == 422
        content = response.body.decode()
        assert '"type":"error"' in content
        assert '"error_type":"validation_error"' in content

    def test_handle_exception_sse_response(self):
        """Test handling exceptions with SSE response type."""
        error = MythosValidationError(
            message="Validation failed",
            context=create_error_context(user_id="test_user"),
            user_friendly="Please check your input",
        )

        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error, response_type="sse")

        assert response.status_code == 422
        content = response.body.decode()
        assert '"type":"error"' in content
        assert '"error_type":"validation_error"' in content

    def test_status_code_mappings(self):
        """Test that status code mappings are correct."""
        handler = StandardizedErrorResponse()

        # Test authentication errors
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.AUTHENTICATION_FAILED] == 401
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.AUTHORIZATION_DENIED] == 403

        # Test validation errors
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.VALIDATION_ERROR] == 422
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.INVALID_INPUT] == 400

        # Test resource errors
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.RESOURCE_NOT_FOUND] == 404
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.RESOURCE_CONFLICT] == 409

        # Test system errors
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.INTERNAL_ERROR] == 500
        assert handler.STATUS_CODE_MAPPINGS[ErrorType.DATABASE_ERROR] == 503

    def test_user_friendly_message_mappings(self):
        """Test that user-friendly message mappings are correct."""
        handler = StandardizedErrorResponse()

        # Test that all error types have user-friendly messages
        for error_type in ErrorType:
            assert error_type in handler.USER_FRIENDLY_MESSAGES
            assert handler.USER_FRIENDLY_MESSAGES[error_type] is not None
            assert len(handler.USER_FRIENDLY_MESSAGES[error_type]) > 0

    def test_determine_error_type_from_exception(self):
        """Test determination of error type from exception."""
        handler = StandardizedErrorResponse()

        # Test AuthenticationError
        auth_error = AuthenticationError("Auth failed")
        assert handler._determine_error_type_from_exception(auth_error) == ErrorType.AUTHENTICATION_FAILED

        # Test MythosValidationError
        validation_error = MythosValidationError("Validation failed")
        assert handler._determine_error_type_from_exception(validation_error) == ErrorType.VALIDATION_ERROR

        # Test GameLogicError
        game_error = GameLogicError("Game logic failed")
        assert handler._determine_error_type_from_exception(game_error) == ErrorType.GAME_LOGIC_ERROR

        # Test DatabaseError
        db_error = DatabaseError("Database failed")
        assert handler._determine_error_type_from_exception(db_error) == ErrorType.DATABASE_ERROR

        # Test NetworkError
        network_error = NetworkError("Network failed")
        assert handler._determine_error_type_from_exception(network_error) == ErrorType.NETWORK_ERROR

        # Test RateLimitError
        rate_error = RateLimitError("Rate limit exceeded")
        assert handler._determine_error_type_from_exception(rate_error) == ErrorType.RATE_LIMIT_EXCEEDED

        # Test ResourceNotFoundError
        resource_error = ResourceNotFoundError("Resource not found")
        assert handler._determine_error_type_from_exception(resource_error) == ErrorType.RESOURCE_NOT_FOUND

    def test_map_status_code_to_error_type(self):
        """Test mapping of status codes to error types."""
        handler = StandardizedErrorResponse()

        assert handler._map_status_code_to_error_type(400) == ErrorType.INVALID_INPUT
        assert handler._map_status_code_to_error_type(401) == ErrorType.AUTHENTICATION_FAILED
        assert handler._map_status_code_to_error_type(403) == ErrorType.AUTHORIZATION_DENIED
        assert handler._map_status_code_to_error_type(404) == ErrorType.RESOURCE_NOT_FOUND
        assert handler._map_status_code_to_error_type(409) == ErrorType.RESOURCE_CONFLICT
        assert handler._map_status_code_to_error_type(422) == ErrorType.VALIDATION_ERROR
        assert handler._map_status_code_to_error_type(429) == ErrorType.RATE_LIMIT_EXCEEDED
        assert handler._map_status_code_to_error_type(500) == ErrorType.INTERNAL_ERROR
        assert handler._map_status_code_to_error_type(503) == ErrorType.SYSTEM_ERROR
        assert handler._map_status_code_to_error_type(504) == ErrorType.TIMEOUT_ERROR

        # Test unknown status code
        assert handler._map_status_code_to_error_type(999) == ErrorType.INTERNAL_ERROR

    def test_generate_user_friendly_message(self):
        """Test generation of user-friendly messages."""
        handler = StandardizedErrorResponse()

        # Test with custom user-friendly message
        error = MythosValidationError(message="Technical message", user_friendly="Custom user message")
        message = handler._generate_user_friendly_message(ErrorType.VALIDATION_ERROR, error)
        assert message == "Custom user message"

        # Test with default message (MythosValidationError sets user_friendly to message if not provided)
        error = MythosValidationError(message="Technical message")
        # The error will have user_friendly set to the same as message
        message = handler._generate_user_friendly_message(ErrorType.VALIDATION_ERROR, error)
        assert message == "Technical message"  # Because user_friendly is set to message

    def test_create_error_details(self):
        """Test creation of error details."""
        handler = StandardizedErrorResponse()

        error = MythosValidationError(
            message="Test error",
            context=create_error_context(user_id="test_user"),
            details={"field": "message", "value": "invalid"},
        )

        # Test without details
        details = handler._create_error_details(error, include_details=False)
        assert details == {}

        # Test with details
        details = handler._create_error_details(error, include_details=True)
        assert "field" in details
        assert "value" in details
        assert "context" in details
        assert details["context"]["user_id"] == "test_user"

    def test_create_fallback_response(self):
        """Test creation of fallback error response."""
        handler = StandardizedErrorResponse()

        exception = ValueError("Test error")

        # Test HTTP fallback
        response = handler._create_fallback_response(exception, "http")
        assert response.status_code == 500
        content = response.body.decode()
        assert '"type":"internal_error"' in content
        assert '"fallback":true' in content

        # Test WebSocket fallback
        response = handler._create_fallback_response(exception, "websocket")
        assert response.status_code == 500
        content = response.body.decode()
        assert '"type":"error"' in content
        assert '"error_type":"internal_error"' in content

        # Test SSE fallback
        response = handler._create_fallback_response(exception, "sse")
        assert response.status_code == 500
        content = response.body.decode()
        assert '"type":"error"' in content
        assert '"error_type":"internal_error"' in content

    def test_convenience_functions(self):
        """Test convenience functions for error handling."""
        # Test create_standardized_error_response
        handler = create_standardized_error_response()
        assert isinstance(handler, StandardizedErrorResponse)

        # Test handle_api_error
        exception = ValueError("Test error")
        response = handle_api_error(exception)

        assert response.status_code == 500
        content = response.body.decode()
        assert '"type":"internal_error"' in content

    def test_extract_context_from_request(self):
        """Test extraction of context from request."""

        # Mock request object
        class MockRequest:
            def __init__(self):
                self.state = type("State", (), {})()
                self.state.user = {"id": "test_user_id"}
                self.state.session_id = "test_session"
                self.state.request_id = "test_request"
                self.url = "http://test.com/api/test"
                self.method = "POST"
                self.headers = {"user-agent": "test-agent", "content-type": "application/json"}

        mock_request = MockRequest()
        handler = StandardizedErrorResponse(request=mock_request)

        context = handler._extract_context_from_request(mock_request)
        assert context.user_id == "test_user_id"
        assert context.session_id == "test_session"
        assert context.request_id == "test_request"
        assert context.metadata["url"] == "http://test.com/api/test"
        assert context.metadata["method"] == "POST"
        assert context.metadata["user_agent"] == "test-agent"
        assert context.metadata["content_type"] == "application/json"

    def test_extract_context_from_none_request(self):
        """Test extraction of context from None request."""
        handler = StandardizedErrorResponse()
        context = handler._extract_context_from_request(None)

        assert isinstance(context, ErrorContext)
        assert context.user_id is None
        assert context.session_id is None
        assert context.request_id is None
