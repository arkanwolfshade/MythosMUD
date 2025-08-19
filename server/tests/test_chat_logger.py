"""
Unit tests for ChatLogger service.

These tests verify the structured logging functionality for chat messages,
moderation events, and system events in MythosMUD.
"""

import json
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from unittest.mock import patch

import pytest

from server.services.chat_logger import ChatLogger


class TestChatLogger:
    """Test suite for ChatLogger class."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a temporary directory for test logs
        self.temp_dir = tempfile.mkdtemp()
        self.log_dir = Path(self.temp_dir)

        # Create ChatLogger instance with test directory
        self.chat_logger = ChatLogger(str(self.log_dir))

    def teardown_method(self):
        """Clean up test fixtures."""
        # Remove temporary directory and all contents
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_chat_logger_initialization(self):
        """Test ChatLogger initialization creates required directories."""
        # Verify directories were created
        assert (self.log_dir / "chat").exists()
        assert (self.log_dir / "moderation").exists()
        assert (self.log_dir / "system").exists()

        # Verify attributes are set correctly
        assert self.chat_logger.log_dir == self.log_dir
        assert self.chat_logger.chat_dir == self.log_dir / "chat"
        assert self.chat_logger.moderation_dir == self.log_dir / "moderation"
        assert self.chat_logger.system_dir == self.log_dir / "system"

    def test_get_current_log_file_chat(self):
        """Test getting current log file path for chat type."""
        log_file = self.chat_logger._get_current_log_file("chat")
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        expected_filename = f"chat_{today}.log"

        assert log_file == self.chat_logger.chat_dir / expected_filename

    def test_get_current_log_file_moderation(self):
        """Test getting current log file path for moderation type."""
        log_file = self.chat_logger._get_current_log_file("moderation")
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        expected_filename = f"moderation_{today}.log"

        assert log_file == self.chat_logger.moderation_dir / expected_filename

    def test_get_current_log_file_system(self):
        """Test getting current log file path for system type."""
        log_file = self.chat_logger._get_current_log_file("system")
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        expected_filename = f"system_{today}.log"

        assert log_file == self.chat_logger.system_dir / expected_filename

    def test_get_current_log_file_invalid_type(self):
        """Test getting current log file with invalid type raises ValueError."""
        with pytest.raises(ValueError, match="Unknown log type: invalid"):
            self.chat_logger._get_current_log_file("invalid")

    def test_write_log_entry_success(self):
        """Test successful log entry writing."""
        entry = {"test": "data", "number": 42}

        # Write log entry
        self.chat_logger._write_log_entry("chat", entry)

        # Verify file was created and contains the entry
        log_file = self.chat_logger._get_current_log_file("chat")
        assert log_file.exists()

        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) == 1

            # Parse the JSON line
            logged_entry = json.loads(lines[0].strip())
            assert logged_entry["test"] == "data"
            assert logged_entry["number"] == 42
            assert "timestamp" in logged_entry  # Should be added automatically

    def test_write_log_entry_with_existing_timestamp(self):
        """Test log entry writing when timestamp already exists."""
        timestamp = "2023-01-01T12:00:00+00:00"
        entry = {"test": "data", "timestamp": timestamp}

        # Write log entry
        self.chat_logger._write_log_entry("chat", entry)

        # Verify timestamp was not overwritten
        log_file = self.chat_logger._get_current_log_file("chat")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())
            assert logged_entry["timestamp"] == timestamp

    def test_write_log_entry_unicode_content(self):
        """Test log entry writing with Unicode content."""
        entry = {"message": "Hello, 世界! 🌍", "emoji": "😀"}

        # Write log entry
        self.chat_logger._write_log_entry("chat", entry)

        # Verify Unicode content was written correctly
        log_file = self.chat_logger._get_current_log_file("chat")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())
            assert logged_entry["message"] == "Hello, 世界! 🌍"
            assert logged_entry["emoji"] == "😀"

    @patch("server.services.chat_logger.logger")
    def test_write_log_entry_exception_handling(self, mock_logger):
        """Test log entry writing handles exceptions gracefully."""
        # Mock open to raise an exception
        with patch("builtins.open", side_effect=PermissionError("Access denied")):
            entry = {"test": "data"}

            # Should not raise exception
            self.chat_logger._write_log_entry("chat", entry)

            # Verify error was logged
            mock_logger.error.assert_called_once()
            call_args = mock_logger.error.call_args
            assert call_args[1]["error"] == "Access denied"
            assert call_args[1]["log_type"] == "chat"
            assert call_args[1]["entry"] == entry

    def test_log_chat_message(self):
        """Test logging a chat message."""
        message_data = {
            "message_id": "msg_123",
            "channel": "say",
            "sender_id": "player_456",
            "sender_name": "TestPlayer",
            "content": "Hello, world!",
            "room_id": "room_789",
            "party_id": "party_101",
            "target_player_id": None,
            "filtered": False,
            "moderation_notes": None,
        }

        # Log the message
        self.chat_logger.log_chat_message(message_data)

        # Verify log file was created
        log_file = self.chat_logger._get_current_log_file("chat")
        assert log_file.exists()

        # Verify log entry
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) == 1

            logged_entry = json.loads(lines[0].strip())
            assert logged_entry["event_type"] == "chat_message"
            assert logged_entry["message_id"] == "msg_123"
            assert logged_entry["channel"] == "say"
            assert logged_entry["sender_id"] == "player_456"
            assert logged_entry["sender_name"] == "TestPlayer"
            assert logged_entry["content"] == "Hello, world!"
            assert logged_entry["room_id"] == "room_789"
            assert logged_entry["party_id"] == "party_101"
            assert logged_entry["target_player_id"] is None
            assert logged_entry["filtered"] is False
            assert logged_entry["moderation_notes"] is None

    def test_log_chat_message_minimal_data(self):
        """Test logging a chat message with minimal required data."""
        message_data = {
            "message_id": "msg_123",
            "channel": "say",
            "sender_id": "player_456",
            "sender_name": "TestPlayer",
            "content": "Hello!",
        }

        # Log the message
        self.chat_logger.log_chat_message(message_data)

        # Verify log entry has default values
        log_file = self.chat_logger._get_current_log_file("chat")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            # Required fields
            assert logged_entry["message_id"] == "msg_123"
            assert logged_entry["channel"] == "say"
            assert logged_entry["sender_id"] == "player_456"
            assert logged_entry["sender_name"] == "TestPlayer"
            assert logged_entry["content"] == "Hello!"

            # Optional fields with defaults
            assert logged_entry["room_id"] is None
            assert logged_entry["party_id"] is None
            assert logged_entry["target_player_id"] is None
            assert logged_entry["filtered"] is False
            assert logged_entry["moderation_notes"] is None

    def test_log_moderation_event(self):
        """Test logging a moderation event."""
        event_type = "player_warned"
        event_data = {
            "moderator_id": "mod_123",
            "target_id": "player_456",
            "reason": "Inappropriate language",
            "warning_level": "first",
        }

        # Log the event
        self.chat_logger.log_moderation_event(event_type, event_data)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == event_type
            assert logged_entry["moderator_id"] == "mod_123"
            assert logged_entry["target_id"] == "player_456"
            assert logged_entry["reason"] == "Inappropriate language"
            assert logged_entry["warning_level"] == "first"

    def test_log_message_flagged(self):
        """Test logging a flagged message."""
        message_id = "msg_123"
        flag_reason = "profanity"
        confidence = 0.85
        ai_model = "content_filter_v2"
        action_taken = "muted"

        # Log the flagged message
        self.chat_logger.log_message_flagged(message_id, flag_reason, confidence, ai_model, action_taken)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == "message_flagged"
            assert logged_entry["message_id"] == message_id
            assert logged_entry["flag_reason"] == flag_reason
            assert logged_entry["confidence"] == confidence
            assert logged_entry["ai_model"] == ai_model
            assert logged_entry["action_taken"] == action_taken
            assert logged_entry["moderator_id"] == "ai_system"

    def test_log_message_flagged_defaults(self):
        """Test logging a flagged message with default values."""
        message_id = "msg_123"
        flag_reason = "spam"

        # Log the flagged message with defaults
        self.chat_logger.log_message_flagged(message_id, flag_reason)

        # Verify log entry has default values
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["confidence"] == 0.0
            assert logged_entry["ai_model"] == "content_filter_v1"
            assert logged_entry["action_taken"] == "none"

    def test_log_player_muted(self):
        """Test logging a player mute action."""
        muter_id = "mod_123"
        target_id = "player_456"
        target_name = "TestPlayer"
        mute_type = "channel"
        duration_minutes = 30
        reason = "Spam in global chat"

        # Log the mute
        self.chat_logger.log_player_muted(muter_id, target_id, target_name, mute_type, duration_minutes, reason)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == "player_muted"
            assert logged_entry["muter_id"] == muter_id
            assert logged_entry["target_id"] == target_id
            assert logged_entry["target_name"] == target_name
            assert logged_entry["mute_type"] == mute_type
            assert logged_entry["duration_minutes"] == duration_minutes
            assert logged_entry["reason"] == reason
            assert "timestamp" in logged_entry

    def test_log_player_muted_permanent(self):
        """Test logging a permanent player mute."""
        muter_id = "mod_123"
        target_id = "player_456"
        target_name = "TestPlayer"
        mute_type = "global"

        # Log the permanent mute
        self.chat_logger.log_player_muted(muter_id, target_id, target_name, mute_type)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["duration_minutes"] is None
            assert logged_entry["reason"] == ""

    def test_log_player_unmuted(self):
        """Test logging a player unmute action."""
        unmuter_id = "mod_123"
        target_id = "player_456"
        target_name = "TestPlayer"
        mute_type = "channel"

        # Log the unmute
        self.chat_logger.log_player_unmuted(unmuter_id, target_id, target_name, mute_type)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == "player_unmuted"
            assert logged_entry["unmuter_id"] == unmuter_id
            assert logged_entry["target_id"] == target_id
            assert logged_entry["target_name"] == target_name
            assert logged_entry["mute_type"] == mute_type
            assert "timestamp" in logged_entry

    def test_log_system_event(self):
        """Test logging a system event."""
        event_type = "server_startup"
        event_data = {"version": "1.0.0", "uptime": 3600, "active_players": 25}

        # Log the system event
        self.chat_logger.log_system_event(event_type, event_data)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("system")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == event_type
            assert logged_entry["version"] == "1.0.0"
            assert logged_entry["uptime"] == 3600
            assert logged_entry["active_players"] == 25

    def test_log_player_joined_room(self):
        """Test logging when a player joins a room."""
        player_id = "player_123"
        player_name = "TestPlayer"
        room_id = "room_456"
        room_name = "Arkham Library"

        # Log the room join
        self.chat_logger.log_player_joined_room(player_id, player_name, room_id, room_name)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("system")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == "player_joined_room"
            assert logged_entry["player_id"] == player_id
            assert logged_entry["player_name"] == player_name
            assert logged_entry["room_id"] == room_id
            assert logged_entry["room_name"] == room_name

    def test_log_player_left_room(self):
        """Test logging when a player leaves a room."""
        player_id = "player_123"
        player_name = "TestPlayer"
        room_id = "room_456"
        room_name = "Arkham Library"

        # Log the room leave
        self.chat_logger.log_player_left_room(player_id, player_name, room_id, room_name)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("system")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == "player_left_room"
            assert logged_entry["player_id"] == player_id
            assert logged_entry["player_name"] == player_name
            assert logged_entry["room_id"] == room_id
            assert logged_entry["room_name"] == room_name

    def test_log_rate_limit_violation(self):
        """Test logging a rate limit violation."""
        player_id = "player_123"
        player_name = "TestPlayer"
        channel = "say"
        message_count = 15
        limit = 10

        # Log the rate limit violation
        self.chat_logger.log_rate_limit_violation(player_id, player_name, channel, message_count, limit)

        # Verify log entry
        log_file = self.chat_logger._get_current_log_file("moderation")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            logged_entry = json.loads(lines[0].strip())

            assert logged_entry["event_type"] == "rate_limit_violation"
            assert logged_entry["player_id"] == player_id
            assert logged_entry["player_name"] == player_name
            assert logged_entry["channel"] == channel
            assert logged_entry["message_count"] == message_count
            assert logged_entry["limit"] == limit

    def test_get_log_file_paths(self):
        """Test getting current log file paths."""
        paths = self.chat_logger.get_log_file_paths()

        assert "chat" in paths
        assert "moderation" in paths
        assert "system" in paths

        # Verify paths are correct
        today = datetime.now(UTC).strftime("%Y-%m-%d")
        assert paths["chat"] == self.chat_logger.chat_dir / f"chat_{today}.log"
        assert paths["moderation"] == self.chat_logger.moderation_dir / f"moderation_{today}.log"
        assert paths["system"] == self.chat_logger.system_dir / f"system_{today}.log"

    def test_get_log_stats_empty_files(self):
        """Test getting log stats for empty log files."""
        stats = self.chat_logger.get_log_stats()

        assert "chat" in stats
        assert "moderation" in stats
        assert "system" in stats

        # Verify stats for empty files
        for log_type in ["chat", "moderation", "system"]:
            assert stats[log_type]["file_size_bytes"] == 0
            assert stats[log_type]["last_modified"] is None
            assert "file_path" in stats[log_type]

    def test_get_log_stats_with_data(self):
        """Test getting log stats for files with data."""
        # Write some test data
        test_entry = {"test": "data"}
        self.chat_logger._write_log_entry("chat", test_entry)
        self.chat_logger._write_log_entry("moderation", test_entry)

        stats = self.chat_logger.get_log_stats()

        # Verify chat file has data
        assert stats["chat"]["file_size_bytes"] > 0
        assert stats["chat"]["last_modified"] is not None

        # Verify moderation file has data
        assert stats["moderation"]["file_size_bytes"] > 0
        assert stats["moderation"]["last_modified"] is not None

        # Verify system file is still empty
        assert stats["system"]["file_size_bytes"] == 0
        assert stats["system"]["last_modified"] is None

    def test_multiple_log_entries_same_file(self):
        """Test writing multiple entries to the same log file."""
        entries = [
            {"message": "First message", "id": 1},
            {"message": "Second message", "id": 2},
            {"message": "Third message", "id": 3},
        ]

        # Write multiple entries
        for entry in entries:
            self.chat_logger._write_log_entry("chat", entry)

        # Verify all entries were written
        log_file = self.chat_logger._get_current_log_file("chat")
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            assert len(lines) == 3

            for i, line in enumerate(lines):
                logged_entry = json.loads(line.strip())
                assert logged_entry["message"] == entries[i]["message"]
                assert logged_entry["id"] == entries[i]["id"]

    def test_log_entries_across_different_types(self):
        """Test writing entries to different log types."""
        # Write entries to different log types
        self.chat_logger._write_log_entry("chat", {"type": "chat", "id": 1})
        self.chat_logger._write_log_entry("moderation", {"type": "moderation", "id": 2})
        self.chat_logger._write_log_entry("system", {"type": "system", "id": 3})

        # Verify each file contains the correct entry
        chat_file = self.chat_logger._get_current_log_file("chat")
        with open(chat_file, encoding="utf-8") as f:
            entry = json.loads(f.readline().strip())
            assert entry["type"] == "chat"

        moderation_file = self.chat_logger._get_current_log_file("moderation")
        with open(moderation_file, encoding="utf-8") as f:
            entry = json.loads(f.readline().strip())
            assert entry["type"] == "moderation"

        system_file = self.chat_logger._get_current_log_file("system")
        with open(system_file, encoding="utf-8") as f:
            entry = json.loads(f.readline().strip())
            assert entry["type"] == "system"

    def test_ensure_log_directories_creates_missing_dirs(self):
        """Test that _ensure_log_directories creates missing directories."""
        # Remove directories
        import shutil

        shutil.rmtree(self.log_dir / "chat", ignore_errors=True)
        shutil.rmtree(self.log_dir / "moderation", ignore_errors=True)
        shutil.rmtree(self.log_dir / "system", ignore_errors=True)

        # Recreate directories
        self.chat_logger._ensure_log_directories()

        # Verify directories exist
        assert (self.log_dir / "chat").exists()
        assert (self.log_dir / "moderation").exists()
        assert (self.log_dir / "system").exists()

    def test_ensure_log_directories_handles_existing_dirs(self):
        """Test that _ensure_log_directories handles existing directories gracefully."""
        # Call multiple times - should not raise errors
        self.chat_logger._ensure_log_directories()
        self.chat_logger._ensure_log_directories()
        self.chat_logger._ensure_log_directories()

        # Verify directories still exist
        assert (self.log_dir / "chat").exists()
        assert (self.log_dir / "moderation").exists()
        assert (self.log_dir / "system").exists()


class TestChatLoggerGlobalInstance:
    """Test the global chat_logger instance."""

    def test_global_chat_logger_instance(self):
        """Test that the global chat_logger instance is created correctly."""
        from server.services.chat_logger import chat_logger

        # Verify it's a ChatLogger instance
        assert isinstance(chat_logger, ChatLogger)

        # Verify it has the expected attributes
        assert hasattr(chat_logger, "log_dir")
        assert hasattr(chat_logger, "chat_dir")
        assert hasattr(chat_logger, "moderation_dir")
        assert hasattr(chat_logger, "system_dir")
