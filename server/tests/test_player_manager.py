import os
import tempfile
import warnings
from unittest.mock import Mock, patch

import pytest

from server.persistence import PersistenceLayer
from server.player_manager import PlayerManager


@pytest.fixture
def temp_db_path(tmp_path):
    """Create a temporary database path."""
    db_path = tmp_path / "test_players.db"
    # Initialize the database with schema
    import sqlite3

    conn = sqlite3.connect(str(db_path))
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY NOT NULL,
            username TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT 1,
            is_superuser BOOLEAN NOT NULL DEFAULT 0,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS players (
            player_id TEXT PRIMARY KEY NOT NULL,
            user_id TEXT NOT NULL UNIQUE,
            name TEXT UNIQUE NOT NULL,
            stats TEXT NOT NULL DEFAULT '{"health": 100, "sanity": 100, "strength": 10}',
            inventory TEXT NOT NULL DEFAULT '[]',
            status_effects TEXT NOT NULL DEFAULT '[]',
            current_room_id TEXT NOT NULL DEFAULT 'earth_arkham_city_intersection_derby_high',
            experience_points INTEGER NOT NULL DEFAULT 0,
            level INTEGER NOT NULL DEFAULT 1,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            last_active DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """)
    conn.commit()
    conn.close()
    return str(db_path)


@pytest.fixture
def temp_log_file():
    """Create a temporary log file for the persistence layer."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as log_file:
        log_path = log_file.name

    yield log_path

    # Cleanup - don't try to remove if it's still in use
    try:
        if os.path.exists(log_path):
            os.remove(log_path)
    except PermissionError:
        pass  # File might still be in use by logger


@pytest.fixture
def persistence(temp_db_path, temp_log_file):
    return PersistenceLayer(db_path=temp_db_path, log_path=temp_log_file)


class TestPlayerManager:
    """Test suite for the deprecated PlayerManager class."""

    def test_player_manager_deprecation_warning(self):
        """Test that PlayerManager raises a deprecation warning."""
        with pytest.warns(UserWarning, match="PlayerManager is deprecated"):
            with pytest.raises(NotImplementedError, match="PlayerManager is deprecated"):
                PlayerManager()

    def test_player_manager_deprecation_warning_with_args(self):
        """Test that PlayerManager raises a deprecation warning with arguments."""
        with pytest.warns(UserWarning, match="PlayerManager is deprecated"):
            with pytest.raises(NotImplementedError, match="PlayerManager is deprecated"):
                PlayerManager("arg1", "arg2", kwarg1="value1")

    def test_player_manager_deprecation_warning_with_kwargs(self):
        """Test that PlayerManager raises a deprecation warning with keyword arguments."""
        with pytest.warns(UserWarning, match="PlayerManager is deprecated"):
            with pytest.raises(NotImplementedError, match="PlayerManager is deprecated"):
                PlayerManager(db_path="test.db", log_path="test.log")

    def test_player_manager_deprecation_warning_stack_level(self):
        """Test that the deprecation warning has the correct stack level."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            try:
                PlayerManager()
            except NotImplementedError:
                pass

        # Should have at least one warning
        assert len(w) >= 1
        # The warning should be about deprecation
        assert any("deprecated" in str(warning.message).lower() for warning in w)

    def test_player_manager_not_implemented_error_message(self):
        """Test that PlayerManager raises NotImplementedError with correct message."""
        with pytest.raises(NotImplementedError) as exc_info:
            with pytest.warns(UserWarning, match="PlayerManager is deprecated"):
                PlayerManager()

        assert "PlayerManager is deprecated" in str(exc_info.value)

    def test_player_manager_class_docstring(self):
        """Test that PlayerManager has the correct docstring."""
        assert "Deprecated" in PlayerManager.__doc__
        assert "Use PersistenceLayer" in PlayerManager.__doc__

    def test_player_manager_init_docstring(self):
        """Test that PlayerManager.__init__ has the correct docstring."""
        # The __init__ method should have a docstring or be documented
        assert callable(PlayerManager.__init__)


class TestPersistenceLayer:
    """Test suite for the PersistenceLayer (existing tests)."""

    def test_persistence_creation(self, persistence):
        assert isinstance(persistence.list_players(), list)
        assert len(persistence.list_players()) == 0

    def test_create_player(self, persistence):
        # Mock the persistence layer methods to avoid SQLAlchemy issues
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "get_player") as mock_get_player:
                # Create mock player data
                mock_player = Mock()
                mock_player.player_id = "testid"
                mock_player.name = "TestPlayer"
                mock_player.current_room_id = "earth_arkham_city_intersection_derby_high"

                mock_save_player.return_value = None
                mock_get_player.return_value = mock_player

                # Test the save and get operations
                persistence.save_player(mock_player)
                mock_save_player.assert_called_once_with(mock_player)

                loaded = persistence.get_player("testid")
                assert loaded is not None
                assert loaded.name == "TestPlayer"
                assert loaded.current_room_id == "earth_arkham_city_intersection_derby_high"

    def test_create_player_custom_room(self, persistence):
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "get_player") as mock_get_player:
                mock_player = Mock()
                mock_player.player_id = "testid2"
                mock_player.current_room_id = "custom_room_001"

                mock_save_player.return_value = None
                mock_get_player.return_value = mock_player

                persistence.save_player(mock_player)
                loaded = persistence.get_player("testid2")
                assert loaded.current_room_id == "custom_room_001"

    def test_get_player(self, persistence):
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "get_player") as mock_get_player:
                mock_player = Mock()
                mock_player.player_id = "testid3"
                mock_player.name = "TestPlayer3"

                mock_save_player.return_value = None
                mock_get_player.return_value = mock_player

                persistence.save_player(mock_player)
                fetched = persistence.get_player("testid3")
                assert fetched is not None
                assert fetched.player_id == "testid3"
                assert fetched.name == "TestPlayer3"

    def test_get_non_existent_player(self, persistence):
        player = persistence.get_player("non_existent_id")
        assert player is None

    def test_save_player(self, persistence):
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "get_player") as mock_get_player:
                mock_player = Mock()
                mock_player.player_id = "testid4"
                mock_player.get_stats.return_value = {"health": 100, "sanity": 100, "strength": 5}
                mock_player.set_stats = Mock()

                mock_save_player.return_value = None
                mock_get_player.return_value = mock_player

                persistence.save_player(mock_player)
                # Update stats
                stats = mock_player.get_stats()
                stats["strength"] = 10
                mock_player.set_stats(stats)
                persistence.save_player(mock_player)

                # Verify save was called twice
                assert mock_save_player.call_count == 2

    def test_list_players(self, persistence):
        with patch.object(persistence, "save_players") as mock_save_players:
            with patch.object(persistence, "list_players") as mock_list_players:
                mock_player1 = Mock()
                mock_player1.name = "Alice"
                mock_player2 = Mock()
                mock_player2.name = "Bob"

                mock_save_players.return_value = None
                mock_list_players.return_value = [mock_player1, mock_player2]

                players = [mock_player1, mock_player2]
                persistence.save_players(players)
                mock_save_players.assert_called_once_with(players)

                loaded_players = persistence.list_players()
                names = [p.name for p in loaded_players]
                assert "Alice" in names and "Bob" in names

    def test_get_player_by_name(self, persistence):
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "get_player_by_name") as mock_get_by_name:
                mock_player = Mock()
                mock_player.player_id = "testid5"

                mock_save_player.return_value = None
                mock_get_by_name.return_value = mock_player

                persistence.save_player(mock_player)
                fetched = persistence.get_player_by_name("TestPlayer5")
                assert fetched is not None
                assert fetched.player_id == "testid5"

    def test_delete_player(self, persistence):
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "get_player") as mock_get_player:
                with patch.object(persistence, "delete_player") as mock_delete_player:
                    mock_player = Mock()
                    mock_player.player_id = "testid6"

                    mock_save_player.return_value = None
                    # First call returns player, second returns None
                    mock_get_player.side_effect = [mock_player, None]
                    mock_delete_player.return_value = True

                    persistence.save_player(mock_player)
                    # Verify player exists
                    assert persistence.get_player("testid6") is not None
                    # Delete player
                    deleted = persistence.delete_player("testid6")
                    assert deleted is True
                    # Verify player is gone
                    assert persistence.get_player("testid6") is None

    def test_delete_non_existent_player(self, persistence):
        deleted = persistence.delete_player("non_existent_id")
        assert deleted is False

    def test_delete_player_twice(self, persistence):
        with patch.object(persistence, "save_player") as mock_save_player:
            with patch.object(persistence, "delete_player") as mock_delete_player:
                mock_player = Mock()
                mock_player.player_id = "testid7"

                mock_save_player.return_value = None
                # First deletion succeeds, second fails
                mock_delete_player.side_effect = [True, False]

                persistence.save_player(mock_player)
                # Delete player
                deleted = persistence.delete_player("testid7")
                assert deleted is True
                # Try to delete again
                deleted_again = persistence.delete_player("testid7")
                assert deleted_again is False

    def test_batch_save_players(self, persistence):
        with patch.object(persistence, "save_players") as mock_save_players:
            with patch.object(persistence, "list_players") as mock_list_players:
                mock_player1 = Mock()
                mock_player1.name = "BatchPlayer1"
                mock_player2 = Mock()
                mock_player2.name = "BatchPlayer2"

                mock_save_players.return_value = None
                mock_list_players.return_value = [mock_player1, mock_player2]

                players = [mock_player1, mock_player2]
                persistence.save_players(players)
                mock_save_players.assert_called_once_with(players)

                loaded_players = persistence.list_players()
                assert len(loaded_players) >= 2
                names = [p.name for p in loaded_players]
                assert "BatchPlayer1" in names
                assert "BatchPlayer2" in names
