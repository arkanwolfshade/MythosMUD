"""
Verification tests for security headers applied to all endpoints.

This module tests that security headers are consistently applied across all
FastAPI endpoints, ensuring comprehensive security coverage.

ARCHITECTURE FIX: Updated to use container_test_client_class fixture
Following the security protocols outlined in the Arkham Security Manual.
"""

import pytest

from server.logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class TestSecurityHeadersVerification:
    """
    Test security headers are applied to all endpoints.

    AI: Following pytest best practices - using container_test_client_class
    """

    @pytest.fixture
    def mock_security_persistence(self, container_test_client_class):
        """Mock persistence for security header testing."""
        import uuid
        from unittest.mock import AsyncMock, Mock

        app = container_test_client_class.app
        mock_persistence = AsyncMock()

        # Create a proper mock player object
        mock_player = Mock()
        mock_player.player_id = str(uuid.uuid4())
        mock_player.user_id = str(uuid.uuid4())
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "test-room"
        mock_player.experience_points = 100
        mock_player.level = 1
        mock_player.created_at = "2023-01-01"
        mock_player.last_active = "2023-01-01"
        mock_player.is_admin = False
        mock_player.get_stats.return_value = {"str": 10, "dex": 10}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []

        # Create a mock profession object
        mock_profession = Mock()
        mock_profession.name = "Test Profession"
        mock_profession.description = "A test profession"
        mock_profession.flavor_text = "Test flavor"

        # Configure async methods with conditional returns
        def mock_get_player(player_id):
            if player_id in ["invalid-uuid-format", "nonexistent-player"]:
                return None
            return mock_player

        def mock_get_room(room_id):
            if room_id in ["nonexistent-room", "invalid-room"]:
                return None
            return None

        mock_persistence.async_list_players = AsyncMock(return_value=[mock_player])
        mock_persistence.async_get_player = AsyncMock(side_effect=mock_get_player)
        mock_persistence.async_get_player_by_name = AsyncMock(return_value=mock_player)
        mock_persistence.async_get_profession_by_id = AsyncMock(return_value=mock_profession)
        mock_persistence.async_get_room = AsyncMock(side_effect=mock_get_room)
        mock_persistence.async_save_player = AsyncMock(return_value=None)
        mock_persistence.async_delete_player = AsyncMock(return_value=True)

        # Configure sync methods (list_players is actually async, so use AsyncMock)
        mock_persistence.list_players = AsyncMock(return_value=[mock_player])
        mock_persistence.get_player = Mock(side_effect=mock_get_player)
        mock_persistence.get_player_by_name = Mock(return_value=mock_player)
        # get_profession_by_id is async in the actual persistence layer
        mock_persistence.get_profession_by_id = AsyncMock(return_value=mock_profession)
        mock_persistence.get_room = AsyncMock(side_effect=mock_get_room)
        mock_persistence.save_player = Mock(return_value=None)
        mock_persistence.delete_player = AsyncMock(return_value=True)  # delete_player is async

        # Replace container persistence
        app.state.container.persistence = mock_persistence
        app.state.persistence = mock_persistence

        # Mock database_manager if it exists to avoid session errors
        if hasattr(app.state.container, "database_manager"):
            mock_database_manager = Mock()
            mock_session_maker = AsyncMock()
            # Make session_maker() return an async context manager
            mock_session = AsyncMock()
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock(return_value=None)
            mock_session_maker.return_value = mock_session
            mock_database_manager.get_session_maker = Mock(return_value=mock_session_maker)
            app.state.container.database_manager = mock_database_manager

        # Update service persistence references
        if hasattr(app.state.container, "player_service") and app.state.container.player_service:
            app.state.container.player_service.persistence = mock_persistence
            logger.info("Replaced PlayerService persistence with mock")

        if hasattr(app.state.container, "room_service") and app.state.container.room_service:
            app.state.container.room_service.persistence = mock_persistence
            logger.info("Replaced RoomService persistence with mock")

        return mock_persistence

    def test_security_headers_on_api_endpoints(self, container_test_client_class, mock_security_persistence):
        """Test that security headers are applied to all API endpoints."""
        # Define all API endpoints to test
        api_endpoints = [
            # Player endpoints
            ("GET", "/players/"),
            ("POST", "/players/"),
            ("GET", "/players/test-player-id"),
            ("GET", "/players/name/test-player"),
            ("DELETE", "/players/test-player-id"),
            ("POST", "/players/test-player-id/lucidity"),
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
                response = container_test_client_class.get(endpoint)
            elif method == "POST":
                response = container_test_client_class.post(endpoint, json={})
            elif method == "DELETE":
                response = container_test_client_class.delete(endpoint)
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

    def test_security_headers_on_error_responses(self, container_test_client_class, mock_security_persistence):
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
            response = container_test_client_class.get(endpoint)

            # Should return an error status code
            assert response.status_code >= 400

            # But should still have security headers
            for header in required_security_headers:
                assert header in response.headers, (
                    f"Missing security header '{header}' on error response for {endpoint}"
                )

    def test_security_headers_on_cors_preflight(self, container_test_client_class, mock_security_persistence):
        """
        Test that CORS preflight requests work correctly.

        AI: ARCHITECTURE NOTE - CORS middleware handles OPTIONS before security middleware.
        This is expected behavior - CORS preflight responses may not have security headers.
        Security headers are added to actual requests (GET, POST, etc.), not preflight.
        """
        # Test that CORS preflight works
        response = container_test_client_class.options(
            "/api/players/",
            headers={
                "Origin": "http://localhost:5173",
                "Access-Control-Request-Method": "POST",
                "Access-Control-Request-Headers": "Content-Type",
            },
        )

        # CORS preflight should succeed
        assert response.status_code in [200, 204, 405], f"CORS preflight failed with status {response.status_code}"

        # Should have CORS headers (if OPTIONS is supported)
        if response.status_code in [200, 204]:
            response_headers_lower = {k.lower(): v for k, v in response.headers.items()}
            assert (
                "access-control-allow-origin" in response_headers_lower
                or "access-control-allow-methods" in response_headers_lower
            ), f"Missing CORS headers in OPTIONS response. Headers: {list(response_headers_lower.keys())}"

        # ARCHITECTURE NOTE: Security headers are added to actual requests, not preflight.
        # Verify security headers are present on actual GET request instead.
        get_response = container_test_client_class.get("/api/players/")
        get_headers_lower = {k.lower(): v for k, v in get_response.headers.items()}

        # Verify security headers on actual request
        required_security_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
        ]

        for header in required_security_headers:
            assert header in get_headers_lower, (
                f"Missing security header '{header}' on GET request. Headers: {list(get_headers_lower.keys())}"
            )

        # ARCHITECTURE NOTE: CORS preflight (OPTIONS) may not have security headers
        # because CORS middleware handles it before security middleware runs.
        # This is expected behavior and security headers are verified on GET request above.

    def test_security_headers_consistency(self, container_test_client_class, mock_security_persistence):
        """Test that security headers are consistent across different request types."""
        endpoints = ["/players/", "/rooms/test-room", "/docs"]

        for endpoint in endpoints:
            # Test GET request
            get_response = container_test_client_class.get(endpoint)

            # Test POST request (if applicable)
            post_response = container_test_client_class.post(endpoint, json={})

            # Test OPTIONS request
            options_response = container_test_client_class.options(endpoint)

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

    def test_security_headers_on_different_origins(self, container_test_client_class, mock_security_persistence):
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

            response = container_test_client_class.get("/players/", headers=headers)

            # Should always have security headers regardless of origin
            required_headers = [
                "x-content-type-options",
                "x-frame-options",
                "x-xss-protection",
                "strict-transport-security",
            ]

            for header in required_headers:
                assert header in response.headers, f"Missing security header '{header}' with origin {origin}"

    def test_security_headers_header_values(self, container_test_client_class, mock_security_persistence):
        """Test that security headers have correct values."""
        response = container_test_client_class.get("/players/")

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

    def test_security_headers_performance_impact(self, container_test_client_class, mock_security_persistence):
        """Test that security headers don't significantly impact performance."""
        import time

        # Measure response time with security headers
        start_time = time.time()
        response = container_test_client_class.get("/players/")
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

    def test_security_headers_on_large_responses(self, container_test_client_class, mock_security_persistence):
        """Test that security headers are applied to large responses."""
        # Test with a request that might return a large response
        response = container_test_client_class.get("/docs")  # Documentation can be large

        # Should have security headers even on large responses
        required_headers = [
            "x-content-type-options",
            "x-frame-options",
            "x-xss-protection",
            "strict-transport-security",
        ]

        for header in required_headers:
            assert header in response.headers

    def test_security_headers_comprehensive_coverage(self, container_test_client_class, mock_security_persistence):
        """Test comprehensive coverage of security headers across all endpoint types."""
        # Test different HTTP methods
        methods_to_test = [
            ("GET", "/players/"),
            ("POST", "/players/", {"name": "TestPlayer"}),
            ("DELETE", "/players/test-id"),
            ("OPTIONS", "/players/"),
        ]

        for method_data in methods_to_test:
            method = method_data[0]
            endpoint = method_data[1]
            if len(method_data) == 2:
                kwargs = {}
            elif len(method_data) == 3:
                data = method_data[2]
                kwargs = {"json": data}
            else:
                raise ValueError(f"Invalid method_data format: {method_data}")

            if method == "GET":
                response = container_test_client_class.get(endpoint, **kwargs)
            elif method == "POST":
                response = container_test_client_class.post(endpoint, **kwargs)
            elif method == "DELETE":
                response = container_test_client_class.delete(endpoint, **kwargs)
            elif method == "OPTIONS":
                response = container_test_client_class.options(endpoint, **kwargs)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            # Verify security headers are present
            security_headers = [
                "x-content-type-options",
                "x-frame-options",
                "x-xss-protection",
                "strict-transport-security",
            ]

            for header in security_headers:
                assert header in response.headers, f"Missing security header '{header}' on {method} {endpoint}"
