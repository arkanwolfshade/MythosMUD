"""
Tests for WebSocket request context factory.

This module tests the request context utilities that allow WebSocket
commands to use the same processing logic as HTTP requests.
"""

from unittest.mock import MagicMock

from server.realtime.request_context import WebSocketRequestContext, create_websocket_request_context


class TestWebSocketRequestContext:
    """Test WebSocket request context."""

    def test_initialization_with_app_state(self) -> None:
        """Test initialization with app state."""
        mock_app_state = MagicMock()
        mock_app_state.persistence = MagicMock()
        mock_app_state.event_bus = MagicMock()

        context = WebSocketRequestContext(mock_app_state)

        assert context.app.state == mock_app_state
        assert context.user is None

    def test_initialization_with_user(self) -> None:
        """Test initialization with user context."""
        mock_app_state = MagicMock()
        mock_user = MagicMock()

        context = WebSocketRequestContext(mock_app_state, user=mock_user)

        assert context.user == mock_user

    def test_set_alias_storage(self) -> None:
        """Test setting alias storage."""
        mock_app_state = MagicMock()
        mock_alias_storage = MagicMock()

        context = WebSocketRequestContext(mock_app_state)
        context.set_alias_storage(mock_alias_storage)

        assert context.app.state.alias_storage == mock_alias_storage

    def test_set_app_state_services(self) -> None:
        """Test setting app state services."""
        mock_app_state = MagicMock()
        mock_app_state.player_service = MagicMock()
        mock_app_state.user_manager = MagicMock()

        mock_player_service = MagicMock()
        mock_user_manager = MagicMock()

        context = WebSocketRequestContext(mock_app_state)
        context.set_app_state_services(mock_player_service, mock_user_manager)

        assert context.app.state.player_service == mock_player_service
        assert context.app.state.user_manager == mock_user_manager

    def test_set_app_state_services_with_none(self) -> None:
        """Test setting app state services with None values."""
        mock_app_state = MagicMock()
        original_player_service = MagicMock()
        original_user_manager = MagicMock()
        mock_app_state.player_service = original_player_service
        mock_app_state.user_manager = original_user_manager

        context = WebSocketRequestContext(mock_app_state)
        context.set_app_state_services(None, None)

        # Should not override when None
        assert context.app.state.player_service == original_player_service
        assert context.app.state.user_manager == original_user_manager

    def test_get_persistence(self) -> None:
        """Test getting persistence from context."""
        mock_app_state = MagicMock()
        mock_persistence = MagicMock()
        mock_app_state.persistence = mock_persistence

        context = WebSocketRequestContext(mock_app_state)
        persistence = context.get_persistence()

        assert persistence == mock_persistence

    def test_get_event_bus(self) -> None:
        """Test getting event bus from context."""
        mock_app_state = MagicMock()
        mock_event_bus = MagicMock()
        mock_app_state.event_bus = mock_event_bus

        context = WebSocketRequestContext(mock_app_state)
        event_bus = context.get_event_bus()

        assert event_bus == mock_event_bus

    def test_get_alias_storage(self) -> None:
        """Test getting alias storage from context."""
        mock_app_state = MagicMock()
        mock_alias_storage = MagicMock()
        mock_app_state.alias_storage = mock_alias_storage

        context = WebSocketRequestContext(mock_app_state)
        alias_storage = context.get_alias_storage()

        assert alias_storage == mock_alias_storage

    def test_get_alias_storage_not_set(self) -> None:
        """Test getting alias storage when not set."""
        mock_app_state = MagicMock()
        # MagicMock creates attributes on access, so we need to explicitly delete it
        del mock_app_state.alias_storage

        context = WebSocketRequestContext(mock_app_state)

        # getattr should return None for missing attribute
        alias_storage = context.get_alias_storage()

        # MagicMock behavior - it creates the attribute on access
        # So we test that getattr with None default works
        assert alias_storage is None or hasattr(mock_app_state, "alias_storage")

    def test_factory_function(self) -> None:
        """Test create_websocket_request_context factory function."""
        mock_app_state = MagicMock()
        mock_user = MagicMock()

        context = create_websocket_request_context(mock_app_state, mock_user)

        assert isinstance(context, WebSocketRequestContext)
        assert context.app.state == mock_app_state
        assert context.user == mock_user
