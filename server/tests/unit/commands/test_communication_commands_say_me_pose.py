"""Unit tests for say, me, and pose communication command handlers."""

import uuid
from typing import cast
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.communication_commands import (
    handle_me_command,
    handle_pose_command,
    handle_say_command,
)

from .communication_commands_mocks import request_with_app_container


@pytest.mark.asyncio
async def test_handle_say_command_no_message():
    """Test handle_say_command with no message."""
    result = await handle_say_command(
        command_data={},
        _current_user={},
        request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Say what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_say_command_no_services():
    """Test handle_say_command when services are not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not available" in result["result"]


@pytest.mark.asyncio
async def test_handle_say_command_player_not_found():
    """Test handle_say_command when player is not found."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Player not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_say_command_success():
    """Test handle_say_command successful execution."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_say_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_chat_service.send_say_message = send_say_message
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You say: Hello" in result["result"]
    send_say_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_say_command_delegates_broadcast_to_chat_service_with_ids():
    """Room say must call chat_service.send_say_message(player_id, message) for broadcast pipeline."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    send_say_message: AsyncMock = AsyncMock(return_value={"success": True, "message": {"id": "x"}})
    mock_chat_service.send_say_message = send_say_message
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "room_z"
    expected_pid = uuid.uuid4()
    mock_player.player_id = expected_pid
    mock_player.id = None
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_say_command(
        command_data={"message": "Hear me"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="Orator",
    )

    assert "You say: Hear me" in result["result"]
    send_say_message.assert_awaited_once_with(expected_pid, "Hear me")


@pytest.mark.asyncio
async def test_handle_me_command_no_action():
    """Test handle_me_command with no action."""
    result = await handle_me_command(
        command_data={},
        _current_user={},
        _request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Do what?" in result["result"]


@pytest.mark.asyncio
async def test_handle_me_command_success():
    """Test handle_me_command successful execution."""
    result = await handle_me_command(
        command_data={"action": "waves hello"},
        _current_user={},
        _request=MagicMock(),
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "TestPlayer waves hello" in result["result"]


@pytest.mark.asyncio
async def test_handle_pose_command_no_persistence():
    """Test handle_pose_command when persistence is not available."""
    mock_request = MagicMock()
    mock_request.app = None

    result = await handle_pose_command(
        command_data={"pose": "standing tall"},
        current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "cannot set your pose" in result["result"]


@pytest.mark.asyncio
async def test_handle_pose_command_player_not_found():
    """Test handle_pose_command when player is not found."""
    mock_request, container = request_with_app_container()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    container.async_persistence = mock_persistence

    result = await handle_pose_command(
        command_data={"pose": "standing tall"},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "cannot set your pose" in result["result"]


@pytest.mark.asyncio
async def test_handle_pose_command_clear_pose():
    """Test handle_pose_command clearing pose."""
    mock_request, container = request_with_app_container()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.pose = "old pose"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    save_player: AsyncMock = AsyncMock()
    mock_persistence.save_player = save_player
    container.async_persistence = mock_persistence

    result = await handle_pose_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "pose has been cleared" in result["result"]
    assert cast(object | None, mock_player.pose) is None
    save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_pose_command_set_pose():
    """Test handle_pose_command setting pose."""
    mock_request, container = request_with_app_container()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    save_player: AsyncMock = AsyncMock()
    mock_persistence.save_player = save_player
    container.async_persistence = mock_persistence

    result = await handle_pose_command(
        command_data={"pose": "standing tall"},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Your pose is now: standing tall" in result["result"]
    assert cast(object, mock_player.pose) == "standing tall"
    save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_say_command_no_room():
    """Test handle_say_command when player has no current room."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "not in a room" in result["result"]


@pytest.mark.asyncio
async def test_handle_say_command_no_player_id():
    """Test handle_say_command when player has no ID."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = None
    mock_player.player_id = None
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Player ID not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_say_command_chat_service_failure():
    """Test handle_say_command when chat service returns failure."""
    mock_request, container = request_with_app_container()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_say_message = AsyncMock(return_value={"success": False, "error": "Service unavailable"})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    container.chat_service = mock_chat_service
    container.player_service = mock_player_service

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Error" in result["result"] or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_say_command_exception():
    """Test handle_say_command handles exceptions."""
    mock_request, container = request_with_app_container()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=RuntimeError("Database error"))
    container.player_service = mock_player_service
    container.chat_service = AsyncMock()

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Error" in result["result"] or "error" in result["result"].lower()
