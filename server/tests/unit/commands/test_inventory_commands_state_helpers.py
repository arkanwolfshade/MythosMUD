"""
Unit tests for inventory command state helper functions.

Tests the state resolution helper functions in inventory_commands.py.
"""

from unittest.mock import MagicMock

from server.commands.inventory_commands import _resolve_state


def test_resolve_state_success():
    """Test _resolve_state() resolves persistence and connection manager."""
    mock_persistence = MagicMock()
    mock_connection_manager = MagicMock()
    mock_state = MagicMock()
    mock_state.persistence = mock_persistence
    mock_state.connection_manager = mock_connection_manager
    mock_app = MagicMock()
    mock_app.state = mock_state
    mock_request = MagicMock()
    mock_request.app = mock_app
    persistence, connection_manager = _resolve_state(mock_request)
    assert persistence == mock_persistence
    assert connection_manager == mock_connection_manager


def test_resolve_state_no_app():
    """Test _resolve_state() handles missing app."""
    mock_request = MagicMock()
    mock_request.app = None
    persistence, connection_manager = _resolve_state(mock_request)
    assert persistence is None
    assert connection_manager is None


def test_resolve_state_no_state():
    """Test _resolve_state() handles missing state."""
    mock_app = MagicMock()
    mock_app.state = None
    mock_request = MagicMock()
    mock_request.app = mock_app
    persistence, connection_manager = _resolve_state(mock_request)
    assert persistence is None
    assert connection_manager is None
