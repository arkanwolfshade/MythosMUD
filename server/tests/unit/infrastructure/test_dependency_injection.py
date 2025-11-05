"""
Tests for dependency injection system.

This module tests the dependency injection system to ensure that
services are properly injected into API endpoints.
"""


class TestDependencyInjection:
    """Test the dependency injection system."""

    def test_dependency_injection_in_fastapi_app(self, container_test_client):
        """
        Test that dependency injection works in the FastAPI application with container.

        AI: ARCHITECTURE CHANGE - Updated to use container-based TestClient
        """
        # Test that the dependency injection works by making a request
        # This should not raise an import error or dependency resolution error
        response = container_test_client.get("/api/players/")

        # The response might be 401 (unauthorized), 422 (validation error), or 200 (success)
        # The important thing is that it doesn't fail with dependency injection errors
        assert response.status_code in [200, 401, 403, 422]
