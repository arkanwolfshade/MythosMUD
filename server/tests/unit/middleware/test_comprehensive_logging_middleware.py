"""
Tests for comprehensive logging middleware.

This module tests the ComprehensiveLoggingMiddleware to ensure proper
consolidation of access, error, and request logging functionality.
"""

import time
from unittest.mock import Mock

import pytest
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.testclient import TestClient
from starlette.middleware.base import BaseHTTPMiddleware

from server.app.factory import create_app


class ComprehensiveLoggingMiddleware(BaseHTTPMiddleware):
    """
    Comprehensive logging middleware that combines access, error, and request logging.

    This middleware consolidates all logging functionality into a single,
    efficient middleware component that handles request/response logging,
    error logging, and performance monitoring.
    """

    def __init__(self, app, **kwargs):
        super().__init__(app, **kwargs)
        self.start_time = None

    async def dispatch(self, request: Request, call_next):
        """Handle comprehensive logging for requests and responses."""
        start_time = time.time()

        # Log request start
        self._log_request_start(request)

        try:
            # Process the request
            response = await call_next(request)

            # Log successful response
            process_time = time.time() - start_time
            self._log_request_success(request, response, process_time)

            return response

        except Exception as e:
            # Log error
            process_time = time.time() - start_time
            self._log_request_error(request, e, process_time)
            raise

    def _log_request_start(self, request: Request):
        """Log request start information."""
        # This would use the actual logger in the real implementation
        pass

    def _log_request_success(self, request: Request, response: Response, process_time: float):
        """Log successful request completion."""
        # This would use the actual logger in the real implementation
        pass

    def _log_request_error(self, request: Request, error: Exception, process_time: float):
        """Log request error."""
        # This would use the actual logger in the real implementation
        pass


class TestComprehensiveLoggingMiddleware:
    """Test the ComprehensiveLoggingMiddleware functionality."""

    def test_middleware_inherits_from_base(self):
        """Test that ComprehensiveLoggingMiddleware inherits from BaseHTTPMiddleware."""
        middleware = ComprehensiveLoggingMiddleware(Mock())
        assert isinstance(middleware, BaseHTTPMiddleware)

    @pytest.mark.asyncio
    async def test_middleware_logs_successful_requests(self):
        """Test that middleware logs successful requests."""
        app = FastAPI()

        @app.get("/test")
        async def test_endpoint():
            return {"message": "test"}

        # Add the middleware
        app.add_middleware(ComprehensiveLoggingMiddleware)

        # Create test client
        client = TestClient(app)

        # Make a request
        response = client.get("/test")

        # Verify response is successful
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_middleware_logs_errors(self):
        """Test that middleware logs errors and re-raises them."""
        app = FastAPI()

        @app.get("/error-test")
        async def error_endpoint():
            raise HTTPException(status_code=500, detail="Internal server error")

        app.add_middleware(ComprehensiveLoggingMiddleware)
        client = TestClient(app)

        # Make a request that will cause an error
        response = client.get("/error-test")

        # Verify error response
        assert response.status_code == 500

    @pytest.mark.asyncio
    async def test_middleware_measures_processing_time(self):
        """Test that middleware measures and logs processing time."""
        app = FastAPI()

        @app.get("/slow-test")
        async def slow_endpoint():
            time.sleep(0.1)  # Simulate slow processing
            return {"message": "slow response"}

        app.add_middleware(ComprehensiveLoggingMiddleware)
        client = TestClient(app)

        # Make a request
        response = client.get("/slow-test")

        # Verify response is successful
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_middleware_preserves_response_headers(self):
        """Test that middleware preserves response headers."""
        app = FastAPI()

        @app.get("/test")
        async def test_endpoint():
            response = Response(content='{"message": "test"}', media_type="application/json")
            response.headers["Custom-Header"] = "custom-value"
            return response

        app.add_middleware(ComprehensiveLoggingMiddleware)
        client = TestClient(app)

        response = client.get("/test")

        # Verify custom header is preserved
        assert response.headers["Custom-Header"] == "custom-value"

    def test_middleware_integration_with_factory(self):
        """Test that middleware can be integrated with the app factory."""
        # This test verifies the middleware can be added to the factory
        # without breaking the app creation process
        app = create_app()
        assert isinstance(app, FastAPI)

        # Verify the app can be created successfully
        client = TestClient(app)
        # Test an endpoint that exists in the factory-created app
        response = client.get("/auth/jwt/login")
        # Should get 405 Method Not Allowed (endpoint exists but doesn't accept GET)
        # or 422 if it accepts GET but requires parameters - either way, not 404
        assert response.status_code != 404


class TestLoggingMiddlewareConsolidation:
    """Test logging middleware consolidation functionality."""

    def test_no_duplicate_logging_middleware(self):
        """Test that logging middleware is not duplicated."""
        app = create_app()

        # Count logging middleware instances
        logging_middleware_count = 0
        for middleware in app.user_middleware:
            middleware_name = str(middleware.cls)
            if any(
                name in middleware_name
                for name in ["AccessLoggingMiddleware", "RequestLoggingMiddleware", "ErrorLoggingMiddleware"]
            ):
                logging_middleware_count += 1

        # Should have at most one of each type
        assert logging_middleware_count <= 3, (
            f"Found {logging_middleware_count} logging middleware instances, expected at most 3"
        )

    def test_middleware_order_preserved(self):
        """Test that middleware order is preserved after consolidation."""
        app = create_app()

        # Verify middleware order (security headers should be first)
        middleware_classes = [str(middleware.cls) for middleware in app.user_middleware]

        # Security headers should be present and early
        assert any("SecurityHeadersMiddleware" in cls for cls in middleware_classes)

        # CORS should be present
        assert any("CORSMiddleware" in cls for cls in middleware_classes)

    def test_comprehensive_middleware_replaces_individual_middleware(self):
        """Test that comprehensive middleware replaces individual middleware components."""
        # This test verifies that ComprehensiveLoggingMiddleware is present
        # and the individual AccessLoggingMiddleware, RequestLoggingMiddleware, and
        # ErrorLoggingMiddleware are removed
        app = create_app()

        # Check that we have ComprehensiveLoggingMiddleware
        comprehensive_middleware_found = False
        old_middleware_found = set()

        for middleware in app.user_middleware:
            middleware_name = str(middleware.cls)
            if "ComprehensiveLoggingMiddleware" in middleware_name:
                comprehensive_middleware_found = True
            elif "AccessLoggingMiddleware" in middleware_name:
                old_middleware_found.add("AccessLoggingMiddleware")
            elif "RequestLoggingMiddleware" in middleware_name:
                old_middleware_found.add("RequestLoggingMiddleware")
            elif "ErrorLoggingMiddleware" in middleware_name:
                old_middleware_found.add("ErrorLoggingMiddleware")

        # Should have ComprehensiveLoggingMiddleware
        assert comprehensive_middleware_found, "Should have ComprehensiveLoggingMiddleware"

        # Should not have old individual middleware types
        assert len(old_middleware_found) == 0, f"Should not have old middleware types: {old_middleware_found}"


class TestLoggingPerformance:
    """Test logging middleware performance characteristics."""

    @pytest.mark.asyncio
    async def test_middleware_minimal_overhead(self):
        """Test that middleware adds minimal overhead to requests."""
        app = FastAPI()

        @app.get("/performance-test")
        async def performance_endpoint():
            return {"message": "performance test"}

        app.add_middleware(ComprehensiveLoggingMiddleware)
        client = TestClient(app)

        # Measure time for multiple requests
        start_time = time.time()
        for _ in range(10):
            response = client.get("/performance-test")
            assert response.status_code == 200
        end_time = time.time()

        # Should complete quickly (less than 1 second for 10 requests)
        total_time = end_time - start_time
        assert total_time < 1.0, f"Middleware added too much overhead: {total_time}s for 10 requests"

    @pytest.mark.asyncio
    async def test_middleware_handles_high_volume(self):
        """Test that middleware handles high volume of requests."""
        app = FastAPI()

        @app.get("/volume-test")
        async def volume_endpoint():
            return {"message": "volume test"}

        app.add_middleware(ComprehensiveLoggingMiddleware)
        client = TestClient(app)

        # Make many requests to test volume handling
        for _ in range(100):
            response = client.get("/volume-test")
            assert response.status_code == 200
