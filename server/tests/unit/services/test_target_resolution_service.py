"""
Tests for target resolution service.
"""

import uuid
from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4

import pytest

from server.schemas.target_resolution import TargetType
from server.services.target_resolution_service import TargetResolutionService


class TestTargetResolutionService:
    """Test target resolution service functionality."""

    @pytest.fixture
    def mock_persistence(self):
        """Create a mock persistence layer."""
        return Mock()

    @pytest.fixture
    def mock_player_service(self):
        """Create a mock player service."""
        return Mock()

    @pytest.fixture
    def target_resolution_service(self, mock_persistence, mock_player_service):
        """Create a target resolution service instance."""
        return TargetResolutionService(mock_persistence, mock_player_service)

    @pytest.mark.asyncio
    async def test_resolve_target_player_not_found(self, target_resolution_service, mock_persistence):
        """Test target resolution when player is not found."""
        player_id = str(uuid4())
        target_name = "test_target"

        # Mock player not found - service checks get_player_by_id first, then get_player
        mock_persistence.get_player_by_id = Mock(return_value=None)
        mock_persistence.get_player = Mock(return_value=None)

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is False
        assert "Player not found" in result.error_message
        # Service converts string to UUID before calling get_player_by_id
        mock_persistence.get_player_by_id.assert_called_once_with(uuid.UUID(player_id))

    @pytest.mark.asyncio
    async def test_resolve_target_no_current_room(self, target_resolution_service, mock_persistence):
        """Test target resolution when player has no current room."""
        player_id = str(uuid4())
        target_name = "test_target"

        # Mock player without current room - service checks get_player_by_id first
        mock_player = Mock()
        mock_player.current_room_id = None
        mock_persistence.get_player_by_id = Mock(return_value=mock_player)
        mock_persistence.get_player = Mock(return_value=mock_player)

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is False
        assert "not in a room" in result.error_message

    @pytest.mark.asyncio
    async def test_resolve_target_empty_target_name(self, target_resolution_service, mock_persistence):
        """Test target resolution with empty target name."""
        player_id = str(uuid4())
        target_name = ""

        # Mock player and room - service checks get_player_by_id first
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_id = Mock(return_value=mock_player)
        mock_persistence.get_player = Mock(return_value=mock_player)
        # No player matches by name in this test
        mock_persistence.get_players_in_room.return_value = []

        mock_room = Mock()
        mock_room.room_id = "room_001"
        mock_persistence.get_room.return_value = mock_room

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is False
        assert "No target specified" in result.error_message

    @pytest.mark.asyncio
    async def test_resolve_target_player_match(self, target_resolution_service, mock_persistence):
        """Test target resolution finding a player match."""
        player_id = str(uuid4())
        target_name = "TestPlayer"

        # Mock player and room - service checks get_player_by_id first
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_id = Mock(return_value=mock_player)
        mock_persistence.get_player = Mock(return_value=mock_player)

        # Mock player service to return matching player
        mock_target_player = Mock()
        mock_target_player.player_id = "player_1"
        mock_target_player.name = "TestPlayer"
        mock_target_player.current_room_id = "room_001"

        # Mock the get_players_in_room method to return the matching player
        mock_persistence.get_players_in_room.return_value = [mock_target_player]

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is True
        assert len(result.matches) == 1
        assert result.matches[0].target_type == TargetType.PLAYER
        assert result.matches[0].target_name == "TestPlayer"

    @pytest.mark.asyncio
    async def test_resolve_target_npc_match(self, target_resolution_service, mock_persistence):
        """Test target resolution finding an NPC match."""
        player_id = str(uuid4())
        target_name = "rat"

        # Mock player and room - service checks get_player_by_id first
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_id = Mock(return_value=mock_player)
        mock_persistence.get_player = Mock(return_value=mock_player)
        # No player matches by name in this test
        mock_persistence.get_players_in_room.return_value = []

        mock_room = Mock()
        mock_room.room_id = "room_001"
        mock_room.get_npcs.return_value = ["npc_1"]
        # TargetResolutionService prefers get_room_by_id when available
        mock_persistence.get_room_by_id = Mock(return_value=mock_room)
        mock_persistence.get_room = AsyncMock(return_value=mock_room)

        # Mock NPC instance
        mock_npc = Mock()
        mock_npc.name = "rat"
        mock_npc.is_alive = True
        # NPC should be in the same room as the player
        mock_npc.current_room_id = "room_001"

        # Simplify by mocking _get_npc_instance to return our NPC for any ID
        target_resolution_service._get_npc_instance = AsyncMock(return_value=mock_npc)

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is True
        assert len(result.matches) == 1
        assert result.matches[0].target_type == TargetType.NPC
        assert result.matches[0].target_name == "rat"

    @pytest.mark.asyncio
    async def test_resolve_target_no_matches(self, target_resolution_service, mock_persistence):
        """Test target resolution when no matches are found."""
        player_id = str(uuid4())
        target_name = "nonexistent"

        # Mock player and room - service checks get_player_by_id first
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_id = Mock(return_value=mock_player)
        mock_persistence.get_player = Mock(return_value=mock_player)

        # Mock no players in room
        mock_persistence.get_players_in_room.return_value = []

        # Mock room with no NPCs
        mock_room = Mock()
        mock_room.room_id = "room_001"
        mock_room.get_npcs.return_value = []
        mock_persistence.get_room.return_value = mock_room

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is False
        assert len(result.matches) == 0
        assert "No targets found" in result.error_message

    @pytest.mark.asyncio
    async def test_resolve_target_multiple_matches(self, target_resolution_service, mock_persistence):
        """Test target resolution with multiple matches requiring disambiguation."""
        player_id = str(uuid4())
        target_name = "test"

        # Mock player and room - service checks get_player_by_id first
        mock_player = Mock()
        mock_player.current_room_id = "room_001"
        mock_persistence.get_player_by_id = Mock(return_value=mock_player)
        mock_persistence.get_player = Mock(return_value=mock_player)

        # Mock multiple matching players
        mock_player1 = Mock()
        mock_player1.player_id = "player_1"
        mock_player1.name = "TestPlayer1"
        mock_player1.current_room_id = "room_001"

        mock_player2 = Mock()
        mock_player2.player_id = "player_2"
        mock_player2.name = "TestPlayer2"
        mock_player2.current_room_id = "room_001"

        # Mock the get_players_in_room method to return multiple matching players
        mock_persistence.get_players_in_room.return_value = [mock_player1, mock_player2]

        # Mock room for NPC search
        mock_room = Mock()
        mock_room.room_id = "room_001"
        mock_room.get_npcs.return_value = ["npc_1"]
        mock_persistence.get_room.return_value = mock_room

        # Mock NPC instance
        mock_npc = Mock()
        mock_npc.name = "TestNPC"
        mock_npc.is_alive = True

        target_resolution_service._get_npc_instance = AsyncMock(return_value=mock_npc)

        result = await target_resolution_service.resolve_target(player_id, target_name)

        assert result.success is False
        assert len(result.matches) > 1
        assert "Multiple targets match" in result.error_message

    def test_get_npc_instance_found(self, target_resolution_service, mock_persistence):
        """Test getting an NPC instance when found."""
        npc_id = str(uuid4())
        mock_npc = Mock()
        mock_npc.name = "TestNPC"

        # Mock the NPC instance service with lifecycle manager
        with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
            mock_service = Mock()
            mock_lifecycle_manager = Mock()
            mock_lifecycle_manager.active_npcs = {npc_id: mock_npc}
            mock_service.lifecycle_manager = mock_lifecycle_manager
            mock_get_service.return_value = mock_service

            result = target_resolution_service._get_npc_instance(npc_id)

            assert result == mock_npc

    def test_get_npc_instance_not_found(self, target_resolution_service, mock_persistence):
        """Test getting an NPC instance when not found."""
        npc_id = str(uuid4())

        # Mock the NPC instance service with no NPCs
        with patch("server.services.npc_instance_service.get_npc_instance_service") as mock_get_service:
            mock_service = Mock()
            mock_spawning_service = Mock()
            mock_spawning_service.active_npc_instances = {}
            mock_service.spawning_service = mock_spawning_service
            mock_get_service.return_value = mock_service

            result = target_resolution_service._get_npc_instance(npc_id)

            assert result is None
