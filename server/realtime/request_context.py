"""
Request context factory for WebSocket command processing.

This module provides utilities to create FastAPI Request-like objects
for WebSocket commands, enabling unified command processing between
HTTP and WebSocket interfaces.
"""

from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class WebSocketRequestContext:
    """
    Creates FastAPI Request-like objects for WebSocket commands.

    This allows WebSocket connections to use the same command processing
    logic as HTTP requests, ensuring consistency across all interfaces.
    """

    def __init__(self, app_state: Any, user: Any | None = None):
        """
        Initialize the WebSocket request context.

        Args:
            app_state: Real application state object
            user: User object with authentication context
        """
        # Use the real app state instead of creating a mock
        self.app = type("WebSocketApp", (), {"state": app_state})()

        # Store user context
        self.user = user

        logger.debug(
            "WebSocket request context created with real app state",
            has_persistence=hasattr(app_state, "persistence"),
            has_event_bus=hasattr(app_state, "event_bus"),
            has_user=user is not None,
        )

    def set_alias_storage(self, alias_storage: Any) -> None:
        """
        Set the alias storage in the app state.

        Args:
            alias_storage: Alias storage instance
        """
        self.app.state.alias_storage = alias_storage
        logger.debug("Alias storage set in request context")

    def set_app_state_services(self, player_service: Any, user_manager: Any) -> None:
        """
        Set the app state services in the request context.
        Note: This method is kept for backward compatibility but services
        should already be available in the real app state.

        Args:
            player_service: Player service instance
            user_manager: User manager instance
        """
        logger.debug(
            "App state services already available",
            player_service_available=self.app.state.player_service is not None,
            user_manager_available=self.app.state.user_manager is not None,
        )
        # Services should already be available in the real app state
        # Only override if explicitly provided and different
        if player_service is not None:
            self.app.state.player_service = player_service
        if user_manager is not None:
            self.app.state.user_manager = user_manager
        logger.debug("App state services verified in request context")

    def get_persistence(self) -> Any:
        """Get the persistence layer from the request context."""
        return self.app.state.persistence

    def get_event_bus(self) -> Any | None:
        """Get the event bus from the request context."""
        return self.app.state.event_bus

    def get_alias_storage(self) -> Any | None:
        """Get the alias storage from the request context."""
        return getattr(self.app.state, "alias_storage", None)


def create_websocket_request_context(app_state: Any, user: Any | None = None) -> WebSocketRequestContext:
    """
    Factory function to create a WebSocket request context.

    Args:
        app_state: Real application state object
        user: User object with authentication context

    Returns:
        WebSocketRequestContext: Configured request context
    """
    return WebSocketRequestContext(app_state, user)
