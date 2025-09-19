"""
Tests for the user manager functionality.

This module tests the UserManager class which handles player muting, channel muting,
permissions, and user state tracking for the chat system.
"""

import json
import tempfile
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import Mock, patch

from ..services.user_manager import UserManager


class TestUserManager:
    """Test cases for UserManager."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a temporary directory for test data
        self.temp_dir = tempfile.mkdtemp()
        self.test_data_dir = Path(self.temp_dir) / "user_management"
        self.test_data_dir.mkdir(parents=True, exist_ok=True)

        # Create the user manager instance with test data directory
        self.user_manager = UserManager(data_dir=self.test_data_dir)

        # Mock chat logger
        self.mock_chat_logger = Mock()
        self.user_manager.chat_logger = self.mock_chat_logger

        # Clear admin cache to ensure clean state between tests
        self.user_manager._admin_players.clear()

    def teardown_method(self):
        """Clean up test fixtures."""
        # Clean up temporary directory
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_initialization(self):
        """Test UserManager initialization."""
        assert self.user_manager._player_mutes == {}
        assert self.user_manager._channel_mutes == {}
        assert self.user_manager._global_mutes == {}
        assert self.user_manager._admin_players == set()
        assert self.user_manager.chat_logger is not None
        assert self.user_manager.data_dir == self.test_data_dir

    @patch("server.persistence.get_persistence")
    def test_add_admin_success(self, mock_get_persistence):
        """Test successful admin addition."""
        # Mock persistence and player
        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.set_admin_status = Mock()
        mock_persistence.get_player.return_value = mock_player
        mock_get_persistence.return_value = mock_persistence

        result = self.user_manager.add_admin("player_001", "TestPlayer")

        assert result is True
        assert "player_001" in self.user_manager._admin_players
        mock_player.set_admin_status.assert_called_once_with(True)
        mock_persistence.save_player.assert_called_once_with(mock_player)

    @patch("server.persistence.get_persistence")
    def test_add_admin_player_not_found(self, mock_get_persistence):
        """Test admin addition when player not found."""
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = None
        mock_get_persistence.return_value = mock_persistence

        result = self.user_manager.add_admin("player_001", "TestPlayer")

        assert result is False
        assert "player_001" not in self.user_manager._admin_players

    @patch("server.persistence.get_persistence")
    def test_add_admin_with_exception(self, mock_get_persistence):
        """Test admin addition when exception occurs."""
        mock_get_persistence.side_effect = Exception("Database error")

        result = self.user_manager.add_admin("player_001", "TestPlayer")

        assert result is False

    @patch("server.persistence.get_persistence")
    def test_remove_admin_success(self, mock_get_persistence):
        """Test successful admin removal."""
        # Add admin first
        self.user_manager._admin_players.add("player_001")

        # Mock persistence and player
        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.set_admin_status = Mock()
        mock_persistence.get_player.return_value = mock_player
        mock_get_persistence.return_value = mock_persistence

        result = self.user_manager.remove_admin("player_001", "TestPlayer")

        assert result is True
        assert "player_001" not in self.user_manager._admin_players
        mock_player.set_admin_status.assert_called_once_with(False)
        mock_persistence.save_player.assert_called_once_with(mock_player)

    @patch("server.persistence.get_persistence")
    def test_remove_admin_player_not_found(self, mock_get_persistence):
        """Test admin removal when player not found."""
        mock_persistence = Mock()
        mock_persistence.get_player.return_value = None
        mock_get_persistence.return_value = mock_persistence

        result = self.user_manager.remove_admin("player_001", "TestPlayer")

        assert result is False

    def test_is_admin_in_memory_cache(self):
        """Test admin check using in-memory cache."""
        self.user_manager._admin_players.add("player_001")

        result = self.user_manager.is_admin("player_001")

        assert result is True

    @patch("server.persistence.get_persistence")
    def test_is_admin_from_database(self, mock_get_persistence):
        """Test admin check from database."""
        # Mock persistence and player
        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.is_admin_user.return_value = True
        mock_persistence.get_player.return_value = mock_player
        mock_get_persistence.return_value = mock_persistence

        result = self.user_manager.is_admin("player_001")

        assert result is True
        assert "player_001" in self.user_manager._admin_players

    @patch("server.persistence.get_persistence")
    def test_is_admin_not_admin(self, mock_get_persistence):
        """Test admin check for non-admin player."""
        # Ensure admin cache is clear for this test
        self.user_manager._admin_players.clear()

        mock_persistence = Mock()
        mock_player = Mock()
        mock_player.is_admin_user.return_value = False
        mock_persistence.get_player.return_value = mock_player
        mock_get_persistence.return_value = mock_persistence

        result = self.user_manager.is_admin("player_001")

        assert result is False
        assert "player_001" not in self.user_manager._admin_players

    @patch("server.persistence.get_persistence")
    def test_is_admin_with_exception(self, mock_get_persistence):
        """Test admin check when exception occurs."""
        mock_get_persistence.side_effect = Exception("Database error")

        result = self.user_manager.is_admin("player_001")

        assert result is False

    def test_mute_player_success(self):
        """Test successful player muting."""
        result = self.user_manager.mute_player(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="TargetPlayer",
            duration_minutes=30,
            reason="Spam",
        )

        assert result is True
        assert "player_001" in self.user_manager._player_mutes
        assert "player_002" in self.user_manager._player_mutes["player_001"]

        mute_info = self.user_manager._player_mutes["player_001"]["player_002"]
        assert mute_info["target_id"] == "player_002"
        assert mute_info["target_name"] == "TargetPlayer"
        assert mute_info["muted_by"] == "player_001"
        assert mute_info["muted_by_name"] == "MuterPlayer"
        assert mute_info["reason"] == "Spam"
        assert mute_info["is_permanent"] is False
        assert mute_info["expires_at"] is not None

    def test_mute_player_permanent(self):
        """Test permanent player muting."""
        result = self.user_manager.mute_player(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="TargetPlayer",
            reason="Harassment",
        )

        assert result is True
        mute_info = self.user_manager._player_mutes["player_001"]["player_002"]
        assert mute_info["is_permanent"] is True
        assert mute_info["expires_at"] is None

    def test_mute_player_admin_immune(self):
        """Test that admin players are immune to muting."""
        # Add target as admin
        self.user_manager._admin_players.add("player_002")

        result = self.user_manager.mute_player(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="AdminPlayer",
            reason="Test",
        )

        assert result is False
        assert "player_001" not in self.user_manager._player_mutes

    def test_mute_player_with_exception(self):
        """Test player muting when exception occurs."""
        # Mock save_player_mutes to raise exception
        with patch.object(self.user_manager, "save_player_mutes", side_effect=Exception("Save error")):
            result = self.user_manager.mute_player(
                muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
            )

            assert result is False

    def test_unmute_player_success(self):
        """Test successful player unmuting."""
        # First mute the player
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        # Then unmute
        result = self.user_manager.unmute_player(
            unmuter_id="player_001", unmuter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        assert result is True
        assert "player_001" not in self.user_manager._player_mutes

    def test_unmute_player_not_muted(self):
        """Test unmuting a player that wasn't muted."""
        result = self.user_manager.unmute_player(
            unmuter_id="player_001", unmuter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        assert result is False

    def test_mute_channel_success(self):
        """Test successful channel muting."""
        result = self.user_manager.mute_channel(
            player_id="player_001", player_name="TestPlayer", channel="global", duration_minutes=60, reason="Too noisy"
        )

        assert result is True
        assert "player_001" in self.user_manager._channel_mutes
        assert "global" in self.user_manager._channel_mutes["player_001"]

        mute_info = self.user_manager._channel_mutes["player_001"]["global"]
        assert mute_info["channel"] == "global"
        assert mute_info["reason"] == "Too noisy"
        assert mute_info["is_permanent"] is False

    def test_mute_channel_permanent(self):
        """Test permanent channel muting."""
        result = self.user_manager.mute_channel(
            player_id="player_001", player_name="TestPlayer", channel="say", reason="Annoying"
        )

        assert result is True
        mute_info = self.user_manager._channel_mutes["player_001"]["say"]
        assert mute_info["is_permanent"] is True
        assert mute_info["expires_at"] is None

    def test_unmute_channel_success(self):
        """Test successful channel unmuting."""
        # First mute the channel
        self.user_manager.mute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        # Then unmute
        result = self.user_manager.unmute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        assert result is True
        assert "player_001" not in self.user_manager._channel_mutes

    def test_unmute_channel_not_muted(self):
        """Test unmuting a channel that wasn't muted."""
        result = self.user_manager.unmute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        assert result is False

    def test_mute_global_success(self):
        """Test successful global muting."""
        result = self.user_manager.mute_global(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="TargetPlayer",
            duration_minutes=120,
            reason="Severe violation",
        )

        assert result is True
        assert "player_002" in self.user_manager._global_mutes

        mute_info = self.user_manager._global_mutes["player_002"]
        assert mute_info["target_id"] == "player_002"
        assert mute_info["muted_by"] == "player_001"
        assert mute_info["reason"] == "Severe violation"
        assert mute_info["is_permanent"] is False

    def test_mute_global_admin_immune(self):
        """Test that admin players are immune to global muting."""
        # Add target as admin
        self.user_manager._admin_players.add("player_002")

        result = self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="AdminPlayer"
        )

        assert result is False
        assert "player_002" not in self.user_manager._global_mutes

    def test_unmute_global_success(self):
        """Test successful global unmuting."""
        # First apply global mute
        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        # Then remove it
        result = self.user_manager.unmute_global(
            unmuter_id="player_001", unmuter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        assert result is True
        assert "player_002" not in self.user_manager._global_mutes

    def test_unmute_global_not_muted(self):
        """Test removing global mute that doesn't exist."""
        result = self.user_manager.unmute_global(
            unmuter_id="player_001", unmuter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        assert result is False

    def test_is_player_muted_active(self):
        """Test checking if a player is actively muted."""
        # Mute a player
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        result = self.user_manager.is_player_muted("player_001", "player_002")

        assert result is True

    def test_is_player_muted_expired(self):
        """Test checking if a player is muted with expired mute."""
        # Mute a player with short duration
        self.user_manager.mute_player(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="TargetPlayer",
            duration_minutes=1,
        )

        # Manually expire the mute
        mute_info = self.user_manager._player_mutes["player_001"]["player_002"]
        mute_info["expires_at"] = datetime.now(UTC) - timedelta(minutes=1)

        # Mock the load_player_mutes method to avoid database calls
        with patch.object(self.user_manager, "load_player_mutes"):
            result = self.user_manager.is_player_muted("player_001", "player_002")

            assert result is False
            # Should be cleaned up
            assert "player_001" not in self.user_manager._player_mutes

    def test_is_player_muted_not_muted(self):
        """Test checking if a player is muted when not muted."""
        result = self.user_manager.is_player_muted("player_001", "player_002")

        assert result is False

    def test_is_channel_muted_active(self):
        """Test checking if a channel is actively muted."""
        # Mute a channel
        self.user_manager.mute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        result = self.user_manager.is_channel_muted("player_001", "global")

        assert result is True

    def test_is_channel_muted_expired(self):
        """Test checking if a channel is muted with expired mute."""
        # Mute a channel with short duration
        self.user_manager.mute_channel(
            player_id="player_001", player_name="TestPlayer", channel="global", duration_minutes=1
        )

        # Manually expire the mute
        mute_info = self.user_manager._channel_mutes["player_001"]["global"]
        mute_info["expires_at"] = datetime.now(UTC) - timedelta(minutes=1)

        result = self.user_manager.is_channel_muted("player_001", "global")

        assert result is False
        # Should be cleaned up
        assert "player_001" not in self.user_manager._channel_mutes

    def test_is_globally_muted_active(self):
        """Test checking if a player is actively globally muted."""
        # Apply global mute
        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        result = self.user_manager.is_globally_muted("player_002")

        assert result is True

    def test_is_globally_muted_expired(self):
        """Test checking if a player is globally muted with expired mute."""
        # Apply global mute with short duration
        self.user_manager.mute_global(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="TargetPlayer",
            duration_minutes=1,
        )

        # Manually expire the mute
        mute_info = self.user_manager._global_mutes["player_002"]
        mute_info["expires_at"] = datetime.now(UTC) - timedelta(minutes=1)

        result = self.user_manager.is_globally_muted("player_002")

        assert result is False
        # Should be cleaned up
        assert "player_002" not in self.user_manager._global_mutes

    def test_can_send_message_admin(self):
        """Test that admins can always send messages."""
        self.user_manager._admin_players.add("player_001")

        result = self.user_manager.can_send_message("player_001")

        assert result is True

    def test_can_send_message_globally_muted(self):
        """Test that globally muted players cannot send messages."""
        # Apply global mute
        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        result = self.user_manager.can_send_message("player_002")

        assert result is False

    def test_can_send_message_channel_muted(self):
        """Test that channel muted players cannot send to that channel."""
        # Mute a channel
        self.user_manager.mute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        result = self.user_manager.can_send_message("player_001", channel="global")

        assert result is False

    def test_can_send_message_normal(self):
        """Test that normal players can send messages."""
        result = self.user_manager.can_send_message("player_001")

        assert result is True

    def test_get_player_mutes(self):
        """Test getting all mutes for a player."""
        # Add various mutes
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        self.user_manager.mute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_003", target_name="GlobalTarget"
        )

        mutes = self.user_manager.get_player_mutes("player_001")

        assert len(mutes["player_mutes"]) == 1
        assert len(mutes["channel_mutes"]) == 1
        assert len(mutes["global_mutes"]) == 1
        assert "player_002" in mutes["player_mutes"]
        assert "global" in mutes["channel_mutes"]
        assert "player_003" in mutes["global_mutes"]

    def test_get_player_mutes_empty(self):
        """Test getting mutes for player with no mutes."""
        mutes = self.user_manager.get_player_mutes("player_001")

        assert mutes["player_mutes"] == {}
        assert mutes["channel_mutes"] == {}
        assert mutes["global_mutes"] == {}

    def test_is_player_muted_by_others_true(self):
        """Test checking if player is muted by others."""
        # Apply global mute
        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        result = self.user_manager.is_player_muted_by_others("player_002")

        assert result is True

    def test_is_player_muted_by_others_false(self):
        """Test checking if player is not muted by others."""
        result = self.user_manager.is_player_muted_by_others("player_001")

        assert result is False

    def test_get_who_muted_player(self):
        """Test getting information about who muted a player."""
        # Apply global mute
        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        # Apply personal mute
        self.user_manager.mute_player(
            muter_id="player_003", muter_name="AnotherMuter", target_id="player_002", target_name="TargetPlayer"
        )

        muted_by = self.user_manager.get_who_muted_player("player_002")

        assert len(muted_by) == 2
        muter_names = [muter[0] for muter in muted_by]
        assert "MuterPlayer" in muter_names
        assert "AnotherMuter" in muter_names

    def test_get_system_stats(self):
        """Test getting system statistics."""
        # Add some test data
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        self.user_manager.mute_channel(player_id="player_003", player_name="TestPlayer", channel="global")

        self.user_manager.mute_global(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_004", target_name="GlobalTarget"
        )

        self.user_manager._admin_players.add("player_001")

        stats = self.user_manager.get_system_stats()

        assert stats["total_players_with_mutes"] == 1
        assert stats["total_channel_mutes"] == 1
        assert stats["total_global_mutes"] == 1
        assert stats["total_admin_players"] == 1
        assert "player_001" in stats["admin_players"]

    def test_cleanup_expired_mutes(self):
        """Test cleanup of expired mutes."""
        # Add expired mutes
        self.user_manager._player_mutes["player_001"] = {
            "player_002": {"target_id": "player_002", "expires_at": datetime.now(UTC) - timedelta(minutes=1)}
        }

        self.user_manager._channel_mutes["player_001"] = {
            "global": {"channel": "global", "expires_at": datetime.now(UTC) - timedelta(minutes=1)}
        }

        self.user_manager._global_mutes["player_003"] = {
            "target_id": "player_003",
            "expires_at": datetime.now(UTC) - timedelta(minutes=1),
        }

        # Clean up
        self.user_manager._cleanup_expired_mutes()

        assert "player_001" not in self.user_manager._player_mutes
        assert "player_001" not in self.user_manager._channel_mutes
        assert "player_003" not in self.user_manager._global_mutes

    def test_get_player_mute_file(self):
        """Test getting player mute file path."""
        file_path = self.user_manager._get_player_mute_file("player_001")

        expected_path = self.test_data_dir / "mutes_player_001.json"
        assert file_path == expected_path

    def test_load_player_mutes_file_not_exists(self):
        """Test loading player mutes when file doesn't exist."""
        result = self.user_manager.load_player_mutes("player_001")

        assert result is False

    def test_load_player_mutes_success(self):
        """Test successful loading of player mutes."""
        # Create test data
        test_data = {
            "player_id": "player_001",
            "last_updated": datetime.now(UTC).isoformat(),
            "player_mutes": {
                "player_002": {
                    "target_id": "player_002",
                    "target_name": "TargetPlayer",
                    "muted_by": "player_001",
                    "muted_by_name": "MuterPlayer",
                    "muted_at": datetime.now(UTC).isoformat(),
                    "expires_at": None,
                    "reason": "Test",
                    "is_permanent": True,
                }
            },
            "channel_mutes": {
                "global": {
                    "channel": "global",
                    "muted_at": datetime.now(UTC).isoformat(),
                    "expires_at": None,
                    "reason": "Test",
                    "is_permanent": True,
                }
            },
            "global_mutes": {},
            "is_admin": True,
        }

        # Write test file
        mute_file = self.user_manager._get_player_mute_file("player_001")
        with open(mute_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f)

        # Load mutes
        result = self.user_manager.load_player_mutes("player_001")

        assert result is True
        assert "player_001" in self.user_manager._player_mutes
        assert "player_002" in self.user_manager._player_mutes["player_001"]
        assert "player_001" in self.user_manager._channel_mutes
        assert "global" in self.user_manager._channel_mutes["player_001"]
        assert "player_001" in self.user_manager._admin_players

    def test_save_player_mutes_success(self):
        """Test successful saving of player mutes."""
        # Add some test data
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        self.user_manager.mute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        self.user_manager._admin_players.add("player_001")

        # Save mutes
        result = self.user_manager.save_player_mutes("player_001")

        assert result is True

        # Verify file was created
        mute_file = self.user_manager._get_player_mute_file("player_001")
        assert mute_file.exists()

        # Verify file contents
        with open(mute_file, encoding="utf-8") as f:
            data = json.load(f)

        assert data["player_id"] == "player_001"
        assert "player_mutes" in data
        assert "channel_mutes" in data
        assert data["is_admin"] is True

    def test_save_player_mutes_with_exception(self):
        """Test saving player mutes when exception occurs."""
        # Mock file operations to raise exception
        with patch("builtins.open", side_effect=Exception("File error")):
            result = self.user_manager.save_player_mutes("player_001")

            assert result is False

    def test_cleanup_player_mutes_success(self):
        """Test successful cleanup of player mutes."""
        # Add test data
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        self.user_manager._admin_players.add("player_001")

        # Create a test file
        mute_file = self.user_manager._get_player_mute_file("player_001")
        mute_file.write_text("test data")

        # Cleanup
        result = self.user_manager.cleanup_player_mutes("player_001")

        assert result is True
        assert "player_001" not in self.user_manager._player_mutes
        assert "player_001" not in self.user_manager._admin_players
        assert not mute_file.exists()

    def test_cleanup_player_mutes_with_exception(self):
        """Test cleanup of player mutes when exception occurs."""
        result = self.user_manager.cleanup_player_mutes("player_001")

        # Should still return True even if player doesn't exist
        assert result is True


class TestUserManagerIntegration:
    """Integration tests for UserManager."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_data_dir = Path(self.temp_dir) / "user_management"
        self.test_data_dir.mkdir(parents=True, exist_ok=True)

        self.user_manager = UserManager(data_dir=self.test_data_dir)

    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil

        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_full_mute_lifecycle(self):
        """Test complete mute lifecycle: mute, check, unmute."""
        # 1. Mute a player
        result = self.user_manager.mute_player(
            muter_id="player_001",
            muter_name="MuterPlayer",
            target_id="player_002",
            target_name="TargetPlayer",
            duration_minutes=30,
            reason="Spam",
        )
        assert result is True

        # 2. Check if muted
        is_muted = self.user_manager.is_player_muted("player_001", "player_002")
        assert is_muted is True

        # 3. Unmute
        result = self.user_manager.unmute_player(
            unmuter_id="player_001", unmuter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )
        assert result is True

        # 4. Check if no longer muted
        is_muted = self.user_manager.is_player_muted("player_001", "player_002")
        assert is_muted is False

    def test_persistence_lifecycle(self):
        """Test save and load persistence lifecycle."""
        # 1. Add mutes
        self.user_manager.mute_player(
            muter_id="player_001", muter_name="MuterPlayer", target_id="player_002", target_name="TargetPlayer"
        )

        self.user_manager.mute_channel(player_id="player_001", player_name="TestPlayer", channel="global")

        self.user_manager._admin_players.add("player_001")

        # 2. Save
        result = self.user_manager.save_player_mutes("player_001")
        assert result is True

        # 3. Create new instance and load
        new_user_manager = UserManager(data_dir=self.test_data_dir)

        result = new_user_manager.load_player_mutes("player_001")
        assert result is True

        # 4. Verify data was loaded correctly
        assert "player_001" in new_user_manager._player_mutes
        assert "player_002" in new_user_manager._player_mutes["player_001"]
        assert "player_001" in new_user_manager._channel_mutes
        assert "global" in new_user_manager._channel_mutes["player_001"]
        assert "player_001" in new_user_manager._admin_players

    def test_expired_mute_cleanup(self):
        """Test that expired mutes are automatically cleaned up."""
        # Add expired mute
        self.user_manager._player_mutes["player_001"] = {
            "player_002": {
                "target_id": "player_002",
                "target_name": "TargetPlayer",
                "muted_by": "player_001",
                "muted_by_name": "MuterPlayer",
                "muted_at": datetime.now(UTC),
                "expires_at": datetime.now(UTC) - timedelta(minutes=1),
                "reason": "Test",
                "is_permanent": False,
            }
        }

        # Check if muted (should trigger cleanup)
        is_muted = self.user_manager.is_player_muted("player_001", "player_002")
        assert is_muted is False

        # Verify cleanup occurred
        assert "player_001" not in self.user_manager._player_mutes
