"""
Unit tests for whisper command.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.commands.communication_commands import handle_whisper_command


@pytest.fixture
def mock_request():
    """Create a mock request object."""
    app = MagicMock()
    state = MagicMock()
    player_service = MagicMock()
    chat_service = MagicMock()
    state.player_service = player_service
    state.chat_service = chat_service
    app.state = state
    request = MagicMock()
    request.app = app
    return request


@pytest.fixture
def mock_sender():
    """Create a mock sender player."""
    sender = MagicMock()
    sender.id = uuid.uuid4()
    sender.player_id = sender.id
    sender.name = "sender"
    return sender


@pytest.fixture
def mock_target():
    """Create a mock target player."""
    target = MagicMock()
    target.id = uuid.uuid4()
    target.player_id = target.id
    target.name = "target"
    return target


@pytest.mark.asyncio
async def test_whisper_command_missing_target(mock_request):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test whisper command with missing target."""
    result = await handle_whisper_command(
        command_data={"message": "hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "say what" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_whisper_command_missing_message(mock_request):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test whisper command with missing message."""
    result = await handle_whisper_command(
        command_data={"target": "target"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "say what" in result["result"].lower() or "usage" in result["result"].lower()


@pytest.mark.asyncio
async def test_whisper_command_no_player_service(mock_request):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test whisper command when player service is unavailable."""
    mock_request.app.state.player_service = None

    result = await handle_whisper_command(
        command_data={"target": "target", "message": "hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "not available" in result["result"].lower()


@pytest.mark.asyncio
async def test_whisper_command_sender_not_found(mock_request):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter name matches fixture function name, pytest standard pattern
    """Test whisper command when sender not found."""
    mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=None)

    result = await handle_whisper_command(
        command_data={"target": "target", "message": "hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "player not found" in result["result"].lower()


@pytest.mark.asyncio
async def test_whisper_command_target_not_found(mock_request, mock_sender):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test whisper command when target not found."""
    mock_request.app.state.player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, None])

    result = await handle_whisper_command(
        command_data={"target": "nonexistent", "message": "hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "whisper into the aether" in result["result"].lower()


@pytest.mark.asyncio
async def test_whisper_command_whisper_to_self(mock_request, mock_sender):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test whisper command when trying to whisper to self."""
    mock_request.app.state.player_service.resolve_player_name = AsyncMock(return_value=mock_sender)

    result = await handle_whisper_command(
        command_data={"target": "sender", "message": "hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "cannot whisper to yourself" in result["result"].lower()


@pytest.mark.asyncio
async def test_whisper_command_success(mock_request, mock_sender, mock_target):  # pylint: disable=redefined-outer-name  # Reason: Fixture parameter names match fixture function names, pytest standard pattern
    """Test successful whisper command."""
    mock_request.app.state.player_service.resolve_player_name = AsyncMock(side_effect=[mock_sender, mock_target])
    mock_request.app.state.chat_service.send_whisper_message = AsyncMock(
        return_value={"success": True, "message": {"id": "msg123"}}
    )

    result = await handle_whisper_command(
        command_data={"target": "target", "message": "hello"},
        _current_user={},
        request=mock_request,
        _alias_storage=None,
        player_name="sender",
    )

    assert "you whisper to target" in result["result"].lower()
    assert "hello" in result["result"]
