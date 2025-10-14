"""
Tests for application lifespan management.

This module tests the application startup and shutdown procedures,
including database initialization, service setup, and the game tick loop.

As documented in the Cultes des Goules, proper lifecycle management
is essential for maintaining the dimensional integrity of our server.
"""

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest
from fastapi import FastAPI

from ..app.lifespan import game_tick_loop, lifespan


class TestLifespanStartup:
    """Test application startup procedures."""

    @pytest.mark.asyncio
    async def test_lifespan_startup_basic(self):
        """Test basic lifespan startup sequence.

        AI: Tests that critical services are initialized during startup.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence") as mock_persistence:
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry") as mock_registry:
                                with patch("server.app.lifespan.connection_manager"):
                                    # Setup mocks
                                    mock_handler = Mock()
                                    mock_handler.event_bus = Mock()
                                    mock_handler.event_bus.set_main_loop = Mock()
                                    mock_event_handler.return_value = mock_handler

                                    mock_persist = Mock()
                                    mock_persistence.return_value = mock_persist

                                    config = Mock()
                                    config.logging.environment = "unit_test"
                                    config.nats.enabled = False
                                    mock_config.return_value = config

                                    task_reg = Mock()
                                    task_reg.register_task = Mock(return_value=Mock())
                                    mock_registry.return_value = task_reg

                                    # Run lifespan
                                    async with lifespan(app):
                                        # Verify critical services are initialized
                                        assert hasattr(app.state, "persistence")
                                        assert hasattr(app.state, "event_handler")
                                        assert hasattr(app.state, "event_bus")
                                        assert hasattr(app.state, "task_registry")

    @pytest.mark.asyncio
    async def test_lifespan_nats_disabled_in_test(self):
        """Test lifespan with NATS disabled in test environment.

        AI: Tests that NATS can be disabled in test environments without error.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry"):
                                with patch("server.app.lifespan.connection_manager"):
                                    mock_handler = Mock()
                                    mock_handler.event_bus = Mock()
                                    mock_handler.event_bus.set_main_loop = Mock()
                                    mock_event_handler.return_value = mock_handler

                                    config = Mock()
                                    config.logging.environment = "unit_test"
                                    config.nats.enabled = False
                                    mock_config.return_value = config

                                    async with lifespan(app):
                                        # Verify NATS service is None in test environment
                                        assert app.state.nats_service is None
                                        assert app.state.nats_message_handler is None

    @pytest.mark.asyncio
    async def test_lifespan_nats_connection_failure_in_test(self):
        """Test NATS connection failure is non-fatal in test environment.

        AI: Tests graceful degradation when NATS connection fails in test mode.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry"):
                                with patch("server.app.lifespan.nats_service") as mock_nats:
                                    with patch("server.app.lifespan.connection_manager"):
                                        mock_handler = Mock()
                                        mock_handler.event_bus = Mock()
                                        mock_handler.event_bus.set_main_loop = Mock()
                                        mock_event_handler.return_value = mock_handler

                                        config = Mock()
                                        config.logging.environment = "unit_test"
                                        config.nats.enabled = True
                                        mock_config.return_value = config

                                        # Simulate NATS connection failure
                                        mock_nats.connect = AsyncMock(return_value=False)

                                        async with lifespan(app):
                                            # Should continue without error
                                            assert app.state.nats_service is None

    @pytest.mark.asyncio
    async def test_lifespan_initializes_player_service(self):
        """Test that PlayerService is initialized.

        AI: Tests initialization of critical PlayerService.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence") as mock_persistence:
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry"):
                                with patch("server.game.player_service.PlayerService") as mock_player_service:
                                    with patch("server.app.lifespan.connection_manager"):
                                        mock_handler = Mock()
                                        mock_handler.event_bus = Mock()
                                        mock_handler.event_bus.set_main_loop = Mock()
                                        mock_event_handler.return_value = mock_handler

                                        mock_persist = Mock()
                                        mock_persistence.return_value = mock_persist

                                        config = Mock()
                                        config.logging.environment = "unit_test"
                                        config.nats.enabled = False
                                        mock_config.return_value = config

                                        mock_service = Mock()
                                        mock_player_service.return_value = mock_service

                                        async with lifespan(app):
                                            assert hasattr(app.state, "player_service")
                                            mock_player_service.assert_called_once_with(mock_persist)

    @pytest.mark.asyncio
    async def test_lifespan_initializes_user_manager(self):
        """Test that UserManager is initialized with correct path.

        AI: Tests initialization of UserManager with environment-aware paths.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry"):
                                with patch("server.services.user_manager.UserManager") as mock_user_manager:
                                    with patch("server.app.lifespan.connection_manager"):
                                        mock_handler = Mock()
                                        mock_handler.event_bus = Mock()
                                        mock_handler.event_bus.set_main_loop = Mock()
                                        mock_event_handler.return_value = mock_handler

                                        config = Mock()
                                        config.logging.environment = "unit_test"
                                        config.nats.enabled = False
                                        mock_config.return_value = config

                                        mock_manager = Mock()
                                        mock_user_manager.return_value = mock_manager

                                        async with lifespan(app):
                                            assert hasattr(app.state, "user_manager")
                                            # Verify data_dir includes environment
                                            call_args = mock_user_manager.call_args
                                            data_dir = call_args.kwargs.get("data_dir")
                                            assert "unit_test" in str(data_dir)

    @pytest.mark.asyncio
    async def test_lifespan_initializes_npc_services(self):
        """Test that NPC services are initialized.

        AI: Tests initialization of NPC lifecycle, spawning, and population services.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry"):
                                with patch("server.npc.lifecycle_manager.NPCLifecycleManager"):
                                    with patch("server.npc.spawning_service.NPCSpawningService"):
                                        with patch("server.npc.population_control.NPCPopulationController"):
                                            with patch(
                                                "server.services.npc_instance_service.initialize_npc_instance_service"
                                            ):
                                                with patch("server.app.lifespan.connection_manager"):
                                                    with patch("server.npc_database.get_npc_session"):
                                                        mock_handler = Mock()
                                                        mock_handler.event_bus = Mock()
                                                        mock_handler.event_bus.set_main_loop = Mock()
                                                        mock_event_handler.return_value = mock_handler

                                                        config = Mock()
                                                        config.logging.environment = "unit_test"
                                                        config.nats.enabled = False
                                                        mock_config.return_value = config

                                                        async with lifespan(app):
                                                            assert hasattr(app.state, "npc_lifecycle_manager")
                                                            assert hasattr(app.state, "npc_spawning_service")
                                                            assert hasattr(app.state, "npc_population_controller")

    @pytest.mark.asyncio
    async def test_lifespan_initializes_chat_service(self):
        """Test that ChatService is initialized.

        AI: Tests initialization of ChatService with required dependencies.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence") as mock_persistence:
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry"):
                                with patch("server.game.chat_service.ChatService") as mock_chat_service:
                                    with patch("server.app.lifespan.connection_manager"):
                                        mock_handler = Mock()
                                        mock_handler.event_bus = Mock()
                                        mock_handler.event_bus.set_main_loop = Mock()
                                        mock_event_handler.return_value = mock_handler

                                        mock_persist = Mock()
                                        mock_persistence.return_value = mock_persist

                                        config = Mock()
                                        config.logging.environment = "unit_test"
                                        config.nats.enabled = False
                                        mock_config.return_value = config

                                        mock_chat = Mock()
                                        mock_chat.nats_service = None
                                        mock_chat_service.return_value = mock_chat

                                        async with lifespan(app):
                                            assert hasattr(app.state, "chat_service")
                                            mock_chat_service.assert_called_once()


class TestLifespanShutdown:
    """Test application shutdown procedures."""

    @pytest.mark.asyncio
    async def test_lifespan_shutdown_stops_nats(self):
        """Test that NATS services are stopped during shutdown.

        AI: Tests proper shutdown of NATS message handler and service.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry") as mock_registry:
                                with patch("server.app.lifespan.connection_manager"):
                                    mock_handler = Mock()
                                    mock_handler.event_bus = Mock()
                                    mock_handler.event_bus.set_main_loop = Mock()
                                    mock_event_handler.return_value = mock_handler

                                    config = Mock()
                                    config.logging.environment = "unit_test"
                                    config.nats.enabled = False
                                    mock_config.return_value = config

                                    task_reg = Mock()
                                    task_reg.register_task = Mock(return_value=Mock())
                                    task_reg.shutdown_all = AsyncMock(return_value=True)
                                    mock_registry.return_value = task_reg

                                    async with lifespan(app):
                                        # Add mock NATS services
                                        mock_nats_handler = Mock()
                                        mock_nats_handler.stop = AsyncMock()
                                        app.state.nats_message_handler = mock_nats_handler

                                        mock_nats_service = Mock()
                                        mock_nats_service.disconnect = AsyncMock()
                                        app.state.nats_service = mock_nats_service

                                    # Verify shutdown methods were called
                                    mock_nats_handler.stop.assert_called_once()
                                    mock_nats_service.disconnect.assert_called_once()

    @pytest.mark.asyncio
    async def test_lifespan_shutdown_cleans_connection_manager(self):
        """Test that connection manager is cleaned up.

        AI: Tests proper cleanup of connection manager during shutdown.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry") as mock_registry:
                                with patch("server.app.lifespan.connection_manager") as mock_conn_mgr:
                                    mock_handler = Mock()
                                    mock_handler.event_bus = Mock()
                                    mock_handler.event_bus.set_main_loop = Mock()
                                    mock_event_handler.return_value = mock_handler

                                    config = Mock()
                                    config.logging.environment = "unit_test"
                                    config.nats.enabled = False
                                    mock_config.return_value = config

                                    task_reg = Mock()
                                    task_reg.register_task = Mock(return_value=Mock())
                                    task_reg.shutdown_all = AsyncMock(return_value=True)
                                    mock_registry.return_value = task_reg

                                    mock_conn_mgr.force_cleanup = AsyncMock()

                                    async with lifespan(app):
                                        pass

                                    # Verify force_cleanup was called
                                    mock_conn_mgr.force_cleanup.assert_called_once()

    @pytest.mark.asyncio
    async def test_lifespan_shutdown_uses_task_registry(self):
        """Test that shutdown uses TaskRegistry coordination.

        AI: Tests TaskRegistry-coordinated shutdown of all tasks.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry") as mock_registry:
                                with patch("server.app.lifespan.connection_manager"):
                                    mock_handler = Mock()
                                    mock_handler.event_bus = Mock()
                                    mock_handler.event_bus.set_main_loop = Mock()
                                    mock_event_handler.return_value = mock_handler

                                    config = Mock()
                                    config.logging.environment = "unit_test"
                                    config.nats.enabled = False
                                    mock_config.return_value = config

                                    task_reg = Mock()
                                    task_reg.register_task = Mock(return_value=Mock())
                                    task_reg.shutdown_all = AsyncMock(return_value=True)
                                    mock_registry.return_value = task_reg

                                    async with lifespan(app):
                                        pass

                                    # Verify TaskRegistry shutdown was called
                                    task_reg.shutdown_all.assert_called_once()

    @pytest.mark.asyncio
    async def test_lifespan_shutdown_handles_errors_gracefully(self):
        """Test that shutdown errors are handled gracefully.

        AI: Tests error handling during shutdown doesn't prevent completion.
        """
        app = FastAPI()

        with patch("server.app.lifespan.init_db", AsyncMock()):
            with patch("server.app.lifespan.init_npc_db", AsyncMock()):
                with patch("server.app.lifespan.get_real_time_event_handler") as mock_event_handler:
                    with patch("server.app.lifespan.get_persistence"):
                        with patch("server.app.lifespan.get_config") as mock_config:
                            with patch("server.app.lifespan.TaskRegistry") as mock_registry:
                                with patch("server.app.lifespan.connection_manager"):
                                    mock_handler = Mock()
                                    mock_handler.event_bus = Mock()
                                    mock_handler.event_bus.set_main_loop = Mock()
                                    mock_event_handler.return_value = mock_handler

                                    config = Mock()
                                    config.logging.environment = "unit_test"
                                    config.nats.enabled = False
                                    mock_config.return_value = config

                                    task_reg = Mock()
                                    task_reg.register_task = Mock(return_value=Mock())
                                    # Simulate error during shutdown
                                    task_reg.shutdown_all = AsyncMock(side_effect=Exception("Shutdown error"))
                                    mock_registry.return_value = task_reg

                                    # Should not raise exception
                                    async with lifespan(app):
                                        pass


class TestGameTickLoop:
    """Test game tick loop functionality."""

    @pytest.mark.asyncio
    async def test_game_tick_loop_broadcasts_events(self):
        """Test that game tick loop broadcasts tick events.

        AI: Tests that tick data is broadcast to connected players.
        """
        app = FastAPI()

        with patch("server.app.lifespan.broadcast_game_event", AsyncMock()) as mock_broadcast:
            with patch("server.app.lifespan.connection_manager") as mock_conn_mgr:
                mock_conn_mgr.player_websockets = {}

                # Run loop for a short time
                task = asyncio.create_task(game_tick_loop(app))

                # Wait for a few ticks
                await asyncio.sleep(0.1)

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
    async def test_game_tick_loop_handles_cancellation(self):
        """Test that game tick loop handles cancellation gracefully.

        AI: Tests proper cancellation handling in game tick loop.
        """
        app = FastAPI()

        with patch("server.app.lifespan.broadcast_game_event", AsyncMock()):
            with patch("server.app.lifespan.connection_manager") as mock_conn_mgr:
                mock_conn_mgr.player_websockets = {}

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
    async def test_game_tick_loop_handles_errors(self):
        """Test that game tick loop handles errors and continues.

        AI: Tests error recovery in game tick loop.
        """
        app = FastAPI()

        call_count = 0

        async def mock_broadcast_with_error(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise Exception("Broadcast error")
            # Succeed on subsequent calls

        with patch("server.app.lifespan.broadcast_game_event", mock_broadcast_with_error):
            with patch("server.app.lifespan.connection_manager") as mock_conn_mgr:
                mock_conn_mgr.player_websockets = {}

                task = asyncio.create_task(game_tick_loop(app))

                # Wait for multiple ticks (2 seconds at 1 second interval = 2 ticks minimum)
                await asyncio.sleep(2.5)

                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

                # Should have attempted multiple ticks despite first error
                assert call_count >= 2

    @pytest.mark.asyncio
    async def test_game_tick_loop_includes_active_player_count(self):
        """Test that tick data includes active player count.

        AI: Tests that broadcast includes connection manager player count.
        """
        app = FastAPI()

        captured_data = []

        async def capture_broadcast(event_type, data):
            captured_data.append((event_type, data))

        with patch("server.app.lifespan.broadcast_game_event", capture_broadcast):
            with patch("server.app.lifespan.connection_manager") as mock_conn_mgr:
                mock_conn_mgr.player_websockets = {"player1": Mock(), "player2": Mock()}

                task = asyncio.create_task(game_tick_loop(app))

                # Wait for at least one tick
                await asyncio.sleep(0.05)

                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

                # Verify tick data structure
                assert len(captured_data) > 0
                event_type, tick_data = captured_data[0]
                assert event_type == "game_tick"
                assert "tick_number" in tick_data
                assert "timestamp" in tick_data
                assert tick_data["active_players"] == 2
