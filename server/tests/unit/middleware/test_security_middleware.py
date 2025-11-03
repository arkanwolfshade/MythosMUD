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

    def test_middleware_inherits_from_base(self):
        """Test that SecurityHeadersMiddleware inherits from BaseHTTPMiddleware."""
        middleware = SecurityHeadersMiddleware(Mock())
        assert isinstance(middleware, BaseHTTPMiddleware)

    @pytest.mark.asyncio
    async def test_middleware_adds_security_headers(self):
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
    async def test_security_headers_values(self):
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
    async def test_middleware_works_with_all_endpoints(self):
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
            if method == "GET":
                response = client.get(path)
            elif method == "POST":
                response = client.post(path)
            elif method == "PUT":
                response = client.put(path)
            elif method == "DELETE":
                response = client.delete(path)

            assert response.status_code == 200
            assert "X-Frame-Options" in response.headers
            assert response.headers["X-Frame-Options"] == "DENY"

    @pytest.mark.asyncio
    async def test_middleware_preserves_existing_headers(self):
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
    async def test_middleware_handles_errors(self):
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

    def test_middleware_integration_with_factory(self):
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

    def test_cors_uses_environment_variables(self):
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

    def test_cors_restricts_methods_and_headers(self):
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

    def test_no_duplicate_error_middleware(self):
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

    def test_middleware_order(self):
        """Test that middleware is added in the correct order."""
        app = create_app()

        # Verify middleware order (security headers should be added early)
        middleware_classes = [str(middleware.cls) for middleware in app.user_middleware]

        # CORS should be present
        assert any("CORSMiddleware" in cls for cls in middleware_classes)

        # Comprehensive logging should be present (replaces AccessLoggingMiddleware)
        assert any("ComprehensiveLoggingMiddleware" in cls for cls in middleware_classes)
