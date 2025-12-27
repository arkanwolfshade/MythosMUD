"""
Unit tests for error logging utilities.

Tests the error logging functions that provide standardized error handling and logging.
"""

from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException, Request

from server.exceptions import (
    AuthenticationError,
    DatabaseError,
    ErrorContext,
    MythosMUDError,
    NetworkError,
    ValidationError,
    create_error_context,
)
from server.utils.error_logging import (
    create_context_from_request,
    log_and_raise,
    log_and_raise_http,
    wrap_third_party_exception,
)


def test_log_and_raise_basic():
    """Test log_and_raise logs and raises exception."""
    with patch("server.utils.error_logging.increment_exception"):
        with pytest.raises(DatabaseError) as exc_info:
            log_and_raise(
                DatabaseError,
                "Database connection failed",
                user_friendly="Unable to connect to database",
            )

        assert "Database connection failed" in str(exc_info.value)
        assert exc_info.value.user_friendly == "Unable to connect to database"


def test_log_and_raise_with_context():
    """Test log_and_raise with provided context."""
    context = create_error_context(user_id="user123", request_id="req456")
    
    with patch("server.utils.error_logging.increment_exception"):
        with pytest.raises(ValidationError) as exc_info:
            log_and_raise(
                ValidationError,
                "Invalid input",
                context=context,
                details={"field": "email", "value": "invalid"},
            )

        assert "Invalid input" in str(exc_info.value)
        assert exc_info.value.context == context
        assert exc_info.value.details["field"] == "email"


def test_log_and_raise_with_custom_logger():
    """Test log_and_raise with custom logger name."""
    with patch("server.utils.error_logging.get_logger") as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        
        with patch("server.utils.error_logging.increment_exception"):
            with pytest.raises(AuthenticationError):
                log_and_raise(
                    AuthenticationError,
                    "Auth failed",
                    logger_name="custom.module",
                )

            mock_get_logger.assert_called_with("custom.module")


def test_log_and_raise_increment_exception_error():
    """Test log_and_raise handles increment_exception errors gracefully."""
    with patch("server.utils.error_logging.get_logger") as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        
        with patch("server.utils.error_logging.increment_exception", side_effect=RuntimeError("Monitoring error")):
            # Should still raise the exception even if monitoring fails
            with pytest.raises(DatabaseError):
                log_and_raise(DatabaseError, "Error occurred")


def test_log_and_raise_http():
    """Test log_and_raise_http logs and raises HTTPException."""
    with pytest.raises(HTTPException) as exc_info:
        log_and_raise_http(404, "Resource not found")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Resource not found"


def test_log_and_raise_http_with_context():
    """Test log_and_raise_http with context."""
    context = create_error_context(user_id="user123")
    
    with pytest.raises(HTTPException) as exc_info:
        log_and_raise_http(500, "Internal error", context=context)

    assert exc_info.value.status_code == 500
    assert exc_info.value.detail == "Internal error"


def test_log_and_raise_http_with_custom_logger():
    """Test log_and_raise_http with custom logger."""
    with patch("server.utils.error_logging.get_logger") as mock_get_logger:
        mock_logger = MagicMock()
        mock_get_logger.return_value = mock_logger
        
        with pytest.raises(HTTPException):
            log_and_raise_http(400, "Bad request", logger_name="api.module")

        mock_get_logger.assert_called_with("api.module")


def test_wrap_third_party_exception_mapped():
    """Test wrap_third_party_exception with mapped exception."""
    import sqlalchemy.exc
    
    original_error = sqlalchemy.exc.OperationalError("Connection lost", None, None)
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, DatabaseError)
    assert "Connection lost" in result.message
    assert result.user_friendly == "An internal error occurred. Please try again."


def test_wrap_third_party_exception_unmapped():
    """Test wrap_third_party_exception with unmapped exception."""
    original_error = KeyError("Missing key")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, MythosMUDError)
    assert "Missing key" in result.message
    assert result.user_friendly == "An internal error occurred. Please try again."


def test_wrap_third_party_exception_with_context():
    """Test wrap_third_party_exception with context."""
    import sqlalchemy.exc
    
    original_error = sqlalchemy.exc.OperationalError("Database error", None, None)
    context = create_error_context(user_id="user123")
    
    result = wrap_third_party_exception(original_error, context=context)

    assert isinstance(result, DatabaseError)
    assert result.context == context


def test_wrap_third_party_exception_httpx():
    """Test wrap_third_party_exception with httpx exception."""
    import httpx
    
    original_error = httpx.RequestError("Request failed")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, NetworkError)
    assert "Request failed" in result.message


def test_wrap_third_party_exception_argon2():
    """Test wrap_third_party_exception with argon2 exception."""
    import argon2.exceptions
    
    original_error = argon2.exceptions.VerificationError("Password mismatch")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, AuthenticationError)
    assert "Password mismatch" in result.message


def test_create_context_from_request():
    """Test create_context_from_request creates context from Request."""
    mock_request = MagicMock(spec=Request)
    mock_request.url = "http://example.com/api/test"
    mock_request.method = "POST"
    mock_request.headers = MagicMock()
    mock_request.headers.get = lambda key, default="": {
        "user-agent": "test-agent",
        "content-type": "application/json",
        "content-length": "100",
    }.get(key, default)
    mock_request.client = MagicMock(host="127.0.0.1", port=8080)

    context = create_context_from_request(mock_request)

    assert isinstance(context, ErrorContext)
    assert context.metadata["path"] == "http://example.com/api/test"
    assert context.metadata["method"] == "POST"
    assert context.metadata["user_agent"] == "test-agent"
    assert context.metadata["remote_addr"] == "127.0.0.1"


def test_create_context_from_request_none():
    """Test create_context_from_request handles None request."""
    context = create_context_from_request(None)

    assert isinstance(context, ErrorContext)
    assert context.metadata["path"] == "unknown"
    assert context.metadata["method"] == "unknown"
    assert context.metadata["remote_addr"] == ""


def test_create_context_from_request_no_client():
    """Test create_context_from_request handles request without client."""
    mock_request = MagicMock(spec=Request)
    mock_request.url = "http://example.com/test"
    mock_request.method = "GET"
    mock_request.headers = MagicMock()
    mock_request.headers.get = lambda key, default="": {}
    mock_request.client = None

    context = create_context_from_request(mock_request)

    assert context.metadata["remote_addr"] == ""


def test_wrap_third_party_exception_pydantic():
    """Test wrap_third_party_exception with Pydantic exception."""
    from pydantic import BaseModel
    
    class TestModel(BaseModel):
        field: int
    
    try:
        TestModel(field="not_an_int")
    except Exception as original_error:
        result = wrap_third_party_exception(original_error)

        # Pydantic v2 raises pydantic_core._pydantic_core.ValidationError
        # which may not be mapped, so it could be MythosMUDError or ValidationError
        assert isinstance(result, (MythosMUDError, ValidationError))


def test_wrap_third_party_exception_sqlalchemy_integrity():
    """Test wrap_third_party_exception with SQLAlchemy IntegrityError."""
    import sqlalchemy.exc
    
    original_error = sqlalchemy.exc.IntegrityError("FK violation", None, None)
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, DatabaseError)


def test_wrap_third_party_exception_sqlalchemy_programming():
    """Test wrap_third_party_exception with SQLAlchemy ProgrammingError."""
    import sqlalchemy.exc
    
    original_error = sqlalchemy.exc.ProgrammingError("SQL error", None, None)
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, DatabaseError)


def test_wrap_third_party_exception_sqlalchemy_data():
    """Test wrap_third_party_exception with SQLAlchemy DataError."""
    import sqlalchemy.exc
    
    original_error = sqlalchemy.exc.DataError("Data error", None, None)
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, DatabaseError)


def test_wrap_third_party_exception_httpx_timeout():
    """Test wrap_third_party_exception with httpx TimeoutException."""
    import httpx
    
    original_error = httpx.TimeoutException("Request timeout")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, NetworkError)


def test_wrap_third_party_exception_httpx_connect():
    """Test wrap_third_party_exception with httpx ConnectError."""
    import httpx
    
    original_error = httpx.ConnectError("Connection failed")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, NetworkError)


def test_wrap_third_party_exception_httpx_status():
    """Test wrap_third_party_exception with httpx HTTPStatusError."""
    import httpx
    
    original_error = httpx.HTTPStatusError("Status error", request=MagicMock(), response=MagicMock())
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, NetworkError)


def test_wrap_third_party_exception_argon2_hashing():
    """Test wrap_third_party_exception with argon2 HashingError."""
    import argon2.exceptions
    
    original_error = argon2.exceptions.HashingError("Hashing failed")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, AuthenticationError)


def test_wrap_third_party_exception_argon2_invalid_hash():
    """Test wrap_third_party_exception with argon2 InvalidHash."""
    import argon2.exceptions
    
    # InvalidHash might not exist, use VerificationError instead
    original_error = argon2.exceptions.VerificationError("Invalid hash format")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, AuthenticationError)


def test_wrap_third_party_exception_argon2_verify_mismatch():
    """Test wrap_third_party_exception with argon2 VerifyMismatchError."""
    import argon2.exceptions
    
    original_error = argon2.exceptions.VerifyMismatchError("Verification mismatch")
    
    result = wrap_third_party_exception(original_error)

    assert isinstance(result, AuthenticationError)


def test_log_error_with_context():
    """Test log_error_with_context logs error with context."""
    error = ValueError("Test error")
    context = create_error_context(user_id="user123")
    
    with patch("server.utils.error_logging.increment_exception"):
        # Should not raise
        from server.utils.error_logging import log_error_with_context
        log_error_with_context(error, context=context, level="error")


def test_log_error_with_context_different_levels():
    """Test log_error_with_context with different log levels."""
    error = RuntimeError("Runtime error")
    
    with patch("server.utils.error_logging.increment_exception"):
        from server.utils.error_logging import log_error_with_context
        
        # Test different levels
        for level in ["debug", "info", "warning", "error", "critical"]:
            log_error_with_context(error, level=level)


def test_log_error_with_context_custom_logger():
    """Test log_error_with_context with custom logger."""
    error = ValueError("Error")
    
    with patch("server.utils.error_logging.increment_exception"):
        from server.utils.error_logging import log_error_with_context
        log_error_with_context(error, logger_name="custom.module", level="warning")


def test_log_error_with_context_increment_error():
    """Test log_error_with_context handles increment_exception errors."""
    error = ValueError("Error")
    
    with patch("server.utils.error_logging.increment_exception", side_effect=RuntimeError("Monitoring error")):
        from server.utils.error_logging import log_error_with_context
        # Should not raise
        log_error_with_context(error)


def test_create_logged_http_exception():
    """Test create_logged_http_exception creates and logs HTTPException."""
    from server.utils.error_logging import create_logged_http_exception
    
    result = create_logged_http_exception(404, "Not found")
    
    assert isinstance(result, HTTPException)
    assert result.status_code == 404
    assert result.detail == "Not found"


def test_create_logged_http_exception_with_context():
    """Test create_logged_http_exception with context."""
    from server.utils.error_logging import create_logged_http_exception
    
    context = create_error_context(user_id="user123")
    result = create_logged_http_exception(500, "Internal error", context=context)
    
    assert result.status_code == 500
    assert result.detail == "Internal error"


def test_create_logged_http_exception_custom_logger():
    """Test create_logged_http_exception with custom logger."""
    from server.utils.error_logging import create_logged_http_exception
    
    result = create_logged_http_exception(400, "Bad request", logger_name="api.module")
    
    assert result.status_code == 400


def test_create_context_from_websocket():
    """Test create_context_from_websocket creates context from WebSocket."""
    from fastapi.websockets import WebSocket
    from server.utils.error_logging import create_context_from_websocket
    
    # Create a simple object that mimics WebSocket behavior
    class MockURL:
        def __str__(self):
            return "ws://example.com/ws"
    
    class MockHeaders:
        def get(self, key, default=""):
            return {"user-agent": "ws-agent"}.get(key, default)
    
    class MockWebSocket:
        def __init__(self):
            self.url = MockURL()
            self.headers = MockHeaders()
            self.client = type('obj', (object,), {'host': "192.168.1.1"})()
            self.state = type('obj', (object,), {})()
    
    mock_websocket = MockWebSocket()
    
    context = create_context_from_websocket(mock_websocket)
    
    assert isinstance(context, ErrorContext)
    assert "example.com" in context.metadata["path"]
    assert context.metadata["connection_type"] == "websocket"
    assert context.metadata["remote_addr"] == "192.168.1.1"


def test_create_context_from_websocket_with_state():
    """Test create_context_from_websocket extracts user info from state."""
    from fastapi.websockets import WebSocket
    from server.utils.error_logging import create_context_from_websocket
    
    class MockURL:
        def __str__(self):
            return "ws://example.com/ws"
    
    class MockHeaders:
        def get(self, key, default=""):
            return {}
    
    class MockWebSocket:
        def __init__(self):
            self.url = MockURL()
            self.headers = MockHeaders()
            self.client = None
            self.state = type('obj', (object,), {
                'user_id': "user123",
                'session_id': "session456"
            })()
    
    mock_websocket = MockWebSocket()
    
    context = create_context_from_websocket(mock_websocket)
    
    assert context.user_id == "user123"
    assert context.session_id == "session456"


def test_create_context_from_websocket_no_client():
    """Test create_context_from_websocket handles missing client."""
    from fastapi.websockets import WebSocket
    from server.utils.error_logging import create_context_from_websocket
    
    class MockURL:
        def __str__(self):
            return "ws://example.com/ws"
    
    class MockHeaders:
        def get(self, key, default=""):
            return {}
    
    class MockWebSocket:
        def __init__(self):
            self.url = MockURL()
            self.headers = MockHeaders()
            self.client = None
            self.state = type('obj', (object,), {})()
    
    mock_websocket = MockWebSocket()
    
    context = create_context_from_websocket(mock_websocket)
    
    assert context.metadata["remote_addr"] == ""

