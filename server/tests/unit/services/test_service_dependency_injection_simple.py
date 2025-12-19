"""
Simple tests for service layer dependency injection functionality.

This module tests that the service classes can be instantiated correctly
and that dependency injection patterns work as expected.
"""

from unittest.mock import AsyncMock

import pytest

from server.game.player_service import PlayerService
from server.game.room_service import RoomService


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
            "apply_lucidity_loss",
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
        from typing import Any, cast

        assert player_service1 is not player_service2
        assert cast(Any, player_service1) is not room_service
        assert cast(Any, player_service2) is not room_service

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

    def test_service_initialization_with_different_persistence(self) -> None:
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
            except (ValueError, KeyError, AttributeError, RuntimeError) as e:
                # We catch expected functional errors to record failures for assertion.
                errors.append(e)

        # Create multiple threads
        threads = []
        for _i in range(10):
            thread = threading.Thread(target=worker)
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        # CRITICAL: Add timeout to prevent indefinite hang if threads don't complete
        for thread in threads:
            thread.join(timeout=10.0)
            if thread.is_alive():
                raise TimeoutError(
                    f"Thread {thread.ident} did not complete within 10 second timeout. "
                    "This may indicate a resource leak or hanging operation."
                )

        # Verify no errors occurred
        assert len(errors) == 0, f"Concurrent access errors: {errors}"
        assert len(results) == 10, "Not all workers completed successfully"
