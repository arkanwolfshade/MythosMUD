"""
Unit tests for game tick service.

Tests the GameTickService class for managing game tick intervals and events.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.services.game_tick_service import GameTickService

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions
# ruff: noqa: SLF001  # Reason: Test file - accessing protected members is standard practice for unit testing


class TestGameTickService:
    """Test suite for GameTickService class."""

    def test_init_default_interval(self):
        """Test GameTickService initialization with default interval."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        assert service.event_publisher == event_publisher
        assert service.tick_interval == 10.0
        assert service.is_running is False
        assert service.tick_count == 0
        assert service._tick_task is None

    def test_init_custom_interval(self):
        """Test GameTickService initialization with custom interval."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher, tick_interval=5.0)
        assert service.tick_interval == 5.0

    @pytest.mark.asyncio
    async def test_start_success(self):
        """Test start successfully starts the service."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        with patch("server.services.game_tick_service.get_global_tracked_manager") as mock_manager:
            mock_task = MagicMock()
            mock_task.done.return_value = False
            mock_tracked_manager = MagicMock()
            mock_tracked_manager.create_tracked_task.return_value = mock_task
            mock_manager.return_value = mock_tracked_manager

            result = await service.start()
            assert result is True
            assert service.is_running is True
            assert service._tick_task == mock_task

    @pytest.mark.asyncio
    async def test_start_already_running(self):
        """Test start returns True when already running."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.is_running = True

        result = await service.start()
        assert result is True

    @pytest.mark.asyncio
    async def test_start_failure(self):
        """Test start handles exceptions gracefully."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        with patch("server.services.game_tick_service.get_global_tracked_manager", side_effect=Exception("Test error")):
            result = await service.start()
            assert result is False
            assert service.is_running is False

    @pytest.mark.asyncio
    async def test_stop_success(self):
        """Test stop successfully stops the service."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.is_running = True

        # Create a real asyncio task that can be cancelled
        async def dummy_task():
            while True:
                await asyncio.sleep(0.1)

        real_task = asyncio.create_task(dummy_task())
        service._tick_task = real_task

        result = await service.stop()
        assert result is True
        assert service.is_running is False
        assert service._tick_task is None

    @pytest.mark.asyncio
    async def test_stop_not_running(self):
        """Test stop returns True when not running."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.is_running = False

        result = await service.stop()
        assert result is True

    @pytest.mark.asyncio
    async def test_stop_task_already_done(self):
        """Test stop handles task that's already done."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.is_running = True
        mock_task = MagicMock()
        mock_task.done.return_value = True
        service._tick_task = mock_task

        result = await service.stop()
        assert result is True
        mock_task.cancel.assert_not_called()

    @pytest.mark.asyncio
    async def test_stop_failure(self):
        """Test stop handles exceptions gracefully."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.is_running = True
        mock_task = MagicMock()
        mock_task.done.side_effect = Exception("Test error")
        service._tick_task = mock_task

        result = await service.stop()
        assert result is False

    def test_get_tick_count(self):
        """Test get_tick_count returns current count."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.tick_count = 42
        assert service.get_tick_count() == 42

    def test_reset_tick_count(self):
        """Test reset_tick_count resets count to zero."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher)
        service.tick_count = 100
        service.reset_tick_count()
        assert service.tick_count == 0

    def test_get_tick_interval(self):
        """Test get_tick_interval returns interval."""
        event_publisher = MagicMock()
        service = GameTickService(event_publisher, tick_interval=5.0)
        assert service.get_tick_interval() == 5.0

    @pytest.mark.asyncio
    async def test_tick_loop_increments_count(self):
        """Test _tick_loop increments tick count."""
        event_publisher = AsyncMock()
        event_publisher.publish_game_tick_event = AsyncMock(return_value=True)
        service = GameTickService(event_publisher, tick_interval=1.0)
        service.is_running = True

        # Mock sleep to make the test deterministic and fast
        tick_count_before = service.tick_count
        with patch("server.services.game_tick_service.sleep") as mock_sleep:
            # Make sleep return immediately after first call
            call_count = 0

            async def mock_sleep_side_effect(_duration):
                nonlocal call_count
                call_count += 1
                if call_count >= 1:  # After first tick, stop the loop
                    service.is_running = False
                # Use a very short actual sleep to allow the loop to process
                await asyncio.sleep(0.001)

            mock_sleep.side_effect = mock_sleep_side_effect

            # Start the loop
            task = asyncio.create_task(service._tick_loop())

            # Wait for task to complete (it will stop after first tick due to mock)
            try:
                await asyncio.wait_for(task, timeout=1.0)
            except TimeoutError:
                # If it times out, cancel it
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        assert service.tick_count > tick_count_before

    @pytest.mark.asyncio
    async def test_tick_loop_publishes_events(self):
        """Test _tick_loop publishes game tick events."""
        event_publisher = AsyncMock()
        event_publisher.publish_game_tick_event = AsyncMock(return_value=True)
        service = GameTickService(event_publisher, tick_interval=1.0)
        service.is_running = True

        # Mock sleep to make the test deterministic and fast
        with patch("server.services.game_tick_service.sleep") as mock_sleep:
            # Make sleep return immediately after first call
            call_count = 0

            async def mock_sleep_side_effect(_duration):
                nonlocal call_count
                call_count += 1
                if call_count >= 1:  # After first tick, stop the loop
                    service.is_running = False
                # Use a very short actual sleep to allow the loop to process
                await asyncio.sleep(0.001)

            mock_sleep.side_effect = mock_sleep_side_effect

            # Start the loop
            task = asyncio.create_task(service._tick_loop())

            # Wait for task to complete (it will stop after first tick due to mock)
            try:
                await asyncio.wait_for(task, timeout=1.0)
            except TimeoutError:
                # If it times out, cancel it
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        assert event_publisher.publish_game_tick_event.called

    @pytest.mark.asyncio
    async def test_tick_loop_handles_cancellation(self):
        """Test _tick_loop handles cancellation gracefully."""
        event_publisher = AsyncMock()
        event_publisher.publish_game_tick_event = AsyncMock(return_value=True)
        service = GameTickService(event_publisher, tick_interval=0.1)
        service.is_running = True

        # Mock sleep to make the test deterministic
        with patch("server.services.game_tick_service.sleep") as mock_sleep:
            # Make sleep return immediately and stop the loop after first iteration
            call_count = 0

            async def mock_sleep_side_effect(_duration):
                nonlocal call_count
                call_count += 1
                if call_count >= 1:  # After first tick, stop the loop
                    service.is_running = False
                # Use a very short actual sleep to allow the loop to process
                await asyncio.sleep(0.001)

            mock_sleep.side_effect = mock_sleep_side_effect

            # Start the loop
            task = asyncio.create_task(service._tick_loop())

            # Wait briefly then cancel
            await asyncio.sleep(0.01)
            task.cancel()
            service.is_running = False  # Ensure loop stops

            # Wait for cancellation to complete
            try:
                await asyncio.wait_for(task, timeout=0.5)
            except (asyncio.CancelledError, TimeoutError):
                # If it times out or is cancelled, ensure it's cleaned up
                if not task.done():
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass

        # Should have handled cancellation without error
        assert True  # If we get here, cancellation was handled

    @pytest.mark.asyncio
    async def test_tick_loop_handles_publish_failure(self):
        """Test _tick_loop continues on publish failure."""
        event_publisher = AsyncMock()
        event_publisher.publish_game_tick_event = AsyncMock(return_value=False)
        service = GameTickService(event_publisher, tick_interval=0.1)
        service.is_running = True

        # Mock sleep to make the test deterministic
        with patch("server.services.game_tick_service.sleep") as mock_sleep:
            # Make sleep return immediately after first call
            call_count = 0

            async def mock_sleep_side_effect(_duration):
                nonlocal call_count
                call_count += 1
                if call_count >= 1:  # After first tick, stop the loop
                    service.is_running = False
                # Use a very short actual sleep to allow the loop to process
                await asyncio.sleep(0.001)

            mock_sleep.side_effect = mock_sleep_side_effect

            # Start the loop
            task = asyncio.create_task(service._tick_loop())

            # Wait for task to complete (it will stop after first tick due to mock)
            try:
                await asyncio.wait_for(task, timeout=1.0)
            except TimeoutError:
                # If it times out, cancel it
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        # Should have continued despite publish failure
        assert service.tick_count > 0

    @pytest.mark.asyncio
    async def test_tick_loop_handles_exceptions(self):
        """Test _tick_loop handles exceptions and continues."""
        event_publisher = AsyncMock()
        event_publisher.publish_game_tick_event = AsyncMock(side_effect=ValueError("Test error"))
        service = GameTickService(event_publisher, tick_interval=0.1)
        service.is_running = True

        # Start the loop and let it run briefly
        task = asyncio.create_task(service._tick_loop())
        await asyncio.sleep(0.15)  # Wait for at least one tick
        service.is_running = False
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        # Should have continued despite exception
        assert service.tick_count > 0
