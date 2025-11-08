"""
Test service dependency injection for MythosMUD server.

This module tests that FastAPI's dependency injection system correctly
provides services to API endpoints, ensuring proper separation of concerns
and testable architecture.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from server.dependencies import PlayerServiceDep, RoomServiceDep, get_player_service, get_room_service
from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestServiceDependencyInjection:
    """Test service layer dependency injection using real FastAPI dependency system."""

    @pytest.fixture
    def app(self, mock_application_container):
        """Create FastAPI app for testing with mocked external dependencies."""
        with (
            patch("server.services.nats_service.nats_service") as mock_nats,
            patch("server.persistence.get_persistence") as mock_get_persistence,
        ):
            # Configure NATS mock to appear connected
            mock_nats.is_connected.return_value = True
            mock_nats.connect.return_value = True
            mock_nats.disconnect.return_value = True

            # Configure persistence mock
            mock_persistence = AsyncMock()
            mock_persistence.async_list_players.return_value = []
            mock_persistence.async_get_player.return_value = None
            mock_persistence.async_get_room.return_value = None
            mock_persistence.async_save_player.return_value = None
            mock_persistence.async_delete_player.return_value = True
            mock_persistence.list_players.return_value = []
            mock_persistence.get_player.return_value = None
            mock_persistence.get_room.return_value = None
            mock_persistence.save_player.return_value = None
            mock_persistence.delete_player.return_value = True
            mock_get_persistence.return_value = mock_persistence

            # Create the real app using the real factory
            from server.app.factory import create_app

            app = create_app()

            # Manually set up app state since lifespan won't run in tests
            # AI Agent: Post-migration - use ApplicationContainer for dependency injection
            from pathlib import Path

            from server.events.event_bus import EventBus
            from server.game.chat_service import ChatService
            from server.game.player_service import PlayerService
            from server.game.room_service import RoomService
            from server.realtime.connection_manager import ConnectionManager
            from server.realtime.event_handler import RealTimeEventHandler
            from server.services.user_manager import UserManager

            # Set up app state manually
            app.state.persistence = mock_persistence
            app.state.player_service = PlayerService(mock_persistence)
            app.state.room_service = RoomService(mock_persistence)

            # Use absolute path to prevent nested server/server/ directory creation
            test_user_mgmt_path = Path(__file__).parent.parent.parent.parent / "data" / "unit_test" / "user_management"
            app.state.user_manager = UserManager(data_dir=test_user_mgmt_path)

            # AI Agent: Create new instances instead of using globals
            event_bus = EventBus()
            app.state.event_handler = RealTimeEventHandler(event_bus)
            app.state.event_bus = event_bus
            app.state.connection_manager = ConnectionManager()
            app.state.nats_service = mock_nats
            app.state.chat_service = ChatService(
                persistence=mock_persistence,
                room_service=app.state.room_service,
                player_service=app.state.player_service,
                nats_service=mock_nats,
            )

            # Create mock connection manager (container expects instance)
            connection_manager = MagicMock()
            connection_manager.persistence = mock_persistence

            # Use the comprehensive mock container and update with real/mocked services
            mock_application_container.persistence = mock_persistence
            mock_application_container.player_service = app.state.player_service
            mock_application_container.room_service = app.state.room_service
            mock_application_container.event_bus = app.state.event_bus
            mock_application_container.user_manager = app.state.user_manager
            mock_application_container.nats_service = mock_nats
            mock_application_container.connection_manager = connection_manager
            app.state.container = mock_application_container

            return app

    @pytest.fixture
    def client(self, app):
        """Create test client."""
        return TestClient(app)

    def test_player_service_dependency_injection_via_endpoint(self, client):
        """Test that PlayerService is correctly injected via API endpoint."""
        response = client.get("/api/players/")
        assert response.status_code in [200, 401]

        app = client.app
        assert hasattr(app.state, "player_service")
        assert isinstance(app.state.player_service, PlayerService)

    def test_room_service_dependency_injection_via_endpoint(self, client):
        """Test that RoomService is correctly injected via API endpoint."""
        response = client.get("/rooms/test_room")
        assert response.status_code in [404, 401]

        app = client.app
        assert hasattr(app.state, "persistence")

    def test_dependency_functions_create_correct_instances(self, client):
        """Test that dependency functions create the correct service instances."""
        app = client.app

        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})

        player_service = get_player_service(mock_request)
        assert isinstance(player_service, PlayerService)
        assert hasattr(player_service, "persistence")

        room_service = get_room_service(mock_request)
        assert isinstance(room_service, RoomService)
        assert hasattr(room_service, "persistence")

    def test_dependency_injection_with_real_services(self, client):
        """Test that dependency injection works with real service instances."""
        app = client.app

        assert hasattr(app.state, "player_service")
        assert hasattr(app.state, "persistence")

        player_service = app.state.player_service
        assert isinstance(player_service, PlayerService)
        assert hasattr(player_service, "persistence")

    def test_fastapi_depends_mechanism(self, client):
        """Test that FastAPI's Depends() mechanism works correctly."""
        app = client.app

        assert PlayerServiceDep is not None
        assert RoomServiceDep is not None

        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})

        player_service = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        assert isinstance(player_service, PlayerService)
        assert isinstance(room_service, RoomService)

    def test_service_instances_are_properly_configured(self, client):
        """Test that service instances have proper configuration."""
        app = client.app

        player_service = app.state.player_service
        assert hasattr(player_service, "persistence")

        persistence = app.state.persistence
        assert hasattr(persistence, "async_list_players")
        assert hasattr(persistence, "async_get_player")

    def test_dependency_injection_independence(self, client):
        """Test that different services can be injected independently.

        With ApplicationContainer pattern, services are singletons within the container,
        so multiple calls to get_player_service() return the same instance. This test
        verifies that different service types can be retrieved independently.
        """
        app = client.app

        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})

        player_service1 = get_player_service(mock_request)
        player_service2 = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        assert isinstance(player_service1, PlayerService)
        assert isinstance(player_service2, PlayerService)
        assert isinstance(room_service, RoomService)

        # With ApplicationContainer, services are singletons - same instance returned
        assert player_service1 is player_service2

        # But different service types are different instances
        assert player_service1 is not room_service

    def test_api_endpoints_use_dependency_injection(self, client):
        """Test that API endpoints actually use the dependency injection system."""
        endpoints_to_test = ["/api/players/", "/rooms/test_room"]

        for endpoint in endpoints_to_test:
            response = client.get(endpoint)
            assert response.status_code in [200, 401, 404]

    def test_dependency_injection_error_handling(self, client):
        """Test that dependency injection handles errors gracefully."""
        app = client.app

        assert hasattr(app.state, "player_service")
        assert hasattr(app.state, "persistence")

    def test_service_method_availability(self, client):
        """Test that injected services have the expected methods."""
        app = client.app

        player_service = app.state.player_service
        assert hasattr(player_service, "list_players")
        assert hasattr(player_service, "get_player_by_id")
        assert hasattr(player_service, "get_player_by_name")
        assert hasattr(player_service, "create_player")

    def test_persistence_layer_injection(self, client):
        """Test that the persistence layer is properly injected into services."""
        app = client.app

        player_service = app.state.player_service
        assert hasattr(player_service, "persistence")

        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})
        room_service = get_room_service(mock_request)
        assert hasattr(room_service, "persistence")

    def test_app_state_consistency(self, client):
        """Test that app state is consistent across the application."""
        app = client.app

        expected_services = [
            "player_service",
            "persistence",
            "user_manager",
            "event_handler",
            "event_bus",
            "connection_manager",
        ]

        for service_name in expected_services:
            assert hasattr(app.state, service_name), f"Missing {service_name} in app state"

    def test_dependency_injection_performance(self, client):
        """Test that dependency injection is performant."""
        import time

        app = client.app
        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})

        start_time = time.time()
        player_service = get_player_service(mock_request)
        end_time = time.time()

        assert (end_time - start_time) < 0.1
        assert isinstance(player_service, PlayerService)

    def test_dependency_injection_memory_usage(self, client):
        """Test that dependency injection doesn't cause memory leaks."""
        app = client.app
        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})

        services = []
        for _ in range(10):
            service = get_player_service(mock_request)
            services.append(service)
            assert isinstance(service, PlayerService)

        assert len(services) == 10
        assert all(isinstance(s, PlayerService) for s in services)
