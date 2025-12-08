"""
EventPublisher service for MythosMUD real-time events.

This module provides a service class for publishing player_entered, player_left,
and game_tick events to NATS subjects for real-time game event distribution.
"""

import uuid
from datetime import datetime
from typing import Any

from ..logging.enhanced_logging_config import get_logger
from ..services.nats_subject_manager import NATSSubjectManager

logger = get_logger("realtime.event_publisher")


class EventPublisher:
    """
    Service for publishing real-time game events to NATS subjects.

    This service handles publishing player movement events (player_entered, player_left)
    and game tick events to appropriate NATS subjects for real-time distribution
    to connected clients.
    """

    def __init__(
        self, nats_service: Any, subject_manager: NATSSubjectManager | None = None, initial_sequence: int = 0
    ) -> None:
        """
        Initialize EventPublisher service.

        Args:
            nats_service: NATS service instance for publishing messages
            subject_manager: Subject manager for standardized NATS subjects (optional for backward compatibility)
            initial_sequence: Initial sequence number for event ordering

        AI: subject_manager is optional for backward compatibility but recommended for standardized patterns.
        AI: Falls back to legacy subject construction if subject_manager is None.
        """
        self.nats_service = nats_service
        self.subject_manager = subject_manager
        self.sequence_number = initial_sequence
        self._async_persistence: Any | None = None  # Lazy-loaded from ApplicationContainer

        logger.info("EventPublisher initialized", subject_manager_enabled=subject_manager is not None)

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
            # Check if NATS service is available and connected
            if self.nats_service is None or not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish player_entered event")
                return False

            # Get actual player and room names from persistence
            player_name = f"Player_{player_id}"  # Fallback
            room_name = f"Room_{room_id}"  # Fallback

            async_persistence = self._get_async_persistence()
            if async_persistence:
                try:
                    # Get player name
                    try:
                        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
                        player = await async_persistence.get_player_by_id(player_id_uuid)
                        if player and hasattr(player, "name") and player.name:
                            player_name = player.name
                    except (ValueError, TypeError, AttributeError) as e:
                        logger.debug("Failed to get player name", player_id=player_id, error=str(e))

                    # Get room name (sync cache method)
                    room = async_persistence.get_room_by_id(room_id)
                    if room and hasattr(room, "name") and room.name:
                        room_name = room.name
                except Exception as e:
                    logger.debug("Failed to get player/room names", player_id=player_id, room_id=room_id, error=str(e))

            # Generate event data
            event_data = {
                "player_id": player_id,
                "room_id": room_id,
                "player_name": player_name,
                "room_name": room_name,
            }

            # Create the complete event message
            event_message = self._create_event_message(
                event_type="player_entered",
                data=event_data,
                timestamp=timestamp,
                additional_metadata=additional_metadata,
            )

            # Build subject using standardized pattern
            if self.subject_manager:
                subject = self.subject_manager.build_subject("event_player_entered", room_id=room_id)
            else:
                # Legacy fallback for backward compatibility
                subject = f"events.player_entered.{room_id}"
                logger.warning(
                    "Using legacy subject construction - subject_manager not configured",
                    event_type="player_entered",
                    room_id=room_id,
                )

            success = await self.nats_service.publish(subject, event_message)

            if success:
                logger.info(
                    "Player entered event published successfully",
                    player_id=player_id,
                    room_id=room_id,
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                )
                return True
            else:
                logger.error(
                    "Failed to publish player entered event", player_id=player_id, room_id=room_id, subject=subject
                )
                return False

        except (OSError, ValueError, TypeError, Exception) as e:
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
            # Check if NATS service is available and connected
            if self.nats_service is None or not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish player_left event")
                return False

            # Get actual player and room names from persistence
            player_name = f"Player_{player_id}"  # Fallback
            room_name = f"Room_{room_id}"  # Fallback

            async_persistence = self._get_async_persistence()
            if async_persistence:
                try:
                    # Get player name
                    try:
                        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
                        player = await async_persistence.get_player_by_id(player_id_uuid)
                        if player and hasattr(player, "name") and player.name:
                            player_name = player.name
                    except (ValueError, TypeError, AttributeError) as e:
                        logger.debug("Failed to get player name", player_id=player_id, error=str(e))

                    # Get room name (sync cache method)
                    room = async_persistence.get_room_by_id(room_id)
                    if room and hasattr(room, "name") and room.name:
                        room_name = room.name
                except Exception as e:
                    logger.debug("Failed to get player/room names", player_id=player_id, room_id=room_id, error=str(e))

            # Generate event data
            event_data = {
                "player_id": player_id,
                "room_id": room_id,
                "player_name": player_name,
                "room_name": room_name,
            }

            # Create the complete event message
            event_message = self._create_event_message(
                event_type="player_left", data=event_data, timestamp=timestamp, additional_metadata=additional_metadata
            )

            # Build subject using standardized pattern
            if self.subject_manager:
                subject = self.subject_manager.build_subject("event_player_left", room_id=room_id)
            else:
                # Legacy fallback for backward compatibility
                subject = f"events.player_left.{room_id}"
                logger.warning(
                    "Using legacy subject construction - subject_manager not configured",
                    event_type="player_left",
                    room_id=room_id,
                )

            success = await self.nats_service.publish(subject, event_message)

            if success:
                logger.info(
                    "Player left event published successfully",
                    player_id=player_id,
                    room_id=room_id,
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                )
                return True
            else:
                logger.error(
                    "Failed to publish player left event", player_id=player_id, room_id=room_id, subject=subject
                )
                return False

        except (OSError, ValueError, TypeError, Exception) as e:
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
            # Check if NATS service is available and connected
            if self.nats_service is None or not self.nats_service.is_connected():
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

            # Build subject using standardized pattern
            if self.subject_manager:
                subject = self.subject_manager.build_subject("event_game_tick")
            else:
                # Legacy fallback for backward compatibility
                subject = "events.game_tick"
                logger.warning(
                    "Using legacy subject construction - subject_manager not configured", event_type="game_tick"
                )

            success = await self.nats_service.publish(subject, event_message)

            if success:
                logger.info(
                    "Game tick event published successfully",
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                    tick_number=event_data["tick_number"],
                )
                return True
            else:
                logger.error("Failed to publish game tick event")
                return False

        except (OSError, ValueError, TypeError, Exception) as e:
            logger.error("Error publishing game tick event", error=str(e), error_type=type(e).__name__)
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

    def _get_async_persistence(self) -> Any | None:
        """Get async_persistence from ApplicationContainer (lazy-loaded)."""
        if self._async_persistence is None:
            try:
                from ..container import ApplicationContainer

                container = ApplicationContainer.get_instance()
                if container and container.async_persistence:
                    self._async_persistence = container.async_persistence
            except Exception as e:
                logger.warning("Failed to get async_persistence from ApplicationContainer", error=str(e))
        return self._async_persistence


# AI Agent: Global singleton removed - use ApplicationContainer.event_publisher instead
# Migration complete: All code now uses dependency injection via container
