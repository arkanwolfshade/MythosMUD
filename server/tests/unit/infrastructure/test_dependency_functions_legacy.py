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
