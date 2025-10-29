"""
Room service for MythosMUD server.

This module handles all room-related business logic including
room information retrieval and room state management.
"""

from typing import Any

from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class RoomService:
    """Service class for room-related operations."""

    def __init__(self, persistence):
        """Initialize the room service with a persistence layer."""
        self.persistence = persistence
        logger.info("RoomService initialized")

    async def get_room(self, room_id: str) -> dict[str, Any] | None:
        """
        Get room information by room ID.

        Args:
            room_id: The room's ID

        Returns:
            Dict[str, Any]: The room data, or None if not found
        """
        logger.debug("Getting room by ID", room_id=room_id)

        room = await self.persistence.async_get_room(room_id)
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

    async def get_adjacent_rooms(self, room_id: str) -> list[dict[str, Any]]:
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
        source_room = await self.get_room(room_id)
        if not source_room:
            logger.debug("Source room not found", room_id=room_id)
            return []

        adjacent_rooms = []
        exits = source_room.get("exits", {})

        # Check each exit direction
        for direction, target_room_id in exits.items():
            if target_room_id:  # Skip null/None exits
                target_room = await self.get_room(target_room_id)
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

    async def get_local_chat_scope(self, room_id: str) -> list[str]:
        """
        Get the scope of rooms for local chat (current room + adjacent rooms).

        Args:
            room_id: The room's ID

        Returns:
            list[str]: List of room IDs in the local chat scope
        """
        logger.debug("Getting local chat scope", room_id=room_id)

        # Get the source room first
        source_room = await self.get_room(room_id)
        if not source_room:
            logger.debug("Source room not found for local chat scope", room_id=room_id)
            return []

        # Start with the current room
        local_scope = [room_id]

        # Add adjacent rooms
        adjacent_rooms = await self.get_adjacent_rooms(room_id)
        for adjacent in adjacent_rooms:
            local_scope.append(adjacent["room_id"])

        logger.debug(
            "Local chat scope determined", room_id=room_id, scope_count=len(local_scope), scope_rooms=local_scope
        )
        return local_scope

    async def validate_room_exists(self, room_id: str) -> bool:
        """
        Validate that a room exists.

        Args:
            room_id: The room's ID

        Returns:
            bool: True if the room exists, False otherwise
        """
        logger.debug("Validating room exists", room_id=room_id)

        room = await self.persistence.async_get_room(room_id)
        exists = room is not None

        logger.debug("Room existence validation", room_id=room_id, exists=exists)
        return exists

    async def validate_exit_exists(self, from_room_id: str, to_room_id: str) -> bool:
        """
        Validate that there's a valid exit from one room to another.

        Args:
            from_room_id: The ID of the room the player is leaving
            to_room_id: The ID of the room the player is entering

        Returns:
            bool: True if there's a valid exit, False otherwise
        """
        logger.debug("Validating exit exists", from_room_id=from_room_id, to_room_id=to_room_id)

        from_room = await self.get_room(from_room_id)
        if not from_room:
            logger.debug("From room not found for exit validation", from_room_id=from_room_id)
            return False

        exits = from_room.get("exits", {})
        if not exits:
            logger.debug("No exits found in room", room_id=from_room_id)
            return False

        # Check each exit direction
        for direction, target_id in exits.items():
            if target_id == to_room_id:
                logger.debug("Valid exit found", from_room_id=from_room_id, direction=direction, to_room_id=to_room_id)
                return True

        logger.debug(
            "No valid exit found", from_room_id=from_room_id, to_room_id=to_room_id, available_exits=list(exits.keys())
        )
        return False

    async def get_room_occupants(self, room_id: str) -> list[str]:
        """
        Get all players currently in a room.

        Args:
            room_id: The ID of the room to check

        Returns:
            list[str]: List of player IDs in the room
        """
        logger.debug("Getting room occupants", room_id=room_id)

        room = await self.persistence.async_get_room(room_id)
        if not room:
            logger.debug("Room not found for occupant lookup", room_id=room_id)
            return []

        # If it's a Room object, use its method
        if hasattr(room, "get_players"):
            occupants = room.get_players()
        else:
            # If it's a dictionary, check for occupants field
            occupants = room.get("occupants", [])

        logger.debug("Room occupants retrieved", room_id=room_id, occupant_count=len(occupants))
        return occupants

    async def validate_player_in_room(self, player_id: str, room_id: str) -> bool:
        """
        Validate that a player is in the specified room.

        Args:
            player_id: The ID of the player to validate
            room_id: The ID of the room to check

        Returns:
            bool: True if the player is in the specified room, False otherwise
        """
        logger.debug("Validating player in room", player_id=player_id, room_id=room_id)

        room = await self.persistence.async_get_room(room_id)
        if not room:
            logger.debug("Room not found for player validation", room_id=room_id)
            return False

        # If it's a Room object, use its method
        if hasattr(room, "has_player"):
            is_in_room = room.has_player(player_id)
        else:
            # If it's a dictionary, check occupants field
            occupants = room.get("occupants", [])
            is_in_room = player_id in occupants

        logger.debug("Player room validation", player_id=player_id, room_id=room_id, is_in_room=is_in_room)
        return is_in_room

    async def get_room_exits(self, room_id: str) -> dict[str, str]:
        """
        Get all exits from a room.

        Args:
            room_id: The ID of the room

        Returns:
            dict[str, str]: Dictionary of direction -> target_room_id mappings
        """
        logger.debug("Getting room exits", room_id=room_id)

        room = await self.get_room(room_id)
        if not room:
            logger.debug("Room not found for exit lookup", room_id=room_id)
            return {}

        exits = room.get("exits", {})
        logger.debug("Room exits retrieved", room_id=room_id, exit_count=len(exits))
        return exits

    async def get_room_info(self, room_id: str) -> dict[str, Any] | None:
        """
        Get comprehensive room information including occupants and exits.

        Args:
            room_id: The ID of the room

        Returns:
            dict[str, Any]: Comprehensive room information, or None if not found
        """
        logger.debug("Getting comprehensive room info", room_id=room_id)

        room = await self.get_room(room_id)
        if not room:
            logger.debug("Room not found for comprehensive info", room_id=room_id)
            return None

        # Get additional information
        occupants = await self.get_room_occupants(room_id)
        exits = await self.get_room_exits(room_id)
        adjacent_rooms = await self.get_adjacent_rooms(room_id)

        room_info = {
            **room,
            "occupants": occupants,
            "exits": exits,
            "adjacent_rooms": adjacent_rooms,
            "occupant_count": len(occupants),
            "exit_count": len(exits),
        }

        logger.debug(
            "Comprehensive room info retrieved", room_id=room_id, occupant_count=len(occupants), exit_count=len(exits)
        )
        return room_info

    def search_rooms_by_name(self, search_term: str) -> list[dict[str, Any]]:
        """
        Search for rooms by name (case-insensitive partial match).

        Args:
            search_term: The search term to match against room names

        Returns:
            list[dict[str, Any]]: List of matching rooms
        """
        logger.debug("Searching rooms by name", search_term=search_term)

        if not search_term or len(search_term.strip()) < 2:
            logger.debug("Search term too short", search_term=search_term)
            return []

        # This would need to be implemented in the persistence layer
        # For now, we'll return an empty list as this functionality isn't available
        logger.debug("Room search by name not implemented", search_term=search_term)
        return []

    def get_rooms_in_zone(self, zone_id: str) -> list[dict[str, Any]]:
        """
        Get all rooms in a specific zone.

        Args:
            zone_id: The zone ID

        Returns:
            list[dict[str, Any]]: List of rooms in the zone
        """
        logger.debug("Getting rooms in zone", zone_id=zone_id)

        # This would need to be implemented in the persistence layer
        # For now, we'll return an empty list as this functionality isn't available
        logger.debug("Zone room listing not implemented", zone_id=zone_id)
        return []
