"""
Unit tests for NPC combat lifecycle.

Tests the NPCCombatLifecycle class for managing NPC despawning during combat.
"""

from unittest.mock import MagicMock

import pytest

from server.services.npc_combat_lifecycle import NPCCombatLifecycle


class TestNPCCombatLifecycle:
    """Test suite for NPCCombatLifecycle class."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return MagicMock()

    @pytest.fixture
    def lifecycle_service(self, mock_persistence):
        """Create a NPCCombatLifecycle instance for testing."""
        return NPCCombatLifecycle(mock_persistence)

    def test_init(self, mock_persistence):
        """Test NPCCombatLifecycle initialization."""
        service = NPCCombatLifecycle(mock_persistence)
        assert service._persistence == mock_persistence

    @pytest.mark.asyncio
    async def test_despawn_npc_safely_success(self, lifecycle_service, mock_persistence):
        """Test despawn_npc_safely successfully despawns NPC."""
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.despawn_npc = MagicMock()
        mock_lifecycle_manager.record_npc_death = MagicMock()

        # get_npc_lifecycle_manager is called via asyncio.to_thread, so it should be synchronous
        def get_lifecycle_manager():
            return mock_lifecycle_manager

        mock_persistence.get_npc_lifecycle_manager = get_lifecycle_manager

        await lifecycle_service.despawn_npc_safely("npc_001", "room_001")

        mock_lifecycle_manager.record_npc_death.assert_called_once_with("npc_001")
        mock_lifecycle_manager.despawn_npc.assert_called_once_with("npc_001", "combat_death")

    @pytest.mark.asyncio
    async def test_despawn_npc_safely_no_lifecycle_manager(self, lifecycle_service, mock_persistence):
        """Test despawn_npc_safely handles missing lifecycle manager."""
        mock_persistence.get_npc_lifecycle_manager = None

        await lifecycle_service.despawn_npc_safely("npc_001", "room_001")
        # Should not raise

    @pytest.mark.asyncio
    async def test_despawn_npc_safely_exception(self, lifecycle_service, mock_persistence):
        """Test despawn_npc_safely handles exceptions gracefully."""
        mock_persistence.get_npc_lifecycle_manager = MagicMock(side_effect=ValueError("Test error"))

        await lifecycle_service.despawn_npc_safely("npc_001", "room_001")
        # Should not raise, just log error

    @pytest.mark.asyncio
    async def test_despawn_npc_safely_sqlalchemy_error(self, lifecycle_service, mock_persistence):
        """Test despawn_npc_safely handles SQLAlchemy errors."""
        from sqlalchemy.exc import SQLAlchemyError

        def get_lifecycle_manager():
            raise SQLAlchemyError("Database error")

        mock_persistence.get_npc_lifecycle_manager = get_lifecycle_manager

        await lifecycle_service.despawn_npc_safely("npc_001", "room_001")
        # Should not raise, just log error

    @pytest.mark.asyncio
    async def test_despawn_npc_with_active_npcs(self, lifecycle_service, mock_persistence):
        """Test _despawn_npc handles NPC in active_npcs via fallback path."""
        # The first path returns early, so we need to make it return None
        # to test the second path that handles active_npcs
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {"npc_001": MagicMock()}
        call_count = 0

        def get_lifecycle_manager():
            nonlocal call_count
            call_count += 1
            # First call returns None to skip first path
            if call_count == 1:
                return None
            # Second call returns manager with active_npcs for fallback path
            return mock_lifecycle_manager

        mock_persistence.get_npc_lifecycle_manager = get_lifecycle_manager

        await lifecycle_service._despawn_npc("npc_001", "room_001")

        # The fallback path should delete from active_npcs
        assert "npc_001" not in mock_lifecycle_manager.active_npcs

    @pytest.mark.asyncio
    async def test_despawn_npc_no_active_npcs(self, lifecycle_service, mock_persistence):
        """Test _despawn_npc handles NPC not in active_npcs."""
        mock_lifecycle_manager = MagicMock()
        mock_lifecycle_manager.active_npcs = {}

        def get_lifecycle_manager():
            return mock_lifecycle_manager

        mock_persistence.get_npc_lifecycle_manager = get_lifecycle_manager

        await lifecycle_service._despawn_npc("npc_002", "room_001")
        # Should not raise
