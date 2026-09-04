"""
Unit tests for message filtering helper functions.

Tests the helper functions in message_filtering.py.
"""

from unittest.mock import MagicMock

import pytest

from server.realtime.message_filtering import MessageFilteringHelper


@pytest.fixture
def mock_connection_manager():
    """Create a mock connection manager."""
    manager = MagicMock()
    manager.room_subscriptions = {}
    manager.canonical_room_id = MagicMock(return_value=None)
    manager.online_players = {}
    return manager


@pytest.fixture
def message_filtering_helper(mock_connection_manager):
    """Create a MessageFilteringHelper instance."""
    return MessageFilteringHelper(mock_connection_manager)


def test_extract_chat_event_info(message_filtering_helper):
    """Test extract_chat_event_info() extracts event information."""
    chat_event = {"event_type": "say", "data": {"id": "msg_001", "echo_sent": True}}
    event_type, chat_event_data, message_id, sender_notified = message_filtering_helper.extract_chat_event_info(
        chat_event
    )
    assert event_type == "say"
    assert message_id == "msg_001"
    assert sender_notified is True


def test_should_apply_mute_check(message_filtering_helper):
    """Test should_apply_mute_check() determines if mute check needed."""
    assert message_filtering_helper.should_apply_mute_check("say", "msg_001") is True
    assert message_filtering_helper.should_apply_mute_check("say", None) is True
    assert message_filtering_helper.should_apply_mute_check("other", "msg_001") is False


def test_compare_canonical_rooms(message_filtering_helper, mock_connection_manager):
    """Test compare_canonical_rooms() compares room IDs."""
    mock_connection_manager.canonical_room_id = MagicMock(side_effect=lambda x: x)
    result = message_filtering_helper.compare_canonical_rooms("room_001", "room_001")
    assert result is True


def test_get_player_room_from_online_players(message_filtering_helper, mock_connection_manager):
    """Test get_player_room_from_online_players() gets room from cache."""
    mock_connection_manager.online_players = {"player_001": {"current_room_id": "room_001"}}
    result = message_filtering_helper.get_player_room_from_online_players("player_001")
    assert result == "room_001"


def test_get_player_room_from_online_players_not_found(message_filtering_helper, mock_connection_manager):
    """Test get_player_room_from_online_players() returns None when not found."""
    mock_connection_manager.online_players = {}
    result = message_filtering_helper.get_player_room_from_online_players("player_001")
    assert result is None
