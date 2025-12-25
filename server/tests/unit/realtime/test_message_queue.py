"""
Unit tests for the MessageQueue class.

These tests verify the message queuing functionality for guaranteed delivery
of messages to players who may be temporarily disconnected.

AI: Tests cover all public methods, edge cases, error handling, and memory management.
"""

import time
from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

from server.realtime.message_queue import MessageQueue


class TestMessageQueueInitialization:
    """Test initialization of MessageQueue."""

    def test_init_default_max_messages(self) -> None:
        """Test initialization with default max_messages_per_player."""
        queue = MessageQueue()
        assert queue.max_messages_per_player == 1000
        assert queue.pending_messages == {}

    def test_init_custom_max_messages(self) -> None:
        """Test initialization with custom max_messages_per_player."""
        queue = MessageQueue(max_messages_per_player=500)
        assert queue.max_messages_per_player == 500
        assert queue.pending_messages == {}


class TestAddMessage:
    """Test message addition to the queue."""

    def test_add_message_creates_player_queue(self) -> None:
        """Test that add_message creates a new queue for a new player."""
        queue = MessageQueue()
        message = {"type": "chat", "content": "Hello from the void"}

        result = queue.add_message("player1", message)

        assert result is True
        assert "player1" in queue.pending_messages
        assert len(queue.pending_messages["player1"]) == 1
        assert "timestamp" in queue.pending_messages["player1"][0]

    def test_add_message_with_existing_timestamp(self) -> None:
        """Test that add_message preserves existing timestamp."""
        queue = MessageQueue()
        custom_timestamp = time.time() - 100
        message = {"type": "chat", "content": "Old message", "timestamp": custom_timestamp}

        queue.add_message("player1", message)

        assert queue.pending_messages["player1"][0]["timestamp"] == custom_timestamp

    def test_add_message_without_timestamp(self) -> None:
        """Test that add_message adds timestamp if not present."""
        queue = MessageQueue()
        message = {"type": "chat", "content": "Message without timestamp"}

        before = time.time()
        queue.add_message("player1", message)
        after = time.time()

        timestamp = queue.pending_messages["player1"][0]["timestamp"]
        assert before <= timestamp <= after

    def test_add_multiple_messages_to_same_player(self) -> None:
        """Test adding multiple messages to the same player."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "First message"})
        queue.add_message("player1", {"content": "Second message"})
        queue.add_message("player1", {"content": "Third message"})

        assert len(queue.pending_messages["player1"]) == 3

    def test_add_message_exceeds_limit(self) -> None:
        """Test that exceeding max_messages_per_player drops oldest messages."""
        queue = MessageQueue(max_messages_per_player=3)

        # Add 5 messages, should keep only the last 3
        for i in range(5):
            queue.add_message("player1", {"content": f"Message {i}"})

        messages = queue.pending_messages["player1"]
        assert len(messages) == 3
        assert messages[0]["content"] == "Message 2"
        assert messages[1]["content"] == "Message 3"
        assert messages[2]["content"] == "Message 4"

    def test_add_message_logs_warning_on_limit(self) -> None:
        """Test that add_message logs warning when limit is reached."""
        queue = MessageQueue(max_messages_per_player=2)

        # Add 3 messages to trigger warning
        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.add_message("player1", {"content": "Message 3"})
            mock_logger.warning.assert_called_once()

    def test_add_message_exception_handling(self) -> None:
        """Test error handling when add_message encounters an exception."""
        queue = MessageQueue()

        # Create a mock that raises a specific exception when accessed
        with patch.object(queue, "pending_messages", new_callable=MagicMock) as mock_dict:
            mock_dict.__contains__.side_effect = ValueError("Simulated error")

            result = queue.add_message("player1", {"content": "Test"})

            assert result is False

    def test_add_message_logs_debug_on_success(self) -> None:
        """Test that add_message logs debug message on success."""
        queue = MessageQueue()

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.add_message("player1", {"content": "Test"})
            mock_logger.debug.assert_called_with("Added message to queue", player_id="player1")


class TestGetMessages:
    """Test retrieving messages from the queue."""

    def test_get_messages_returns_all_messages(self) -> None:
        """Test that get_messages returns all pending messages for a player."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})

        messages = queue.get_messages("player1")

        assert len(messages) == 2
        assert messages[0]["content"] == "Message 1"
        assert messages[1]["content"] == "Message 2"

    def test_get_messages_clears_queue(self) -> None:
        """Test that get_messages clears the player's queue."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "Message 1"})
        queue.get_messages("player1")

        assert "player1" not in queue.pending_messages

    def test_get_messages_for_nonexistent_player(self) -> None:
        """Test that get_messages returns empty list for nonexistent player."""
        queue = MessageQueue()

        messages = queue.get_messages("nonexistent")

        assert messages == []

    def test_get_messages_logs_debug_on_retrieval(self) -> None:
        """Test that get_messages logs debug message when retrieving messages."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.get_messages("player1")
            mock_logger.debug.assert_called_with("Retrieved and cleared messages", message_count=1, player_id="player1")

    def test_get_messages_exception_handling(self) -> None:
        """Test error handling when get_messages encounters an exception."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        # Simulate exception by replacing the entire dict with a mock
        original_pending = queue.pending_messages
        try:
            mock_dict = MagicMock()
            mock_dict.get.side_effect = ValueError("Simulated error")
            mock_dict.__contains__ = lambda self, key: True
            queue.pending_messages = mock_dict

            messages = queue.get_messages("player1")
            assert messages == []
        finally:
            queue.pending_messages = original_pending


class TestHasMessages:
    """Test checking if a player has pending messages."""

    def test_has_messages_true(self) -> None:
        """Test has_messages returns True when player has messages."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        assert queue.has_messages("player1") is True

    def test_has_messages_false_nonexistent_player(self) -> None:
        """Test has_messages returns False for nonexistent player."""
        queue = MessageQueue()

        assert queue.has_messages("nonexistent") is False

    def test_has_messages_false_empty_queue(self) -> None:
        """Test has_messages returns False when queue is empty."""
        queue = MessageQueue()
        queue.pending_messages["player1"] = []

        assert queue.has_messages("player1") is False


class TestGetMessageCount:
    """Test getting the count of pending messages."""

    def test_get_message_count_zero(self) -> None:
        """Test get_message_count returns 0 for nonexistent player."""
        queue = MessageQueue()

        assert queue.get_message_count("nonexistent") == 0

    def test_get_message_count_multiple(self) -> None:
        """Test get_message_count returns correct count."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})
        queue.add_message("player1", {"content": "Message 3"})

        assert queue.get_message_count("player1") == 3


class TestRemovePlayerMessages:
    """Test removing all messages for a specific player."""

    def test_remove_player_messages_success(self) -> None:
        """Test that remove_player_messages deletes all player messages."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})

        queue.remove_player_messages("player1")

        assert "player1" not in queue.pending_messages

    def test_remove_player_messages_nonexistent_player(self) -> None:
        """Test remove_player_messages handles nonexistent player gracefully."""
        queue = MessageQueue()

        # Should not raise an exception
        queue.remove_player_messages("nonexistent")

    def test_remove_player_messages_logs_debug(self) -> None:
        """Test that remove_player_messages logs debug message."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.remove_player_messages("player1")
            mock_logger.debug.assert_called_with("Removed all pending messages", player_id="player1")

    def test_remove_player_messages_exception_handling(self) -> None:
        """Test error handling when remove_player_messages encounters an exception."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        # Simulate exception by replacing the entire dict with a mock
        original_pending = queue.pending_messages
        try:
            mock_dict = MagicMock()
            mock_dict.__contains__ = lambda self, key: True
            mock_dict.__delitem__.side_effect = KeyError("Simulated error")
            queue.pending_messages = mock_dict

            # Should not raise exception
            queue.remove_player_messages("player1")
        finally:
            queue.pending_messages = original_pending


class TestCleanupOldMessages:
    """Test cleanup of old messages."""

    def test_cleanup_old_messages_removes_old(self) -> None:
        """Test that cleanup_old_messages removes messages older than max_age."""
        queue = MessageQueue()

        old_time = time.time() - 7200  # 2 hours ago
        recent_time = time.time() - 100  # Recent

        queue.add_message("player1", {"content": "Old message", "timestamp": old_time})
        queue.add_message("player1", {"content": "Recent message", "timestamp": recent_time})

        queue.cleanup_old_messages(max_age_seconds=3600)  # 1 hour

        messages = queue.pending_messages["player1"]
        assert len(messages) == 1
        assert messages[0]["content"] == "Recent message"

    def test_cleanup_old_messages_removes_empty_queues(self) -> None:
        """Test that cleanup_old_messages removes empty player queues."""
        queue = MessageQueue()

        old_time = time.time() - 7200  # 2 hours ago
        queue.add_message("player1", {"content": "Old message", "timestamp": old_time})

        queue.cleanup_old_messages(max_age_seconds=3600)

        assert "player1" not in queue.pending_messages

    def test_cleanup_old_messages_logs_info(self) -> None:
        """Test that cleanup_old_messages logs info when cleaning up."""
        queue = MessageQueue()

        old_time = time.time() - 7200
        queue.add_message("player1", {"content": "Old message", "timestamp": old_time})

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.cleanup_old_messages(max_age_seconds=3600)
            mock_logger.info.assert_called_once()

    def test_cleanup_old_messages_no_changes(self) -> None:
        """Test that cleanup_old_messages handles case with no changes."""
        queue = MessageQueue()

        recent_time = time.time() - 100
        queue.add_message("player1", {"content": "Recent message", "timestamp": recent_time})

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.cleanup_old_messages(max_age_seconds=3600)
            # Should not log info if nothing was removed
            mock_logger.info.assert_not_called()

    def test_cleanup_old_messages_exception_handling(self) -> None:
        """Test error handling when cleanup_old_messages encounters an exception."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        # Simulate exception by replacing the entire dict with a mock
        original_pending = queue.pending_messages
        try:
            mock_dict = MagicMock()
            mock_dict.items.side_effect = TypeError("Simulated error")
            queue.pending_messages = mock_dict

            # Should not raise exception
            queue.cleanup_old_messages()
        finally:
            queue.pending_messages = original_pending


class TestCleanupLargeStructures:
    """Test cleanup of large data structures."""

    def test_cleanup_large_structures_trims_excess(self) -> None:
        """Test that cleanup_large_structures trims queues exceeding max_entries."""
        queue = MessageQueue()

        # Add 150 messages
        for i in range(150):
            queue.add_message("player1", {"content": f"Message {i}"})

        queue.cleanup_large_structures(max_entries=100)

        messages = queue.pending_messages["player1"]
        assert len(messages) == 100
        # Should keep the most recent messages
        assert messages[0]["content"] == "Message 50"
        assert messages[-1]["content"] == "Message 149"

    def test_cleanup_large_structures_no_change_under_limit(self) -> None:
        """Test that cleanup_large_structures doesn't change queues under limit."""
        queue = MessageQueue()

        for i in range(50):
            queue.add_message("player1", {"content": f"Message {i}"})

        queue.cleanup_large_structures(max_entries=100)

        assert len(queue.pending_messages["player1"]) == 50

    def test_cleanup_large_structures_logs_debug(self) -> None:
        """Test that cleanup_large_structures logs debug message when trimming."""
        queue = MessageQueue()

        for i in range(150):
            queue.add_message("player1", {"content": f"Message {i}"})

        with patch("server.realtime.message_queue.logger") as mock_logger:
            queue.cleanup_large_structures(max_entries=100)
            mock_logger.debug.assert_called_once()

    def test_cleanup_large_structures_exception_handling(self) -> None:
        """Test error handling when cleanup_large_structures encounters an exception."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        # Simulate exception by replacing the entire dict with a mock
        original_pending = queue.pending_messages
        try:
            mock_dict = MagicMock()
            mock_dict.items.side_effect = TypeError("Simulated error")
            queue.pending_messages = mock_dict

            # Should not raise exception
            queue.cleanup_large_structures()
        finally:
            queue.pending_messages = original_pending


class TestIsMessageRecent:
    """Test timestamp validation for messages."""

    def test_is_message_recent_with_float_timestamp(self) -> None:
        """Test _is_message_recent with float timestamp."""
        queue = MessageQueue()

        current_time = time.time()
        msg = {"timestamp": current_time - 100}  # 100 seconds ago

        assert queue._is_message_recent(msg, current_time, 3600) is True

    def test_is_message_recent_with_int_timestamp(self) -> None:
        """Test _is_message_recent with int timestamp."""
        queue = MessageQueue()

        current_time = time.time()
        msg = {"timestamp": int(current_time - 100)}  # 100 seconds ago

        assert queue._is_message_recent(msg, current_time, 3600) is True

    def test_is_message_recent_with_iso_timestamp(self) -> None:
        """Test _is_message_recent with ISO format timestamp."""
        queue = MessageQueue()

        current_time = time.time()
        past_datetime = datetime.fromtimestamp(current_time - 100, tz=UTC)
        iso_timestamp = past_datetime.isoformat()

        msg = {"timestamp": iso_timestamp}

        assert queue._is_message_recent(msg, current_time, 3600) is True

    def test_is_message_recent_with_iso_timestamp_z_suffix(self) -> None:
        """Test _is_message_recent with ISO format timestamp ending in Z."""
        queue = MessageQueue()

        current_time = time.time()
        past_datetime = datetime.fromtimestamp(current_time - 100, tz=UTC)
        iso_timestamp = past_datetime.isoformat().replace("+00:00", "Z")

        msg = {"timestamp": iso_timestamp}

        assert queue._is_message_recent(msg, current_time, 3600) is True

    def test_is_message_recent_old_message(self) -> None:
        """Test _is_message_recent returns False for old message."""
        queue = MessageQueue()

        current_time = time.time()
        msg = {"timestamp": current_time - 7200}  # 2 hours ago

        assert queue._is_message_recent(msg, current_time, 3600) is False

    def test_is_message_recent_no_timestamp(self) -> None:
        """Test _is_message_recent returns False when no timestamp present."""
        queue = MessageQueue()

        current_time = time.time()
        msg = {"content": "No timestamp"}

        assert queue._is_message_recent(msg, current_time, 3600) is False

    def test_is_message_recent_invalid_string_timestamp(self) -> None:
        """Test _is_message_recent returns False for invalid string timestamp."""
        queue = MessageQueue()

        current_time = time.time()
        msg = {"timestamp": "not a valid timestamp"}

        assert queue._is_message_recent(msg, current_time, 3600) is False

    def test_is_message_recent_invalid_type_timestamp(self) -> None:
        """Test _is_message_recent returns False for invalid timestamp type."""
        queue = MessageQueue()

        current_time = time.time()
        msg = {"timestamp": ["invalid", "type"]}

        assert queue._is_message_recent(msg, current_time, 3600) is False

    def test_is_message_recent_exception_handling(self) -> None:
        """Test _is_message_recent returns False on exception."""
        queue = MessageQueue()

        current_time = time.time()
        # Create a message with a mock timestamp that raises exception
        msg = {"timestamp": MagicMock(side_effect=Exception("Simulated error"))}

        assert queue._is_message_recent(msg, current_time, 3600) is False


class TestGetStats:
    """Test getting statistics about the message queue."""

    def test_get_stats_empty_queue(self) -> None:
        """Test get_stats with empty queue."""
        queue = MessageQueue()

        stats = queue.get_stats()

        assert stats["total_queues"] == 0
        assert stats["total_messages"] == 0
        assert stats["average_queue_size"] == 0
        assert stats["largest_queues"] == []

    def test_get_stats_single_player(self) -> None:
        """Test get_stats with single player."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})

        stats = queue.get_stats()

        assert stats["total_queues"] == 1
        assert stats["total_messages"] == 2
        assert stats["average_queue_size"] == 2
        assert stats["largest_queues"] == [("player1", 2)]

    def test_get_stats_multiple_players(self) -> None:
        """Test get_stats with multiple players."""
        queue = MessageQueue()

        # Add different numbers of messages for each player
        for i in range(5):
            queue.add_message("player1", {"content": f"Message {i}"})

        for i in range(3):
            queue.add_message("player2", {"content": f"Message {i}"})

        for i in range(1):
            queue.add_message("player3", {"content": f"Message {i}"})

        stats = queue.get_stats()

        assert stats["total_queues"] == 3
        assert stats["total_messages"] == 9
        assert stats["average_queue_size"] == 3
        # Should be sorted by size, descending
        assert stats["largest_queues"][0] == ("player1", 5)
        assert stats["largest_queues"][1] == ("player2", 3)
        assert stats["largest_queues"][2] == ("player3", 1)

    def test_get_stats_max_messages_per_player(self) -> None:
        """Test that get_stats includes max_messages_per_player."""
        queue = MessageQueue(max_messages_per_player=500)

        stats = queue.get_stats()

        assert stats["max_messages_per_player"] == 500

    def test_get_stats_top_5_largest(self) -> None:
        """Test that get_stats returns only top 5 largest queues."""
        queue = MessageQueue()

        # Add 10 players with different message counts
        for player_num in range(10):
            for msg_num in range(player_num + 1):
                queue.add_message(f"player{player_num}", {"content": f"Message {msg_num}"})

        stats = queue.get_stats()

        assert len(stats["largest_queues"]) == 5
        # Should be the 5 players with most messages (player5-player9)
        assert stats["largest_queues"][0][0] == "player9"

    def test_get_stats_exception_handling(self) -> None:
        """Test error handling when get_stats encounters an exception."""
        queue = MessageQueue()
        queue.add_message("player1", {"content": "Test"})

        # Simulate exception by replacing the entire dict with a mock
        original_pending = queue.pending_messages
        try:
            mock_dict = MagicMock()
            mock_dict.values.side_effect = TypeError("Simulated error")
            queue.pending_messages = mock_dict

            stats = queue.get_stats()
            assert stats == {}
        finally:
            queue.pending_messages = original_pending


class TestMessageQueueIntegration:
    """Integration tests for MessageQueue operations."""

    def test_full_message_lifecycle(self) -> None:
        """Test complete lifecycle: add, check, retrieve, verify empty."""
        queue = MessageQueue()

        # Add messages
        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})

        # Check has messages
        assert queue.has_messages("player1") is True
        assert queue.get_message_count("player1") == 2

        # Retrieve messages
        messages = queue.get_messages("player1")
        assert len(messages) == 2

        # Verify empty after retrieval
        assert queue.has_messages("player1") is False
        assert queue.get_message_count("player1") == 0

    def test_multiple_players_independence(self) -> None:
        """Test that multiple players' queues are independent."""
        queue = MessageQueue()

        queue.add_message("player1", {"content": "Player 1 Message"})
        queue.add_message("player2", {"content": "Player 2 Message"})

        # Retrieve player1's messages
        player1_messages = queue.get_messages("player1")

        assert len(player1_messages) == 1
        assert player1_messages[0]["content"] == "Player 1 Message"

        # Player 2's messages should still exist
        assert queue.has_messages("player2") is True
        assert queue.get_message_count("player2") == 1

    def test_cleanup_workflows(self) -> None:
        """Test that cleanup methods work together."""
        queue = MessageQueue()

        old_time = time.time() - 7200  # 2 hours ago

        # Add many old messages
        for i in range(150):
            queue.add_message("player1", {"content": f"Message {i}", "timestamp": old_time})

        # Clean up old messages first
        queue.cleanup_old_messages(max_age_seconds=3600)

        # Should be empty now
        assert queue.get_message_count("player1") == 0

        # Add many new messages
        for i in range(150):
            queue.add_message("player2", {"content": f"Message {i}"})

        # Clean up large structures
        queue.cleanup_large_structures(max_entries=100)

        # Should be trimmed to 100
        assert queue.get_message_count("player2") == 100

    def test_stats_after_operations(self) -> None:
        """Test that stats reflect the current state after various operations."""
        queue = MessageQueue()

        # Add messages to multiple players
        queue.add_message("player1", {"content": "Message 1"})
        queue.add_message("player1", {"content": "Message 2"})
        queue.add_message("player2", {"content": "Message 1"})

        stats = queue.get_stats()
        assert stats["total_queues"] == 2
        assert stats["total_messages"] == 3

        # Retrieve player1's messages
        queue.get_messages("player1")

        stats = queue.get_stats()
        assert stats["total_queues"] == 1
        assert stats["total_messages"] == 1

        # Remove player2's messages
        queue.remove_player_messages("player2")

        stats = queue.get_stats()
        assert stats["total_queues"] == 0
        assert stats["total_messages"] == 0
