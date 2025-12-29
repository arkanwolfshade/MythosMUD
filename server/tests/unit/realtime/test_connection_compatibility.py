"""
Unit tests for connection compatibility.

Tests the connection_compatibility module functions.
"""

from unittest.mock import MagicMock

import pytest

from server.realtime.connection_compatibility import attach_compatibility_properties


def test_attach_compatibility_properties_room_subscriptions():
    """Test attach_compatibility_properties() attaches room_subscriptions property."""
    mock_class = type("TestClass", (), {})
    mock_manager = MagicMock()
    mock_subscriptions = MagicMock()
    mock_subscriptions.clear = MagicMock()
    mock_manager.room_manager.room_subscriptions = mock_subscriptions

    attach_compatibility_properties(mock_class)

    # Test getter
    result = mock_class.room_subscriptions.fget(mock_manager)
    assert result == mock_subscriptions

    # Test setter
    new_value = {"room_2": ["player_2"]}
    mock_class.room_subscriptions.fset(mock_manager, new_value)
    assert mock_manager.room_manager.room_subscriptions == new_value

    # Test deleter - it calls clear() on the object stored in room_manager
    mock_manager.room_manager.room_subscriptions = MagicMock()
    mock_manager.room_manager.room_subscriptions.clear = MagicMock()
    mock_class.room_subscriptions.fdel(mock_manager)
    mock_manager.room_manager.room_subscriptions.clear.assert_called_once()


def test_attach_compatibility_properties_room_occupants():
    """Test attach_compatibility_properties() attaches room_occupants property."""
    mock_class = type("TestClass", (), {})
    mock_manager = MagicMock()
    mock_occupants = MagicMock()
    mock_occupants.clear = MagicMock()
    mock_manager.room_manager.room_occupants = mock_occupants

    attach_compatibility_properties(mock_class)

    # Test getter
    result = mock_class.room_occupants.fget(mock_manager)
    assert result == mock_occupants

    # Test setter
    new_value = {"room_2": ["player_2"]}
    mock_class.room_occupants.fset(mock_manager, new_value)
    assert mock_manager.room_manager.room_occupants == new_value

    # Test deleter - it calls clear() on the object stored in room_manager
    mock_manager.room_manager.room_occupants = MagicMock()
    mock_manager.room_manager.room_occupants.clear = MagicMock()
    mock_class.room_occupants.fdel(mock_manager)
    mock_manager.room_manager.room_occupants.clear.assert_called_once()


def test_attach_compatibility_properties_connection_attempts():
    """Test attach_compatibility_properties() attaches connection_attempts property."""
    mock_class = type("TestClass", (), {})
    mock_manager = MagicMock()
    mock_attempts = MagicMock()
    mock_attempts.clear = MagicMock()
    mock_manager.rate_limiter.connection_attempts = mock_attempts

    attach_compatibility_properties(mock_class)

    # Test getter
    result = mock_class.connection_attempts.fget(mock_manager)
    assert result == mock_attempts

    # Test setter
    new_value = {"ip_2": 3}
    mock_class.connection_attempts.fset(mock_manager, new_value)
    assert mock_manager.rate_limiter.connection_attempts == new_value

    # Test deleter - reset to a mock object with clear method before testing deleter
    mock_clearable = MagicMock()
    mock_clearable.clear = MagicMock()
    mock_manager.rate_limiter.connection_attempts = mock_clearable
    mock_class.connection_attempts.fdel(mock_manager)
    mock_clearable.clear.assert_called_once()


def test_attach_compatibility_properties_pending_messages():
    """Test attach_compatibility_properties() attaches pending_messages property."""
    mock_class = type("TestClass", (), {})
    mock_manager = MagicMock()
    mock_messages = MagicMock()
    mock_messages.clear = MagicMock()
    mock_manager.message_queue.pending_messages = mock_messages

    attach_compatibility_properties(mock_class)

    # Test getter
    result = mock_class.pending_messages.fget(mock_manager)
    assert result == mock_messages

    # Test setter
    new_value = ["msg_3"]
    mock_class.pending_messages.fset(mock_manager, new_value)
    assert mock_manager.message_queue.pending_messages == new_value

    # Test deleter - it calls clear() on the object stored in message_queue
    mock_manager.message_queue.pending_messages = MagicMock()
    mock_manager.message_queue.pending_messages.clear = MagicMock()
    mock_class.pending_messages.fdel(mock_manager)
    mock_manager.message_queue.pending_messages.clear.assert_called_once()


def test_attach_compatibility_properties_max_connection_attempts():
    """Test attach_compatibility_properties() attaches max_connection_attempts property."""
    mock_class = type("TestClass", (), {})
    mock_manager = MagicMock()
    mock_manager.rate_limiter.max_connection_attempts = 10

    attach_compatibility_properties(mock_class)

    result = mock_class.max_connection_attempts.fget(mock_manager)
    assert result == 10


def test_attach_compatibility_properties_connection_window():
    """Test attach_compatibility_properties() attaches connection_window property."""
    mock_class = type("TestClass", (), {})
    mock_manager = MagicMock()
    mock_manager.rate_limiter.connection_window = 60

    attach_compatibility_properties(mock_class)

    result = mock_class.connection_window.fget(mock_manager)
    assert result == 60
