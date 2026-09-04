"""Unit tests for whisper and reply communication command handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.communication_commands import (
    handle_reply_command,
    handle_whisper_command,
)

from .communication_commands_mocks import request_with_app_container


@pytest.mark.asyncio
async def test_handle_whisper_command_no_target():
    """Test handle_whisper_command with no target."""
    result = await handle_whisper_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Say what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_whisper_command_no_message():
    """Test handle_whisper_command with no message."""
    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer"},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Say what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_whisper_command_no_services():
    """Test handle_whisper_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_whisper_command_target_not_found():
    """Test handle_whisper_command when target is not found."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, None])
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "whisper into the aether" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_whisper_command_whisper_to_self():
    """Test handle_whisper_command when trying to whisper to self."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    player_id = uuid.uuid4()
    mock_player.id = player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_whisper_command(
        command_data={"target": "TestPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "cannot whisper to yourself" in result["result"]


@pytest.mark.asyncio
async def test_handle_whisper_command_success():
    """Test handle_whisper_command successful execution."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_whisper_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_chat_service.send_whisper_message = send_whisper_message
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You whisper to OtherPlayer: Hello" in result["result"]
    send_whisper_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_reply_command_no_message():
    """Test handle_reply_command with no message."""
    result = await handle_reply_command(
        command_data={},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Say what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_reply_command_no_services():
    """Test handle_reply_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_reply_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_reply_command_no_last_whisper_sender():
    """Test handle_reply_command when no last whisper sender."""
    mock_request, container = request_with_app_container()
    mock_chat_service = MagicMock()
    mock_chat_service.get_last_whisper_sender = MagicMock(return_value=None)
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_reply_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "No one has whispered to you recently" in result["result"]


@pytest.mark.asyncio
async def test_handle_reply_command_success():
    """Test handle_reply_command successful execution."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    mock_chat_service.get_last_whisper_sender = MagicMock(return_value="OtherPlayer")
    send_whisper_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_chat_service.send_whisper_message = send_whisper_message
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_reply_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You whisper to OtherPlayer: Hello" in result["result"]
    send_whisper_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_whisper_command_chat_service_failure():
    """Test handle_whisper_command when chat service returns failure."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_whisper_message: AsyncMock = AsyncMock(return_value={"success": False, "error": "Target offline"})
    mock_chat_service.send_whisper_message = send_whisper_message
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Error" in result["result"] or "error" in result["result"].lower()
