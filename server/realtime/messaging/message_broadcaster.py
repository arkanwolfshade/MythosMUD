"""
Message broadcasting for connection management.

This module provides room and global message broadcasting with concurrent
delivery optimization.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Message broadcasting is now a focused, independently testable component.
"""

import asyncio
import uuid
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from ..room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)


class MessageBroadcaster:
    """
    Broadcasts messages to rooms and globally.

    This class provides:
    - Room-scoped broadcasting
    - Global broadcasting
    - Concurrent message delivery
    - Delivery statistics tracking
    - Player exclusion support

    AI Agent: Single Responsibility - Message broadcasting only.
    """

    def __init__(
        self,
        room_manager: "RoomSubscriptionManager",
        send_personal_message_callback: Callable[[uuid.UUID, dict[str, Any]], "Awaitable[dict[str, Any]]"],
    ) -> None:
        """
        Initialize the message broadcaster.

        Args:
            room_manager: RoomSubscriptionManager instance
            send_personal_message_callback: Callback to send personal message
        """
        self.room_manager = room_manager
        self.send_personal_message = send_personal_message_callback

    def _build_target_mapping(
        self, target_list: list[str], room_id: str, broadcast_stats: dict[str, Any]
    ) -> list[tuple[str, uuid.UUID]]:
        """
        Convert string player IDs to UUIDs for message sending.

        Args:
            target_list: List of player ID strings
            room_id: Room ID for logging
            broadcast_stats: Stats dict to update with failures

        Returns:
            List of (player_id_str, player_id_uuid) tuples
        """
        target_mapping: list[tuple[str, uuid.UUID]] = []
        for pid_str in target_list:
            try:
                pid_uuid = uuid.UUID(pid_str)
                target_mapping.append((pid_str, pid_uuid))
            except (ValueError, TypeError, AttributeError):
                logger.warning("Invalid player ID format in room subscribers", player_id=pid_str, room_id=room_id)
                broadcast_stats["delivery_details"][pid_str] = {
                    "success": False,
                    "error": "Invalid player ID format",
                }
                broadcast_stats["failed_deliveries"] += 1
        return target_mapping

    def _process_batch_delivery_results(
        self,
        delivery_results: list[Any],
        target_mapping: list[tuple[str, uuid.UUID]],
        room_id: str,
        broadcast_stats: dict[str, Any],
    ) -> None:
        """
        Process results from batch message delivery.

        Args:
            delivery_results: Results from asyncio.gather
            target_mapping: List of (player_id_str, player_id_uuid) tuples
            room_id: Room ID for logging
            broadcast_stats: Stats dict to update
        """
        for i, (pid_str, _pid_uuid) in enumerate(target_mapping):
            if i >= len(delivery_results):
                continue
            result = delivery_results[i]
            if isinstance(result, Exception):
                logger.error(
                    "Error sending message in batch broadcast",
                    player_id=pid_str,
                    room_id=room_id,
                    error=str(result),
                )
                broadcast_stats["delivery_details"][pid_str] = {"success": False, "error": str(result)}
                broadcast_stats["failed_deliveries"] += 1
            else:
                delivery_status: dict[str, Any] = result
                broadcast_stats["delivery_details"][pid_str] = delivery_status
                if delivery_status["success"]:
                    broadcast_stats["successful_deliveries"] += 1
                else:
                    broadcast_stats["failed_deliveries"] += 1

    async def _fallback_individual_send(
        self,
        target_mapping: list[tuple[str, uuid.UUID]],
        event: dict[str, Any],
        _room_id: str,
        broadcast_stats: dict[str, Any],
    ) -> None:
        """
        Fallback to individual message sending if batch fails.

        Args:
            target_mapping: List of (player_id_str, player_id_uuid) tuples
            event: Event to send
            room_id: Room ID for logging
            broadcast_stats: Stats dict to update
        """
        for pid_str, pid_uuid in target_mapping:
            try:
                delivery_status = await self.send_personal_message(pid_uuid, event)
                broadcast_stats["delivery_details"][pid_str] = delivery_status
                if delivery_status["success"]:
                    broadcast_stats["successful_deliveries"] += 1
                else:
                    broadcast_stats["failed_deliveries"] += 1
            except Exception as individual_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Individual message sending errors unpredictable, must continue processing
                logger.error(
                    "Error sending individual message in fallback",
                    player_id=pid_str,
                    error=str(individual_error),
                )
                broadcast_stats["failed_deliveries"] += 1

    async def broadcast_to_room(
        self,
        room_id: str,
        event: dict[str, Any],
        exclude_player: uuid.UUID | str | None = None,
        _player_websockets: dict[uuid.UUID, list[str]] | None = None,  # pylint: disable=unused-argument  # Reason: Parameter reserved for future websocket filtering
    ) -> dict[str, Any]:
        """
        Broadcast a message to all players in a room.

        Args:
            room_id: The room's ID
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast (UUID or string)
            player_websockets: Player to WebSocket connection mapping (for validation)

        Returns:
            dict: Broadcast delivery statistics
        """
        targets = await self.room_manager.get_room_subscribers(room_id)

        broadcast_stats: dict[str, Any] = {
            "room_id": room_id,
            "total_targets": len(targets),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        # Convert exclude_player to string for comparison with targets (room_manager uses strings)
        exclude_player_str = str(exclude_player) if exclude_player else None

        logger.debug("broadcast_to_room", room_id=room_id, exclude_player=exclude_player_str)
        logger.debug("broadcast_to_room targets", targets=targets)

        # OPTIMIZATION: Batch send messages concurrently to all recipients
        target_list = [pid for pid in targets if pid != exclude_player_str]
        excluded_count = len(targets) - len(target_list)

        if excluded_count > 0:
            broadcast_stats["excluded_players"] = excluded_count

        if target_list:
            target_mapping = self._build_target_mapping(target_list, room_id, broadcast_stats)

            try:
                delivery_results = await asyncio.gather(
                    *[self.send_personal_message(pid_uuid, event) for _pid_str, pid_uuid in target_mapping],
                    return_exceptions=True,
                )

                self._process_batch_delivery_results(delivery_results, target_mapping, room_id, broadcast_stats)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Batch broadcast errors unpredictable, must handle gracefully
                logger.error(
                    "Error in batch broadcast",
                    room_id=room_id,
                    target_count=len(target_list),
                    error=str(e),
                    exc_info=True,
                )
                await self._fallback_individual_send(target_mapping, event, room_id, broadcast_stats)

        logger.debug("broadcast_to_room: delivery stats for room", room_id=room_id, stats=broadcast_stats)
        return broadcast_stats

    async def broadcast_global(
        self,
        event: dict[str, Any],
        exclude_player: str | None,
        player_websockets: dict[uuid.UUID, list[str]],
    ) -> dict[str, Any]:
        """
        Broadcast a message to all connected players.

        Args:
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast
            player_websockets: Player to WebSocket connection mapping

        Returns:
            dict: Global broadcast delivery statistics
        """
        # Get all players with WebSocket connections
        all_players = set(player_websockets.keys())

        global_stats: dict[str, Any] = {
            "total_players": len(all_players),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        # OPTIMIZATION: Batch send messages concurrently to all recipients
        target_list = [pid for pid in all_players if pid != exclude_player]
        excluded_count = len(all_players) - len(target_list)

        if excluded_count > 0:
            global_stats["excluded_players"] = excluded_count

        if target_list:
            # Send to all targets concurrently using asyncio.gather
            try:
                delivery_results = await asyncio.gather(
                    *[self.send_personal_message(pid, event) for pid in target_list],
                    return_exceptions=True,
                )

                # Process results
                for i, player_id in enumerate(target_list):
                    result = delivery_results[i]
                    if isinstance(result, Exception):
                        logger.error(
                            "Error sending message in batch global broadcast",
                            player_id=player_id,
                            error=str(result),
                        )
                        global_stats["delivery_details"][player_id] = {"success": False, "error": str(result)}
                        global_stats["failed_deliveries"] += 1
                    else:
                        delivery_status: dict[str, Any] = result  # type: ignore[assignment]  # Reason: After isinstance(result, Exception) check, result must be dict[str, Any] from send_personal_message, but mypy cannot verify this type narrowing
                        global_stats["delivery_details"][player_id] = delivery_status
                        if delivery_status["success"]:
                            global_stats["successful_deliveries"] += 1
                        else:
                            global_stats["failed_deliveries"] += 1
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Batch global broadcast errors unpredictable, must handle gracefully
                logger.error(
                    "Error in batch global broadcast",
                    target_count=len(target_list),
                    error=str(e),
                    exc_info=True,
                )
                # Fallback: send individually if batch fails
                for player_id in target_list:
                    try:
                        delivery_status = await self.send_personal_message(player_id, event)
                        global_stats["delivery_details"][player_id] = delivery_status
                        if delivery_status["success"]:
                            global_stats["successful_deliveries"] += 1
                        else:
                            global_stats["failed_deliveries"] += 1
                    except Exception as individual_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Individual message sending errors unpredictable, must continue processing
                        logger.error(
                            "Error sending individual message in fallback",
                            player_id=player_id,
                            error=str(individual_error),
                        )
                        global_stats["failed_deliveries"] += 1

        logger.debug("broadcast_global: delivery stats", stats=global_stats)
        return global_stats

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, Any]) -> dict[str, Any]:
        """Broadcast a room-specific event."""
        try:
            from ..envelope import build_event

            event = build_event(event_type, data)
            result = await self.broadcast_to_room(room_id, event, None, None)
            return result
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room event broadcasting errors unpredictable, must return error response
            logger.error("Error broadcasting room event", error=str(e), event_type=event_type, room_id=room_id)
            return {
                "room_id": room_id,
                "total_targets": 0,
                "excluded_players": 0,
                "successful_deliveries": 0,
                "failed_deliveries": 0,
                "delivery_details": {},
                "error": str(e),
            }

    async def broadcast_global_event(self, event_type: str, data: dict[str, Any]) -> dict[str, Any]:
        """Broadcast a global event to all connected players."""
        try:
            from ..envelope import build_event

            event = build_event(event_type, data)
            return await self.broadcast_global(event, None, {})
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Global event broadcasting errors unpredictable, must return error response
            logger.error("Error broadcasting global event", error=str(e), event_type=event_type)
            return {
                "total_players": 0,
                "excluded_players": 0,
                "successful_deliveries": 0,
                "failed_deliveries": 0,
                "delivery_details": {},
                "error": str(e),
            }
