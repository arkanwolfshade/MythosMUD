"""
Tests for security headers middleware.

This module tests the SecurityHeadersMiddleware to ensure proper security headers
are added to all HTTP responses.
"""

import os
from unittest.mock import Mock, patch

import pytest
from fastapi import FastAPI, Request, Response
from fastapi.testclient import TestClient
from starlette.middleware.base import BaseHTTPMiddleware

from server.app.factory import create_app
from server.config import reset_config


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware to add comprehensive security headers to all HTTP responses.

    This middleware adds essential security headers to protect against common
    web vulnerabilities including XSS, clickjacking, and information disclosure.
    """

    async def dispatch(self, request: Request, call_next):
        """Add security headers to the response."""
        response = await call_next(request)

        # Add comprehensive security headers
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = "default-src 'self'"

        return response


class TestSecurityHeadersMiddleware:
    """Test the SecurityHeadersMiddleware functionality."""

    def test_middleware_inherits_from_base(self) -> None:
        """Test that SecurityHeadersMiddleware inherits from BaseHTTPMiddleware."""
        middleware = SecurityHeadersMiddleware(Mock())
        assert isinstance(middleware, BaseHTTPMiddleware)

    @pytest.mark.asyncio
    async def test_middleware_adds_security_headers(self) -> None:
        """Test that middleware adds all required security headers."""
        # Create a mock app and request
        app = FastAPI()

        @app.get("/test")
        async def test_endpoint():
            return {"message": "test"}

        # Add the middleware
        app.add_middleware(SecurityHeadersMiddleware)

        # Create test client
        client = TestClient(app)

        # Make a request
        response = client.get("/test")

        # Verify response is successful
        assert response.status_code == 200

        # Verify all security headers are present
        assert "Strict-Transport-Security" in response.headers
        assert "X-Frame-Options" in response.headers
        assert "X-Content-Type-Options" in response.headers
        assert "Referrer-Policy" in response.headers
        assert "Content-Security-Policy" in response.headers

    @pytest.mark.asyncio
    async def test_security_headers_values(self) -> None:
        """Test that security headers have correct values."""
        app = FastAPI()

        @app.get("/test")
        async def test_endpoint():
            return {"message": "test"}

        app.add_middleware(SecurityHeadersMiddleware)
        client = TestClient(app)

        response = client.get("/test")

        # Verify header values
        assert response.headers["Strict-Transport-Security"] == "max-age=31536000; includeSubDomains"
        assert response.headers["X-Frame-Options"] == "DENY"
        assert response.headers["X-Content-Type-Options"] == "nosniff"
        assert response.headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
        assert response.headers["Content-Security-Policy"] == "default-src 'self'"

    @pytest.mark.asyncio
    async def test_middleware_works_with_all_endpoints(self) -> None:
        """Test that security headers are added to all endpoint types."""
        app = FastAPI()

        @app.get("/get-test")
        async def get_endpoint():
            return {"method": "GET"}

        @app.post("/post-test")
        async def post_endpoint():
            return {"method": "POST"}

        @app.put("/put-test")
        async def put_endpoint():
            return {"method": "PUT"}

        @app.delete("/delete-test")
        async def delete_endpoint():
            return {"method": "DELETE"}

        app.add_middleware(SecurityHeadersMiddleware)
        client = TestClient(app)

        # Test all HTTP methods
        for method, path in [
            ("GET", "/get-test"),
            ("POST", "/post-test"),
            ("PUT", "/put-test"),
            ("DELETE", "/delete-test"),
        ]:
            response = None
            if method == "GET":
                response = client.get(path)
            elif method == "POST":
                response = client.post(path)
            elif method == "PUT":
                response = client.put(path)
            elif method == "DELETE":
                response = client.delete(path)

            assert response is not None
            assert response.status_code == 200
            assert "X-Frame-Options" in response.headers
            assert response.headers["X-Frame-Options"] == "DENY"

    @pytest.mark.asyncio
    async def test_middleware_preserves_existing_headers(self) -> None:
        """Test that middleware preserves existing response headers."""
        app = FastAPI()

        @app.get("/test")
        async def test_endpoint():
            response = Response(content='{"message": "test"}', media_type="application/json")
            response.headers["Custom-Header"] = "custom-value"
            return response

        app.add_middleware(SecurityHeadersMiddleware)
        client = TestClient(app)

        response = client.get("/test")

        # Verify custom header is preserved
        assert response.headers["Custom-Header"] == "custom-value"
        # Verify security headers are added
        assert "X-Frame-Options" in response.headers

    @pytest.mark.asyncio
    async def test_middleware_handles_errors(self) -> None:
        """Test that middleware adds security headers even when endpoints return errors."""
        app = FastAPI()

        @app.get("/error-test")
        async def error_endpoint():
            from fastapi import HTTPException

            raise HTTPException(status_code=404, detail="Not found")

        app.add_middleware(SecurityHeadersMiddleware)
        client = TestClient(app)

        response = client.get("/error-test")

        # Verify error response still has security headers
        assert response.status_code == 404
        assert "X-Frame-Options" in response.headers
        assert response.headers["X-Frame-Options"] == "DENY"

    def test_middleware_integration_with_factory(self) -> None:
        """Test that middleware can be integrated with the app factory."""
        # This test verifies the middleware can be added to the factory
        # without breaking the app creation process
        app = create_app()
        assert isinstance(app, FastAPI)

        # Verify the app can be created successfully
        client = TestClient(app)
        # Test an endpoint that exists in the factory-created app
        # The auth router should have endpoints available
        response = client.get("/auth/jwt/login")
        # Should get 405 Method Not Allowed (endpoint exists but doesn't accept GET)
        # or 422 if it accepts GET but requires parameters - either way, not 404
        assert response.status_code != 404

        # Verify security headers are present even on error responses
        assert "X-Frame-Options" in response.headers
        assert response.headers["X-Frame-Options"] == "DENY"


class TestCORSConfiguration:
    """Test CORS configuration improvements."""

    def test_cors_uses_environment_variables(self) -> None:
        """Test that CORS configuration uses environment variables."""
        with patch.dict(
            os.environ,
            {
                "ALLOWED_ORIGINS": "http://localhost:3000,https://example.com",
                "ALLOWED_METHODS": "GET,POST",
                "ALLOWED_HEADERS": "Content-Type,Authorization",
            },
        ):
            reset_config()
            app = create_app()

            cors_middleware = None
            for middleware in app.user_middleware:
                if "CORSMiddleware" in str(middleware.cls):
                    cors_middleware = middleware
                    break

            assert cors_middleware is not None, "CORS middleware should be present when configured"
            assert cors_middleware.kwargs["allow_origins"] == [
                "http://localhost:3000",
                "https://example.com",
            ]
            assert cors_middleware.kwargs["allow_methods"] == ["GET", "POST"]
            assert cors_middleware.kwargs["allow_headers"] == ["Content-Type", "Authorization"]

        reset_config()

    def test_cors_restricts_methods_and_headers(self) -> None:
        """Test that CORS configuration restricts methods and headers."""
        app = create_app()

        # Check that CORS middleware is configured
        cors_middleware = None
        for middleware in app.user_middleware:
            if "CORSMiddleware" in str(middleware.cls):
                cors_middleware = middleware
                break

        assert cors_middleware is not None, "CORS middleware should be present"


class TestMiddlewareConsolidation:
    """Test middleware consolidation functionality."""

    def test_no_duplicate_error_middleware(self) -> None:
        """Test that ErrorLoggingMiddleware is not registered twice."""
        app = create_app()

        # Count ErrorLoggingMiddleware instances
        error_middleware_count = 0
        for middleware in app.user_middleware:
            if "ErrorLoggingMiddleware" in str(middleware.cls):
                error_middleware_count += 1

        # Should have at most one ErrorLoggingMiddleware
        assert error_middleware_count <= 1, (
            f"Found {error_middleware_count} ErrorLoggingMiddleware instances, expected at most 1"
        )

    def test_middleware_order(self) -> None:
        """Test that middleware is added in the correct order."""
        app = create_app()

        # Verify middleware order (security headers should be added early)
        middleware_classes = [str(middleware.cls) for middleware in app.user_middleware]

        # CORS should be present
        assert any("CORSMiddleware" in cls for cls in middleware_classes)

        # Comprehensive logging should be present (replaces AccessLoggingMiddleware)
        assert any("ComprehensiveLoggingMiddleware" in cls for cls in middleware_classes)


class TestSecurityHeadersMiddlewareImplementation:
    """Test the actual SecurityHeadersMiddleware implementation."""

    @pytest.mark.asyncio
    async def test_security_headers_middleware_asgi_interface(self) -> None:
        """Test SecurityHeadersMiddleware ASGI interface."""
        from unittest.mock import AsyncMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        # Create mock app
        mock_app = AsyncMock()

        # Create middleware
        middleware = SecurityHeadersMiddleware(mock_app)

        # Create mock scope, receive, send
        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        receive = AsyncMock()
        send = AsyncMock()

        # Mock send_with_headers to capture headers
        headers_captured = {}

        async def mock_send(message):
            if message["type"] == "http.response.start":
                headers_captured.update(message.get("headers", []))
            await send(message)

        # Call middleware
        await middleware(scope, receive, mock_send)

        # Verify app was called
        mock_app.assert_called_once()

    @pytest.mark.asyncio
    async def test_security_headers_middleware_non_http_scope(self) -> None:
        """Test SecurityHeadersMiddleware passes through non-HTTP scopes."""
        from unittest.mock import AsyncMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = AsyncMock()
        middleware = SecurityHeadersMiddleware(mock_app)

        # WebSocket scope
        websocket_scope = {"type": "websocket"}
        receive = AsyncMock()
        send = AsyncMock()

        await middleware(websocket_scope, receive, send)

        # Should pass through without modification
        mock_app.assert_called_once_with(websocket_scope, receive, send)

    @pytest.mark.asyncio
    async def test_security_headers_middleware_dispatch_method(self) -> None:
        """Test SecurityHeadersMiddleware dispatch method (backward compatibility)."""
        from unittest.mock import AsyncMock, MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = MagicMock()
        middleware = SecurityHeadersMiddleware(mock_app)

        # Create mock request with proper scope
        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        request = Request(scope, AsyncMock())

        # Create proper Response object
        response = Response(content="test", status_code=200)

        # Mock call_next
        call_next = AsyncMock(return_value=response)

        # Call dispatch
        result = await middleware.dispatch(request, call_next)

        # Verify headers were added
        assert result == response
        # Headers should be added by _add_security_headers_to_response
        # Check headers case-insensitively since Starlette headers are case-insensitive
        header_keys = [key.lower() for key in response.headers.keys()]
        assert "strict-transport-security" in header_keys
        assert "x-frame-options" in header_keys

    @pytest.mark.asyncio
    async def test_security_headers_middleware_dispatch_exception(self) -> None:
        """Test SecurityHeadersMiddleware dispatch exception handling."""
        from unittest.mock import AsyncMock, MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = MagicMock()
        middleware = SecurityHeadersMiddleware(mock_app)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        request = Request(scope, AsyncMock())

        # Mock call_next to raise exception
        call_next = AsyncMock(side_effect=RuntimeError("Test error"))

        with patch("server.middleware.security_headers.logger.error") as mock_error:
            with pytest.raises(RuntimeError):
                await middleware.dispatch(request, call_next)

            # Verify error was logged
            mock_error.assert_called_once()

    @pytest.mark.asyncio
    async def test_security_headers_middleware_asgi_exception(self) -> None:
        """Test SecurityHeadersMiddleware ASGI exception handling."""
        from unittest.mock import AsyncMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = AsyncMock(side_effect=RuntimeError("Test error"))
        middleware = SecurityHeadersMiddleware(mock_app)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        receive = AsyncMock()
        send = AsyncMock()

        with patch("server.middleware.security_headers.logger.error") as mock_error:
            with pytest.raises(RuntimeError):
                await middleware(scope, receive, send)

            # Verify error was logged
            mock_error.assert_called_once()

    def test_security_headers_middleware_environment_config(self) -> None:
        """Test SecurityHeadersMiddleware reads environment variables."""
        from unittest.mock import MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        with patch.dict(
            os.environ,
            {
                "HSTS_MAX_AGE": "63072000",
                "HSTS_INCLUDE_SUBDOMAINS": "false",
                "CSP_POLICY": "default-src 'none'",
                "REFERRER_POLICY": "no-referrer",
            },
        ):
            mock_app = MagicMock()
            middleware = SecurityHeadersMiddleware(mock_app)

            assert middleware.hsts_max_age == 63072000
            assert middleware.hsts_include_subdomains is False
            assert middleware.csp_policy == "default-src 'none'"
            assert middleware.referrer_policy == "no-referrer"

    def test_security_headers_middleware_default_config(self) -> None:
        """Test SecurityHeadersMiddleware uses default configuration."""
        from unittest.mock import MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        # Remove env vars if they exist
        env_vars = ["HSTS_MAX_AGE", "HSTS_INCLUDE_SUBDOMAINS", "CSP_POLICY", "REFERRER_POLICY"]
        # Store original values
        original_env = {var: os.environ.get(var) for var in env_vars}

        try:
            # Remove env vars
            for var in env_vars:
                os.environ.pop(var, None)

            mock_app = MagicMock()
            middleware = SecurityHeadersMiddleware(mock_app)

            # Should use defaults
            assert middleware.hsts_max_age == 31536000
            assert middleware.hsts_include_subdomains is True
            assert middleware.csp_policy == "default-src 'self'"
            assert middleware.referrer_policy == "strict-origin-when-cross-origin"
        finally:
            # Restore original env vars
            for var, value in original_env.items():
                if value is not None:
                    os.environ[var] = value

    def test_security_headers_middleware_add_headers_hsts_without_subdomains(self) -> None:
        """Test SecurityHeadersMiddleware HSTS header without includeSubDomains."""
        from unittest.mock import MagicMock

        from starlette.datastructures import MutableHeaders

        from server.middleware.security_headers import SecurityHeadersMiddleware

        with patch.dict(os.environ, {"HSTS_INCLUDE_SUBDOMAINS": "false"}):
            mock_app = MagicMock()
            middleware = SecurityHeadersMiddleware(mock_app)

            headers = MutableHeaders()
            middleware._add_security_headers(headers)

            hsts_value = headers["Strict-Transport-Security"]
            assert "max-age=" in hsts_value
            assert "includeSubDomains" not in hsts_value

    def test_security_headers_middleware_add_headers_to_non_response(self) -> None:
        """Test SecurityHeadersMiddleware _add_security_headers_to_response with non-Response."""
        from unittest.mock import MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = MagicMock()
        middleware = SecurityHeadersMiddleware(mock_app)

        # Pass non-Response object
        non_response = MagicMock()
        middleware._add_security_headers_to_response(non_response)

        # Should not raise error, just skip
        assert True  # Test passes if no exception raised

    @pytest.mark.asyncio
    async def test_security_headers_middleware_asgi_send_with_headers_non_start_message(self) -> None:
        """Test SecurityHeadersMiddleware send_with_headers with non-start message."""
        from unittest.mock import AsyncMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = AsyncMock()
        middleware = SecurityHeadersMiddleware(mock_app)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        receive = AsyncMock()
        send = AsyncMock()

        # Track calls to send
        send_calls = []

        async def mock_send(message):
            send_calls.append(message)
            await send(message)

        # Mock app to send multiple messages
        async def mock_app_handler(scope, receive, send):
            await send({"type": "http.response.start", "status": 200, "headers": []})
            await send({"type": "http.response.body", "body": b"test"})

        middleware.app = mock_app_handler

        await middleware(scope, receive, mock_send)

        # Should have called send for both messages
        assert len(send_calls) >= 1

    @pytest.mark.asyncio
    async def test_security_headers_middleware_logger_info_initialization(self) -> None:
        """Test SecurityHeadersMiddleware logs info during initialization."""
        from unittest.mock import MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        with patch("server.middleware.security_headers.logger.info") as mock_info:
            mock_app = MagicMock()
            SecurityHeadersMiddleware(mock_app)  # Instantiate to trigger initialization logging
            # Should log initialization info
            mock_info.assert_called_once()
            call_args = mock_info.call_args
            assert "SecurityHeadersMiddleware initialized" in str(call_args)

    def test_security_headers_middleware_hsts_without_subdomains_condition(self) -> None:
        """Test SecurityHeadersMiddleware HSTS header condition when includeSubDomains is False."""
        from unittest.mock import MagicMock

        from starlette.datastructures import MutableHeaders

        from server.middleware.security_headers import SecurityHeadersMiddleware

        with patch.dict(os.environ, {"HSTS_INCLUDE_SUBDOMAINS": "false"}):
            mock_app = MagicMock()
            middleware = SecurityHeadersMiddleware(mock_app)

            headers = MutableHeaders()
            middleware._add_security_headers(headers)

            hsts_value = headers["Strict-Transport-Security"]
            assert "max-age=" in hsts_value
            assert "includeSubDomains" not in hsts_value

    @pytest.mark.asyncio
    async def test_security_headers_middleware_asgi_exception_logging(self) -> None:
        """Test SecurityHeadersMiddleware logs error when exception occurs in ASGI call."""
        from unittest.mock import AsyncMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = AsyncMock(side_effect=ValueError("Test error"))
        middleware = SecurityHeadersMiddleware(mock_app)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        receive = AsyncMock()
        send = AsyncMock()

        with patch("server.middleware.security_headers.logger.error") as mock_error:
            with pytest.raises(ValueError):
                await middleware(scope, receive, send)

            # Should log error
            mock_error.assert_called_once()
            call_args = mock_error.call_args
            assert "Error in security headers middleware" in str(call_args)

    @pytest.mark.asyncio
    async def test_security_headers_middleware_dispatch_exception_logging(self) -> None:
        """Test SecurityHeadersMiddleware logs error when exception occurs in dispatch."""
        from unittest.mock import AsyncMock, MagicMock

        from server.middleware.security_headers import SecurityHeadersMiddleware

        mock_app = MagicMock()
        middleware = SecurityHeadersMiddleware(mock_app)

        scope = {
            "type": "http",
            "method": "GET",
            "path": "/test",
            "headers": [],
            "query_string": b"",
            "scheme": "http",
            "server": ("localhost", 8000),
            "client": ("127.0.0.1", 12345),
        }
        request = Request(scope, AsyncMock())

        # Mock call_next to raise exception
        call_next = AsyncMock(side_effect=KeyError("Test error"))

        with patch("server.middleware.security_headers.logger.error") as mock_error:
            with pytest.raises(KeyError):
                await middleware.dispatch(request, call_next)

            # Should log error
            mock_error.assert_called_once()
            call_args = mock_error.call_args
            assert "Error in security headers middleware" in str(call_args)
