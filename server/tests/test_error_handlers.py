"""
Tests for error handling and sanitization in MythosMUD.

These tests verify that error responses properly sanitize sensitive information
and prevent stack trace exposure to users.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.error_handlers import (
    _is_safe_detail_key,
    _sanitize_context,
    _sanitize_detail_value,
    create_error_response,
    sanitize_html_content,
    sanitize_text_content,
)
from server.exceptions import (
    DatabaseError,
    ErrorContext,
    MythosMUDError,
    ValidationError,
)


class TestErrorSanitization:
    """Test error sanitization functions."""

    def test_safe_detail_keys(self):
        """Test that safe detail keys are allowed."""
        safe_keys = [
            "auth_type",
            "operation",
            "table",
            "field",
            "value",
            "game_action",
            "config_key",
            "connection_type",
            "resource_type",
            "resource_id",
            "limit_type",
            "retry_after",
        ]

        for key in safe_keys:
            assert _is_safe_detail_key(key), f"Key '{key}' should be safe"

    def test_unsafe_detail_keys(self):
        """Test that unsafe detail keys are blocked."""
        unsafe_keys = [
            "password",
            "secret_key",
            "api_token",
            "credentials",
            "file_path",
            "sql_query",
            "stack_trace",
            "debug_info",
            "internal_data",
            "sensitive_info",
            "private_key",
        ]

        for key in unsafe_keys:
            assert not _is_safe_detail_key(key), f"Key '{key}' should be unsafe"

    def test_sanitize_string_values(self):
        """Test that string values are properly sanitized."""
        # Safe strings should pass through
        assert _sanitize_detail_value("normal message") == "normal message"
        assert _sanitize_detail_value("auth_type") == "auth_type"

        # Strings with sensitive patterns should be redacted
        assert _sanitize_detail_value("File: /etc/passwd") == "[REDACTED]"
        assert _sanitize_detail_value("Traceback (most recent call last):") == "[REDACTED]"
        # "line" is not in our sensitive patterns, so it should pass through
        # Note: bleach removes HTML tags, so <module> becomes just the text
        assert _sanitize_detail_value("line 42 in <module>") == "line 42 in "
        assert _sanitize_detail_value("C:\\Users\\admin\\secret.txt") == "[REDACTED]"

    def test_sanitize_dict_values(self):
        """Test that dictionary values are properly sanitized."""
        test_dict = {
            "operation": "safe_value",
            "password": "secret123",
            "file_path": "/etc/passwd",
            "field": "normal_value",
        }

        sanitized = _sanitize_detail_value(test_dict)

        # Only safe keys should be included (operation and field are in safe_keys)
        assert "operation" in sanitized
        assert "field" in sanitized

        # Unsafe keys should be excluded
        assert "password" not in sanitized
        assert "file_path" not in sanitized

    def test_sanitize_context(self):
        """Test that error context is properly sanitized."""
        context = ErrorContext(
            user_id="user123",
            room_id="room456",
            command="look",
            session_id="session789",
            request_id="req123",
            metadata={"safe_meta": "safe_value", "password": "secret123", "file_path": "/etc/passwd"},
        )

        sanitized = _sanitize_context(context)

        # Safe fields should be included
        assert sanitized["user_id"] == "user123"
        assert sanitized["room_id"] == "room456"
        assert sanitized["command"] == "look"
        assert sanitized["session_id"] == "session789"
        assert sanitized["request_id"] == "req123"

        # Metadata should be sanitized
        assert "safe_meta" in sanitized["metadata"]
        assert "password" not in sanitized["metadata"]
        assert "file_path" not in sanitized["metadata"]


class TestErrorResponseCreation:
    """Test error response creation with sanitization."""

    def test_create_error_response_without_details(self):
        """Test error response creation without detailed information."""
        error = ValidationError(
            message="Invalid input", context=ErrorContext(user_id="user123"), field="username", value="invalid@#$%"
        )

        response = create_error_response(error, include_details=False)

        # Should not include details
        assert response.details == {}
        assert response.error_type.value == "validation_error"
        assert response.message == "Invalid input"

    def test_create_error_response_with_safe_details(self):
        """Test error response creation with safe detailed information."""
        error = ValidationError(
            message="Invalid input", context=ErrorContext(user_id="user123"), field="username", value="invalid@#$%"
        )

        response = create_error_response(error, include_details=True)

        # Should include safe details
        assert "field" in response.details
        assert "value" in response.details
        assert "context" in response.details
        assert response.details["field"] == "username"
        assert response.details["value"] == "invalid@#$%"

    def test_create_error_response_with_unsafe_details(self):
        """Test error response creation with unsafe detailed information."""
        error = DatabaseError(
            message="Database error",
            context=ErrorContext(user_id="user123"),
            operation="SELECT",
            table="users",
            details={
                "sql_query": "SELECT * FROM users WHERE password = 'secret123'",
                "file_path": "/etc/database.conf",
                "stack_trace": "Traceback (most recent call last):",
                "safe_field": "safe_value",
            },
        )

        response = create_error_response(error, include_details=True)

        # Should only include safe details
        assert "safe_field" in response.details
        assert response.details["safe_field"] == "safe_value"

        # Unsafe details should be excluded
        assert "sql_query" not in response.details
        assert "file_path" not in response.details
        assert "stack_trace" not in response.details

    def test_create_error_response_with_sensitive_context(self):
        """Test error response creation with sensitive context information."""
        context = ErrorContext(
            user_id="user123",
            metadata={
                "password": "secret123",
                "api_key": "sk-1234567890abcdef",
                "file_path": "/etc/passwd",
                "safe_meta": "safe_value",
            },
        )

        error = MythosMUDError(
            message="Test error", context=context, details={"safe_detail": "safe_value", "password": "secret123"}
        )

        response = create_error_response(error, include_details=True)

        # Should include safe context fields
        assert "context" in response.details
        context_data = response.details["context"]
        assert context_data["user_id"] == "user123"

        # Should include safe metadata
        assert "safe_meta" in context_data["metadata"]
        assert context_data["metadata"]["safe_meta"] == "safe_value"

        # Should exclude sensitive metadata
        assert "password" not in context_data["metadata"]
        assert "api_key" not in context_data["metadata"]
        assert "file_path" not in context_data["metadata"]

        # Should include safe details
        assert "safe_detail" in response.details
        assert response.details["safe_detail"] == "safe_value"

        # Should exclude sensitive details
        assert "password" not in response.details


class TestErrorHandlerIntegration:
    """Test error handler integration with FastAPI."""

    def test_error_handler_registration(self):
        """Test that error handlers are properly registered."""
        app = FastAPI()

        # Import and register error handlers
        from server.error_handlers import register_error_handlers

        register_error_handlers(app)

        client = TestClient(app)

        # Create a test endpoint that raises an error
        @app.get("/test-error")
        def test_error():
            raise ValidationError("Test validation error", field="test_field")

        # Test that the error is handled properly
        response = client.get("/test-error")

        assert response.status_code == 400
        data = response.json()

        # Should not expose sensitive information
        assert "error" in data
        assert data["error"]["type"] == "validation_error"
        assert data["error"]["message"] == "Test validation error"

        # Should not include stack traces or sensitive details
        error_data = data["error"]
        assert "stack_trace" not in error_data
        assert "file_path" not in error_data
        assert "password" not in error_data


class TestBleachSanitization:
    """Test bleach-based sanitization functions."""

    def test_sanitize_html_content_basic(self):
        """Test basic HTML sanitization."""
        # Safe HTML should pass through
        safe_html = "<p>Hello <strong>world</strong></p>"
        sanitized = sanitize_html_content(safe_html)
        assert "<p>" in sanitized
        assert "<strong>" in sanitized
        assert "Hello" in sanitized
        assert "world" in sanitized

    def test_sanitize_html_content_remove_unsafe_tags(self):
        """Test that unsafe HTML tags are removed."""
        unsafe_html = "<script>alert('xss')</script><p>Hello</p>"
        sanitized = sanitize_html_content(unsafe_html)
        assert "<script>" not in sanitized
        # Bleach removes script tags but keeps the content
        assert "alert('xss')" in sanitized
        assert "<p>Hello</p>" in sanitized

    def test_sanitize_html_content_remove_unsafe_attributes(self):
        """Test that unsafe HTML attributes are removed."""
        unsafe_html = '<p onclick="alert(\'xss\')" class="safe">Hello</p>'
        sanitized = sanitize_html_content(unsafe_html)
        assert "onclick=" not in sanitized
        assert 'class="safe"' in sanitized
        assert "Hello" in sanitized

    def test_sanitize_html_content_custom_tags(self):
        """Test HTML sanitization with custom allowed tags."""
        html = "<div><span>Hello</span><script>alert('xss')</script></div>"
        sanitized = sanitize_html_content(html, allow_tags=["div", "span"])
        assert "<div>" in sanitized
        assert "<span>" in sanitized
        assert "<script>" not in sanitized
        # Bleach removes script tags but keeps the content
        assert "alert('xss')" in sanitized

    def test_sanitize_text_content_basic(self):
        """Test basic text sanitization."""
        # Plain text should pass through
        text = "Hello world"
        sanitized = sanitize_text_content(text)
        assert sanitized == "Hello world"

    def test_sanitize_text_content_remove_html(self):
        """Test that HTML is removed from text content."""
        text_with_html = "<p>Hello <script>alert('xss')</script> world</p>"
        sanitized = sanitize_text_content(text_with_html)
        assert "<p>" not in sanitized
        assert "<script>" not in sanitized
        # Bleach removes tags but keeps text content
        assert "Hello" in sanitized
        assert "alert('xss')" in sanitized
        assert "world" in sanitized

    def test_sanitize_text_content_length_limit(self):
        """Test that text content is limited to specified length."""
        long_text = "A" * 2000
        sanitized = sanitize_text_content(long_text, max_length=100)
        assert len(sanitized) == 103  # 100 + "..."
        assert sanitized.endswith("...")

    def test_sanitize_detail_value_with_html(self):
        """Test that _sanitize_detail_value handles HTML content."""
        html_content = "<script>alert('xss')</script>Hello world"
        sanitized = _sanitize_detail_value(html_content)
        assert "<script>" not in sanitized
        # The content contains "script" which triggers our redaction
        assert sanitized == "[REDACTED]"

    def test_sanitize_detail_value_with_sensitive_patterns(self):
        """Test that _sanitize_detail_value redacts sensitive patterns."""
        sensitive_content = "Traceback (most recent call last):\n  File '/etc/passwd'"
        sanitized = _sanitize_detail_value(sensitive_content)
        assert sanitized == "[REDACTED]"

    def test_sanitize_detail_value_with_mixed_content(self):
        """Test that _sanitize_detail_value handles mixed content properly."""
        mixed_content = "Hello <script>alert('xss')</script> world"
        sanitized = _sanitize_detail_value(mixed_content)
        # The content contains "script" which triggers our redaction
        assert sanitized == "[REDACTED]"
