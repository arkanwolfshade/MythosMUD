"""
Personal message delivery for connection management.

This module provides direct message delivery to individual players,
including payload optimization and message queueing.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Personal message delivery is now a focused, independently testable component.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Message sending requires many parameters for context and message routing

import uuid
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from fastapi import WebSocketDisconnect

from ...exceptions import DatabaseError
from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from fastapi import WebSocket

    from ..message_queue import MessageQueue

logger = get_logger(__name__)


class PersonalMessageSender:
    """
    Sends personal messages to individual players.

    This class provides:
    - Personal message delivery via WebSocket
    - Payload optimization
    - Message queueing for offline players
    - Delivery status tracking

    AI Agent: Single Responsibility - Personal message delivery only.
    """

    def __init__(
        self,
        message_queue: "MessageQueue",
        cleanup_dead_websocket_callback: Callable[[uuid.UUID, str], "Awaitable[None]"],
        convert_uuids_to_strings: Callable[[Any], Any],
    ) -> None:
        """
        Initialize the personal message sender.

        Args:
            message_queue: MessageQueue instance
            cleanup_dead_websocket_callback: Callback to cleanup dead WebSocket
            convert_uuids_to_strings: Callback to convert UUIDs to strings
        """
        self.message_queue = message_queue
        self.cleanup_dead_websocket = cleanup_dead_websocket_callback
        self.convert_uuids_to_strings = convert_uuids_to_strings

    def _prepare_payload(self, player_id: uuid.UUID, event: dict[str, Any]) -> dict[str, Any]:
        """Prepare and optimize the payload for sending."""
        serializable_event = self.convert_uuids_to_strings(event)

        try:
            from ..payload_optimizer import get_payload_optimizer

            optimizer = get_payload_optimizer()
            serializable_event = optimizer.optimize_payload(serializable_event)
        except ValueError as size_error:
            logger.error(
                "Payload too large to send",
                player_id=player_id,
                error=str(size_error),
                event_type=event.get("event_type"),
            )
            serializable_event = {
                "type": "error",
                "error_type": "payload_too_large",
                "message": "Message payload too large to transmit",
                "details": {"max_size": optimizer.max_payload_size},
            }
        except (DatabaseError, AttributeError) as opt_error:
            logger.warning(
                "Payload optimization failed, using original",
                player_id=player_id,
                error=str(opt_error),
            )

        if event.get("event_type") == "game_state":
            logger.info("Sending game_state event", player_id=player_id, event_data=serializable_event)

        return serializable_event

    async def _send_to_websocket(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: WebSocket sending requires many parameters for context and message routing
        self,
        player_id: uuid.UUID,
        connection_id: str,
        websocket: "WebSocket",
        serializable_event: dict[str, Any],
        delivery_status: dict[str, Any],
    ) -> bool:
        """Send message to a single WebSocket connection. Returns True if successful."""
        if websocket is None:
            delivery_status["websocket_failed"] += 1  # type: ignore[unreachable]  # Reason: Function signature says websocket is non-optional, but runtime can have None during cleanup/race conditions, this is defensive programming
            await self.cleanup_dead_websocket(player_id, connection_id)
            return False

        try:
            from starlette.websockets import WebSocketState

            ws_state = getattr(websocket, "application_state", None)
            if ws_state == WebSocketState.DISCONNECTED:
                delivery_status["websocket_failed"] += 1
                await self.cleanup_dead_websocket(player_id, connection_id)
                return False

            await websocket.send_json(serializable_event)
            delivery_status["websocket_delivered"] += 1
            delivery_status["active_connections"] += 1
            return True
        except (RuntimeError, ConnectionError, WebSocketDisconnect) as ws_error:
            error_message = str(ws_error)
            if (
                "close message has been sent" not in error_message.lower()
                and "cannot call" not in error_message.lower()
            ):
                logger.warning(
                    "WebSocket send failed",
                    player_id=player_id,
                    connection_id=connection_id,
                    error=error_message,
                )
            delivery_status["websocket_failed"] += 1
            await self.cleanup_dead_websocket(player_id, connection_id)
            return False

    async def _queue_message_if_needed(
        self,
        player_id: uuid.UUID,
        serializable_event: dict[str, Any],
        delivery_status: dict[str, Any],
        had_connection_attempts: bool,
    ) -> None:
        """Queue message if no active connections."""
        if not delivery_status["active_connections"]:
            player_id_str = str(player_id)
            if player_id_str not in self.message_queue.pending_messages:
                self.message_queue.pending_messages[player_id_str] = []
            self.message_queue.pending_messages[player_id_str].append(serializable_event)
            logger.debug(
                "No active connections, queued message for later delivery",
                player_id=player_id,
                event_type=serializable_event.get("event_type"),
            )

            if had_connection_attempts and delivery_status["websocket_failed"] > 0:
                delivery_status["success"] = False
            else:
                delivery_status["success"] = True
        else:
            delivery_status["success"] = delivery_status["websocket_delivered"] > 0

    async def send_message(
        self,
        player_id: uuid.UUID,
        event: dict[str, Any],
        player_websockets: dict[uuid.UUID, list[str]],
        active_websockets: dict[str, "WebSocket"],
    ) -> dict[str, Any]:
        """
        Send a personal message to a player via WebSocket.

        Args:
            player_id: The player's ID (UUID)
            event: The event data to send
            player_websockets: Player to WebSocket connection mapping
            active_websockets: Active WebSocket connections

        Returns:
            dict: Delivery status
        """
        delivery_status = {
            "success": False,
            "websocket_delivered": 0,
            "websocket_failed": 0,
            "total_connections": 0,
            "active_connections": 0,
        }

        try:
            serializable_event = self._prepare_payload(player_id, event)

            websocket_count = len(player_websockets.get(player_id, []))
            delivery_status["total_connections"] = websocket_count

            had_connection_attempts = False

            if player_id in player_websockets:
                connection_ids = player_websockets[player_id].copy()
                for connection_id in connection_ids:
                    if connection_id in active_websockets:
                        had_connection_attempts = True
                        websocket = active_websockets[connection_id]
                        await self._send_to_websocket(
                            player_id, connection_id, websocket, serializable_event, delivery_status
                        )

            await self._queue_message_if_needed(player_id, serializable_event, delivery_status, had_connection_attempts)

            logger.debug("Message delivery status", player_id=player_id, delivery_status=delivery_status)
            return delivery_status

        except (DatabaseError, AttributeError) as e:
            logger.error("Failed to send personal message", player_id=player_id, error=str(e))
            delivery_status["success"] = False
            return delivery_status

    def get_delivery_stats(self, player_id: uuid.UUID, player_websockets: dict[uuid.UUID, list[str]]) -> dict[str, Any]:
        """Get message delivery statistics for a player."""
        player_id_str = str(player_id)
        stats: dict[str, Any] = {
            "player_id": player_id,
            "websocket_connections": len(player_websockets.get(player_id, [])),
            "total_connections": 0,
            "pending_messages": len(self.message_queue.pending_messages.get(player_id_str, [])),
            "has_active_connections": False,
        }

        stats["total_connections"] = stats["websocket_connections"]
        stats["has_active_connections"] = stats["total_connections"] > 0

        return stats
