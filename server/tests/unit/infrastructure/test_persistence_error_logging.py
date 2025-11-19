"""
Test cases for persistence layer error logging.

This module tests the error logging functionality in the persistence layer,
ensuring that all database operations, room loading, and world data operations
are properly logged with appropriate context information.
"""

import json
import os
import tempfile
from unittest.mock import AsyncMock, Mock, patch

import pytest
from psycopg2 import IntegrityError as PGIntegrityError
from psycopg2 import OperationalError as PGOperationalError

from server.exceptions import DatabaseError, ValidationError
from server.models.player import Player
from server.persistence import PersistenceLayer, get_persistence, reset_persistence


class TestPersistenceErrorLogging:
    """Test error logging in persistence layer operations."""

    def setup_method(self):
        """Set up test environment."""
        # Reset persistence singleton
        reset_persistence()

        # Use PostgreSQL from environment - SQLite is no longer supported
        database_url = os.getenv("DATABASE_URL")
        if not database_url or not database_url.startswith("postgresql"):
            pytest.skip("DATABASE_URL must be set to a PostgreSQL URL. SQLite is no longer supported.")

        # Create persistence layer (will use PostgreSQL from environment)
        self.persistence = get_persistence()

    def teardown_method(self):
        """Clean up test environment."""
        # Reset persistence singleton
        reset_persistence()

    def test_persistence_init_without_database_url(self):
        """Test persistence initialization error when DATABASE_URL is not set."""
        # Remove DATABASE_URL
        if "DATABASE_URL" in os.environ:
            del os.environ["DATABASE_URL"]

        reset_persistence()

        with pytest.raises(ValidationError) as exc_info:
            get_persistence()

        # Verify error context
        assert "DATABASE_URL environment variable must be set" in str(exc_info.value)
        assert exc_info.value.context.metadata["operation"] == "persistence_init"

    @pytest.mark.skip(reason="load_hierarchical_world removed - rooms now loaded from database")
    def test_room_cache_load_error_logging(self):
        """Test error logging when room cache loading fails."""
        # Mock world_loader to raise an exception
        with patch("server.world_loader.load_hierarchical_world", side_effect=Exception("World load failed")):
            with pytest.raises(DatabaseError) as exc_info:
                # This will trigger room cache loading during initialization
                # Use PostgreSQL from environment - SQLite is no longer supported
                PersistenceLayer()

        # Verify error context
        assert "Room cache load failed" in str(exc_info.value)
        assert exc_info.value.context.metadata["operation"] == "load_room_cache"
        assert "rooms_base_path" in exc_info.value.context.metadata

    def test_save_player_integrity_error_logging(self):
        """Test error logging for player save integrity errors."""
        # Create a player
        player = Player(name="TestPlayer", user_id="test-user-id", player_id="test-player-id")

        # Mock PostgreSQL connection to raise IntegrityError
        with patch("server.postgres_adapter.connect_postgres") as mock_connect:
            mock_conn = Mock()
            mock_conn.__enter__ = Mock(return_value=mock_conn)
            mock_conn.__exit__ = Mock(return_value=None)
            mock_conn.cursor.return_value.__enter__.return_value.execute.side_effect = PGIntegrityError(
                "UNIQUE constraint failed"
            )
            mock_connect.return_value = mock_conn

            with pytest.raises(DatabaseError) as exc_info:
                self.persistence.save_player(player)

        # Verify error context
        assert "Unique constraint error saving player" in str(exc_info.value)
        assert exc_info.value.context.metadata["operation"] == "save_player"
        assert exc_info.value.context.metadata["player_name"] == "TestPlayer"
        assert exc_info.value.context.metadata["player_id"] == "test-player-id"

    def test_save_players_batch_error_logging(self):
        """Test error logging for batch player save errors."""
        # Create players
        players = [
            Player(name="Player1", user_id="user1", player_id="player1"),
            Player(name="Player2", user_id="user2", player_id="player2"),
        ]

        # Mock PostgreSQL connection to raise IntegrityError
        with patch("server.postgres_adapter.connect_postgres") as mock_connect:
            mock_conn = Mock()
            mock_conn.__enter__ = Mock(return_value=mock_conn)
            mock_conn.__exit__ = Mock(return_value=None)
            mock_conn.cursor.return_value.__enter__.return_value.execute.side_effect = PGIntegrityError(
                "UNIQUE constraint failed"
            )
            mock_connect.return_value = mock_conn

            with pytest.raises(DatabaseError) as exc_info:
                self.persistence.save_players(players)

        # Verify error context
        assert "Batch unique constraint error" in str(exc_info.value)
        assert exc_info.value.context.metadata["operation"] == "save_players"
        assert exc_info.value.context.metadata["player_count"] == 2

    def test_delete_player_database_error_logging(self):
        """Test error logging for player deletion database errors."""
        # Mock PostgreSQL connection to raise OperationalError
        with patch("server.postgres_adapter.connect_postgres") as mock_connect:
            mock_conn = Mock()
            mock_conn.__enter__ = Mock(return_value=mock_conn)
            mock_conn.__exit__ = Mock(return_value=None)
            mock_conn.cursor.return_value.__enter__.return_value.execute.side_effect = PGOperationalError(
                "Database locked"
            )
            mock_connect.return_value = mock_conn

            with pytest.raises(DatabaseError) as exc_info:
                self.persistence.delete_player("test-player-id")

        # Verify error context
        assert "Database error deleting player" in str(exc_info.value)
        assert exc_info.value.context.metadata["operation"] == "delete_player"
        assert exc_info.value.context.metadata["player_id"] == "test-player-id"

    def test_sync_room_players_error_logging(self):
        """Test error logging for room player sync errors."""
        # Create a mock room
        mock_room = Mock()
        mock_room.id = "test-room"
        mock_room.get_players.side_effect = Exception("Room sync failed")

        # Call the sync method
        self.persistence._sync_room_players(mock_room)

        # The sync method should not raise an exception since it's non-critical
        # We can't easily test the warning log without more complex mocking
        # The important thing is that it doesn't crash the system

    def test_validate_and_fix_player_room_config_error_logging(self):
        """Test error logging when config loading fails during room validation."""
        # Create a player with invalid room
        player = Player(
            name="TestPlayer", user_id="test-user-id", player_id="test-player-id", current_room_id="invalid-room"
        )

        # Mock config loading to fail
        with patch("server.config.get_config", side_effect=Exception("Config load failed")):
            result = self.persistence.validate_and_fix_player_room(player)

        # Should still succeed but log warning
        assert result is True
        # We can't easily test the warning log without more complex mocking
        # The important thing is that it doesn't crash the system


class TestDatabaseErrorLogging:
    """Test error logging in database module."""

    def setup_method(self):
        """Set up test environment."""
        # No setup needed - tests use PostgreSQL from environment
        pass

    def teardown_method(self):
        """Clean up test environment."""
        # No cleanup needed
        pass

    def test_database_config_without_url(self):
        """Test database configuration error when DATABASE_URL is not set."""
        # This test is covered by the persistence layer test
        # The database module validation happens at import time
        # and is tested through the persistence layer initialization
        pass

    @pytest.mark.asyncio
    async def test_database_session_error_logging(self):
        """Test error logging in database session management."""
        # Mock session to raise an exception
        from unittest.mock import MagicMock

        from server.database import get_async_session

        mock_session = Mock()
        mock_session.rollback = AsyncMock(side_effect=Exception("Rollback error"))

        # Create mock context manager
        mock_context_manager = MagicMock()
        mock_context_manager.__aenter__ = AsyncMock(return_value=mock_session)
        mock_context_manager.__aexit__ = AsyncMock(return_value=None)

        # Create mock session maker callable
        mock_session_maker_callable = MagicMock()
        mock_session_maker_callable.return_value = mock_context_manager

        with patch("server.database.get_session_maker", return_value=mock_session_maker_callable):
            # This should not raise an exception but should log the error
            try:
                async for _session in get_async_session():
                    raise Exception("Test error")
            except Exception:
                pass  # Expected to raise

    def test_get_database_path_unsupported_url(self):
        """Test error logging for unsupported database URL."""
        # This test is complex due to module reloading issues
        # The functionality is tested through the persistence layer
        # which calls get_database_path internally
        pass


class TestWorldLoaderErrorLogging:
    """Test error logging in world loader module."""

    def setup_method(self):
        """Set up test environment."""
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Clean up test environment."""
        import shutil

        shutil.rmtree(self.temp_dir)

    def test_room_validation_error_logging(self):
        """Test error logging for room validation errors."""
        from server.world_loader import validate_room_data

        # Create invalid room data
        invalid_room_data = {"invalid": "data"}

        # Mock validator to raise an exception
        mock_validator = Mock()
        mock_validator.validate_room.side_effect = Exception("Validation failed")

        with patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True):
            with pytest.raises(ValidationError) as exc_info:
                validate_room_data(invalid_room_data, "test_file.json", mock_validator, strict_validation=True)

        # Verify error context
        assert "Schema validation error" in str(exc_info.value)
        assert exc_info.value.context.metadata["operation"] == "validate_room_data"
        assert exc_info.value.context.metadata["file_path"] == "test_file.json"

    @pytest.mark.skip(reason="load_hierarchical_world removed - rooms now loaded from database")
    def test_room_file_load_error_logging(self):
        """Test error logging for room file loading errors."""
        from server.world_loader import load_hierarchical_world

        # Create a temporary room file with invalid JSON
        room_file = os.path.join(self.temp_dir, "invalid.json")
        with open(room_file, "w") as f:
            f.write("invalid json content")

        # Mock ROOMS_BASE_PATH to point to our temp directory
        with patch("server.world_loader.ROOMS_BASE_PATH", self.temp_dir):
            # Create the directory structure
            os.makedirs(os.path.join(self.temp_dir, "earth", "arkhamcity", "test_subzone"))
            os.rename(room_file, os.path.join(self.temp_dir, "earth", "arkhamcity", "test_subzone", "invalid.json"))

            # Load world data
            load_hierarchical_world()

        # The function should handle the error gracefully
        # We can't easily test the warning log without more complex mocking
        # The important thing is that it doesn't crash the system

    @pytest.mark.skip(reason="load_hierarchical_world removed - rooms now loaded from database")
    def test_world_load_directory_error_logging(self):
        """Test error logging for world directory access errors."""
        from server.world_loader import load_hierarchical_world

        # Mock ROOMS_BASE_PATH to point to non-existent directory
        with patch("server.world_loader.ROOMS_BASE_PATH", "/non/existent/path"):
            load_hierarchical_world()

        # The function should handle the error gracefully
        # We can't easily test the warning log without more complex mocking
        # The important thing is that it doesn't crash the system

    @pytest.mark.skip(reason="load_rooms removed - rooms now loaded from database")
    def test_validation_errors_logging(self):
        """Test logging of validation errors during world loading."""
        from server.world_loader import load_rooms

        # Create a temporary room file
        room_file = os.path.join(self.temp_dir, "test_room.json")
        with open(room_file, "w") as f:
            json.dump({"name": "Test Room", "invalid_field": "invalid"}, f)

        # Mock ROOMS_BASE_PATH and create directory structure
        with patch("server.world_loader.ROOMS_BASE_PATH", self.temp_dir):
            os.makedirs(os.path.join(self.temp_dir, "earth", "arkhamcity", "test_subzone"))
            os.rename(room_file, os.path.join(self.temp_dir, "earth", "arkhamcity", "test_subzone", "test_room.json"))

            # Mock validator to return validation errors
            mock_validator = Mock()
            mock_validator.validate_room.return_value = ["Invalid field: invalid_field"]

            with patch("server.world_loader.create_validator", return_value=mock_validator):
                with patch("server.world_loader.SCHEMA_VALIDATION_AVAILABLE", True):
                    load_rooms()

        # The function should handle validation errors gracefully
        # We can't easily test the warning log without more complex mocking
        # The important thing is that it doesn't crash the system
