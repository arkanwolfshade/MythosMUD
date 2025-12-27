"""
Unit tests for read command handler.

Tests the /read command for reading spellbooks.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.read_command import handle_read_command


@pytest.mark.asyncio
async def test_handle_read_command_no_app():
    """Test handle_read_command returns error when no app."""
    mock_request = MagicMock()
    mock_request.app = None
    
    result = await handle_read_command({}, {}, mock_request, None, "testplayer")
    
    assert "application not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_no_persistence():
    """Test handle_read_command returns error when no persistence."""
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    del mock_app.state.persistence
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_read_command({}, {}, mock_request, None, "testplayer")
    
    assert "persistence layer not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_no_spell_service():
    """Test handle_read_command returns error when no spell learning service."""
    mock_persistence = MagicMock()
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    del mock_app.state.spell_learning_service
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_read_command({}, {}, mock_request, None, "testplayer")
    
    assert "not initialized" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_player_not_found():
    """Test handle_read_command returns error when player not found."""
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_read_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "not recognized" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_no_args():
    """Test handle_read_command returns usage when no args."""
    mock_player = MagicMock()
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    result = await handle_read_command({}, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "Usage:" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_item_not_found():
    """Test handle_read_command returns error when item not found."""
    mock_player = MagicMock()
    mock_player.inventory = json.dumps([])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["nonexistent_book"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_item_not_spellbook():
    """Test handle_read_command returns error when item is not a spellbook."""
    mock_player = MagicMock()
    mock_player.inventory = json.dumps([
        {"name": "sword", "metadata": {}}
    ])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["sword"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "not a spellbook" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_empty_spellbook():
    """Test handle_read_command returns error when spellbook is empty."""
    mock_player = MagicMock()
    mock_player.inventory = json.dumps([
        {"name": "spellbook", "metadata": {"spellbook": True, "spells": []}}
    ])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["spellbook"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "empty or corrupted" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_single_spell_no_name():
    """Test handle_read_command learns spell when only one spell in book and no name specified."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    # spells_in_book should be a list of spell IDs (integers)
    mock_player.inventory = json.dumps([
        {"name": "spellbook", "id": "book1", "metadata": {"spellbook": True, "spells": [1]}}
    ])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_service = MagicMock()
    mock_spell_service.learn_spell = AsyncMock(return_value={"success": True, "message": "You learn Fireball."})
    mock_spell = MagicMock()
    mock_spell.name = "Fireball"
    mock_spell_registry = MagicMock()
    mock_spell_registry.get_spell = MagicMock(return_value=mock_spell)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = mock_spell_service
    mock_app.state.spell_registry = mock_spell_registry
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["spellbook"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "learn" in result["result"].lower() or "fireball" in result["result"].lower()
    mock_spell_service.learn_spell.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_read_command_multiple_spells_no_name():
    """Test handle_read_command lists spells when multiple spells and no name specified."""
    mock_player = MagicMock()
    # spells_in_book should be a list of spell IDs (integers)
    mock_player.inventory = json.dumps([
        {"name": "spellbook", "metadata": {"spellbook": True, "spells": [1, 2]}}
    ])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell1 = MagicMock()
    mock_spell1.name = "Fireball"
    mock_spell2 = MagicMock()
    mock_spell2.name = "Icebolt"
    mock_spell_registry = MagicMock()
    mock_spell_registry.get_spell = MagicMock(side_effect=lambda sid: mock_spell1 if sid == 1 else (mock_spell2 if sid == 2 else None))
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_app.state.spell_registry = mock_spell_registry
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["spellbook"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    # Should list available spells
    assert "fireball" in result["result"].lower() or "icebolt" in result["result"].lower() or "spells" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_with_spell_name():
    """Test handle_read_command learns specific spell when name is provided."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    # spells_in_book should be a list of spell IDs (integers), not dicts
    mock_player.inventory = json.dumps([
        {"name": "spellbook", "id": "book1", "metadata": {"spellbook": True, "spells": [1, 2]}}
    ])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_service = MagicMock()
    mock_spell_service.learn_spell = AsyncMock(return_value={"success": True, "message": "You learn Fireball."})
    mock_spell = MagicMock()
    mock_spell.spell_id = 1
    mock_spell.name = "Fireball"
    mock_spell_registry = MagicMock()
    mock_spell_registry.get_spell_by_name = MagicMock(return_value=mock_spell)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = mock_spell_service
    mock_app.state.spell_registry = mock_spell_registry
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["spellbook", "Fireball"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "learn" in result["result"].lower() or "fireball" in result["result"].lower()
    mock_spell_service.learn_spell.assert_awaited_once()
    mock_spell_registry.get_spell_by_name.assert_called_once_with("Fireball")


@pytest.mark.asyncio
async def test_handle_read_command_spell_not_found():
    """Test handle_read_command returns error when specified spell not found."""
    mock_player = MagicMock()
    # spells_in_book should be a list of spell IDs (integers)
    mock_player.inventory = json.dumps([
        {"name": "spellbook", "metadata": {"spellbook": True, "spells": [1]}}
    ])
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_registry = MagicMock()
    mock_spell_registry.get_spell_by_name = MagicMock(return_value=None)  # Spell not found
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = MagicMock()
    mock_app.state.spell_registry = mock_spell_registry
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["spellbook", "NonexistentSpell"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_inventory_as_dict():
    """Test handle_read_command handles inventory as dict (not JSON string)."""
    mock_player = MagicMock()
    mock_player.player_id = "test-player-id"
    # spells_in_book should be a list of spell IDs (integers)
    mock_player.inventory = [{"name": "spellbook", "id": "book1", "metadata": {"spellbook": True, "spells": [1]}}]
    mock_persistence = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_service = MagicMock()
    mock_spell_service.learn_spell = AsyncMock(return_value={"success": True, "message": "You learn Fireball."})
    mock_spell = MagicMock()
    mock_spell.name = "Fireball"
    mock_spell_registry = MagicMock()
    mock_spell_registry.get_spell = MagicMock(return_value=mock_spell)
    mock_app = MagicMock()
    mock_app.state = MagicMock()
    mock_app.state.persistence = mock_persistence
    mock_app.state.spell_learning_service = mock_spell_service
    mock_app.state.spell_registry = mock_spell_registry
    mock_request = MagicMock()
    mock_request.app = mock_app
    
    command_data = {"args": ["spellbook"]}
    result = await handle_read_command(command_data, {"username": "testuser"}, mock_request, None, "testplayer")
    
    assert "learn" in result["result"].lower() or "fireball" in result["result"].lower()
