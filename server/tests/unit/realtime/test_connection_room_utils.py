"""
Unit tests for connection room utils.

Tests the connection_room_utils module functions.
"""

import uuid
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from server.realtime.connection_room_utils import (
    canonical_room_id_impl,
    prune_player_from_all_rooms_impl,
    reconcile_room_presence_impl,
)


def test_canonical_room_id_impl_none():
    """Test canonical_room_id_impl() returns None when room_id is None."""
    mock_manager = MagicMock()

    result = canonical_room_id_impl(None, mock_manager)

    assert result is None


def test_canonical_room_id_impl_empty_string():
    """Test canonical_room_id_impl() returns empty string when room_id is empty."""
    mock_manager = MagicMock()

    result = canonical_room_id_impl("", mock_manager)

    assert result == ""


def test_canonical_room_id_impl_success_room_manager():
    """Test canonical_room_id_impl() resolves room ID from room_manager persistence."""
    room_id = "room_123"
    canonical_id = "canonical_room_123"
    mock_manager = MagicMock()
    mock_room = MagicMock()
    mock_room.id = canonical_id
    mock_manager.room_manager.async_persistence = MagicMock()
    mock_manager.room_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = canonical_room_id_impl(room_id, mock_manager)

    assert result == canonical_id
    mock_manager.room_manager.async_persistence.get_room_by_id.assert_called_once_with(room_id)


def test_canonical_room_id_impl_fallback_to_main_persistence():
    """Test canonical_room_id_impl() falls back to main persistence."""
    room_id = "room_123"
    canonical_id = "canonical_room_123"
    mock_manager = MagicMock()
    mock_manager.room_manager.async_persistence = None
    mock_room = MagicMock()
    mock_room.id = canonical_id
    mock_manager.async_persistence = MagicMock()
    mock_manager.async_persistence.get_room_by_id = MagicMock(return_value=mock_room)

    result = canonical_room_id_impl(room_id, mock_manager)

    assert result == canonical_id
    mock_manager.async_persistence.get_room_by_id.assert_called_once_with(room_id)


def test_canonical_room_id_impl_no_room_found():
    """Test canonical_room_id_impl() returns original room_id when room not found."""
    room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.room_manager.async_persistence = MagicMock()
    mock_manager.room_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)
    mock_manager.async_persistence = MagicMock()
    mock_manager.async_persistence.get_room_by_id = MagicMock(return_value=None)

    result = canonical_room_id_impl(room_id, mock_manager)

    assert result == room_id


def test_canonical_room_id_impl_room_no_id_attribute():
    """Test canonical_room_id_impl() returns original room_id when room has no id."""
    room_id = "room_123"
    # Create a real room object that doesn't have an id attribute
    # The source code uses getattr(room, "id", None), so we need a room without id
    class RoomWithoutId:
        pass

    room_without_id = RoomWithoutId()
    # Ensure it doesn't have id attribute
    assert not hasattr(room_without_id, "id")
    assert getattr(room_without_id, "id", None) is None
    # Create a real persistence object (not MagicMock) to avoid auto-attribute creation
    class MockPersistence:
        def get_room_by_id(self, room_id):
            return room_without_id

    # Create a real room_manager object (not MagicMock)
    class MockRoomManager:
        def __init__(self):
            self.async_persistence = MockPersistence()

    # Use a simple object instead of MagicMock to avoid auto-attribute creation
    class MockManager:
        def __init__(self):
            self.room_manager = MockRoomManager()

    mock_manager = MockManager()

    result = canonical_room_id_impl(room_id, mock_manager)

    # When room has no id, getattr(room, "id", None) returns None, so original room_id is returned
    assert result == room_id


def test_canonical_room_id_impl_database_error():
    """Test canonical_room_id_impl() handles DatabaseError."""
    from server.exceptions import DatabaseError

    room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.room_manager.async_persistence = MagicMock()
    mock_manager.room_manager.async_persistence.get_room_by_id = MagicMock(side_effect=DatabaseError("DB error"))

    result = canonical_room_id_impl(room_id, mock_manager)

    assert result == room_id


def test_canonical_room_id_impl_attribute_error():
    """Test canonical_room_id_impl() handles AttributeError."""
    room_id = "room_123"
    mock_manager = MagicMock()
    del mock_manager.room_manager  # Cause AttributeError

    result = canonical_room_id_impl(room_id, mock_manager)

    assert result == room_id


def test_reconcile_room_presence_impl():
    """Test reconcile_room_presence_impl() calls room_manager.reconcile_room_presence()."""
    room_id = "room_123"
    mock_manager = MagicMock()
    mock_manager.online_players = {"player_1": {"name": "Player1"}, "player_2": {"name": "Player2"}}
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.reconcile_room_presence = MagicMock()

    reconcile_room_presence_impl(room_id, mock_manager)

    mock_manager.room_manager.reconcile_room_presence.assert_called_once()
    call_args = mock_manager.room_manager.reconcile_room_presence.call_args
    assert call_args[0][0] == room_id
    assert "player_1" in call_args[0][1]
    assert "player_2" in call_args[0][1]


def test_prune_player_from_all_rooms_impl():
    """Test prune_player_from_all_rooms_impl() calls room_manager.remove_player_from_all_rooms()."""
    player_id = uuid.uuid4()
    mock_manager = MagicMock()
    mock_manager.room_manager = MagicMock()
    mock_manager.room_manager.remove_player_from_all_rooms = MagicMock()

    prune_player_from_all_rooms_impl(player_id, mock_manager)

    mock_manager.room_manager.remove_player_from_all_rooms.assert_called_once_with(str(player_id))
