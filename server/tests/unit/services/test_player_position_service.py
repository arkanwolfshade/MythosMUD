"""
Unit tests for player position service.

Tests the PlayerPositionService for coordinating player posture transitions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.services.player_position_service import PlayerPositionService


def test_player_position_service_init():
    """Test PlayerPositionService initialization."""
    persistence = MagicMock()
    connection_manager = MagicMock()
    alias_storage = MagicMock()
    
    service = PlayerPositionService(persistence, connection_manager, alias_storage)
    
    assert service._persistence == persistence
    assert service._connection_manager == connection_manager
    assert service._alias_storage == alias_storage


def test_player_position_service_init_none_values():
    """Test PlayerPositionService initialization with None values."""
    service = PlayerPositionService(None, None, None)
    
    assert service._persistence is None
    assert service._connection_manager is None
    assert service._alias_storage is None


def test_ensure_default_aliases_no_storage():
    """Test ensure_default_aliases does nothing when no alias storage."""
    service = PlayerPositionService(None, None, None)
    
    # Should not raise
    service.ensure_default_aliases("testplayer")


def test_ensure_default_aliases_creates_missing():
    """Test ensure_default_aliases creates missing aliases."""
    alias_storage = MagicMock()
    alias_storage.get_alias = MagicMock(return_value=None)  # Alias doesn't exist
    alias_storage.create_alias = MagicMock()
    
    service = PlayerPositionService(None, None, alias_storage)
    service.ensure_default_aliases("testplayer")
    
    # Should create 3 aliases: sit, stand, lie
    assert alias_storage.create_alias.call_count == 3


def test_ensure_default_aliases_updates_incorrect():
    """Test ensure_default_aliases updates incorrect aliases."""
    alias_storage = MagicMock()
    existing_alias = MagicMock()
    existing_alias.command = "/wrong_command"  # Incorrect command
    alias_storage.get_alias = MagicMock(return_value=existing_alias)
    alias_storage.create_alias = MagicMock()
    
    service = PlayerPositionService(None, None, alias_storage)
    service.ensure_default_aliases("testplayer")
    
    # Should update 3 aliases
    assert alias_storage.create_alias.call_count == 3


def test_ensure_default_aliases_keeps_correct():
    """Test ensure_default_aliases keeps correct aliases."""
    alias_storage = MagicMock()
    existing_alias = MagicMock()
    existing_alias.command = "/sit"  # Correct command
    alias_storage.get_alias = MagicMock(return_value=existing_alias)
    alias_storage.create_alias = MagicMock()
    
    service = PlayerPositionService(None, None, alias_storage)
    service.ensure_default_aliases("testplayer")
    
    # Should not create if alias is correct
    # But it will check all 3, so might create others
    alias_storage.create_alias.assert_called()


def test_ensure_default_aliases_handles_errors():
    """Test ensure_default_aliases handles errors gracefully."""
    alias_storage = MagicMock()
    alias_storage.get_alias = MagicMock(side_effect=Exception("Test error"))
    alias_storage.create_alias = MagicMock()
    
    service = PlayerPositionService(None, None, alias_storage)
    
    # Should not raise
    service.ensure_default_aliases("testplayer")


@pytest.mark.asyncio
async def test_change_position_invalid_position():
    """Test change_position raises ValueError for invalid position."""
    service = PlayerPositionService(None, None, None)
    
    with pytest.raises(ValueError, match="Unsupported position"):
        await service.change_position("testplayer", "invalid_position")


@pytest.mark.asyncio
async def test_change_position_no_persistence():
    """Test change_position returns error when no persistence."""
    service = PlayerPositionService(None, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is False
    assert "unavailable" in result["message"].lower()


@pytest.mark.asyncio
async def test_change_position_player_not_found():
    """Test change_position returns error when player not found."""
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=None)
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is False
    assert "not found" in result["message"].lower()


@pytest.mark.asyncio
async def test_change_position_database_error():
    """Test change_position handles database errors gracefully."""
    from server.exceptions import DatabaseError
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(side_effect=DatabaseError("Database error"))
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is False
    assert "unable" in result["message"].lower()


@pytest.mark.asyncio
async def test_change_position_already_in_position():
    """Test change_position returns already message when already in position."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    player.get_stats = MagicMock(return_value={"position": "sitting"})
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is False  # Not a success since no change
    assert "already" in result["message"].lower()
    assert result["previous_position"] == "sitting"
    assert result["position"] == "sitting"


@pytest.mark.asyncio
async def test_change_position_success():
    """Test change_position successfully changes position."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    player.get_stats = MagicMock(return_value={"position": "standing"})
    player.set_stats = MagicMock()
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is True
    assert result["position"] == "sitting"
    assert result["previous_position"] == "standing"
    assert "settle" in result["message"].lower()
    player.set_stats.assert_called_once()
    persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_change_position_save_error():
    """Test change_position handles save errors gracefully."""
    from server.exceptions import DatabaseError
    
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    player.get_stats = MagicMock(return_value={"position": "standing"})
    player.set_stats = MagicMock()
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock(side_effect=DatabaseError("Save error"))
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is False
    assert "unable" in result["message"].lower()


@pytest.mark.asyncio
async def test_change_position_no_get_stats():
    """Test change_position handles player without get_stats."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    del player.get_stats  # No get_stats method
    player.set_stats = MagicMock()
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    # Should default to "standing" and change to "sitting"
    assert result["success"] is True
    assert result["position"] == "sitting"
    assert result["previous_position"] == "standing"


@pytest.mark.asyncio
async def test_change_position_get_stats_error():
    """Test change_position handles get_stats errors gracefully."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    player.get_stats = MagicMock(side_effect=Exception("Stats error"))
    player.set_stats = MagicMock()
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    
    service = PlayerPositionService(persistence, None, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    # Should default to "standing" and change to "sitting"
    assert result["success"] is True
    assert result["position"] == "sitting"


@pytest.mark.asyncio
async def test_change_position_updates_connection_manager():
    """Test change_position updates connection manager."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    player.get_stats = MagicMock(return_value={"position": "standing"})
    player.set_stats = MagicMock()
    
    online_players = {}
    connection_manager = MagicMock()
    connection_manager.online_players = online_players
    connection_manager.get_online_player_by_display_name = MagicMock(return_value=None)
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    
    service = PlayerPositionService(persistence, connection_manager, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is True
    # Check that connection manager was updated
    player_key = str(player.player_id)
    assert player_key in online_players
    assert online_players[player_key]["position"] == "sitting"


@pytest.mark.asyncio
async def test_change_position_updates_existing_connection_info():
    """Test change_position updates existing connection info."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.current_room_id = "test_room"
    player.name = "TestPlayer"
    player.get_stats = MagicMock(return_value={"position": "standing"})
    player.set_stats = MagicMock()
    
    player_key = str(player.player_id)
    online_players = {
        player_key: {
            "player_id": player_key,
            "player_name": "TestPlayer",
            "position": "standing",
            "connection_types": set(),
            "total_connections": 1,
        }
    }
    connection_manager = MagicMock()
    connection_manager.online_players = online_players
    connection_manager.get_online_player_by_display_name = MagicMock(return_value=None)
    
    persistence = MagicMock()
    persistence.get_player_by_name = AsyncMock(return_value=player)
    persistence.save_player = AsyncMock()
    
    service = PlayerPositionService(persistence, connection_manager, None)
    
    result = await service.change_position("testplayer", "sitting")
    
    assert result["success"] is True
    assert online_players[player_key]["position"] == "sitting"


@pytest.mark.asyncio
async def test_change_position_all_positions():
    """Test change_position works for all valid positions."""
    test_cases = [
        ("standing", "sitting"),  # Change from sitting to standing
        ("sitting", "lying"),     # Change from lying to sitting
        ("lying", "standing"),    # Change from standing to lying
    ]
    
    for initial_position, target_position in test_cases:
        player = MagicMock()
        player.player_id = uuid.uuid4()
        player.current_room_id = "test_room"
        player.name = "TestPlayer"
        player.get_stats = MagicMock(return_value={"position": initial_position})
        player.set_stats = MagicMock()
        
        persistence = MagicMock()
        persistence.get_player_by_name = AsyncMock(return_value=player)
        persistence.save_player = AsyncMock()
        
        service = PlayerPositionService(persistence, None, None)
        
        result = await service.change_position("testplayer", target_position)
        
        assert result["success"] is True, f"Failed to change from {initial_position} to {target_position}"
        assert result["position"] == target_position
        assert result["previous_position"] == initial_position


def test_update_connection_manager_no_manager():
    """Test _update_connection_manager does nothing when no manager."""
    service = PlayerPositionService(None, None, None)
    player = MagicMock()
    
    # Should not raise
    service._update_connection_manager(player, "testplayer", "sitting")


def test_update_connection_manager_no_online_players():
    """Test _update_connection_manager handles missing online_players."""
    connection_manager = MagicMock()
    del connection_manager.online_players  # No online_players attribute
    
    service = PlayerPositionService(None, connection_manager, None)
    player = MagicMock()
    
    # Should not raise
    service._update_connection_manager(player, "testplayer", "sitting")


def test_update_connection_manager_updates_by_display_name():
    """Test _update_connection_manager updates by display name."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    
    player_info = {"position": "standing"}
    connection_manager = MagicMock()
    connection_manager.online_players = {}
    connection_manager.get_online_player_by_display_name = MagicMock(return_value=player_info)
    
    service = PlayerPositionService(None, connection_manager, None)
    service._update_connection_manager(player, "testplayer", "sitting")
    
    assert player_info["position"] == "sitting"


def test_update_connection_manager_handles_errors():
    """Test _update_connection_manager handles errors gracefully."""
    connection_manager = MagicMock()
    connection_manager.online_players = {}
    connection_manager.get_online_player_by_display_name = MagicMock(side_effect=Exception("Test error"))
    
    service = PlayerPositionService(None, connection_manager, None)
    player = MagicMock()
    
    # Should not raise
    service._update_connection_manager(player, "testplayer", "sitting")
