"""
Tests for player channel preferences functionality.

This module tests the player channel preferences table and service
for the Advanced Chat Channels feature.
"""

import json
import sqlite3

import pytest

from server.services.player_preferences_service import PlayerPreferencesService


class TestPlayerChannelPreferencesTable:
    """Test the player_channel_preferences table schema and operations."""

    @pytest.fixture
    def temp_db_path(self, tmp_path):
        """Create a temporary database for testing."""
        db_path = tmp_path / "unit_test_players.db"
        return str(db_path)

    @pytest.fixture
    def preferences_service(self, temp_db_path):
        """Create a PlayerPreferencesService instance with test database."""
        return PlayerPreferencesService(temp_db_path)

    def test_create_preferences_table(self, temp_db_path):
        """Test that the preferences table can be created."""
        PlayerPreferencesService(temp_db_path)

        # Table should be created during service initialization
        with sqlite3.connect(temp_db_path) as conn:
            cursor = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='player_channel_preferences'"
            )
            table_exists = cursor.fetchone() is not None
            assert table_exists, "player_channel_preferences table should be created"

    def test_preferences_table_schema(self, temp_db_path):
        """Test that the preferences table has the correct schema."""
        PlayerPreferencesService(temp_db_path)

        with sqlite3.connect(temp_db_path) as conn:
            cursor = conn.execute("PRAGMA table_info(player_channel_preferences)")
            columns = {row[1]: row[2] for row in cursor.fetchall()}

            # Check required columns exist
            assert "player_id" in columns
            assert "default_channel" in columns
            assert "muted_channels" in columns
            assert "created_at" in columns
            assert "updated_at" in columns

            # Check data types
            assert columns["player_id"] == "TEXT"
            assert columns["default_channel"] == "TEXT"
            assert columns["muted_channels"] == "TEXT"
            assert columns["created_at"] == "TIMESTAMP"
            assert columns["updated_at"] == "TIMESTAMP"

    def test_preferences_table_constraints(self, temp_db_path):
        """Test that the preferences table has correct constraints."""
        PlayerPreferencesService(temp_db_path)

        with sqlite3.connect(temp_db_path) as conn:
            # Test primary key constraint
            cursor = conn.execute("PRAGMA table_info(player_channel_preferences)")
            columns = cursor.fetchall()

            player_id_col = next(col for col in columns if col[1] == "player_id")
            assert player_id_col[5] == 1, "player_id should be primary key"

            # Test default value for default_channel
            default_channel_col = next(col for col in columns if col[1] == "default_channel")
            assert default_channel_col[4] == "'local'", "default_channel should default to 'local'"


class TestPlayerPreferencesService:
    """Test the PlayerPreferencesService functionality."""

    @pytest.fixture
    def temp_db_path(self, tmp_path):
        """Create a temporary database for testing."""
        db_path = tmp_path / "unit_test_players.db"
        return str(db_path)

    @pytest.fixture
    def preferences_service(self, temp_db_path):
        """Create a PlayerPreferencesService instance with test database."""
        return PlayerPreferencesService(temp_db_path)

    def test_create_player_preferences(self, preferences_service):
        """Test creating preferences for a new player."""
        player_id = "test-player-123"

        # Create preferences
        result = preferences_service.create_player_preferences(player_id)
        assert result["success"] is True

        # Verify preferences were created with defaults
        preferences = preferences_service.get_player_preferences(player_id)
        assert preferences["success"] is True
        assert preferences["data"]["player_id"] == player_id
        assert preferences["data"]["default_channel"] == "local"
        assert preferences["data"]["muted_channels"] == "[]"

    def test_get_player_preferences_not_found(self, preferences_service):
        """Test getting preferences for non-existent player."""
        player_id = "non-existent-player"

        result = preferences_service.get_player_preferences(player_id)
        assert result["success"] is False
        assert "not found" in result["error"].lower()

    def test_update_default_channel(self, preferences_service):
        """Test updating a player's default channel."""
        player_id = "test-player-456"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Update default channel
        result = preferences_service.update_default_channel(player_id, "global")
        assert result["success"] is True

        # Verify update
        preferences = preferences_service.get_player_preferences(player_id)
        assert preferences["data"]["default_channel"] == "global"

    def test_update_default_channel_invalid(self, preferences_service):
        """Test updating default channel with invalid value."""
        player_id = "test-player-789"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Try to update with invalid channel
        result = preferences_service.update_default_channel(player_id, "invalid_channel")
        assert result["success"] is False
        assert "invalid" in result["error"].lower()

    def test_mute_channel(self, preferences_service):
        """Test muting a channel for a player."""
        player_id = "test-player-mute"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Mute global channel
        result = preferences_service.mute_channel(player_id, "global")
        assert result["success"] is True

        # Verify channel is muted
        preferences = preferences_service.get_player_preferences(player_id)
        muted_channels = json.loads(preferences["data"]["muted_channels"])
        assert "global" in muted_channels

    def test_unmute_channel(self, preferences_service):
        """Test unmuting a channel for a player."""
        player_id = "test-player-unmute"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Mute global channel first
        preferences_service.mute_channel(player_id, "global")

        # Unmute global channel
        result = preferences_service.unmute_channel(player_id, "global")
        assert result["success"] is True

        # Verify channel is unmuted
        preferences = preferences_service.get_player_preferences(player_id)
        muted_channels = json.loads(preferences["data"]["muted_channels"])
        assert "global" not in muted_channels

    def test_mute_system_channel(self, preferences_service):
        """Test that system channel cannot be muted."""
        player_id = "test-player-system"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Try to mute system channel
        result = preferences_service.mute_channel(player_id, "system")
        assert result["success"] is False
        assert "system channel cannot be muted" in result["error"].lower()

    def test_get_muted_channels(self, preferences_service):
        """Test getting list of muted channels for a player."""
        player_id = "test-player-muted-list"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Mute multiple channels
        preferences_service.mute_channel(player_id, "global")
        preferences_service.mute_channel(player_id, "whisper")

        # Get muted channels
        result = preferences_service.get_muted_channels(player_id)
        assert result["success"] is True
        muted_channels = result["data"]
        assert "global" in muted_channels
        assert "whisper" in muted_channels
        assert "local" not in muted_channels

    def test_is_channel_muted(self, preferences_service):
        """Test checking if a specific channel is muted."""
        player_id = "test-player-check-mute"

        # Create initial preferences
        preferences_service.create_player_preferences(player_id)

        # Initially not muted
        result = preferences_service.is_channel_muted(player_id, "global")
        assert result["success"] is True
        assert result["data"] is False

        # Mute the channel
        preferences_service.mute_channel(player_id, "global")

        # Now should be muted
        result = preferences_service.is_channel_muted(player_id, "global")
        assert result["success"] is True
        assert result["data"] is True

    def test_delete_player_preferences(self, preferences_service):
        """Test deleting player preferences."""
        player_id = "test-player-delete"

        # Create preferences
        preferences_service.create_player_preferences(player_id)

        # Verify they exist
        preferences = preferences_service.get_player_preferences(player_id)
        assert preferences["success"] is True

        # Delete preferences
        result = preferences_service.delete_player_preferences(player_id)
        assert result["success"] is True

        # Verify they're gone
        preferences = preferences_service.get_player_preferences(player_id)
        assert preferences["success"] is False

    def test_preferences_persistence(self, temp_db_path):
        """Test that preferences persist across service instances."""
        player_id = "test-player-persistence"

        # Create preferences with first service instance
        service1 = PlayerPreferencesService(temp_db_path)
        service1.create_player_preferences(player_id)
        service1.update_default_channel(player_id, "global")

        # Create new service instance
        service2 = PlayerPreferencesService(temp_db_path)

        # Verify preferences persist
        preferences = service2.get_player_preferences(player_id)
        assert preferences["success"] is True
        assert preferences["data"]["default_channel"] == "global"

    def test_concurrent_access(self, temp_db_path):
        """Test concurrent access to preferences."""
        player_id = "test-player-concurrent"

        # Create two service instances
        service1 = PlayerPreferencesService(temp_db_path)
        service2 = PlayerPreferencesService(temp_db_path)

        # Create preferences with first service
        service1.create_player_preferences(player_id)

        # Both services should see the preferences
        prefs1 = service1.get_player_preferences(player_id)
        prefs2 = service2.get_player_preferences(player_id)

        assert prefs1["success"] is True
        assert prefs2["success"] is True
        assert prefs1["data"]["player_id"] == prefs2["data"]["player_id"]


class TestPlayerPreferencesValidation:
    """Test validation of player preferences data."""

    @pytest.fixture
    def temp_db_path(self, tmp_path):
        """Create a temporary database for testing."""
        db_path = tmp_path / "unit_test_players.db"
        return str(db_path)

    @pytest.fixture
    def preferences_service(self, temp_db_path):
        """Create a PlayerPreferencesService instance with test database."""
        return PlayerPreferencesService(temp_db_path)

    def test_valid_channel_names(self, preferences_service):
        """Test that valid channel names are accepted."""
        valid_channels = ["local", "global", "whisper", "system"]

        for channel in valid_channels:
            # This should not raise an exception
            assert preferences_service._is_valid_channel(channel) is True

    def test_invalid_channel_names(self, preferences_service):
        """Test that invalid channel names are rejected."""
        invalid_channels = ["invalid", "test", "random", "chat", ""]

        for channel in invalid_channels:
            assert preferences_service._is_valid_channel(channel) is False

    def test_player_id_validation(self, preferences_service):
        """Test player ID validation."""
        # Valid player IDs
        valid_ids = ["player-123", "test_player", "user_456", "admin"]

        for player_id in valid_ids:
            assert preferences_service._is_valid_player_id(player_id) is True

        # Invalid player IDs
        invalid_ids = ["", None, "a" * 256]  # Too long

        for player_id in invalid_ids:
            assert preferences_service._is_valid_player_id(player_id) is False

    def test_json_validation(self, preferences_service):
        """Test JSON validation for muted_channels field."""
        # Valid JSON arrays
        valid_jsons = ["[]", '["local"]', '["global", "whisper"]']

        for json_str in valid_jsons:
            assert preferences_service._is_valid_json_array(json_str) is True

        # Invalid JSON
        invalid_jsons = ["", "invalid", '{"key": "value"}']

        for json_str in invalid_jsons:
            assert preferences_service._is_valid_json_array(json_str) is False
