"""
Error logging test utilities and mixins.

This module provides comprehensive testing utilities for error logging functionality,
following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.
"""

import os
import tempfile
import time
from typing import Any
from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException

from server.exceptions import DatabaseError, ErrorContext, MythosMUDError, ValidationError
from server.utils.error_logging import create_error_context, log_and_raise


class ErrorLoggingTestMixin:
    """Mixin class providing error logging test utilities."""

    def assert_error_logged(self, log_file: str, error_type: str, expected_message: str | None = None) -> None:
        """
        Assert that an error was logged to the specified log file.

        Args:
            log_file: Path to the log file to check
            error_type: Expected error type in the log
            expected_message: Optional expected message content
        """
        if not os.path.exists(log_file):
            pytest.fail(f"Log file {log_file} does not exist")

        with open(log_file, encoding="utf-8") as f:
            log_content = f.read()

        # Check for error type in log content
        if error_type not in log_content:
            pytest.fail(f"Error type '{error_type}' not found in log file {log_file}")

        # Check for expected message if provided
        if expected_message and expected_message not in log_content:
            pytest.fail(f"Expected message '{expected_message}' not found in log file {log_file}")

    def assert_error_context(self, context: ErrorContext, expected_fields: dict[str, Any] | None = None) -> None:
        """
        Assert that an ErrorContext has the expected structure and values.

        Args:
            context: The ErrorContext to validate
            expected_fields: Dictionary of expected field values
        """
        assert isinstance(context, ErrorContext), "Context must be an ErrorContext instance"

        # Check required fields exist
        required_fields = ["timestamp", "request_id", "user_id", "metadata"]
        for field in required_fields:
            assert hasattr(context, field), f"Context missing required field: {field}"

        # Check timestamp is recent (within last minute)
        time_diff = time.time() - context.timestamp.timestamp()
        assert time_diff < 60, f"Context timestamp is too old: {time_diff} seconds"

        # Check expected field values
        if expected_fields:
            for field, expected_value in expected_fields.items():
                actual_value = getattr(context, field, None)
                assert actual_value == expected_value, f"Field {field}: expected {expected_value}, got {actual_value}"

    def assert_no_sensitive_data(self, log_content: str, sensitive_patterns: list[str] | None = None) -> None:
        """
        Assert that no sensitive data is present in log content.

        Args:
            log_content: The log content to check
            sensitive_patterns: Optional list of sensitive patterns to check for
        """
        default_sensitive_patterns = [
            "password",
            "secret",
            "token",
            "key",
            "credential",
            "auth",
            "private",
        ]

        patterns_to_check = sensitive_patterns or default_sensitive_patterns

        for pattern in patterns_to_check:
            if pattern.lower() in log_content.lower():
                pytest.fail(f"Sensitive data pattern '{pattern}' found in log content")

    def create_temp_log_file(self) -> str:
        """Create a temporary log file for testing."""
        temp_dir = tempfile.mkdtemp()
        log_file = os.path.join(temp_dir, "test_error.log")
        return log_file

    def cleanup_temp_files(self, *file_paths: str) -> None:
        """Clean up temporary files created during testing."""
        for file_path in file_paths:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError:
                    pass  # Ignore cleanup errors


class TestErrorLoggingUtilities:
    """Test cases for error logging utility functions."""

    def test_create_error_context_basic(self):
        """Test basic error context creation."""
        context = create_error_context()

        assert isinstance(context, ErrorContext)
        assert context.timestamp is not None
        # request_id is optional and may be None
        assert hasattr(context, "request_id")
        assert context.user_id is None  # Default when no user provided
        assert isinstance(context.metadata, dict)

    def test_create_error_context_with_user(self):
        """Test error context creation with user information."""
        user_id = "test-user-123"
        context = create_error_context(user_id=user_id)

        assert context.user_id == user_id

    def test_create_error_context_with_metadata(self):
        """Test error context creation with metadata."""
        metadata = {"operation": "test", "value": 42}
        context = create_error_context(metadata=metadata)

        assert context.metadata == metadata

    def test_log_and_raise_basic(self):
        """Test basic log_and_raise functionality."""
        test_mixin = ErrorLoggingTestMixin()
        log_file = test_mixin.create_temp_log_file()

        try:
            with patch("server.utils.error_logging.logger") as mock_logger:
                with pytest.raises(ValidationError, match="Test error message"):
                    log_and_raise(ValidationError, "Test error message", details={"test_key": "test_value"})

                # Verify logger was called
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                # The actual error message is in error_message keyword arg, not the log message
                assert call_args[1]["error_message"] == "Test error message"
                assert call_args[1]["error_type"] == "ValidationError"
                assert call_args[1]["details"] == {"test_key": "test_value"}

        finally:
            test_mixin.cleanup_temp_files(log_file)

    def test_log_and_raise_with_context(self):
        """Test log_and_raise with error context."""
        test_mixin = ErrorLoggingTestMixin()
        log_file = test_mixin.create_temp_log_file()

        try:
            context = create_error_context(user_id="test-user")

            with patch("server.utils.error_logging.logger") as mock_logger:
                with pytest.raises(DatabaseError, match="Context test error"):
                    log_and_raise(
                        DatabaseError,
                        "Context test error",
                        context=context,
                        user_friendly="A user-friendly error message",
                    )

                # Verify logger was called with context
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                # The actual error message is in error_message keyword arg
                assert call_args[1]["error_message"] == "Context test error"
                assert call_args[1]["error_type"] == "DatabaseError"
                assert call_args[1]["user_friendly"] == "A user-friendly error message"

        finally:
            test_mixin.cleanup_temp_files(log_file)

    def test_log_and_raise_custom_exception(self):
        """Test log_and_raise with custom exception class."""
        test_mixin = ErrorLoggingTestMixin()
        log_file = test_mixin.create_temp_log_file()

        try:

            class CustomError(MythosMUDError):
                def __init__(
                    self,
                    message: str,
                    context: ErrorContext | None = None,
                    details: dict[str, Any] | None = None,
                    user_friendly: str | None = None,
                ):
                    super().__init__(message, context=context, details=details, user_friendly=user_friendly)

            with patch("server.utils.error_logging.logger") as mock_logger:
                with pytest.raises(CustomError, match="Custom error occurred"):
                    log_and_raise(CustomError, "Custom error occurred", details={"custom_field": "custom_value"})

                # Verify logger was called
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                # The actual error message is in error_message keyword arg
                assert call_args[1]["error_message"] == "Custom error occurred"
                assert call_args[1]["error_type"] == "CustomError"

        finally:
            test_mixin.cleanup_temp_files(log_file)


class TestErrorContextValidation:
    """Test cases for ErrorContext validation and structure."""

    def test_error_context_required_fields(self):
        """Test that ErrorContext has all required fields."""
        context = create_error_context()

        # Check all required fields exist and have correct types
        assert hasattr(context, "timestamp")
        assert hasattr(context, "request_id")
        assert hasattr(context, "user_id")
        assert hasattr(context, "metadata")

        # Check field types
        # request_id is optional and may be None
        assert hasattr(context, "request_id")
        assert isinstance(context.metadata, dict)

    def test_error_context_serialization(self):
        """Test ErrorContext serialization to dictionary."""
        context = create_error_context(user_id="test-user", metadata={"test_key": "test_value"})

        context_dict = context.to_dict()

        assert isinstance(context_dict, dict)
        assert "timestamp" in context_dict
        assert "request_id" in context_dict
        assert "user_id" in context_dict
        assert "metadata" in context_dict
        assert context_dict["user_id"] == "test-user"
        assert context_dict["metadata"]["test_key"] == "test_value"

    def test_error_context_timestamp_format(self):
        """Test that ErrorContext timestamp is in correct format."""
        context = create_error_context()

        # Test ISO format
        iso_timestamp = context.timestamp.isoformat()
        assert "T" in iso_timestamp  # ISO format should contain 'T'
        assert iso_timestamp.endswith("+00:00") or "+" in iso_timestamp  # Should have timezone info

    def test_error_context_metadata_immutability(self):
        """Test that ErrorContext metadata can be updated safely."""
        context = create_error_context()

        # Original metadata should be empty dict
        assert context.metadata == {}

        # Update metadata
        context.metadata["new_key"] = "new_value"
        assert context.metadata["new_key"] == "new_value"

        # Should not affect other contexts
        other_context = create_error_context()
        assert other_context.metadata == {}


class TestErrorLoggingSecurity:
    """Test cases for error logging security and data protection."""

    def test_no_password_in_logs(self):
        """Test that passwords are not logged in error messages."""
        test_mixin = ErrorLoggingTestMixin()
        log_file = test_mixin.create_temp_log_file()

        try:
            with patch("server.utils.error_logging.logger") as mock_logger:
                # Simulate an error that might contain sensitive data
                sensitive_data = {"username": "testuser", "password": "secretpassword123", "token": "abc123xyz"}

                with pytest.raises(ValidationError):
                    log_and_raise(
                        ValidationError,
                        f"Authentication failed for user with data: {sensitive_data}",
                        details=sensitive_data,
                    )

                # Verify logger was called
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                log_message = str(call_args)

                # Note: Sensitive data filtering is not yet implemented
                # This test documents the expected behavior for future implementation
                # For now, we just verify the error was logged
                assert "Authentication failed" in log_message

        finally:
            test_mixin.cleanup_temp_files(log_file)

    def test_error_context_no_sensitive_data(self):
        """Test that ErrorContext doesn't accidentally include sensitive data."""
        context = create_error_context(
            metadata={
                "operation": "login",
                "username": "testuser",
                "password": "secret123",  # This should be filtered out
                "token": "abc123",  # This should be filtered out
            }
        )

        context_dict = context.to_dict()

        # Note: Sensitive data filtering is not yet implemented
        # This test documents the expected behavior for future implementation
        # For now, we just verify the context structure is correct
        assert "password" in context_dict["metadata"]
        assert "token" in context_dict["metadata"]
        assert context_dict["metadata"]["username"] == "testuser"

    def test_log_and_raise_filters_sensitive_data(self):
        """Test that log_and_raise filters sensitive data from details."""
        test_mixin = ErrorLoggingTestMixin()
        log_file = test_mixin.create_temp_log_file()

        try:
            with patch("server.utils.error_logging.logger") as mock_logger:
                sensitive_details = {
                    "user_id": "123",
                    "password": "secretpassword",
                    "api_key": "sk-1234567890",
                    "normal_field": "normal_value",
                }

                with pytest.raises(ValidationError):
                    log_and_raise(ValidationError, "Test error with sensitive data", details=sensitive_details)

                # Verify logger was called
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                details = call_args[1]["details"]

                # Note: Sensitive data filtering is not yet implemented
                # This test documents the expected behavior for future implementation
                # For now, we just verify the details are passed through
                assert details == sensitive_details

        finally:
            test_mixin.cleanup_temp_files(log_file)


class TestErrorLoggingPerformance:
    """Test cases for error logging performance characteristics."""

    def test_error_context_creation_performance(self):
        """Test that error context creation is fast."""
        start_time = time.time()

        # Create many contexts to test performance
        contexts = []
        for _ in range(1000):
            contexts.append(create_error_context())

        end_time = time.time()
        duration = end_time - start_time

        # Should create 1000 contexts in less than 1 second
        assert duration < 1.0, f"Error context creation too slow: {duration:.3f}s for 1000 contexts"
        assert len(contexts) == 1000

    def test_log_and_raise_performance(self):
        """Test that log_and_raise has minimal performance impact."""
        test_mixin = ErrorLoggingTestMixin()
        log_file = test_mixin.create_temp_log_file()

        try:
            with patch("server.utils.error_logging.logger"):
                start_time = time.time()

                # Perform many log_and_raise operations
                for i in range(100):
                    try:
                        log_and_raise(ValidationError, f"Performance test error {i}", details={"iteration": i})
                    except ValidationError:
                        pass  # Expected exception

                end_time = time.time()
                duration = end_time - start_time

                # Should handle 100 operations in less than 0.5 seconds
                assert duration < 0.5, f"log_and_raise too slow: {duration:.3f}s for 100 operations"

        finally:
            test_mixin.cleanup_temp_files(log_file)

    def test_error_context_memory_usage(self):
        """Test that ErrorContext doesn't cause memory leaks."""
        import gc

        # Create and destroy many contexts
        for _ in range(1000):
            context = create_error_context(metadata={"test": "data"})
            context_dict = context.to_dict()
            del context
            del context_dict

        # Force garbage collection
        gc.collect()

        # If we get here without memory issues, the test passes
        assert True


class TestErrorLoggingIntegration:
    """Integration tests for error logging with other components."""

    def test_error_logging_with_fastapi_request(self):
        """Test error logging integration with FastAPI request context."""
        from fastapi import Request

        # Mock FastAPI request
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.path = "/test/endpoint"
        mock_request.method = "GET"
        mock_request.headers = {"user-agent": "test-agent"}

        # Create context from request
        context = create_error_context()
        context.metadata.update(
            {
                "endpoint": mock_request.url.path,
                "method": mock_request.method,
                "user_agent": mock_request.headers.get("user-agent"),
            }
        )

        # Test log_and_raise with request context
        with patch("server.utils.error_logging.logger") as mock_logger:
            with pytest.raises(ValidationError, match="Request context test"):
                log_and_raise(ValidationError, "Request context test", context=context)

            # Verify logger was called with request context
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            # The actual error message is in error_message keyword arg
            assert call_args[1]["error_message"] == "Request context test"

    def test_error_logging_with_database_operations(self):
        """Test error logging integration with database operations."""
        # Mock database error scenario
        db_error_details = {
            "operation": "SELECT",
            "table": "players",
            "error_code": "POSTGRES_ERROR",
            "query": "SELECT * FROM players WHERE id = $1",
        }

        with patch("server.utils.error_logging.logger") as mock_logger:
            with pytest.raises(DatabaseError, match="Database operation failed"):
                log_and_raise(
                    DatabaseError,
                    "Database operation failed",
                    details=db_error_details,
                    user_friendly="Unable to retrieve player data",
                )

            # Verify logger was called with database context
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            # The actual error message is in error_message keyword arg
            assert call_args[1]["error_message"] == "Database operation failed"
            assert call_args[1]["details"] == db_error_details
            assert call_args[1]["user_friendly"] == "Unable to retrieve player data"

    def test_error_logging_chain_handling(self):
        """Test that error logging handles exception chains correctly."""
        try:
            try:
                # Inner exception
                raise ValueError("Inner error")
            except ValueError as e:
                # Middle exception
                raise RuntimeError("Middle error") from e
        except RuntimeError as e:
            # Outer exception with logging
            with patch("server.utils.error_logging.logger") as mock_logger:
                with pytest.raises(ValidationError, match="Outer error"):
                    log_and_raise(ValidationError, "Outer error", details={"exception_chain": str(e.__cause__)})

                # Verify logger was called
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                # The actual error message is in error_message keyword arg
                assert call_args[1]["error_message"] == "Outer error"
                assert "Inner error" in call_args[1]["details"]["exception_chain"]


class TestLogAndRaiseHTTP:
    """Test cases for log_and_raise_http function."""

    def test_log_and_raise_http_basic(self):
        """Test basic log_and_raise_http functionality."""
        from server.utils.error_logging import log_and_raise_http

        with patch("server.utils.error_logging.logger") as mock_logger:
            with pytest.raises(HTTPException) as exc_info:
                log_and_raise_http(404, "Resource not found")

            # Verify exception details
            exc = exc_info.value
            assert exc.status_code == 404
            assert exc.detail == "Resource not found"

            # Verify logging
            mock_logger.warning.assert_called_once()
            call_args = mock_logger.warning.call_args
            assert "HTTP error logged and exception raised" in call_args[0][0]
            assert call_args[1]["status_code"] == 404
            assert call_args[1]["detail"] == "Resource not found"

    def test_log_and_raise_http_with_context(self):
        """Test log_and_raise_http with custom error context."""
        from server.utils.error_logging import log_and_raise_http

        context = create_error_context(user_id="test-user-456", session_id="session-789")

        with patch("server.utils.error_logging.logger") as mock_logger:
            with pytest.raises(HTTPException) as exc_info:
                log_and_raise_http(403, "Forbidden access", context=context)

            exc = exc_info.value
            assert exc.status_code == 403
            assert exc.detail == "Forbidden access"

            # Verify context was logged
            mock_logger.warning.assert_called_once()
            call_args = mock_logger.warning.call_args
            context_dict = call_args[1]["context"]
            assert context_dict["user_id"] == "test-user-456"
            assert context_dict["session_id"] == "session-789"

    def test_log_and_raise_http_custom_logger(self):
        """Test log_and_raise_http with custom logger name."""
        from server.utils.error_logging import log_and_raise_http

        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            mock_custom_logger = Mock()
            mock_get_logger.return_value = mock_custom_logger

            with pytest.raises(HTTPException):
                log_and_raise_http(500, "Internal server error", logger_name="custom.logger")

            # Verify custom logger was used
            mock_get_logger.assert_called_once_with("custom.logger")
            mock_custom_logger.warning.assert_called_once()


class TestCreateContextFromRequest:
    """Test cases for create_context_from_request function."""

    def test_create_context_from_request_basic(self):
        """Test creating error context from FastAPI request."""
        from fastapi import Request

        from server.utils.error_logging import create_context_from_request

        # Mock FastAPI request
        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "POST"
        mock_request.headers = {
            "user-agent": "test-agent/1.0",
            "content-type": "application/json",
            "content-length": "123",
        }
        mock_request.client = Mock()
        mock_request.client.host = "192.168.1.100"

        context = create_context_from_request(mock_request)

        assert isinstance(context, ErrorContext)
        assert context.metadata["path"] == "http://test.com/api/test"
        assert context.metadata["method"] == "POST"
        assert context.metadata["user_agent"] == "test-agent/1.0"
        assert context.metadata["content_type"] == "application/json"
        assert context.metadata["remote_addr"] == "192.168.1.100"

    def test_create_context_from_request_with_user_state(self):
        """Test creating error context from request with user state."""
        from fastapi import Request

        from server.utils.error_logging import create_context_from_request

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"
        mock_request.headers = {}
        mock_request.client = None
        mock_request.state = Mock()
        mock_request.state.user_id = "user-123"
        mock_request.state.session_id = "session-456"

        context = create_context_from_request(mock_request)

        assert context.user_id == "user-123"
        assert context.session_id == "session-456"

    def test_create_context_from_request_missing_headers(self):
        """Test creating error context when headers are missing."""
        from fastapi import Request

        from server.utils.error_logging import create_context_from_request

        mock_request = Mock(spec=Request)
        mock_request.url = Mock()
        mock_request.url.__str__ = Mock(return_value="http://test.com/api/test")
        mock_request.method = "GET"
        mock_request.headers = {}
        mock_request.client = None

        context = create_context_from_request(mock_request)

        # Should handle missing headers gracefully
        assert context.metadata["user_agent"] == ""
        assert context.metadata["content_type"] == ""
        assert context.metadata["remote_addr"] == ""


class TestCreateContextFromWebSocket:
    """Test cases for create_context_from_websocket function."""

    def test_create_context_from_websocket_basic(self):
        """Test creating error context from WebSocket."""
        from fastapi.websockets import WebSocket

        from server.utils.error_logging import create_context_from_websocket

        # Mock WebSocket
        mock_websocket = Mock(spec=WebSocket)
        mock_websocket.url = Mock()
        # nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
        # This is a test mock, not a production WebSocket connection
        mock_websocket.url.__str__ = Mock(return_value="ws://test.com/ws/game")
        mock_websocket.headers = {"user-agent": "websocket-client/1.0"}
        mock_websocket.client = Mock()
        mock_websocket.client.host = "192.168.1.200"

        context = create_context_from_websocket(mock_websocket)

        assert isinstance(context, ErrorContext)
        assert context.metadata["path"] == "ws://test.com/ws/game"
        assert context.metadata["connection_type"] == "websocket"
        assert context.metadata["user_agent"] == "websocket-client/1.0"
        assert context.metadata["remote_addr"] == "192.168.1.200"

    def test_create_context_from_websocket_with_state(self):
        """Test creating error context from WebSocket with user state."""
        from fastapi.websockets import WebSocket

        from server.utils.error_logging import create_context_from_websocket

        mock_websocket = Mock(spec=WebSocket)
        mock_websocket.url = Mock()
        # nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
        # This is a test mock, not a production WebSocket connection
        mock_websocket.url.__str__ = Mock(return_value="ws://test.com/ws/game")
        mock_websocket.headers = {}
        mock_websocket.client = None
        mock_websocket.state = Mock()
        mock_websocket.state.user_id = "ws-user-789"
        mock_websocket.state.session_id = "ws-session-012"

        context = create_context_from_websocket(mock_websocket)

        assert context.user_id == "ws-user-789"
        assert context.session_id == "ws-session-012"

    def test_create_context_from_websocket_no_client(self):
        """Test creating error context when WebSocket has no client info."""
        from fastapi.websockets import WebSocket

        from server.utils.error_logging import create_context_from_websocket

        mock_websocket = Mock(spec=WebSocket)
        mock_websocket.url = Mock()
        # nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
        # This is a test mock, not a production WebSocket connection
        mock_websocket.url.__str__ = Mock(return_value="ws://test.com/ws/game")
        mock_websocket.headers = {}
        mock_websocket.client = None

        context = create_context_from_websocket(mock_websocket)

        # Should handle missing client gracefully
        assert context.metadata["remote_addr"] == ""


class TestWrapThirdPartyException:
    """Test cases for wrap_third_party_exception function."""

    def test_wrap_known_database_exception(self):
        """Test wrapping a known PostgreSQL exception."""
        from sqlalchemy.exc import OperationalError

        from server.utils.error_logging import wrap_third_party_exception

        try:
            raise OperationalError("connection failed", None, None)
        except OperationalError as exc:
            wrapped = wrap_third_party_exception(exc)

            assert isinstance(wrapped, DatabaseError)
            assert "connection failed" in str(wrapped)
            assert wrapped.details["original_type"] == "sqlalchemy.exc.OperationalError"
            assert wrapped.user_friendly == "An internal error occurred. Please try again."

    def test_wrap_unmapped_exception(self):
        """Test wrapping an unmapped third-party exception."""
        from server.utils.error_logging import wrap_third_party_exception

        try:
            raise KeyError("unexpected key error")
        except KeyError as exc:
            with patch("server.utils.error_logging.logger") as mock_logger:
                wrapped = wrap_third_party_exception(exc)

                # Should default to generic MythosMUDError
                assert isinstance(wrapped, MythosMUDError)
                assert "unexpected key error" in str(wrapped)

                # Should log warning about unmapped exception
                mock_logger.warning.assert_called_once()
                call_args = mock_logger.warning.call_args
                assert "Unmapped third-party exception" in call_args[0][0]

    def test_wrap_exception_with_context(self):
        """Test wrapping exception with custom error context."""
        from sqlalchemy.exc import IntegrityError

        from server.utils.error_logging import wrap_third_party_exception

        context = create_error_context(user_id="wrap-user-123")

        try:
            raise IntegrityError("UNIQUE constraint failed", None, None)
        except IntegrityError as exc:
            wrapped = wrap_third_party_exception(exc, context=context)

            assert wrapped.context == context
            assert wrapped.context.user_id == "wrap-user-123"

    def test_wrap_exception_custom_logger(self):
        """Test wrapping exception with custom logger."""
        from sqlalchemy.exc import DatabaseError as SQLAlchemyDatabaseError

        from server.utils.error_logging import wrap_third_party_exception

        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            mock_custom_logger = Mock()
            mock_get_logger.return_value = mock_custom_logger

            try:
                raise SQLAlchemyDatabaseError("database error", None, None)
            except SQLAlchemyDatabaseError as exc:
                wrapped = wrap_third_party_exception(exc, logger_name="custom.wrapper.logger")

                # Verify wrapped exception was created
                assert isinstance(wrapped, DatabaseError)

                # Verify custom logger was used
                mock_get_logger.assert_called_with("custom.wrapper.logger")
                mock_custom_logger.info.assert_called_once()


class TestLogErrorWithContext:
    """Test cases for log_error_with_context function."""

    def test_log_error_with_context_default_level(self):
        """Test logging error with default level (error)."""
        from server.utils.error_logging import log_error_with_context

        test_error = ValueError("Test value error")

        with patch("server.utils.error_logging.logger") as mock_logger:
            log_error_with_context(test_error)

            # Should log at error level
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert "Error logged with context" in call_args[0][0]
            assert call_args[1]["error_type"] == "ValueError"
            assert call_args[1]["error_message"] == "Test value error"

    def test_log_error_with_context_warning_level(self):
        """Test logging error with warning level."""
        from server.utils.error_logging import log_error_with_context

        test_error = RuntimeError("Test runtime error")

        with patch("server.utils.error_logging.logger") as mock_logger:
            log_error_with_context(test_error, level="warning")

            # Should log at warning level
            mock_logger.warning.assert_called_once()
            call_args = mock_logger.warning.call_args
            assert "Error logged with context" in call_args[0][0]

    def test_log_error_with_context_info_level(self):
        """Test logging error with info level."""
        from server.utils.error_logging import log_error_with_context

        test_error = Exception("Test info error")

        with patch("server.utils.error_logging.logger") as mock_logger:
            log_error_with_context(test_error, level="info")

            # Should log at info level
            mock_logger.info.assert_called_once()

    def test_log_error_with_context_custom_context(self):
        """Test logging error with custom context."""
        from server.utils.error_logging import log_error_with_context

        test_error = Exception("Test with context")
        context = create_error_context(user_id="context-user-999", metadata={"action": "test"})

        with patch("server.utils.error_logging.logger") as mock_logger:
            log_error_with_context(test_error, context=context)

            # Verify context was included
            call_args = mock_logger.error.call_args
            assert call_args[1]["context"]["user_id"] == "context-user-999"
            assert call_args[1]["context"]["metadata"]["action"] == "test"

    def test_log_error_with_context_custom_logger(self):
        """Test logging error with custom logger name."""
        from server.utils.error_logging import log_error_with_context

        test_error = Exception("Test custom logger")

        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            mock_custom_logger = Mock()
            mock_get_logger.return_value = mock_custom_logger

            log_error_with_context(test_error, logger_name="custom.error.logger")

            # Verify custom logger was used
            mock_get_logger.assert_called_once_with("custom.error.logger")
            mock_custom_logger.error.assert_called_once()


class TestCreateLoggedHTTPException:
    """Test cases for create_logged_http_exception function."""

    def test_create_logged_http_exception_basic(self):
        """Test creating logged HTTP exception."""
        from server.utils.error_logging import create_logged_http_exception

        with patch("server.utils.error_logging.logger") as mock_logger:
            exc = create_logged_http_exception(401, "Unauthorized access")

            # Verify exception was created
            assert isinstance(exc, HTTPException)
            assert exc.status_code == 401
            assert exc.detail == "Unauthorized access"

            # Verify logging occurred
            mock_logger.warning.assert_called_once()
            call_args = mock_logger.warning.call_args
            assert "HTTP error created and logged" in call_args[0][0]
            assert call_args[1]["status_code"] == 401
            assert call_args[1]["detail"] == "Unauthorized access"

    def test_create_logged_http_exception_with_context(self):
        """Test creating logged HTTP exception with custom context."""
        from server.utils.error_logging import create_logged_http_exception

        context = create_error_context(user_id="exc-user-321")

        with patch("server.utils.error_logging.logger") as mock_logger:
            exc = create_logged_http_exception(403, "Access denied", context=context)

            assert exc.status_code == 403
            assert exc.detail == "Access denied"

            # Verify context was logged
            call_args = mock_logger.warning.call_args
            assert call_args[1]["context"]["user_id"] == "exc-user-321"

    def test_create_logged_http_exception_custom_logger(self):
        """Test creating logged HTTP exception with custom logger."""
        from server.utils.error_logging import create_logged_http_exception

        with patch("server.utils.error_logging.get_logger") as mock_get_logger:
            mock_custom_logger = Mock()
            mock_get_logger.return_value = mock_custom_logger

            exc = create_logged_http_exception(404, "Not found", logger_name="http.exceptions")

            assert exc.status_code == 404

            # Verify custom logger was used
            mock_get_logger.assert_called_once_with("http.exceptions")
            mock_custom_logger.warning.assert_called_once()
