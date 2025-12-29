"""
Unit tests for message queue.

Tests the message_queue module classes and functions.
"""

import time
from datetime import UTC
from unittest.mock import patch

from server.realtime.message_queue import MessageQueue


def test_message_queue_init_defaults():
    """Test MessageQueue.__init__() with default values."""
    queue = MessageQueue()

    assert queue.max_messages_per_player == 1000
    assert queue.pending_messages == {}


def test_message_queue_init_custom():
    """Test MessageQueue.__init__() with custom values."""
    queue = MessageQueue(max_messages_per_player=500)

    assert queue.max_messages_per_player == 500
    assert queue.pending_messages == {}


def test_message_queue_add_message():
    """Test MessageQueue.add_message() adds message successfully."""
    queue = MessageQueue()
    player_id = "player_123"
    message = {"type": "chat", "content": "Hello"}

    with patch("server.realtime.message_queue.logger") as mock_logger:
        result = queue.add_message(player_id, message)

        assert result is True
        assert player_id in queue.pending_messages
        assert len(queue.pending_messages[player_id]) == 1
        assert queue.pending_messages[player_id][0]["type"] == "chat"
        assert "timestamp" in queue.pending_messages[player_id][0]
        mock_logger.debug.assert_called_once()


def test_message_queue_add_message_with_timestamp():
    """Test MessageQueue.add_message() preserves existing timestamp."""
    queue = MessageQueue()
    player_id = "player_123"
    timestamp = 1234567890.0
    message = {"type": "chat", "content": "Hello", "timestamp": timestamp}

    queue.add_message(player_id, message)

    assert queue.pending_messages[player_id][0]["timestamp"] == timestamp


def test_message_queue_add_message_multiple():
    """Test MessageQueue.add_message() adds multiple messages."""
    queue = MessageQueue()
    player_id = "player_123"

    for i in range(5):
        message = {"type": "chat", "content": f"Message {i}"}
        queue.add_message(player_id, message)

    assert len(queue.pending_messages[player_id]) == 5


def test_message_queue_add_message_limit_reached():
    """Test MessageQueue.add_message() drops oldest when limit reached."""
    queue = MessageQueue(max_messages_per_player=3)
    player_id = "player_123"

    # Add 5 messages (exceeds limit of 3)
    for i in range(5):
        message = {"type": "chat", "content": f"Message {i}"}
        queue.add_message(player_id, message)

    # Should only keep the 3 most recent
    assert len(queue.pending_messages[player_id]) == 3
    # First two messages should be dropped
    assert queue.pending_messages[player_id][0]["content"] == "Message 2"
    assert queue.pending_messages[player_id][-1]["content"] == "Message 4"


def test_message_queue_add_message_error():
    """Test MessageQueue.add_message() handles errors."""
    queue = MessageQueue()
    player_id = "player_123"
    # Create a message that will cause an error when adding timestamp
    message = {"type": "chat"}

    # Force an error by making time.time() raise an exception
    with patch("time.time", side_effect=ValueError("Test error")):
        with patch("server.realtime.message_queue.logger") as mock_logger:
            result = queue.add_message(player_id, message)

            assert result is False
            mock_logger.error.assert_called_once()


def test_message_queue_get_messages():
    """Test MessageQueue.get_messages() retrieves and clears messages."""
    queue = MessageQueue()
    player_id = "player_123"

    message1 = {"type": "chat", "content": "Hello"}
    message2 = {"type": "system", "content": "Welcome"}
    queue.add_message(player_id, message1)
    queue.add_message(player_id, message2)

    with patch("server.realtime.message_queue.logger") as mock_logger:
        messages = queue.get_messages(player_id)

        assert len(messages) == 2
        assert messages[0]["content"] == "Hello"
        assert messages[1]["content"] == "Welcome"
        # Queue should be cleared
        assert player_id not in queue.pending_messages
        mock_logger.debug.assert_called_once()


def test_message_queue_get_messages_empty():
    """Test MessageQueue.get_messages() returns empty list for player with no messages."""
    queue = MessageQueue()
    player_id = "player_123"

    messages = queue.get_messages(player_id)

    assert messages == []
    assert player_id not in queue.pending_messages


def test_message_queue_get_messages_error():
    """Test MessageQueue.get_messages() handles errors."""
    queue = MessageQueue()
    player_id = "player_123"
    queue.pending_messages[player_id] = [{"type": "chat"}]

    # Force an error by making del raise an exception
    class ErrorDict(dict):
        def __delitem__(self, key):
            raise KeyError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [{"type": "chat"}]
    queue.pending_messages = error_dict

    with patch("server.realtime.message_queue.logger") as mock_logger:
        messages = queue.get_messages(player_id)

        assert messages == []
        mock_logger.error.assert_called_once()


def test_message_queue_has_messages_true():
    """Test MessageQueue.has_messages() returns True when player has messages."""
    queue = MessageQueue()
    player_id = "player_123"

    queue.add_message(player_id, {"type": "chat", "content": "Hello"})

    assert queue.has_messages(player_id) is True


def test_message_queue_has_messages_false():
    """Test MessageQueue.has_messages() returns False when player has no messages."""
    queue = MessageQueue()
    player_id = "player_123"

    assert queue.has_messages(player_id) is False


def test_message_queue_has_messages_empty_list():
    """Test MessageQueue.has_messages() returns False for empty list."""
    queue = MessageQueue()
    player_id = "player_123"
    queue.pending_messages[player_id] = []

    assert queue.has_messages(player_id) is False


def test_message_queue_get_message_count():
    """Test MessageQueue.get_message_count() returns correct count."""
    queue = MessageQueue()
    player_id = "player_123"

    for i in range(3):
        queue.add_message(player_id, {"type": "chat", "content": f"Message {i}"})

    assert queue.get_message_count(player_id) == 3


def test_message_queue_get_message_count_zero():
    """Test MessageQueue.get_message_count() returns 0 for player with no messages."""
    queue = MessageQueue()
    player_id = "player_123"

    assert queue.get_message_count(player_id) == 0


def test_message_queue_remove_player_messages():
    """Test MessageQueue.remove_player_messages() removes all messages."""
    queue = MessageQueue()
    player_id = "player_123"

    queue.add_message(player_id, {"type": "chat", "content": "Hello"})
    queue.add_message(player_id, {"type": "system", "content": "Welcome"})

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.remove_player_messages(player_id)

        assert player_id not in queue.pending_messages
        mock_logger.debug.assert_called_once()


def test_message_queue_remove_player_messages_not_present():
    """Test MessageQueue.remove_player_messages() handles player not present."""
    queue = MessageQueue()
    player_id = "player_123"

    # Should not raise error if player not in dict
    queue.remove_player_messages(player_id)

    assert player_id not in queue.pending_messages


def test_message_queue_remove_player_messages_error():
    """Test MessageQueue.remove_player_messages() handles errors."""
    queue = MessageQueue()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error on deletion
    class ErrorDict(dict):
        def __delitem__(self, key):
            raise KeyError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [{"type": "chat"}]
    queue.pending_messages = error_dict

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.remove_player_messages(player_id)

        mock_logger.error.assert_called_once()


def test_message_queue_cleanup_old_messages():
    """Test MessageQueue.cleanup_old_messages() removes old messages."""
    queue = MessageQueue()
    player_id = "player_123"

    # Add old and recent messages
    old_time = time.time() - 7200  # 2 hours ago
    recent_time = time.time() - 30  # 30 seconds ago
    queue.pending_messages[player_id] = [
        {"type": "chat", "content": "Old", "timestamp": old_time},
        {"type": "chat", "content": "Recent", "timestamp": recent_time},
    ]

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.cleanup_old_messages(max_age_seconds=3600)

        # Only recent message should remain
        assert len(queue.pending_messages[player_id]) == 1
        assert queue.pending_messages[player_id][0]["content"] == "Recent"
        mock_logger.info.assert_called_once()


def test_message_queue_cleanup_old_messages_removes_empty():
    """Test MessageQueue.cleanup_old_messages() removes empty queues."""
    queue = MessageQueue()
    player_id = "player_123"

    # Add only old messages
    old_time = time.time() - 7200
    queue.pending_messages[player_id] = [{"type": "chat", "content": "Old", "timestamp": old_time}]

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.cleanup_old_messages(max_age_seconds=3600)

        # Player entry should be removed
        assert player_id not in queue.pending_messages
        mock_logger.info.assert_called_once()


def test_message_queue_cleanup_old_messages_string_timestamp():
    """Test MessageQueue.cleanup_old_messages() handles ISO string timestamps."""
    queue = MessageQueue()
    player_id = "player_123"

    # Add message with ISO string timestamp
    from datetime import datetime

    old_dt = datetime.now(UTC).replace(hour=0, minute=0, second=0, microsecond=0)
    old_iso = old_dt.isoformat()
    recent_time = time.time() - 30

    queue.pending_messages[player_id] = [
        {"type": "chat", "content": "Old", "timestamp": old_iso},
        {"type": "chat", "content": "Recent", "timestamp": recent_time},
    ]

    queue.cleanup_old_messages(max_age_seconds=3600)

    # Recent message should remain
    assert len(queue.pending_messages[player_id]) == 1
    assert queue.pending_messages[player_id][0]["content"] == "Recent"


def test_message_queue_cleanup_old_messages_invalid_timestamp():
    """Test MessageQueue.cleanup_old_messages() handles invalid timestamps."""
    queue = MessageQueue()
    player_id = "player_123"

    # Add message with invalid timestamp
    queue.pending_messages[player_id] = [
        {"type": "chat", "content": "Invalid", "timestamp": "not-a-timestamp"},
        {"type": "chat", "content": "Recent", "timestamp": time.time()},
    ]

    queue.cleanup_old_messages(max_age_seconds=3600)

    # Invalid timestamp message should be removed (treated as old)
    assert len(queue.pending_messages[player_id]) == 1
    assert queue.pending_messages[player_id][0]["content"] == "Recent"


def test_message_queue_cleanup_old_messages_error():
    """Test MessageQueue.cleanup_old_messages() handles errors."""
    queue = MessageQueue()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise ValueError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [{"type": "chat", "timestamp": time.time()}]
    queue.pending_messages = error_dict

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.cleanup_old_messages()

        mock_logger.error.assert_called_once()


def test_message_queue_cleanup_large_structures():
    """Test MessageQueue.cleanup_large_structures() trims large queues."""
    queue = MessageQueue()
    player_id = "player_123"

    # Create a large queue
    large_list = [{"type": "chat", "content": f"Message {i}", "timestamp": time.time()} for i in range(2000)]
    queue.pending_messages[player_id] = large_list

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.cleanup_large_structures(max_entries=1000)

        # Should be trimmed to 1000 most recent
        assert len(queue.pending_messages[player_id]) == 1000
        mock_logger.debug.assert_called_once()


def test_message_queue_cleanup_large_structures_error():
    """Test MessageQueue.cleanup_large_structures() handles errors."""
    queue = MessageQueue()
    player_id = "player_123"

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise TypeError("Test error")

    error_dict = ErrorDict()
    error_dict[player_id] = [{"type": "chat", "timestamp": time.time()}]
    queue.pending_messages = error_dict

    with patch("server.realtime.message_queue.logger") as mock_logger:
        queue.cleanup_large_structures()

        mock_logger.error.assert_called_once()


def test_message_queue_get_stats():
    """Test MessageQueue.get_stats() returns statistics."""
    queue = MessageQueue()
    player_id1 = "player_123"
    player_id2 = "player_456"

    queue.add_message(player_id1, {"type": "chat", "content": "Hello"})
    queue.add_message(player_id1, {"type": "system", "content": "Welcome"})
    queue.add_message(player_id2, {"type": "chat", "content": "Hi"})

    stats = queue.get_stats()

    assert stats["total_queues"] == 2
    assert stats["total_messages"] == 3
    assert stats["max_messages_per_player"] == 1000
    assert len(stats["largest_queues"]) == 2
    assert stats["average_queue_size"] == 1.5


def test_message_queue_get_stats_empty():
    """Test MessageQueue.get_stats() handles empty state."""
    queue = MessageQueue()

    stats = queue.get_stats()

    assert stats["total_queues"] == 0
    assert stats["total_messages"] == 0
    assert stats["average_queue_size"] == 0


def test_message_queue_get_stats_error():
    """Test MessageQueue.get_stats() handles errors."""
    queue = MessageQueue()

    # Create a custom dict-like object that raises an error
    class ErrorDict(dict):
        def items(self):
            raise KeyError("Test error")

    error_dict = ErrorDict()
    error_dict["player_123"] = [{"type": "chat"}]
    queue.pending_messages = error_dict

    with patch("server.realtime.message_queue.logger") as mock_logger:
        stats = queue.get_stats()

        assert stats == {}
        mock_logger.error.assert_called_once()
