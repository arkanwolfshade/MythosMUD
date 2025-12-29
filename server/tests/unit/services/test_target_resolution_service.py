"""
Unit tests for target resolution service.

Tests the TargetResolutionService class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.schemas.target_resolution import TargetResolutionResult
from server.services.target_resolution_service import TargetResolutionService


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    return AsyncMock()


@pytest.fixture
def mock_player_service():
    """Create a mock player service."""
    return AsyncMock()


@pytest.fixture
def target_service(mock_persistence, mock_player_service):
    """Create a TargetResolutionService instance."""
    return TargetResolutionService(mock_persistence, mock_player_service)


@pytest.mark.asyncio
async def test_target_resolution_service_init(mock_persistence, mock_player_service):
    """Test TargetResolutionService initialization."""
    service = TargetResolutionService(mock_persistence, mock_player_service)
    assert service.persistence == mock_persistence
    assert service.player_service == mock_player_service


@pytest.mark.asyncio
async def test_resolve_target_persistence_no_methods(mock_player_service):
    """Test resolve_target() when persistence has no get methods."""
    from server.services.target_resolution_service import TargetResolutionService

    mock_persistence = MagicMock()
    # Remove both get_player and get_player_by_id
    if hasattr(mock_persistence, "get_player"):
        delattr(mock_persistence, "get_player")
    if hasattr(mock_persistence, "get_player_by_id"):
        delattr(mock_persistence, "get_player_by_id")
    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "error" in result.error_message.lower() or "not configured" in result.error_message.lower()


@pytest.mark.asyncio
async def test_resolve_target_player_not_found(mock_persistence, mock_player_service):
    """Test resolve_target() when player not found."""
    from server.services.target_resolution_service import TargetResolutionService

    mock_persistence.get_player_by_id = AsyncMock(return_value=None)
    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "not found" in result.error_message.lower() or "error" in result.error_message.lower()


@pytest.mark.asyncio
async def test_resolve_target_player_no_room_id(mock_persistence, mock_player_service):
    """Test resolve_target() when player has no current_room_id."""
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service.resolve_target(uuid.uuid4(), "target")
    assert isinstance(result, TargetResolutionResult)
    assert result.success is False
    assert "not in a room" in result.error_message.lower()


@pytest.mark.asyncio
async def test_search_players_in_room_empty_list(mock_persistence, mock_player_service):
    """Test _search_players_in_room() with empty player list."""
    from server.services.target_resolution_service import TargetResolutionService

    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service._search_players_in_room("room_001", "target", [])
    assert len(result) == 0


@pytest.mark.asyncio
async def test_search_players_in_room_no_match(mock_persistence, mock_player_service):
    """Test _search_players_in_room() with no matching players."""
    from server.services.target_resolution_service import TargetResolutionService

    mock_player1 = MagicMock()
    mock_player1.name = "Alice"
    mock_player1.player_id = uuid.uuid4()
    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service._search_players_in_room("room_001", "Bob", [mock_player1])
    assert len(result) == 0


@pytest.mark.asyncio
async def test_search_npcs_in_room_empty_list(mock_persistence, mock_player_service):
    """Test _search_npcs_in_room() with empty NPC list."""
    from server.services.target_resolution_service import TargetResolutionService

    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service._search_npcs_in_room("room_001", "target", [])
    assert len(result) == 0


@pytest.mark.asyncio
async def test_search_npcs_in_room_no_match(mock_persistence, mock_player_service):
    """Test _search_npcs_in_room() with no matching NPCs."""
    from server.services.target_resolution_service import TargetResolutionService

    mock_npc = MagicMock()
    mock_npc.name = "Goblin"
    mock_npc.npc_id = "npc_001"
    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service._search_npcs_in_room("room_001", "Orc", [mock_npc])
    assert len(result) == 0


@pytest.mark.asyncio
async def test_get_npc_instance_not_found(mock_persistence, mock_player_service):
    """Test _get_npc_instance() when NPC not found."""
    from server.services.target_resolution_service import TargetResolutionService

    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = service._get_npc_instance("nonexistent_npc")
    assert result is None


@pytest.mark.asyncio
async def test_resolve_target_string_player_id(mock_persistence, mock_player_service):
    """Test resolve_target() with string player_id."""
    from server.services.target_resolution_service import TargetResolutionService

    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    service = TargetResolutionService(mock_persistence, mock_player_service)
    result = await service.resolve_target(str(uuid.uuid4()), "target")
    assert isinstance(result, TargetResolutionResult)


@pytest.mark.asyncio
async def test_resolve_target_no_persistence_methods(target_service, mock_persistence):
    """Test resolve_target() when persistence has no get methods."""
    # Remove the methods by deleting the attributes
    if hasattr(mock_persistence, "get_player_by_id"):
        delattr(mock_persistence, "get_player_by_id")
    if hasattr(mock_persistence, "get_player"):
        delattr(mock_persistence, "get_player")
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "error" in result.error_message.lower() or "not configured" in result.error_message.lower()




@pytest.mark.asyncio
async def test_resolve_target_no_room(target_service, mock_persistence):
    """Test resolve_target() when player has no room."""
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    assert result.success is False
    assert "not in a room" in result.error_message.lower() or "room" in result.error_message.lower()


@pytest.mark.asyncio
async def test_resolve_target_empty_target_name(target_service, mock_persistence):
    """Test resolve_target() with empty target name."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await target_service.resolve_target(uuid.uuid4(), "")
    assert result.success is False
    assert "No target specified" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_whitespace_target_name(target_service, mock_persistence):
    """Test resolve_target() with whitespace-only target name."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    result = await target_service.resolve_target(uuid.uuid4(), "   ")
    assert result.success is False
    assert "No target specified" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_uses_get_player_fallback(target_service, mock_persistence):
    """Test resolve_target() uses get_player when get_player_by_id not available."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    # Remove get_player_by_id, add get_player
    if hasattr(mock_persistence, "get_player_by_id"):
        delattr(mock_persistence, "get_player_by_id")
    mock_persistence.get_player = AsyncMock(return_value=mock_player)
    mock_persistence.get_room = MagicMock(return_value=MagicMock())
    mock_persistence.get_players_in_room = MagicMock(return_value=[])
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    # Should proceed to search (may find no matches, but shouldn't error on player lookup)
    assert result.search_term == "target"


@pytest.mark.asyncio
async def test_resolve_target_sync_get_player_by_id(target_service, mock_persistence):
    """Test resolve_target() handles sync get_player_by_id."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    # Use sync method (not AsyncMock)
    mock_persistence.get_player_by_id = MagicMock(return_value=mock_player)
    mock_persistence.get_room = MagicMock(return_value=MagicMock())
    mock_persistence.get_players_in_room = MagicMock(return_value=[])
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    assert result.search_term == "target"




@pytest.mark.asyncio
async def test_resolve_target_no_matches(target_service, mock_persistence):
    """Test resolve_target() when no matches found."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_room = MagicMock()
    mock_room.room_id = "room_001"
    mock_persistence.get_room = MagicMock(return_value=mock_room)
    mock_persistence.get_players_in_room = MagicMock(return_value=[])
    # Mock the _search_npcs_in_room method to return empty list
    target_service._search_npcs_in_room = AsyncMock(return_value=[])
    result = await target_service.resolve_target(uuid.uuid4(), "nonexistent")
    assert result.success is False
    assert "No targets found" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_single_match(target_service, mock_persistence):
    """Test resolve_target() with single match."""

    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_room = MagicMock()
    mock_room.room_id = "room_001"
    mock_persistence.get_room = MagicMock(return_value=mock_room)
    mock_target_player = MagicMock()
    mock_target_player.name = "TargetPlayer"
    mock_target_player.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room = MagicMock(return_value=[mock_target_player])
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    # Should find the player match
    assert result.success is True or len(result.matches) > 0


@pytest.mark.asyncio
async def test_resolve_target_multiple_matches(target_service, mock_persistence):
    """Test resolve_target() with multiple matches requires disambiguation."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_room = MagicMock()
    mock_room.room_id = "room_001"
    mock_persistence.get_room = MagicMock(return_value=mock_room)
    mock_target_player1 = MagicMock()
    mock_target_player1.name = "TargetPlayer1"
    mock_target_player1.player_id = uuid.uuid4()
    mock_target_player2 = MagicMock()
    mock_target_player2.name = "TargetPlayer2"
    mock_target_player2.player_id = uuid.uuid4()
    mock_persistence.get_players_in_room = MagicMock(return_value=[mock_target_player1, mock_target_player2])
    result = await target_service.resolve_target(uuid.uuid4(), "target")
    # Should require disambiguation
    assert result.disambiguation_required is True or "Multiple targets" in result.error_message


@pytest.mark.asyncio
async def test_resolve_target_with_disambiguation_suffix(target_service, mock_persistence):
    """Test resolve_target() with disambiguation suffix."""
    mock_player = MagicMock()
    mock_player.current_room_id = "room_001"
    mock_persistence.get_player_by_id = AsyncMock(return_value=mock_player)
    mock_room = MagicMock()
    mock_room.room_id = "room_001"
    mock_persistence.get_room = MagicMock(return_value=mock_room)
    mock_persistence.get_players_in_room = MagicMock(return_value=[])
    result = await target_service.resolve_target(uuid.uuid4(), "target-1")
    # Should extract suffix and search
    assert result.search_term == "target-1"
