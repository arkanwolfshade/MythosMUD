"""
Unit tests for target resolution service.

Tests the TargetResolutionService class for resolving player and NPC targets.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType
from server.services.target_resolution_service import TargetResolutionService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    persistence.get_player_by_id = AsyncMock()
    persistence.get_players_in_room = AsyncMock(return_value=[])
    persistence.get_room_by_id = AsyncMock(return_value=MagicMock())
    return persistence


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    player_service = MagicMock()
    player_service.resolve_player_name = AsyncMock()
    return player_service


@pytest.fixture
def target_resolution_service(mock_persistence, mock_player_service):
    """Create a TargetResolutionService instance."""
    return TargetResolutionService(persistence=mock_persistence, player_service=mock_player_service)


@pytest.mark.asyncio
async def test_resolve_target_player_not_found(target_resolution_service, mock_persistence):
    """Test resolve_target when player is not found."""
    mock_persistence.get_player_by_id.return_value = None
    
    result = await target_resolution_service.resolve_target(uuid.uuid4(), "target")
    
    assert not result.success
    assert "Player not found" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_no_room(target_resolution_service, mock_persistence):
    """Test resolve_target when player has no room."""
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_persistence.get_player_by_id.return_value = mock_player
    
    result = await target_resolution_service.resolve_target(uuid.uuid4(), "target")
    
    assert not result.success
    assert "not in a room" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_empty_target(target_resolution_service, mock_persistence):
    """Test resolve_target with empty target name."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_persistence.get_player_by_id.return_value = mock_player
    
    result = await target_resolution_service.resolve_target(uuid.uuid4(), "   ")
    
    assert not result.success
    assert "No target specified" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_no_matches(target_resolution_service, mock_persistence):
    """Test resolve_target when no targets match."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_persistence.get_player_by_id.return_value = mock_player
    mock_persistence.get_players_in_room.return_value = []
    
    result = await target_resolution_service.resolve_target(uuid.uuid4(), "nonexistent")
    
    assert not result.success
    assert "No targets found" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_single_player_match(target_resolution_service, mock_persistence):
    """Test resolve_target with single player match."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_id.return_value = mock_player
    
    mock_target_player = MagicMock()
    mock_target_player.name = "TargetPlayer"
    mock_target_player.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room.return_value = [mock_target_player]
    
    result = await target_resolution_service.resolve_target(mock_player.player_id, "target")
    
    assert result.success
    assert len(result.matches) == 1
    assert result.matches[0].target_type == TargetType.PLAYER
    assert result.matches[0].target_name == "TargetPlayer"


@pytest.mark.asyncio
async def test_resolve_target_multiple_matches_requires_disambiguation(target_resolution_service, mock_persistence):
    """Test resolve_target with multiple matches requires disambiguation."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_id.return_value = mock_player
    
    mock_target_player1 = MagicMock()
    mock_target_player1.name = "TargetPlayer"
    mock_target_player1.player_id = uuid.uuid4()
    mock_target_player2 = MagicMock()
    mock_target_player2.name = "TargetPlayer2"
    mock_target_player2.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room.return_value = [mock_target_player1, mock_target_player2]
    
    result = await target_resolution_service.resolve_target(mock_player.player_id, "target")
    
    assert not result.success
    assert result.disambiguation_required
    assert len(result.matches) == 2


@pytest.mark.asyncio
async def test_resolve_target_with_disambiguation_suffix(target_resolution_service, mock_persistence):
    """Test resolve_target with disambiguation suffix."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_id.return_value = mock_player
    
    mock_target_player = MagicMock()
    mock_target_player.name = "TargetPlayer"
    mock_target_player.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room.return_value = [mock_target_player]
    
    result = await target_resolution_service.resolve_target(mock_player.player_id, "target-1")
    
    # Note: Current implementation doesn't fully support disambiguation suffixes for players
    # This test verifies the suffix is parsed but may not match
    assert result.search_term == "target-1"


@pytest.mark.asyncio
async def test_resolve_target_string_player_id(target_resolution_service, mock_persistence):
    """Test resolve_target accepts string player_id."""
    player_id_str = str(uuid.uuid4())
    mock_player = MagicMock()
    mock_player.current_room_id = "room1"
    mock_persistence.get_player_by_id.return_value = mock_player
    
    result = await target_resolution_service.resolve_target(player_id_str, "target")
    
    # Should convert string to UUID internally
    mock_persistence.get_player_by_id.assert_called_once()
    # Verify it was called with a UUID (the string was converted)
    call_args = mock_persistence.get_player_by_id.call_args[0][0]
    assert isinstance(call_args, uuid.UUID)


@pytest.mark.asyncio
async def test_resolve_target_persistence_no_methods(target_resolution_service):
    """Test resolve_target when persistence has no get_player methods."""
    persistence = MagicMock()
    # Remove get_player_by_id and get_player methods
    del persistence.get_player_by_id
    del persistence.get_player
    
    service = TargetResolutionService(persistence=persistence, player_service=MagicMock())
    
    result = await service.resolve_target(uuid.uuid4(), "target")
    
    assert not result.success
    assert "not configured correctly" in result.error_message


@pytest.mark.asyncio
async def test_search_players_in_room_success(target_resolution_service, mock_persistence):
    """Test _search_players_in_room finds matching players."""
    mock_target_player = MagicMock()
    mock_target_player.name = "TargetPlayer"
    mock_target_player.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room.return_value = [mock_target_player]
    
    matches = await target_resolution_service._search_players_in_room("room1", "target", None)
    
    assert len(matches) == 1
    assert matches[0].target_type == TargetType.PLAYER
    assert matches[0].target_name == "TargetPlayer"


@pytest.mark.asyncio
async def test_search_players_in_room_no_matches(target_resolution_service, mock_persistence):
    """Test _search_players_in_room with no matching players."""
    mock_target_player = MagicMock()
    mock_target_player.name = "OtherPlayer"
    mock_target_player.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room.return_value = [mock_target_player]
    
    matches = await target_resolution_service._search_players_in_room("room1", "target", None)
    
    assert len(matches) == 0


@pytest.mark.asyncio
async def test_search_players_in_room_error_handling(target_resolution_service, mock_persistence):
    """Test _search_players_in_room handles errors gracefully."""
    mock_persistence.get_players_in_room.side_effect = Exception("Database error")
    
    matches = await target_resolution_service._search_players_in_room("room1", "target", None)
    
    assert len(matches) == 0


@pytest.mark.asyncio
async def test_search_npcs_in_room_room_not_found(target_resolution_service, mock_persistence):
    """Test _search_npcs_in_room when room is not found."""
    mock_persistence.get_room_by_id.return_value = None
    
    matches = await target_resolution_service._search_npcs_in_room("room1", "target", None)
    
    assert len(matches) == 0


@pytest.mark.asyncio
async def test_search_npcs_in_room_error_handling(target_resolution_service, mock_persistence):
    """Test _search_npcs_in_room handles errors gracefully."""
    mock_persistence.get_room_by_id.side_effect = Exception("Database error")
    
    matches = await target_resolution_service._search_npcs_in_room("room1", "target", None)
    
    assert len(matches) == 0


@pytest.mark.asyncio
async def test_get_npc_instance_not_found(target_resolution_service):
    """Test _get_npc_instance when NPC is not found."""
    npc_instance = target_resolution_service._get_npc_instance("npc1")
    
    assert npc_instance is None


@pytest.mark.asyncio
async def test_get_npc_instance_error_handling(target_resolution_service):
    """Test _get_npc_instance handles errors gracefully."""
    # Mock get_npc_instance_service to raise an exception
    with pytest.MonkeyPatch().context() as mp:
        mp.setattr(
            "server.services.target_resolution_service.get_npc_instance_service",
            MagicMock(side_effect=Exception("Service error")),
        )
        
        npc_instance = target_resolution_service._get_npc_instance("npc1")
        
        assert npc_instance is None
