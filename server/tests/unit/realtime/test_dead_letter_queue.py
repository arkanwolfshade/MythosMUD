"""
Tests for Dead Letter Queue (DLQ) implementation.

Like the forbidden tomes sequestered in the restricted section,
failed messages are quarantined for later examination.

AI: Tests DLQ for storing and managing permanently failed messages.
"""

import json
import os
import tempfile
import time
from datetime import datetime

import pytest

from server.realtime.dead_letter_queue import DeadLetterMessage, DeadLetterQueue


@pytest.fixture
def temp_dlq_dir():
    """Create a temporary directory for DLQ storage."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def dlq(temp_dlq_dir):
    """Create a DeadLetterQueue instance with temporary storage."""
    return DeadLetterQueue(storage_dir=temp_dlq_dir)


class TestDeadLetterQueue:
    """Test suite for Dead Letter Queue."""

    def test_initialization(self, temp_dlq_dir):
        """DLQ initializes with correct storage directory."""
        dlq = DeadLetterQueue(storage_dir=temp_dlq_dir)

        assert dlq.storage_dir.exists()
        assert dlq.storage_dir.is_dir()

    def test_enqueue_creates_file(self, dlq):
        """Enqueuing a message creates a DLQ file."""
        message = DeadLetterMessage(
            subject="test.subject", data={"test": "data"}, error="Test error", timestamp=datetime.now(), retry_count=3
        )

        filepath = dlq.enqueue(message)

        assert filepath.exists()
        assert filepath.suffix == ".json"

    def test_enqueue_stores_message_data(self, dlq):
        """Enqueued message data is correctly stored."""
        message = DeadLetterMessage(
            subject="game.events",
            data={"player": "test_player", "action": "move"},
            error="Connection timeout",
            timestamp=datetime.now(),
            retry_count=5,
        )

        filepath = dlq.enqueue(message)

        with open(filepath, encoding="utf-8") as f:
            stored_data = json.load(f)

        assert stored_data["subject"] == "game.events"
        assert stored_data["data"] == {"player": "test_player", "action": "move"}
        assert stored_data["error"] == "Connection timeout"
        assert stored_data["retry_count"] == 5

    def test_dequeue_returns_oldest_message(self, dlq):
        """Dequeue returns the oldest message first."""
        # Enqueue multiple messages
        msg1 = DeadLetterMessage("test1", {}, "error1", datetime.now(), 1)
        msg2 = DeadLetterMessage("test2", {}, "error2", datetime.now(), 1)
        msg3 = DeadLetterMessage("test3", {}, "error3", datetime.now(), 1)

        file1 = dlq.enqueue(msg1)
        time.sleep(0.01)  # Ensure different timestamps
        dlq.enqueue(msg2)
        time.sleep(0.01)
        dlq.enqueue(msg3)

        # Dequeue should return oldest (first)
        dequeued = dlq.dequeue()

        assert dequeued["subject"] == "test1"
        assert not file1.exists()  # Should be removed after dequeue

    def test_dequeue_removes_file(self, dlq):
        """Dequeuing a message removes its file."""
        message = DeadLetterMessage("test", {}, "error", datetime.now(), 1)
        filepath = dlq.enqueue(message)

        assert filepath.exists()

        dlq.dequeue()

        assert not filepath.exists()

    def test_dequeue_empty_queue_returns_none(self, dlq):
        """Dequeuing from empty queue returns None."""
        result = dlq.dequeue()

        assert result is None

    @pytest.mark.serial  # Flaky in parallel execution - likely due to shared DeadLetterQueue state
    def test_get_statistics(self, dlq):
        """Get statistics returns correct counts."""
        # Enqueue multiple messages
        for i in range(5):
            msg = DeadLetterMessage(f"test{i}", {}, f"error{i}", datetime.now(), i)
            dlq.enqueue(msg)

        stats = dlq.get_statistics()

        assert stats["total_messages"] == 5
        assert stats["oldest_message_age"] is not None

    def test_get_statistics_empty_queue(self, dlq):
        """Get statistics for empty queue."""
        stats = dlq.get_statistics()

        assert stats["total_messages"] == 0
        assert stats["oldest_message_age"] is None

    @pytest.mark.serial  # Flaky in parallel execution - shared DeadLetterQueue state
    def test_list_messages(self, dlq):
        """List messages returns all messages in queue."""
        messages = [DeadLetterMessage(f"test{i}", {"id": i}, f"error{i}", datetime.now(), i) for i in range(3)]

        for msg in messages:
            dlq.enqueue(msg)

        listed = dlq.list_messages()

        assert len(listed) == 3
        assert all("subject" in msg for msg in listed)
        assert all("timestamp" in msg for msg in listed)

    def test_list_messages_with_limit(self, dlq):
        """List messages respects limit parameter."""
        for i in range(10):
            msg = DeadLetterMessage(f"test{i}", {}, "error", datetime.now(), i)
            dlq.enqueue(msg)

        listed = dlq.list_messages(limit=5)

        assert len(listed) == 5

    def test_replay_message_by_filepath(self, dlq):
        """Replay message removes it from DLQ and returns data."""
        message = DeadLetterMessage("test", {"key": "value"}, "error", datetime.now(), 3)
        filepath = dlq.enqueue(message)

        replayed = dlq.replay_message(str(filepath))

        assert replayed["subject"] == "test"
        assert replayed["data"] == {"key": "value"}
        assert not filepath.exists()

    def test_delete_message_by_filepath(self, dlq):
        """Delete message removes it from DLQ."""
        message = DeadLetterMessage("test", {}, "error", datetime.now(), 1)
        filepath = dlq.enqueue(message)

        assert filepath.exists()

        dlq.delete_message(str(filepath))

        assert not filepath.exists()

    def test_cleanup_old_messages(self, dlq):
        """Cleanup removes messages older than max_age."""
        # Create an old message
        old_message = DeadLetterMessage("old", {}, "error", datetime.now(), 1)
        old_file = dlq.enqueue(old_message)

        # Manually set modification time to 10 days ago
        ten_days_ago = time.time() - (10 * 24 * 60 * 60)
        os.utime(old_file, (ten_days_ago, ten_days_ago))

        # Create a recent message
        recent_message = DeadLetterMessage("recent", {}, "error", datetime.now(), 1)
        recent_file = dlq.enqueue(recent_message)

        # Cleanup messages older than 7 days
        removed_count = dlq.cleanup_old_messages(max_age_days=7)

        assert removed_count == 1
        assert not old_file.exists()
        assert recent_file.exists()

    def test_dead_letter_message_to_dict(self) -> None:
        """DeadLetterMessage converts to dict correctly."""
        now = datetime.now()
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error message",
            timestamp=now,
            retry_count=5,
            original_headers={"content-type": "application/json"},
        )

        data = message.to_dict()

        assert data["subject"] == "test.subject"
        assert data["data"] == {"key": "value"}
        assert data["error"] == "Test error message"
        assert data["retry_count"] == 5
        assert data["original_headers"] == {"content-type": "application/json"}

    def test_dead_letter_message_from_dict(self) -> None:
        """DeadLetterMessage can be reconstructed from dict."""
        original = DeadLetterMessage(
            subject="test", data={"test": "data"}, error="error", timestamp=datetime.now(), retry_count=3
        )

        data_dict = original.to_dict()
        reconstructed = DeadLetterMessage.from_dict(data_dict)

        assert reconstructed.subject == original.subject
        assert reconstructed.data == original.data
        assert reconstructed.error == original.error
        assert reconstructed.retry_count == original.retry_count
