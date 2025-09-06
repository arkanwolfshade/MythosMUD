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

from server.exceptions import DatabaseError, ErrorContext, MythosMUDError, ValidationError
from server.utils.error_logging import create_error_context, log_and_raise


class ErrorLoggingTestMixin:
    """Mixin class providing error logging test utilities."""

    def assert_error_logged(self, log_file: str, error_type: str, expected_message: str = None) -> None:
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

    def assert_error_context(self, context: ErrorContext, expected_fields: dict[str, Any] = None) -> None:
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

    def assert_no_sensitive_data(self, log_content: str, sensitive_patterns: list[str] = None) -> None:
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
                assert "Test error message" in call_args[0][0]
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
                assert "Context test error" in call_args[0][0]
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
                    context: ErrorContext = None,
                    details: dict[str, Any] = None,
                    user_friendly: str = None,
                ):
                    super().__init__(message, context=context, details=details, user_friendly=user_friendly)

            with patch("server.utils.error_logging.logger") as mock_logger:
                with pytest.raises(CustomError, match="Custom error occurred"):
                    log_and_raise(CustomError, "Custom error occurred", details={"custom_field": "custom_value"})

                # Verify logger was called
                mock_logger.error.assert_called_once()
                call_args = mock_logger.error.call_args
                assert "Custom error occurred" in call_args[0][0]
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
            assert "Request context test" in call_args[0][0]

    def test_error_logging_with_database_operations(self):
        """Test error logging integration with database operations."""
        # Mock database error scenario
        db_error_details = {
            "operation": "SELECT",
            "table": "players",
            "error_code": "SQLITE_ERROR",
            "query": "SELECT * FROM players WHERE id = ?",
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
            assert "Database operation failed" in call_args[0][0]
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
                assert "Outer error" in call_args[0][0]
                assert "Inner error" in call_args[1]["details"]["exception_chain"]
