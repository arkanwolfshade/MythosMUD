"""
Unit tests for chat service.

Tests the ChatService class and ChatMessage class.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock

import pytest

from server.game.chat_service import ChatMessage, ChatService


def test_chat_message_init():
    """Test ChatMessage initialization."""
    player_id = uuid.uuid4()
    message = ChatMessage(player_id, "TestPlayer", "say", "Hello world")
    assert message.sender_id == str(player_id)
    assert message.sender_name == "TestPlayer"
    assert message.channel == "say"
    assert message.content == "Hello world"
    assert message.target_id is None
    assert message.target_name is None


def test_chat_message_init_with_target():
    """Test ChatMessage initialization with target."""
    sender_id = uuid.uuid4()
    target_id = uuid.uuid4()
    message = ChatMessage(sender_id, "TestPlayer", "whisper", "Hello", target_id, "OtherPlayer")
    assert message.sender_id == str(sender_id)
    assert message.target_id == str(target_id)
    assert message.target_name == "OtherPlayer"


def test_chat_message_to_dict():
    """Test ChatMessage.to_dict() conversion."""
    player_id = uuid.uuid4()
    message = ChatMessage(player_id, "TestPlayer", "say", "Hello world")
    result = message.to_dict()
    assert result["sender_id"] == str(player_id)
    assert result["sender_name"] == "TestPlayer"
    assert result["channel"] == "say"
    assert result["content"] == "Hello world"
    assert "timestamp" in result


def test_chat_message_to_dict_with_target():
    """Test ChatMessage.to_dict() with target."""
    sender_id = uuid.uuid4()
    target_id = uuid.uuid4()
    message = ChatMessage(sender_id, "TestPlayer", "whisper", "Hello", target_id, "OtherPlayer")
    result = message.to_dict()
    assert result["target_id"] == str(target_id)
    assert result["target_name"] == "OtherPlayer"


def test_chat_service_init():
    """Test ChatService initialization."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    assert service.persistence == mock_persistence
    assert service.room_service == mock_room_service
    assert service.player_service == mock_player_service


@pytest.mark.asyncio
async def test_send_say_message_empty():
    """Test send_say_message() with empty message."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    result = await service.send_say_message(uuid.uuid4(), "")
    assert result["success"] is False
    assert "empty" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_say_message_too_long():
    """Test send_say_message() with message too long."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    long_message = "a" * 501
    result = await service.send_say_message(uuid.uuid4(), long_message)
    assert result["success"] is False
    assert "too long" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_say_message_player_not_found():
    """Test send_say_message() when player is not found."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = AsyncMock()
    mock_player_service.get_player_by_id = AsyncMock(return_value=None)
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    result = await service.send_say_message(uuid.uuid4(), "Hello")
    assert result["success"] is False
    assert "not found" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_say_message_rate_limited():
    """Test send_say_message() when rate limited."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = "room_001"
    mock_player_service.get_player_by_id = AsyncMock(return_value=mock_player)
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    service.rate_limiter.check_rate_limit = MagicMock(return_value=False)
    result = await service.send_say_message(uuid.uuid4(), "Hello")
    assert result["success"] is False
    assert "rate limit" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_say_message_no_room():
    """Test send_say_message() when player is not in a room."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    mock_player.current_room_id = None
    mock_player_service.get_player_by_id = AsyncMock(return_value=mock_player)
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    service.rate_limiter.check_rate_limit = MagicMock(return_value=True)
    result = await service.send_say_message(uuid.uuid4(), "Hello")
    assert result["success"] is False
    assert "not in a room" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_local_message_empty():
    """Test send_local_message() with empty message."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    result = await service.send_local_message(uuid.uuid4(), "")
    assert result["success"] is False
    assert "empty" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_global_message_empty():
    """Test send_global_message() with empty message."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    result = await service.send_global_message(uuid.uuid4(), "")
    assert result["success"] is False
    assert "empty" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_emote_message_empty():
    """Test send_emote_message() with empty action."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    result = await service.send_emote_message(uuid.uuid4(), "")
    assert result["success"] is False
    assert "empty" in result["error"].lower()


@pytest.mark.asyncio
async def test_send_whisper_message_no_target():
    """Test send_whisper_message() with no target."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = AsyncMock()
    mock_player = MagicMock()
    mock_player.name = "TestPlayer"
    # First call returns sender, second call (for target) returns None
    mock_player_service.get_player_by_id = AsyncMock(side_effect=[mock_player, None])
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    service.rate_limiter.check_rate_limit = MagicMock(return_value=True)
    result = await service.send_whisper_message(uuid.uuid4(), None, "Hello")
    assert result["success"] is False
    assert "target" in result["error"].lower() or "not found" in result["error"].lower()


@pytest.mark.asyncio
async def test_get_last_whisper_sender():
    """Test get_last_whisper_sender() returns last sender."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    service._last_whisper_senders["TestPlayer"] = "OtherPlayer"
    result = service.get_last_whisper_sender("TestPlayer")
    assert result == "OtherPlayer"


@pytest.mark.asyncio
async def test_get_last_whisper_sender_none():
    """Test get_last_whisper_sender() returns None when no sender."""
    mock_persistence = MagicMock()
    mock_room_service = MagicMock()
    mock_player_service = MagicMock()
    service = ChatService(mock_persistence, mock_room_service, mock_player_service)
    result = service.get_last_whisper_sender("TestPlayer")
    assert result is None
