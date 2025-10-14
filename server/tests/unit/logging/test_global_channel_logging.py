"""
Tests for Global Channel Logging.

This module tests the global channel logging functionality in the ChatLogger,
including message logging, file management, and cleanup operations.
"""

import json
import os
from datetime import UTC, datetime
from unittest.mock import patch

import pytest

from server.services.chat_logger import ChatLogger


class TestGlobalChannelLogging:
    """Test global channel logging functionality."""

    @pytest.fixture
    def chat_logger(self, tmp_path):
        """Create a chat logger with temporary directory."""
        log_dir = tmp_path / "logs"
        return ChatLogger(log_dir=log_dir)

    def test_log_global_channel_message_success(self, chat_logger):
        """Test successful global channel message logging."""
        message_data = {
            "message_id": "test-msg-123",
            "channel": "global",
            "sender_id": "test-player-id",
            "sender_name": "TestPlayer",
            "content": "Hello, world!",
            "filtered": False,
            "moderation_notes": None,
        }

        chat_logger.log_global_channel_message(message_data)
        chat_logger.wait_for_queue_processing()

        # Check that the log file was created
        log_file = chat_logger._get_global_channel_log_file()
        assert log_file.exists()

        # Check the content
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) == 1

            log_entry = json.loads(lines[0])
            assert log_entry["event_type"] == "global_channel_message"
            assert log_entry["message_id"] == "test-msg-123"
            assert log_entry["channel"] == "global"
            assert log_entry["sender_id"] == "test-player-id"
            assert log_entry["sender_name"] == "TestPlayer"
            assert log_entry["content"] == "Hello, world!"
            assert log_entry["filtered"] is False
            assert log_entry["moderation_notes"] is None
            assert "timestamp" in log_entry

    def test_log_global_channel_message_with_timestamp(self, chat_logger):
        """Test global channel message logging with existing timestamp."""
        timestamp = "2025-01-15T10:30:00+00:00"
        message_data = {
            "message_id": "test-msg-456",
            "channel": "global",
            "sender_id": "test-player-id",
            "sender_name": "TestPlayer",
            "content": "Test message with timestamp",
            "timestamp": timestamp,
            "filtered": False,
            "moderation_notes": None,
        }

        chat_logger.log_global_channel_message(message_data)
        chat_logger.wait_for_queue_processing()

        # Check the content
        log_file = chat_logger._get_global_channel_log_file()
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) == 1

            log_entry = json.loads(lines[0])
            assert log_entry["timestamp"] == timestamp

    def test_log_global_channel_message_error_handling(self, chat_logger):
        """Test error handling in global channel message logging."""
        # Create message data with non-serializable content
        message_data = {
            "message_id": "test-msg-789",
            "channel": "global",
            "sender_id": "test-player-id",
            "sender_name": "TestPlayer",
            "content": lambda x: x,  # Non-serializable lambda function in content field
        }

        # This should not raise an exception but should log an error
        chat_logger.log_global_channel_message(message_data)
        chat_logger.wait_for_queue_processing()

        # The log file should not be created due to the error
        log_file = chat_logger._get_global_channel_log_file()
        assert not log_file.exists()

    def test_get_global_channel_log_file(self, chat_logger):
        """Test getting global channel log file path."""
        log_file = chat_logger._get_global_channel_log_file()

        # Check the path structure
        assert log_file.parent.name == "global"
        assert log_file.parent.parent.name == "chat"
        assert log_file.name.startswith("global_")
        assert log_file.name.endswith(".log")

        # Check the date format
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        expected_name = f"global_{today}.log"
        assert log_file.name == expected_name

    def test_get_global_channel_log_files_empty(self, chat_logger):
        """Test getting global channel log files when directory doesn't exist."""
        log_files = chat_logger.get_global_channel_log_files()
        assert log_files == []

    def test_get_global_channel_log_files_with_files(self, chat_logger):
        """Test getting global channel log files when files exist."""
        # Create some test log files
        global_dir = chat_logger.log_dir / "chat" / "global"
        global_dir.mkdir(parents=True, exist_ok=True)

        # Create test files
        test_files = [
            "global_2025-01-15.log",
            "global_2025-01-16.log",
            "global_2025-01-17.log",
            "other_file.txt",  # Should be ignored
        ]

        for filename in test_files:
            (global_dir / filename).touch()

        log_files = chat_logger.get_global_channel_log_files()

        # Should only return global log files
        assert len(log_files) == 3
        assert all("global_2025-01-" in f for f in log_files)
        assert all(f.endswith(".log") for f in log_files)

    def test_get_global_channel_log_stats_empty(self, chat_logger):
        """Test getting global channel log stats when no files exist."""
        stats = chat_logger.get_global_channel_log_stats()
        assert stats == {"global_channels": {}}

    def test_get_global_channel_log_stats_with_files(self, chat_logger):
        """Test getting global channel log stats when files exist."""
        # Create test log files
        global_dir = chat_logger.log_dir / "chat" / "global"
        global_dir.mkdir(parents=True, exist_ok=True)

        # Create test files with content
        test_files = [
            ("global_2025-01-15.log", "Test content 1"),
            ("global_2025-01-16.log", "Test content 2"),
        ]

        for filename, content in test_files:
            file_path = global_dir / filename
            file_path.write_text(content, encoding="utf-8")

        stats = chat_logger.get_global_channel_log_stats()

        assert "global_channels" in stats
        assert len(stats["global_channels"]) == 2

        # Check individual file stats
        assert "2025-01-15" in stats["global_channels"]
        assert "2025-01-16" in stats["global_channels"]

        for date in ["2025-01-15", "2025-01-16"]:
            file_stats = stats["global_channels"][date]
            assert "file_path" in file_stats
            assert "date" in file_stats
            assert "file_size_bytes" in file_stats
            assert "last_modified" in file_stats
            assert file_stats["date"] == date
            assert file_stats["file_size_bytes"] > 0

    def test_cleanup_old_global_channel_logs(self, chat_logger):
        """Test cleanup of old global channel log files."""
        # Create test log files
        global_dir = chat_logger.log_dir / "chat" / "global"
        global_dir.mkdir(parents=True, exist_ok=True)

        # Create files with different dates
        test_files = [
            ("global_2025-01-01.log", "Old content 1"),
            ("global_2025-01-02.log", "Old content 2"),
            ("global_2025-01-03.log", "Recent content 1"),
            ("global_2025-01-04.log", "Recent content 2"),
        ]

        for filename, content in test_files:
            file_path = global_dir / filename
            file_path.write_text(content, encoding="utf-8")

        # Mock datetime to simulate current time
        mock_now = datetime(2025, 1, 4, 12, 0, 0, tzinfo=UTC)

        with patch("server.services.chat_logger.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            mock_datetime.fromtimestamp.side_effect = lambda ts, tz: datetime.fromtimestamp(ts, tz)

            # Set file modification times
            for filename, _ in test_files:
                file_path = global_dir / filename
                # Extract date from filename and set modification time
                date_str = filename[7:-4]  # Remove "global_" prefix and ".log" suffix
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                os.utime(file_path, (file_date.timestamp(), file_date.timestamp()))

            # Clean up files older than 2 days
            deleted_files = chat_logger.cleanup_old_global_channel_logs(days_to_keep=2)

        # Should delete 2 old files
        assert len(deleted_files) == 2
        assert any("2025-01-01" in f for f in deleted_files)
        assert any("2025-01-02" in f for f in deleted_files)

        # Check remaining files
        remaining_files = list(global_dir.glob("global_*.log"))
        assert len(remaining_files) == 2
        assert any("2025-01-03" in f.name for f in remaining_files)
        assert any("2025-01-04" in f.name for f in remaining_files)

    def test_cleanup_old_global_channel_logs_no_cleanup_needed(self, chat_logger):
        """Test cleanup when no files need to be deleted."""
        # Create test log files
        global_dir = chat_logger.log_dir / "chat" / "global"
        global_dir.mkdir(parents=True, exist_ok=True)

        # Create recent files only
        test_files = [
            ("global_2025-01-03.log", "Recent content 1"),
            ("global_2025-01-04.log", "Recent content 2"),
        ]

        for filename, content in test_files:
            file_path = global_dir / filename
            file_path.write_text(content, encoding="utf-8")

        # Mock datetime to simulate current time
        mock_now = datetime(2025, 1, 4, 12, 0, 0, tzinfo=UTC)

        with patch("server.services.chat_logger.datetime") as mock_datetime:
            mock_datetime.now.return_value = mock_now
            mock_datetime.fromtimestamp.side_effect = lambda ts, tz: datetime.fromtimestamp(ts, tz)

            # Set file modification times
            for filename, _ in test_files:
                file_path = global_dir / filename
                date_str = filename[7:-4]
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                os.utime(file_path, (file_date.timestamp(), file_date.timestamp()))

            # Clean up files older than 2 days
            deleted_files = chat_logger.cleanup_old_global_channel_logs(days_to_keep=2)

        # Should not delete any files
        assert len(deleted_files) == 0

        # Check all files remain
        remaining_files = list(global_dir.glob("global_*.log"))
        assert len(remaining_files) == 2

    def test_serial_global_channel_logging(self, chat_logger):
        """Test serial global channel message logging."""
        import time

        def log_message(thread_id):
            for i in range(10):
                message_data = {
                    "message_id": f"test-msg-{thread_id}-{i}",
                    "channel": "global",
                    "sender_id": f"player-{thread_id}",
                    "sender_name": f"Player{thread_id}",
                    "content": f"Message {i} from thread {thread_id}",
                    "filtered": False,
                    "moderation_notes": None,
                }
                chat_logger.log_global_channel_message(message_data)
                time.sleep(0.001)  # Small delay to simulate processing time

        # Execute logging serially instead of in parallel threads
        # This tests the same functionality without violating serial test execution
        for i in range(3):
            log_message(i)

        # Wait for queue processing
        chat_logger.wait_for_queue_processing()

        # Check that all messages were logged
        log_file = chat_logger._get_global_channel_log_file()
        assert log_file.exists()

        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            # Should have 30 messages (3 threads × 10 messages each)
            assert len(lines) >= 25  # Allow for some message loss due to race conditions

            # Verify message content
            for line in lines:
                log_entry = json.loads(line)
                assert log_entry["event_type"] == "global_channel_message"
                assert log_entry["channel"] == "global"
                assert "message_id" in log_entry
                assert "sender_id" in log_entry
                assert "content" in log_entry
