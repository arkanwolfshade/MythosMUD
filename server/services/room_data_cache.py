"""
Room data cache and freshness management for MythosMUD.

This module provides caching and freshness validation for room data,
ensuring that stale data is detected and refreshed appropriately.
"""

import time
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomDataCache:
    """Manages room data caching and freshness validation."""

    def __init__(self, freshness_threshold_seconds: int = 5) -> None:
        """
        Initialize the room data cache.

        Args:
            freshness_threshold_seconds: Threshold in seconds for considering data fresh
        """
        self._room_data_cache: dict[str, dict[str, Any]] = {}
        self._freshness_threshold_seconds: int = freshness_threshold_seconds

    def is_room_data_fresh(
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

        except (AttributeError, TypeError) as e:
            logger.error("Error checking room data freshness", error=str(e), exc_info=True)
            return False  # Default to stale on error

    def get_cache(self, room_id: str) -> dict[str, Any] | None:
        """
        Get room data from cache.

        Args:
            room_id: Room ID to retrieve

        Returns:
            Dict[str, Any] | None: Cached room data or None if not found
        """
        return self._room_data_cache.get(room_id)

    def set_cache(self, room_id: str, room_data: dict[str, Any]) -> None:
        """
        Store room data in cache.

        Args:
            room_id: Room ID to store
            room_data: Room data to cache
        """
        self._room_data_cache[room_id] = room_data

    def clear_cache(self, room_id: str | None = None) -> None:
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

        except (AttributeError, TypeError) as e:
            logger.error("Error clearing cache", error=str(e), exc_info=True)

    def get_cache_stats(self, is_room_data_fresh_func: Any) -> dict[str, Any]:
        """
        Get statistics about the room data cache.

        Args:
            is_room_data_fresh_func: Function to check if room data is fresh

        Returns:
            Dict[str, Any]: Cache statistics
        """
        try:
            total_rooms = len(self._room_data_cache)
            fresh_rooms = 0
            stale_rooms = 0

            # Calculate cache freshness
            current_time = time.time()

            for room_data in self._room_data_cache.values():
                if is_room_data_fresh_func(room_data, current_time):
                    fresh_rooms += 1
                else:
                    stale_rooms += 1

            return {
                "total_rooms_cached": total_rooms,
                "fresh_rooms": fresh_rooms,
                "stale_rooms": stale_rooms,
                "freshness_threshold_seconds": self._freshness_threshold_seconds,
            }

        except (AttributeError, TypeError) as e:
            logger.error("Error getting cache stats", error=str(e), exc_info=True)
            return {"error": str(e)}

    def merge_room_data(self, old_data: dict[str, Any], new_data: dict[str, Any]) -> dict[str, Any]:
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

        except (AttributeError, TypeError) as e:
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

        except (AttributeError, TypeError) as e:
            logger.warning("Error comparing data freshness", key=key, error=str(e))
            return True  # Default to accepting new data
