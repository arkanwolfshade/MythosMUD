"""Unit tests for local, global, and system chat command handlers."""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.communication_commands import (
    handle_global_command,
    handle_local_command,
    handle_system_command,
)

from .communication_commands_mocks import request_with_app_container


@pytest.mark.asyncio
async def test_handle_local_command_no_message():
    """Test handle_local_command with no message."""
    result = await handle_local_command(
        command_data={},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Say what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_local_command_no_services():
    """Test handle_local_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_local_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_local_command_success():
    """Test handle_local_command successful execution."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_local_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_chat_service.send_local_message = send_local_message
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_local_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You say locally: Hello" in result["result"]
    send_local_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_global_command_no_message():
    """Test handle_global_command with no message."""
    result = await handle_global_command(
        command_data={},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Say what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_global_command_no_services():
    """Test handle_global_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_global_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_global_command_level_too_low():
    """Test handle_global_command when player level is too low."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.level = 0  # Too low for global chat
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_global_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "must be at least level 1" in result["result"]


@pytest.mark.asyncio
async def test_handle_global_command_success():
    """Test handle_global_command successful execution."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_global_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_chat_service.send_global_message = send_global_message
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player.level = 1  # Required for global chat
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_global_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You say (global): Hello" in result["result"]
    send_global_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_system_command_no_message():
    """Test handle_system_command with no message."""
    result = await handle_system_command(
        command_data={},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "System what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_system_command_no_services():
    """Test handle_system_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_system_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_system_command_not_admin():
    """Test handle_system_command when player is not admin."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    player_id = uuid.uuid4()
    mock_player.id = player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=False)  # Not admin
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()
    container.user_manager = mock_user_manager

    result = await handle_system_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "must be an admin" in result["result"]


@pytest.mark.asyncio
async def test_handle_system_command_success():
    """Test handle_system_command successful execution."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_system_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_chat_service.send_system_message = send_system_message
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    player_id = uuid.uuid4()
    mock_player.id = player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_user_manager = MagicMock()
    is_admin: MagicMock = MagicMock(return_value=True)  # Admin check
    mock_user_manager.is_admin = is_admin
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service
    container.user_manager = mock_user_manager

    result = await handle_system_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You system: Hello" in result["result"]
    send_system_message.assert_awaited_once()
    is_admin.assert_called_once_with(player_id)


@pytest.mark.asyncio
async def test_handle_local_command_no_room():
    """Test handle_local_command when player has no current room."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_local_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not in a room" in result["result"]


@pytest.mark.asyncio
async def test_handle_global_command_player_not_found():
    """Test handle_global_command when player is not found."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_global_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Player not found" in result["result"]
