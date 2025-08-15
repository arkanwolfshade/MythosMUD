"""
Room service for MythosMUD server.

This module handles all room-related business logic including
room information retrieval and room state management.
"""

from typing import Any

from ..logging_config import get_logger

logger = get_logger(__name__)


class RoomService:
    """Service class for room-related operations."""

    def __init__(self, persistence):
        """Initialize the room service with a persistence layer."""
        self.persistence = persistence
        logger.info("RoomService initialized")

    def get_room(self, room_id: str) -> dict[str, Any] | None:
        """
        Get room information by room ID.

        Args:
            room_id: The room's ID

        Returns:
            Dict[str, Any]: The room data, or None if not found
        """
        logger.debug("Getting room by ID", room_id=room_id)

        room = self.persistence.get_room(room_id)
        if not room:
            logger.debug("Room not found by ID", room_id=room_id)
            return None

        # Convert Room object to dictionary if it's a Room object
        if hasattr(room, "to_dict"):
            room_dict = room.to_dict()
        else:
            # If it's already a dictionary, use it directly
            room_dict = room

        logger.debug("Room found by ID", room_id=room_id, room_name=room_dict.get("name", "Unknown"))
        return room_dict

    def get_room_by_name(self, room_name: str) -> dict[str, Any] | None:
        """
        Get room information by room name.

        Args:
            room_name: The room's name

        Returns:
            Dict[str, Any]: The room data, or None if not found
        """
        logger.debug("Getting room by name", room_name=room_name)

        # This would need to be implemented in the persistence layer
        # For now, we'll return None as this functionality isn't available
        logger.debug("Room lookup by name not implemented", room_name=room_name)
        return None

    def list_rooms_in_zone(self, zone_id: str) -> list[dict[str, Any]]:
        """
        Get a list of all rooms in a specific zone.

        Args:
            zone_id: The zone ID

        Returns:
            list[Dict[str, Any]]: List of rooms in the zone
        """
        logger.debug("Listing rooms in zone", zone_id=zone_id)

        # This would need to be implemented in the persistence layer
        # For now, we'll return an empty list
        logger.debug("Zone room listing not implemented", zone_id=zone_id)
        return []

    def get_adjacent_rooms(self, room_id: str) -> list[dict[str, Any]]:
        """
        Get a list of rooms adjacent to the specified room.

        Args:
            room_id: The room's ID

        Returns:
            list[Dict[str, Any]]: List of adjacent rooms with direction and room
            data
        """
        logger.debug("Getting adjacent rooms", room_id=room_id)

        # Get the source room
        source_room = self.get_room(room_id)
        if not source_room:
            logger.debug("Source room not found", room_id=room_id)
            return []

        adjacent_rooms = []
        exits = source_room.get("exits", {})

        # Check each exit direction
        for direction, target_room_id in exits.items():
            if target_room_id:  # Skip null/None exits
                target_room = self.get_room(target_room_id)
                if target_room:
                    adjacent_rooms.append({"direction": direction, "room_id": target_room_id, "room_data": target_room})
                    logger.debug(
                        "Found adjacent room",
                        source_room_id=room_id,
                        direction=direction,
                        target_room_id=target_room_id,
                    )
                else:
                    logger.warning(
                        "Adjacent room not found",
                        source_room_id=room_id,
                        direction=direction,
                        target_room_id=target_room_id,
                    )

        logger.debug("Adjacent rooms found", room_id=room_id, adjacent_count=len(adjacent_rooms))
        return adjacent_rooms

    def get_local_chat_scope(self, room_id: str) -> list[str]:
        """
        Get the scope of rooms for local chat (current room + adjacent rooms).

        Args:
            room_id: The room's ID

        Returns:
            list[str]: List of room IDs in the local chat scope
        """
        logger.debug("Getting local chat scope", room_id=room_id)

        # Get the source room first
        source_room = self.get_room(room_id)
        if not source_room:
            logger.debug("Source room not found for local chat scope", room_id=room_id)
            return []

        # Start with the current room
        local_scope = [room_id]

        # Add adjacent rooms
        adjacent_rooms = self.get_adjacent_rooms(room_id)
        for adjacent in adjacent_rooms:
            local_scope.append(adjacent["room_id"])

        logger.debug(
            "Local chat scope determined", room_id=room_id, scope_count=len(local_scope), scope_rooms=local_scope
        )
        return local_scope
