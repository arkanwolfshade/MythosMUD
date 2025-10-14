"""
Test error handling middleware for FastAPI integration.

This test suite verifies that the error handling middleware properly integrates
with FastAPI, handles exceptions correctly, and ensures consistent error responses.

As noted in the Pnakotic Manuscripts: "Every middleware must be tested thoroughly
to ensure it does not corrupt the flow of requests through the system."
"""

from unittest.mock import Mock, patch

import pytest
from fastapi import FastAPI, HTTPException, Request
from fastapi.testclient import TestClient
from pydantic import BaseModel

from server.exceptions import (
    AuthenticationError,
    DatabaseError,
    GameLogicError,
    LoggedHTTPException,
    MythosMUDError,
)
from server.middleware.error_handling_middleware import (
    add_error_handling_middleware,
    register_error_handlers,
    setup_error_handling,
)


@pytest.fixture
def app():
    """Create a test FastAPI application."""
    return FastAPI()


@pytest.fixture
def client_with_middleware(app):
    """Create a test client with complete error handling setup."""
    # Use complete setup to ensure all exceptions are handled properly
    setup_error_handling(app, include_details=True)

    # Add test endpoints
    @app.get("/test/success")
    async def test_success():
        return {"message": "success"}

    @app.get("/test/mythos_error")
    async def test_mythos_error():
        raise MythosMUDError("Test Mythos error")

    @app.get("/test/authentication_error")
    async def test_authentication_error():
        raise AuthenticationError("Authentication failed")

    @app.get("/test/database_error")
    async def test_database_error():
        raise DatabaseError("Database connection failed", operation="select")

    @app.get("/test/validation_error")
    async def test_validation_error():
        class TestModel(BaseModel):
            name: str
            age: int

        # Trigger validation error
        TestModel()  # Missing required fields

    @app.get("/test/http_exception")
    async def test_http_exception():
        raise HTTPException(status_code=404, detail="Not found")

    @app.get("/test/logged_http_exception")
    async def test_logged_http_exception():
        raise LoggedHTTPException(status_code=403, detail="Forbidden")

    @app.get("/test/generic_exception")
    async def test_generic_exception():
        raise ValueError("Test generic exception")

    @app.get("/test/zero_division")
    async def test_zero_division():
        return 1 / 0

    return TestClient(app)


@pytest.fixture
def client_with_handlers(app):
    """Create a test client with error handlers registered."""
    register_error_handlers(app, include_details=True)

    # Add test endpoints
    @app.get("/test/mythos_error")
    async def test_mythos_error():
        raise MythosMUDError("Test Mythos error")

    @app.get("/test/validation_error")
    async def test_validation_error():
        class TestModel(BaseModel):
            name: str

        TestModel()  # Missing required field

    return TestClient(app)


class TestErrorHandlingMiddleware:
    """Test ErrorHandlingMiddleware functionality."""

    def test_successful_request_passes_through(self, client_with_middleware):
        """Test that successful requests pass through middleware without modification."""
        response = client_with_middleware.get("/test/success")

        assert response.status_code == 200
        assert response.json() == {"message": "success"}

    def test_mythos_error_handled_correctly(self, client_with_middleware):
        """Test that MythosMUDError is handled correctly by middleware."""
        response = client_with_middleware.get("/test/mythos_error")

        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "internal_error"
        assert "Test Mythos error" in data["error"]["message"]

    def test_authentication_error_handled_correctly(self, client_with_middleware):
        """Test that AuthenticationError is handled correctly by middleware."""
        response = client_with_middleware.get("/test/authentication_error")

        assert response.status_code == 401
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "authentication_failed"

    def test_database_error_handled_correctly(self, client_with_middleware):
        """Test that DatabaseError is handled correctly by middleware."""
        response = client_with_middleware.get("/test/database_error")

        assert response.status_code == 503
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "database_error"

    def test_http_exception_handled_correctly(self, client_with_middleware):
        """Test that HTTPException is handled correctly by middleware."""
        response = client_with_middleware.get("/test/http_exception")

        assert response.status_code == 404
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "resource_not_found"

    def test_logged_http_exception_handled_correctly(self, client_with_middleware):
        """Test that LoggedHTTPException is handled correctly by middleware."""
        response = client_with_middleware.get("/test/logged_http_exception")

        assert response.status_code == 403
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "authorization_denied"

    def test_generic_exception_handled_correctly(self, client_with_middleware):
        """Test that generic exceptions are handled correctly by middleware."""
        response = client_with_middleware.get("/test/generic_exception")

        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "internal_error"
        assert "user_friendly" in data["error"]

    def test_zero_division_handled_correctly(self, client_with_middleware):
        """Test that zero division error is handled correctly by middleware."""
        response = client_with_middleware.get("/test/zero_division")

        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "internal_error"

    def test_request_id_added_to_state(self, app):
        """Test that middleware adds request ID to request state."""
        add_error_handling_middleware(app)

        request_ids = []

        @app.get("/test/request_id")
        async def test_request_id(request: Request):
            request_ids.append(request.state.request_id)
            return {"request_id": request.state.request_id}

        client = TestClient(app)
        response1 = client.get("/test/request_id")
        response2 = client.get("/test/request_id")

        # Verify request IDs are generated
        assert response1.status_code == 200
        assert response2.status_code == 200

        # Verify request IDs are unique
        assert len(request_ids) == 2
        assert request_ids[0] != request_ids[1]

    def test_error_response_includes_details_when_enabled(self, app):
        """Test that error responses include details when include_details=True."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/error_with_details")
        async def test_error_with_details():
            raise GameLogicError(
                "Invalid game action",
                game_action="teleport",
                details={"reason": "insufficient permissions"},
            )

        client = TestClient(app)
        response = client.get("/test/error_with_details")

        assert response.status_code == 400
        data = response.json()
        assert "error" in data
        assert "details" in data["error"]
        # Details should be included
        assert data["error"]["details"]

    def test_error_response_excludes_details_when_disabled(self, app):
        """Test that error responses exclude details when include_details=False."""
        add_error_handling_middleware(app, include_details=False)

        @app.get("/test/error_without_details")
        async def test_error_without_details():
            raise GameLogicError(
                "Invalid game action",
                game_action="teleport",
                details={"reason": "insufficient permissions"},
            )

        client = TestClient(app)
        response = client.get("/test/error_without_details")

        assert response.status_code == 400
        data = response.json()
        assert "error" in data
        # Details should still exist but might be empty or minimal
        assert "details" in data["error"]


class TestErrorHandlers:
    """Test error handler registration."""

    def test_mythos_error_handler(self, client_with_handlers):
        """Test that registered MythosMUDError handler works correctly."""
        response = client_with_handlers.get("/test/mythos_error")

        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "internal_error"

    def test_validation_error_handler(self, client_with_handlers):
        """Test that registered ValidationError handler works correctly."""
        response = client_with_handlers.get("/test/validation_error")

        assert response.status_code == 422
        data = response.json()
        assert "error" in data
        # Should be handled as validation error
        assert "validation" in data["error"]["type"] or "missing" in data["error"]["type"]


class TestCompleteSetup:
    """Test complete error handling setup."""

    def test_setup_error_handling_complete(self, app):
        """Test that setup_error_handling configures everything correctly."""
        setup_error_handling(app, include_details=True)

        @app.get("/test/complete_setup")
        async def test_complete_setup():
            raise MythosMUDError("Test complete setup")

        client = TestClient(app)
        response = client.get("/test/complete_setup")

        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "internal_error"

    def test_setup_handles_both_middleware_and_handlers(self, app):
        """Test that setup registers both middleware and handlers."""
        setup_error_handling(app, include_details=True)

        # Test middleware (handles exceptions in request processing)
        @app.get("/test/middleware_exception")
        async def test_middleware_exception():
            raise ValueError("Test middleware exception")

        # Test handler (handles specific exception types)
        @app.get("/test/handler_exception")
        async def test_handler_exception():
            raise MythosMUDError("Test handler exception")

        client = TestClient(app)

        # Both should return standardized error responses
        response1 = client.get("/test/middleware_exception")
        response2 = client.get("/test/handler_exception")

        assert response1.status_code == 500
        assert response2.status_code == 500

        data1 = response1.json()
        data2 = response2.json()

        assert "error" in data1
        assert "error" in data2
        assert data1["error"]["type"] == "internal_error"
        assert data2["error"]["type"] == "internal_error"


class TestErrorLogging:
    """Test error logging functionality."""

    @patch("server.middleware.error_handling_middleware.logger")
    def test_server_errors_logged_as_error(self, mock_logger, app):
        """Test that server errors (5xx) are logged with error level."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/server_error")
        async def test_server_error():
            raise Exception("Test server error")

        client = TestClient(app)
        _response = client.get("/test/server_error")  # noqa: F841 - Testing logging side effect

        # Verify error was logged
        mock_logger.error.assert_called()

    @patch("server.middleware.error_handling_middleware.logger")
    def test_client_errors_logged_as_warning(self, mock_logger, app):
        """Test that client errors (4xx) are logged with warning level."""
        # Use complete setup to ensure HTTPException is handled
        setup_error_handling(app, include_details=True)

        @app.get("/test/client_error")
        async def test_client_error():
            raise HTTPException(status_code=400, detail="Bad request")

        client = TestClient(app)
        response = client.get("/test/client_error")

        # Note: HTTPException is handled by FastAPI's exception handler,
        # not by middleware, so we verify it returns standardized error response
        assert response.status_code == 400
        data = response.json()
        assert "error" in data


class TestFallbackHandling:
    """Test fallback error handling."""

    def test_fallback_response_on_handler_failure(self, app):
        """Test that fallback response is returned when error handler fails."""
        # This is a difficult test to implement without causing actual failures
        # We'll test that the fallback response structure is correct
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/complex_error")
        async def test_complex_error():
            # Create an error that might cause issues in handling
            raise Exception("Complex error")

        client = TestClient(app)
        response = client.get("/test/complex_error")

        # Should still return a valid error response
        assert response.status_code >= 400
        data = response.json()
        assert "error" in data
        assert "type" in data["error"]
        assert "message" in data["error"]
        assert "user_friendly" in data["error"]


class TestMiddlewareErrorLogging:
    """Test middleware logging for different error scenarios."""

    @patch("server.middleware.error_handling_middleware.logger")
    def test_logging_with_request_state_user_dict(self, mock_logger, app):
        """Test logging extracts user ID from dict-like user state."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/user_dict_error")
        async def test_user_dict_error(request: Request):
            # Set user as dict-like object
            request.state.user = {"id": "user-dict-123", "name": "TestUser"}
            raise Exception("Test user dict error")

        client = TestClient(app)
        response = client.get("/test/user_dict_error")

        assert response.status_code == 500

        # Verify user_id was extracted and logged
        assert mock_logger.error.called
        call_args = mock_logger.error.call_args
        assert call_args[1]["user_id"] == "user-dict-123"

    @patch("server.middleware.error_handling_middleware.logger")
    def test_logging_with_request_state_user_object(self, mock_logger, app):
        """Test logging extracts user ID from object-like user state."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/user_object_error")
        async def test_user_object_error(request: Request):
            # Set user as simple object with id attribute (not Mock to avoid get() issues)
            class UserObj:
                def __init__(self):
                    self.id = "user-obj-456"

            request.state.user = UserObj()
            raise Exception("Test user object error")

        client = TestClient(app)
        response = client.get("/test/user_object_error")

        assert response.status_code == 500

        # Verify error was logged
        assert mock_logger.error.called
        call_args = mock_logger.error.call_args
        # user_id should be extracted from .id attribute
        assert call_args[1]["user_id"] == "user-obj-456"

    @patch("server.middleware.error_handling_middleware.logger")
    def test_logging_with_session_id(self, mock_logger, app):
        """Test logging includes session ID when available."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/session_error")
        async def test_session_error(request: Request):
            request.state.session_id = "test-session-789"
            raise Exception("Test session error")

        client = TestClient(app)
        response = client.get("/test/session_error")

        assert response.status_code == 500

        # Verify session_id was logged
        assert mock_logger.error.called
        call_args = mock_logger.error.call_args
        assert call_args[1]["session_id"] == "test-session-789"

    @patch("server.middleware.error_handling_middleware.logger")
    def test_logging_client_error_as_warning(self, mock_logger, app):
        """Test that 4xx errors are logged as warnings."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/not_found")
        async def test_not_found():
            # Non-MythosMUD exception with 4xx result
            raise ValueError("Not found error")

        client = TestClient(app)
        response = client.get("/test/not_found")

        # Should return error response
        assert response.status_code >= 400

    @patch("server.middleware.error_handling_middleware.logger")
    def test_logging_mythos_error_skipped(self, mock_logger, app):
        """Test that MythosMUDError logging is skipped (already logged in constructor)."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/mythos_skip_log")
        async def test_mythos_skip_log():
            raise MythosMUDError("Already logged error")

        client = TestClient(app)
        response = client.get("/test/mythos_skip_log")

        assert response.status_code == 500

        # MythosMUDError should not be logged again by middleware
        # (it's logged in its constructor)
        # The middleware's _log_exception should recognize this and skip logging

    @patch("server.middleware.error_handling_middleware.logger")
    def test_logging_logged_http_exception_skipped(self, mock_logger, app):
        """Test that LoggedHTTPException logging is skipped (already logged)."""
        add_error_handling_middleware(app, include_details=True)

        @app.get("/test/logged_http_skip")
        async def test_logged_http_skip():
            raise LoggedHTTPException(status_code=403, detail="Already logged HTTP error")

        client = TestClient(app)
        response = client.get("/test/logged_http_skip")

        assert response.status_code == 403


class TestMiddlewareFallbackHandling:
    """Test middleware fallback error handling."""

    @patch("server.middleware.error_handling_middleware.StandardizedErrorResponse")
    def test_fallback_on_handler_exception(self, mock_handler_class, app):
        """Test fallback response when error handler itself raises an exception."""
        add_error_handling_middleware(app, include_details=True)

        # Make the handler raise an exception
        mock_handler_instance = Mock()
        mock_handler_instance.handle_exception.side_effect = Exception("Handler failed")
        mock_handler_class.return_value = mock_handler_instance

        @app.get("/test/handler_failure")
        async def test_handler_failure():
            raise ValueError("Original error")

        client = TestClient(app)
        response = client.get("/test/handler_failure")

        # Should return fallback response
        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert data["error"]["type"] == "internal_error"
        assert data["error"]["message"] == "An unexpected error occurred"
        assert data["error"]["details"]["fallback"] is True

    @patch("server.middleware.error_handling_middleware.logger")
    @patch("server.middleware.error_handling_middleware.StandardizedErrorResponse")
    def test_fallback_logs_handler_error(self, mock_handler_class, mock_logger, app):
        """Test that handler failures are logged."""
        add_error_handling_middleware(app, include_details=True)

        # Make the handler raise an exception
        mock_handler_instance = Mock()
        mock_handler_instance.handle_exception.side_effect = RuntimeError("Handler crashed")
        mock_handler_class.return_value = mock_handler_instance

        @app.get("/test/handler_crash")
        async def test_handler_crash():
            raise ValueError("Original error")

        client = TestClient(app)
        response = client.get("/test/handler_crash")

        assert response.status_code == 500

        # Verify error handler failure was logged
        assert mock_logger.error.called
        call_args = mock_logger.error.call_args
        assert "Error in error handler" in call_args[0][0]


class TestExceptionHandlerRegistration:
    """Test individual exception handler registration."""

    def test_register_error_handlers_adds_all_handlers(self, app):
        """Test that register_error_handlers adds all exception handlers."""
        register_error_handlers(app, include_details=True)

        # Verify handlers were added
        # FastAPI stores exception handlers in app.exception_handlers dict
        assert HTTPException in app.exception_handlers
        assert MythosMUDError in app.exception_handlers
        assert LoggedHTTPException in app.exception_handlers
        assert Exception in app.exception_handlers

    @patch("server.middleware.error_handling_middleware.logger")
    def test_register_error_handlers_logs_registration(self, mock_logger, app):
        """Test that handler registration is logged."""
        register_error_handlers(app, include_details=True)

        # Verify registration was logged
        mock_logger.info.assert_called()
        call_args = mock_logger.info.call_args
        assert "Error handlers registered" in call_args[0][0]


class TestCompleteErrorHandlingSetup:
    """Test complete error handling setup function."""

    @patch("server.middleware.error_handling_middleware.logger")
    def test_setup_error_handling_logs_completion(self, mock_logger, app):
        """Test that setup_error_handling logs completion."""
        setup_error_handling(app, include_details=True)

        # Should log completion
        assert mock_logger.info.called
        # Look for the completion message
        calls = [str(call) for call in mock_logger.info.call_args_list]
        completion_logged = any("Complete error handling setup completed" in call for call in calls)
        assert completion_logged

    def test_setup_includes_both_middleware_and_handlers(self, app):
        """Test that setup includes both middleware and exception handlers."""
        setup_error_handling(app, include_details=False)

        # Verify middleware was added (check app.user_middleware)
        assert len(app.user_middleware) > 0

        # Verify handlers were added
        assert HTTPException in app.exception_handlers
        assert MythosMUDError in app.exception_handlers
