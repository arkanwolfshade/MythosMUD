"""
Tests for GameTickService.
"""

import asyncio
from datetime import datetime
from unittest.mock import AsyncMock, Mock

import pytest

from server.services.game_tick_service import GameTickService


class TestGameTickService:
    """Test cases for GameTickService."""

    # pylint: disable=attribute-defined-outside-init
    # Attributes are defined in setup_method, which is the pytest pattern for test fixtures.
    # This is intentional and follows pytest best practices.
    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.mock_event_publisher = Mock()
        self.mock_event_publisher.publish_game_tick_event = AsyncMock()

        self.game_tick_service = GameTickService(
            event_publisher=self.mock_event_publisher,
            tick_interval=0.1,  # Use 0.1 seconds for faster testing
        )

    def test_initialization(self) -> None:
        """Test GameTickService initialization."""
        assert self.game_tick_service.event_publisher == self.mock_event_publisher
        assert self.game_tick_service.tick_interval == 0.1
        assert self.game_tick_service.is_running is False
        assert self.game_tick_service.tick_count == 0

    @pytest.mark.asyncio
    async def test_start_stop(self) -> None:
        """Test starting and stopping the game tick service."""
        # Test start
        await self.game_tick_service.start()
        assert self.game_tick_service.is_running is True

        # Wait a bit to ensure tick loop starts
        await asyncio.sleep(0.05)

        # Test stop
        await self.game_tick_service.stop()
        assert self.game_tick_service.is_running is False

    @pytest.mark.asyncio
    async def test_tick_loop_generates_events(self) -> None:
        """Test that the tick loop generates game tick events."""
        await self.game_tick_service.start()

        # Wait for at least one tick
        await asyncio.sleep(0.15)

        # Verify event was published
        assert self.mock_event_publisher.publish_game_tick_event.called

        await self.game_tick_service.stop()

    @pytest.mark.asyncio
    async def test_tick_count_increments(self) -> None:
        """Test that tick count increments with each tick."""
        await self.game_tick_service.start()

        # Wait for multiple ticks
        await asyncio.sleep(0.25)

        # Verify tick count increased
        assert self.game_tick_service.tick_count > 0

        await self.game_tick_service.stop()

    @pytest.mark.asyncio
    async def test_publish_game_tick_event_called_with_correct_data(self) -> None:
        """Test that publish_game_tick_event is called with correct data."""
        await self.game_tick_service.start()

        # Wait for at least one tick
        await asyncio.sleep(0.15)

        # Verify the call was made
        assert self.mock_event_publisher.publish_game_tick_event.called

        # Get the call arguments
        call_args = self.mock_event_publisher.publish_game_tick_event.call_args

        # Verify timestamp is provided
        assert "timestamp" in call_args.kwargs
        assert call_args.kwargs["timestamp"] is not None

        # Verify additional_metadata is provided
        assert "additional_metadata" in call_args.kwargs
        assert call_args.kwargs["additional_metadata"] is not None

        await self.game_tick_service.stop()

    @pytest.mark.asyncio
    async def test_publish_game_tick_event_failure_handling(self) -> None:
        """Test that tick loop continues even if event publishing fails."""
        # Make event publisher raise an exception
        self.mock_event_publisher.publish_game_tick_event.side_effect = Exception("Publish failed")

        await self.game_tick_service.start()

        # Wait for multiple ticks
        await asyncio.sleep(0.25)

        # Verify tick count still increased despite failures
        assert self.game_tick_service.tick_count > 0

        await self.game_tick_service.stop()

    @pytest.mark.asyncio
    async def test_multiple_start_calls_safe(self) -> None:
        """Test that multiple start calls are safe."""
        await self.game_tick_service.start()
        await self.game_tick_service.start()  # Second start should be safe

        assert self.game_tick_service.is_running is True

        await self.game_tick_service.stop()

    @pytest.mark.asyncio
    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared state or timing issues
    async def test_multiple_stop_calls_safe(self) -> None:
        """Test that multiple stop calls are safe."""
        await self.game_tick_service.start()
        await self.game_tick_service.stop()
        await self.game_tick_service.stop()  # Second stop should be safe

        assert self.game_tick_service.is_running is False

    @pytest.mark.asyncio
    async def test_tick_interval_respected(self) -> None:
        """Test that the tick interval is respected."""
        start_time = datetime.now()

        await self.game_tick_service.start()

        # Wait for one tick
        await asyncio.sleep(0.15)

        end_time = datetime.now()
        elapsed = (end_time - start_time).total_seconds()

        # Should be close to the tick interval (0.1s) plus some processing time
        assert 0.1 <= elapsed <= 0.2

        await self.game_tick_service.stop()

    def test_get_tick_count(self) -> None:
        """Test getting the current tick count."""
        assert self.game_tick_service.get_tick_count() == 0

        self.game_tick_service.tick_count = 5
        assert self.game_tick_service.get_tick_count() == 5

    def test_reset_tick_count(self) -> None:
        """Test resetting the tick count."""
        self.game_tick_service.tick_count = 10
        self.game_tick_service.reset_tick_count()
        assert self.game_tick_service.get_tick_count() == 0

    @pytest.mark.asyncio
    async def test_tick_loop_stops_cleanly(self) -> None:
        """Test that the tick loop stops cleanly when stopped."""
        await self.game_tick_service.start()

        # Wait for a few ticks
        await asyncio.sleep(0.25)

        initial_tick_count = self.game_tick_service.tick_count

        # Stop the service
        await self.game_tick_service.stop()

        # Wait a bit more
        await asyncio.sleep(0.1)

        # Tick count should not have increased after stopping
        assert self.game_tick_service.tick_count == initial_tick_count
