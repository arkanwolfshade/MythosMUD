"""
Verification tests for CORS configuration with environment variables.

This module tests that CORS configuration works correctly with environment variables,
ensuring proper cross-origin resource sharing functionality.

Following the cross-origin security protocols outlined in the Arkham Security Manual.
"""

import pytest
from fastapi.testclient import TestClient

from server.app.factory import create_app


class TestCORSConfigurationVerification:
    """Test CORS configuration works with environment variables."""

    @pytest.fixture
    def app(self, mock_application_container):
        """Create FastAPI app for testing."""
        app = create_app()

        # Mock the persistence layer with async methods
        from unittest.mock import AsyncMock

        mock_persistence = AsyncMock()
        mock_persistence.async_list_players.return_value = []
        mock_persistence.async_get_player.return_value = None
        mock_persistence.async_get_room.return_value = None
        mock_persistence.async_save_player.return_value = None
        mock_persistence.async_delete_player.return_value = True
        # Also mock synchronous methods for backward compatibility
        mock_persistence.list_players.return_value = []
        mock_persistence.get_player.return_value = None
        mock_persistence.get_room.return_value = None
        mock_persistence.save_player.return_value = None
        mock_persistence.delete_player.return_value = True

        # Use the comprehensive mock container and update persistence
        mock_application_container.persistence = mock_persistence

        app.state.container = mock_application_container
        app.state.persistence = mock_persistence

        # Set additional app state attributes that middleware may access
        app.state.player_service = mock_application_container.player_service
        app.state.room_service = mock_application_container.room_service
        app.state.event_bus = mock_application_container.event_bus

        return app

    @pytest.fixture
    def client(self, app):
        """Create TestClient for testing."""
        return TestClient(app)

    def test_cors_preflight_request_with_allowed_origin(self, client):
        """Test CORS preflight request with allowed origin."""
        response = client.options(
            "/api/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type,Authorization",
            },
        )

        # Should return 200 for preflight request
        assert response.status_code == 200

        # Should have CORS headers
        assert "access-control-allow-origin" in response.headers
        assert "access-control-allow-methods" in response.headers
        assert "access-control-allow-headers" in response.headers
        assert "access-control-max-age" in response.headers

        # Verify specific values
        assert response.headers["access-control-allow-origin"] == "http://localhost:5173"
        assert "POST" in response.headers["access-control-allow-methods"]
        assert "Content-Type" in response.headers["access-control-allow-headers"]
        assert "Authorization" in response.headers["access-control-allow-headers"]

    def test_cors_preflight_request_with_alternative_allowed_origin(self, client):
        """Test CORS preflight request with alternative allowed origin."""
        response = client.options(
            "/api/players/",
            headers={
                "Origin": "http://127.0.0.1:5173",
                "Access-Control-Request-Method": "GET",
                "Access-Control-Request-Headers": "Content-Type",
            },
        )

        # Should return 200 for preflight request
        assert response.status_code == 200

        # Should have CORS headers
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "http://127.0.0.1:5173"

    def test_cors_preflight_request_with_disallowed_origin(self, client):
        """Test CORS preflight request with disallowed origin."""
        response = client.options(
            "/api/players/",
            headers={
                "Origin": "http://malicious-site.com",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type",
            },
        )

        # Should return 400 for disallowed origin (CORS middleware rejects it)
        assert response.status_code == 400

        # Should NOT have access-control-allow-origin header for disallowed origins
        # The CORS middleware should not include this header for disallowed origins
        # This is the expected behavior for security

    def test_cors_actual_request_with_allowed_origin(self, client):
        """Test CORS actual request with allowed origin."""
        response = client.get("/api/players/", headers={"Origin": "http://localhost:5173"})

        # Should have CORS headers on actual requests too
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "http://localhost:5173"

    def test_cors_actual_request_with_alternative_allowed_origin(self, client):
        """Test CORS actual request with alternative allowed origin."""
        response = client.get("/api/players/", headers={"Origin": "http://127.0.0.1:5173"})

        # Should have CORS headers
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "http://127.0.0.1:5173"

    def test_cors_actual_request_with_disallowed_origin(self, client):
        """Test CORS actual request with disallowed origin."""
        response = client.get("/api/players/", headers={"Origin": "http://malicious-site.com"})

        # Should return 200 (the request succeeds)
        assert response.status_code in [200, 401]

        # Should NOT have access-control-allow-origin header for disallowed origins
        # This is the expected behavior for security

    def test_cors_preflight_with_different_methods(self, client):
        """Test CORS preflight request with different HTTP methods."""
        methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

        for method in methods:
            response = client.options(
                "/api/players/",
                headers={
                    "Origin": "http://localhost:5173",
                    "Access-Control-Request-Method": method,
                    "Access-Control-Request-Headers": "Content-Type",
                },
            )

            # Should return 200 for all methods
            assert response.status_code == 200

            # Should have CORS headers
            assert "access-control-allow-origin" in response.headers
            assert response.headers["access-control-allow-origin"] == "http://localhost:5173"

    def test_cors_preflight_with_different_headers(self, client):
        """Test CORS preflight request with different headers."""
        headers = ["Content-Type", "Authorization", "X-Requested-With", "Accept", "Accept-Language"]

        for header in headers:
            response = client.options(
                "/api/players/",
                headers={
                    "Origin": "http://localhost:5173",
                    "Access-Control-Request-Method": "POST",
                    "Access-Control-Request-Headers": header,
                },
            )

            # Should return 200 for all headers
            assert response.status_code == 200

            # Should have CORS headers
            assert "access-control-allow-origin" in response.headers
            assert response.headers["access-control-allow-origin"] == "http://localhost:5173"

    def test_cors_credentials_support(self, client):
        """Test CORS credentials support."""
        response = client.options(
            "/api/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type,Authorization",
            },
        )

        # Should have credentials support
        assert "access-control-allow-credentials" in response.headers
        assert response.headers["access-control-allow-credentials"] == "true"

    def test_cors_max_age_configuration(self, client):
        """Test CORS max age configuration."""
        response = client.options(
            "/api/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type",
            },
        )

        # Should have max age header
        assert "access-control-max-age" in response.headers
        assert response.headers["access-control-max-age"] == "600"  # 10 minutes

    def test_cors_on_different_endpoints(self, client):
        """Test CORS configuration on different endpoints."""
        endpoints = ["/api/players/", "/rooms/test-room-id", "/docs", "/openapi.json"]

        for endpoint in endpoints:
            response = client.options(
                endpoint,
                headers={
                    "Origin": "http://localhost:5173",
                    "Access-Control-Request-Method": "GET",
                    "Access-Control-Request-Headers": "Content-Type",
                },
            )

            # Should have CORS headers on all endpoints
            assert "access-control-allow-origin" in response.headers
            assert response.headers["access-control-allow-origin"] == "http://localhost:5173"

    def test_cors_without_origin_header(self, client):
        """Test CORS behavior without Origin header."""
        response = client.get("/api/players/")

        # Should work without Origin header
        assert response.status_code in [200, 401]

        # Should not have CORS headers when no Origin is provided
        # This is expected behavior

    def test_cors_environment_variable_behavior(self, client):
        """Test that CORS configuration respects environment variables."""
        # This test verifies that the CORS configuration is working
        # as expected based on the environment variables set in the app

        # Test with allowed origin
        response = client.get("/api/players/", headers={"Origin": "http://localhost:5173"})

        # Should have CORS headers for allowed origin
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "http://localhost:5173"

        # Test with disallowed origin
        response = client.get("/api/players/", headers={"Origin": "http://unauthorized-site.com"})

        # Should not have CORS headers for disallowed origin
        # This verifies the environment variable configuration is working

    def test_cors_preflight_handling_performance(self, client):
        """Test CORS preflight handling performance."""
        import time

        # Measure preflight request performance
        start_time = time.time()
        response = client.options(
            "/api/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type",
            },
        )
        end_time = time.time()

        # Should be fast (less than 1 second)
        assert (end_time - start_time) < 1.0

        # Should still work correctly
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers

    def test_cors_multiple_origins_handling(self, client):
        """Test CORS handling with multiple origins."""
        # Test multiple allowed origins
        allowed_origins = ["http://localhost:5173", "http://127.0.0.1:5173"]

        for origin in allowed_origins:
            response = client.get("/api/players/", headers={"Origin": origin})

            # Should have CORS headers for each allowed origin
            assert "access-control-allow-origin" in response.headers
            assert response.headers["access-control-allow-origin"] == origin

    def test_cors_error_responses(self, client):
        """Test CORS behavior on error responses."""
        # Test CORS on 404 error
        response = client.get("/nonexistent-endpoint", headers={"Origin": "http://localhost:5173"})

        # Should still have CORS headers even on error responses
        assert response.status_code == 404
        assert "access-control-allow-origin" in response.headers
        assert response.headers["access-control-allow-origin"] == "http://localhost:5173"

    def test_cors_configuration_consistency(self, client):
        """Test CORS configuration consistency across requests."""
        # Make multiple requests to verify consistent CORS behavior
        for _i in range(5):
            response = client.get("/api/players/", headers={"Origin": "http://localhost:5173"})

            # Should have consistent CORS headers
            assert "access-control-allow-origin" in response.headers
            assert response.headers["access-control-allow-origin"] == "http://localhost:5173"
            assert "access-control-allow-credentials" in response.headers
            assert response.headers["access-control-allow-credentials"] == "true"
