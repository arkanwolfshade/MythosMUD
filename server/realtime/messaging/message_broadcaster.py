"""
Message broadcasting for connection management.

This module provides room and global message broadcasting with concurrent
delivery optimization.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Message broadcasting is now a focused, independently testable component.
"""

from __future__ import annotations

import asyncio
import uuid
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, SupportsInt, cast

from structlog.stdlib import BoundLogger

from ...structured_logging.enhanced_logging_config import get_logger
from ..envelope import build_event

if TYPE_CHECKING:
    from ..room_subscription_manager import RoomSubscriptionManager

logger: BoundLogger = get_logger(__name__)

# WebSocket event payloads and per-recipient delivery status from ConnectionManager.
SendPersonalMessage = Callable[[uuid.UUID, dict[str, object]], Awaitable[dict[str, object]]]


def _narrow_gather_delivery_dict(result: object) -> dict[str, object] | None:
    """Narrow asyncio.gather results when return_exceptions=True."""
    if isinstance(result, dict):
        return cast(dict[str, object], result)
    return None


def _stats_counter(stats: dict[str, object], key: str) -> int:
    """Read an integer delivery counter from stats dicts typed as dict[str, object]."""
    raw = stats[key]
    if isinstance(raw, int):
        return raw
    return int(cast(SupportsInt, raw))


def _global_targets_and_stats(
    player_websockets: dict[uuid.UUID, list[str]],
    exclude_player: str | None,
) -> tuple[list[uuid.UUID], dict[str, object]]:
    """Compute recipient list and initial stats for broadcast_global."""
    all_players = set(player_websockets.keys())
    target_list = [pid for pid in all_players if pid != exclude_player]
    excluded_count = len(all_players) - len(target_list)
    global_stats: dict[str, object] = {
        "total_players": len(all_players),
        "excluded_players": excluded_count,
        "successful_deliveries": 0,
        "failed_deliveries": 0,
        "delivery_details": {},
    }
    return target_list, global_stats


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

    room_manager: RoomSubscriptionManager
    send_personal_message: SendPersonalMessage

    def __init__(
        self,
        room_manager: RoomSubscriptionManager,
        send_personal_message_callback: SendPersonalMessage,
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
        self, target_list: list[str], room_id: str, broadcast_stats: dict[str, object]
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
                delivery_details = cast(dict[str, object], broadcast_stats["delivery_details"])
                delivery_details[pid_str] = {
                    "success": False,
                    "error": "Invalid player ID format",
                }
                broadcast_stats["failed_deliveries"] = _stats_counter(broadcast_stats, "failed_deliveries") + 1
        return target_mapping

    def _process_batch_delivery_results(
        self,
        delivery_results: list[object],
        target_mapping: list[tuple[str, uuid.UUID]],
        room_id: str,
        broadcast_stats: dict[str, object],
    ) -> None:
        """
        Process results from batch message delivery.

        Args:
            delivery_results: Results from asyncio.gather
            target_mapping: List of (player_id_str, player_id_uuid) tuples
            room_id: Room ID for logging
            broadcast_stats: Stats dict to update
        """
        delivery_details = cast(dict[str, object], broadcast_stats["delivery_details"])
        for i, (pid_str, _pid_uuid) in enumerate(target_mapping):
            if i >= len(delivery_results):
                continue
            result = delivery_results[i]
            if isinstance(result, Exception):
                logger.error(
                    "Error sending message in batch broadcast",
                    player_id=pid_str,
                    room_id=room_id,
                    error_message=str(result),
                )
                delivery_details[pid_str] = {"success": False, "error": str(result)}
                broadcast_stats["failed_deliveries"] = _stats_counter(broadcast_stats, "failed_deliveries") + 1
            else:
                delivery_status = _narrow_gather_delivery_dict(result)
                if delivery_status is None:
                    logger.warning(
                        "Unexpected batch broadcast result type",
                        player_id=pid_str,
                        room_id=room_id,
                        result_type=type(result).__name__,
                    )
                    delivery_details[pid_str] = {"success": False, "error": "unexpected_result_type"}
                    broadcast_stats["failed_deliveries"] = _stats_counter(broadcast_stats, "failed_deliveries") + 1
                    continue
                delivery_details[pid_str] = delivery_status
                if delivery_status.get("success") is True:
                    broadcast_stats["successful_deliveries"] = (
                        _stats_counter(broadcast_stats, "successful_deliveries") + 1
                    )
                else:
                    broadcast_stats["failed_deliveries"] = _stats_counter(broadcast_stats, "failed_deliveries") + 1

    async def _fallback_individual_send(
        self,
        target_mapping: list[tuple[str, uuid.UUID]],
        event: dict[str, object],
        _room_id: str,
        broadcast_stats: dict[str, object],
    ) -> None:
        """
        Fallback to individual message sending if batch fails.

        Args:
            target_mapping: List of (player_id_str, player_id_uuid) tuples
            event: Event to send
            room_id: Room ID for logging
            broadcast_stats: Stats dict to update
        """
        delivery_details = cast(dict[str, object], broadcast_stats["delivery_details"])
        for pid_str, pid_uuid in target_mapping:
            try:
                delivery_status = await self.send_personal_message(pid_uuid, event)
                delivery_details[pid_str] = delivery_status
                if delivery_status.get("success") is True:
                    broadcast_stats["successful_deliveries"] = (
                        _stats_counter(broadcast_stats, "successful_deliveries") + 1
                    )
                else:
                    broadcast_stats["failed_deliveries"] = _stats_counter(broadcast_stats, "failed_deliveries") + 1
            except Exception as individual_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Individual message sending errors unpredictable, must continue processing
                logger.error(
                    "Error sending individual message in fallback",
                    player_id=pid_str,
                    error_message=str(individual_error),
                )
                broadcast_stats["failed_deliveries"] = _stats_counter(broadcast_stats, "failed_deliveries") + 1

    def _prepare_room_targets(self, targets: set[str], exclude_player_str: str | None) -> tuple[list[str], int]:
        """Dedupe subscribers and count exclusions."""
        target_list = list(dict.fromkeys(pid for pid in targets if pid != exclude_player_str))
        excluded_count = len(targets) - len(target_list)
        return target_list, excluded_count

    async def _deliver_room_broadcast(
        self,
        room_id: str,
        target_list: list[str],
        event: dict[str, object],
        broadcast_stats: dict[str, object],
    ) -> None:
        """Run batch gather (or fallback) for a room broadcast."""
        target_mapping = self._build_target_mapping(target_list, room_id, broadcast_stats)
        try:
            delivery_results = cast(
                list[object],
                await asyncio.gather(
                    *[self.send_personal_message(pid_uuid, event) for _pid_str, pid_uuid in target_mapping],
                    return_exceptions=True,
                ),
            )
            self._process_batch_delivery_results(delivery_results, target_mapping, room_id, broadcast_stats)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Batch broadcast errors unpredictable, must handle gracefully
            logger.error(
                "Error in batch broadcast",
                room_id=room_id,
                target_count=len(target_list),
                error_message=str(e),
                exc_info=True,
            )
            await self._fallback_individual_send(target_mapping, event, room_id, broadcast_stats)

    async def broadcast_to_room(
        self,
        room_id: str,
        event: dict[str, object],
        exclude_player: uuid.UUID | str | None = None,
        _player_websockets: dict[uuid.UUID, list[str]] | None = None,  # pylint: disable=unused-argument  # Reason: Parameter reserved for future websocket filtering
    ) -> dict[str, object]:
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

        broadcast_stats: dict[str, object] = {
            "room_id": room_id,
            "total_targets": len(targets),
            "excluded_players": 0,
            "successful_deliveries": 0,
            "failed_deliveries": 0,
            "delivery_details": {},
        }

        exclude_player_str = str(exclude_player) if exclude_player else None

        logger.debug("broadcast_to_room", room_id=room_id, exclude_player=exclude_player_str)
        logger.debug("broadcast_to_room targets", targets=targets)

        target_list, excluded_count = self._prepare_room_targets(targets, exclude_player_str)

        if excluded_count > 0:
            broadcast_stats["excluded_players"] = excluded_count

        if target_list:
            await self._deliver_room_broadcast(room_id, target_list, event, broadcast_stats)

        logger.debug("broadcast_to_room: delivery stats for room", room_id=room_id, stats=broadcast_stats)
        return broadcast_stats

    def _process_global_batch_results(
        self,
        delivery_results: list[object],
        target_list: list[uuid.UUID],
        global_stats: dict[str, object],
    ) -> None:
        """Merge asyncio.gather outcomes into global broadcast stats."""
        delivery_details = cast(dict[object, object], global_stats["delivery_details"])
        for i, player_id in enumerate(target_list):
            if i >= len(delivery_results):
                continue
            result = delivery_results[i]
            if isinstance(result, Exception):
                logger.error(
                    "Error sending message in batch global broadcast",
                    player_id=player_id,
                    error_message=str(result),
                )
                delivery_details[player_id] = {"success": False, "error": str(result)}
                global_stats["failed_deliveries"] = _stats_counter(global_stats, "failed_deliveries") + 1
            else:
                delivery_status = _narrow_gather_delivery_dict(result)
                if delivery_status is None:
                    logger.warning(
                        "Unexpected global batch broadcast result type",
                        player_id=player_id,
                        result_type=type(result).__name__,
                    )
                    delivery_details[player_id] = {"success": False, "error": "unexpected_result_type"}
                    global_stats["failed_deliveries"] = _stats_counter(global_stats, "failed_deliveries") + 1
                    continue
                delivery_details[player_id] = delivery_status
                if delivery_status.get("success") is True:
                    global_stats["successful_deliveries"] = _stats_counter(global_stats, "successful_deliveries") + 1
                else:
                    global_stats["failed_deliveries"] = _stats_counter(global_stats, "failed_deliveries") + 1

    async def _fallback_global_individual(
        self,
        target_list: list[uuid.UUID],
        event: dict[str, object],
        global_stats: dict[str, object],
    ) -> None:
        """Send global broadcast recipients one-by-one after batch failure."""
        delivery_details = cast(dict[object, object], global_stats["delivery_details"])
        for player_id in target_list:
            try:
                delivery_status = await self.send_personal_message(player_id, event)
                delivery_details[player_id] = delivery_status
                if delivery_status.get("success") is True:
                    global_stats["successful_deliveries"] = _stats_counter(global_stats, "successful_deliveries") + 1
                else:
                    global_stats["failed_deliveries"] = _stats_counter(global_stats, "failed_deliveries") + 1
            except Exception as individual_error:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Individual message sending errors unpredictable, must continue processing
                logger.error(
                    "Error sending individual message in fallback",
                    player_id=player_id,
                    error_message=str(individual_error),
                )
                global_stats["failed_deliveries"] = _stats_counter(global_stats, "failed_deliveries") + 1

    async def broadcast_global(
        self,
        event: dict[str, object],
        exclude_player: str | None,
        player_websockets: dict[uuid.UUID, list[str]],
    ) -> dict[str, object]:
        """
        Broadcast a message to all connected players.

        Args:
            event: The event data to send
            exclude_player: Player ID to exclude from broadcast
            player_websockets: Player to WebSocket connection mapping

        Returns:
            dict: Global broadcast delivery statistics
        """
        target_list, global_stats = _global_targets_and_stats(player_websockets, exclude_player)

        if target_list:
            try:
                delivery_results = cast(
                    list[object],
                    await asyncio.gather(
                        *[self.send_personal_message(pid, event) for pid in target_list],
                        return_exceptions=True,
                    ),
                )
                self._process_global_batch_results(delivery_results, target_list, global_stats)
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Batch global broadcast errors unpredictable, must handle gracefully
                logger.error(
                    "Error in batch global broadcast",
                    target_count=len(target_list),
                    error_message=str(e),
                    exc_info=True,
                )
                await self._fallback_global_individual(target_list, event, global_stats)

        logger.debug("broadcast_global: delivery stats", stats=global_stats)
        return global_stats

    async def broadcast_room_event(self, event_type: str, room_id: str, data: dict[str, object]) -> dict[str, object]:
        """Broadcast a room-specific event."""
        try:
            event = build_event(event_type, data)
            result = await self.broadcast_to_room(room_id, event, None, None)
            return result
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room event broadcasting errors unpredictable, must return error response
            logger.error(
                "Error broadcasting room event",
                error_message=str(e),
                event_type=event_type,
                room_id=room_id,
            )
            return {
                "room_id": room_id,
                "total_targets": 0,
                "excluded_players": 0,
                "successful_deliveries": 0,
                "failed_deliveries": 0,
                "delivery_details": {},
                "error": str(e),
            }

    async def broadcast_global_event(self, event_type: str, data: dict[str, object]) -> dict[str, object]:
        """Broadcast a global event to all connected players."""
        try:
            event = build_event(event_type, data)
            return await self.broadcast_global(event, None, {})
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Global event broadcasting errors unpredictable, must return error response
            logger.error("Error broadcasting global event", error_message=str(e), event_type=event_type)
            return {
                "total_players": 0,
                "excluded_players": 0,
                "successful_deliveries": 0,
                "failed_deliveries": 0,
                "delivery_details": {},
                "error": str(e),
            }
