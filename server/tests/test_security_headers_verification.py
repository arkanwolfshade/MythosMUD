"""
Verification tests for security headers applied to all endpoints.

This module tests that security headers are consistently applied across all
FastAPI endpoints, ensuring comprehensive security coverage.

Following the security protocols outlined in the Arkham Security Manual.
"""

import pytest
from fastapi.testclient import TestClient

from ..app.factory import create_app


class TestSecurityHeadersVerification:
    """Test security headers are applied to all endpoints."""

    @pytest.fixture
    def app(self):
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

        app.state.persistence = mock_persistence
        return app

    @pytest.fixture
    def client(self, app):
        """Create TestClient for testing."""
        return TestClient(app)

    def test_security_headers_on_api_endpoints(self, client):
        """Test that security headers are applied to all API endpoints."""
        # Define all API endpoints to test
        api_endpoints = [
            # Player endpoints
            ("GET", "/players/"),
            ("POST", "/players/"),
            ("GET", "/players/test-player-id"),
            ("GET", "/players/name/test-player"),
            ("DELETE", "/players/test-player-id"),
            ("POST", "/players/test-player-id/sanity"),
            ("POST", "/players/test-player-id/fear"),
            ("POST", "/players/test-player-id/corruption"),
            ("POST", "/players/test-player-id/occult-knowledge"),
            ("POST", "/players/test-player-id/heal"),
            ("POST", "/players/test-player-id/damage"),
            ("POST", "/players/roll-stats"),
            ("POST", "/players/create-character"),
            ("POST", "/players/validate-stats"),
            ("GET", "/players/available-classes"),
            ("GET", "/players/class-description/investigator"),
            # Room endpoints
            ("GET", "/rooms/test-room-id"),
            # Auth endpoints (if they exist)
            ("POST", "/auth/login"),
            ("POST", "/auth/logout"),
            # Documentation endpoints
            ("GET", "/docs"),
            ("GET", "/openapi.json"),
            ("GET", "/redoc"),
            # Health check endpoints
            ("GET", "/health"),
            ("GET", "/"),
        ]

        required_security_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
            "referrer-policy",
            "content-security-policy",
            "permissions-policy",
        ]

        for method, endpoint in api_endpoints:
            # Make request to endpoint
            if method == "GET":
                response = client.get(endpoint)
            elif method == "POST":
                response = client.post(endpoint, json={})
            elif method == "DELETE":
                response = client.delete(endpoint)
            else:
                continue

            # Verify all required security headers are present
            for header in required_security_headers:
                assert header in response.headers, f"Missing security header '{header}' on {method} {endpoint}"

            # Verify specific header values
            assert response.headers["x-content-type-options"] == "nosniff"
            assert response.headers["x-frame-options"] == "DENY"
            assert response.headers["x-xss-protection"] == "1; mode=block"
            assert "max-age=" in response.headers["strict-transport-security"]

    def test_security_headers_on_error_responses(self, client):
        """Test that security headers are applied even to error responses."""
        error_endpoints = [
            "/nonexistent-endpoint",
            "/players/invalid-uuid-format",
            "/rooms/nonexistent-room",
        ]

        required_security_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
        ]

        for endpoint in error_endpoints:
            response = client.get(endpoint)

            # Should return an error status code
            assert response.status_code >= 400

            # But should still have security headers
            for header in required_security_headers:
                assert header in response.headers, (
                    f"Missing security header '{header}' on error response for {endpoint}"
                )

    def test_security_headers_on_cors_preflight(self, client):
        """Test that security headers are applied to CORS preflight requests."""
        response = client.options(
            "/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type",
            },
        )

        # Should have CORS headers
        assert "access-control-allow-origin" in response.headers

        # Should also have security headers
        required_security_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
        ]

        for header in required_security_headers:
            assert header in response.headers, f"Missing security header '{header}' on CORS preflight"

    def test_security_headers_consistency(self, client):
        """Test that security headers are consistent across different request types."""
        endpoints = ["/players/", "/rooms/test-room", "/docs"]

        for endpoint in endpoints:
            # Test GET request
            get_response = client.get(endpoint)

            # Test POST request (if applicable)
            post_response = client.post(endpoint, json={})

            # Test OPTIONS request
            options_response = client.options(endpoint)

            responses = [get_response, post_response, options_response]

            # Verify all responses have the same security headers
            security_headers = [
                "x-content-type-options",
                "x-frame-options",
                "x-xss-protection",
                "strict-transport-security",
            ]

            for header in security_headers:
                values = []
                for response in responses:
                    if header in response.headers:
                        values.append(response.headers[header])

                # All responses should have the same security header values
                if values:
                    assert all(v == values[0] for v in values), (
                        f"Inconsistent '{header}' values across requests to {endpoint}"
                    )

    def test_security_headers_on_different_origins(self, client):
        """Test that security headers are applied regardless of origin."""
        origins = [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "https://example.com",
            None,  # No origin header
        ]

        for origin in origins:
            headers = {}
            if origin:
                headers["Origin"] = origin

            response = client.get("/players/", headers=headers)

            # Should always have security headers regardless of origin
            required_headers = [
                "x-content-type-options",
                "x-frame-options",
                "x-xss-protection",
                "strict-transport-security",
            ]

            for header in required_headers:
                assert header in response.headers, f"Missing security header '{header}' with origin {origin}"

    def test_security_headers_header_values(self, client):
        """Test that security headers have correct values."""
        response = client.get("/players/")

        # Verify specific security header values
        assert response.headers["x-content-type-options"] == "nosniff"
        assert response.headers["x-frame-options"] == "DENY"
        assert response.headers["x-xss-protection"] == "1; mode=block"
        assert "max-age=" in response.headers["strict-transport-security"]
        assert "includeSubDomains" in response.headers["strict-transport-security"]
        assert response.headers["referrer-policy"] == "strict-origin-when-cross-origin"
        assert response.headers["content-security-policy"] == "default-src 'self'"

        # Verify permissions policy has restrictive settings
        permissions_policy = response.headers["permissions-policy"]
        assert "geolocation=()" in permissions_policy
        assert "microphone=()" in permissions_policy
        assert "camera=()" in permissions_policy

    def test_security_headers_performance_impact(self, client):
        """Test that security headers don't significantly impact performance."""
        import time

        # Measure response time with security headers
        start_time = time.time()
        response = client.get("/players/")
        end_time = time.time()

        response_time = end_time - start_time

        # Should be fast (less than 1 second)
        assert response_time < 1.0

        # Should still have all security headers
        required_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
        ]

        for header in required_headers:
            assert header in response.headers

    def test_security_headers_on_large_responses(self, client):
        """Test that security headers are applied to large responses."""
        # Test with a request that might return a large response
        response = client.get("/docs")  # Documentation can be large

        # Should have security headers even on large responses
        required_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
        ]

        for header in required_headers:
            assert header in response.headers

    def test_security_headers_comprehensive_coverage(self, client):
        """Test comprehensive coverage of security headers across all endpoint types."""
        # Test different HTTP methods
        methods_to_test = [
            ("GET", "/players/"),
            ("POST", "/players/", {"name": "TestPlayer"}),
            ("DELETE", "/players/test-id"),
            ("OPTIONS", "/players/"),
        ]

        for method_data in methods_to_test:
            if len(method_data) == 2:
                method, endpoint = method_data
                kwargs = {}
            else:
                method, endpoint, data = method_data
                kwargs = {"json": data}

            if method == "GET":
                response = client.get(endpoint, **kwargs)
            elif method == "POST":
                response = client.post(endpoint, **kwargs)
            elif method == "DELETE":
                response = client.delete(endpoint, **kwargs)
            elif method == "OPTIONS":
                response = client.options(endpoint, **kwargs)

            # Verify security headers are present
            security_headers = [
                "x-content-type-options",
                "x-frame-options",
                "x-xss-protection",
                "strict-transport-security",
            ]

            for header in security_headers:
                assert header in response.headers, f"Missing security header '{header}' on {method} {endpoint}"
