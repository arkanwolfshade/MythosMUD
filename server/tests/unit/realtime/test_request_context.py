"""
Unit tests for request context.

Tests the request_context module classes and functions.
"""

from unittest.mock import MagicMock

import pytest

from server.realtime.request_context import WebSocketRequestContext, create_websocket_request_context


def test_websocket_request_context_init():
    """Test WebSocketRequestContext initialization."""
    mock_app_state = MagicMock()
    mock_user = MagicMock()

    context = WebSocketRequestContext(mock_app_state, mock_user)

    assert context.app.state == mock_app_state
    assert context.user == mock_user


def test_websocket_request_context_init_no_user():
    """Test WebSocketRequestContext initialization without user."""
    mock_app_state = MagicMock()

    context = WebSocketRequestContext(mock_app_state, None)

    assert context.app.state == mock_app_state
    assert context.user is None


def test_websocket_request_context_set_alias_storage():
    """Test WebSocketRequestContext.set_alias_storage()."""
    mock_app_state = MagicMock()
    mock_alias_storage = MagicMock()

    context = WebSocketRequestContext(mock_app_state)
    context.set_alias_storage(mock_alias_storage)

    assert context.app.state.alias_storage == mock_alias_storage


def test_websocket_request_context_set_app_state_services():
    """Test WebSocketRequestContext.set_app_state_services()."""
    mock_app_state = MagicMock()
    mock_app_state.player_service = MagicMock()
    mock_app_state.user_manager = MagicMock()
    mock_player_service = MagicMock()
    mock_user_manager = MagicMock()

    context = WebSocketRequestContext(mock_app_state)
    context.set_app_state_services(mock_player_service, mock_user_manager)

    assert context.app.state.player_service == mock_player_service
    assert context.app.state.user_manager == mock_user_manager


def test_websocket_request_context_set_app_state_services_none():
    """Test WebSocketRequestContext.set_app_state_services() with None values."""
    mock_app_state = MagicMock()
    mock_app_state.player_service = MagicMock()
    mock_app_state.user_manager = MagicMock()

    context = WebSocketRequestContext(mock_app_state)
    context.set_app_state_services(None, None)

    # Should keep existing services
    assert context.app.state.player_service is not None
    assert context.app.state.user_manager is not None


def test_websocket_request_context_get_persistence():
    """Test WebSocketRequestContext.get_persistence()."""
    mock_app_state = MagicMock()
    mock_persistence = MagicMock()
    mock_app_state.persistence = mock_persistence

    context = WebSocketRequestContext(mock_app_state)

    result = context.get_persistence()
    assert result == mock_persistence


def test_websocket_request_context_get_event_bus():
    """Test WebSocketRequestContext.get_event_bus()."""
    mock_app_state = MagicMock()
    mock_event_bus = MagicMock()
    mock_app_state.event_bus = mock_event_bus

    context = WebSocketRequestContext(mock_app_state)

    result = context.get_event_bus()
    assert result == mock_event_bus


def test_websocket_request_context_get_event_bus_none():
    """Test WebSocketRequestContext.get_event_bus() when event_bus is None."""
    mock_app_state = MagicMock()
    mock_app_state.event_bus = None

    context = WebSocketRequestContext(mock_app_state)

    result = context.get_event_bus()
    assert result is None


def test_websocket_request_context_get_alias_storage():
    """Test WebSocketRequestContext.get_alias_storage()."""
    mock_app_state = MagicMock()
    mock_alias_storage = MagicMock()
    mock_app_state.alias_storage = mock_alias_storage

    context = WebSocketRequestContext(mock_app_state)

    result = context.get_alias_storage()
    assert result == mock_alias_storage


def test_websocket_request_context_get_alias_storage_not_set():
    """Test WebSocketRequestContext.get_alias_storage() when not set."""
    mock_app_state = MagicMock()
    # Remove alias_storage attribute to simulate it not being set
    if hasattr(mock_app_state, "alias_storage"):
        del mock_app_state.alias_storage

    context = WebSocketRequestContext(mock_app_state)

    result = context.get_alias_storage()
    assert result is None


def test_create_websocket_request_context():
    """Test create_websocket_request_context() factory function."""
    mock_app_state = MagicMock()
    mock_user = MagicMock()

    context = create_websocket_request_context(mock_app_state, mock_user)

    assert isinstance(context, WebSocketRequestContext)
    assert context.app.state == mock_app_state
    assert context.user == mock_user


def test_create_websocket_request_context_no_user():
    """Test create_websocket_request_context() without user."""
    mock_app_state = MagicMock()

    context = create_websocket_request_context(mock_app_state, None)

    assert isinstance(context, WebSocketRequestContext)
    assert context.app.state == mock_app_state
    assert context.user is None
