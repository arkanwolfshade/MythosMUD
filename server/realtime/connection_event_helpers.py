"""
Event subscription helpers for connection manager.

This module provides helper functions for event subscription operations.
"""

from typing import Any

from ..exceptions import DatabaseError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


async def subscribe_to_room_events_impl(manager: Any) -> None:
    """Subscribe to room movement events for occupant broadcasting."""
    event_bus = manager._get_event_bus()  # pylint: disable=protected-access
    if not event_bus:
        logger.warning("No event bus available for room event subscription")
        return

    try:
        from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom

        event_bus.subscribe(PlayerEnteredRoom, manager._handle_player_entered_room)  # pylint: disable=protected-access
        event_bus.subscribe(PlayerLeftRoom, manager._handle_player_left_room)  # pylint: disable=protected-access
        logger.info("Successfully subscribed to room movement events")
    except (DatabaseError, AttributeError) as e:
        logger.error("Error subscribing to room events", error=str(e), exc_info=True)


async def unsubscribe_from_room_events_impl(manager: Any) -> None:
    """Unsubscribe from room movement events."""
    event_bus = manager._get_event_bus()  # pylint: disable=protected-access
    if not event_bus:
        return

    try:
        from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom

        event_bus.unsubscribe(PlayerEnteredRoom, manager._handle_player_entered_room)  # pylint: disable=protected-access
        event_bus.unsubscribe(PlayerLeftRoom, manager._handle_player_left_room)  # pylint: disable=protected-access
        logger.info("Successfully unsubscribed from room movement events")
    except (DatabaseError, AttributeError) as e:
        logger.error("Error unsubscribing from room events", error=str(e), exc_info=True)
