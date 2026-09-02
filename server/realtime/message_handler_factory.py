"""
Message Handler Factory for WebSocket message routing.

This module implements a factory pattern for handling different types of
WebSocket messages, replacing the if/elif chain with a more maintainable
and extensible approach. As noted in the restricted archives, this pattern
provides O(1) lookup and eliminates the need for repetitive conditional logic.

Messages are dispatched as validated `WebSocketInboundMessage` envelopes (see
`server/schemas/realtime/websocket_messages.py`, `#765`), not raw dicts — `parse_and_validate`
already matched `message.type` against the schema registry's discriminator, so every concrete
handler's `isinstance` narrowing below always succeeds in production. It stays a real `isinstance`
check (not an `assert`/`cast`) so a caller that bypasses validation fails with a clear TypeError
rather than a silent attribute-access crash.
"""

# pyright: reportImportCycles=false
# Reason: message_handlers.py and websocket_handler.py both import back to this module
# (deferred to function scope inside handle_command_message/handle_chat_message and
# handle_websocket_message, so no runtime circular-import) to reach coordinator entry points
# and the global message_handler_factory instance. basedpyright still flags the structural
# cycle regardless of the deferred import.

# pylint: disable=too-few-public-methods  # Reason: Handler classes have focused responsibility, minimal public interface

from abc import ABC, abstractmethod

from fastapi import WebSocket

from ..error_types import ErrorMessages, ErrorType, create_websocket_error_response
from ..schemas.realtime.websocket_messages import (
    ChatMessage,
    ClientErrorReportMessage,
    CommandMessage,
    FollowResponseMessage,
    GameCommandMessage,
    PartyInviteResponseMessage,
    PingMessage,
    WebSocketInboundMessage,
)
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class MessageHandler(ABC):
    """Abstract base class for message handlers."""

    @abstractmethod
    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """
        Handle a specific message type.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID
            message: The validated, typed inbound message
        """


class CommandMessageHandler(MessageHandler):
    """Handler for command/game_command messages."""

    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """Handle command message type."""
        from .message_handlers import handle_command_message

        if not isinstance(message, CommandMessage | GameCommandMessage):
            raise TypeError(f"CommandMessageHandler received unexpected message type: {type(message)!r}")
        await handle_command_message(websocket, player_id, message)


class ChatMessageHandler(MessageHandler):
    """Handler for chat messages."""

    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """Handle chat message type."""
        from .message_handlers import handle_chat_message

        if not isinstance(message, ChatMessage):
            raise TypeError(f"ChatMessageHandler received unexpected message type: {type(message)!r}")
        await handle_chat_message(websocket, player_id, message)


class PingMessageHandler(MessageHandler):
    """Handler for ping messages."""

    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """Handle ping message type."""
        from .message_handlers import handle_ping_message

        if not isinstance(message, PingMessage):
            raise TypeError(f"PingMessageHandler received unexpected message type: {type(message)!r}")
        await handle_ping_message(websocket, player_id, message)


class FollowResponseMessageHandler(MessageHandler):
    """Handler for follow_response messages (accept/decline follow request)."""

    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """Handle follow_response message type."""
        from .message_handlers import handle_follow_response_message

        if not isinstance(message, FollowResponseMessage):
            raise TypeError(f"FollowResponseMessageHandler received unexpected message type: {type(message)!r}")
        await handle_follow_response_message(websocket, player_id, message)


class PartyInviteResponseMessageHandler(MessageHandler):
    """Handler for party_invite_response messages (accept/decline party invite)."""

    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """Handle party_invite_response message type."""
        from .message_handlers import handle_party_invite_response_message

        if not isinstance(message, PartyInviteResponseMessage):
            raise TypeError(f"PartyInviteResponseMessageHandler received unexpected message type: {type(message)!r}")
        await handle_party_invite_response_message(websocket, player_id, message)


class ClientErrorReportMessageHandler(MessageHandler):
    """Handler for client_error_report messages (client-reported errors for server logging)."""

    async def handle(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """Handle client_error_report message type."""
        from .message_handlers import handle_client_error_report_message

        if not isinstance(message, ClientErrorReportMessage):
            raise TypeError(f"ClientErrorReportMessageHandler received unexpected message type: {type(message)!r}")
        await handle_client_error_report_message(websocket, player_id, message)


class MessageHandlerFactory:
    """
    Factory for creating and managing message handlers.

    This factory replaces the if/elif chain approach with a dictionary-based
    lookup system, providing O(1) handler resolution and easy extensibility
    for new message types.

    As noted in the restricted archives, this pattern provides better
    maintainability and testability compared to conditional chains.
    """

    def __init__(self) -> None:
        """Initialize the factory with registered handlers."""
        self._handlers: dict[str, MessageHandler] = {
            "command": CommandMessageHandler(),
            "game_command": CommandMessageHandler(),  # Alias for game_command message type
            "chat": ChatMessageHandler(),
            "ping": PingMessageHandler(),
            "follow_response": FollowResponseMessageHandler(),
            "party_invite_response": PartyInviteResponseMessageHandler(),
            "client_error_report": ClientErrorReportMessageHandler(),
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

    async def handle_message(self, websocket: WebSocket, player_id: str, message: WebSocketInboundMessage) -> None:
        """
        Handle a validated WebSocket message using the appropriate handler.

        `message.type` is one of the schema registry's discriminator values (see
        `WebSocketInboundMessage`), which `test_websocket_message_schema_registry.py` asserts is
        exactly this factory's registered key set — so the "no handler" branch below is
        unreachable for any message that passed `parse_and_validate`. It stays as defence in
        depth for callers that construct a message some other way.

        Args:
            websocket: The WebSocket connection
            player_id: The player's ID
            message: The validated, typed inbound message
        """
        message_type = message.type

        handler = self.get_handler(message_type)
        if handler:
            await handler.handle(websocket, player_id, message)
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
