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
        # CRITICAL FIX: Always set services on app.state if provided, even if they exist
        # This ensures command handlers can access app.state.user_manager and app.state.player_service
        # This fixes Bugs #1 and #3 where State object was missing these attributes
        if player_service is not None:
            self.app.state.player_service = player_service
            logger.debug("Player service set on app.state in request context")
        elif hasattr(self.app.state, "container") and self.app.state.container:
            # Fallback: get from container if not provided
            container_service = getattr(self.app.state.container, "player_service", None)
            if container_service:
                self.app.state.player_service = container_service
                logger.debug("Player service set on app.state from container in request context")

        if user_manager is not None:
            self.app.state.user_manager = user_manager
            logger.debug("User manager set on app.state in request context")
        elif hasattr(self.app.state, "container") and self.app.state.container:
            # Fallback: get from container if not provided
            container_manager = getattr(self.app.state.container, "user_manager", None)
            if container_manager:
                self.app.state.user_manager = container_manager
                logger.debug("User manager set on app.state from container in request context")

        logger.debug(
            "App state services verified in request context",
            player_service_available=self.app.state.player_service is not None,
            user_manager_available=self.app.state.user_manager is not None,
        )

    def get_persistence(self) -> Any:
        """Get the persistence layer from the request context."""
        # Prefer container, fallback to app.state for backward compatibility
        if hasattr(self.app.state, "container") and self.app.state.container:
            return self.app.state.container.async_persistence
        return getattr(self.app.state, "persistence", None)

    def get_event_bus(self) -> Any | None:
        """Get the event bus from the request context."""
        # Prefer container, fallback to app.state for backward compatibility
        if hasattr(self.app.state, "container") and self.app.state.container:
            return self.app.state.container.event_bus
        return getattr(self.app.state, "event_bus", None)

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
