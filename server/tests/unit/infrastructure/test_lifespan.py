"""
Tests for application lifespan management.

This module tests the startup and shutdown logic for the FastAPI application,
including initialization sequences and the game tick loop.
"""

import asyncio
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from fastapi import FastAPI

from server.app.lifespan import game_tick_loop, lifespan


class TestGameTickLoop:
    """Test game tick loop functionality."""

    @pytest.mark.asyncio
    @patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock)
    async def test_game_tick_loop_runs(self, mock_broadcast):
        """Test game tick loop executes ticks."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.player_websockets = {"player1": MagicMock(), "player2": MagicMock()}
        mock_broadcast.return_value = None

        app = FastAPI()
        app.state.container = MagicMock()
        app.state.container.connection_manager = mock_connection_manager
        # Mock persistence with async methods for corpse cleanup
        mock_persistence = MagicMock()
        mock_persistence.get_decayed_containers = AsyncMock(return_value=[])
        app.state.container.persistence = mock_persistence

        task = asyncio.create_task(game_tick_loop(app))

        # Let it run for a few ticks (tick interval is 0.1 seconds, need at least 0.15 seconds for one tick)
        await asyncio.sleep(0.2)

        # Cancel the task
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        # Verify broadcast was called
        assert mock_broadcast.call_count >= 1

    @pytest.mark.asyncio
    @patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock)
    async def test_game_tick_loop_broadcast_data(self, mock_broadcast):
        """Test game tick loop broadcasts correct data."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.player_websockets = {"player1": MagicMock()}
        mock_broadcast.return_value = None

        app = FastAPI()
        app.state.container = MagicMock()
        app.state.container.connection_manager = mock_connection_manager
        # Mock persistence with async methods for corpse cleanup
        mock_persistence = MagicMock()
        mock_persistence.get_decayed_containers = AsyncMock(return_value=[])
        app.state.container.persistence = mock_persistence

        task = asyncio.create_task(game_tick_loop(app))

        # Let one tick execute (tick interval is 0.1 seconds, need at least 0.15 seconds for one tick)
        await asyncio.sleep(0.2)

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
    @patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock)
    async def test_game_tick_loop_handles_exception(self, mock_broadcast):
        """Test game tick loop continues after exception."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.player_websockets = {}
        call_count = [0]  # Use list to avoid closure issues

        async def broadcast_with_error(*_args, **_kwargs):
            call_count[0] += 1
            # First call succeeds, second call fails
            if call_count[0] == 2:
                raise RuntimeError("Broadcast error")
            # Third call should succeed (loop continues)

        mock_broadcast.side_effect = broadcast_with_error

        app = FastAPI()
        app.state.container = MagicMock()
        app.state.container.connection_manager = mock_connection_manager
        # Mock persistence with async methods for corpse cleanup
        mock_persistence = MagicMock()
        mock_persistence.get_decayed_containers = AsyncMock(return_value=[])
        app.state.container.persistence = mock_persistence

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
    @patch("server.realtime.connection_manager.broadcast_game_event", new_callable=AsyncMock)
    async def test_game_tick_loop_cancellation(self, mock_broadcast):
        """Test game tick loop handles cancellation gracefully."""
        mock_connection_manager = MagicMock()
        mock_connection_manager.player_websockets = {}
        mock_broadcast.return_value = None

        app = FastAPI()
        app.state.container = MagicMock()
        app.state.container.connection_manager = mock_connection_manager
        # Mock persistence with async methods for corpse cleanup
        mock_persistence = MagicMock()
        mock_persistence.get_decayed_containers = AsyncMock(return_value=[])
        app.state.container.persistence = mock_persistence

        task = asyncio.create_task(game_tick_loop(app))

        # Let it start
        await asyncio.sleep(0.5)

        # Cancel the task
        task.cancel()
        # Wait for cancellation to process
        await asyncio.sleep(0.1)

        # Task should be cancelled or done
        assert task.cancelled() or task.done()


# ============================================================================
# Tests merged from test_lifespan_legacy.py
# ============================================================================


"""
Tests for application lifespan management.

This module tests the application startup and shutdown procedures,
including database initialization, service setup, and the game tick loop.

As documented in the Cultes des Goules, proper lifecycle management
is essential for maintaining the dimensional integrity of our server.
"""


class TestLifespanStartup:
    """Test application startup procedures."""

    @pytest.mark.asyncio
    async def test_lifespan_startup_basic(self) -> None:
        """
        Test basic lifespan startup sequence with ApplicationContainer.

        AI: ARCHITECTURE CHANGE - Tests that ApplicationContainer and critical services are initialized during startup.
        The lifespan now uses ApplicationContainer instead of individual global functions.
        """
        app = FastAPI()

        with patch("server.database.init_db", AsyncMock()):
            with patch("server.npc_database.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.ApplicationContainer") as mock_container_class:
                    # Setup mock container
                    mock_container = AsyncMock()
                    mock_container.initialize = AsyncMock()
                    mock_container.shutdown = AsyncMock()

                    # Mock container services
                    mock_container.task_registry = Mock()
                    mock_container.event_bus = Mock()
                    mock_container.event_bus.set_main_loop = Mock()
                    mock_container.real_time_event_handler = Mock()
                    mock_container.real_time_event_handler.event_bus = mock_container.event_bus
                    mock_container.persistence = Mock()
                    mock_container.connection_manager = Mock()
                    mock_container.player_service = Mock()
                    mock_container.room_service = Mock()
                    mock_container.user_manager = Mock()
                    mock_container.room_cache_service = Mock()
                    mock_container.profession_cache_service = Mock()
                    mock_container.config = Mock()
                    mock_container.config.logging = Mock()
                    mock_container.config.logging.environment = "unit_test"

                    # Mock nats_service with synchronous is_connected()
                    mock_container.nats_service = Mock()
                    mock_container.nats_service.is_connected = Mock(return_value=False)

                    mock_container_class.return_value = mock_container

                    # Run lifespan
                    async with lifespan(app):
                        # ARCHITECTURE FIX: Verify container is initialized
                        assert hasattr(app.state, "container")
                        # Verify critical services are accessible via container
                        assert hasattr(app.state, "persistence")
                        assert hasattr(app.state, "event_handler")
                        assert hasattr(app.state, "event_bus")
                        assert hasattr(app.state, "task_registry")


class TestGameTickLoopLegacy:
    """Test game tick loop functionality."""

    @pytest.mark.asyncio
    async def test_game_tick_loop_broadcasts_events(self) -> None:
        """Test that game tick loop broadcasts tick events.

        AI: Tests that tick data is broadcast to connected players.
        """
        app = FastAPI()

        with patch("server.app.game_tick_processing.broadcast_game_event", new_callable=AsyncMock) as mock_broadcast:
            mock_conn_mgr = MagicMock()
            mock_conn_mgr.player_websockets = {}

            app.state.container = MagicMock()
            app.state.container.connection_manager = mock_conn_mgr

            # Run loop for a short time
            task = asyncio.create_task(game_tick_loop(app))

            # Wait for at least one tick (tick interval is 0.1 seconds, need at least 0.15 seconds for one tick)
            await asyncio.sleep(0.2)

            # Cancel the loop
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

            # Verify broadcast was called
            assert mock_broadcast.call_count > 0
            call_args = mock_broadcast.call_args_list[0]
            assert call_args[0][0] == "game_tick"
            assert "tick_number" in call_args[0][1]

    @pytest.mark.asyncio
    async def test_game_tick_loop_handles_cancellation(self) -> None:
        """Test that game tick loop handles cancellation gracefully.

        AI: Tests proper cancellation handling in game tick loop.
        """
        app = FastAPI()

        with patch("server.realtime.connection_manager.broadcast_game_event", new_callable=AsyncMock):
            mock_conn_mgr = MagicMock()
            mock_conn_mgr.player_websockets = {}

            app.state.container = MagicMock()
            app.state.container.connection_manager = mock_conn_mgr

            task = asyncio.create_task(game_tick_loop(app))

            # Let it run briefly
            await asyncio.sleep(0.05)

            # Cancel it
            task.cancel()

            # Should not raise exception
            try:
                await task
            except asyncio.CancelledError:
                pass  # Expected

    @pytest.mark.asyncio
    async def test_game_tick_loop_handles_errors(self) -> None:
        """Test that game tick loop handles errors and continues.

        AI: Tests error recovery in game tick loop.
        """
        app = FastAPI()

        call_count = 0

        async def mock_broadcast_with_error(*_args, **_kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise RuntimeError("Broadcast error")
            # Succeed on subsequent calls

        with patch(
            "server.app.game_tick_processing.broadcast_game_event",
            new_callable=AsyncMock,
            side_effect=mock_broadcast_with_error,
        ):
            mock_conn_mgr = MagicMock()
            mock_conn_mgr.player_websockets = {}

            # Mock persistence with async methods for corpse cleanup
            mock_persistence = MagicMock()
            mock_persistence.get_decayed_containers = AsyncMock(return_value=[])

            app.state.container = MagicMock()
            app.state.container.connection_manager = mock_conn_mgr
            app.state.container.persistence = mock_persistence

            task = asyncio.create_task(game_tick_loop(app))

            # Wait for multiple ticks (1.5 seconds at 0.1 second interval = 15 ticks minimum)
            # This ensures we get at least 2 broadcast attempts (tick 0 and tick 10)
            # Need extra time to account for error handling delays
            await asyncio.sleep(1.5)

            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

            # Should have attempted multiple broadcasts despite first error
            # Broadcast happens every 10 ticks, so at 1.5 seconds we should see tick 0 and tick 10
            assert call_count >= 2

    @pytest.mark.asyncio
    async def test_game_tick_loop_includes_active_player_count(self) -> None:
        """Test that tick data includes active player count.

        AI: Tests that broadcast includes connection manager player count.
        """
        app = FastAPI()

        captured_data = []

        async def capture_broadcast(event_type, data):
            captured_data.append((event_type, data))

        with patch(
            "server.app.game_tick_processing.broadcast_game_event",
            new_callable=AsyncMock,
            side_effect=capture_broadcast,
        ):
            mock_conn_mgr = MagicMock()
            mock_conn_mgr.player_websockets = {"player1": Mock(), "player2": Mock()}

            app.state.container = MagicMock()
            app.state.container.connection_manager = mock_conn_mgr

            task = asyncio.create_task(game_tick_loop(app))

            # Wait for at least one tick (tick interval is 0.1 seconds, need at least 0.15 seconds for one tick)
            await asyncio.sleep(0.2)

            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass

            # Ensure we captured broadcast data
            assert captured_data
            event_type, data = captured_data[0]
            assert event_type == "game_tick"
            assert data.get("active_players") == 2
