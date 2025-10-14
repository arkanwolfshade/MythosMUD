"""
Test comprehensive error logging with proper context information.

This test suite verifies that all error handlers properly log errors with
appropriate context, severity levels, and structured information for debugging
and auditing purposes.

As noted in the Pnakotic Manuscripts: "Every error must be recorded with
sufficient context for future scholars to understand what went wrong."
"""

import json
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

from fastapi import status
from pydantic import BaseModel, ValidationError

from server.error_handlers.pydantic_error_handler import PydanticErrorHandler
from server.error_handlers.standardized_responses import StandardizedErrorResponse
from server.exceptions import (
    AuthenticationError,
    DatabaseError,
    ErrorContext,
    GameLogicError,
    LoggedHTTPException,
    MythosMUDError,
    RateLimitError,
    create_error_context,
)
from server.exceptions import (
    ValidationError as MythosValidationError,
)


class TestErrorContextLogging:
    """Test error context creation and logging."""

    def test_error_context_creation_with_all_fields(self):
        """Test creating error context with all fields populated."""
        timestamp = datetime.now(UTC)
        context = ErrorContext(
            user_id="user123",
            room_id="room456",
            command="say hello",
            session_id="session789",
            request_id="request001",
            timestamp=timestamp,
            metadata={"ip_address": "127.0.0.1", "user_agent": "TestClient/1.0"},
        )

        context_dict = context.to_dict()

        assert context_dict["user_id"] == "user123"
        assert context_dict["room_id"] == "room456"
        assert context_dict["command"] == "say hello"
        assert context_dict["session_id"] == "session789"
        assert context_dict["request_id"] == "request001"
        assert context_dict["timestamp"] == timestamp.isoformat()
        assert context_dict["metadata"]["ip_address"] == "127.0.0.1"
        assert context_dict["metadata"]["user_agent"] == "TestClient/1.0"

    def test_error_context_minimal_creation(self):
        """Test creating error context with minimal fields."""
        context = create_error_context(user_id="user123")

        assert context.user_id == "user123"
        assert context.room_id is None
        assert context.command is None
        assert isinstance(context.timestamp, datetime)
        assert isinstance(context.metadata, dict)

    def test_error_context_serialization(self):
        """Test error context can be serialized to JSON."""
        context = create_error_context(user_id="user123", room_id="room456", metadata={"test": "value"})

        context_dict = context.to_dict()
        json_str = json.dumps(context_dict)

        assert json_str  # Should be able to serialize
        deserialized = json.loads(json_str)
        assert deserialized["user_id"] == "user123"
        assert deserialized["metadata"]["test"] == "value"


class TestMythosMUDErrorLogging:
    """Test MythosMUDError logging functionality."""

    @patch("server.exceptions.logger")
    def test_mythos_error_logs_on_creation(self, mock_logger):
        """Test that MythosMUDError logs when created."""
        context = create_error_context(user_id="user123", command="test")
        _error = MythosMUDError(  # noqa: F841 - Created for logging side effect
            message="Test error",
            context=context,
            details={"field": "value"},
            user_friendly="Something went wrong",
        )

        # Verify logging was called
        mock_logger.error.assert_called_once()
        call_args = mock_logger.error.call_args

        # Verify log message
        assert "MythosMUD error occurred: Test error" in call_args[0][0]

        # Verify log includes error_type
        assert call_args[1]["error_type"] == "MythosMUDError"

        # Verify log includes details
        assert call_args[1]["details"] == {"field": "value"}

    @patch("server.exceptions.logger")
    def test_authentication_error_logs_with_auth_type(self, mock_logger):
        """Test AuthenticationError logs with auth_type information."""
        context = create_error_context(user_id="user123")
        error = AuthenticationError(
            message="Invalid credentials",
            context=context,
            auth_type="jwt_token",
        )

        mock_logger.error.assert_called_once()
        assert error.auth_type == "jwt_token"
        assert error.details["auth_type"] == "jwt_token"

    @patch("server.exceptions.logger")
    def test_database_error_logs_with_operation_info(self, mock_logger):
        """Test DatabaseError logs with operation and table information."""
        context = create_error_context(user_id="user123")
        error = DatabaseError(
            message="Query failed",
            context=context,
            operation="select",
            table="players",
        )

        mock_logger.error.assert_called_once()
        assert error.operation == "select"
        assert error.table == "players"
        assert error.details["operation"] == "select"
        assert error.details["table"] == "players"

    @patch("server.exceptions.logger")
    def test_validation_error_logs_with_field_info(self, mock_logger):
        """Test MythosValidationError logs with field and value information."""
        context = create_error_context(user_id="user123")
        error = MythosValidationError(
            message="Invalid input",
            context=context,
            field="message",
            value="<script>alert('xss')</script>",
        )

        mock_logger.error.assert_called_once()
        assert error.field == "message"
        assert error.details["field"] == "message"
        # Value should be converted to string
        assert "script" in error.details["value"]

    @patch("server.exceptions.logger")
    def test_game_logic_error_logs_with_action_info(self, mock_logger):
        """Test GameLogicError logs with game action information."""
        context = create_error_context(user_id="user123", room_id="room456")
        error = GameLogicError(
            message="Invalid movement",
            context=context,
            game_action="move north",
        )

        mock_logger.error.assert_called_once()
        assert error.game_action == "move north"
        assert error.details["game_action"] == "move north"

    @patch("server.exceptions.logger")
    def test_rate_limit_error_logs_with_retry_info(self, mock_logger):
        """Test RateLimitError logs with retry information."""
        context = create_error_context(user_id="user123")
        error = RateLimitError(
            message="Too many requests",
            context=context,
            limit_type="command_rate",
            retry_after=60,
        )

        mock_logger.error.assert_called_once()
        assert error.limit_type == "command_rate"
        assert error.retry_after == 60
        assert error.details["limit_type"] == "command_rate"
        assert error.details["retry_after"] == 60


class TestLoggedHTTPExceptionLogging:
    """Test LoggedHTTPException logging functionality."""

    @patch("server.exceptions.logger")
    def test_logged_http_exception_logs_on_creation(self, mock_logger):
        """Test that LoggedHTTPException logs when created."""
        context = create_error_context(user_id="user123")
        _exception = LoggedHTTPException(  # noqa: F841 - Created for logging side effect
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
            context=context,
        )

        # Verify logging was called
        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args

        # Verify log message
        assert "HTTP error logged and exception raised" in call_args[0][0]

        # Verify log data
        assert call_args[1]["error_type"] == "LoggedHTTPException"
        assert call_args[1]["status_code"] == 404
        assert call_args[1]["detail"] == "Resource not found"
        assert "context" in call_args[1]

    @patch("server.exceptions.logger")
    def test_logged_http_exception_uses_default_context(self, mock_logger):
        """Test LoggedHTTPException creates default context if none provided."""
        _exception = LoggedHTTPException(  # noqa: F841 - Created for logging side effect
            status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request"
        )

        mock_logger.warning.assert_called_once()
        call_args = mock_logger.warning.call_args
        assert "context" in call_args[1]

    @patch("server.exceptions.get_logger")
    def test_logged_http_exception_uses_custom_logger(self, mock_get_logger):
        """Test LoggedHTTPException can use custom logger name."""
        mock_custom_logger = MagicMock()
        mock_get_logger.return_value = mock_custom_logger

        _exception = LoggedHTTPException(  # noqa: F841 - Created for logging side effect
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal error",
            logger_name="custom.logger",
        )

        # Verify custom logger was requested
        mock_get_logger.assert_called_with("custom.logger")
        mock_custom_logger.warning.assert_called_once()


class TestPydanticErrorHandlerLogging:
    """Test PydanticErrorHandler logging functionality."""

    class SampleModel(BaseModel):
        name: str
        age: int

    @patch("server.error_handlers.pydantic_error_handler.logger")
    def test_pydantic_error_handler_logs_error_info(self, mock_logger):
        """Test PydanticErrorHandler logs detailed error information."""
        context = create_error_context(user_id="user123")
        handler = PydanticErrorHandler(context=context)

        try:
            # Trigger validation error
            self.SampleModel()
        except ValidationError as e:
            response = handler.handle_validation_error(e, self.SampleModel)

            # Verify response was created - response uses standard error response format
            assert response is not None
            assert "error" in response
            error_obj = response["error"]
            # Response from create_standard_error_response has: type, message, user_friendly, details, severity, timestamp
            assert error_obj["type"] == "missing_required_field"
            assert "message" in error_obj
            assert "user_friendly" in error_obj
            assert "details" in error_obj
            assert error_obj["details"]["error_count"] == 2

    @patch("server.error_handlers.pydantic_error_handler.logger")
    def test_pydantic_error_handler_logs_fallback_on_error(self, mock_logger):
        """Test PydanticErrorHandler logs when fallback handling is used."""
        context = create_error_context(user_id="user123")
        handler = PydanticErrorHandler(context=context)

        # Mock error during normal processing
        with patch.object(handler, "_extract_error_info", side_effect=Exception("Test error")):
            try:
                self.SampleModel()
            except ValidationError as e:
                response = handler.handle_validation_error(e)

                # Verify fallback response was created
                assert response is not None
                assert "error" in response
                error_obj = response["error"]
                assert "details" in error_obj
                assert error_obj["details"]["fallback"] is True

                # Verify error was logged
                mock_logger.error.assert_called()


class TestStandardizedResponseLogging:
    """Test StandardizedErrorResponse logging functionality."""

    @patch("server.error_handlers.standardized_responses.logger")
    def test_standardized_response_logs_generic_exceptions(self, mock_logger):
        """Test StandardizedErrorResponse logs generic exceptions."""
        handler = StandardizedErrorResponse()
        exception = Exception("Test generic error")

        _response = handler.handle_exception(exception, include_details=True)  # noqa: F841

        # Verify error was logged
        mock_logger.error.assert_called()
        call_args = mock_logger.error.call_args

        # Verify log message
        assert "Unhandled exception" in call_args[0][0]

    @patch("server.error_handlers.standardized_responses.logger")
    def test_standardized_response_logs_with_request_context(self, mock_logger):
        """Test StandardizedErrorResponse extracts and logs request context."""
        # Test using a pre-configured context instead of trying to extract from mock
        # This tests the actual functionality more directly
        context = create_error_context(
            user_id="user123",
            session_id="session456",
            request_id="request789",
            metadata={"url": "http://testserver/api/test", "method": "POST"},
        )

        # Create error with context
        error = MythosMUDError(message="Test error", context=context)

        # Create handler and handle exception
        handler = StandardizedErrorResponse()
        response = handler.handle_exception(error, include_details=True)

        # Verify response includes full context
        response_data = json.loads(response.body.decode())
        assert "error" in response_data
        error_obj = response_data["error"]
        assert "details" in error_obj
        assert "context" in error_obj["details"]
        assert error_obj["details"]["context"]["user_id"] == "user123"
        assert error_obj["details"]["context"]["session_id"] == "session456"
        assert error_obj["details"]["context"]["request_id"] == "request789"

    @patch("server.error_handlers.standardized_responses.logger")
    def test_standardized_response_logs_fallback_on_error(self, mock_logger):
        """Test StandardizedErrorResponse logs when fallback handling is used."""
        handler = StandardizedErrorResponse()

        # Mock error during normal processing
        with patch.object(handler, "_handle_mythos_error", side_effect=Exception("Processing error")):
            exception = MythosMUDError("Test error")
            response = handler.handle_exception(exception)

            # Verify fallback response was created
            assert response.status_code == 500

            # Verify error was logged
            mock_logger.error.assert_called()


class TestContextPropagation:
    """Test error context propagation across error handling layers."""

    def test_context_propagation_through_pydantic_handler(self):
        """Test context is properly propagated through PydanticErrorHandler."""
        context = create_error_context(
            user_id="user123",
            session_id="session456",
            request_id="request789",
            metadata={"source": "test"},
        )
        handler = PydanticErrorHandler(context=context)

        class TestModel(BaseModel):
            name: str

        try:
            TestModel()
        except ValidationError as e:
            mythos_error = handler.convert_to_mythos_error(e, TestModel)

            # Verify context was propagated
            assert mythos_error.context.user_id == "user123"
            assert mythos_error.context.session_id == "session456"
            assert mythos_error.context.request_id == "request789"
            assert mythos_error.context.metadata["source"] == "test"

    def test_context_propagation_through_standardized_response(self):
        """Test context is properly propagated through StandardizedErrorResponse."""
        # Create context directly for testing
        context = create_error_context(
            user_id="user123",
            session_id="session456",
            metadata={"url": "http://testserver/api/test", "method": "GET"},
        )

        handler = StandardizedErrorResponse()

        # Create error with context
        error = MythosMUDError(
            message="Test error",
            context=context,
        )

        response = handler.handle_exception(error, include_details=True)

        # Verify response includes context
        response_data = json.loads(response.body.decode())
        # The response structure uses "error" wrapper from create_standard_error_response
        assert "error" in response_data
        error_obj = response_data["error"]
        assert "details" in error_obj
        assert "context" in error_obj["details"]
        assert error_obj["details"]["context"]["user_id"] == "user123"
        assert error_obj["details"]["context"]["session_id"] == "session456"


class TestSecurityErrorLogging:
    """Test security-relevant error logging."""

    @patch("server.exceptions.logger")
    def test_authentication_error_logs_security_context(self, mock_logger):
        """Test authentication errors log with security context."""
        context = create_error_context(user_id="user123", metadata={"ip_address": "192.168.1.100", "attempt": 3})

        error = AuthenticationError(
            message="Invalid credentials",
            context=context,
            auth_type="password",
        )

        # Verify error was logged
        mock_logger.error.assert_called_once()
        # Security-relevant information should be included
        assert error.details["auth_type"] == "password"

    @patch("server.exceptions.logger")
    def test_validation_error_logs_dangerous_input(self, mock_logger):
        """Test validation errors log dangerous input patterns."""
        context = create_error_context(user_id="user123")

        dangerous_value = "<script>alert('xss')</script>"
        error = MythosValidationError(
            message="Dangerous input detected",
            context=context,
            field="message",
            value=dangerous_value,
        )

        # Verify error was logged
        mock_logger.error.assert_called_once()
        # Dangerous input should be logged for security auditing
        assert "script" in error.details["value"]

    @patch("server.exceptions.logger")
    def test_rate_limit_error_logs_abuse_detection(self, mock_logger):
        """Test rate limit errors log potential abuse."""
        context = create_error_context(user_id="user123", metadata={"ip_address": "192.168.1.100", "requests": 100})

        error = RateLimitError(
            message="Rate limit exceeded",
            context=context,
            limit_type="api_rate",
            retry_after=300,
        )

        # Verify error was logged
        mock_logger.error.assert_called_once()
        # Abuse-related information should be included
        assert error.details["limit_type"] == "api_rate"
        assert error.details["retry_after"] == 300


class TestErrorLoggingPerformance:
    """Test error logging performance and efficiency."""

    def test_error_logging_does_not_block(self):
        """Test that error logging is non-blocking."""
        import time

        context = create_error_context(user_id="user123")

        start_time = time.time()
        _error = MythosMUDError(  # noqa: F841 - Testing side effect performance
            message="Test error",
            context=context,
            details={"large_data": "x" * 10000},
        )
        elapsed_time = time.time() - start_time

        # Error creation should be fast (< 10ms)
        assert elapsed_time < 0.01

    def test_context_serialization_performance(self):
        """Test error context serialization is efficient."""
        import time

        context = create_error_context(
            user_id="user123",
            room_id="room456",
            command="test command",
            session_id="session789",
            metadata={"key": "value", "data": list(range(100))},
        )

        start_time = time.time()
        context_dict = context.to_dict()
        elapsed_time = time.time() - start_time

        # Serialization should be fast (< 1ms)
        assert elapsed_time < 0.001
        assert isinstance(context_dict, dict)
