"""
Room event handling for connection management.

This module provides integration with the EventBus for room movement events,
enabling real-time occupant updates when players enter or leave rooms.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Room event handling is now a focused, independently testable component.
"""

# pylint: disable=too-many-arguments,too-many-positional-arguments,too-many-locals  # Reason: Room event handling requires many parameters and intermediate variables for complex event processing logic

import uuid
from collections.abc import Callable, Sequence
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, cast

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

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments  # Reason: Event handler initialization requires many service dependencies
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

            # Use service_id for tracking and cleanup (Task 2: Event Subscriber Cleanup)
            event_bus.subscribe(PlayerEnteredRoom, self.handle_player_entered_room, service_id="room_event_handler")
            event_bus.subscribe(PlayerLeftRoom, self.handle_player_left_room, service_id="room_event_handler")
            logger.info("Successfully subscribed to room movement events")
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event subscription errors unpredictable, must handle gracefully
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
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event unsubscription errors unpredictable, must handle gracefully
            logger.error("Error unsubscribing from room events", error=str(e), exc_info=True)

    @staticmethod
    def _extract_valid_occupant_names(occ_infos: Sequence[object], room_id: str) -> list[str]:
        """Collect occupant display names, dropping any that are actually raw UUIDs."""
        names: list[str] = []
        for occ in occ_infos:
            name = cast("dict[str, object]", occ).get("player_name") if isinstance(occ, dict) else None
            # CRITICAL: Validate name is not a UUID before adding
            if name and isinstance(name, str):
                # Skip if it looks like a UUID (36 chars, 4 dashes, hex)
                is_uuid = len(name) == 36 and name.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in name)
                if not is_uuid:
                    names.append(name)
                else:
                    logger.warning(
                        "Skipping UUID as player name in room_occupants event",
                        name=name,
                        room_id=room_id,
                    )
        return names

    async def _publish_room_movement_nats_event(
        self, publish_method_name: str, event_label: str, player_id: object, room_id: str
    ) -> None:
        """Best-effort NATS publish for a player entered/left event; never raises."""
        event_publisher = cast(object, self.get_event_publisher())
        if not (event_publisher and player_id):
            return
        try:
            timestamp = datetime.now(UTC).isoformat()
            # Reason: DYNAMIC_DISPATCH - publish_method_name selects which NATS publisher
            # method to call at runtime (entered vs. left); the event_publisher itself is
            # already untyped (get_event_publisher: Callable[[], Any]).
            # Appropriate because: the two possible methods share a call signature but the
            # publisher has no common typed interface to name here without inventing one.
            publish = getattr(event_publisher, publish_method_name)  # pyright: ignore[reportAny]
            await publish(player_id=player_id, room_id=room_id, timestamp=timestamp)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NATS event publishing errors unpredictable, must handle gracefully
            logger.error(f"Failed to publish {event_label} NATS event", error=str(e))

    async def _broadcast_room_occupants_update(
        self,
        # Reason: SERIALIZATION_BOUNDARY - event_data is an EventBus payload dict (mirrors
        # handle_player_entered_room/handle_player_left_room's own event_data: dict[str, Any]).
        # Appropriate because: shape varies by event type; only room_id/player_id are read.
        event_data: dict[str, Any],  # pyright: ignore[reportExplicitAny]
        *,
        event_label: str,
        publish_method_name: str,
    ) -> None:
        """Shared core of handle_player_entered_room/handle_player_left_room (issue #787:
        the two were identical apart from which event name/publisher method they used).
        """
        try:
            room_id_raw = event_data.get("room_id")
            player_id = event_data.get("player_id")

            if not room_id_raw:
                logger.warning(f"{event_label} event missing room_id")
                return
            room_id = cast(str, room_id_raw)

            await self._publish_room_movement_nats_event(publish_method_name, event_label, player_id, room_id)

            # Get current room occupants
            # CRITICAL: Convert UUID keys to strings for room_manager compatibility
            online_players = self.get_online_players()
            online_players_str = {str(k): v for k, v in online_players.items()}
            occ_infos = await self.room_manager.get_room_occupants(room_id, online_players_str)
            names = self._extract_valid_occupant_names(occ_infos, room_id)

            # Build and broadcast room_occupants event
            from ..envelope import build_event

            occ_event = build_event(
                "room_occupants",
                {"occupants": names, "count": len(names)},
                room_id=room_id,
            )
            await self.broadcast_to_room(room_id, occ_event, None)

            logger.debug("Broadcasted room_occupants event for room", room_id=room_id, occupant_count=len(names))

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room movement event handling errors unpredictable, must handle gracefully
            logger.error(f"Error handling {event_label} event", error=str(e), exc_info=True)

    # Reason: SERIALIZATION_BOUNDARY - event_data is an EventBus payload dict; shape varies
    # by event type, and only room_id/player_id are read (see _broadcast_room_occupants_update).
    # Appropriate because: this mirrors the pre-existing dict[str, Any] contract EventBus
    # subscribers use throughout this module; narrowing it here alone would be inconsistent.
    async def handle_player_entered_room(self, event_data: dict[str, Any]) -> None:  # pyright: ignore[reportExplicitAny]
        """Handle PlayerEnteredRoom events by broadcasting updated occupant count."""
        await self._broadcast_room_occupants_update(
            event_data, event_label="PlayerEnteredRoom", publish_method_name="publish_player_entered_event"
        )

    async def handle_player_left_room(self, event_data: dict[str, Any]) -> None:
        """Handle PlayerLeftRoom events by broadcasting updated occupant count."""
        await self._broadcast_room_occupants_update(
            event_data, event_label="PlayerLeftRoom", publish_method_name="publish_player_left_event"
        )
