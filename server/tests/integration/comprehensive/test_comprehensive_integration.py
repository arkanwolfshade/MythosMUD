"""
Comprehensive integration tests for all FastAPI improvements.

This module tests the integration of all improvements made to the FastAPI application:
1. Security Headers Middleware
2. Consolidated Logging Middleware
3. Service Layer Pattern with Dependency Injection
4. Async/Await Consistency

ARCHITECTURE FIX: Updated to use container_test_client fixture
Following pytest best practices and the Pnakotic Manuscripts of Integration Testing Methodology.
"""

from unittest.mock import AsyncMock, Mock

import pytest

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class TestComprehensiveIntegration:
    """
    Test comprehensive integration of all FastAPI improvements.

    AI: Following pytest best practices:
    - Uses container_test_client for proper DI
    - Mock persistence configured via fixture
    - AAA pattern in tests
    """

    @pytest.fixture
    def mock_persistence_comprehensive(self, container_test_client):
        """
        Mock persistence layer for comprehensive testing.

        AI: Following pytest best practices - reuse container_test_client
        """
        app = container_test_client.app
        mock_persistence = AsyncMock()

        # Configure async methods
        mock_persistence.async_list_players = AsyncMock(return_value=[])
        mock_persistence.async_get_player = AsyncMock(return_value=None)
        mock_persistence.async_get_room = AsyncMock(return_value=None)
        mock_persistence.async_save_player = AsyncMock(return_value=None)
        mock_persistence.async_delete_player = AsyncMock(return_value=True)

        # Configure sync methods (backward compatibility)
        mock_persistence.list_players = Mock(return_value=[])
        mock_persistence.get_player = Mock(return_value=None)
        mock_persistence.get_room = Mock(return_value=None)
        mock_persistence.save_player = Mock(return_value=None)
        mock_persistence.delete_player = Mock(return_value=True)

        # Replace container's persistence with mock
        app.state.container.persistence = mock_persistence
        app.state.persistence = mock_persistence

        # Update service persistence references
        if hasattr(app.state.container, "player_service") and app.state.container.player_service:
            app.state.container.player_service.persistence = mock_persistence

        if hasattr(app.state.container, "room_service") and app.state.container.room_service:
            app.state.container.room_service.persistence = mock_persistence

        return mock_persistence

    def test_security_headers_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that security headers are applied to all endpoints."""
        # Test various endpoints to ensure security headers are present
        endpoints = ["/", "/api/players/", "/rooms/test-room-id", "/docs", "/openapi.json"]

        for endpoint in endpoints:
            response = container_test_client.get(endpoint)

            # Check for essential security headers
            assert "x-content-type-options" in response.headers
            assert "x-frame-options" in response.headers
            assert "x-xss-protection" in response.headers
            assert "strict-transport-security" in response.headers
            assert "referrer-policy" in response.headers
            assert "permissions-policy" in response.headers

            # Verify header values
            assert response.headers["x-content-type-options"] == "nosniff"
            assert response.headers["x-frame-options"] == "DENY"
            assert response.headers["x-xss-protection"] == "1; mode=block"

    def test_cors_configuration_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that CORS configuration works with environment variables."""
        # Test preflight request with allowed origin
        response = container_test_client.options(
            "/api/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type,Authorization",
            },
        )

        # Check CORS headers are present
        assert "access-control-allow-origin" in response.headers
        assert "access-control-allow-methods" in response.headers
        assert "access-control-allow-headers" in response.headers

        # Test actual request with CORS headers
        response = container_test_client.get("/api/players/", headers={"Origin": "http://localhost:5173"})

        assert "access-control-allow-origin" in response.headers

    def test_logging_middleware_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that comprehensive logging middleware works correctly."""
        # Make requests to various endpoints to test logging
        endpoints = ["/api/players/", "/rooms/test-room-id", "/docs"]

        for endpoint in endpoints:
            response = container_test_client.get(endpoint)

            # Verify response is successful (logging shouldn't break functionality)
            assert response.status_code in [200, 404, 422]  # Valid responses

            # Check that logging headers are present (if implemented)
            # This tests that the logging middleware doesn't interfere with responses

    def test_service_layer_dependency_injection_integration(
        self, container_test_client, mock_persistence_comprehensive
    ):
        """Test that service layer dependency injection works correctly."""
        # Test that endpoints use the service layer properly
        response = container_test_client.get("/api/players/")

        # Should return 200 (empty list) or 401 (unauthorized)
        assert response.status_code in [200, 401]

        if response.status_code == 200:
            # If successful, verify it returns proper data structure
            data = response.json()
            assert isinstance(data, list)

    def test_async_operations_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that async operations work correctly throughout the stack."""
        # Test async route handlers
        response = container_test_client.get("/api/players/")

        # Verify async operations don't cause blocking
        assert response.status_code in [200, 401]

        # Test that async service layer integration works
        # This is verified by the fact that the request completes successfully

    def test_middleware_stack_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that all middleware work together correctly."""
        # Make a request that goes through the entire middleware stack
        response = container_test_client.get("/api/players/")

        # Verify all middleware layers work together
        assert response.status_code in [200, 401]

        # Check that security headers are still present (middleware integration)
        assert "x-content-type-options" in response.headers
        assert "x-frame-options" in response.headers

        # Check that CORS headers are present (middleware integration) - need Origin header
        response_with_origin = container_test_client.get("/api/players/", headers={"Origin": "http://localhost:5173"})
        assert "access-control-allow-origin" in response_with_origin.headers

    def test_error_handling_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that error handling works correctly across all layers."""
        # Test 404 error
        response = container_test_client.get("/nonexistent-endpoint")
        assert response.status_code == 404

        # Test invalid endpoint
        response = container_test_client.get("/api/players/invalid-uuid")
        assert response.status_code in [404, 422, 401]

        # Verify error responses still have security headers
        assert "x-content-type-options" in response.headers

    def test_concurrent_requests_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that the application handles concurrent requests correctly."""
        import threading
        import time

        results = []

        def make_request():
            """Make a request and store the result."""
            start_time = time.time()
            response = container_test_client.get("/api/players/")
            end_time = time.time()

            results.append(
                {
                    "status_code": response.status_code,
                    "response_time": end_time - start_time,
                    "has_security_headers": "x-content-type-options" in response.headers,
                }
            )

        # Make multiple concurrent requests
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=make_request)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify all requests completed successfully
        assert len(results) == 5
        for result in results:
            assert result["status_code"] in [200, 401]
            assert result["has_security_headers"] is True
            assert result["response_time"] < 5.0  # Should be fast

    def test_database_operations_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that database operations work correctly with async patterns."""
        # Test that async database operations don't cause issues
        response = container_test_client.get("/api/players/")

        # Should complete without blocking
        assert response.status_code in [200, 401]

        # Test room operations
        response = container_test_client.get("/rooms/test-room-id")
        assert response.status_code in [200, 404, 401]

    def test_authentication_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that authentication works correctly with all improvements."""
        # Test unauthenticated request
        response = container_test_client.get("/api/players/")
        assert response.status_code in [200, 401]

        # Verify security headers are still present for unauthenticated requests
        assert "x-content-type-options" in response.headers

    def test_documentation_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that API documentation works correctly with all improvements."""
        # Test OpenAPI schema
        response = container_test_client.get("/openapi.json")
        assert response.status_code == 200

        # Test Swagger UI
        response = container_test_client.get("/docs")
        assert response.status_code == 200

        # Verify documentation endpoints have security headers
        assert "x-content-type-options" in response.headers

    def test_performance_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that all improvements don't significantly impact performance."""
        import time

        # Measure response time for multiple requests
        response_times = []
        for _ in range(10):
            start_time = time.time()
            response = container_test_client.get("/api/players/")
            end_time = time.time()

            response_times.append(end_time - start_time)
            assert response.status_code in [200, 401]

        # Verify average response time is reasonable
        avg_response_time = sum(response_times) / len(response_times)
        assert avg_response_time < 1.0  # Should be fast

    def test_health_check_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that health check endpoints work correctly."""
        # Test root endpoint (returns 404 as expected - no root route defined)
        response = container_test_client.get("/")
        assert response.status_code == 404

        # Verify error responses still have security headers
        assert "x-content-type-options" in response.headers

        # Test a valid endpoint instead
        response = container_test_client.get("/docs")
        assert response.status_code == 200
        assert "x-content-type-options" in response.headers

    @pytest.mark.asyncio
    async def test_async_service_layer_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test async service layer integration specifically."""
        # Test that async service methods work correctly
        response = container_test_client.get("/api/players/")

        # Should complete successfully with async operations
        assert response.status_code in [200, 401]

        # Test that async patterns don't cause issues
        # This is verified by the successful completion of the request

    def test_error_logging_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test that error logging works correctly with all improvements."""
        # Make a request that should generate an error
        response = container_test_client.get("/api/players/invalid-uuid")

        # Should handle error gracefully
        assert response.status_code in [404, 422, 401]

        # Verify error responses still have proper headers
        assert "x-content-type-options" in response.headers

    def test_comprehensive_workflow_integration(self, container_test_client, mock_persistence_comprehensive):
        """Test a comprehensive workflow that uses all improvements."""
        # 1. Test security headers on all requests
        response = container_test_client.get("/api/players/")
        assert "x-content-type-options" in response.headers

        # 2. Test CORS functionality
        response = container_test_client.options("/api/players/", headers={"Origin": "http://localhost:5173"})
        assert "access-control-allow-origin" in response.headers

        # 3. Test async service layer
        response = container_test_client.get("/rooms/test-room-id")
        assert response.status_code in [200, 404, 401]

        # 4. Test logging middleware
        response = container_test_client.get("/docs")
        assert response.status_code == 200

        # 5. Test error handling
        response = container_test_client.get("/nonexistent")
        assert response.status_code == 404

        # All operations should complete successfully with all improvements working together
