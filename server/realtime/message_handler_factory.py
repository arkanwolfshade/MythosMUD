"""
Message Handler Factory for WebSocket message routing.

This module implements a factory pattern for handling different types of
WebSocket messages, replacing the if/elif chain with a more maintainable
and extensible approach. As noted in the restricted archives, this pattern
provides O(1) lookup and eliminates the need for repetitive conditional logic.
"""

from abc import ABC, abstractmethod
from typing import Any

from fastapi import WebSocket

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MessageHandler(ABC):
    """Abstract base class for message handlers."""

    @abstractmethod
    async def handle(self, websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
        """
        Handle a specific message type.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID
            data: The message data
        """
        pass


class CommandMessageHandler(MessageHandler):
    """Handler for command messages."""

    async def handle(self, websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
        """Handle command message type."""
        from .message_handlers import handle_command_message

        await handle_command_message(websocket, player_id, data)


class ChatMessageHandler(MessageHandler):
    """Handler for chat messages."""

    async def handle(self, websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
        """Handle chat message type."""
        from .message_handlers import handle_chat_message

        await handle_chat_message(websocket, player_id, data)


class PingMessageHandler(MessageHandler):
    """Handler for ping messages."""

    async def handle(self, websocket: WebSocket, player_id: str, data: dict[str, Any]) -> None:
        """Handle ping message type."""
        from .message_handlers import handle_ping_message

        await handle_ping_message(websocket, player_id, data)


class MessageHandlerFactory:
    """
    Factory for creating and managing message handlers.

    This factory pattern eliminates the need for if/elif chains in message
    routing and provides O(1) lookup for message handlers. As noted in the
    restricted archives, this approach scales better as new message types
    are added to the system.
    """

    def __init__(self):
        """Initialize the factory with registered handlers."""
        self._handlers: dict[str, MessageHandler] = {
            "command": CommandMessageHandler(),
            "game_command": CommandMessageHandler(),  # Alias for game_command message type
            "chat": ChatMessageHandler(),
            "ping": PingMessageHandler(),
        }

    def register_handler(self, message_type: str, handler: MessageHandler) -> None:
        """
        Register a new message handler.

        Args:
            message_type: The message type to handle
            handler: The handler instance
        """
        self._handlers[message_type] = handler
        logger.debug("Registered handler for message type", message_type=message_type)

    def get_handler(self, message_type: str) -> MessageHandler | None:
        """
        Get a handler for the specified message type.

        Args:
            message_type: The message type to get handler for

        Returns:
            The message handler or None if not found
        """
        return self._handlers.get(message_type)

    async def handle_message(self, websocket: WebSocket, player_id: str, message: dict[str, Any]) -> None:
        """
        Handle a WebSocket message using the appropriate handler.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID
            message: The message data

        Raises:
            ValueError: If no handler is found for the message type
        """
        message_type = message.get("type", "unknown")
        data = message.get("data", {})

        logger.info(
            "🚨 SERVER DEBUG: message_handler_factory.handle_message called",
            extra={"message_type": message_type, "data": data, "player_id": player_id, "full_message": message},
        )

        handler = self.get_handler(message_type)
        if handler:
            logger.info("🚨 SERVER DEBUG: Found handler for message type", message_type=message_type)
            await handler.handle(websocket, player_id, data)
        else:
            # Unknown message type - send error response
            logger.warning("Unknown message type", message_type=message_type, player_id=player_id)
            error_response = create_websocket_error_response(
                ErrorType.INVALID_COMMAND,
                f"Unknown message type: {message_type}",
                ErrorMessages.INVALID_COMMAND,
                {"message_type": message_type, "player_id": player_id},
            )
            await websocket.send_json(error_response)

    def get_supported_message_types(self) -> list[str]:
        """
        Get a list of supported message types.

        Returns:
            List of supported message type strings
        """
        return list(self._handlers.keys())


# Global factory instance
message_handler_factory = MessageHandlerFactory()
