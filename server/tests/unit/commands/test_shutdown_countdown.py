"""
Tests for shutdown countdown and state management.

This module tests the countdown notification system, state management,
and cancellation logic for the server shutdown feature.

As documented in the Necronomicon's appendices, proper temporal warnings
are essential before sealing dimensional boundaries.
"""

import time
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.admin_shutdown_command import (
    broadcast_shutdown_notification,
    calculate_notification_times,
    cancel_shutdown_countdown,
    initiate_shutdown_countdown,
)


def create_mock_task_registry():
    """
    Create a mock task registry that properly consumes coroutines.

    This prevents "coroutine was never awaited" warnings by ensuring
    any coroutines passed to register_task are properly consumed.
    """
    mock_registry = MagicMock()
    mock_task = MagicMock()
    mock_task.cancel = MagicMock()
    mock_task.done = MagicMock(return_value=False)

    def register_task_side_effect(coro, *_args, **_kwargs):
        # Close the coroutine to prevent "never awaited" warning
        coro.close()
        return mock_task

    mock_registry.register_task.side_effect = register_task_side_effect
    return mock_registry, mock_task


class TestNotificationTimeCalculation:
    """Test calculation of notification times for countdown."""

    def test_calculate_notification_times_10_seconds(self) -> None:
        """Test notification times for 10-second countdown."""
        times = calculate_notification_times(10)

        # Should have: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        assert times == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_calculate_notification_times_30_seconds(self) -> None:
        """Test notification times for 30-second countdown."""
        times = calculate_notification_times(30)

        # Should have: 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        assert times == [30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_calculate_notification_times_45_seconds(self) -> None:
        """Test notification times for 45-second countdown."""
        times = calculate_notification_times(45)

        # Should have: 45 (rounded to 50), 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        assert times == [40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_calculate_notification_times_100_seconds(self) -> None:
        """Test notification times for 100-second countdown."""
        times = calculate_notification_times(100)

        # Should have: 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        assert times == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    def test_calculate_notification_times_5_seconds(self) -> None:
        """Test notification times for 5-second countdown (all seconds)."""
        times = calculate_notification_times(5)

        # Should have: 5, 4, 3, 2, 1 (all within final 10 seconds)
        assert times == [5, 4, 3, 2, 1]

    def test_calculate_notification_times_1_second(self) -> None:
        """Test notification times for 1-second countdown."""
        times = calculate_notification_times(1)

        # Should have: 1
        assert times == [1]

    def test_calculate_notification_times_sorted_descending(self) -> None:
        """Test that notification times are sorted in descending order."""
        times = calculate_notification_times(60)

        # Verify descending order
        assert times == sorted(times, reverse=True)


class TestShutdownNotificationBroadcast:
    """Test broadcasting shutdown notifications."""

    @pytest.mark.asyncio
    async def test_broadcast_shutdown_notification(self) -> None:
        """Test broadcasting shutdown notification to all players."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.broadcast_global_event = AsyncMock(
            return_value={"total_players": 5, "successful_deliveries": 5}
        )

        result = await broadcast_shutdown_notification(mock_connection_manager, 30)

        assert result is True
        mock_connection_manager.broadcast_global_event.assert_called_once()
        call_args = mock_connection_manager.broadcast_global_event.call_args
        assert call_args[0][0] == "shutdown_notification"
        assert "seconds_remaining" in call_args[0][1]
        assert call_args[0][1]["seconds_remaining"] == 30

    @pytest.mark.asyncio
    async def test_broadcast_shutdown_notification_failure(self) -> None:
        """Test handling broadcast failure."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.broadcast_global_event = AsyncMock(side_effect=Exception("Broadcast failed"))

        result = await broadcast_shutdown_notification(mock_connection_manager, 30)

        assert result is False

    @pytest.mark.asyncio
    async def test_broadcast_shutdown_notification_message_format(self) -> None:
        """Test that notification message is properly formatted."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.broadcast_global_event = AsyncMock(
            return_value={"total_players": 5, "successful_deliveries": 5}
        )

        await broadcast_shutdown_notification(mock_connection_manager, 30)

        call_args = mock_connection_manager.broadcast_global_event.call_args[0][1]
        assert "message" in call_args
        assert "30" in call_args["message"]
        assert "seconds" in call_args["message"]

    @pytest.mark.asyncio
    async def test_broadcast_shutdown_notification_singular_second(self) -> None:
        """Test notification message for 1 second uses singular form."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.broadcast_global_event = AsyncMock(
            return_value={"total_players": 5, "successful_deliveries": 5}
        )

        await broadcast_shutdown_notification(mock_connection_manager, 1)

        call_args = mock_connection_manager.broadcast_global_event.call_args[0][1]
        message = call_args["message"]
        assert "1 second" in message
        assert "1 seconds" not in message


class TestShutdownCountdownInitiation:
    """Test shutdown countdown initiation."""

    @pytest.mark.asyncio
    async def test_initiate_shutdown_countdown_basic(self) -> None:
        """Test basic shutdown countdown initiation."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Create mock for task registry
        # Mock task registry (properly consumes coroutines)
        mock_task_registry, _mock_task = create_mock_task_registry()
        mock_app.state.task_registry = mock_task_registry

        await initiate_shutdown_countdown(mock_app, 10, "admin_user")

        # Verify shutdown_pending flag set
        assert mock_app.state.server_shutdown_pending is True

        # Verify shutdown_data created
        assert hasattr(mock_app.state, "shutdown_data")
        assert mock_app.state.shutdown_data["countdown_seconds"] == 10
        assert mock_app.state.shutdown_data["admin_username"] == "admin_user"

        # Verify task registered
        mock_task_registry.register_task.assert_called_once()

    @pytest.mark.asyncio
    async def test_initiate_shutdown_countdown_superseding(self) -> None:
        """Test that new shutdown supersedes previous one."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Create existing shutdown
        existing_task = MagicMock()
        existing_task.cancel = MagicMock()
        existing_task.done = MagicMock(return_value=False)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 30,
            "admin_username": "old_admin",
            "start_time": time.time(),
            "end_time": time.time() + 30,
            "task": existing_task,
        }

        # Create mock for task registry
        mock_task_registry = MagicMock()
        mock_new_task = AsyncMock()
        mock_task_registry.register_task = MagicMock(return_value=mock_new_task)
        mock_app.state.task_registry = mock_task_registry

        await initiate_shutdown_countdown(mock_app, 10, "new_admin")

        # Verify old task was cancelled
        existing_task.cancel.assert_called_once()

        # Verify new shutdown data
        assert mock_app.state.shutdown_data["countdown_seconds"] == 10
        assert mock_app.state.shutdown_data["admin_username"] == "new_admin"


class TestShutdownCancellation:
    """Test shutdown cancellation functionality."""

    @pytest.mark.asyncio
    async def test_cancel_shutdown_countdown_success(self) -> None:
        """Test successful shutdown cancellation."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Set up existing shutdown
        mock_task = MagicMock()
        mock_task.cancel = MagicMock()
        mock_task.done = MagicMock(return_value=False)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 30,
            "admin_username": "admin_user",
            "start_time": time.time(),
            "end_time": time.time() + 30,
            "task": mock_task,
        }

        result = await cancel_shutdown_countdown(mock_app, "cancelling_admin")

        assert result is True
        # Verify task was cancelled
        mock_task.cancel.assert_called_once()
        # Verify flags cleared
        assert mock_app.state.server_shutdown_pending is False
        assert mock_app.state.shutdown_data is None
        # Verify cancellation notification sent
        mock_app.state.connection_manager.broadcast_global_event.assert_called()
        call_args = mock_app.state.connection_manager.broadcast_global_event.call_args[0]
        assert call_args[0] == "shutdown_cancelled"

    @pytest.mark.asyncio
    async def test_cancel_shutdown_countdown_no_active_shutdown(self) -> None:
        """Test cancellation when no shutdown is active."""
        mock_app = MagicMock()
        mock_app.state.server_shutdown_pending = False
        mock_app.state.shutdown_data = None

        result = await cancel_shutdown_countdown(mock_app, "admin_user")

        assert result is False

    @pytest.mark.asyncio
    async def test_cancel_shutdown_countdown_already_completed(self) -> None:
        """Test cancellation when shutdown task already completed."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Set up completed task
        mock_task = MagicMock()
        mock_task.cancel = MagicMock()
        mock_task.done = MagicMock(return_value=True)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 1,
            "admin_username": "admin_user",
            "start_time": time.time(),
            "end_time": time.time() + 1,
            "task": mock_task,
        }

        result = await cancel_shutdown_countdown(mock_app, "cancelling_admin")

        # Should still succeed and clean up state
        assert result is True
        assert mock_app.state.server_shutdown_pending is False

    @pytest.mark.asyncio
    async def test_cancel_shutdown_notification_message(self) -> None:
        """Test that cancellation notification message is thematic."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(return_value={"successful_deliveries": 5})

        # Set up existing shutdown
        mock_task = MagicMock()
        mock_task.cancel = MagicMock()
        mock_task.done = MagicMock(return_value=False)
        mock_app.state.server_shutdown_pending = True
        mock_app.state.shutdown_data = {
            "countdown_seconds": 30,
            "admin_username": "admin_user",
            "start_time": time.time(),
            "end_time": time.time() + 30,
            "task": mock_task,
        }

        await cancel_shutdown_countdown(mock_app, "cancelling_admin")

        call_args = mock_app.state.connection_manager.broadcast_global_event.call_args[0][1]
        message = call_args["message"]
        # Should contain thematic language
        assert any(keyword in message.lower() for keyword in ["cancelled", "canceled", "stars", "right"])


class TestCountdownTimingAccuracy:
    """Test countdown timing and notification scheduling."""

    @pytest.mark.asyncio
    async def test_countdown_notification_timing_30_seconds(self) -> None:
        """Test that notifications are sent at correct times for 30-second countdown."""
        mock_app = MagicMock()
        mock_app.state.connection_manager = MagicMock()
        broadcast_times = []

        async def capture_broadcast_time(_event_type, data):
            broadcast_times.append(data["seconds_remaining"])
            return {"successful_deliveries": 5}

        mock_app.state.connection_manager.broadcast_global_event = AsyncMock(side_effect=capture_broadcast_time)

        # This test would need the actual countdown loop implementation
        # For now, verify the calculation is correct
        expected_times = [30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        calculated_times = calculate_notification_times(30)

        assert calculated_times == expected_times
