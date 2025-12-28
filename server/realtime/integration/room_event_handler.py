"""
Room event handling for connection management.

This module provides integration with the EventBus for room movement events,
enabling real-time occupant updates when players enter or leave rooms.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Room event handling is now a focused, independently testable component.
"""

import uuid
from collections.abc import Callable
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any

from ...structured_logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from ..room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)


class RoomEventHandler:
    """
    Handles room movement events and broadcasts occupant updates.

    This class provides:
    - EventBus subscription management
    - PlayerEnteredRoom event handling
    - PlayerLeftRoom event handling
    - NATS event publishing
    - Room occupant broadcasting

    AI Agent: Single Responsibility - Room event integration only.
    """

    def __init__(
        self,
        room_manager: "RoomSubscriptionManager",
        get_event_bus: Callable[[], Any],
        get_event_publisher: Callable[[], Any],
        broadcast_to_room_callback: Callable[
            [str, dict[str, Any], uuid.UUID | str | None], "Awaitable[dict[str, Any]]"
        ],
        get_online_players: Callable[[], dict[uuid.UUID, dict[str, Any]]],
    ) -> None:
        """
        Initialize the room event handler.

        Args:
            room_manager: RoomSubscriptionManager instance
            get_event_bus: Callback to get EventBus instance
            get_event_publisher: Callback to get event publisher instance
            broadcast_to_room_callback: Callback to broadcast to room
            get_online_players: Callback to get online players dictionary
        """
        self.room_manager = room_manager
        self.get_event_bus = get_event_bus
        self.get_event_publisher = get_event_publisher
        self.broadcast_to_room = broadcast_to_room_callback
        self.get_online_players = get_online_players

    async def subscribe_to_events(self) -> None:
        """Subscribe to room movement events for occupant broadcasting."""
        event_bus = self.get_event_bus()
        if not event_bus:
            logger.warning("No event bus available for room event subscription")
            return

        try:
            from ...events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            event_bus.subscribe(PlayerEnteredRoom, self.handle_player_entered_room)
            event_bus.subscribe(PlayerLeftRoom, self.handle_player_left_room)
            logger.info("Successfully subscribed to room movement events")
        except Exception as e:
            logger.error("Error subscribing to room events", error=str(e), exc_info=True)

    async def unsubscribe_from_events(self) -> None:
        """Unsubscribe from room movement events."""
        event_bus = self.get_event_bus()
        if not event_bus:
            return

        try:
            from ...events.event_types import PlayerEnteredRoom, PlayerLeftRoom

            event_bus.unsubscribe(PlayerEnteredRoom, self.handle_player_entered_room)
            event_bus.unsubscribe(PlayerLeftRoom, self.handle_player_left_room)
            logger.info("Successfully unsubscribed from room movement events")
        except Exception as e:
            logger.error("Error unsubscribing from room events", error=str(e), exc_info=True)

    async def handle_player_entered_room(self, event_data: dict[str, Any]) -> None:
        """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
        try:
            room_id = event_data.get("room_id")
            player_id = event_data.get("player_id")

            if not room_id:
                logger.warning("PlayerEnteredRoom event missing room_id")
                return

            # Publish NATS event if event_publisher is available
            event_publisher = self.get_event_publisher()
            if event_publisher and player_id:
                try:
                    timestamp = datetime.now(UTC).isoformat()
                    await event_publisher.publish_player_entered_event(
                        player_id=player_id, room_id=room_id, timestamp=timestamp
                    )
                except Exception as e:
                    logger.error("Failed to publish player_entered NATS event", error=str(e))

            # Get current room occupants
            # CRITICAL: Convert UUID keys to strings for room_manager compatibility
            online_players = self.get_online_players()
            online_players_str = {str(k): v for k, v in online_players.items()}
            occ_infos = await self.room_manager.get_room_occupants(room_id, online_players_str)
            names: list[str] = []
            for occ in occ_infos:
                name = occ.get("player_name") if isinstance(occ, dict) else None
                # CRITICAL: Validate name is not a UUID before adding
                if name and isinstance(name, str):
                    # Skip if it looks like a UUID (36 chars, 4 dashes, hex)
                    is_uuid = (
                        len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
                    )
                    if not is_uuid:
                        names.append(name)
                    else:
                        logger.warning(
                            "Skipping UUID as player name in room_occupants event",
                            name=name,
                            room_id=room_id,
                        )

            # Build and broadcast room_occupants event
            from ..envelope import build_event

            occ_event = build_event(
                "room_occupants",
                {"occupants": names, "count": len(names)},
                room_id=room_id,
            )

            await self.broadcast_to_room(room_id, occ_event, None)

            logger.debug("Broadcasted room_occupants event for room", room_id=room_id, occupant_count=len(names))

        except Exception as e:
            logger.error("Error handling PlayerEnteredRoom event", error=str(e), exc_info=True)

    async def handle_player_left_room(self, event_data: dict[str, Any]) -> None:
        """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
        try:
            room_id = event_data.get("room_id")
            player_id = event_data.get("player_id")

            if not room_id:
                logger.warning("PlayerLeftRoom event missing room_id")
                return

            # Publish NATS event if event_publisher is available
            event_publisher = self.get_event_publisher()
            if event_publisher and player_id:
                try:
                    timestamp = datetime.now(UTC).isoformat()
                    await event_publisher.publish_player_left_event(
                        player_id=player_id, room_id=room_id, timestamp=timestamp
                    )
                except Exception as e:
                    logger.error("Failed to publish player_left NATS event", error=str(e))

            # Get current room occupants
            # CRITICAL: Convert UUID keys to strings for room_manager compatibility
            online_players = self.get_online_players()
            online_players_str = {str(k): v for k, v in online_players.items()}
            occ_infos = await self.room_manager.get_room_occupants(room_id, online_players_str)
            names: list[str] = []
            for occ in occ_infos:
                name = occ.get("player_name") if isinstance(occ, dict) else None
                # CRITICAL: Validate name is not a UUID before adding
                if name and isinstance(name, str):
                    # Skip if it looks like a UUID (36 chars, 4 dashes, hex)
                    is_uuid = (
                        len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
                    )
                    if not is_uuid:
                        names.append(name)
                    else:
                        logger.warning(
                            "Skipping UUID as player name in room_occupants event",
                            name=name,
                            room_id=room_id,
                        )

            # Build and broadcast room_occupants event
            from ..envelope import build_event

            occ_event = build_event(
                "room_occupants",
                {"occupants": names, "count": len(names)},
                room_id=room_id,
            )
            await self.broadcast_to_room(room_id, occ_event, None)

            logger.debug("Broadcasted room_occupants event for room", room_id=room_id, occupant_count=len(names))

        except Exception as e:
            logger.error("Error handling PlayerLeftRoom event", error=str(e), exc_info=True)
