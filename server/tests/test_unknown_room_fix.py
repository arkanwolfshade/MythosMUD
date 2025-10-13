"""
Test for unknown room handling and automatic relocation to default starting room.

This test verifies that players who find themselves in non-existent rooms
are automatically moved to the configured default starting room, as described
in the dimensional mapping protocols of the Pnakotic Manuscripts.
"""

from unittest.mock import Mock, patch

from server.models import Player
from server.persistence import PersistenceLayer


class TestUnknownRoomFix:
    """Test suite for unknown room validation and fixing."""

    def test_validate_and_fix_player_room_valid_room(self):
        """Test that players in valid rooms are not moved."""
        # Arrange
        persistence = PersistenceLayer(":memory:", "test.log")
        persistence.get_room = Mock(return_value=Mock())  # Room exists

        player = Player(name="TestPlayer", current_room_id="valid_room_123")

        # Act
        result = persistence.validate_and_fix_player_room(player)

        # Assert
        assert result is True
        assert player.current_room_id == "valid_room_123"  # Room unchanged
        persistence.get_room.assert_called_once_with("valid_room_123")

    def test_validate_and_fix_player_room_invalid_room(self):
        """Test that players in invalid rooms are moved to default room."""
        # Arrange
        persistence = PersistenceLayer(":memory:", "test.log")
        persistence.get_room = Mock(return_value=None)  # Room doesn't exist

        # Mock config to return expected default room
        with patch("server.config.get_config") as mock_get_config:
            mock_config = Mock()
            mock_config.game.default_player_room = "earth_arkhamcity_sanitarium_room_foyer_001"
            mock_get_config.return_value = mock_config

            player = Player(name="TestPlayer", current_room_id="invalid_room_456")

            # Act
            result = persistence.validate_and_fix_player_room(player)

            # Assert
            expected_room = "earth_arkhamcity_sanitarium_room_foyer_001"
            assert result is True
            assert player.current_room_id == expected_room

    def test_validate_and_fix_player_room_fallback_default(self):
        """Test that fallback default room is used if config is missing."""
        # Arrange
        persistence = PersistenceLayer(":memory:", "test.log")
        persistence.get_room = Mock(return_value=None)  # Room doesn't exist

        # Mock config to fail, forcing fallback to hardcoded default
        with patch("server.config.get_config", side_effect=Exception("Config error")):
            player = Player(name="TestPlayer", current_room_id="invalid_room_789")

            # Act
            result = persistence.validate_and_fix_player_room(player)

            # Assert - should use hardcoded fallback
            expected_room = "earth_arkhamcity_sanitarium_room_foyer_001"
            assert result is True
            assert player.current_room_id == expected_room

    def test_validate_and_fix_player_room_config_error(self):
        """Test that fallback default room is used if config loading fails."""
        # Arrange
        persistence = PersistenceLayer(":memory:", "test.log")
        persistence.get_room = Mock(return_value=None)  # Room doesn't exist

        # Mock config to raise an exception
        with patch("server.config.get_config") as mock_get_config:
            mock_get_config.side_effect = Exception("Config error")

            player = Player(name="TestPlayer", current_room_id="invalid_room_999")

            # Act
            result = persistence.validate_and_fix_player_room(player)

            # Assert
            expected_room = "earth_arkhamcity_sanitarium_room_foyer_001"
            assert result is True
            assert player.current_room_id == expected_room
