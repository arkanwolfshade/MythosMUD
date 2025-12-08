"""
Room repository for async persistence operations.

This module provides async database operations for room CRUD and caching
using SQLAlchemy ORM with PostgreSQL.
"""

from typing import TYPE_CHECKING

from server.logging.enhanced_logging_config import get_logger

if TYPE_CHECKING:
    from server.models.room import Room

logger = get_logger(__name__)


class RoomRepository:
    """
    Repository for room persistence operations.

    Handles room caching and retrieval. Rooms are typically loaded
    at startup and cached in memory for fast access.
    """

    def __init__(self, room_cache: dict[str, "Room"]):
        """
        Initialize the room repository.

        Args:
            room_cache: Shared room cache dictionary
        """
        self._room_cache = room_cache
        self._logger = get_logger(__name__)

    def get_room_by_id(self, room_id: str) -> "Room | None":
        """
        Get a room by ID from cache.

        Args:
            room_id: Room identifier

        Returns:
            Room | None: Room object or None if not found

        Note: This is synchronous as rooms are cached at startup
        """
        return self._room_cache.get(room_id)

    def list_rooms(self) -> list["Room"]:
        """
        List all cached rooms.

        Returns:
            list[Room]: List of all rooms

        Note: This is synchronous as rooms are cached at startup
        """
        return list(self._room_cache.values())

    def save_room(self, room: "Room") -> None:
        """
        Save a room to the cache.

        Args:
            room: Room object to save

        Note: Rooms are currently read-only and stored in JSON files.
        This method updates the in-memory cache only.
        """
        self._room_cache[room.id] = room
        self._logger.info("Room updated in cache", room_id=room.id)

    def save_rooms(self, rooms: list["Room"]) -> None:
        """
        Save multiple rooms to the cache.

        Args:
            rooms: List of room objects to save

        Note: Rooms are currently read-only and stored in JSON files.
        This method updates the in-memory cache only.
        """
        for room in rooms:
            self._room_cache[room.id] = room
        self._logger.info("Rooms updated in cache", room_count=len(rooms))
