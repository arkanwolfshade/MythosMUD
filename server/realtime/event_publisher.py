"""
EventPublisher service for MythosMUD real-time events.

This module provides a service class for publishing player_entered, player_left,
and game_tick events to NATS subjects for real-time game event distribution.
"""

from datetime import datetime
from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger("realtime.event_publisher")


class EventPublisher:
    """
    Service for publishing real-time game events to NATS subjects.

    This service handles publishing player movement events (player_entered, player_left)
    and game tick events to appropriate NATS subjects for real-time distribution
    to connected clients.
    """

    def __init__(self, nats_service, initial_sequence: int = 0):
        """
        Initialize EventPublisher service.

        Args:
            nats_service: NATS service instance for publishing messages
            initial_sequence: Initial sequence number for event ordering
        """
        self.nats_service = nats_service
        self.sequence_number = initial_sequence

        logger.info("EventPublisher initialized")

    async def publish_player_entered_event(
        self,
        player_id: str,
        room_id: str,
        timestamp: str | None = None,
        additional_metadata: dict[str, Any] | None = None,
    ) -> bool:
        """
        Publish a player_entered event to NATS.

        Args:
            player_id: ID of the player who entered the room
            room_id: ID of the room the player entered
            timestamp: Optional custom timestamp (defaults to current time)
            additional_metadata: Optional additional metadata to include

        Returns:
            True if published successfully, False otherwise
        """
        try:
            # Check if NATS service is connected
            if not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish player_entered event")
                return False

            # Generate event data
            event_data = {
                "player_id": player_id,
                "room_id": room_id,
                "player_name": f"Player_{player_id}",  # TODO: Get actual player name from persistence
                "room_name": f"Room_{room_id}",  # TODO: Get actual room name from persistence
            }

            # Create the complete event message
            event_message = self._create_event_message(
                event_type="player_entered",
                data=event_data,
                timestamp=timestamp,
                additional_metadata=additional_metadata,
            )

            # Publish to room-specific NATS subject
            subject = f"events.player_entered.{room_id}"
            success = await self.nats_service.publish(subject, event_message)

            if success:
                logger.info(
                    "Player entered event published successfully",
                    player_id=player_id,
                    room_id=room_id,
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                )
            else:
                logger.error(
                    "Failed to publish player entered event", player_id=player_id, room_id=room_id, subject=subject
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing player entered event",
                error=str(e),
                error_type=type(e).__name__,
                player_id=player_id,
                room_id=room_id,
            )
            return False

    async def publish_player_left_event(
        self,
        player_id: str,
        room_id: str,
        timestamp: str | None = None,
        additional_metadata: dict[str, Any] | None = None,
    ) -> bool:
        """
        Publish a player_left event to NATS.

        Args:
            player_id: ID of the player who left the room
            room_id: ID of the room the player left
            timestamp: Optional custom timestamp (defaults to current time)
            additional_metadata: Optional additional metadata to include

        Returns:
            True if published successfully, False otherwise
        """
        try:
            # Check if NATS service is connected
            if not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish player_left event")
                return False

            # Generate event data
            event_data = {
                "player_id": player_id,
                "room_id": room_id,
                "player_name": f"Player_{player_id}",  # TODO: Get actual player name from persistence
                "room_name": f"Room_{room_id}",  # TODO: Get actual room name from persistence
            }

            # Create the complete event message
            event_message = self._create_event_message(
                event_type="player_left", data=event_data, timestamp=timestamp, additional_metadata=additional_metadata
            )

            # Publish to room-specific NATS subject
            subject = f"events.player_left.{room_id}"
            success = await self.nats_service.publish(subject, event_message)

            if success:
                logger.info(
                    "Player left event published successfully",
                    player_id=player_id,
                    room_id=room_id,
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                )
            else:
                logger.error(
                    "Failed to publish player left event", player_id=player_id, room_id=room_id, subject=subject
                )

            return success

        except Exception as e:
            logger.error(
                "Error publishing player left event",
                error=str(e),
                error_type=type(e).__name__,
                player_id=player_id,
                room_id=room_id,
            )
            return False

    async def publish_game_tick_event(
        self, timestamp: str | None = None, additional_metadata: dict[str, Any] | None = None
    ) -> bool:
        """
        Publish a game_tick event to NATS.

        Args:
            timestamp: Optional custom timestamp (defaults to current time)
            additional_metadata: Optional additional metadata to include

        Returns:
            True if published successfully, False otherwise
        """
        try:
            # Check if NATS service is connected
            if not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish game_tick event")
                return False

            # Generate event data
            current_time = datetime.now()
            event_data = {
                "tick_number": self.sequence_number + 1,  # Use next sequence number as tick number
                "server_time": current_time.isoformat(),
            }

            # Create the complete event message
            event_message = self._create_event_message(
                event_type="game_tick", data=event_data, timestamp=timestamp, additional_metadata=additional_metadata
            )

            # Publish to global NATS subject
            subject = "events.game_tick"
            success = await self.nats_service.publish(subject, event_message)

            if success:
                logger.info(
                    "Game tick event published successfully",
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                    tick_number=event_data["tick_number"],
                )
            else:
                logger.error("Failed to publish game tick event")

            return success

        except Exception:
            logger.error("Error publishing game tick event")
            return False

    def _create_event_message(
        self,
        event_type: str,
        data: dict[str, Any],
        timestamp: str | None = None,
        additional_metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Create a standardized event message structure.

        Args:
            event_type: Type of event (player_entered, player_left, game_tick)
            data: Event-specific data
            timestamp: Optional custom timestamp
            additional_metadata: Optional additional metadata

        Returns:
            Standardized event message dictionary
        """
        # Generate timestamp if not provided
        if timestamp is None:
            timestamp = datetime.now().isoformat()

        # Generate sequence number
        sequence_number = self.get_next_sequence_number()

        # Create base metadata
        metadata = {
            "event_type": event_type,
            "timestamp": timestamp,
            "sequence_number": sequence_number,
        }

        # Add additional metadata if provided
        if additional_metadata:
            metadata.update(additional_metadata)

        # Create the complete event message
        event_message = {
            "event_type": event_type,
            "timestamp": timestamp,
            "sequence_number": sequence_number,
            "data": data,
            "metadata": metadata,
        }

        return event_message

    def get_next_sequence_number(self) -> int:
        """
        Get the next sequence number for event ordering.

        Returns:
            Next sequence number
        """
        self.sequence_number += 1
        return self.sequence_number

    def reset_sequence_number(self) -> None:
        """Reset the sequence number to 0."""
        self.sequence_number = 0
        logger.info("EventPublisher sequence number reset")


# Global EventPublisher instance
event_publisher = None


def get_event_publisher(nats_service=None) -> EventPublisher | None:
    """
    Get or create the global EventPublisher instance.

    Args:
        nats_service: NATS service instance (optional, for testing)

    Returns:
        EventPublisher instance or None if nats_service not provided
    """
    global event_publisher
    if event_publisher is None and nats_service is not None:
        event_publisher = EventPublisher(nats_service)
    return event_publisher
