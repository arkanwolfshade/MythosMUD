"""
Unit tests for communication command handlers.

Tests the say, me, pose, local, global, system, whisper, and reply commands.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.communication_commands import (
    handle_global_command,
    handle_local_command,
    handle_me_command,
    handle_pose_command,
    handle_reply_command,
    handle_say_command,
    handle_system_command,
    handle_whisper_command,
)


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_say_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You say: Hello" in result["result"]
    mock_chat_service.send_say_message.assert_awaited_once()


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=None)
    mock_request.app.state.persistence = mock_persistence

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_player.pose = "old pose"
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_request.app.state.persistence = mock_persistence

    result = await handle_pose_command(
        command_data={},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "pose has been cleared" in result["result"]
    assert mock_player.pose is None
    mock_persistence.save_player.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_pose_command_set_pose():
    """Test handle_pose_command setting pose."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_persistence = AsyncMock()
    mock_player = MagicMock()
    mock_persistence.get_player_by_name = AsyncMock(return_value=mock_player)
    mock_persistence.save_player = AsyncMock()
    mock_request.app.state.persistence = mock_persistence

    result = await handle_pose_command(
        command_data={"pose": "standing tall"},
        current_user={"username": "TestPlayer"},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Your pose is now: standing tall" in result["result"]
    assert mock_player.pose == "standing tall"
    mock_persistence.save_player.assert_awaited_once()


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_local_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

    result = await handle_local_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You say locally: Hello" in result["result"]
    mock_chat_service.send_local_message.assert_awaited_once()


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.level = 0  # Too low for global chat
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_global_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player.level = 1  # Required for global chat
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

    result = await handle_global_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You say (global): Hello" in result["result"]
    mock_chat_service.send_global_message.assert_awaited_once()


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    player_id = uuid.uuid4()
    mock_player.id = player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=False)  # Not admin
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()
    mock_request.app.state.user_manager = mock_user_manager

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_system_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    player_id = uuid.uuid4()
    mock_player.id = player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_user_manager = MagicMock()
    mock_user_manager.is_admin = MagicMock(return_value=True)  # Admin check
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.user_manager = mock_user_manager

    result = await handle_system_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You system: Hello" in result["result"]
    mock_chat_service.send_system_message.assert_awaited_once()
    mock_user_manager.is_admin.assert_called_once_with(player_id)


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, None])
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    player_id = uuid.uuid4()
    mock_player.id = player_id
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_whisper_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You whisper to OtherPlayer: Hello" in result["result"]
    mock_chat_service.send_whisper_message.assert_awaited_once()


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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = MagicMock()
    mock_chat_service.get_last_whisper_sender = MagicMock(return_value=None)
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.get_last_whisper_sender = MagicMock(return_value="OtherPlayer")
    mock_chat_service.send_whisper_message = AsyncMock(return_value={"success": True, "message": {"id": "123"}})
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

    result = await handle_reply_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "You whisper to OtherPlayer: Hello" in result["result"]
    mock_chat_service.send_whisper_message.assert_awaited_once()


@pytest.mark.asyncio
async def test_handle_say_command_no_room():
    """Test handle_say_command when player has no current room."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = None
    mock_player.player_id = None
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_say_message = AsyncMock(return_value={"success": False, "error": "Service unavailable"})
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = "test_room"
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=RuntimeError("Database error"))
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

    result = await handle_say_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Error" in result["result"] or "error" in result["result"].lower()


@pytest.mark.asyncio
async def test_handle_local_command_no_room():
    """Test handle_local_command when player has no current room."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.current_room_id = None
    mock_player.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(return_value=mock_player)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

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
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.resolve_player_name = AsyncMock(return_value=None)
    mock_request.app.state.player_service = mock_player_service
    mock_request.app.state.chat_service = AsyncMock()

    result = await handle_global_command(
        command_data={"message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Player not found" in result["result"]


@pytest.mark.asyncio
async def test_handle_whisper_command_chat_service_failure():
    """Test handle_whisper_command when chat service returns failure."""
    mock_request = MagicMock()
    mock_request.app = MagicMock()
    mock_request.app.state = MagicMock()
    mock_chat_service = AsyncMock()
    mock_chat_service.send_whisper_message = AsyncMock(return_value={"success": False, "error": "Target offline"})
    mock_player_service = AsyncMock()
    mock_sender = MagicMock()
    mock_sender.id = uuid.uuid4()
    mock_target = MagicMock()
    mock_target.id = uuid.uuid4()
    mock_player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    mock_request.app.state.chat_service = mock_chat_service
    mock_request.app.state.player_service = mock_player_service

    result = await handle_whisper_command(
        command_data={"target": "OtherPlayer", "message": "Hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="TestPlayer",
    )

    assert "Error" in result["result"] or "error" in result["result"].lower()
