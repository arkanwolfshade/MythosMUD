"""
Unit tests for emote command handler.

Tests the emote command functionality.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.commands.emote_commands import (
    _extract_emote_action,
    _format_emote_messages,
    _get_emote_services,
    _handle_emote_result,
    _validate_player_for_emote,
    handle_emote_command,
)


def test_extract_emote_action_from_action_key():
    """Test _extract_emote_action extracts action from action key."""
    command_data = {"action": "waves hello"}
    assert _extract_emote_action(command_data) == "waves hello"


def test_extract_emote_action_from_parsed_command():
    """Test _extract_emote_action extracts action from parsed_command attribute."""
    mock_parsed_command = MagicMock()
    mock_parsed_command.action = "waves hello"
    command_data = {"parsed_command": mock_parsed_command}
    assert _extract_emote_action(command_data) == "waves hello"


def test_extract_emote_action_not_found():
    """Test _extract_emote_action returns None when action not found."""
    command_data = {}
    assert _extract_emote_action(command_data) is None


def test_get_emote_services_with_services():
    """Test _get_emote_services returns services when available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_request.app.state.chat_service = MagicMock()
    mock_request.app.state.player_service = MagicMock()
    
    chat_service, player_service = _get_emote_services(mock_request)
    
    assert chat_service is not None
    assert player_service is not None


def test_get_emote_services_no_request():
    """Test _get_emote_services returns None when request is None."""
    chat_service, player_service = _get_emote_services(None)
    
    assert chat_service is None
    assert player_service is None


def test_get_emote_services_no_app():
    """Test _get_emote_services returns None when app is not available."""
    mock_request = MagicMock()
    mock_request.app = None
    
    chat_service, player_service = _get_emote_services(mock_request)
    
    assert chat_service is None
    assert player_service is None


def test_get_emote_services_no_state():
    """Test _get_emote_services returns None when state is not available."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = None
    
    chat_service, player_service = _get_emote_services(mock_request)
    
    assert chat_service is None
    assert player_service is None


@pytest.mark.asyncio
async def test_validate_player_for_emote_success():
    """Test _validate_player_for_emote with valid player."""
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    
    player_obj, room_id, player_id, error = await _validate_player_for_emote(mock_player_service, "TestPlayer")
    
    assert player_obj == mock_player
    assert room_id == "test_room"
    assert player_id == mock_player.id
    assert error is None


@pytest.mark.asyncio
async def test_validate_player_for_emote_player_not_found():
    """Test _validate_player_for_emote when player is not found."""
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    
    player_obj, room_id, player_id, error = await _validate_player_for_emote(mock_player_service, "TestPlayer")
    
    assert player_obj is None
    assert room_id is None
    assert player_id is None
    assert error == "Player not found."


@pytest.mark.asyncio
async def test_validate_player_for_emote_no_room():
    """Test _validate_player_for_emote when player has no room."""
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    
    player_obj, room_id, player_id, error = await _validate_player_for_emote(mock_player_service, "TestPlayer")
    
    assert error == "You are not in a room."


@pytest.mark.asyncio
async def test_validate_player_for_emote_no_player_id():
    """Test _validate_player_for_emote when player has no ID."""
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    del mock_player.id
    del mock_player.player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    
    player_obj, room_id, player_id, error = await _validate_player_for_emote(mock_player_service, "TestPlayer")
    
    assert error == "Player ID not found."


@pytest.mark.asyncio
async def test_validate_player_for_emote_player_id_from_player_id_attribute():
    """Test _validate_player_for_emote uses player_id attribute when id is missing."""
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    del mock_player.id
    mock_player.player_id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    
    player_obj, room_id, player_id, error = await _validate_player_for_emote(mock_player_service, "TestPlayer")
    
    assert player_id == mock_player.player_id
    assert error is None


def test_format_emote_messages_custom_emote():
    """Test _format_emote_messages with custom emote."""
    with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
        mock_emote_service = MagicMock()
        mock_emote_service.is_emote_alias = MagicMock(return_value=False)
        mock_emote_service_class.return_value = mock_emote_service
        
        self_message, formatted_action = _format_emote_messages("waves hello", "TestPlayer")
        
        assert self_message == "TestPlayer waves hello"
        assert formatted_action == "waves hello"


def test_format_emote_messages_predefined_emote():
    """Test _format_emote_messages with predefined emote alias."""
    with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
        mock_emote_service = MagicMock()
        mock_emote_service.is_emote_alias = MagicMock(return_value=True)
        mock_emote_service.format_emote_messages = MagicMock(return_value=("You wave hello", "TestPlayer waves hello"))
        mock_emote_service_class.return_value = mock_emote_service
        
        self_message, formatted_action = _format_emote_messages("wave", "TestPlayer")
        
        assert self_message == "You wave hello"
        assert formatted_action == "waves hello"  # Player name prefix removed


def test_handle_emote_result_success():
    """Test _handle_emote_result with successful result."""
    result = {"success": True, "message": {"id": "123"}}
    self_message = "TestPlayer waves hello"
    
    output = _handle_emote_result(result, self_message, "TestPlayer", "test_room")
    
    assert output["result"] == self_message


def test_handle_emote_result_failure():
    """Test _handle_emote_result with failed result."""
    result = {"success": False, "error": "Rate limit exceeded"}
    self_message = "TestPlayer waves hello"
    
    output = _handle_emote_result(result, self_message, "TestPlayer", "test_room")
    
    assert "Error sending emote" in output["result"]
    assert "Rate limit exceeded" in output["result"]


def test_handle_emote_result_failure_no_error():
    """Test _handle_emote_result with failed result and no error message."""
    result = {"success": False}
    self_message = "TestPlayer waves hello"
    
    output = _handle_emote_result(result, self_message, "TestPlayer", "test_room")
    
    assert "Error sending emote" in output["result"]
    assert "Unknown error" in output["result"]


@pytest.mark.asyncio
async def test_handle_emote_command_no_action():
    """Test handle_emote_command with no action."""
    result = await handle_emote_command(
        command_data={},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "Emote what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_emote_command_no_services():
    """Test handle_emote_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None
    
    result = await handle_emote_command(
        command_data={"action": "waves hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_emote_command_player_not_found():
    """Test handle_emote_command when player is not found."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service
    
    result = await handle_emote_command(
        command_data={"action": "waves hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "Player not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_emote_command_success():
    """Test handle_emote_command successful execution."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_emote_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service
    
    with patch("server.game.emote_service.EmoteService") as mock_emote_service_class:
        mock_emote_service = MagicMock()
        mock_emote_service.is_emote_alias = MagicMock(return_value=False)
        mock_emote_service_class.return_value = mock_emote_service
        
        result = await handle_emote_command(
            command_data={"action": "waves hello"},
            _current_user={},
            request=mock_request,
            _alias_storage=None,
            player_name="TestPlayer",
        )
        
        assert "TestPlayer waves hello" in result["result"]
        mock_chat_service.send_emote_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_emote_command_error_handling():
    """Test handle_emote_command handles exceptions gracefully."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=ValueError("Test error"))
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service
    
    result = await handle_emote_command(
        command_data={"action": "waves hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )
    
    assert "Error sending emote" in result["result"]
    assert "Test error" in result["result"]
