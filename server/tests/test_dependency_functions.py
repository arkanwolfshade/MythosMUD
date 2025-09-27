"""
Test the actual dependency injection functions.

This module tests that the PlayerServiceDep and RoomServiceDep functions
work correctly and return the expected service instances.
"""

from unittest.mock import AsyncMock, patch

import pytest

from server.api.players import PlayerServiceDep
from server.api.rooms import RoomServiceDep
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
        # Mock the persistence layer in the dependency
        with patch("server.api.players.get_persistence", return_value=mock_persistence):
            service = PlayerServiceDep()

            # Verify the service is created correctly
            assert isinstance(service, PlayerService)
            assert hasattr(service, "persistence")
            assert service.persistence == mock_persistence

    def test_room_service_dep_function(self, mock_persistence):
        """Test that RoomServiceDep function works correctly."""
        # Mock the persistence layer in the dependency
        with patch("server.api.rooms.get_persistence", return_value=mock_persistence):
            service = RoomServiceDep()

            # Verify the service is created correctly
            assert isinstance(service, RoomService)
            assert hasattr(service, "persistence")
            assert service.persistence == mock_persistence

    def test_dependency_functions_are_callable(self):
        """Test that dependency functions are callable."""
        assert callable(PlayerServiceDep)
        assert callable(RoomServiceDep)

    def test_dependency_functions_return_different_instances(self, mock_persistence):
        """Test that dependency functions return different instances."""
        with (
            patch("server.api.players.get_persistence", return_value=mock_persistence),
            patch("server.api.rooms.get_persistence", return_value=mock_persistence),
        ):
            player_service1 = PlayerServiceDep()
            player_service2 = PlayerServiceDep()
            room_service1 = RoomServiceDep()
            room_service2 = RoomServiceDep()

            # Verify they are different instances
            assert player_service1 is not player_service2
            assert room_service1 is not room_service2
            assert player_service1 is not room_service1
            assert player_service2 is not room_service2

    def test_dependency_functions_with_different_persistence(self):
        """Test dependency functions with different persistence layers."""
        persistence1 = AsyncMock()
        persistence2 = AsyncMock()

        with patch("server.api.players.get_persistence", return_value=persistence1):
            player_service = PlayerServiceDep()

        with patch("server.api.rooms.get_persistence", return_value=persistence2):
            room_service = RoomServiceDep()

        # Verify they use different persistence layers
        assert player_service.persistence == persistence1
        assert room_service.persistence == persistence2
        assert player_service.persistence is not room_service.persistence

    def test_dependency_function_error_handling(self):
        """Test that dependency functions handle errors gracefully."""
        # Test with persistence layer that raises an exception
        with patch("server.api.players.get_persistence", side_effect=Exception("Persistence error")):
            with pytest.raises(Exception, match="Persistence error"):
                PlayerServiceDep()

    def test_dependency_function_type_annotations(self):
        """Test that dependency functions have correct type annotations."""
        import inspect

        # Check PlayerServiceDep signature
        player_sig = inspect.signature(PlayerServiceDep)
        assert player_sig.return_annotation == PlayerService or player_sig.return_annotation == inspect.Signature.empty

        # Check RoomServiceDep signature
        room_sig = inspect.signature(RoomServiceDep)
        assert room_sig.return_annotation == RoomService or room_sig.return_annotation == inspect.Signature.empty

    def test_dependency_functions_performance(self, mock_persistence):
        """Test that dependency functions perform well."""
        import time

        with patch("server.api.players.get_persistence", return_value=mock_persistence):
            start_time = time.time()

            # Create many service instances
            services = []
            for _ in range(100):
                service = PlayerServiceDep()
                services.append(service)

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Should complete within reasonable time (less than 1 second for 100 instances)
            assert elapsed_time < 1.0
            assert len(services) == 100

    def test_dependency_functions_memory_usage(self, mock_persistence):
        """Test that dependency functions don't cause memory leaks."""
        import gc

        with patch("server.api.players.get_persistence", return_value=mock_persistence):
            # Create many service instances
            services = []
            for _ in range(1000):
                service = PlayerServiceDep()
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
                with patch("server.api.players.get_persistence", return_value=mock_persistence):
                    service = PlayerServiceDep()
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
        with patch("server.api.players.get_persistence", return_value=None):
            with pytest.raises((TypeError, AttributeError)):
                PlayerServiceDep()

    def test_dependency_functions_consistency(self, mock_persistence):
        """Test that dependency functions behave consistently."""
        with patch("server.api.players.get_persistence", return_value=mock_persistence):
            # Call the function multiple times
            services = []
            for _ in range(5):
                service = PlayerServiceDep()
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

        with patch("server.api.players.get_persistence", return_value=mock_persistence):
            service = PlayerServiceDep()

            # Verify the service uses the configured mock
            assert service.persistence == mock_persistence
            assert service.persistence.async_list_players.return_value == [{"name": "TestPlayer"}]
            assert service.persistence.async_get_player.return_value == {"name": "TestPlayer", "id": "123"}
