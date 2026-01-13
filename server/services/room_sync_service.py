"""
Room synchronization service for MythosMUD.

This module provides enhanced room synchronization capabilities including
event processing order, state validation, and room data freshness validation.

As noted in the Pnakotic Manuscripts, proper synchronization of our
dimensional coordinates is essential for maintaining the integrity
of our eldritch architecture.
"""

# pylint: disable=too-many-instance-attributes  # Reason: Room sync service requires many state tracking and cache attributes

import asyncio
import time
from collections import defaultdict
from typing import Any, TypeAlias, TypeVar

from anyio import Lock

from ..events.event_types import BaseEvent
from ..structured_logging.enhanced_logging_config import get_logger
from .room_data_cache import RoomDataCache
from .room_data_fixer import RoomDataFixer
from .room_data_validator import RoomDataValidator

# TypeVar for generic event processing
T = TypeVar("T", bound=BaseEvent)

# Type aliases for better readability
# Using TypeAlias instead of 'type' keyword for Pylint compatibility (Pylint 3.3.6 doesn't support Python 3.12+ 'type' keyword)
RoomData: TypeAlias = dict[str, Any]  # noqa: UP040  # Reason: Using TypeAlias instead of Python 3.12+ 'type' keyword for Pylint compatibility, dict syntax is clearer for type annotations
EventSequence: TypeAlias = dict[str, int]  # noqa: UP040  # Reason: Using TypeAlias instead of Python 3.12+ 'type' keyword for Pylint compatibility, dict syntax is clearer for type annotations

logger = get_logger(__name__)


class RoomSyncService:  # pylint: disable=too-many-instance-attributes  # Reason: Room sync service requires many state tracking and cache attributes
    """
    Enhanced room synchronization service.

    Provides improved event processing order, state validation,
    and room data freshness validation to prevent race conditions
    and ensure consistent room state across all clients.
    """

    def __init__(self, room_service: Any | None = None) -> None:
        """
        Initialize the room synchronization service.

        Args:
            room_service: Optional RoomService instance for fetching fresh room data
        """
        self._event_sequence_counter: int = 0
        self._room_update_locks: dict[str, Lock] = defaultdict(Lock)
        self._processing_queue: asyncio.Queue[BaseEvent] = asyncio.Queue()
        self._freshness_threshold_seconds: int = 5  # Default 5 seconds
        self._room_service: Any | None = room_service

        # Event processing order tracking
        self._last_processed_events: EventSequence = {}

        # Initialize helper components
        self._room_data_cache = RoomDataCache(self._freshness_threshold_seconds)
        self._validator = RoomDataValidator()
        self._fixer = RoomDataFixer()

        logger.info("RoomSyncService initialized with enhanced synchronization")

    def set_room_service(self, room_service: Any) -> None:
        """
        Set the room service for fetching fresh room data.

        Args:
            room_service: RoomService instance for fetching fresh room data
        """
        self._room_service = room_service
        logger.debug("Room service set for RoomSyncService")

    def process_event_with_ordering(self, event: T) -> T:
        """
        Process events with proper ordering to prevent race conditions.

        Args:
            event: The event to process

        Returns:
            BaseEvent: The processed event with ordering information
        """
        try:
            # Generate sequence number for ordering
            self._event_sequence_counter += 1
            event.sequence_number = self._event_sequence_counter

            # Track last processed event for this room/player combination
            event_key = (
                f"{event.room_id}_{event.player_id}"
                if hasattr(event, "room_id") and hasattr(event, "player_id")
                else str(event.__class__.__name__)
            )
            self._last_processed_events[event_key] = self._event_sequence_counter

            logger.debug(
                "Processed event with ordering",
                event_type=event.__class__.__name__,
                sequence_number=self._event_sequence_counter,
                event_key=event_key,
                timestamp=event.timestamp,
            )

            return event

        except Exception as e:
            logger.error("Error processing event with ordering", error=str(e), exc_info=True)
            raise

    async def _process_room_update_with_validation(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Process room update with comprehensive validation.

        Args:
            room_data: Room data to process and validate

        Returns:
            Dict[str, Any]: Processed and validated room data
        """
        try:
            logger.info("Processing room update with validation", room_id=room_data.get("id"))

            # Validate room data structure
            validation_result = self._validator.validate_room_data(room_data)
            if not validation_result["is_valid"]:
                logger.warning(
                    "Room data validation failed", room_id=room_data.get("id"), errors=validation_result["errors"]
                )
                # Apply fixes if possible
                room_data = self._fixer.apply_room_data_fixes(room_data, validation_result["errors"])

            # Check freshness
            if not self._room_data_cache.is_room_data_fresh(room_data):
                logger.warning(
                    "Stale room data detected", room_id=room_data.get("id"), timestamp=room_data.get("timestamp")
                )
                # Handle stale data (async)
                stale_handling_result = await self._handle_stale_room_data(room_data)
                # If fresh data was fetched, use it instead
                if stale_handling_result.get("fresh_data_fetched") and stale_handling_result.get("fresh_data"):
                    room_data = stale_handling_result["fresh_data"]
                    logger.debug("Using fresh room data after stale detection", room_id=room_data.get("id"))

            # Update cache with proper merging
            room_id = room_data.get("id")
            if room_id:
                cached_data = self._room_data_cache.get_cache(room_id)
                if cached_data:
                    room_data = self._room_data_cache.merge_room_data(cached_data, room_data)
                self._room_data_cache.set_cache(room_id, room_data)

            logger.debug("Room update processed and validated", room_id=room_id)
            return room_data

        except (AttributeError, TypeError) as e:
            logger.error("Error processing room update", error=str(e), exc_info=True)
            return room_data  # Return original data on error

    def _invalidate_stale_cache(self, room_id: str) -> bool:
        """
        Invalidate stale room cache entry.

        Args:
            room_id: Room ID to invalidate

        Returns:
            bool: True if cache was invalidated successfully
        """
        if not (self._room_service and self._room_service.room_cache):
            return False

        try:
            self._room_service.room_cache.invalidate_room(room_id)
            logger.debug("Invalidated stale room cache entry", room_id=room_id)
            return True
        except (AttributeError, TypeError) as cache_error:
            logger.warning(
                "Failed to invalidate room cache",
                room_id=room_id,
                error=str(cache_error),
            )
            return False

    async def _fetch_fresh_room_data(self, room_id: str) -> dict[str, Any] | None:
        """
        Fetch fresh room data from room service.

        Args:
            room_id: Room ID to fetch

        Returns:
            Dict[str, Any] | None: Fresh room data or None if not available
        """
        if not self._room_service:
            logger.debug(
                "Room service not available, skipping fresh data fetch",
                room_id=room_id,
            )
            return None

        try:
            fresh_room_data = await self._room_service.get_room(room_id)
            if fresh_room_data:
                # Update timestamp to current time
                fresh_room_data["timestamp"] = time.time()

                # Update local cache with fresh data
                if room_id:
                    self._room_data_cache.set_cache(room_id, fresh_room_data)

                logger.info(
                    "Fetched fresh room data",
                    room_id=room_id,
                    room_name=fresh_room_data.get("name", "Unknown"),
                )
                return fresh_room_data
            logger.warning("Fresh room data not found", room_id=room_id)
            return None
        except (AttributeError, TypeError) as fetch_error:
            logger.error(
                "Error fetching fresh room data",
                room_id=room_id,
                error=str(fetch_error),
                exc_info=True,
            )
            raise

    async def _handle_stale_room_data(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Handle stale room data by requesting fresh data.

        Args:
            room_data: Stale room data

        Returns:
            Dict[str, Any]: Result of stale data handling
        """
        try:
            room_id = room_data.get("id")
            if not isinstance(room_id, str):
                logger.error(
                    "Invalid room_id type in stale room data",
                    room_id=room_id,
                    room_id_type=type(room_id).__name__,
                )
                return {
                    "action_taken": "error",
                    "reason": "invalid_room_id_type",
                    "timestamp": time.time(),
                }

            logger.warning(
                "Handling stale room data",
                room_id=room_id,
                timestamp=room_data.get("timestamp"),
                age_seconds=time.time() - room_data.get("timestamp", 0),
            )

            result = {
                "action_taken": "request_fresh_data",
                "reason": "stale_data_detected",
                "room_id": room_id,
                "timestamp": time.time(),
            }

            # Invalidate cache entry
            result["cache_invalidated"] = self._invalidate_stale_cache(room_id)

            # Request fresh data
            try:
                fresh_data = await self._fetch_fresh_room_data(room_id)
                if fresh_data:
                    result["fresh_data_fetched"] = True
                    result["fresh_data"] = fresh_data
                else:
                    result["fresh_data_fetched"] = False
                    if not self._room_service:
                        result["reason"] = "room_service_not_available"
            except (AttributeError, TypeError) as fetch_error:
                result["fresh_data_fetched"] = False
                result["fetch_error"] = str(fetch_error)

            logger.info("Stale data handling completed", room_id=room_id, result=result)
            return result

        except (AttributeError, TypeError) as e:
            logger.error("Error handling stale room data", error=str(e), exc_info=True)
            return {"action_taken": "error", "reason": str(e)}

    async def _process_room_transition(self, transition_data: dict[str, Any]) -> dict[str, Any]:
        """
        Process room transition with proper ordering and validation.

        Args:
            transition_data: Room transition data

        Returns:
            Dict[str, Any]: Processing result
        """
        try:
            player_id = transition_data.get("player_id")
            from_room = transition_data.get("from_room")
            to_room = transition_data.get("to_room")

            logger.info("Processing room transition", player_id=player_id, from_room=from_room, to_room=to_room)

            # Validate transition data
            if not all([player_id, from_room, to_room]):
                return {"success": False, "errors": ["Missing required transition data"], "player_id": player_id}

            # Type guard for mypy
            assert isinstance(to_room, str), "to_room must be str after validation"

            # Use room-specific lock to prevent race conditions
            async with self._room_update_locks[to_room]:
                # Process the transition
                # In a real implementation, this would update room state
                # and broadcast appropriate events

                result = {
                    "success": True,
                    "player_id": player_id,
                    "from_room": from_room,
                    "to_room": to_room,
                    "timestamp": time.time(),
                }

                logger.debug("Room transition processed successfully", result=result)
                return result

        except (AttributeError, TypeError) as e:
            logger.error("Error processing room transition", error=str(e), exc_info=True)
            # Safely get player_id, or default to None if transition_data is None
            player_id_for_log = transition_data.get("player_id") if isinstance(transition_data, dict) else None
            return {"success": False, "errors": [str(e)], "player_id": player_id_for_log}

    def get_room_data_cache_stats(self) -> dict[str, Any]:
        """
        Get statistics about the room data cache.

        Returns:
            Dict[str, Any]: Cache statistics
        """
        try:
            cache_stats = self._room_data_cache.get_cache_stats(self._room_data_cache.is_room_data_fresh)
            cache_stats["total_events_processed"] = self._event_sequence_counter
            cache_stats["active_update_locks"] = len(self._room_update_locks)
            return cache_stats

        except (AttributeError, TypeError) as e:
            logger.error("Error getting cache stats", error=str(e), exc_info=True)
            return {"error": str(e)}

    def clear_cache(self, room_id: str | None = None) -> None:
        """
        Clear room data cache.

        Args:
            room_id: Specific room ID to clear, or None to clear all
        """
        self._room_data_cache.clear_cache(room_id)


# Global room sync service instance
room_sync_service = RoomSyncService()


def get_room_sync_service() -> RoomSyncService:
    """
    Get the global room sync service instance.

    Returns:
        RoomSyncService: The room sync service instance
    """
    return room_sync_service
