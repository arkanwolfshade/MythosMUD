"""
Request context factory for WebSocket command processing.

This module provides utilities to create FastAPI Request-like objects
for WebSocket commands, enabling unified command processing between
HTTP and WebSocket interfaces.
"""

from typing import Any

from ..logging_config import get_logger

logger = get_logger(__name__)


class WebSocketRequestContext:
    """
    Creates FastAPI Request-like objects for WebSocket commands.

    This allows WebSocket connections to use the same command processing
    logic as HTTP requests, ensuring consistency across all interfaces.
    """

    def __init__(self, persistence: Any, event_bus: Any | None = None, user: Any | None = None):
        """
        Initialize the WebSocket request context.

        Args:
            persistence: Database persistence layer
            event_bus: Event bus for inter-service communication
            user: User object with authentication context
        """
        # Create a mock app state with required attributes
        mock_state = type(
            "MockState",
            (),
            {
                "persistence": persistence,
                "event_bus": event_bus,
                "alias_storage": None,  # Will be set separately
            },
        )()

        # Create a mock app with the state
        self.app = type("MockApp", (), {"state": mock_state})()

        # Store user context
        self.user = user

        logger.debug(
            "WebSocket request context created",
            has_persistence=persistence is not None,
            has_event_bus=event_bus is not None,
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

    def get_persistence(self) -> Any:
        """Get the persistence layer from the request context."""
        return self.app.state.persistence

    def get_event_bus(self) -> Any | None:
        """Get the event bus from the request context."""
        return self.app.state.event_bus

    def get_alias_storage(self) -> Any | None:
        """Get the alias storage from the request context."""
        return getattr(self.app.state, "alias_storage", None)


def create_websocket_request_context(
    persistence: Any, event_bus: Any | None = None, user: Any | None = None
) -> WebSocketRequestContext:
    """
    Factory function to create a WebSocket request context.

    Args:
        persistence: Database persistence layer
        event_bus: Event bus for inter-service communication
        user: User object with authentication context

    Returns:
        WebSocketRequestContext: Configured request context
    """
    return WebSocketRequestContext(persistence, event_bus, user)
