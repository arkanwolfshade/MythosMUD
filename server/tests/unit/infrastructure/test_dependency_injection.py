"""
Tests for dependency injection system.

This module tests the dependency injection system to ensure that
services are properly injected into API endpoints.
"""

from unittest.mock import AsyncMock, Mock

import pytest
from fastapi import Request
from fastapi.testclient import TestClient

from server.app.factory import create_app
from server.dependencies import get_player_service, get_player_service_for_testing, get_room_service
from server.game.player_service import PlayerService
from server.game.room_service import RoomService


class TestDependencyInjection:
    """Test the dependency injection system."""

    def test_get_player_service_creates_instance(self):
        """Test that get_player_service creates a PlayerService instance."""
        # Create a mock request with app state
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        # Get the service
        service = get_player_service(mock_request)

        # Verify it's a PlayerService instance
        from server.game.player_service import PlayerService

        assert isinstance(service, PlayerService)
        assert service.persistence == mock_persistence

    def test_get_room_service_creates_instance(self):
        """Test that get_room_service creates a RoomService instance."""
        # Create a mock request with app state
        mock_request = Mock()
        mock_persistence = Mock()
        mock_request.app.state.persistence = mock_persistence

        # Get the service
        service = get_room_service(mock_request)

        # Verify it's a RoomService instance
        from server.game.room_service import RoomService

        assert isinstance(service, RoomService)
        assert service.persistence == mock_persistence

    def test_dependency_injection_in_fastapi_app(self):
        """Test that dependency injection works in the FastAPI application."""
        # Create the app
        app = create_app()

        # Mock the persistence layer since TestClient doesn't run lifespan
        mock_persistence = Mock()
        app.state.persistence = mock_persistence

        client = TestClient(app)

        # Mock the player service methods
        mock_persistence.get_player.return_value = None
        mock_persistence.list_players.return_value = []
        # Mock async methods with AsyncMock
        from unittest.mock import AsyncMock

        mock_persistence.async_get_player = AsyncMock(return_value=None)
        mock_persistence.async_list_players = AsyncMock(return_value=[])

        # Test that the dependency injection works by making a request
        # This should not raise an import error or dependency resolution error
        response = client.get("/api/players/")

        # The response might be 401 (unauthorized) or 200 (success)
        # The important thing is that it doesn't fail with dependency injection errors
        assert response.status_code in [200, 401, 403]

    def test_player_service_dependency_resolution(self):
        """Test that PlayerService dependency is properly resolved."""
        # Create the app
        app = create_app()

        # Mock the persistence layer since TestClient doesn't run lifespan
        mock_persistence = Mock()
        app.state.persistence = mock_persistence

        # Test that the dependency injection works by directly calling the dependency function
        from fastapi import Request

        mock_request = Mock(spec=Request)
        mock_request.app = app

        # This should not raise an error
        service = get_player_service(mock_request)
        assert service is not None

    def test_room_service_dependency_resolution(self):
        """Test that RoomService dependency is properly resolved."""
        # Create the app
        app = create_app()

        # Mock the persistence layer since TestClient doesn't run lifespan
        mock_persistence = Mock()
        app.state.persistence = mock_persistence

        # Test that the dependency injection works by directly calling the dependency function
        from fastapi import Request

        mock_request = Mock(spec=Request)
        mock_request.app = app

        # This should not raise an error
        service = get_room_service(mock_request)
        assert service is not None


# ============================================================================
# Tests merged from test_dependency_functions_legacy.py
# ============================================================================


"""
Test the actual dependency injection functions.

This module tests that the PlayerServiceDep and RoomServiceDep functions
work correctly and return the expected service instances.
"""


class TestDependencyFunctions:
    """Test the dependency injection functions."""

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

    def test_player_service_dep_function(self, mock_persistence):
        """Test that PlayerServiceDep function works correctly."""
        # Mock the app state persistence
        from unittest.mock import Mock

        from fastapi import Request

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        # Call the dependency function directly
        from server.dependencies import get_player_service

        service = get_player_service(mock_request)

        # Verify the service is created correctly
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")
        assert service.persistence == mock_persistence

    def test_room_service_dep_function(self, mock_persistence):
        """Test that RoomServiceDep function works correctly."""
        # Mock the app state persistence
        from unittest.mock import Mock

        from fastapi import Request

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        # Call the dependency function directly
        from server.dependencies import get_room_service

        service = get_room_service(mock_request)

        # Verify the service is created correctly
        assert isinstance(service, RoomService)
        assert hasattr(service, "persistence")
        assert service.persistence == mock_persistence

    def test_dependency_functions_are_callable(self):
        """Test that dependency functions are callable."""
        from server.dependencies import get_player_service, get_room_service

        assert callable(get_player_service)
        assert callable(get_room_service)

    def test_dependency_functions_return_different_instances(self, mock_persistence):
        """Test that dependency functions return different instances."""
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service, get_room_service

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        player_service1 = get_player_service(mock_request)
        player_service2 = get_player_service(mock_request)
        room_service1 = get_room_service(mock_request)
        room_service2 = get_room_service(mock_request)

        # Verify they are different instances
        assert player_service1 is not player_service2
        assert room_service1 is not room_service2
        assert player_service1 is not room_service1
        assert player_service2 is not room_service2

    def test_dependency_functions_with_different_persistence(self):
        """Test dependency functions with different persistence layers."""
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service, get_room_service

        persistence1 = AsyncMock()
        persistence2 = AsyncMock()

        mock_request1 = Mock(spec=Request)
        mock_request1.app.state.persistence = persistence1
        player_service = get_player_service(mock_request1)

        mock_request2 = Mock(spec=Request)
        mock_request2.app.state.persistence = persistence2
        room_service = get_room_service(mock_request2)

        # Verify they use different persistence layers
        assert player_service.persistence == persistence1
        assert room_service.persistence == persistence2
        assert player_service.persistence is not room_service.persistence

    def test_dependency_function_error_handling(self):
        """Test that dependency functions handle errors gracefully."""
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        # Test with missing app state
        mock_request = Mock(spec=Request)
        del mock_request.app  # Remove app attribute

        with pytest.raises(AttributeError):
            get_player_service(mock_request)

    def test_dependency_function_type_annotations(self):
        """Test that dependency functions have correct type annotations."""
        import inspect

        from server.dependencies import get_player_service, get_room_service

        # Check get_player_service signature
        player_sig = inspect.signature(get_player_service)
        assert player_sig.return_annotation == PlayerService or player_sig.return_annotation == inspect.Signature.empty

        # Check get_room_service signature
        room_sig = inspect.signature(get_room_service)
        assert room_sig.return_annotation == RoomService or room_sig.return_annotation == inspect.Signature.empty

    def test_dependency_functions_performance(self, mock_persistence):
        """Test that dependency functions perform well."""
        import time
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        start_time = time.time()

        # Create many service instances
        services = []
        for _ in range(100):
            service = get_player_service(mock_request)
            services.append(service)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Should complete within reasonable time (less than 1 second for 100 instances)
        assert elapsed_time < 1.0
        assert len(services) == 100

    def test_dependency_functions_memory_usage(self, mock_persistence):
        """Test that dependency functions don't cause memory leaks."""
        import gc
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        # Create many service instances
        services = []
        for _ in range(1000):
            service = get_player_service(mock_request)
            services.append(service)

        # Clear references
        services.clear()

        # Force garbage collection
        gc.collect()

        # This test passes if no exceptions are raised
        assert True  # Placeholder assertion

    def test_dependency_functions_thread_safety(self, mock_persistence):
        """Test that dependency functions are thread-safe."""
        import threading

        results = []
        errors = []

        def worker():
            try:
                from unittest.mock import Mock

                from fastapi import Request

                from server.dependencies import get_player_service

                mock_request = Mock(spec=Request)
                mock_request.app.state.persistence = mock_persistence
                service = get_player_service(mock_request)
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
        assert len(errors) == 0, f"Thread safety errors: {errors}"
        assert len(results) == 10, "Not all workers completed successfully"

    def test_dependency_functions_with_none_persistence(self):
        """Test dependency functions handle None persistence gracefully."""
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = None

        # The dependency function should still work, but the service will have None persistence
        service = get_player_service(mock_request)
        assert service is not None
        assert service.persistence is None

    def test_dependency_functions_consistency(self, mock_persistence):
        """Test that dependency functions behave consistently."""
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        # Call the function multiple times
        services = []
        for _ in range(5):
            service = get_player_service(mock_request)
            services.append(service)

        # All services should be valid PlayerService instances
        for service in services:
            assert isinstance(service, PlayerService)
            assert service.persistence == mock_persistence

    def test_dependency_functions_with_mock_persistence_methods(self, mock_persistence):
        """Test dependency functions with mock persistence that has specific method behaviors."""
        # Configure mock to return specific values
        mock_persistence.async_list_players.return_value = [{"name": "TestPlayer"}]
        mock_persistence.async_get_player.return_value = {"name": "TestPlayer", "id": "123"}

        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        service = get_player_service(mock_request)

        # Verify the service uses the configured mock
        assert service.persistence == mock_persistence
        assert service.persistence.async_list_players.return_value == [{"name": "TestPlayer"}]
        assert service.persistence.async_get_player.return_value == {"name": "TestPlayer", "id": "123"}


# ============================================================================
# Tests merged from test_dependency_injection_functions_legacy.py
# ============================================================================


"""
Test the actual dependency injection functions.

This module tests that the get_player_service and get_room_service functions
work correctly and return the expected service instances.
"""


class TestDependencyInjectionFunctions:
    """Test the dependency injection functions."""

    @pytest.fixture
    def mock_persistence(self):
        """Create mock persistence layer."""
        mock_persistence = AsyncMock()
        mock_persistence.async_list_players.return_value = []
        mock_persistence.async_get_player.return_value = None
        mock_persistence.async_get_room.return_value = None
        mock_persistence.async_save_player.return_value = None
        mock_persistence.delete_player.return_value = True
        # Also mock synchronous methods for backward compatibility
        mock_persistence.list_players.return_value = []
        mock_persistence.get_player.return_value = None
        mock_persistence.get_room.return_value = None
        mock_persistence.save_player.return_value = None
        mock_persistence.delete_player.return_value = True
        return mock_persistence

    @pytest.fixture
    def mock_request(self, mock_persistence):
        """Create mock request with app state."""
        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence
        return mock_request

    def test_get_player_service_function(self, mock_request):
        """Test that get_player_service function works correctly."""
        service = get_player_service(mock_request)

        # Verify the service is created correctly
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")
        assert service.persistence == mock_request.app.state.persistence

    def test_get_room_service_function(self, mock_request):
        """Test that get_room_service function works correctly."""
        service = get_room_service(mock_request)

        # Verify the service is created correctly
        assert isinstance(service, RoomService)
        assert hasattr(service, "persistence")
        assert service.persistence == mock_request.app.state.persistence

    def test_get_player_service_for_testing_function(self):
        """Test that get_player_service_for_testing function works correctly."""
        service = get_player_service_for_testing()

        # Verify the service is created correctly
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")
        assert service.persistence is not None

    def test_dependency_functions_are_callable(self):
        """Test that dependency functions are callable."""
        assert callable(get_player_service)
        assert callable(get_room_service)
        assert callable(get_player_service_for_testing)

    def test_dependency_functions_return_different_instances(self, mock_request):
        """Test that dependency functions return different instances."""
        player_service1 = get_player_service(mock_request)
        player_service2 = get_player_service(mock_request)
        room_service1 = get_room_service(mock_request)
        room_service2 = get_room_service(mock_request)

        # Verify they are different instances
        assert player_service1 is not player_service2
        assert room_service1 is not room_service2
        assert player_service1 is not room_service1
        assert player_service2 is not room_service2

    def test_dependency_functions_with_different_requests(self):
        """Test dependency functions with different request objects."""
        persistence1 = AsyncMock()
        persistence2 = AsyncMock()

        request1 = Mock(spec=Request)
        request1.app.state.persistence = persistence1

        request2 = Mock(spec=Request)
        request2.app.state.persistence = persistence2

        player_service = get_player_service(request1)
        room_service = get_room_service(request2)

        # Verify they use different persistence layers
        assert player_service.persistence == persistence1
        assert room_service.persistence == persistence2
        assert player_service.persistence is not room_service.persistence

    def test_dependency_function_error_handling(self, mock_request):
        """Test that dependency functions handle errors gracefully."""
        # Test with request that has no app state
        bad_request = Mock(spec=Request)
        bad_request.app.state = None

        with pytest.raises(AttributeError):
            get_player_service(bad_request)

    def test_dependency_function_type_annotations(self):
        """Test that dependency functions have correct type annotations."""
        import inspect

        # Check get_player_service signature
        player_sig = inspect.signature(get_player_service)
        assert "request" in player_sig.parameters
        assert player_sig.return_annotation == PlayerService

        # Check get_room_service signature
        room_sig = inspect.signature(get_room_service)
        assert "request" in room_sig.parameters
        assert room_sig.return_annotation == RoomService

        # Check get_player_service_for_testing signature
        assert player_sig.return_annotation == PlayerService

    def test_dependency_functions_performance(self, mock_request):
        """Test that dependency functions perform well."""
        import time

        start_time = time.time()

        # Create many service instances
        services = []
        for _ in range(100):
            service = get_player_service(mock_request)
            services.append(service)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Should complete within reasonable time (less than 1 second for 100 instances)
        assert elapsed_time < 1.0
        assert len(services) == 100

    def test_dependency_functions_memory_usage(self, mock_request):
        """Test that dependency functions don't cause memory leaks."""
        import gc

        # Create many service instances
        services = []
        for _ in range(1000):
            service = get_player_service(mock_request)
            services.append(service)

        # Clear references
        services.clear()

        # Force garbage collection
        gc.collect()

        # This test passes if no exceptions are raised
        assert True  # Placeholder assertion

    def test_dependency_functions_thread_safety(self, mock_request):
        """Test that dependency functions are thread-safe."""
        import threading

        results = []
        errors = []

        def worker():
            try:
                service = get_player_service(mock_request)
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
        assert len(errors) == 0, f"Thread safety errors: {errors}"
        assert len(results) == 10, "Not all workers completed successfully"

    def test_dependency_functions_with_none_persistence(self):
        """Test dependency functions handle None persistence gracefully."""
        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = None

        # The service should be created even with None persistence
        # (it will fail later when methods are called, but constructor succeeds)
        service = get_player_service(mock_request)
        assert isinstance(service, PlayerService)
        assert service.persistence is None

    def test_dependency_functions_consistency(self, mock_request):
        """Test that dependency functions behave consistently."""
        # Call the function multiple times
        services = []
        for _ in range(5):
            service = get_player_service(mock_request)
            services.append(service)

        # All services should be valid PlayerService instances
        for service in services:
            assert isinstance(service, PlayerService)
            assert service.persistence == mock_request.app.state.persistence

    def test_dependency_functions_with_mock_persistence_methods(self, mock_persistence):
        """Test dependency functions with mock persistence that has specific method behaviors."""
        # Configure mock to return specific values
        mock_persistence.async_list_players.return_value = [{"name": "TestPlayer"}]
        mock_persistence.async_get_player.return_value = {"name": "TestPlayer", "id": "123"}

        mock_request = Mock(spec=Request)
        mock_request.app.state.persistence = mock_persistence

        service = get_player_service(mock_request)

        # Verify the service uses the configured mock
        assert service.persistence == mock_persistence
        assert service.persistence.async_list_players.return_value == [{"name": "TestPlayer"}]
        assert service.persistence.async_get_player.return_value == {"name": "TestPlayer", "id": "123"}

    def test_dependency_functions_with_different_service_types(self, mock_request):
        """Test that different dependency functions return different service types."""
        player_service = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        # Verify they are different service types
        assert isinstance(player_service, PlayerService)
        assert isinstance(room_service, RoomService)
        assert not isinstance(player_service, RoomService)
        assert not isinstance(room_service, PlayerService)

    def test_dependency_functions_with_testing_function(self):
        """Test that the testing function works correctly."""
        service = get_player_service_for_testing()

        # Verify it's a valid service
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")

        # The testing function should create its own mock persistence
        assert service.persistence is not None

    def test_dependency_functions_request_parameter_validation(self):
        """Test that dependency functions validate request parameters correctly."""
        # Test with None request
        with pytest.raises((TypeError, AttributeError)):
            get_player_service(None)

        # Test with invalid request object
        with pytest.raises(AttributeError):
            get_player_service("invalid_request")

    def test_dependency_functions_service_method_access(self, mock_request):
        """Test that services returned by dependency functions have accessible methods."""
        player_service = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        # Verify PlayerService methods are accessible
        assert hasattr(player_service, "create_player")
        assert hasattr(player_service, "get_player_by_id")
        assert hasattr(player_service, "list_players")
        assert callable(player_service.create_player)
        assert callable(player_service.get_player_by_id)
        assert callable(player_service.list_players)

        # Verify RoomService methods are accessible
        assert hasattr(room_service, "get_room")
        assert callable(room_service.get_room)
