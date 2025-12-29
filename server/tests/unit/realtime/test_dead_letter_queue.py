"""
Unit tests for dead letter queue.

Tests the DeadLetterQueue class and DeadLetterMessage dataclass.
"""

import json
import tempfile
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import patch

from server.realtime.dead_letter_queue import DeadLetterMessage, DeadLetterQueue


def test_dead_letter_message_to_dict():
    """Test DeadLetterMessage.to_dict() converts to dictionary."""
    message = DeadLetterMessage(
        subject="test.subject",
        data={"key": "value"},
        error="Test error",
        timestamp=datetime.now(UTC),
        retry_count=3,
        original_headers={"header1": "value1"},
    )
    result = message.to_dict()
    assert result["subject"] == "test.subject"
    assert result["data"] == {"key": "value"}
    assert result["error"] == "Test error"
    assert result["retry_count"] == 3
    assert result["original_headers"] == {"header1": "value1"}
    assert "timestamp" in result


def test_dead_letter_message_to_dict_no_headers():
    """Test DeadLetterMessage.to_dict() handles None headers."""
    message = DeadLetterMessage(
        subject="test.subject",
        data={"key": "value"},
        error="Test error",
        timestamp=datetime.now(UTC),
        retry_count=0,
        original_headers=None,
    )
    result = message.to_dict()
    assert result["original_headers"] == {}


def test_dead_letter_message_from_dict():
    """Test DeadLetterMessage.from_dict() reconstructs message."""
    timestamp = datetime.now(UTC)
    data = {
        "subject": "test.subject",
        "data": {"key": "value"},
        "error": "Test error",
        "timestamp": timestamp.isoformat(),
        "retry_count": 3,
        "original_headers": {"header1": "value1"},
    }
    message = DeadLetterMessage.from_dict(data)
    assert message.subject == "test.subject"
    assert message.data == {"key": "value"}
    assert message.error == "Test error"
    assert message.retry_count == 3
    assert message.original_headers == {"header1": "value1"}


def test_dead_letter_message_from_dict_string_timestamp():
    """Test DeadLetterMessage.from_dict() handles string timestamp."""
    data = {
        "subject": "test.subject",
        "data": {"key": "value"},
        "error": "Test error",
        "timestamp": "2024-01-01T12:00:00+00:00",
        "retry_count": 0,
    }
    message = DeadLetterMessage.from_dict(data)
    assert isinstance(message.timestamp, datetime)


def test_dead_letter_message_from_dict_datetime_timestamp():
    """Test DeadLetterMessage.from_dict() handles datetime timestamp."""
    timestamp = datetime.now(UTC)
    data = {
        "subject": "test.subject",
        "data": {"key": "value"},
        "error": "Test error",
        "timestamp": timestamp,
        "retry_count": 0,
    }
    message = DeadLetterMessage.from_dict(data)
    assert message.timestamp == timestamp


def test_dead_letter_queue_init_with_storage_dir():
    """Test DeadLetterQueue initialization with storage directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        assert dlq.storage_dir == Path(tmpdir)
        assert dlq.storage_dir.exists()


def test_dead_letter_queue_init_without_storage_dir():
    """Test DeadLetterQueue initialization without storage directory."""
    # This test verifies that DeadLetterQueue can initialize without explicit storage_dir
    # The actual path resolution is complex, so we just verify it doesn't raise
    with patch("server.realtime.dead_letter_queue.get_config") as mock_config:
        mock_config.return_value.logging.environment = "test"
        mock_config.return_value.logging.log_base = "logs"
        # Should not raise - uses default path resolution
        dlq = DeadLetterQueue()
        assert hasattr(dlq, "storage_dir")
        assert dlq.storage_dir is not None


def test_enqueue_creates_file():
    """Test enqueue() creates DLQ file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        filepath = dlq.enqueue(message)
        assert filepath.exists()
        assert filepath.name.startswith("dlq_")
        assert filepath.suffix == ".json"


def test_enqueue_writes_correct_data():
    """Test enqueue() writes correct message data."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=3,
        )
        filepath = dlq.enqueue(message)
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        assert data["subject"] == "test.subject"
        assert data["data"] == {"key": "value"}
        assert data["error"] == "Test error"
        assert data["retry_count"] == 3


def test_dequeue_returns_none_when_empty():
    """Test dequeue() returns None when queue is empty."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        result = dlq.dequeue()
        assert result is None


def test_dequeue_returns_oldest_message():
    """Test dequeue() returns oldest message."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        # Create two messages with slight delay
        message1 = DeadLetterMessage(
            subject="test.subject1",
            data={"key": "value1"},
            error="Error 1",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        filepath1 = dlq.enqueue(message1)
        # Small delay to ensure different timestamps
        import time

        time.sleep(0.01)
        message2 = DeadLetterMessage(
            subject="test.subject2",
            data={"key": "value2"},
            error="Error 2",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        dlq.enqueue(message2)
        # Dequeue should return oldest (first)
        result = dlq.dequeue()
        assert result is not None
        assert result["subject"] == "test.subject1"
        # File should be removed
        assert not filepath1.exists()


def test_dequeue_removes_file():
    """Test dequeue() removes file after reading."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        filepath = dlq.enqueue(message)
        assert filepath.exists()
        dlq.dequeue()
        assert not filepath.exists()


def test_dequeue_handles_read_error():
    """Test dequeue() handles file read errors."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        # Create invalid JSON file
        invalid_file = dlq.storage_dir / "dlq_test.json"
        invalid_file.write_text("invalid json")
        result = dlq.dequeue()
        # Should return None on error
        assert result is None


def test_get_statistics_empty():
    """Test get_statistics() returns stats for empty queue."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        stats = dlq.get_statistics()
        assert stats["total_messages"] == 0
        assert stats["oldest_message_age"] is None
        assert stats["storage_dir"] == str(dlq.storage_dir)


def test_get_statistics_with_messages():
    """Test get_statistics() returns stats with messages."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        dlq.enqueue(message)
        stats = dlq.get_statistics()
        assert stats["total_messages"] == 1
        assert stats["oldest_message_age"] is not None
        assert stats["oldest_message_age"] >= 0


def test_list_messages_empty():
    """Test list_messages() returns empty list when queue is empty."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        messages = dlq.list_messages()
        assert messages == []


def test_list_messages_returns_all():
    """Test list_messages() returns all messages."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message1 = DeadLetterMessage(
            subject="test.subject1",
            data={"key": "value1"},
            error="Error 1",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        message2 = DeadLetterMessage(
            subject="test.subject2",
            data={"key": "value2"},
            error="Error 2",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        dlq.enqueue(message1)
        dlq.enqueue(message2)
        messages = dlq.list_messages()
        assert len(messages) == 2
        assert all("dlq_file" in msg for msg in messages)


def test_list_messages_respects_limit():
    """Test list_messages() respects limit parameter."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        for i in range(5):
            message = DeadLetterMessage(
                subject=f"test.subject{i}",
                data={"key": f"value{i}"},
                error="Error",
                timestamp=datetime.now(UTC),
                retry_count=0,
            )
            dlq.enqueue(message)
        messages = dlq.list_messages(limit=3)
        assert len(messages) == 3


def test_list_messages_handles_read_error():
    """Test list_messages() handles file read errors."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        # Create valid message
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        dlq.enqueue(message)
        # Create invalid JSON file
        invalid_file = dlq.storage_dir / "dlq_invalid.json"
        invalid_file.write_text("invalid json")
        messages = dlq.list_messages()
        # Should return only valid message
        assert len(messages) == 1


def test_replay_message():
    """Test replay_message() retrieves and removes message."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        filepath = dlq.enqueue(message)
        result = dlq.replay_message(str(filepath))
        assert result["subject"] == "test.subject"
        assert result["data"] == {"key": "value"}
        # File should be removed
        assert not filepath.exists()


def test_delete_message():
    """Test delete_message() removes message file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        filepath = dlq.enqueue(message)
        assert filepath.exists()
        dlq.delete_message(str(filepath))
        assert not filepath.exists()


def test_cleanup_old_messages():
    """Test cleanup_old_messages() removes old messages."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        # Create old file (manually set mtime)
        old_file = dlq.storage_dir / "dlq_old.json"
        old_file.write_text(json.dumps({"subject": "old"}))
        old_time = datetime.now(UTC) - timedelta(days=10)
        old_timestamp = old_time.timestamp()
        old_file.touch()
        import os

        os.utime(old_file, (old_timestamp, old_timestamp))
        # Create recent file
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        dlq.enqueue(message)
        # Cleanup messages older than 7 days
        removed = dlq.cleanup_old_messages(max_age_days=7)
        assert removed == 1
        assert not old_file.exists()
        # Recent file should still exist
        assert len(list(dlq.storage_dir.glob("dlq_*.json"))) == 1


def test_cleanup_old_messages_no_old_messages():
    """Test cleanup_old_messages() returns 0 when no old messages."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        message = DeadLetterMessage(
            subject="test.subject",
            data={"key": "value"},
            error="Test error",
            timestamp=datetime.now(UTC),
            retry_count=0,
        )
        dlq.enqueue(message)
        removed = dlq.cleanup_old_messages(max_age_days=7)
        assert removed == 0
        # Message should still exist
        assert len(list(dlq.storage_dir.glob("dlq_*.json"))) == 1


def test_cleanup_old_messages_handles_errors():
    """Test cleanup_old_messages() handles file errors."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dlq = DeadLetterQueue(storage_dir=tmpdir)
        # Create file that will cause error on stat
        old_file = dlq.storage_dir / "dlq_old.json"
        old_file.write_text(json.dumps({"subject": "old"}))
        # Should not raise, just return 0
        with patch.object(Path, "stat", side_effect=OSError("Permission denied")):
            removed = dlq.cleanup_old_messages(max_age_days=7)
            assert removed == 0
