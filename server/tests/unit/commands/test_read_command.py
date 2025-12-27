"""
Unit tests for read command.

Tests the /read command for reading spellbooks.
"""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.read_command import handle_read_command


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    app.state = MagicMock()
    request = MagicMock()
    request.app = app
    return request


@pytest.fixture
def mock_persistence():
    """Create a mock persistence layer."""
    persistence = MagicMock()
    return persistence


@pytest.fixture
def mock_spell_learning_service():
    """Create a mock spell learning service."""
    service = MagicMock()
    service.learn_spell = AsyncMock()
    return service


@pytest.fixture
def mock_spell_registry():
    """Create a mock spell registry."""
    registry = MagicMock()
    spell = MagicMock()
    spell.spell_id = "spell_001"
    spell.name = "Test Spell"
    registry.get_spell_by_name.return_value = spell
    registry.get_spell.return_value = spell
    return registry


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = "player_001"
    player.inventory = json.dumps(
        [
            {
                "id": "spellbook_001",
                "name": "Ancient Tome",
                "metadata": {
                    "spellbook": True,
                    "spells": ["spell_001"],
                },
            }
        ]
    )
    return player


@pytest.mark.asyncio
async def test_handle_read_command_no_app(mock_request):
    """Test read command when app is not available."""
    mock_request.app = None
    result = await handle_read_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "System error: application not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_no_persistence(mock_request):
    """Test read command when persistence is not available."""
    mock_request.app.state.persistence = None
    result = await handle_read_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "System error: persistence layer not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_no_spell_learning_service(mock_request, mock_persistence):
    """Test read command when spell learning service is not available."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = None
    result = await handle_read_command({}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "Spell learning system not initialized" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_no_args(mock_request, mock_persistence, mock_spell_learning_service):
    """Test read command with no arguments."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_persistence.get_player_by_name = AsyncMock(return_value=MagicMock())
    result = await handle_read_command({"args": []}, {"username": "testuser"}, mock_request, None, "TestPlayer")
    assert "Usage: /read <item_name> [spell_name]" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_player_not_found(mock_request, mock_persistence, mock_spell_learning_service):
    """Test read command when player is not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handle_read_command(
        {"args": ["Ancient Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_item_not_found(mock_request, mock_persistence, mock_spell_learning_service, mock_player):
    """Test read command when item is not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_player.inventory = json.dumps([])
    result = await handle_read_command(
        {"args": ["Nonexistent Book"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "not found in your inventory or the room" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_not_spellbook(mock_request, mock_persistence, mock_spell_learning_service, mock_player):
    """Test read command when item is not a spellbook."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_player.inventory = json.dumps([{"id": "item_001", "name": "Regular Book", "metadata": {}}])
    result = await handle_read_command(
        {"args": ["Regular Book"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "is not a spellbook" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_empty_spellbook(mock_request, mock_persistence, mock_spell_learning_service, mock_player):
    """Test read command when spellbook is empty."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_player.inventory = json.dumps(
        [{"id": "spellbook_001", "name": "Empty Tome", "metadata": {"spellbook": True, "spells": []}}]
    )
    result = await handle_read_command(
        {"args": ["Empty Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "empty or corrupted" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_single_spell_auto_learn(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command with single spell auto-learning."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Test Spell!", "corruption_applied": 0}
    )
    result = await handle_read_command(
        {"args": ["Ancient Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "Learned Test Spell!" in result["result"]
    mock_spell_learning_service.learn_spell.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_read_command_single_spell_with_corruption(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command with single spell that applies corruption."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Test Spell!", "corruption_applied": 5}
    )
    result = await handle_read_command(
        {"args": ["Ancient Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "Learned Test Spell!" in result["result"]
    assert "tainted your mind (+5 corruption)" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_specific_spell(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command with specific spell name."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Test Spell!", "corruption_applied": 0}
    )
    result = await handle_read_command(
        {"args": ["Ancient Tome", "Test Spell"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "Learned Test Spell!" in result["result"]
    mock_spell_learning_service.learn_spell.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_read_command_spell_not_found(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command when specified spell is not found."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_registry.get_spell_by_name.return_value = None
    result = await handle_read_command(
        {"args": ["Ancient Tome", "Nonexistent Spell"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "not found in the spellbook" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_spell_not_in_book(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command when specified spell is not in the book."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    spell = MagicMock()
    spell.spell_id = "spell_002"
    spell.name = "Other Spell"
    mock_spell_registry.get_spell_by_name.return_value = spell
    result = await handle_read_command(
        {"args": ["Ancient Tome", "Other Spell"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "is not in this spellbook" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_multiple_spells_list(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command with multiple spells lists them."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_player.inventory = json.dumps(
        [
            {
                "id": "spellbook_001",
                "name": "Ancient Tome",
                "metadata": {
                    "spellbook": True,
                    "spells": ["spell_001", "spell_002"],
                },
            }
        ]
    )
    spell2 = MagicMock()
    spell2.spell_id = "spell_002"
    spell2.name = "Second Spell"
    mock_spell_registry.get_spell.side_effect = lambda sid: spell2 if sid == "spell_002" else mock_spell_registry.get_spell.return_value
    result = await handle_read_command(
        {"args": ["Ancient Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "contains the following spells" in result["result"]
    assert "Test Spell" in result["result"] or "spell_001" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_learn_failure(
    mock_request, mock_persistence, mock_spell_learning_service, mock_spell_registry, mock_player
):
    """Test read command when learning spell fails."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": False, "message": "Cannot learn spell: insufficient knowledge"}
    )
    result = await handle_read_command(
        {"args": ["Ancient Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "Cannot learn spell" in result["result"]


@pytest.mark.asyncio
async def test_handle_read_command_error_handling(mock_request, mock_persistence, mock_spell_learning_service, mock_player):
    """Test read command error handling."""
    mock_request.app.state.persistence = mock_persistence
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_player.inventory = "invalid json"
    result = await handle_read_command(
        {"args": ["Ancient Tome"]}, {"username": "testuser"}, mock_request, None, "TestPlayer"
    )
    assert "error occurred" in result["result"].lower()
