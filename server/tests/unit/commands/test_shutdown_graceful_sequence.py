"""
Tests for the graceful shutdown sequence.

This module tests the complete shutdown sequence execution, including
player persistence, NPC despawning, player disconnection, and service shutdown.

As noted in the Cultes des Goules, proper closure of dimensional portals
requires a specific sequence of rituals.
"""

from unittest.mock import AsyncMock, MagicMock
from uuid import uuid4

import pytest

from server.commands.admin_shutdown_command import execute_shutdown_sequence


class TestGracefulShutdownSequence:
    """Test the complete graceful shutdown sequence."""

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_complete(self):
        """Test complete shutdown sequence with all services present."""
        # Create mock app with all services
        mock_app = MagicMock()

        # Generate UUIDs for test players
        player_id1 = uuid4()
        player_id2 = uuid4()
        player_id3 = uuid4()

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_players = MagicMock(
            side_effect=[
                [
                    {"player_id": player_id1},
                    {"player_id": player_id2},
                    {"player_id": player_id3},
                ],  # First call for persistence
                [
                    {"player_id": player_id1},
                    {"player_id": player_id2},
                    {"player_id": player_id3},
                ],  # Second call for disconnection
            ]
        )
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.force_cleanup = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()
        mock_persistence.save_player = MagicMock()
        # Mock get_player to return Player objects
        mock_player1 = MagicMock()
        mock_player1.player_id = player_id1
        mock_player2 = MagicMock()
        mock_player2.player_id = player_id2
        mock_player3 = MagicMock()
        mock_player3.player_id = player_id3
        mock_persistence.get_player = MagicMock(
            side_effect=lambda player_id: {
                player_id1: mock_player1,
                player_id2: mock_player2,
                player_id3: mock_player3,
            }.get(player_id)
        )
        mock_app.state.persistence = mock_persistence

        # Mock NPC services
        mock_npc_spawning_service = MagicMock()
        mock_app.state.npc_spawning_service = mock_npc_spawning_service

        mock_npc_lifecycle_manager = MagicMock()
        mock_npc_lifecycle_manager.active_npcs = {
            "npc1": MagicMock(),
            "npc2": MagicMock(),
        }
        mock_npc_lifecycle_manager.despawn_npc = MagicMock(return_value=True)
        mock_app.state.npc_lifecycle_manager = mock_npc_lifecycle_manager

        # Mock NATS services
        mock_nats_message_handler = MagicMock()
        mock_nats_message_handler.stop = AsyncMock()
        mock_app.state.nats_message_handler = mock_nats_message_handler

        mock_nats_service = MagicMock()
        mock_nats_service.disconnect = AsyncMock()
        mock_app.state.nats_service = mock_nats_service

        # Mock task registry
        mock_task_registry = MagicMock()
        mock_task_registry.shutdown_all = AsyncMock(return_value=True)
        mock_app.state.task_registry = mock_task_registry

        # Execute shutdown sequence
        await execute_shutdown_sequence(mock_app)

        # Verify Phase 1: Player persistence
        assert mock_persistence.save_player.call_count == 3
        mock_persistence.save_player.assert_any_call(mock_player1)
        mock_persistence.save_player.assert_any_call(mock_player2)
        mock_persistence.save_player.assert_any_call(mock_player3)

        # Verify Phase 2: NPC despawning
        assert mock_npc_lifecycle_manager.despawn_npc.call_count == 2
        mock_npc_lifecycle_manager.despawn_npc.assert_any_call("npc1", reason="server_shutdown")
        mock_npc_lifecycle_manager.despawn_npc.assert_any_call("npc2", reason="server_shutdown")

        # Verify Phase 3: Player disconnection (force_disconnect_player expects UUIDs)
        assert mock_connection_manager.force_disconnect_player.call_count == 3
        mock_connection_manager.force_disconnect_player.assert_any_call(player_id1)
        mock_connection_manager.force_disconnect_player.assert_any_call(player_id2)
        mock_connection_manager.force_disconnect_player.assert_any_call(player_id3)

        # Verify Phase 4: NATS message handler stopped
        mock_nats_message_handler.stop.assert_called_once()

        # Verify Phase 5: NATS service disconnected
        mock_nats_service.disconnect.assert_called_once()

        # Verify Phase 6: Connection manager cleanup
        mock_connection_manager.force_cleanup.assert_called_once()

        # Verify Phase 7: Task registry shutdown
        mock_task_registry.shutdown_all.assert_called_once_with(timeout=5.0)

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_no_players(self):
        """Test shutdown sequence with no connected players."""
        mock_app = MagicMock()

        # Mock connection manager with no players
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_players = MagicMock(return_value=[])
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.force_cleanup = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        mock_persistence = MagicMock()
        mock_persistence.save_player = AsyncMock()
        mock_app.state.persistence = mock_persistence

        # No NPC services
        mock_app.state.npc_spawning_service = None
        mock_app.state.npc_lifecycle_manager = None

        # No NATS services
        mock_app.state.nats_message_handler = None
        mock_app.state.nats_service = None

        # Mock task registry
        mock_task_registry = MagicMock()
        mock_task_registry.shutdown_all = AsyncMock(return_value=True)
        mock_app.state.task_registry = mock_task_registry

        # Execute shutdown sequence
        await execute_shutdown_sequence(mock_app)

        # Verify no player persistence or disconnection occurred
        mock_persistence.save_player.assert_not_called()
        mock_connection_manager.force_disconnect_player.assert_not_called()

        # Verify cleanup still occurred
        mock_connection_manager.force_cleanup.assert_called_once()
        mock_task_registry.shutdown_all.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_player_persistence_error(self):
        """Test shutdown sequence continues even if player persistence fails."""
        mock_app = MagicMock()

        # Generate UUIDs for test players
        player_id1 = uuid4()
        player_id2 = uuid4()

        # Mock connection manager
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_players = MagicMock(
            side_effect=[
                [{"player_id": player_id1}, {"player_id": player_id2}],  # First call for persistence
                [{"player_id": player_id1}, {"player_id": player_id2}],  # Second call for disconnection
            ]
        )
        mock_connection_manager.force_disconnect_player = AsyncMock()
        mock_connection_manager.force_cleanup = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence with error on first save
        mock_persistence = MagicMock()
        mock_persistence.save_player = AsyncMock(
            side_effect=[
                Exception("Database error"),
                None,  # Second save succeeds
            ]
        )
        # Mock get_player to return Player objects
        mock_player1 = MagicMock()
        mock_player1.player_id = player_id1
        mock_player2 = MagicMock()
        mock_player2.player_id = player_id2
        mock_persistence.get_player = MagicMock(
            side_effect=lambda player_id: {
                player_id1: mock_player1,
                player_id2: mock_player2,
            }.get(player_id)
        )
        mock_app.state.persistence = mock_persistence

        # No NPC services
        mock_app.state.npc_spawning_service = None

        # Mock NATS services
        mock_nats_message_handler = MagicMock()
        mock_nats_message_handler.stop = AsyncMock()
        mock_app.state.nats_message_handler = mock_nats_message_handler

        mock_nats_service = MagicMock()
        mock_nats_service.disconnect = AsyncMock()
        mock_app.state.nats_service = mock_nats_service

        # Mock task registry
        mock_task_registry = MagicMock()
        mock_task_registry.shutdown_all = AsyncMock(return_value=True)
        mock_app.state.task_registry = mock_task_registry

        # Execute shutdown sequence - should not raise exception
        await execute_shutdown_sequence(mock_app)

        # Verify persistence was attempted for both players
        assert mock_persistence.save_player.call_count == 2

        # Verify shutdown continued despite error
        assert mock_connection_manager.force_disconnect_player.call_count == 2
        mock_nats_message_handler.stop.assert_called_once()
        mock_task_registry.shutdown_all.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_npc_despawn_error(self):
        """Test shutdown sequence continues even if NPC despawn fails."""
        mock_app = MagicMock()

        # Minimal mocks for other phases
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_players = MagicMock(return_value=[])
        mock_connection_manager.force_cleanup = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        mock_persistence = MagicMock()
        mock_app.state.persistence = mock_persistence

        # Mock NPC services with error on first despawn
        mock_npc_spawning_service = MagicMock()
        mock_app.state.npc_spawning_service = mock_npc_spawning_service

        mock_npc_lifecycle_manager = MagicMock()
        mock_npc_lifecycle_manager.active_npcs = {
            "npc1": MagicMock(),
            "npc2": MagicMock(),
        }
        mock_npc_lifecycle_manager.despawn_npc = MagicMock(
            side_effect=[
                Exception("Despawn error"),
                True,  # Second despawn succeeds
            ]
        )
        mock_app.state.npc_lifecycle_manager = mock_npc_lifecycle_manager

        # Mock NATS services
        mock_nats_message_handler = MagicMock()
        mock_nats_message_handler.stop = AsyncMock()
        mock_app.state.nats_message_handler = mock_nats_message_handler

        mock_nats_service = MagicMock()
        mock_nats_service.disconnect = AsyncMock()
        mock_app.state.nats_service = mock_nats_service

        # Mock task registry
        mock_task_registry = MagicMock()
        mock_task_registry.shutdown_all = AsyncMock(return_value=True)
        mock_app.state.task_registry = mock_task_registry

        # Execute shutdown sequence - should not raise exception
        await execute_shutdown_sequence(mock_app)

        # Verify despawn was attempted for both NPCs
        assert mock_npc_lifecycle_manager.despawn_npc.call_count == 2

        # Verify shutdown continued despite error
        mock_nats_message_handler.stop.assert_called_once()
        mock_task_registry.shutdown_all.assert_called_once()

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_task_registry_timeout(self):
        """Test shutdown sequence handles task registry timeout gracefully."""
        mock_app = MagicMock()

        # Minimal mocks
        mock_connection_manager = MagicMock()
        mock_connection_manager.get_online_players = MagicMock(return_value=[])
        mock_connection_manager.force_cleanup = AsyncMock()
        mock_app.state.connection_manager = mock_connection_manager

        mock_persistence = MagicMock()
        mock_app.state.persistence = mock_persistence

        # No NPC or NATS services
        mock_app.state.npc_spawning_service = None
        mock_app.state.nats_message_handler = None
        mock_app.state.nats_service = None

        # Mock task registry with timeout
        mock_task_registry = MagicMock()
        mock_task_registry.shutdown_all = AsyncMock(return_value=False)  # Timeout
        mock_app.state.task_registry = mock_task_registry

        # Execute shutdown sequence - should not raise exception
        await execute_shutdown_sequence(mock_app)

        # Verify task registry shutdown was attempted
        mock_task_registry.shutdown_all.assert_called_once_with(timeout=5.0)

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_missing_services(self):
        """Test shutdown sequence handles missing services gracefully."""
        mock_app = MagicMock()

        # No services at all
        mock_app.state.connection_manager = None
        mock_app.state.persistence = None
        mock_app.state.npc_spawning_service = None
        mock_app.state.npc_lifecycle_manager = None
        mock_app.state.nats_message_handler = None
        mock_app.state.nats_service = None
        mock_app.state.task_registry = None

        # Execute shutdown sequence - should not raise exception
        await execute_shutdown_sequence(mock_app)

        # Test should complete without errors

    @pytest.mark.asyncio
    async def test_execute_shutdown_sequence_phase_ordering(self):
        """Test that shutdown phases execute in the correct order."""
        mock_app = MagicMock()
        execution_order = []

        # Generate UUID for test player
        player_id = uuid4()

        # Mock connection manager
        mock_connection_manager = MagicMock()

        def record_get_players_call():
            execution_order.append("get_players")
            return [{"player_id": player_id}]

        mock_connection_manager.get_online_players = MagicMock(side_effect=record_get_players_call)

        async def record_force_disconnect(*args, **kwargs):
            execution_order.append("disconnect_player")

        mock_connection_manager.force_disconnect_player = AsyncMock(side_effect=record_force_disconnect)

        async def record_force_cleanup():
            execution_order.append("cleanup_connection_manager")

        mock_connection_manager.force_cleanup = AsyncMock(side_effect=record_force_cleanup)
        mock_app.state.connection_manager = mock_connection_manager

        # Mock persistence
        mock_persistence = MagicMock()

        def record_get_player(player_id):
            execution_order.append(f"get_player_{player_id}")
            mock_player = MagicMock()
            mock_player.player_id = player_id
            return mock_player

        def record_save_player(player_obj):
            execution_order.append(f"save_player_{player_obj.player_id}")

        mock_persistence.get_player = MagicMock(side_effect=record_get_player)
        mock_persistence.save_player = MagicMock(side_effect=record_save_player)
        mock_app.state.persistence = mock_persistence

        # Mock NPC services
        mock_npc_spawning_service = MagicMock()
        mock_app.state.npc_spawning_service = mock_npc_spawning_service

        mock_npc_lifecycle_manager = MagicMock()
        mock_npc_lifecycle_manager.active_npcs = {"npc1": MagicMock()}

        def record_despawn_npc(npc_id, **kwargs):
            execution_order.append(f"despawn_npc_{npc_id}")
            return True

        mock_npc_lifecycle_manager.despawn_npc = MagicMock(side_effect=record_despawn_npc)
        mock_app.state.npc_lifecycle_manager = mock_npc_lifecycle_manager

        # Mock NATS services
        mock_nats_message_handler = MagicMock()

        async def record_stop_nats_handler():
            execution_order.append("stop_nats_handler")

        mock_nats_message_handler.stop = AsyncMock(side_effect=record_stop_nats_handler)
        mock_app.state.nats_message_handler = mock_nats_message_handler

        mock_nats_service = MagicMock()

        async def record_disconnect_nats():
            execution_order.append("disconnect_nats")

        mock_nats_service.disconnect = AsyncMock(side_effect=record_disconnect_nats)
        mock_app.state.nats_service = mock_nats_service

        # Mock task registry
        mock_task_registry = MagicMock()

        async def record_shutdown_tasks(timeout):
            execution_order.append("shutdown_tasks")
            return True

        mock_task_registry.shutdown_all = AsyncMock(side_effect=record_shutdown_tasks)
        mock_app.state.task_registry = mock_task_registry

        # Execute shutdown sequence
        await execute_shutdown_sequence(mock_app)

        # Verify execution order (player_id will be UUID, so check pattern instead of exact match)
        assert execution_order[0] == "get_players"  # Phase 1: Get players for persistence
        assert execution_order[1].startswith("get_player_")  # Phase 1: Get player object
        assert execution_order[2].startswith("save_player_")  # Phase 1: Save player
        assert execution_order[3] == "despawn_npc_npc1"  # Phase 2: Despawn NPC
        assert execution_order[4] == "get_players"  # Phase 3: Get players for disconnection
        assert execution_order[5] == "disconnect_player"  # Phase 3: Disconnect player
        assert execution_order[6] == "stop_nats_handler"  # Phase 4: Stop NATS handler
        assert execution_order[7] == "disconnect_nats"  # Phase 5: Disconnect NATS
        assert execution_order[8] == "cleanup_connection_manager"  # Phase 6: Cleanup connection manager
        assert execution_order[9] == "shutdown_tasks"  # Phase 7: Shutdown tasks
        assert len(execution_order) == 10  # Verify all phases executed
