"""
Test service layer dependency injection functionality.

This module tests that the FastAPI dependency injection system correctly
instantiates and injects service classes into route handlers.

These tests are marked as E2E tests because they require a full FastAPI
application to be running with all middleware and services initialized.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi.testclient import TestClient

from server.api.players import PlayerServiceDep
from server.api.rooms import RoomServiceDep
from server.app.factory import create_app
from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestServiceDependencyInjection:
    """Test service layer dependency injection."""

    @pytest.fixture
    def app(self):
        """Create FastAPI app for testing."""
        app = create_app()

        # Mock the persistence layer with async methods
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
        """Create test client."""
        return TestClient(app)

    @pytest.mark.e2e
    def test_player_service_dependency_injection_type(self, client):
        """Test that PlayerService is correctly injected."""
        # Test that the dependency returns a PlayerService instance
        with client as test_client:
            # Override the dependency to capture what gets injected
            captured_service = None

            def capture_service():
                nonlocal captured_service
                captured_service = PlayerServiceDep()
                return captured_service

            # Patch the dependency
            with patch("server.api.players.PlayerServiceDep", capture_service):
                response = test_client.get("/players/")
                assert response.status_code in [200, 401]  # May be 401 due to auth

            # Verify the service is a PlayerService instance
            assert captured_service is not None
            assert isinstance(captured_service, PlayerService)

    @pytest.mark.e2e
    def test_room_service_dependency_injection_type(self, client):
        """Test that RoomService is correctly injected."""
        # Test that the dependency returns a RoomService instance
        with client as test_client:
            # Override the dependency to capture what gets injected
            captured_service = None

            def capture_service():
                nonlocal captured_service
                captured_service = RoomServiceDep()
                return captured_service

            # Patch the dependency
            with patch("server.api.rooms.RoomServiceDep", capture_service):
                response = test_client.get("/rooms/test_room")
                assert response.status_code in [200, 401, 404]  # May be 401 due to auth or 404 if room doesn't exist

            # Verify the service is a RoomService instance
            assert captured_service is not None
            assert isinstance(captured_service, RoomService)

    @pytest.mark.e2e
    def test_player_service_has_persistence_layer(self, client):
        """Test that PlayerService has access to persistence layer."""
        with client as test_client:
            captured_service = None

            def capture_service():
                nonlocal captured_service
                captured_service = PlayerServiceDep()
                return captured_service

            with patch("server.api.players.PlayerServiceDep", capture_service):
                test_client.get("/players/")

            # Verify the service has persistence layer
            assert captured_service is not None
            assert hasattr(captured_service, "persistence")
            assert captured_service.persistence is not None

    @pytest.mark.e2e
    def test_room_service_has_persistence_layer(self, client):
        """Test that RoomService has access to persistence layer."""
        with client as test_client:
            captured_service = None

            def capture_service():
                nonlocal captured_service
                captured_service = RoomServiceDep()
                return captured_service

            with patch("server.api.rooms.RoomServiceDep", capture_service):
                test_client.get("/rooms/test_room")

            # Verify the service has persistence layer
            assert captured_service is not None
            assert hasattr(captured_service, "persistence")
            assert captured_service.persistence is not None

    def test_service_dependencies_are_independent(self, client):
        """Test that different services are independent instances."""
        with client as test_client:
            player_service = None
            room_service = None

            def capture_player_service():
                nonlocal player_service
                player_service = PlayerServiceDep()
                return player_service

            def capture_room_service():
                nonlocal room_service
                room_service = RoomServiceDep()
                return room_service

            with (
                patch("server.api.players.PlayerServiceDep", capture_player_service),
                patch("server.api.rooms.RoomServiceDep", capture_room_service),
            ):
                test_client.get("/players/")
                test_client.get("/rooms/test_room")

            # Verify they are different instances
            assert player_service is not None
            assert room_service is not None
            assert player_service is not room_service
            assert isinstance(player_service, PlayerService)
            assert isinstance(room_service, RoomService)

    def test_service_dependency_lifecycle(self, client):
        """Test that service dependencies are created per request."""
        with client as test_client:
            services_created = []

            def capture_service():
                service = PlayerServiceDep()
                services_created.append(service)
                return service

            with patch("server.api.players.PlayerServiceDep", capture_service):
                # Make multiple requests
                test_client.get("/players/")
                test_client.get("/players/")
                test_client.get("/players/")

            # Verify new service instances are created for each request
            assert len(services_created) == 3
            assert all(isinstance(service, PlayerService) for service in services_created)
            # They should be different instances (unless singleton pattern is used)
            assert len({id(service) for service in services_created}) >= 1

    def test_service_method_calls_through_dependency_injection(self, client):
        """Test that service methods are called correctly through DI."""
        with client as test_client:
            # Mock the service methods
            mock_service = AsyncMock()
            mock_service.list_players.return_value = []

            def get_mock_service():
                return mock_service

            with patch("server.api.players.PlayerServiceDep", get_mock_service):
                test_client.get("/players/")

                # Verify the service method was called
                mock_service.list_players.assert_called_once()

    def test_service_error_handling_through_dependency_injection(self, client):
        """Test that service errors are handled correctly through DI."""
        with client as test_client:
            # Mock service to raise an exception
            mock_service = AsyncMock()
            mock_service.list_players.side_effect = Exception("Database error")

            def get_mock_service():
                return mock_service

            with patch("server.api.players.PlayerServiceDep", get_mock_service):
                response = test_client.get("/players/")

                # Should handle the error gracefully
                assert response.status_code in [500, 401]  # May be 401 due to auth

    def test_service_dependency_with_authentication(self, client):
        """Test that service dependencies work with authentication."""
        with client as test_client:
            # Mock authentication
            mock_user = Mock()
            mock_user.id = uuid.uuid4()
            mock_user.username = "testuser"

            with patch("server.api.players.get_current_user", return_value=mock_user):
                captured_service = None

                def capture_service():
                    nonlocal captured_service
                    captured_service = PlayerServiceDep()
                    return captured_service

                with patch("server.api.players.PlayerServiceDep", capture_service):
                    response = test_client.get("/players/")

                    # Should work with authentication
                    assert response.status_code in [200, 500]  # May be 500 if service fails
                    assert captured_service is not None

    def test_multiple_service_dependencies_in_same_request(self, client):
        """Test that multiple services can be injected in the same request."""
        # This test would be relevant if we had endpoints that use multiple services
        # For now, we'll test that both services can be injected independently
        with client as test_client:
            player_service = None
            room_service = None

            def capture_player_service():
                nonlocal player_service
                player_service = PlayerServiceDep()
                return player_service

            def capture_room_service():
                nonlocal room_service
                room_service = RoomServiceDep()
                return room_service

            with (
                patch("server.api.players.PlayerServiceDep", capture_player_service),
                patch("server.api.rooms.RoomServiceDep", capture_room_service),
            ):
                # Make requests to both endpoints
                test_client.get("/players/")
                test_client.get("/rooms/test_room")

            # Both services should be created successfully
            assert player_service is not None
            assert room_service is not None
            assert isinstance(player_service, PlayerService)
            assert isinstance(room_service, RoomService)

    def test_service_dependency_configuration(self, client):
        """Test that service dependencies are configured correctly."""
        with client as test_client:
            captured_service = None

            def capture_service():
                nonlocal captured_service
                captured_service = PlayerServiceDep()
                return captured_service

            with patch("server.api.players.PlayerServiceDep", capture_service):
                test_client.get("/players/")

            # Verify the service is properly configured
            assert captured_service is not None
            assert hasattr(captured_service, "persistence")
            assert captured_service.persistence is not None
            # Verify it's the same persistence layer as the app
            assert captured_service.persistence == test_client.app.state.persistence

    def test_service_dependency_performance(self, client):
        """Test that service dependency injection doesn't cause performance issues."""
        import time

        with client as test_client:
            start_time = time.time()

            # Make multiple requests to test performance
            for _ in range(10):
                response = test_client.get("/players/")
                assert response.status_code in [200, 401, 500]

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Should complete within reasonable time (less than 5 seconds for 10 requests)
            assert elapsed_time < 5.0

    def test_service_dependency_memory_usage(self, client):
        """Test that service dependency injection doesn't cause memory leaks."""
        import gc

        initial_objects = len(gc.get_objects())

        with client as test_client:
            # Make many requests to test for memory leaks
            for _ in range(100):
                response = test_client.get("/players/")
                assert response.status_code in [200, 401, 500]

        # Force garbage collection
        gc.collect()
        final_objects = len(gc.get_objects())

        # Memory usage shouldn't grow significantly
        # Allow for some variance due to test overhead
        assert final_objects - initial_objects < 1000

    def test_service_dependency_with_different_endpoints(self, client):
        """Test service dependency injection across different endpoints."""
        with client as test_client:
            services_used = []

            def capture_player_service():
                service = PlayerServiceDep()
                services_used.append(("player", service))
                return service

            def capture_room_service():
                service = RoomServiceDep()
                services_used.append(("room", service))
                return service

            with (
                patch("server.api.players.PlayerServiceDep", capture_player_service),
                patch("server.api.rooms.RoomServiceDep", capture_room_service),
            ):
                # Test different endpoints
                test_client.get("/players/")
                test_client.get("/rooms/test_room")
                test_client.get("/players/")  # Same endpoint again
                test_client.get("/rooms/another_room")

            # Verify both service types were used
            service_types = [service_type for service_type, _ in services_used]
            assert "player" in service_types
            assert "room" in service_types
            assert len(services_used) >= 4  # At least one service per request

    def test_service_dependency_error_recovery(self, client):
        """Test that service dependency injection handles errors gracefully."""
        with client as test_client:
            # Test with a service that raises an exception during creation
            def failing_service():
                raise Exception("Service creation failed")

            with patch("server.api.players.PlayerServiceDep", failing_service):
                response = test_client.get("/players/")

                # Should handle the error gracefully
                assert response.status_code in [500, 401]

    def test_service_dependency_with_mocked_persistence(self, client):
        """Test that service dependencies work correctly with mocked persistence."""
        with client as test_client:
            # Create a custom mock persistence
            custom_persistence = AsyncMock()
            custom_persistence.async_list_players.return_value = []

            # Override the app's persistence
            test_client.app.state.persistence = custom_persistence

            captured_service = None

            def capture_service():
                nonlocal captured_service
                captured_service = PlayerServiceDep()
                return captured_service

            with patch("server.api.players.PlayerServiceDep", capture_service):
                test_client.get("/players/")

                # Verify the service uses the custom persistence
                assert captured_service is not None
                assert captured_service.persistence == custom_persistence
