"""
EventPublisher service for MythosMUD real-time events.

This module provides a service class for publishing player_entered, player_left,
and game_tick events to NATS subjects for real-time game event distribution.
"""

# pylint: disable=too-many-locals,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Event publishing locals; Protocol stubs (PEP 544)

from __future__ import annotations

import uuid
from collections.abc import Mapping
from datetime import datetime
from typing import Protocol, cast

from ..services.nats_subject_manager import NATSSubjectManager
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("realtime.event_publisher")

JsonMap = dict[str, object]


class _Named(Protocol):
    name: object


class _EventPersistence(Protocol):
    async def get_player_by_id(self, player_id: uuid.UUID) -> _Named | None: ...

    def get_room_by_id(self, room_id: str) -> _Named | None: ...


class _NatsPublish(Protocol):
    def is_connected(self) -> bool: ...

    async def publish(self, subject: str, data: Mapping[str, object]) -> object: ...


class EventPublisher:
    """
    Service for publishing real-time game events to NATS subjects.

    This service handles publishing player movement events (player_entered, player_left)
    and game tick events to appropriate NATS subjects for real-time distribution
    to connected clients.
    """

    nats_service: _NatsPublish | None
    subject_manager: NATSSubjectManager | None
    sequence_number: int
    _async_persistence: _EventPersistence | None

    def __init__(
        self,
        nats_service: _NatsPublish | None,
        subject_manager: NATSSubjectManager | None = None,
        initial_sequence: int = 0,
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
        self._async_persistence = None

        logger.info("EventPublisher initialized", subject_manager_enabled=subject_manager is not None)

    async def _resolve_player_and_room_names(self, player_id: str, room_id: str) -> tuple[str, str]:
        player_name = f"Player_{player_id}"
        room_name = f"Room_{room_id}"
        async_persistence = self._get_async_persistence()
        if not async_persistence:
            return player_name, room_name
        try:
            try:
                player = await async_persistence.get_player_by_id(uuid.UUID(player_id))
                if player is not None:
                    name = str(player.name)
                    if name:
                        player_name = name
            except (ValueError, TypeError, AttributeError) as e:
                logger.debug("Failed to get player name", player_id=player_id, error=str(e))
            room = async_persistence.get_room_by_id(room_id)
            if room is not None:
                name = str(room.name)
                if name:
                    room_name = name
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: optional metadata
            logger.debug("Failed to get player/room names", player_id=player_id, room_id=room_id, error=str(e))
        return player_name, room_name

    def _player_event_subject(self, event_key: str, room_id: str, legacy_prefix: str) -> str:
        if self.subject_manager:
            return self.subject_manager.build_subject(event_key, room_id=room_id)
        logger.warning(
            "Using legacy subject construction - subject_manager not configured",
            event_type=event_key,
            room_id=room_id,
        )
        return f"{legacy_prefix}.{room_id}"

    async def _publish_event(self, subject: str, event_message: JsonMap) -> bool:
        nats_service = self.nats_service
        if nats_service is None or not nats_service.is_connected():
            return False
        published = await nats_service.publish(subject, event_message)
        return published is not False

    async def publish_player_entered_event(
        self,
        player_id: str,
        room_id: str,
        timestamp: str | None = None,
        additional_metadata: JsonMap | None = None,
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
            if self.nats_service is None or not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish player_entered event")
                return False

            player_name, room_name = await self._resolve_player_and_room_names(player_id, room_id)
            event_data: JsonMap = {
                "player_id": player_id,
                "room_id": room_id,
                "player_name": player_name,
                "room_name": room_name,
            }
            event_message = self._create_event_message(
                event_type="player_entered",
                data=event_data,
                timestamp=timestamp,
                additional_metadata=additional_metadata,
            )
            subject = self._player_event_subject("event_player_entered", room_id, "events.player_entered")

            if await self._publish_event(subject, event_message):
                logger.info(
                    "Player entered event published successfully",
                    player_id=player_id,
                    room_id=room_id,
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                )
                return True

            logger.error(
                "Failed to publish player entered event", player_id=player_id, room_id=room_id, subject=subject
            )
            return False

        except (OSError, ValueError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event publishing errors unpredictable, must handle all error types
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
        additional_metadata: JsonMap | None = None,
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
            if self.nats_service is None or not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish player_left event")
                return False

            player_name, room_name = await self._resolve_player_and_room_names(player_id, room_id)
            event_data: JsonMap = {
                "player_id": player_id,
                "room_id": room_id,
                "player_name": player_name,
                "room_name": room_name,
            }
            event_message = self._create_event_message(
                event_type="player_left", data=event_data, timestamp=timestamp, additional_metadata=additional_metadata
            )
            subject = self._player_event_subject("event_player_left", room_id, "events.player_left")

            if await self._publish_event(subject, event_message):
                logger.info(
                    "Player left event published successfully",
                    player_id=player_id,
                    room_id=room_id,
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                )
                return True

            logger.error("Failed to publish player left event", player_id=player_id, room_id=room_id, subject=subject)
            return False

        except (OSError, ValueError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event publishing errors unpredictable, must handle all error types
            logger.error(
                "Error publishing player left event",
                error=str(e),
                error_type=type(e).__name__,
                player_id=player_id,
                room_id=room_id,
            )
            return False

    async def publish_game_tick_event(
        self, timestamp: str | None = None, additional_metadata: JsonMap | None = None
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
            if self.nats_service is None or not self.nats_service.is_connected():
                logger.warning("NATS service not connected, cannot publish game_tick event")
                return False

            current_time = datetime.now()
            tick_number: object = (
                additional_metadata.get("tick_number")
                if additional_metadata and "tick_number" in additional_metadata
                else self.sequence_number + 1
            )
            event_data: JsonMap = {
                "tick_number": tick_number,
                "server_time": current_time.isoformat(),
            }

            event_message = self._create_event_message(
                event_type="game_tick", data=event_data, timestamp=timestamp, additional_metadata=additional_metadata
            )

            if self.subject_manager:
                subject = self.subject_manager.build_subject("event_game_tick")
            else:
                subject = "events.game_tick"
                logger.warning(
                    "Using legacy subject construction - subject_manager not configured", event_type="game_tick"
                )

            if await self._publish_event(subject, event_message):
                logger.info(
                    "Game tick event published successfully",
                    subject=subject,
                    sequence_number=event_message["sequence_number"],
                    tick_number=event_data["tick_number"],
                )
                return True

            logger.error("Failed to publish game tick event")
            return False

        except (OSError, ValueError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Event publishing errors unpredictable, must handle all error types
            logger.error("Error publishing game tick event", error=str(e), error_type=type(e).__name__)
            return False

    def _create_event_message(
        self,
        event_type: str,
        data: JsonMap,
        timestamp: str | None = None,
        additional_metadata: JsonMap | None = None,
    ) -> JsonMap:
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
        if timestamp is None:
            timestamp = datetime.now().isoformat()

        sequence_number = self.get_next_sequence_number()

        metadata: JsonMap = {
            "event_type": event_type,
            "timestamp": timestamp,
            "sequence_number": sequence_number,
        }

        if additional_metadata:
            metadata.update(additional_metadata)

        return {
            "event_type": event_type,
            "timestamp": timestamp,
            "sequence_number": sequence_number,
            "data": data,
            "metadata": metadata,
        }

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

    def _get_async_persistence(self) -> _EventPersistence | None:
        """Get async_persistence from ApplicationContainer (lazy-loaded)."""
        if self._async_persistence is None:
            try:
                from ..container import ApplicationContainer  # noqa: I001,PLC0415  # Reason: lazy load avoids container import cycle

                container = ApplicationContainer.get_instance()
                persistence = getattr(container, "async_persistence", None) if container else None
                if persistence is not None:
                    self._async_persistence = cast(_EventPersistence, cast(object, persistence))
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Container access errors unpredictable, must handle gracefully
                logger.warning("Failed to get async_persistence from ApplicationContainer", error=str(e))
        return self._async_persistence


# AI Agent: Global singleton removed - use ApplicationContainer.event_publisher instead
# Migration complete: All code now uses dependency injection via container
