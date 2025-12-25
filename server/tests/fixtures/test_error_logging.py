"""
Error logging test utilities and mixins.

This module provides comprehensive testing utilities for error logging functionality,
following the academic rigor outlined in the Pnakotic Manuscripts of Testing Methodology.

CRITICAL: This file contains TEST UTILITIES ONLY, not test classes.

- DO NOT add test classes (TestErrorLoggingUtilities, etc.) to this file
- Test classes belong in server/tests/unit/utils/test_error_logging.py
- This file should only contain utility classes and helper functions for other tests
- Test utilities (like ErrorLoggingTestMixin) should NOT be tested themselves

If you need to test error logging functionality, add tests to:
  server/tests/unit/utils/test_error_logging.py
"""

import os
import tempfile
import time
from typing import Any

import pytest

from server.exceptions import ErrorContext


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


# Export only the mixin - test classes have been moved to server/tests/unit/utils/test_error_logging.py
__all__ = ["ErrorLoggingTestMixin"]
