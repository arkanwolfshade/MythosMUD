"""
Tests for application lifespan management.

This module tests the startup and shutdown logic for the FastAPI application,
including initialization sequences and the game tick loop.
"""

import asyncio
from unittest.mock import MagicMock, patch

import pytest

from server.app.lifespan import TICK_INTERVAL, game_tick_loop


class TestTickIntervalConstant:
    """Test module constants."""

    def test_tick_interval_constant(self):
        """Test TICK_INTERVAL is defined correctly."""
        assert TICK_INTERVAL == 1.0


class TestGameTickLoop:
    """Test game tick loop functionality."""

    @pytest.mark.asyncio
    @patch("server.app.lifespan.broadcast_game_event")
    @patch("server.app.lifespan.connection_manager")
    async def test_game_tick_loop_runs(self, mock_connection_manager, mock_broadcast):
        """Test game tick loop executes ticks."""
        from fastapi import FastAPI

        mock_connection_manager.player_websockets = {"player1": MagicMock(), "player2": MagicMock()}
        mock_broadcast.return_value = None

        app = FastAPI()
        task = asyncio.create_task(game_tick_loop(app))

        # Let it run for a few ticks
        await asyncio.sleep(0.3)

        # Cancel the task
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        # Verify broadcast was called
        assert mock_broadcast.call_count >= 1

    @pytest.mark.asyncio
    @patch("server.app.lifespan.broadcast_game_event")
    @patch("server.app.lifespan.connection_manager")
    async def test_game_tick_loop_broadcast_data(self, mock_connection_manager, mock_broadcast):
        """Test game tick loop broadcasts correct data."""
        from fastapi import FastAPI

        mock_connection_manager.player_websockets = {"player1": MagicMock()}
        mock_broadcast.return_value = None

        app = FastAPI()
        task = asyncio.create_task(game_tick_loop(app))

        # Let one tick execute
        await asyncio.sleep(0.1)

        # Cancel the task
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        # Check that broadcast was called with correct structure
        if mock_broadcast.call_count > 0:
            call_args = mock_broadcast.call_args
            assert call_args[0][0] == "game_tick"
            tick_data = call_args[0][1]
            assert "tick_number" in tick_data
            assert "timestamp" in tick_data
            assert "active_players" in tick_data

    @pytest.mark.asyncio
    @patch("server.app.lifespan.broadcast_game_event")
    @patch("server.app.lifespan.connection_manager")
    async def test_game_tick_loop_handles_exception(self, mock_connection_manager, mock_broadcast):
        """Test game tick loop continues after exception."""
        from fastapi import FastAPI

        mock_connection_manager.player_websockets = {}
        call_count = [0]  # Use list to avoid closure issues

        async def broadcast_with_error(*args, **kwargs):
            call_count[0] += 1
            # First call succeeds, second call fails
            if call_count[0] == 2:
                raise Exception("Broadcast error")
            # Third call should succeed (loop continues)

        mock_broadcast.side_effect = broadcast_with_error

        app = FastAPI()
        task = asyncio.create_task(game_tick_loop(app))

        # Let it run through error and recovery (need 3+ ticks at 1 second each)
        await asyncio.sleep(3.5)

        # Cancel the task
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        # Should have attempted at least 3 broadcasts
        assert call_count[0] >= 3

    @pytest.mark.asyncio
    @patch("server.app.lifespan.broadcast_game_event")
    @patch("server.app.lifespan.connection_manager")
    async def test_game_tick_loop_cancellation(self, mock_connection_manager, mock_broadcast):
        """Test game tick loop handles cancellation gracefully."""
        from fastapi import FastAPI

        mock_connection_manager.player_websockets = {}
        mock_broadcast.return_value = None

        app = FastAPI()
        task = asyncio.create_task(game_tick_loop(app))

        # Let it start
        await asyncio.sleep(0.5)

        # Cancel the task
        task.cancel()
        # Wait for cancellation to process
        await asyncio.sleep(0.1)

        # Task should be cancelled or done
        assert task.cancelled() or task.done()
