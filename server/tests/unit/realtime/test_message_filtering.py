"""
Unit tests for message filtering.

Tests the MessageFilteringHelper class.
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from server.realtime.message_filtering import MessageFilteringHelper


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.room_subscriptions = {}
    manager.canonical_room_id = MagicMock(return_value=None)
    return manager


@pytest.fixture
def message_filtering_helper(mock_connection_manager):
    """Create a MessageFilteringHelper instance."""
    return MessageFilteringHelper(mock_connection_manager)


def test_message_filtering_helper_init(message_filtering_helper, mock_connection_manager):
    """Test MessageFilteringHelper initialization."""
    assert message_filtering_helper.connection_manager == mock_connection_manager
    assert message_filtering_helper.user_manager is None


def test_collect_room_targets(message_filtering_helper, mock_connection_manager):
    """Test collect_room_targets() returns subscribed players."""
    mock_connection_manager.room_subscriptions = {"room_001": {"player_001", "player_002"}}
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
    result = message_filtering_helper.collect_room_targets("room_001")
    assert "player_001" in result
    assert "player_002" in result


def test_collect_room_targets_empty(message_filtering_helper, mock_connection_manager):
    """Test collect_room_targets() returns empty set when no subscribers."""
    mock_connection_manager.room_subscriptions = {}
    mock_connection_manager.canonical_room_id = MagicMock(return_value="room_001")
    result = message_filtering_helper.collect_room_targets("room_001")
    assert result == set()


@pytest.mark.asyncio
async def test_preload_receiver_mute_data(message_filtering_helper):
    """Test preload_receiver_mute_data() preloads mute data."""
    mock_user_manager = AsyncMock()
    mock_user_manager.load_player_mutes_batch = AsyncMock(return_value={"player_001": True, "player_002": True})
    targets = {"player_001", "player_002"}
    await message_filtering_helper.preload_receiver_mute_data(mock_user_manager, targets, "sender_001")
    mock_user_manager.load_player_mutes_batch.assert_awaited_once()


@pytest.mark.asyncio
async def test_preload_receiver_mute_data_excludes_sender(message_filtering_helper):
    """Test preload_receiver_mute_data() excludes sender from targets."""
    mock_user_manager = AsyncMock()
    mock_user_manager.load_player_mutes_batch = AsyncMock(return_value={"player_001": True})
    targets = {"player_001", "sender_001"}
    await message_filtering_helper.preload_receiver_mute_data(mock_user_manager, targets, "sender_001")
    # Should only load for player_001, not sender_001
    call_args = mock_user_manager.load_player_mutes_batch.call_args[0][0]
    assert "sender_001" not in call_args
    assert "player_001" in call_args
