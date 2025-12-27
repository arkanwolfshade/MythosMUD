"""
Unit tests for teach command handler.

Tests the /teach command for learning spells from NPCs.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.teach_command import handle_teach_command
from server.schemas.target_resolution import TargetMatch, TargetResolutionResult, TargetType


@pytest.mark.asyncio
async def test_handle_teach_command_no_app():
    """Test handle_teach_command when app is not available."""
    result = await handle_teach_command(
        command_data={},
        current_user={},
        request=None,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "System error: application not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_no_persistence():
    """Test handle_teach_command when persistence is not available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.persistence = None
    
    result = await handle_teach_command(
        command_data={},
        current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "System error: required services not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_no_player_service():
    """Test handle_teach_command when player_service is not available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.persistence = MagicMock()
    mock_request.app.state.player_service = None
    
    result = await handle_teach_command(
        command_data={},
        current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "System error: required services not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_no_spell_learning_service():
    """Test handle_teach_command when spell_learning_service is not available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.persistence = MagicMock()
    mock_request.app.state.player_service = MagicMock()
    mock_request.app.state.spell_learning_service = None
    
    result = await handle_teach_command(
        command_data={},
        current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "Spell learning system not initialized" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_player_not_found():
    """Test handle_teach_command when player is not found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_request.app.state.spell_learning_service = MagicMock()
    
    result = await handle_teach_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_insufficient_args():
    """Test handle_teach_command with insufficient arguments."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_request.app.state.spell_learning_service = MagicMock()
    
    result = await handle_teach_command(
        command_data={"args": ["npc_name"]},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "Usage: /teach <npc_name> <spell_name>" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_target_resolution_fails():
    """Test handle_teach_command when target resolution fails."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_request.app.state.spell_learning_service = MagicMock()
    
    with patch("server.commands.teach_command.TargetResolutionService") as mock_service_class:
        mock_service = MagicMock()
        mock_service_class.return_value = mock_service
        mock_target_result = TargetResolutionResult(
            success=False,
            error_message="NPC not found",
            search_term="npc_name",
            room_id="test_room"
        )
        mock_service.resolve_target = AsyncMock(return_value=mock_target_result)
        
        result = await handle_teach_command(
            command_data={"args": ["npc_name", "spell_name"]},
            current_user={"username": "TestPlayer"},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "NPC not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_no_target_match():
    """Test handle_teach_command when no target match is found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_request.app.state.spell_learning_service = MagicMock()
    
    with patch("server.commands.teach_command.TargetResolutionService") as mock_service_class:
        mock_service = MagicMock()
        mock_service_class.return_value = mock_service
        mock_target_result = TargetResolutionResult(
            success=True,
            error_message=None,
            matches=[],
            search_term="npc_name",
            room_id="test_room"
        )
        mock_service.resolve_target = AsyncMock(return_value=mock_target_result)
        
        result = await handle_teach_command(
            command_data={"args": ["npc_name", "spell_name"]},
            current_user={"username": "TestPlayer"},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "No valid target found" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_target_not_npc():
    """Test handle_teach_command when target is not an NPC."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_request.app.state.spell_learning_service = MagicMock()
    
    with patch("server.commands.teach_command.TargetResolutionService") as mock_service_class:
        mock_service = MagicMock()
        mock_service_class.return_value = mock_service
        mock_target_match = TargetMatch(
            target_id=str(uuid.uuid4()),
            target_name="player_name",
            target_type=TargetType.PLAYER,
            room_id="test_room"
        )
        mock_target_result = TargetResolutionResult(
            success=True,
            error_message=None,
            matches=[mock_target_match],
            search_term="player_name",
            room_id="test_room"
        )
        mock_service.resolve_target = AsyncMock(return_value=mock_target_result)
        
        result = await handle_teach_command(
            command_data={"args": ["player_name", "spell_name"]},
            current_user={"username": "TestPlayer"},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "is not an NPC" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_spell_learning_fails():
    """Test handle_teach_command when spell learning fails."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_spell_learning_service = AsyncMock()
    mock_spell_learning_service.learn_spell_from_npc = AsyncMock(return_value={"success": False, "message": "Spell not found"})
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    
    with patch("server.commands.teach_command.TargetResolutionService") as mock_service_class:
        mock_service = MagicMock()
        mock_service_class.return_value = mock_service
        mock_target_match = TargetMatch(
            target_id=str(uuid.uuid4()),
            target_name="npc_name",
            target_type=TargetType.NPC,
            room_id="test_room"
        )
        mock_target_result = TargetResolutionResult(
            success=True,
            error_message=None,
            matches=[mock_target_match],
            search_term="npc_name",
            room_id="test_room"
        )
        mock_service.resolve_target = AsyncMock(return_value=mock_target_result)
        
        result = await handle_teach_command(
            command_data={"args": ["npc_name", "spell_name"]},
            current_user={"username": "TestPlayer"},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "Spell not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_success():
    """Test handle_teach_command successful spell learning."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_spell_learning_service = AsyncMock()
    mock_spell_learning_service.learn_spell_from_npc = AsyncMock(return_value={
        "success": True,
        "message": "Learned Fireball!",
        "corruption_applied": 0
    })
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    
    with patch("server.commands.teach_command.TargetResolutionService") as mock_service_class:
        mock_service = MagicMock()
        mock_service_class.return_value = mock_service
        mock_target_match = TargetMatch(
            target_id=str(uuid.uuid4()),
            target_name="npc_name",
            target_type=TargetType.NPC,
            room_id="test_room"
        )
        mock_target_result = TargetResolutionResult(
            success=True,
            error_message=None,
            matches=[mock_target_match],
            search_term="npc_name",
            room_id="test_room"
        )
        mock_service.resolve_target = AsyncMock(return_value=mock_target_result)
        
        result = await handle_teach_command(
            command_data={"args": ["npc_name", "Fireball"]},
            current_user={"username": "TestPlayer"},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "Learned Fireball!" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_success_with_corruption():
    """Test handle_teach_command successful spell learning with corruption."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = uuid.uuid4()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.player_service = MagicMock()
    mock_spell_learning_service = AsyncMock()
    mock_spell_learning_service.learn_spell_from_npc = AsyncMock(return_value={
        "success": True,
        "message": "Learned Dark Spell!",
        "corruption_applied": 5
    })
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    
    with patch("server.commands.teach_command.TargetResolutionService") as mock_service_class:
        mock_service = MagicMock()
        mock_service_class.return_value = mock_service
        mock_target_match = TargetMatch(
            target_id=str(uuid.uuid4()),
            target_name="npc_name",
            target_type=TargetType.NPC,
            room_id="test_room"
        )
        mock_target_result = TargetResolutionResult(
            success=True,
            error_message=None,
            matches=[mock_target_match],
            search_term="npc_name",
            room_id="test_room"
        )
        mock_service.resolve_target = AsyncMock(return_value=mock_target_result)
        
        result = await handle_teach_command(
            command_data={"args": ["npc_name", "Dark Spell"]},
            current_user={"username": "TestPlayer"},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "Learned Dark Spell!" in result["result"]
        assert "tainted your mind" in result["result"]
        assert "+5 corruption" in result["result"]
