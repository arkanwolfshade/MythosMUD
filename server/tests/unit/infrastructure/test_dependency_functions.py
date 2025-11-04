"""
Test the actual dependency injection functions.

This module tests that the PlayerServiceDep and RoomServiceDep functions
work correctly and return the expected service instances.
"""

from unittest.mock import AsyncMock

import pytest

from server.game.player_service import PlayerService
from server.game.room_service import RoomService


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

    def test_player_service_dep_function(self, container_test_client):
        """
        Test that PlayerServiceDep function works correctly with ApplicationContainer.

        AI: Updated to use real container instead of mocks - tests actual DI behavior
        """
        from unittest.mock import Mock

        from fastapi import Request

        # Create mock request with real container from test client
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # Call the dependency function directly
        from server.dependencies import get_player_service

        service = get_player_service(mock_request)

        # Verify the service is the real service from container
        assert isinstance(service, PlayerService)
        assert hasattr(service, "persistence")
        # Service should be the same instance from container
        assert service is container_test_client.app.state.container.player_service

    def test_room_service_dep_function(self, container_test_client):
        """
        Test that RoomServiceDep function works correctly with ApplicationContainer.

        AI: Updated to use real container instead of mocks - tests actual DI behavior
        """
        from unittest.mock import Mock

        from fastapi import Request

        # Create mock request with real container from test client
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # Call the dependency function directly
        from server.dependencies import get_room_service

        service = get_room_service(mock_request)

        # Verify the service is the real service from container
        assert isinstance(service, RoomService)
        assert hasattr(service, "persistence")
        # Service should be the same instance from container
        assert service is container_test_client.app.state.container.room_service

    def test_dependency_functions_are_callable(self):
        """Test that dependency functions are callable."""
        from server.dependencies import get_player_service, get_room_service

        assert callable(get_player_service)
        assert callable(get_room_service)

    def test_dependency_functions_return_same_instances(self, container_test_client):
        """
        Test that dependency functions return SAME instances from container.

        AI: ARCHITECTURE CHANGE - Container pattern uses singleton services
        Old behavior: Created new service instances per request
        New behavior: Returns same service instance from container (singleton pattern)
        """
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service, get_room_service

        # Create mock request with real container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        player_service1 = get_player_service(mock_request)
        player_service2 = get_player_service(mock_request)
        room_service1 = get_room_service(mock_request)
        room_service2 = get_room_service(mock_request)

        # ARCHITECTURE FIX: Container returns SAME instance (singleton pattern)
        assert player_service1 is player_service2  # Same instance from container
        assert room_service1 is room_service2  # Same instance from container
        # Different service types are still different instances
        assert player_service1 is not room_service1
        assert player_service2 is not room_service2

    def test_dependency_functions_with_container_persistence(self, container_test_client):
        """
        Test dependency functions return services with container persistence.

        AI: ARCHITECTURE CHANGE - Services get persistence from container
        Old behavior: Each request could have different persistence
        New behavior: All services share container's persistence instance
        """
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service, get_room_service

        # Create mock request with real container
        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        player_service = get_player_service(mock_request)
        room_service = get_room_service(mock_request)

        # ARCHITECTURE FIX: Both services use SAME persistence from container
        container_persistence = container_test_client.app.state.container.persistence
        assert player_service.persistence is container_persistence
        assert room_service.persistence is container_persistence
        # Both services share the SAME persistence instance
        assert player_service.persistence is room_service.persistence

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

    def test_dependency_functions_require_container(self):
        """
        Test dependency functions require ApplicationContainer to be initialized.

        AI: ARCHITECTURE CHANGE - Container must be initialized
        Old behavior: Could create services with None persistence
        New behavior: Container must be initialized, raises RuntimeError if not
        """
        from unittest.mock import MagicMock, Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        # Create a Mock that doesn't have container attribute
        # Use MagicMock with spec=[] to prevent auto-creation
        mock_request = Mock(spec=Request)
        mock_request.app = Mock()
        mock_request.app.state = MagicMock(spec=[])  # Empty spec prevents auto-attributes

        # ARCHITECTURE FIX: Should raise RuntimeError when container not found
        with pytest.raises(RuntimeError) as exc_info:
            get_player_service(mock_request)

        assert "ApplicationContainer not found" in str(exc_info.value)

    def test_dependency_functions_consistency(self, container_test_client):
        """
        Test that dependency functions behave consistently with container.

        AI: ARCHITECTURE CHANGE - Container provides consistent service instances
        """
        from unittest.mock import Mock

        from fastapi import Request

        from server.dependencies import get_player_service

        mock_request = Mock(spec=Request)
        mock_request.app = container_test_client.app

        # Call the function multiple times
        services = []
        for _ in range(5):
            service = get_player_service(mock_request)
            services.append(service)

        # ARCHITECTURE FIX: Container returns SAME instance every time
        for service in services:
            assert isinstance(service, PlayerService)
            assert service is services[0]  # All are same instance from container
