"""
Tests for admin actions logger.

This module tests the admin actions logging functionality including
teleport action logging, permission checks, and log retrieval.
"""

import json
import tempfile
from datetime import datetime
from pathlib import Path
from unittest.mock import patch

from server.logging.admin_actions_logger import AdminActionsLogger, get_admin_actions_logger


class TestAdminActionsLogger:
    """Test admin actions logger functionality."""

    def setup_method(self):
        """Set up test environment."""
        # Create a temporary directory for test logs
        self.temp_dir = tempfile.mkdtemp()
        self.logger = AdminActionsLogger(log_directory=self.temp_dir)

    def teardown_method(self):
        """Clean up test environment."""
        # Remove temporary directory and files
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_logger_initialization(self):
        """Test logger initialization."""
        assert self.logger.log_directory == Path(self.temp_dir)
        assert self.logger.log_directory.exists()

    def test_get_log_file_path(self):
        """Test log file path generation."""
        today = datetime.now().strftime("%Y-%m-%d")
        expected_path = Path(self.temp_dir) / f"admin_actions_{today}.log"
        assert self.logger._get_log_file_path() == expected_path

    def test_ensure_log_file_exists(self):
        """Test log file creation."""
        log_file = self.logger._get_log_file_path()

        # File should not exist initially
        assert not log_file.exists()

        # Create the file
        self.logger._ensure_log_file_exists()

        # File should now exist
        assert log_file.exists()

        # Check file header
        with open(log_file, encoding="utf-8") as f:
            content = f.read()
            assert "# MythosMUD Admin Actions Log" in content
            assert "# Format: JSON lines" in content

    def test_log_teleport_action_success(self):
        """Test logging successful teleport action."""
        self.logger.log_teleport_action(
            admin_name="TestAdmin",
            target_player="TestPlayer",
            action_type="teleport",
            from_room="room_1",
            to_room="room_2",
            success=True,
            additional_data={"test": "data"}
        )

        # Check that log file was created
        log_file = self.logger._get_log_file_path()
        assert log_file.exists()

        # Read and parse the log entry
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            # Skip header lines
            json_lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

        assert len(json_lines) == 1

        entry = json.loads(json_lines[0])
        assert entry["action_type"] == "teleport"
        assert entry["teleport_type"] == "teleport"
        assert entry["admin_name"] == "TestAdmin"
        assert entry["target_player"] == "TestPlayer"
        assert entry["from_room"] == "room_1"
        assert entry["to_room"] == "room_2"
        assert entry["success"] is True
        assert entry["additional_data"]["test"] == "data"
        assert "timestamp" in entry

    def test_log_teleport_action_failure(self):
        """Test logging failed teleport action."""
        self.logger.log_teleport_action(
            admin_name="TestAdmin",
            target_player="TestPlayer",
            action_type="goto",
            from_room="room_1",
            to_room="room_2",
            success=False,
            error_message="Player not found",
            additional_data={"error_code": 404}
        )

        log_file = self.logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            json_lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

        entry = json.loads(json_lines[0])
        assert entry["action_type"] == "teleport"
        assert entry["teleport_type"] == "goto"
        assert entry["success"] is False
        assert entry["error_message"] == "Player not found"
        assert entry["additional_data"]["error_code"] == 404

    def test_log_admin_command(self):
        """Test logging admin command."""
        self.logger.log_admin_command(
            admin_name="TestAdmin",
            command="mute TestPlayer",
            target_player="TestPlayer",
            success=True,
            additional_data={"duration": "1h"}
        )

        log_file = self.logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            json_lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

        entry = json.loads(json_lines[0])
        assert entry["action_type"] == "admin_command"
        assert entry["admin_name"] == "TestAdmin"
        assert entry["command"] == "mute TestPlayer"
        assert entry["target_player"] == "TestPlayer"
        assert entry["success"] is True
        assert entry["additional_data"]["duration"] == "1h"

    def test_log_permission_check(self):
        """Test logging permission check."""
        self.logger.log_permission_check(
            player_name="TestPlayer",
            action="admin_teleport",
            has_permission=False,
            additional_data={"reason": "Not admin"}
        )

        log_file = self.logger._get_log_file_path()
        with open(log_file, encoding="utf-8") as f:
            lines = f.readlines()
            json_lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

        entry = json.loads(json_lines[0])
        assert entry["action_type"] == "permission_check"
        assert entry["player_name"] == "TestPlayer"
        assert entry["action"] == "admin_teleport"
        assert entry["has_permission"] is False
        assert entry["additional_data"]["reason"] == "Not admin"

    def test_log_entry_error_handling(self):
        """Test error handling in log entry writing."""
        # Mock file operations to raise an exception
        with patch("builtins.open", side_effect=Exception("File error")):
            # Should not raise an exception
            self.logger.log_teleport_action(
                admin_name="TestAdmin",
                target_player="TestPlayer",
                action_type="teleport",
                from_room="room_1",
                to_room="room_2",
                success=True
            )

    def test_get_recent_actions(self):
        """Test retrieving recent actions."""
        # Create some test log entries
        self.logger.log_teleport_action(
            admin_name="Admin1",
            target_player="Player1",
            action_type="teleport",
            from_room="room_1",
            to_room="room_2",
            success=True
        )

        self.logger.log_teleport_action(
            admin_name="Admin2",
            target_player="Player2",
            action_type="goto",
            from_room="room_3",
            to_room="room_4",
            success=True
        )

        # Get recent actions
        actions = self.logger.get_recent_actions(hours=24)
        assert len(actions) == 2

        # Filter by action type
        teleport_actions = self.logger.get_recent_actions(hours=24, action_type="teleport")
        assert len(teleport_actions) == 2  # Both are teleport actions

        # Filter by admin name
        admin1_actions = self.logger.get_recent_actions(hours=24, admin_name="Admin1")
        assert len(admin1_actions) == 1
        assert admin1_actions[0]["admin_name"] == "Admin1"

    def test_get_teleport_statistics(self):
        """Test teleport statistics generation."""
        # Create test data
        self.logger.log_teleport_action(
            admin_name="Admin1",
            target_player="Player1",
            action_type="teleport",
            from_room="room_1",
            to_room="room_2",
            success=True
        )

        self.logger.log_teleport_action(
            admin_name="Admin1",
            target_player="Player2",
            action_type="goto",
            from_room="room_3",
            to_room="room_4",
            success=True
        )

        self.logger.log_teleport_action(
            admin_name="Admin2",
            target_player="Player3",
            action_type="teleport",
            from_room="room_5",
            to_room="room_6",
            success=False
        )

        # Get statistics
        stats = self.logger.get_teleport_statistics(hours=24)

        assert stats["total_teleports"] == 3
        assert stats["successful_teleports"] == 2
        assert stats["failed_teleports"] == 1
        assert stats["teleport_types"]["teleport"] == 2
        assert stats["teleport_types"]["goto"] == 1
        assert stats["admin_activity"]["Admin1"] == 2
        assert stats["admin_activity"]["Admin2"] == 1
        assert stats["target_players"]["Player1"] == 1
        assert stats["target_players"]["Player2"] == 1
        assert stats["target_players"]["Player3"] == 1

    def test_log_file_rotation(self):
        """Test log file rotation to new day."""
        # Create two loggers with different dates to simulate rotation
        with patch("server.logging.admin_actions_logger.datetime") as mock_datetime:
            # First logger with first date
            mock_datetime.now.return_value = datetime(2025, 1, 27, 12, 0, 0)
            mock_datetime.strftime = datetime.strftime

            logger1 = AdminActionsLogger(log_directory=self.temp_dir)
            logger1.log_teleport_action(
                admin_name="Admin1",
                target_player="Player1",
                action_type="teleport",
                from_room="room_1",
                to_room="room_2",
                success=True
            )

            # Second logger with second date
            mock_datetime.now.return_value = datetime(2025, 1, 28, 12, 0, 0)

            logger2 = AdminActionsLogger(log_directory=self.temp_dir)
            logger2.log_teleport_action(
                admin_name="Admin2",
                target_player="Player2",
                action_type="goto",
                from_room="room_3",
                to_room="room_4",
                success=True
            )

            # Check that both log files exist
            log_file_1 = Path(self.temp_dir) / "admin_actions_2025-01-27.log"
            log_file_2 = Path(self.temp_dir) / "admin_actions_2025-01-28.log"

            assert log_file_1.exists()
            assert log_file_2.exists()


class TestGlobalAdminActionsLogger:
    """Test global admin actions logger instance."""

    def test_get_admin_actions_logger_singleton(self):
        """Test that get_admin_actions_logger returns a singleton."""
        logger1 = get_admin_actions_logger()
        logger2 = get_admin_actions_logger()

        assert logger1 is logger2
        assert isinstance(logger1, AdminActionsLogger)

    def test_global_logger_functionality(self):
        """Test global logger functionality."""
        logger = get_admin_actions_logger()

        # Test that it can log actions
        with tempfile.TemporaryDirectory() as temp_dir:
            with patch.object(logger, "log_directory", Path(temp_dir)):
                logger.log_teleport_action(
                    admin_name="TestAdmin",
                    target_player="TestPlayer",
                    action_type="teleport",
                    from_room="room_1",
                    to_room="room_2",
                    success=True
                )

                # Verify log was written
                log_file = logger._get_log_file_path()
                assert log_file.exists()


class TestAdminActionsLoggerIntegration:
    """Integration tests for admin actions logger."""

    def test_full_logging_workflow(self):
        """Test complete logging workflow."""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = AdminActionsLogger(log_directory=temp_dir)

            # Log various types of actions
            logger.log_teleport_action(
                admin_name="Admin1",
                target_player="Player1",
                action_type="teleport",
                from_room="room_1",
                to_room="room_2",
                success=True
            )

            logger.log_admin_command(
                admin_name="Admin2",
                command="mute Player2",
                target_player="Player2",
                success=True
            )

            logger.log_permission_check(
                player_name="Player3",
                action="admin_teleport",
                has_permission=False
            )

            # Retrieve and verify all actions
            actions = logger.get_recent_actions(hours=24)
            assert len(actions) == 3

            # Check action types
            action_types = [action["action_type"] for action in actions]
            assert "teleport" in action_types
            assert "admin_command" in action_types
            assert "permission_check" in action_types

            # Check admin names
            admin_names = [action.get("admin_name") for action in actions if "admin_name" in action]
            assert "Admin1" in admin_names
            assert "Admin2" in admin_names

    def test_error_recovery(self):
        """Test logger recovery from errors."""
        with tempfile.TemporaryDirectory() as temp_dir:
            logger = AdminActionsLogger(log_directory=temp_dir)

            # Log a successful action
            logger.log_teleport_action(
                admin_name="Admin1",
                target_player="Player1",
                action_type="teleport",
                from_room="room_1",
                to_room="room_2",
                success=True
            )

            # Simulate a file system error
            with patch("builtins.open", side_effect=Exception("File system error")):
                # Should handle error gracefully
                logger.log_teleport_action(
                    admin_name="Admin2",
                    target_player="Player2",
                    action_type="goto",
                    from_room="room_3",
                    to_room="room_4",
                    success=True
                )

            # Should still be able to log after error
            logger.log_teleport_action(
                admin_name="Admin3",
                target_player="Player3",
                action_type="teleport",
                from_room="room_5",
                to_room="room_6",
                success=True
            )

            # Verify logs were written
            actions = logger.get_recent_actions(hours=24)
            assert len(actions) >= 1  # At least the successful logs
