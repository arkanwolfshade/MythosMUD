"""
Tests for Real-Time API endpoints.

This module tests the WebSocket connection handling and real-time communication
endpoints for the MythosMUD server.

AI Agent: Tests for real-time API covering connection manager resolution,
         state management, and WebSocket endpoint logic. Created for fresh session execution.
"""

# pylint: disable=redefined-outer-name,protected-access
# Justification: pytest fixtures redefine names, protected access needed for testing internals

from unittest.mock import Mock, patch

import pytest
from fastapi import HTTPException


# Note: These imports will trigger bcrypt in same session as other tests
# Run in fresh terminal: uv run pytest server/tests/unit/api/test_real_time.py -v
@pytest.fixture
def real_time_module():
    """Lazily import real_time module."""
    from server.api import real_time

    return real_time


@pytest.fixture
def mock_connection_manager():
    """Provide mock connection manager."""
    manager = Mock()
    manager.async_persistence = Mock()
    return manager


@pytest.fixture
def mock_state_with_manager(mock_connection_manager):
    """Provide mock state with connection manager."""
    state = Mock()
    state.container = Mock()
    state.container.connection_manager = mock_connection_manager
    return state


@pytest.fixture
def mock_state_without_manager():
    """Provide mock state without connection manager."""
    state = Mock()
    state.container = Mock()
    state.container.connection_manager = None
    return state


class TestResolveConnectionManagerFromState:
    """Test _resolve_connection_manager_from_state helper function."""

    @patch("server.api.real_time.resolve_connection_manager")
    def test_resolves_manager_from_container_dict(self, mock_resolve, real_time_module, mock_connection_manager):
        """Test resolves connection manager from container __dict__."""
        mock_resolve.return_value = mock_connection_manager

        state = Mock()
        state.container = Mock()
        state.container.__dict__ = {"connection_manager": mock_connection_manager}

        result = real_time_module._resolve_connection_manager_from_state(state)

        assert result == mock_connection_manager
        mock_resolve.assert_called_once()

    @patch("server.api.real_time.resolve_connection_manager")
    def test_resolves_manager_from_container_attribute(self, mock_resolve, real_time_module, mock_connection_manager):
        """Test resolves connection manager from container attribute."""
        mock_resolve.return_value = mock_connection_manager

        state = Mock()
        state.container = Mock()
        state.container.connection_manager = mock_connection_manager
        # Ensure it doesn't have __dict__ entry
        if hasattr(state.container, "__dict__"):
            delattr(state.container, "__dict__")

        _ = real_time_module._resolve_connection_manager_from_state(state)

        mock_resolve.assert_called_once()

    @patch("server.api.real_time.resolve_connection_manager")
    def test_handles_none_container(self, _mock_resolve, real_time_module):
        """Test handles state with no container."""
        _mock_resolve.return_value = None

        state = Mock()
        state.container = None

        result = real_time_module._resolve_connection_manager_from_state(state)

        assert result is None

    @patch("server.api.real_time.resolve_connection_manager")
    def test_handles_mock_container(self, _mock_resolve, real_time_module):
        """Test handles Mock container gracefully."""
        _mock_resolve.return_value = None

        state = Mock()
        state.container = Mock()

        _ = real_time_module._resolve_connection_manager_from_state(state)

        _mock_resolve.assert_called_once()


class TestEnsureConnectionManager:
    """Test _ensure_connection_manager helper function."""

    @patch("server.api.real_time._resolve_connection_manager_from_state")
    def test_returns_manager_when_available(self, mock_resolve, real_time_module, mock_connection_manager):
        """Test returns connection manager when available."""
        mock_resolve.return_value = mock_connection_manager

        state = Mock()
        result = real_time_module._ensure_connection_manager(state)

        assert result == mock_connection_manager

    @patch("server.api.real_time._resolve_connection_manager_from_state")
    def test_raises_503_when_manager_not_available(self, mock_resolve, real_time_module):
        """Test raises HTTPException when manager not available."""
        mock_resolve.return_value = None

        state = Mock()

        with pytest.raises(HTTPException) as exc_info:
            real_time_module._ensure_connection_manager(state)

        assert exc_info.value.status_code == 503
        assert "unavailable" in exc_info.value.detail.lower()


class TestRealtimeRouter:
    """Test real-time router configuration."""

    def test_router_exists(self, real_time_module):
        """Test realtime router is properly configured."""
        assert hasattr(real_time_module, "realtime_router")
        assert real_time_module.realtime_router is not None

    def test_router_has_correct_prefix(self, real_time_module):
        """Test router configured with correct prefix."""
        router = real_time_module.realtime_router
        assert router.prefix == "/api"

    def test_router_has_realtime_tag(self, real_time_module):
        """Test router tagged with 'realtime'."""
        router = real_time_module.realtime_router
        assert "realtime" in router.tags
