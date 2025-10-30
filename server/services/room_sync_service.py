"""
Room synchronization service for MythosMUD.

This module provides enhanced room synchronization capabilities including
event processing order, state validation, and room data freshness validation.

As noted in the Pnakotic Manuscripts, proper synchronization of our
dimensional coordinates is essential for maintaining the integrity
of our eldritch architecture.
"""

import asyncio
import time
from collections import defaultdict
from typing import Any

from ..events.event_types import BaseEvent
from ..logging.enhanced_logging_config import get_logger

# Type aliases for better readability
type RoomData = dict[str, Any]
type EventSequence = dict[str, int]

logger = get_logger(__name__)


class RoomSyncService:
    """
    Enhanced room synchronization service.

    Provides improved event processing order, state validation,
    and room data freshness validation to prevent race conditions
    and ensure consistent room state across all clients.
    """

    def __init__(self) -> None:
        """Initialize the room synchronization service."""
        self._event_sequence_counter: int = 0
        self._room_data_cache: dict[str, RoomData] = {}
        self._room_update_locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)
        self._processing_queue: asyncio.Queue[BaseEvent] = asyncio.Queue()
        self._freshness_threshold_seconds: int = 5  # Default 5 seconds

        # Event processing order tracking
        self._last_processed_events: EventSequence = {}

        logger.info("RoomSyncService initialized with enhanced synchronization")

    def _process_event_with_ordering(self, event: BaseEvent) -> BaseEvent:
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

    def _merge_room_data(self, old_data: dict[str, Any], new_data: dict[str, Any]) -> dict[str, Any]:
        """
        Merge room data with proper conflict resolution.

        Args:
            old_data: Existing room data
            new_data: New room data to merge

        Returns:
            Dict[str, Any]: Merged room data with newer data taking precedence
        """
        try:
            merged_data = old_data.copy()

            # Merge with newer data taking precedence
            for key, value in new_data.items():
                if key not in merged_data or self._is_newer_data(merged_data, new_data, key):
                    merged_data[key] = value

            # Ensure timestamp is always the latest
            if "timestamp" in new_data:
                merged_data["timestamp"] = new_data["timestamp"]

            logger.debug(
                "Merged room data",
                room_id=merged_data.get("id"),
                old_timestamp=old_data.get("timestamp"),
                new_timestamp=new_data.get("timestamp"),
                merged_timestamp=merged_data.get("timestamp"),
            )

            return merged_data

        except Exception as e:
            logger.error("Error merging room data", error=str(e), exc_info=True)
            return new_data  # Return new data as fallback

    def _is_newer_data(self, old_data: dict[str, Any], new_data: dict[str, Any], key: str) -> bool:
        """
        Check if new data is newer than old data for a specific key.

        Args:
            old_data: Existing data
            new_data: New data
            key: The key to compare

        Returns:
            bool: True if new data is newer
        """
        try:
            # If new data has a timestamp and old data doesn't, new is newer
            if "timestamp" in new_data and "timestamp" not in old_data:
                return True

            # If both have timestamps, compare them
            if "timestamp" in new_data and "timestamp" in old_data:
                return new_data["timestamp"] > old_data["timestamp"]

            # For non-timestamp fields, assume new data is newer
            return True

        except Exception as e:
            logger.warning("Error comparing data freshness", key=key, error=str(e))
            return True  # Default to accepting new data

    def _is_room_data_fresh(
        self, room_data: dict[str, Any], current_time: float | None = None, threshold_seconds: int | None = None
    ) -> bool:
        """
        Check if room data is fresh enough to use.

        Args:
            room_data: Room data to check
            current_time: Current timestamp (defaults to time.time())
            threshold_seconds: Freshness threshold in seconds (defaults to configured threshold)

        Returns:
            bool: True if data is fresh enough
        """
        try:
            if current_time is None:
                current_time = time.time()

            if threshold_seconds is None:
                threshold_seconds = self._freshness_threshold_seconds

            # If no timestamp, consider stale
            if "timestamp" not in room_data:
                logger.warning("Room data has no timestamp, considering stale")
                return False

            # Check if data is within freshness threshold
            data_age = current_time - room_data["timestamp"]
            is_fresh = data_age < threshold_seconds

            logger.debug(
                "Checked room data freshness",
                room_id=room_data.get("id"),
                data_age=data_age,
                threshold=threshold_seconds,
                is_fresh=is_fresh,
            )

            return is_fresh

        except Exception as e:
            logger.error("Error checking room data freshness", error=str(e), exc_info=True)
            return False  # Default to stale on error

    def _process_room_update_with_validation(self, room_data: dict[str, Any]) -> dict[str, Any]:
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
            validation_result = self._validate_room_data(room_data)
            if not validation_result["is_valid"]:
                logger.warning(
                    "Room data validation failed", room_id=room_data.get("id"), errors=validation_result["errors"]
                )
                # Apply fixes if possible
                room_data = self._apply_room_data_fixes(room_data, validation_result["errors"])

            # Check freshness
            if not self._is_room_data_fresh(room_data):
                logger.warning(
                    "Stale room data detected", room_id=room_data.get("id"), timestamp=room_data.get("timestamp")
                )
                # Handle stale data
                self._handle_stale_room_data(room_data)

            # Update cache with proper merging
            room_id = room_data.get("id")
            if room_id:
                if room_id in self._room_data_cache:
                    room_data = self._merge_room_data(self._room_data_cache[room_id], room_data)
                self._room_data_cache[room_id] = room_data

            logger.debug("Room update processed and validated", room_id=room_id)
            return room_data

        except Exception as e:
            logger.error("Error processing room update", error=str(e), exc_info=True)
            return room_data  # Return original data on error

    def _validate_room_data(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Validate room data structure and content.

        Args:
            room_data: Room data to validate

        Returns:
            Dict[str, Any]: Validation result with is_valid flag and errors list
        """
        errors = []

        try:
            # Check required fields
            required_fields = ["id", "name", "description"]
            for field in required_fields:
                if field not in room_data or room_data[field] is None:
                    errors.append(f"Missing required field: {field}")

            # Check field types
            if "id" in room_data and not isinstance(room_data["id"], str):
                errors.append("Field 'id' must be a string")

            if "name" in room_data and not isinstance(room_data["name"], str):
                errors.append("Field 'name' must be a string")

            if "description" in room_data and not isinstance(room_data["description"], str):
                errors.append("Field 'description' must be a string")

            if "timestamp" in room_data and not isinstance(room_data["timestamp"], int | float):
                errors.append("Field 'timestamp' must be a number")

            # Check occupant count consistency
            if "occupants" in room_data and "occupant_count" in room_data:
                occupants = room_data["occupants"]
                occupant_count = room_data["occupant_count"]

                if isinstance(occupants, list) and occupant_count != len(occupants):
                    errors.append(f"Occupant count mismatch: expected {len(occupants)}, got {occupant_count}")

            # Validate room ID format
            if "id" in room_data and not self._is_valid_room_id(room_data["id"]):
                errors.append(f"Invalid room ID format: {room_data['id']}")

            is_valid = len(errors) == 0

            logger.debug(
                "Room data validation completed",
                room_id=room_data.get("id"),
                is_valid=is_valid,
                error_count=len(errors),
            )

            return {"is_valid": is_valid, "errors": errors, "room_id": room_data.get("id")}

        except Exception as e:
            logger.error("Error validating room data", error=str(e), exc_info=True)
            return {"is_valid": False, "errors": [f"Validation error: {str(e)}"], "room_id": room_data.get("id")}

    def _is_valid_room_id(self, room_id: str) -> bool:
        """
        Validate room ID format.

        Args:
            room_id: Room ID to validate

        Returns:
            bool: True if room ID format is valid
        """
        try:
            # Basic validation - should not be empty and should contain valid characters
            if not room_id or not isinstance(room_id, str):
                return False

            # Room IDs should contain alphanumeric characters, underscores, and hyphens
            import re

            pattern = r"^[a-zA-Z0-9_-]+$"
            return bool(re.match(pattern, room_id))

        except (AttributeError, TypeError, re.error) as e:
            logger.warning(
                "Error validating room ID format", room_id=room_id, error=str(e), error_type=type(e).__name__
            )
            return False

    def _apply_room_data_fixes(self, room_data: dict[str, Any], errors: list[str]) -> dict[str, Any]:
        """
        Apply automatic fixes to room data when possible.

        Args:
            room_data: Room data to fix
            errors: List of validation errors

        Returns:
            Dict[str, Any]: Fixed room data
        """
        try:
            fixed_data = room_data.copy()

            # Fix missing required fields with defaults
            if "Missing required field: name" in errors:
                fixed_data["name"] = f"Room {fixed_data.get('id', 'unknown')}"

            if "Missing required field: description" in errors:
                fixed_data["description"] = "No description available"

            # Fix occupant count mismatch
            if any("Occupant count mismatch" in error for error in errors):
                if "occupants" in fixed_data and isinstance(fixed_data["occupants"], list):
                    fixed_data["occupant_count"] = len(fixed_data["occupants"])

            # Add timestamp if missing
            if "timestamp" not in fixed_data:
                fixed_data["timestamp"] = time.time()

            logger.info(
                "Applied room data fixes",
                room_id=fixed_data.get("id"),
                fixes_applied=len([e for e in errors if e.startswith("Missing") or "mismatch" in e]),
            )

            return fixed_data

        except Exception as e:
            logger.error("Error applying room data fixes", error=str(e), exc_info=True)
            return room_data

    def _handle_stale_room_data(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Handle stale room data by requesting fresh data.

        Args:
            room_data: Stale room data

        Returns:
            Dict[str, Any]: Result of stale data handling
        """
        try:
            room_id = room_data.get("id")
            logger.warning(
                "Handling stale room data",
                room_id=room_id,
                timestamp=room_data.get("timestamp"),
                age_seconds=time.time() - room_data.get("timestamp", 0),
            )

            # In a real implementation, this would trigger a request for fresh data
            # For now, we'll log the issue and return the handling result

            result = {
                "action_taken": "request_fresh_data",
                "reason": "stale_data_detected",
                "room_id": room_id,
                "timestamp": time.time(),
            }

            # TODO: Implement actual fresh data request mechanism
            logger.info("Stale data handling completed", room_id=room_id, result=result)

            return result

        except Exception as e:
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

            # Use room-specific lock to prevent race conditions
            async with self._room_update_locks[to_room]:
                # Validate transition data
                if not all([player_id, from_room, to_room]):
                    return {"success": False, "errors": ["Missing required transition data"], "player_id": player_id}

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

        except Exception as e:
            logger.error("Error processing room transition", error=str(e), exc_info=True)
            return {"success": False, "errors": [str(e)], "player_id": transition_data.get("player_id")}

    def _validate_room_consistency(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Validate room data consistency.

        Args:
            room_data: Room data to validate for consistency

        Returns:
            Dict[str, Any]: Consistency validation result
        """
        try:
            inconsistencies = []

            # Check occupant count consistency
            if "occupants" in room_data and "occupant_count" in room_data:
                occupants = room_data["occupants"]
                occupant_count = room_data["occupant_count"]

                if isinstance(occupants, list) and occupant_count != len(occupants):
                    inconsistencies.append(f"Occupant count mismatch: expected {len(occupants)}, got {occupant_count}")

            # Check for duplicate occupants
            if "occupants" in room_data and isinstance(room_data["occupants"], list):
                occupants = room_data["occupants"]
                if len(occupants) != len(set(occupants)):
                    inconsistencies.append("Duplicate occupants found in room")

            # Check for empty room with occupants
            if room_data.get("name", "").strip() == "" and room_data.get("occupant_count", 0) > 0:
                inconsistencies.append("Room has occupants but no name")

            is_consistent = len(inconsistencies) == 0

            logger.debug(
                "Room consistency validation completed",
                room_id=room_data.get("id"),
                is_consistent=is_consistent,
                inconsistency_count=len(inconsistencies),
            )

            return {"is_consistent": is_consistent, "inconsistencies": inconsistencies, "room_id": room_data.get("id")}

        except Exception as e:
            logger.error("Error validating room consistency", error=str(e), exc_info=True)
            return {
                "is_consistent": False,
                "inconsistencies": [f"Consistency check error: {str(e)}"],
                "room_id": room_data.get("id"),
            }

    def get_room_data_cache_stats(self) -> dict[str, Any]:
        """
        Get statistics about the room data cache.

        Returns:
            Dict[str, Any]: Cache statistics
        """
        try:
            total_rooms = len(self._room_data_cache)
            total_events_processed = self._event_sequence_counter
            active_locks = len(self._room_update_locks)

            # Calculate cache freshness
            current_time = time.time()
            fresh_rooms = 0
            stale_rooms = 0

            for room_data in self._room_data_cache.values():
                if self._is_room_data_fresh(room_data, current_time):
                    fresh_rooms += 1
                else:
                    stale_rooms += 1

            return {
                "total_rooms_cached": total_rooms,
                "fresh_rooms": fresh_rooms,
                "stale_rooms": stale_rooms,
                "total_events_processed": total_events_processed,
                "active_update_locks": active_locks,
                "freshness_threshold_seconds": self._freshness_threshold_seconds,
            }

        except Exception as e:
            logger.error("Error getting cache stats", error=str(e), exc_info=True)
            return {"error": str(e)}

    def clear_cache(self, room_id: str | None = None):
        """
        Clear room data cache.

        Args:
            room_id: Specific room ID to clear, or None to clear all
        """
        try:
            if room_id:
                if room_id in self._room_data_cache:
                    del self._room_data_cache[room_id]
                logger.info("Cleared cache for room", room_id=room_id)
            else:
                self._room_data_cache.clear()
                logger.info("Cleared all room data cache")

        except Exception as e:
            logger.error("Error clearing cache", error=str(e), exc_info=True)


# Global room sync service instance
_room_sync_service: RoomSyncService | None = None


def get_room_sync_service() -> RoomSyncService:
    """Get the global room sync service instance."""
    global _room_sync_service
    if _room_sync_service is None:
        _room_sync_service = RoomSyncService()
    return _room_sync_service
