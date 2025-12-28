"""
Unit tests for magic commands.

Tests the /cast, /spells, /spell, /learn, and /stop commands.
"""

import uuid
from enum import Enum
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.magic_commands import (
    MagicCommandHandler,
    handle_cast_command,
    handle_learn_command,
    handle_spell_command,
    handle_spells_command,
    handle_stop_command,
)


class MockSchool(Enum):
    """Mock spell school enum."""

    EVOCATION = "evocation"
    NECROMANCY = "necromancy"


class MockTargetType(Enum):
    """Mock target type enum."""

    SELF = "self"
    TARGET = "target"


class MockRangeType(Enum):
    """Mock range type enum."""

    TOUCH = "touch"
    RANGE = "range"


class MockEffectType(Enum):
    """Mock effect type enum."""

    DAMAGE = "damage"
    HEAL = "heal"


@pytest.fixture
def mock_magic_service():
    """Create a mock magic service."""
    service = MagicMock()
    service.player_service = MagicMock()
    service.player_service.persistence = MagicMock()
    service.cast_spell = AsyncMock()
    service.interrupt_casting = AsyncMock()
    return service


@pytest.fixture
def mock_spell_registry():
    """Create a mock spell registry."""
    registry = MagicMock()
    spell = MagicMock()
    spell.spell_id = "spell_001"
    spell.name = "Test Spell"
    spell.description = "A test spell"
    spell.school = MockSchool.EVOCATION
    spell.mp_cost = 10
    spell.lucidity_cost = 5
    spell.corruption_on_cast = 2
    spell.casting_time_seconds = 3
    spell.target_type = MockTargetType.TARGET
    spell.range_type = MockRangeType.RANGE
    spell.effect_type = MockEffectType.DAMAGE
    spell.materials = []
    spell.requires_lucidity = MagicMock(return_value=True)
    registry.get_spell_by_name.return_value = spell
    registry.get_spell.return_value = spell
    return registry


@pytest.fixture
def mock_player():
    """Create a mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    return player


@pytest.fixture
def mock_player_spell_repository():
    """Create a mock player spell repository."""
    repository = MagicMock()
    repository.get_player_spells = AsyncMock(return_value=[])
    repository.get_player_spell = AsyncMock(return_value=None)
    return repository


@pytest.fixture
def mock_spell_learning_service():
    """Create a mock spell learning service."""
    service = MagicMock()
    service.learn_spell = AsyncMock()
    return service


@pytest.fixture
def mock_chat_service():
    """Create a mock chat service."""
    service = MagicMock()
    service.send_say_message = AsyncMock(return_value={"success": True})
    return service


@pytest.fixture
def handler(mock_magic_service, mock_spell_registry, mock_player_spell_repository):
    """Create a MagicCommandHandler instance."""
    return MagicCommandHandler(mock_magic_service, mock_spell_registry, mock_player_spell_repository)


@pytest.mark.asyncio
async def test_handle_cast_command_no_player(handler, mock_player_spell_repository):
    """Test cast command when player is not found."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handler.handle_cast_command({}, {}, None, None, "TestPlayer")
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_cast_command_no_spell_name(handler, mock_player):
    """Test cast command when no spell name is provided."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    result = await handler.handle_cast_command({}, {}, None, None, "TestPlayer")
    assert "Usage: /cast" in result["result"]


@pytest.mark.asyncio
async def test_handle_cast_command_cast_failure(handler, mock_player):
    """Test cast command when casting fails."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.magic_service.cast_spell = AsyncMock(return_value={"success": False, "message": "Insufficient MP"})
    result = await handler.handle_cast_command({"spell_name": "Test Spell"}, {}, None, None, "TestPlayer")
    assert "Insufficient MP" in result["result"]


@pytest.mark.asyncio
async def test_handle_cast_command_success(handler, mock_player, mock_chat_service):
    """Test cast command success."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.magic_service.cast_spell = AsyncMock(
        return_value={"success": True, "message": "Test Spell cast successfully."}
    )
    handler.chat_service = mock_chat_service
    result = await handler.handle_cast_command({"spell_name": "Test Spell"}, {}, None, None, "TestPlayer")
    assert "cast successfully" in result["result"]
    mock_chat_service.send_say_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_cast_command_with_target(handler, mock_player, mock_chat_service):
    """Test cast command with target."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.magic_service.cast_spell = AsyncMock(
        return_value={"success": True, "message": "Test Spell cast successfully."}
    )
    handler.chat_service = mock_chat_service
    result = await handler.handle_cast_command(
        {"spell_name": "Test Spell", "target": "TargetPlayer"}, {}, None, None, "TestPlayer"
    )
    assert "cast successfully" in result["result"]
    # Verify announcement includes target
    call_args = mock_chat_service.send_say_message.call_args
    assert "targeting TargetPlayer" in call_args[0][1]


@pytest.mark.asyncio
async def test_handle_spells_command_no_player(handler):
    """Test spells command when player is not found."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handler.handle_spells_command({}, {}, None, None, "TestPlayer")
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_spells_command_no_spells(handler, mock_player):
    """Test spells command when player has no spells."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.player_spell_repository.get_player_spells = AsyncMock(return_value=[])
    result = await handler.handle_spells_command({}, {}, None, None, "TestPlayer")
    assert "not learned any spells" in result["result"]


@pytest.mark.asyncio
async def test_handle_spells_command_with_spells(handler, mock_player, mock_spell_registry):
    """Test spells command when player has spells."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    player_spell = MagicMock()
    player_spell.spell_id = "spell_001"
    player_spell.mastery = 50
    handler.player_spell_repository.get_player_spells = AsyncMock(return_value=[player_spell])
    result = await handler.handle_spells_command({}, {}, None, None, "TestPlayer")
    assert "Learned Spells:" in result["result"]
    assert "Test Spell" in result["result"]
    assert "50%" in result["result"]


@pytest.mark.asyncio
async def test_handle_spell_command_no_player(handler):
    """Test spell command when player is not found."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handler.handle_spell_command({}, {}, None, None, "TestPlayer")
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_spell_command_no_spell_name(handler, mock_player):
    """Test spell command when no spell name is provided."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    result = await handler.handle_spell_command({}, {}, None, None, "TestPlayer")
    assert "Usage: /spell" in result["result"]


@pytest.mark.asyncio
async def test_handle_spell_command_spell_not_found(handler, mock_player):
    """Test spell command when spell is not found."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.spell_registry.get_spell_by_name.return_value = None
    result = await handler.handle_spell_command({"spell_name": "Nonexistent"}, {}, None, None, "TestPlayer")
    assert "not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_spell_command_success(handler, mock_player, mock_spell_registry):
    """Test spell command success."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    result = await handler.handle_spell_command({"spell_name": "Test Spell"}, {}, None, None, "TestPlayer")
    assert "Spell: Test Spell" in result["result"]
    assert "Description: A test spell" in result["result"]
    assert "School: evocation" in result["result"]
    assert "MP Cost: 10" in result["result"]
    assert "Lucidity Cost: 5" in result["result"]
    assert "Status: Not learned" in result["result"]


@pytest.mark.asyncio
async def test_handle_spell_command_with_mastery(handler, mock_player, mock_spell_registry):
    """Test spell command when player has mastery."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    player_spell = MagicMock()
    player_spell.mastery = 75
    handler.player_spell_repository.get_player_spell = AsyncMock(return_value=player_spell)
    result = await handler.handle_spell_command({"spell_name": "Test Spell"}, {}, None, None, "TestPlayer")
    assert "Your Mastery: 75%" in result["result"]


@pytest.mark.asyncio
async def test_handle_learn_command_no_service(handler):
    """Test learn command when spell learning service is not available."""
    handler.spell_learning_service = None
    result = await handler.handle_learn_command({}, {}, None, None, "TestPlayer")
    assert "Spell learning system not initialized" in result["result"]


@pytest.mark.asyncio
async def test_handle_learn_command_no_player(handler, mock_spell_learning_service):
    """Test learn command when player is not found."""
    handler.spell_learning_service = mock_spell_learning_service
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handler.handle_learn_command({}, {}, None, None, "TestPlayer")
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_learn_command_no_spell_name(handler, mock_player, mock_spell_learning_service):
    """Test learn command when no spell name is provided."""
    handler.spell_learning_service = mock_spell_learning_service
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    result = await handler.handle_learn_command({}, {}, None, None, "TestPlayer")
    assert "Usage: /learn" in result["result"]


@pytest.mark.asyncio
async def test_handle_learn_command_success(handler, mock_player, mock_spell_learning_service):
    """Test learn command success."""
    handler.spell_learning_service = mock_spell_learning_service
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Test Spell!", "corruption_applied": 0}
    )
    result = await handler.handle_learn_command({"spell_name": "Test Spell"}, {}, None, None, "TestPlayer")
    assert "Learned Test Spell!" in result["result"]


@pytest.mark.asyncio
async def test_handle_learn_command_with_corruption(handler, mock_player, mock_spell_learning_service):
    """Test learn command with corruption applied."""
    handler.spell_learning_service = mock_spell_learning_service
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Test Spell!", "corruption_applied": 5}
    )
    result = await handler.handle_learn_command({"spell_name": "Test Spell"}, {}, None, None, "TestPlayer")
    assert "tainted your mind (+5 corruption)" in result["result"]


@pytest.mark.asyncio
async def test_handle_stop_command_no_player(handler):
    """Test stop command when player is not found."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=None)
    result = await handler.handle_stop_command({}, {}, None, None, "TestPlayer")
    assert "not recognized by the cosmic forces" in result["result"]


@pytest.mark.asyncio
async def test_handle_stop_command_success(handler, mock_player):
    """Test stop command success."""
    handler.magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    handler.magic_service.interrupt_casting = AsyncMock(
        return_value={"success": True, "message": "Casting interrupted."}
    )
    result = await handler.handle_stop_command({}, {}, None, None, "TestPlayer")
    assert "Casting interrupted" in result["result"]


@pytest.mark.asyncio
async def test_announce_spell_cast_no_chat_service(handler, mock_player):
    """Test announce spell cast when chat service is not available."""
    handler.chat_service = None
    await handler._announce_spell_cast(mock_player, {}, "Test Spell", None)
    # Should not raise an error


@pytest.mark.asyncio
async def test_announce_spell_cast_no_player_id(handler, mock_player, mock_chat_service):
    """Test announce spell cast when player has no ID."""
    handler.chat_service = mock_chat_service
    mock_player.id = None
    mock_player.player_id = None
    await handler._announce_spell_cast(mock_player, {}, "Test Spell", None)
    # Should not raise an error, but should log a warning


@pytest.mark.asyncio
async def test_announce_spell_cast_chat_error(handler, mock_player, mock_chat_service):
    """Test announce spell cast when chat service raises an error."""
    handler.chat_service = mock_chat_service
    mock_chat_service.send_say_message = AsyncMock(side_effect=OSError("Network error"))
    await handler._announce_spell_cast(mock_player, {}, "Test Spell", None)
    # Should not raise an error, but should log an error


@pytest.mark.asyncio
async def test_handle_cast_command_wrapper_no_magic_service():
    """Test handle_cast_command wrapper when magic service is not available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.magic_service = None
    result = await handle_cast_command({}, {}, mock_request, None, "TestPlayer")
    assert "Magic system not initialized" in result["result"]


@pytest.mark.asyncio
async def test_handle_spells_command_wrapper_no_spell_registry():
    """Test handle_spells_command wrapper when spell registry is not available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.magic_service = MagicMock()
    mock_request.app.state.spell_registry = None
    result = await handle_spells_command({}, {}, mock_request, None, "TestPlayer")
    assert "Magic system not initialized" in result["result"]


@pytest.mark.asyncio
async def test_handle_spell_command_wrapper_success(
    mock_magic_service, mock_spell_registry, mock_player, mock_player_spell_repository
):
    """Test handle_spell_command wrapper success."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.magic_service = mock_magic_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    # Mock PlayerSpellRepository to avoid creating real database connections
    with patch("server.commands.magic_commands.PlayerSpellRepository", return_value=mock_player_spell_repository):
        result = await handle_spell_command({"spell_name": "Test Spell"}, {}, mock_request, None, "TestPlayer")
    assert "Spell: Test Spell" in result["result"]


@pytest.mark.asyncio
async def test_handle_learn_command_wrapper_success(
    mock_magic_service, mock_spell_registry, mock_player, mock_spell_learning_service
):
    """Test handle_learn_command wrapper success."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.magic_service = mock_magic_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_request.app.state.spell_learning_service = mock_spell_learning_service
    mock_magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_spell_learning_service.learn_spell = AsyncMock(
        return_value={"success": True, "message": "Learned Test Spell!", "corruption_applied": 0}
    )
    result = await handle_learn_command({"spell_name": "Test Spell"}, {}, mock_request, None, "TestPlayer")
    assert "Learned Test Spell!" in result["result"]


@pytest.mark.asyncio
async def test_handle_stop_command_wrapper_success(mock_magic_service, mock_spell_registry, mock_player):
    """Test handle_stop_command wrapper success."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.magic_service = mock_magic_service
    mock_request.app.state.spell_registry = mock_spell_registry
    mock_magic_service.player_service.persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_magic_service.interrupt_casting = AsyncMock(return_value={"success": True, "message": "Casting interrupted."})
    result = await handle_stop_command({}, {}, mock_request, None, "TestPlayer")
    assert "Casting interrupted" in result["result"]
