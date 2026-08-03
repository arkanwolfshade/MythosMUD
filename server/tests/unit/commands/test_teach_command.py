"""
Unit tests for teach command handlers.

Tests the teach command functionality.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.teach_command import handle_teach_command


@pytest.mark.asyncio
async def test_handle_teach_command():
    """Test handle_teach_command() teaches spell to player."""
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

    result = await handle_teach_command(
        {"target": "OtherPlayer", "spell": "test_spell"},
        {"name": "TestPlayer"},
        mock_request,
        None,
        "TestPlayer",
    )

    assert "result" in result
    assert isinstance(result["result"], str)


@pytest.mark.asyncio
async def test_handle_teach_command_no_target():
    """Test handle_teach_command() handles missing target."""
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_state.persistence = mock_persistence
    mock_state.player_service = MagicMock()
    mock_state.spell_learning_service = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app

    result = await handle_teach_command({}, {"name": "TestPlayer"}, mock_request, None, "TestPlayer")
    assert "result" in result
    assert "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_teach_command_no_persistence():
    """Test handle_teach_command() handles missing persistence."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_teach_command(
        {"target": "OtherPlayer", "spell": "test_spell"}, {}, mock_request, None, "TestPlayer"
    )

    assert "result" in result
    assert "not available" in result["result"].lower() or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_teach_command_no_spell_learning_service():
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.persistence = AsyncMock()
    mock_state.player_service = MagicMock()
    mock_state.spell_learning_service = None
    mock_app.state = mock_state
    mock_request.app = mock_app
    result = await handle_teach_command(
        {"args": ["npc", "spell"]}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "not initialized" in result["result"]


@pytest.mark.asyncio
async def test_handle_teach_command_player_not_found():
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    mock_state.persistence = AsyncMock(get_player_by_name=AsyncMock(return_value=None))
    mock_state.player_service = MagicMock()
    mock_state.spell_learning_service = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app
    result = await handle_teach_command({"args": ["npc", "spell"]}, {"username": "Ghost"}, mock_request, None, "Ghost")
    assert "not recognized" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.teach_command.TargetResolutionService")
async def test_handle_teach_command_target_resolution_failure(mock_trs_cls):
    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    player = MagicMock(player_id="player-uuid")
    mock_state.persistence = AsyncMock(get_player_by_name=AsyncMock(return_value=player))
    mock_state.player_service = MagicMock()
    mock_state.spell_learning_service = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app
    mock_trs_cls.return_value.resolve_target = AsyncMock(
        return_value=MagicMock(success=False, error_message="NPC vanished.")
    )
    result = await handle_teach_command(
        {"args": ["npc", "spell"]}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert result["result"] == "NPC vanished."


@pytest.mark.asyncio
@patch("server.commands.teach_command.TargetResolutionService")
async def test_handle_teach_command_not_npc_target(mock_trs_cls):
    from server.schemas.shared import TargetType

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    player = MagicMock(player_id="player-uuid")
    mock_state.persistence = AsyncMock(get_player_by_name=AsyncMock(return_value=player))
    mock_state.player_service = MagicMock()
    mock_state.spell_learning_service = MagicMock()
    mock_app.state = mock_state
    mock_request.app = mock_app
    match = MagicMock(target_type=TargetType.PLAYER, target_id="other")
    mock_trs_cls.return_value.resolve_target = AsyncMock(
        return_value=MagicMock(success=True, get_single_match=MagicMock(return_value=match))
    )
    result = await handle_teach_command(
        {"args": ["Bob", "spell"]}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "not an NPC" in result["result"]


@pytest.mark.asyncio
@patch("server.commands.teach_command.TargetResolutionService")
async def test_handle_teach_command_learn_failure(mock_trs_cls):
    from server.schemas.shared import TargetType

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    player = MagicMock(player_id="player-uuid")
    mock_state.persistence = AsyncMock(get_player_by_name=AsyncMock(return_value=player))
    mock_state.player_service = MagicMock()
    spell_service = MagicMock()
    spell_service.learn_spell_from_npc = AsyncMock(return_value={"success": False, "message": "Forbidden."})
    mock_state.spell_learning_service = spell_service
    mock_app.state = mock_state
    mock_request.app = mock_app
    match = MagicMock(target_type=TargetType.NPC, target_id="npc-1")
    mock_trs_cls.return_value.resolve_target = AsyncMock(
        return_value=MagicMock(success=True, get_single_match=MagicMock(return_value=match))
    )
    result = await handle_teach_command(
        {"args": ["Sage", "heal"]}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert result["result"] == "Forbidden."


@pytest.mark.asyncio
@patch("server.commands.teach_command.TargetResolutionService")
async def test_handle_teach_command_success_with_corruption(mock_trs_cls):
    from server.schemas.shared import TargetType

    mock_request = MagicMock()
    mock_app = MagicMock()
    mock_state = MagicMock()
    player = MagicMock(player_id="player-uuid")
    mock_state.persistence = AsyncMock(get_player_by_name=AsyncMock(return_value=player))
    mock_state.player_service = MagicMock()
    spell_service = MagicMock()
    spell_service.learn_spell_from_npc = AsyncMock(
        return_value={"success": True, "message": "Learned heal!", "corruption_applied": 3}
    )
    mock_state.spell_learning_service = spell_service
    mock_app.state = mock_state
    mock_request.app = mock_app
    match = MagicMock(target_type=TargetType.NPC, target_id="npc-1")
    mock_trs_cls.return_value.resolve_target = AsyncMock(
        return_value=MagicMock(success=True, get_single_match=MagicMock(return_value=match))
    )
    result = await handle_teach_command(
        {"args": ["Sage", "heal"]}, {"username": "TestPlayer"}, mock_request, None, "TestPlayer"
    )
    assert "corruption" in result["result"]
