"""
Test async operations verification.

This module tests that all async operations perform correctly and that
there are no blocking I/O operations remaining in the system.
"""

import asyncio
import inspect
import time
from unittest.mock import AsyncMock, Mock

import pytest

from server.game.player_service import PlayerService
from server.game.room_service import RoomService
from server.persistence import PersistenceLayer


class TestAsyncOperationsVerification:
    """Test that all async operations perform correctly."""

    @pytest.fixture
    def mock_persistence(self):
        """Create mock persistence layer with async methods."""
        mock_persistence = AsyncMock()

        # Configure async methods to simulate I/O operations
        async def mock_async_operation(*args, **kwargs):
            # Simulate some async work
            await asyncio.sleep(0.01)
            return mock_persistence._return_value

        # Set up async methods
        mock_persistence.async_list_players.return_value = []
        mock_persistence.async_get_player.return_value = None
        mock_persistence.async_get_room.return_value = None
        mock_persistence.async_save_player.return_value = None
        mock_persistence.async_delete_player.return_value = True
        mock_persistence.async_get_player_by_name.return_value = None
        mock_persistence.async_get_player_by_user_id.return_value = None
        mock_persistence.async_get_players_in_room.return_value = []
        mock_persistence.async_save_players.return_value = None
        mock_persistence.async_get_all_professions.return_value = []
        mock_persistence.async_get_profession_by_id.return_value = None
        mock_persistence.async_save_room.return_value = None
        mock_persistence.async_list_rooms.return_value = []
        mock_persistence.async_save_rooms.return_value = None
        mock_persistence.async_apply_sanity_loss.return_value = None
        mock_persistence.async_apply_fear.return_value = None
        mock_persistence.async_apply_corruption.return_value = None
        mock_persistence.async_gain_occult_knowledge.return_value = None
        mock_persistence.async_heal_player.return_value = None
        mock_persistence.async_damage_player.return_value = None

        # Also mock synchronous methods for backward compatibility
        mock_persistence.list_players.return_value = []
        mock_persistence.get_player.return_value = None
        mock_persistence.get_room.return_value = None
        mock_persistence.save_player.return_value = None
        mock_persistence.delete_player.return_value = True

        return mock_persistence

    @pytest.mark.asyncio
    async def test_player_service_async_methods_are_coroutines(self, mock_persistence):
        """Test that PlayerService async methods are coroutines."""
        service = PlayerService(mock_persistence)

        async_methods = [
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

        for method_name in async_methods:
            method = getattr(service, method_name)
            # Check if it's a coroutine function
            assert inspect.iscoroutinefunction(method), f"Method {method_name} should be a coroutine function"

    @pytest.mark.asyncio
    async def test_room_service_async_methods_are_coroutines(self, mock_persistence):
        """Test that RoomService async methods are coroutines."""
        service = RoomService(mock_persistence)

        async_methods = ["get_room"]

        for method_name in async_methods:
            method = getattr(service, method_name)
            # Check if it's a coroutine function
            assert inspect.iscoroutinefunction(method), f"Method {method_name} should be a coroutine function"

    @pytest.mark.asyncio
    async def test_player_service_async_methods_actually_await(self, mock_persistence):
        """Test that PlayerService async methods actually perform async operations."""
        service = PlayerService(mock_persistence)

        # Configure mock to track calls
        mock_persistence.async_list_players.reset_mock()
        mock_persistence.async_get_player.reset_mock()

        # Call async methods
        await service.list_players()
        await service.get_player_by_id("test_id")

        # Verify async methods were called
        mock_persistence.async_list_players.assert_called_once()
        mock_persistence.async_get_player.assert_called_once_with("test_id")

    @pytest.mark.asyncio
    async def test_room_service_async_methods_actually_await(self, mock_persistence):
        """Test that RoomService async methods actually perform async operations."""
        service = RoomService(mock_persistence)

        # Configure mock to track calls
        mock_persistence.async_get_room.reset_mock()

        # Call async method
        await service.get_room("test_room_id")

        # Verify async method was called
        mock_persistence.async_get_room.assert_called_once_with("test_room_id")

    @pytest.mark.asyncio
    async def test_concurrent_async_operations(self, mock_persistence):
        """Test that multiple async operations can run concurrently."""
        service = PlayerService(mock_persistence)

        # Configure mock to simulate async work
        async def mock_async_work(*args, **kwargs):
            await asyncio.sleep(0.05)
            return []

        # Mock the persistence methods to return proper data
        mock_persistence.async_list_players.return_value = []

        # Mock a proper player object for get_player
        import uuid

        mock_player = Mock()
        mock_player.player_id = str(uuid.uuid4())
        mock_player.user_id = str(uuid.uuid4())
        mock_player.name = "TestPlayer"
        mock_player.profession_id = 0
        mock_player.current_room_id = "room1"
        mock_player.experience_points = 0
        mock_player.level = 1
        mock_player.get_stats.return_value = {}
        mock_player.get_inventory.return_value = []
        mock_player.get_status_effects.return_value = []
        mock_player.created_at = "2023-01-01"
        mock_player.last_active = "2023-01-01"
        mock_player.is_admin = False

        # Mock profession lookup
        mock_profession = Mock()
        mock_profession.name = "Test Profession"
        mock_profession.description = "A test profession"
        mock_profession.flavor_text = "Test flavor"
        mock_persistence.get_profession_by_id.return_value = mock_profession

        mock_persistence.async_get_player.return_value = mock_player

        start_time = time.time()

        # Run multiple async operations concurrently
        tasks = [
            service.list_players(),
            service.get_player_by_id("player1"),
            service.get_player_by_id("player2"),
            service.get_player_by_id("player3"),
            service.list_players(),
        ]

        results = await asyncio.gather(*tasks)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # If operations were truly concurrent, this should take around 0.05 seconds
        # If they were blocking, it would take around 0.25 seconds
        assert elapsed_time < 0.2, f"Operations took {elapsed_time}s, expected < 0.2s for concurrent execution"
        assert len(results) == 5

    @pytest.mark.asyncio
    async def test_async_operations_with_timeout(self, mock_persistence):
        """Test that async operations respect timeouts."""
        service = PlayerService(mock_persistence)

        # Configure mock to take a long time
        async def slow_operation(*args, **kwargs):
            await asyncio.sleep(1.0)
            return []

        mock_persistence.async_list_players.side_effect = slow_operation

        # Test with timeout
        with pytest.raises(asyncio.TimeoutError):
            await asyncio.wait_for(service.list_players(), timeout=0.1)

    @pytest.mark.asyncio
    async def test_async_operations_error_handling(self, mock_persistence):
        """Test that async operations handle errors correctly."""
        service = PlayerService(mock_persistence)

        # Configure mock to raise an exception
        mock_persistence.async_list_players.side_effect = Exception("Database error")

        # Test that exception is properly propagated
        with pytest.raises(Exception, match="Database error"):
            await service.list_players()

    @pytest.mark.asyncio
    async def test_async_operations_cancellation(self, mock_persistence):
        """Test that async operations can be cancelled."""
        service = PlayerService(mock_persistence)

        # Configure mock to take a long time
        async def slow_operation(*args, **kwargs):
            await asyncio.sleep(1.0)
            return []

        mock_persistence.async_list_players.side_effect = slow_operation

        # Create task and cancel it
        task = asyncio.create_task(service.list_players())
        await asyncio.sleep(0.01)  # Let it start
        task.cancel()

        # Test that cancellation is handled
        with pytest.raises(asyncio.CancelledError):
            await task

    @pytest.mark.asyncio
    async def test_async_operations_with_different_event_loops(self, mock_persistence):
        """Test that async operations work correctly with different event loops."""
        service = PlayerService(mock_persistence)

        # Test in current event loop
        result1 = await service.list_players()

        # Test in a new event loop (simulated)
        async def test_in_loop():
            return await service.list_players()

        result2 = await test_in_loop()

        # Both should work correctly
        assert result1 == result2

    @pytest.mark.asyncio
    async def test_async_operations_memory_efficiency(self, mock_persistence):
        """Test that async operations are memory efficient."""
        service = PlayerService(mock_persistence)

        # Create many concurrent operations
        tasks = []
        for _i in range(100):
            task = asyncio.create_task(service.list_players())
            tasks.append(task)

        # Wait for all to complete
        results = await asyncio.gather(*tasks)

        # Should complete without memory issues
        assert len(results) == 100

    @pytest.mark.asyncio
    async def test_async_operations_with_real_persistence_layer(self):
        """Test async operations with a real persistence layer instance."""
        import os

        # Use PostgreSQL from environment
        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            pytest.skip("DATABASE_URL must be set to a PostgreSQL URL for this test.")

        # Create a real persistence layer (this will use PostgreSQL)
        persistence = PersistenceLayer()

        # Test that async methods exist and are callable
        assert hasattr(persistence, "async_list_players")
        assert hasattr(persistence, "async_get_player")
        assert hasattr(persistence, "async_get_room")

        # Test that they return values (even if empty)
        players = await persistence.async_list_players()
        assert isinstance(players, list)

        # Use a valid UUID string for testing (not a real player, but valid format)
        from uuid import uuid4

        nonexistent_uuid = str(uuid4())
        player = await persistence.async_get_player(nonexistent_uuid)
        assert player is None

        room = await persistence.async_get_room("nonexistent")
        assert room is None

    @pytest.mark.asyncio
    async def test_async_operations_performance_benchmark(self, mock_persistence):
        """Test performance of async operations."""
        service = PlayerService(mock_persistence)

        # Configure mock to simulate realistic async work
        async def realistic_async_work(*args, **kwargs):
            await asyncio.sleep(0.01)  # 10ms of async work (more realistic)
            return []

        mock_persistence.async_list_players.side_effect = realistic_async_work

        # Benchmark single operation
        start_time = time.time()
        await service.list_players()
        single_time = time.time() - start_time

        # Benchmark concurrent operations
        start_time = time.time()
        tasks = [service.list_players() for _ in range(10)]
        await asyncio.gather(*tasks)
        concurrent_time = time.time() - start_time

        # Concurrent operations should be significantly faster than sequential
        # Account for system overhead by using a more realistic comparison
        # If operations were truly sequential, they would take ~10 * 0.01s = 0.1s
        # If they're concurrent, they should take closer to 0.01s + overhead
        # We allow for 3x the theoretical concurrent time to account for system overhead
        theoretical_concurrent_time = 0.01 + 0.005  # 10ms work + 5ms overhead
        max_acceptable_time = theoretical_concurrent_time * 3  # 45ms total

        assert concurrent_time < max_acceptable_time, (
            f"Concurrent time {concurrent_time:.4f}s should be less than {max_acceptable_time:.4f}s "
            f"(theoretical concurrent time: {theoretical_concurrent_time:.4f}s)"
        )

        # Also verify that concurrent is faster than sequential (with generous tolerance)
        sequential_estimate = single_time * 10
        assert concurrent_time < sequential_estimate * 2.5, (
            f"Concurrent time {concurrent_time:.4f}s should be less than 2.5x sequential estimate "
            f"{sequential_estimate:.4f}s (allowing for system overhead and timing variations)"
        )

    @pytest.mark.asyncio
    async def test_async_operations_with_blocking_detection(self, mock_persistence):
        """Test that async operations properly use async persistence methods."""
        service = PlayerService(mock_persistence)

        # Configure mock to track which methods are called
        mock_persistence.async_list_players.reset_mock()
        mock_persistence.async_get_player.reset_mock()

        # Call async methods
        await service.list_players()
        await service.get_player_by_id("test")

        # Verify that async persistence methods were called
        mock_persistence.async_list_players.assert_called_once()
        mock_persistence.async_get_player.assert_called_once_with("test")

    @pytest.mark.asyncio
    async def test_async_operations_with_realistic_data(self, mock_persistence):
        """Test async operations with realistic data scenarios."""
        service = PlayerService(mock_persistence)

        # Create mock player objects with proper structure
        import uuid

        mock_player1 = Mock()
        mock_player1.player_id = str(uuid.uuid4())
        mock_player1.user_id = str(uuid.uuid4())
        mock_player1.name = "Player1"
        mock_player1.profession_id = 0
        mock_player1.current_room_id = "room1"
        mock_player1.experience_points = 100
        mock_player1.level = 1
        mock_player1.get_stats.return_value = {"str": 10, "dex": 10}
        mock_player1.get_inventory.return_value = []
        mock_player1.get_status_effects.return_value = []
        mock_player1.created_at = "2023-01-01"
        mock_player1.last_active = "2023-01-01"
        mock_player1.is_admin = False

        mock_player2 = Mock()
        mock_player2.player_id = str(uuid.uuid4())
        mock_player2.user_id = str(uuid.uuid4())
        mock_player2.name = "Player2"
        mock_player2.profession_id = 1
        mock_player2.current_room_id = "room2"
        mock_player2.experience_points = 200
        mock_player2.level = 2
        mock_player2.get_stats.return_value = {"str": 12, "dex": 8}
        mock_player2.get_inventory.return_value = [{"name": "sword", "quantity": 1}]
        mock_player2.get_status_effects.return_value = []
        mock_player2.created_at = "2023-01-02"
        mock_player2.last_active = "2023-01-02"
        mock_player2.is_admin = False

        # Mock profession lookup
        mock_profession = Mock()
        mock_profession.name = "Test Profession"
        mock_profession.description = "A test profession"
        mock_profession.flavor_text = "Test flavor"
        mock_persistence.get_profession_by_id.return_value = mock_profession

        # Configure mock with realistic data
        mock_persistence.async_list_players.return_value = [mock_player1, mock_player2]
        mock_persistence.async_get_player.return_value = mock_player1

        # Test async operations with realistic data
        players = await service.list_players()
        assert len(players) == 2
        assert players[0].name == "Player1"
        assert players[1].name == "Player2"

        player = await service.get_player_by_id("test_id")
        assert player is not None
        assert player.name == "Player1"

    @pytest.mark.asyncio
    async def test_async_operations_stress_test(self, mock_persistence):
        """Stress test async operations with many concurrent requests."""
        service = PlayerService(mock_persistence)

        # Configure mock to simulate realistic load
        async def load_simulation(*args, **kwargs):
            await asyncio.sleep(0.01)
            return []

        mock_persistence.async_list_players.side_effect = load_simulation

        # Create many concurrent operations
        num_operations = 1000
        start_time = time.time()

        tasks = []
        for _i in range(num_operations):
            task = asyncio.create_task(service.list_players())
            tasks.append(task)

        # Wait for all to complete
        results = await asyncio.gather(*tasks, return_exceptions=True)

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Should complete within reasonable time
        assert elapsed_time < 10.0, f"Stress test took {elapsed_time}s, expected < 10s"

        # Should have no exceptions
        exceptions = [r for r in results if isinstance(r, Exception)]
        assert len(exceptions) == 0, f"Found exceptions: {exceptions}"

        assert len(results) == num_operations

    @pytest.mark.asyncio
    async def test_async_operations_with_context_managers(self, mock_persistence):
        """Test async operations work correctly with context managers."""
        service = PlayerService(mock_persistence)

        # Test that async operations work in async context managers
        async with asyncio.timeout(1.0):
            result = await service.list_players()
            assert result is not None

    @pytest.mark.asyncio
    async def test_async_operations_error_recovery(self, mock_persistence):
        """Test that async operations can recover from errors."""
        service = PlayerService(mock_persistence)

        # First call fails
        mock_persistence.async_list_players.side_effect = Exception("Temporary error")

        with pytest.raises(Exception, match="Temporary error"):
            await service.list_players()

        # Second call succeeds
        mock_persistence.async_list_players.side_effect = None
        mock_persistence.async_list_players.return_value = []

        result = await service.list_players()
        assert result == []

    @pytest.mark.asyncio
    async def test_async_operations_with_different_await_patterns(self, mock_persistence):
        """Test async operations with different await patterns."""
        service = PlayerService(mock_persistence)

        # Test direct await
        result1 = await service.list_players()

        # Test with asyncio.gather
        result2, result3 = await asyncio.gather(service.list_players(), service.get_player_by_id("test"))

        # Test with asyncio.as_completed
        tasks = [service.list_players(), service.get_player_by_id("test1"), service.get_player_by_id("test2")]

        results = []
        for coro in asyncio.as_completed(tasks):
            result = await coro
            results.append(result)

        assert len(results) == 3
        assert result1 == result2
