"""
Unit tests for read command handlers.

Tests the read command functionality.
"""

import json
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.read_command import handle_read_command


@pytest.mark.asyncio
async def test_handle_read_command():
    """Test handle_read_command() reads item."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"target": "book"}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_read_command_no_target():
    """Test handle_read_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_no_persistence():
    """Test handle_read_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_read_command({"target": "book"}, {}, mock_request, None, "TestPlayer")

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_no_spell_learning_service():
    """Test handle_read_command() when spell learning service is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not initialized" in result["result"].lower() or "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_player_not_found():
    """Test handle_read_command() when player is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not recognized" in result["result"].lower() or "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_item_not_found():
    """Test handle_read_command() when item is not found."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = json.dumps([{"name": "sword"}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_not_spellbook():
    """Test handle_read_command() when item is not a spellbook."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = json.dumps([{"name": "book", "metadata": {}}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "not a spellbook" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_empty_spellbook():
    """Test handle_read_command() when spellbook is empty."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = json.dumps([{"name": "book", "metadata": {"spellbook": True, "spells": []}}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "empty" in result["result"].lower() or "corrupted" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_multiple_spells():
    """Test handle_read_command() when spellbook has multiple spells."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = json.dumps(
        [{"name": "book", "metadata": {"spellbook": True, "spells": ["spell1", "spell2"]}}]
    )
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_spell_registry = MagicMock()
    mock_spell1 = MagicMock()
    mock_spell1.name = "Fireball"
    mock_spell2 = MagicMock()
    mock_spell2.name = "Icebolt"
    mock_spell_registry.get_spell = MagicMock(side_effect=[mock_spell1, mock_spell2])
    mock_state.spell_registry = mock_spell_registry
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "contains the following spells" in result["result"].lower() or "Fireball" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_single_spell_learn():
    """Test handle_read_command() learns single spell from spellbook."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = "player_001"
    mock_player.inventory = json.dumps([{"name": "book", "id": "book_001", "metadata": {"spellbook": True, "spells": ["spell1"]}}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_spell_learning_service = AsyncMock()
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Fireball!", "corruption_applied": 0}
    )
    mock_state.spell_learning_service = mock_spell_learning_service
    mock_spell_registry = MagicMock()
    mock_spell = MagicMock()
    mock_spell.name = "Fireball"
    mock_spell_registry.get_spell = MagicMock(return_value=mock_spell)
    mock_state.spell_registry = mock_spell_registry
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "learned" in result["result"].lower() or "Learned" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_specific_spell():
    """Test handle_read_command() learns specific spell from spellbook."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = "player_001"
    mock_player.inventory = json.dumps(
        [{"name": "book", "id": "book_001", "metadata": {"spellbook": True, "spells": ["spell1", "spell2"]}}]
    )
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_spell_learning_service = AsyncMock()
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Fireball!", "corruption_applied": 0}
    )
    mock_state.spell_learning_service = mock_spell_learning_service
    mock_spell_registry = MagicMock()
    mock_spell = MagicMock()
    mock_spell.name = "Fireball"
    mock_spell.spell_id = "spell1"
    mock_spell_registry.get_spell_by_name = MagicMock(return_value=mock_spell)
    mock_state.spell_registry = mock_spell_registry
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command(
        {"args": ["book", "Fireball"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "learned" in result["result"].lower() or "Learned" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_spell_not_in_book():
    """Test handle_read_command() when specified spell is not in book."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = json.dumps(
        [{"name": "book", "metadata": {"spellbook": True, "spells": ["spell1"]}}]
    )
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_spell_registry = MagicMock()
    mock_spell = MagicMock()
    mock_spell.name = "Fireball"
    mock_spell.spell_id = "spell2"  # Different from spell1 in book
    mock_spell_registry.get_spell_by_name = MagicMock(return_value=mock_spell)
    mock_state.spell_registry = mock_spell_registry
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command(
        {"args": ["book", "Fireball"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not in this spellbook" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_spell_registry_not_available():
    """Test handle_read_command() when spell registry is not available."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = json.dumps(
        [{"name": "book", "metadata": {"spellbook": True, "spells": ["spell1"]}}]
    )
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_state.spell_registry = None
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command(
        {"args": ["book", "Fireball"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "result" in result
    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_learn_failure():
    """Test handle_read_command() when spell learning fails."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.player_id = "player_001"
    mock_player.inventory = json.dumps([{"name": "book", "id": "book_001", "metadata": {"spellbook": True, "spells": ["spell1"]}}])
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_spell_learning_service = AsyncMock()
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": False, "message": "Already know this spell"}
    )
    mock_state.spell_learning_service = mock_spell_learning_service
    mock_spell_registry = MagicMock()
    mock_spell = MagicMock()
    mock_spell.name = "Fireball"
    mock_spell_registry.get_spell = MagicMock(return_value=mock_spell)
    mock_state.spell_registry = mock_spell_registry
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "already know" in result["result"].lower() or "failed" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_read_command_inventory_json_error():
    """Test handle_read_command() handles JSON parsing errors."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.inventory = "invalid json"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.spell_learning_service = AsyncMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_read_command({"args": ["book"]}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "error" in result["result"].lower() or "occurred" in result["result"].lower()
