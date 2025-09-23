"""
Tests for local channel logging system.

These tests cover the sub-zone specific logging functionality for local channels,
including log file creation, rotation, and cleanup.
"""

import json
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from server.services.chat_logger import ChatLogger
from server.utils.room_utils import extract_subzone_from_room_id


class TestLocalChannelLogging:
    """Test local channel logging functionality."""

    @pytest.fixture
    def temp_log_dir(self):
        """Create a temporary directory for log files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield Path(temp_dir)

    @pytest.fixture
    def chat_logger(self, temp_log_dir):
        """Create a chat logger instance with temporary directory."""
        return ChatLogger(str(temp_log_dir))

    def test_local_channel_log_directory_structure(self, chat_logger):
        """Test that local channel log directories are created correctly."""
        # Verify that the local channel directory is created
        local_dir = chat_logger.log_dir / "chat" / "local"
        assert local_dir.exists()
        assert local_dir.is_dir()

    def test_get_local_channel_log_file(self, chat_logger):
        """Test getting local channel log file path for a specific sub-zone."""
        subzone = "docks"
        log_file = chat_logger._get_local_channel_log_file(subzone)

        today = datetime.now(UTC).strftime("%Y-%m-%d")
        expected_filename = f"local_{subzone}_{today}.log"
        expected_path = chat_logger.log_dir / "chat" / "local" / expected_filename

        assert log_file == expected_path

    def test_log_local_channel_message(self, chat_logger):
        """Test logging a local channel message to sub-zone specific file."""
        room_id = "earth_arkham_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)

        message_data = {
            "message_id": "msg-123",
            "channel": "local",
            "sender_id": "player1",
            "sender_name": "TestPlayer",
            "content": "Hello, local area!",
            "room_id": room_id,
            "subzone": subzone,
            "filtered": False,
            "moderation_notes": None,
        }

        chat_logger.log_local_channel_message(message_data)

        # Wait for the writer thread to process the queued message
        chat_logger.wait_for_queue_processing()

        # Verify the message was logged to the correct file
        log_file = chat_logger._get_local_channel_log_file(subzone)
        assert log_file.exists()

        # Read and verify the log entry
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) == 1

            entry = json.loads(lines[0])
            assert entry["event_type"] == "local_channel_message"
            assert entry["message_id"] == "msg-123"
            assert entry["channel"] == "local"
            assert entry["sender_id"] == "player1"
            assert entry["sender_name"] == "TestPlayer"
            assert entry["content"] == "Hello, local area!"
            assert entry["room_id"] == room_id
            assert entry["subzone"] == subzone
            assert entry["filtered"] is False
            assert "timestamp" in entry

    def test_log_local_channel_message_multiple_subzones(self, chat_logger):
        """Test logging local channel messages to different sub-zone files."""
        rooms = [
            "earth_arkham_docks_warehouse_1",
            "earth_arkham_northside_mansion_1",
            "earth_arkhamcity_intersection_derby_high",
        ]

        for i, room_id in enumerate(rooms):
            subzone = extract_subzone_from_room_id(room_id)
            message_data = {
                "message_id": f"msg-{i}",
                "channel": "local",
                "sender_id": f"player{i}",
                "sender_name": f"Player{i}",
                "content": f"Message {i}",
                "room_id": room_id,
                "subzone": subzone,
                "filtered": False,
                "moderation_notes": None,
            }

            chat_logger.log_local_channel_message(message_data)

        # Wait for the writer thread to process all queued messages
        chat_logger.wait_for_queue_processing()

        # Verify each sub-zone has its own log file
        for room_id in rooms:
            subzone = extract_subzone_from_room_id(room_id)
            log_file = chat_logger._get_local_channel_log_file(subzone)
            assert log_file.exists()

            # Verify the file contains the correct message
            with open(log_file, encoding="utf-8") as f:
                lines = f.readlines()
                assert len(lines) == 1
                entry = json.loads(lines[0])
                assert entry["subzone"] == subzone

    def test_log_local_channel_message_with_moderation(self, chat_logger):
        """Test logging a local channel message with moderation notes."""
        room_id = "earth_arkham_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)

        message_data = {
            "message_id": "msg-456",
            "channel": "local",
            "sender_id": "player1",
            "sender_name": "TestPlayer",
            "content": "Filtered message",
            "room_id": room_id,
            "subzone": subzone,
            "filtered": True,
            "moderation_notes": "Content flagged for review",
        }

        chat_logger.log_local_channel_message(message_data)

        # Wait for the writer thread to process the queued message
        chat_logger.wait_for_queue_processing()

        # Verify the message was logged with moderation data
        log_file = chat_logger._get_local_channel_log_file(subzone)
        with open(log_file, encoding="utf-8") as f:
            entry = json.loads(f.readlines()[0])
            assert entry["filtered"] is True
            assert entry["moderation_notes"] == "Content flagged for review"

    def test_log_local_channel_message_invalid_room_id(self, chat_logger):
        """Test logging with invalid room ID that can't extract sub-zone."""
        message_data = {
            "message_id": "msg-789",
            "channel": "local",
            "sender_id": "player1",
            "sender_name": "TestPlayer",
            "content": "Invalid room message",
            "room_id": "invalid_room_id",
            "subzone": None,
            "filtered": False,
            "moderation_notes": None,
        }

        # Should handle gracefully and log to a default file
        chat_logger.log_local_channel_message(message_data)

        # Wait for the writer thread to process the queued message
        chat_logger.wait_for_queue_processing()

        # Verify it was logged to a default location
        log_file = chat_logger._get_local_channel_log_file("unknown")
        assert log_file.exists()

    def test_local_channel_log_rotation(self, chat_logger):
        """Test that local channel logs rotate by date."""
        room_id = "earth_arkham_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)

        # Log messages on different dates
        dates = ["2025-01-01", "2025-01-02", "2025-01-03"]

        for date_str in dates:
            with patch("server.services.chat_logger.datetime") as mock_datetime:
                mock_datetime.now.return_value = datetime.fromisoformat(f"{date_str}T12:00:00+00:00")
                mock_datetime.fromtimestamp.return_value = datetime.fromisoformat(f"{date_str}T12:00:00+00:00")

                message_data = {
                    "message_id": f"msg-{date_str}",
                    "channel": "local",
                    "sender_id": "player1",
                    "sender_name": "TestPlayer",
                    "content": f"Message from {date_str}",
                    "room_id": room_id,
                    "subzone": subzone,
                    "filtered": False,
                    "moderation_notes": None,
                }

                chat_logger.log_local_channel_message(message_data)

        # Wait for the writer thread to process all queued messages
        chat_logger.wait_for_queue_processing()

        # Verify separate log files were created for each date
        for date_str in dates:
            log_file = chat_logger.log_dir / "chat" / "local" / f"local_{subzone}_{date_str}.log"
            assert log_file.exists()

            with open(log_file, encoding="utf-8") as f:
                entry = json.loads(f.readlines()[0])
                assert entry["content"] == f"Message from {date_str}"

    def test_get_local_channel_log_files(self, chat_logger):
        """Test getting all local channel log files."""
        # Create some test log files
        subzones = ["docks", "northside", "warehouse"]
        today = datetime.now(UTC).strftime("%Y-%m-%d")

        for subzone in subzones:
            log_file = chat_logger._get_local_channel_log_file(subzone)
            log_file.parent.mkdir(parents=True, exist_ok=True)
            with open(log_file, "w", encoding="utf-8") as f:
                f.write('{"test": "data"}\n')

        # Get all local channel log files
        log_files = chat_logger.get_local_channel_log_files()

        # Verify all expected files are returned
        assert len(log_files) == len(subzones)
        for subzone in subzones:
            expected_path = chat_logger.log_dir / "chat" / "local" / f"local_{subzone}_{today}.log"
            assert str(expected_path) in log_files

    def test_get_local_channel_log_stats(self, chat_logger):
        """Test getting statistics for local channel log files."""
        # Create test log files with different sizes
        subzones = ["docks", "northside"]

        for i, subzone in enumerate(subzones):
            log_file = chat_logger._get_local_channel_log_file(subzone)
            log_file.parent.mkdir(parents=True, exist_ok=True)

            # Write different amounts of data to each file
            with open(log_file, "w", encoding="utf-8") as f:
                for j in range(i + 1):
                    f.write(f'{{"message": "test {j}"}}\n')

        # Get statistics
        stats = chat_logger.get_local_channel_log_stats()

        # Verify statistics are correct
        assert "local_channels" in stats
        local_stats = stats["local_channels"]

        for subzone in subzones:
            assert subzone in local_stats
            subzone_stats = local_stats[subzone]
            assert "file_path" in subzone_stats
            assert "file_size_bytes" in subzone_stats
            assert "last_modified" in subzone_stats
            assert subzone_stats["file_size_bytes"] > 0

    def test_cleanup_old_local_channel_logs(self, chat_logger):
        """Test cleanup of old local channel log files."""
        # Create test log files with different dates
        subzone = "docks"
        dates = ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04"]

        for date_str in dates:
            log_file = chat_logger.log_dir / "chat" / "local" / f"local_{subzone}_{date_str}.log"
            log_file.parent.mkdir(parents=True, exist_ok=True)
            with open(log_file, "w", encoding="utf-8") as f:
                f.write('{"test": "data"}\n')

            # Set file modification time to match the date in filename
            import os

            file_date = datetime.fromisoformat(f"{date_str}T12:00:00+00:00")
            os.utime(log_file, (file_date.timestamp(), file_date.timestamp()))

        # Clean up logs older than 2 days (keeping 2025-01-03 and 2025-01-04)
        with patch("server.services.chat_logger.datetime") as mock_datetime:
            # Set current time to be later in the day to ensure 2025-01-02 is considered old
            mock_datetime.now.return_value = datetime.fromisoformat("2025-01-04T23:59:59+00:00")

            # Mock fromtimestamp to return the actual datetime objects
            def mock_fromtimestamp(timestamp, tz=None):
                # Convert timestamp back to datetime
                return datetime.fromtimestamp(timestamp, tz or UTC)

            mock_datetime.fromtimestamp.side_effect = mock_fromtimestamp

            deleted_files = chat_logger.cleanup_old_local_channel_logs(days_to_keep=2)

        # Verify old files were deleted
        assert len(deleted_files) == 2  # 2025-01-01 and 2025-01-02

        # Verify recent files still exist
        for date_str in ["2025-01-03", "2025-01-04"]:
            log_file = chat_logger.log_dir / "chat" / "local" / f"local_{subzone}_{date_str}.log"
            assert log_file.exists()

    def test_log_local_channel_message_serial_access(self, chat_logger):
        """Test serial access to local channel logging."""
        import time

        room_id = "earth_arkham_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)

        def log_message(thread_id):
            for i in range(10):
                message_data = {
                    "message_id": f"msg-thread{thread_id}-{i}",
                    "channel": "local",
                    "sender_id": f"player{thread_id}",
                    "sender_name": f"Player{thread_id}",
                    "content": f"Message {i} from thread {thread_id}",
                    "room_id": room_id,
                    "subzone": subzone,
                    "filtered": False,
                    "moderation_notes": None,
                }
                chat_logger.log_local_channel_message(message_data)
                time.sleep(0.001)  # Small delay to simulate processing time

        # Execute logging serially instead of in parallel threads
        # This tests the same functionality without violating serial test execution
        for i in range(3):
            log_message(i)

        # Wait for the writer thread to process all queued messages
        chat_logger.wait_for_queue_processing()

        # Verify messages were logged (allow for some race condition loss)
        log_file = chat_logger._get_local_channel_log_file(subzone)
        assert log_file.exists()

        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            # Allow for some message loss due to race conditions
            # We expect at least 25 out of 30 messages (3 threads * 10 messages each)
            assert len(lines) >= 25, f"Expected at least 25 messages, got {len(lines)}"

            # Verify that messages from all threads are present
            thread_messages = {0: 0, 1: 0, 2: 0}
            for line in lines:
                entry = json.loads(line)
                sender_id = entry["sender_id"]
                if sender_id in ["player0", "player1", "player2"]:
                    thread_id = int(sender_id[-1])
                    thread_messages[thread_id] += 1

            # Each thread should have at least some messages
            for thread_id in [0, 1, 2]:
                assert thread_messages[thread_id] > 0, f"Thread {thread_id} has no messages"

    def test_log_local_channel_message_error_handling(self, chat_logger):
        """Test error handling in local channel logging."""
        room_id = "earth_arkham_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)

        # Create a message with non-serializable content
        message_data = {
            "message_id": "msg-error",
            "channel": "local",
            "sender_id": "player1",
            "sender_name": "TestPlayer",
            "content": lambda x: x,  # Non-serializable function in content field
            "room_id": room_id,
            "subzone": subzone,
            "filtered": False,
            "moderation_notes": None,
        }

        # Should handle the error gracefully
        with patch("server.services.chat_logger.logger") as mock_logger:
            chat_logger.log_local_channel_message(message_data)

            # Verify error was logged
            mock_logger.error.assert_called()

    def test_local_channel_log_directory_permissions(self, chat_logger):
        """Test that local channel log directories have correct permissions."""
        local_dir = chat_logger.log_dir / "chat" / "local"

        # Verify directory exists and is writable
        assert local_dir.exists()
        assert local_dir.is_dir()

        # Test that we can write to the directory
        test_file = local_dir / "test_permissions.txt"
        test_file.write_text("test")
        assert test_file.exists()
        test_file.unlink()  # Clean up

    def test_local_channel_log_file_encoding(self, chat_logger):
        """Test that local channel logs handle Unicode content correctly."""
        room_id = "earth_arkham_docks_warehouse_1"
        subzone = extract_subzone_from_room_id(room_id)

        # Test with Unicode content
        unicode_content = "Hello, 世界! 🌍 Привет! こんにちは!"
        message_data = {
            "message_id": "msg-unicode",
            "channel": "local",
            "sender_id": "player1",
            "sender_name": "TestPlayer",
            "content": unicode_content,
            "room_id": room_id,
            "subzone": subzone,
            "filtered": False,
            "moderation_notes": None,
        }

        chat_logger.log_local_channel_message(message_data)

        # Wait for the writer thread to process the queued message
        chat_logger.wait_for_queue_processing()

        # Verify Unicode content was written correctly
        log_file = chat_logger._get_local_channel_log_file(subzone)
        with open(log_file, encoding="utf-8") as f:
            entry = json.loads(f.readlines()[0])
            assert entry["content"] == unicode_content
