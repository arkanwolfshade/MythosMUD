"""
Unit tests for game tick processing functions.

Tests the game tick processing logic including status effects, combat, and maintenance tasks.
"""

from unittest.mock import MagicMock, patch

from fastapi import FastAPI

from server.app.game_tick_processing import (
    _validate_app_state_for_status_effects,
    get_current_tick,
    get_tick_interval,
    reset_current_tick,
)


def test_get_current_tick():
    """Test get_current_tick returns the current tick value."""
    # Reset to known state
    reset_current_tick()
    assert get_current_tick() == 0


def test_reset_current_tick():
    """Test reset_current_tick resets the tick counter."""
    # Set tick to non-zero (we can't directly set it, but we can test reset)
    reset_current_tick()
    initial = get_current_tick()
    assert initial == 0

    # Reset again should still be 0
    reset_current_tick()
    assert get_current_tick() == 0


def test_get_tick_interval():
    """Test get_tick_interval returns tick interval from config."""
    with patch("server.app.game_tick_processing.get_config") as mock_config:
        mock_config_instance = MagicMock()
        mock_config_instance.game.server_tick_rate = 0.5
        mock_config.return_value = mock_config_instance

        interval = get_tick_interval()
        assert interval == 0.5


def test_validate_app_state_for_status_effects_no_container():
    """Test _validate_app_state_for_status_effects returns False when no container."""
    app = FastAPI()
    app.state = MagicMock()
    del app.state.container  # Remove container attribute

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_no_async_persistence():
    """Test _validate_app_state_for_status_effects returns False when no async_persistence."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_no_connection_manager():
    """Test _validate_app_state_for_status_effects returns False when no connection_manager."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = None  # Set connection_manager to None
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_valid():
    """Test _validate_app_state_for_status_effects returns True when all required components exist."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = MagicMock()
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is True
    assert container == mock_container


def test_validate_app_state_for_status_effects_container_is_none():
    """Test _validate_app_state_for_status_effects returns False when container is None."""
    app = FastAPI()
    app.state = MagicMock()
    app.state.container = None

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None


def test_validate_app_state_for_status_effects_connection_manager_is_none():
    """Test _validate_app_state_for_status_effects returns False when connection_manager is None."""
    app = FastAPI()
    app.state = MagicMock()
    mock_container = MagicMock()
    mock_container.async_persistence = MagicMock()
    mock_container.connection_manager = None  # Set connection_manager to None in container
    app.state.container = mock_container

    is_valid, container = _validate_app_state_for_status_effects(app)
    assert is_valid is False
    assert container is None
