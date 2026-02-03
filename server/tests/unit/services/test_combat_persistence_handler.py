"""
Unit tests for combat persistence handler - core functionality.

Tests initialization, persistence layer access, and DP/posture updates.
"""

import uuid
from unittest.mock import MagicMock, patch

import pytest

from server.services.combat_persistence_handler import CombatPersistenceHandler

# pylint: disable=protected-access  # Reason: Test file - accessing protected members is standard practice for unit testing
# pylint: disable=redefined-outer-name  # Reason: Test file - pytest fixture parameter names must match fixture names, causing intentional redefinitions


@pytest.fixture
def mock_combat_service():
    """Create mock combat service."""
    return MagicMock()


@pytest.fixture
def persistence_handler(mock_combat_service):
    """Create CombatPersistenceHandler instance."""
    return CombatPersistenceHandler(mock_combat_service)


@pytest.fixture
def mock_player():
    """Create mock player."""
    player = MagicMock()
    player.player_id = uuid.uuid4()
    player.name = "TestPlayer"
    player.stats = {"current_dp": 50, "max_dp": 100, "position": "standing"}
    player.get_stats = MagicMock(return_value={"current_dp": 50, "max_dp": 100, "position": "standing"})
    player.set_stats = MagicMock()
    player.apply_dp_change = MagicMock(return_value=(50, False, False))
    return player


def test_persistence_handler_init(persistence_handler, mock_combat_service):
    """Test CombatPersistenceHandler initialization."""
    assert persistence_handler._combat_service == mock_combat_service


def test_get_persistence_layer(persistence_handler):
    """Test _get_persistence_layer gets persistence from container."""
    mock_persistence = MagicMock()
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence = mock_persistence
        mock_container.get_instance.return_value = mock_instance
        result = persistence_handler._get_persistence_layer()
        assert result == mock_persistence


def test_get_persistence_layer_no_container(persistence_handler):
    """Test _get_persistence_layer returns None when container unavailable."""
    with patch("server.container.ApplicationContainer.get_instance", side_effect=ImportError("No container")):
        result = persistence_handler._get_persistence_layer()
        assert result is None


def test_get_persistence_layer_container_error(persistence_handler):
    """Test _get_persistence_layer handles container errors."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_container.get_instance.side_effect = RuntimeError("Container error")
        result = persistence_handler._get_persistence_layer()
        assert result is None


def test_get_persistence_layer_no_async_persistence(persistence_handler):
    """Test _get_persistence_layer handles container without async_persistence."""
    with patch("server.container.ApplicationContainer") as mock_container:
        mock_instance = MagicMock()
        mock_instance.async_persistence = None
        mock_container.get_instance.return_value = mock_instance
        result = persistence_handler._get_persistence_layer()
        assert result is None


def test_log_death_state_changes_death_threshold(persistence_handler):
    """Test _log_death_state_changes logs death threshold."""
    player_id = uuid.uuid4()
    # Should not raise, just log
    persistence_handler._log_death_state_changes(player_id, "TestPlayer", -10, 5)


def test_log_death_state_changes_mortally_wounded(persistence_handler):
    """Test _log_death_state_changes logs mortally wounded."""
    player_id = uuid.uuid4()
    persistence_handler._log_death_state_changes(player_id, "TestPlayer", 0, 5)


def test_persist_player_dp_background_public_api(persistence_handler):
    """Test persist_player_dp_background public API method."""
    player_id = uuid.uuid4()
    with patch.object(persistence_handler, "_persist_player_dp_background") as mock_persist:
        persistence_handler.persist_player_dp_background(player_id, 30, 50, 100)
        mock_persist.assert_called_once_with(player_id, 30, 50, 100, None, None)
