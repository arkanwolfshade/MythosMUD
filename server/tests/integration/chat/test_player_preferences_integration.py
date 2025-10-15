"""
Integration tests for player channel preferences functionality.

This module tests the integration between the PlayerPreferencesService
and the database, including persistence and real-world usage scenarios.
"""

import json
import sqlite3
import tempfile
from pathlib import Path

import pytest

from server.services.player_preferences_service import PlayerPreferencesService


class TestPlayerPreferencesIntegration:
    """Integration tests for player preferences system."""

    @pytest.fixture
    def temp_db_path(self):
        """Create a temporary database for integration testing."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            db_path = f.name

        # Create basic schema with players table
        with sqlite3.connect(db_path) as conn:
            # Enable foreign keys
            conn.execute("PRAGMA foreign_keys = ON")

            conn.execute("""
                CREATE TABLE players (
                    player_id TEXT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    level INTEGER NOT NULL DEFAULT 1
                )
            """)
            conn.commit()

        yield db_path

        # Cleanup - close all connections first
        try:
            import gc

            gc.collect()  # Force garbage collection to close connections
            Path(db_path).unlink(missing_ok=True)
        except PermissionError:
            # On Windows, sometimes the file is still in use
            # This is acceptable for tests
            pass

    @pytest.fixture
    def preferences_service(self, temp_db_path):
        """Create a PlayerPreferencesService instance with test database."""
        return PlayerPreferencesService(temp_db_path)

    def test_full_player_lifecycle(self, preferences_service, temp_db_path):
        """Test complete player lifecycle with preferences."""
        player_id = "integration-test-player"

        # 1. Create player in players table
        with sqlite3.connect(temp_db_path) as conn:
            conn.execute("INSERT INTO players (player_id, name, level) VALUES (?, ?, ?)", (player_id, "TestPlayer", 1))
            conn.commit()

        # 2. Create preferences
        result = preferences_service.create_player_preferences(player_id)
        assert result["success"] is True

        # 3. Verify default preferences
        prefs = preferences_service.get_player_preferences(player_id)
        assert prefs["success"] is True
        assert prefs["data"]["default_channel"] == "local"
        assert prefs["data"]["muted_channels"] == "[]"

        # 4. Update default channel
        result = preferences_service.update_default_channel(player_id, "global")
        assert result["success"] is True

        # 5. Mute some channels
        preferences_service.mute_channel(player_id, "whisper")
        preferences_service.mute_channel(player_id, "local")

        # 6. Verify final state
        prefs = preferences_service.get_player_preferences(player_id)
        assert prefs["success"] is True
        assert prefs["data"]["default_channel"] == "global"

        muted_channels = json.loads(prefs["data"]["muted_channels"])
        assert "whisper" in muted_channels
        assert "local" in muted_channels
        assert "global" not in muted_channels  # Should not be muted

        # 7. Verify foreign key constraint works
        with sqlite3.connect(temp_db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute("DELETE FROM players WHERE player_id = ?", (player_id,))
            conn.commit()

        # Preferences should be automatically deleted due to CASCADE
        prefs = preferences_service.get_player_preferences(player_id)
        assert prefs["success"] is False

    def test_multiple_players_preferences(self, preferences_service):
        """Test managing preferences for multiple players."""
        players = ["player1", "player2", "player3"]

        # Create preferences for all players
        for player_id in players:
            result = preferences_service.create_player_preferences(player_id)
            assert result["success"] is True

        # Set different default channels
        preferences_service.update_default_channel("player1", "local")
        preferences_service.update_default_channel("player2", "global")
        preferences_service.update_default_channel("player3", "whisper")

        # Mute different channels for each player
        preferences_service.mute_channel("player1", "global")
        preferences_service.mute_channel("player2", "whisper")
        preferences_service.mute_channel("player3", "local")

        # Verify each player has correct preferences
        prefs1 = preferences_service.get_player_preferences("player1")
        prefs2 = preferences_service.get_player_preferences("player2")
        prefs3 = preferences_service.get_player_preferences("player3")

        assert prefs1["data"]["default_channel"] == "local"
        assert prefs2["data"]["default_channel"] == "global"
        assert prefs3["data"]["default_channel"] == "whisper"

        muted1 = json.loads(prefs1["data"]["muted_channels"])
        muted2 = json.loads(prefs2["data"]["muted_channels"])
        muted3 = json.loads(prefs3["data"]["muted_channels"])

        assert "global" in muted1
        assert "whisper" in muted2
        assert "local" in muted3

    def test_preferences_persistence_across_restarts(self, temp_db_path):
        """Test that preferences persist when service is restarted."""
        player_id = "persistence-test-player"

        # Create preferences with first service instance
        service1 = PlayerPreferencesService(temp_db_path)
        service1.create_player_preferences(player_id)
        service1.update_default_channel(player_id, "global")
        service1.mute_channel(player_id, "whisper")

        # Simulate service restart by creating new instance
        service2 = PlayerPreferencesService(temp_db_path)

        # Verify preferences persist
        prefs = service2.get_player_preferences(player_id)
        assert prefs["success"] is True
        assert prefs["data"]["default_channel"] == "global"

        muted_channels = json.loads(prefs["data"]["muted_channels"])
        assert "whisper" in muted_channels

    def test_concurrent_preferences_access(self, temp_db_path):
        """Test concurrent access to preferences from multiple service instances."""
        player_id = "concurrent-test-player"

        # Create multiple service instances
        services = [PlayerPreferencesService(temp_db_path) for _ in range(3)]

        # Create preferences with first service
        services[0].create_player_preferences(player_id)

        # All services should see the preferences
        for i, service in enumerate(services):
            prefs = service.get_player_preferences(player_id)
            assert prefs["success"] is True, f"Service {i} failed to see preferences"

        # Update preferences from different service
        services[1].update_default_channel(player_id, "global")

        # All services should see the update
        for i, service in enumerate(services):
            prefs = service.get_player_preferences(player_id)
            assert prefs["data"]["default_channel"] == "global", f"Service {i} failed to see update"

    def test_database_constraints_and_indexes(self, temp_db_path):
        """Test that database constraints and indexes work correctly."""
        service = PlayerPreferencesService(temp_db_path)

        with sqlite3.connect(temp_db_path) as conn:
            # Enable foreign keys
            conn.execute("PRAGMA foreign_keys = ON")

            # Test primary key constraint
            service.create_player_preferences("player1")

            # Try to create duplicate - should fail
            with pytest.raises(sqlite3.IntegrityError):
                conn.execute(
                    """
                    INSERT INTO player_channel_preferences
                    (player_id, default_channel, muted_channels)
                    VALUES (?, ?, ?)
                """,
                    ("player1", "local", "[]"),
                )
                conn.commit()

            # Test foreign key constraint
            with pytest.raises(sqlite3.IntegrityError):
                conn.execute(
                    """
                    INSERT INTO player_channel_preferences
                    (player_id, default_channel, muted_channels)
                    VALUES (?, ?, ?)
                """,
                    ("non-existent-player", "local", "[]"),
                )
                conn.commit()

            # Verify indexes exist
            cursor = conn.execute("PRAGMA index_list(player_channel_preferences)")
            indexes = [row[1] for row in cursor.fetchall()]

            assert "idx_player_channel_preferences_player_id" in indexes
            assert "idx_player_channel_preferences_default_channel" in indexes

    def test_error_handling_and_recovery(self, preferences_service):
        """Test error handling and recovery scenarios."""
        player_id = "error-test-player"

        # Test with invalid player ID
        result = preferences_service.create_player_preferences("")
        assert result["success"] is False
        assert "Invalid player ID" in result["error"]

        # Test with invalid channel
        preferences_service.create_player_preferences(player_id)
        result = preferences_service.update_default_channel(player_id, "invalid_channel")
        assert result["success"] is False
        assert "Invalid channel name" in result["error"]

        # Test with non-existent player
        result = preferences_service.get_player_preferences("non-existent")
        assert result["success"] is False
        assert "not found" in result["error"]

        # Test system channel muting
        result = preferences_service.mute_channel(player_id, "system")
        assert result["success"] is False
        assert "System channel cannot be muted" in result["error"]

    def test_json_handling_edge_cases(self, preferences_service):
        """Test edge cases in JSON handling for muted channels."""
        player_id = "json-test-player"

        # Create preferences
        preferences_service.create_player_preferences(player_id)

        # Test with empty muted channels
        prefs = preferences_service.get_player_preferences(player_id)
        muted_channels = json.loads(prefs["data"]["muted_channels"])
        assert muted_channels == []

        # Test adding and removing channels multiple times
        preferences_service.mute_channel(player_id, "global")
        preferences_service.mute_channel(player_id, "whisper")
        preferences_service.unmute_channel(player_id, "global")
        preferences_service.mute_channel(player_id, "local")

        # Verify final state
        prefs = preferences_service.get_player_preferences(player_id)
        muted_channels = json.loads(prefs["data"]["muted_channels"])
        assert "whisper" in muted_channels
        assert "local" in muted_channels
        assert "global" not in muted_channels

        # Test removing non-muted channel (should not error)
        result = preferences_service.unmute_channel(player_id, "global")
        assert result["success"] is True

    def test_timestamp_handling(self, preferences_service):
        """Test that timestamps are handled correctly."""
        player_id = "timestamp-test-player"

        # Create preferences
        preferences_service.create_player_preferences(player_id)

        # Get initial timestamps
        prefs1 = preferences_service.get_player_preferences(player_id)
        created_at1 = prefs1["data"]["created_at"]
        updated_at1 = prefs1["data"]["updated_at"]

        # Update preferences
        preferences_service.update_default_channel(player_id, "global")

        # Get updated timestamps
        prefs2 = preferences_service.get_player_preferences(player_id)
        created_at2 = prefs2["data"]["created_at"]
        updated_at2 = prefs2["data"]["updated_at"]

        # Created timestamp should not change
        assert created_at1 == created_at2

        # Updated timestamp should be different (or at least not older)
        assert updated_at2 >= updated_at1

    def test_service_cleanup_and_cleanup(self, temp_db_path):
        """Test service cleanup and database cleanup."""
        player_id = "cleanup-test-player"

        # Create service and preferences
        service = PlayerPreferencesService(temp_db_path)
        service.create_player_preferences(player_id)
        service.update_default_channel(player_id, "global")

        # Delete preferences
        result = service.delete_player_preferences(player_id)
        assert result["success"] is True

        # Verify preferences are gone
        prefs = service.get_player_preferences(player_id)
        assert prefs["success"] is False

        # Try to delete again - should fail
        result = service.delete_player_preferences(player_id)
        assert result["success"] is False
        assert "not found" in result["error"]
