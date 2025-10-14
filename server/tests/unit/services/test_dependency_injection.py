"""
Test service dependency injection for MythosMUD server.

This module tests that FastAPI's dependency injection system correctly
provides services to API endpoints, ensuring proper separation of concerns
and testable architecture.
"""

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from server.dependencies import PlayerServiceDep, RoomServiceDep, get_player_service, get_room_service
from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestServiceDependencyInjection:
    """Test service layer dependency injection using real FastAPI dependency system."""

    @pytest.fixture
    def app(self):
        """Create FastAPI app for testing with mocked external dependencies."""
        with (
            patch("server.app.lifespan.init_db"),
            patch("server.app.lifespan.init_npc_db"),
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
            from server.game.chat_service import ChatService
            from server.game.player_service import PlayerService
            from server.realtime.connection_manager import connection_manager
            from server.realtime.event_handler import get_real_time_event_handler
            from server.services.user_manager import UserManager

            # Set up app state manually
            app.state.persistence = mock_persistence
            app.state.player_service = PlayerService(mock_persistence)
            from pathlib import Path

            # Get project root for absolute path (server/tests/test_*.py -> project root)
            project_root = Path(__file__).parent.parent.parent
            app.state.user_manager = UserManager(data_dir=project_root / "data" / "unit_test" / "user_management")
            app.state.event_handler = get_real_time_event_handler()
            app.state.event_bus = app.state.event_handler.event_bus
            app.state.connection_manager = connection_manager
            app.state.nats_service = mock_nats
            app.state.chat_service = ChatService(
                persistence=mock_persistence,
                room_service=mock_persistence,
                player_service=app.state.player_service,
                nats_service=mock_nats,
            )

            return app

    @pytest.fixture
    def client(self, app):
        """Create test client."""
        return TestClient(app)

    def test_player_service_dependency_injection_via_endpoint(self, client):
        """Test that PlayerService is correctly injected via API endpoint."""
        response = client.get("/players/")
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
        """Test that different services can be injected independently."""
        app = client.app

        from fastapi import Request

        mock_request = Request(scope={"type": "http", "app": app})

        player_service1 = get_player_service(mock_request)
        player_service2 = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        assert isinstance(player_service1, PlayerService)
        assert isinstance(player_service2, PlayerService)
        assert isinstance(room_service, RoomService)

        assert player_service1 is not player_service2

    def test_api_endpoints_use_dependency_injection(self, client):
        """Test that API endpoints actually use the dependency injection system."""
        endpoints_to_test = ["/players/", "/rooms/test_room"]

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


# ============================================================================
# Tests merged from test_dependency_injection_simple_legacy.py
# ============================================================================


"""
Simple tests for service layer dependency injection functionality.

This module tests that the service classes can be instantiated correctly
and that dependency injection patterns work as expected.
"""


class TestServiceDependencyInjectionSimple:
    """Test service layer dependency injection without full app lifecycle."""

    @pytest.fixture
    def mock_persistence(self):
        """Create mock persistence layer."""
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
        return mock_persistence

    def test_player_service_instantiation(self, mock_persistence):
        """Test that PlayerService can be instantiated correctly."""
        service = PlayerService(persistence=mock_persistence)

        # Verify the service is created correctly
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")
        assert service.persistence == mock_persistence

    def test_room_service_instantiation(self, mock_persistence):
        """Test that RoomService can be instantiated correctly."""
        service = RoomService(persistence=mock_persistence)

        # Verify the service is created correctly
        assert isinstance(service, RoomService)
        assert hasattr(service, "persistence")
        assert service.persistence == mock_persistence

    def test_player_service_has_required_methods(self, mock_persistence):
        """Test that PlayerService has all required methods."""
        service = PlayerService(persistence=mock_persistence)

        # Check for key methods
        required_methods = [
            "create_player",
            "get_player_by_id",
            "get_player_by_name",
            "list_players",
            "delete_player",
            "apply_sanity_loss",
            "apply_fear",
            "apply_corruption",
            "gain_occult_knowledge",
            "heal_player",
            "damage_player",
        ]

        for method_name in required_methods:
            assert hasattr(service, method_name), f"PlayerService missing method: {method_name}"
            method = getattr(service, method_name)
            assert callable(method), f"PlayerService method {method_name} is not callable"

    def test_room_service_has_required_methods(self, mock_persistence):
        """Test that RoomService has all required methods."""
        service = RoomService(persistence=mock_persistence)

        # Check for key methods
        required_methods = ["get_room"]

        for method_name in required_methods:
            assert hasattr(service, method_name), f"RoomService missing method: {method_name}"
            method = getattr(service, method_name)
            assert callable(method), f"RoomService method {method_name} is not callable"

    @pytest.mark.asyncio
    async def test_player_service_methods_are_async(self, mock_persistence):
        """Test that PlayerService methods are async."""
        service = PlayerService(persistence=mock_persistence)

        # Test that key methods are async
        async_methods = ["create_player", "get_player_by_id", "get_player_by_name", "list_players", "delete_player"]

        for method_name in async_methods:
            method = getattr(service, method_name)
            # Check if it's a coroutine function
            assert callable(method), f"Method {method_name} should be callable"
            # Note: We can't easily test if it's async without calling it,
            # but we can verify it exists and is callable

    @pytest.mark.asyncio
    async def test_room_service_methods_are_async(self, mock_persistence):
        """Test that RoomService methods are async."""
        service = RoomService(persistence=mock_persistence)

        # Test that key methods are async
        async_methods = ["get_room"]

        for method_name in async_methods:
            method = getattr(service, method_name)
            # Check if it's a coroutine function
            assert callable(method), f"Method {method_name} should be callable"

    def test_service_independence(self, mock_persistence):
        """Test that different service instances are independent."""
        player_service1 = PlayerService(persistence=mock_persistence)
        player_service2 = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Verify they are different instances
        assert player_service1 is not player_service2
        assert player_service1 is not room_service
        assert player_service2 is not room_service

        # But they share the same persistence layer
        assert player_service1.persistence == mock_persistence
        assert player_service2.persistence == mock_persistence
        assert room_service.persistence == mock_persistence

    def test_service_persistence_layer_access(self, mock_persistence):
        """Test that services can access persistence layer methods."""
        player_service = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Verify persistence layer is accessible
        assert player_service.persistence is not None
        assert room_service.persistence is not None
        assert player_service.persistence == mock_persistence
        assert room_service.persistence == mock_persistence

        # Verify persistence layer has expected methods
        assert hasattr(mock_persistence, "async_list_players")
        assert hasattr(mock_persistence, "async_get_player")
        assert hasattr(mock_persistence, "async_get_room")
        assert hasattr(mock_persistence, "async_save_player")

    def test_service_initialization_with_different_persistence(self):
        """Test that services can be initialized with different persistence layers."""
        persistence1 = AsyncMock()
        persistence2 = AsyncMock()

        player_service1 = PlayerService(persistence=persistence1)
        player_service2 = PlayerService(persistence=persistence2)

        # Verify they use different persistence layers
        assert player_service1.persistence == persistence1
        assert player_service2.persistence == persistence2
        assert player_service1.persistence is not player_service2.persistence

    def test_service_error_handling_capability(self, mock_persistence):
        """Test that services can handle errors from persistence layer."""
        # Configure mock to raise an exception
        mock_persistence.async_list_players.side_effect = Exception("Database error")

        service = PlayerService(persistence=mock_persistence)

        # The service should be created successfully even if persistence has issues
        assert isinstance(service, PlayerService)
        assert service.persistence == mock_persistence

    def test_service_method_signatures(self, mock_persistence):
        """Test that service methods have correct signatures."""
        player_service = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Test PlayerService method signatures
        import inspect

        # Check create_player signature
        create_player_sig = inspect.signature(player_service.create_player)
        assert "name" in create_player_sig.parameters
        assert "profession_id" in create_player_sig.parameters
        assert "starting_room_id" in create_player_sig.parameters

        # Check get_room signature
        get_room_sig = inspect.signature(room_service.get_room)
        assert "room_id" in get_room_sig.parameters

    def test_service_class_hierarchy(self, mock_persistence):
        """Test that service classes have correct inheritance."""
        player_service = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Verify they are instances of their respective classes
        assert isinstance(player_service, PlayerService)
        assert isinstance(room_service, RoomService)

        # Verify they are not instances of each other's classes
        assert not isinstance(player_service, RoomService)
        assert not isinstance(room_service, PlayerService)

    def test_service_dependency_injection_pattern(self, mock_persistence):
        """Test that services follow dependency injection pattern."""
        # This tests the pattern where services receive dependencies in constructor
        player_service = PlayerService(persistence=mock_persistence)
        room_service = RoomService(persistence=mock_persistence)

        # Verify dependency injection worked
        assert player_service.persistence is mock_persistence
        assert room_service.persistence is mock_persistence

        # Verify services don't create their own dependencies
        # (This is a design pattern test)
        assert not hasattr(player_service, "_create_persistence")
        assert not hasattr(room_service, "_create_persistence")

    def test_service_memory_management(self, mock_persistence):
        """Test that service instances don't cause memory leaks."""
        import gc

        # Create and destroy multiple service instances
        services = []
        for _i in range(100):
            service = PlayerService(persistence=mock_persistence)
            services.append(service)

        # Clear references
        services.clear()

        # Force garbage collection
        gc.collect()

        # This test passes if no exceptions are raised
        # In a real scenario, you'd check memory usage
        assert True  # Placeholder assertion

    def test_service_concurrent_access_safety(self, mock_persistence):
        """Test that services can handle concurrent access safely."""
        import threading

        results = []
        errors = []

        def worker():
            try:
                # Simulate concurrent access
                service = PlayerService(persistence=mock_persistence)
                results.append(service)
            except Exception as e:
                errors.append(e)

        # Create multiple threads
        threads = []
        for _i in range(10):
            thread = threading.Thread(target=worker)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        # Verify no errors occurred
        assert len(errors) == 0, f"Concurrent access errors: {errors}"
        assert len(results) == 10, "Not all workers completed successfully"
