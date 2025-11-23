"""
Room model for MythosMUD.

This module provides the Room class that represents a room in the game world.
Rooms track their current occupants (players, objects, NPCs) and provide
event-driven methods for state changes.

As noted in the Pnakotic Manuscripts, proper room awareness is essential
for maintaining the integrity of our eldritch architecture and ensuring
that dimensional shifts are properly tracked.
"""

import uuid

from ..events import EventBus
from ..events.event_types import (
    NPCEnteredRoom,
    NPCLeftRoom,
    ObjectAddedToRoom,
    ObjectRemovedFromRoom,
    PlayerEnteredRoom,
    PlayerLeftRoom,
)
from ..logging.enhanced_logging_config import get_logger


class Room:
    """
    Represents a room in the MythosMUD game world.

    This class provides a stateless design where room data is loaded from
    JSON files and dynamic state (occupants) is tracked in memory. The
    class integrates with the EventBus to notify when state changes occur.

    As documented in the Cultes des Goules, proper tracking of room
    occupants is essential for maintaining awareness of the dimensional
    shifts that occur when entities move between spaces.
    """

    def __init__(self, room_data: dict, event_bus: EventBus | None = None):
        """
        Initialize a Room from JSON data.

        Args:
            room_data: Dictionary containing room information from JSON file
            event_bus: Optional EventBus instance for publishing events
        """
        # Static room data from JSON
        self.id = room_data.get("id", "")
        self.name = room_data.get("name", "")
        self.description = room_data.get("description", "")
        self.plane = room_data.get("plane", "")
        self.zone = room_data.get("zone", "")
        self.sub_zone = room_data.get("sub_zone", "")
        self.environment = room_data.get("resolved_environment", "outdoors")
        self.exits = room_data.get("exits", {})

        # Containers in this room (loaded from PostgreSQL)
        self._containers: list = room_data.get("containers", [])

        # Dynamic state (tracked in memory)
        self._players: set[str] = set()
        self._objects: set[str] = set()
        self._npcs: set[str] = set()

        # Event system integration
        self._event_bus = event_bus
        self._logger = get_logger(f"Room({self.id})")

        self._logger.debug("Initialized room", room_name=self.name, room_id=self.id)

    def player_entered(self, player_id: uuid.UUID | str) -> None:
        """
        Add a player to the room and trigger event.

        Args:
            player_id: The ID of the player entering the room (UUID or string)
        """
        if not player_id:
            raise ValueError("Player ID cannot be empty")

        # Convert to string for internal storage (Room uses set[str] for _players)
        player_id_str = str(player_id) if isinstance(player_id, uuid.UUID) else player_id

        if player_id_str in self._players:
            self._logger.warning("Player already in room", player_id=player_id, room_id=self.id)
            return

        self._players.add(player_id_str)
        self._logger.debug("Player entered room", player_id=player_id, room_id=self.id)

        # Publish event if event bus is available
        # Events still expect string, so convert for event creation
        if self._event_bus:
            event = PlayerEnteredRoom(player_id=player_id_str, room_id=self.id)
            self._event_bus.publish(event)

    def player_left(self, player_id: uuid.UUID | str) -> None:
        """
        Remove a player from the room and trigger event.

        Args:
            player_id: The ID of the player leaving the room (UUID or string)
        """
        if not player_id:
            raise ValueError("Player ID cannot be empty")

        # Convert to string for internal storage (Room uses set[str] for _players)
        player_id_str = str(player_id) if isinstance(player_id, uuid.UUID) else player_id

        if player_id_str not in self._players:
            self._logger.warning("Player not in room", player_id=player_id, room_id=self.id)
            return

        self._players.remove(player_id_str)
        self._logger.debug("Player left room", player_id=player_id, room_id=self.id)

        # Publish event if event bus is available
        # Events still expect string, so convert for event creation
        if self._event_bus:
            event = PlayerLeftRoom(player_id=player_id_str, room_id=self.id)
            self._event_bus.publish(event)

    def object_added(self, object_id: str, player_id: str | None = None) -> None:
        """
        Add an object to the room and trigger event.

        Args:
            object_id: The ID of the object being added
            player_id: Optional ID of the player who added the object
        """
        if not object_id:
            raise ValueError("Object ID cannot be empty")

        if object_id in self._objects:
            self._logger.warning("Object already in room", object_id=object_id, room_id=self.id)
            return

        self._objects.add(object_id)
        self._logger.debug("Object added to room", object_id=object_id, room_id=self.id)

        # Publish event if event bus is available
        if self._event_bus:
            event = ObjectAddedToRoom(object_id=object_id, room_id=self.id, player_id=player_id)
            self._event_bus.publish(event)

    def object_removed(self, object_id: str, player_id: str | None = None) -> None:
        """
        Remove an object from the room and trigger event.

        Args:
            object_id: The ID of the object being removed
            player_id: Optional ID of the player who removed the object
        """
        if not object_id:
            raise ValueError("Object ID cannot be empty")

        if object_id not in self._objects:
            self._logger.warning("Object not in room", object_id=object_id, room_id=self.id)
            return

        self._objects.remove(object_id)
        self._logger.debug("Object removed from room", object_id=object_id, room_id=self.id)

        # Publish event if event bus is available
        if self._event_bus:
            event = ObjectRemovedFromRoom(object_id=object_id, room_id=self.id, player_id=player_id)
            self._event_bus.publish(event)

    def npc_entered(self, npc_id: str) -> None:
        """
        Add an NPC to the room and trigger event.

        Args:
            npc_id: The ID of the NPC entering the room
        """
        if not npc_id:
            raise ValueError("NPC ID cannot be empty")

        if npc_id in self._npcs:
            self._logger.warning("NPC already in room", npc_id=npc_id, room_id=self.id)
            return

        self._npcs.add(npc_id)
        self._logger.debug("NPC entered room", npc_id=npc_id, room_id=self.id)

        # Publish event if event bus is available
        if self._event_bus:
            event = NPCEnteredRoom(npc_id=npc_id, room_id=self.id)
            self._event_bus.publish(event)

    def npc_left(self, npc_id: str) -> None:
        """
        Remove an NPC from the room and trigger event.

        Args:
            npc_id: The ID of the NPC leaving the room
        """
        if not npc_id:
            raise ValueError("NPC ID cannot be empty")

        if npc_id not in self._npcs:
            self._logger.warning("NPC not in room", npc_id=npc_id, room_id=self.id)
            return

        self._npcs.remove(npc_id)
        self._logger.debug("NPC left room", npc_id=npc_id, room_id=self.id)

        # Publish event if event bus is available
        if self._event_bus:
            event = NPCLeftRoom(npc_id=npc_id, room_id=self.id)
            self._event_bus.publish(event)

    def get_players(self) -> list[str]:
        """
        Get list of player IDs currently in the room.

        Returns:
            List of player IDs in the room
        """
        return list(self._players)

    def get_objects(self) -> list[str]:
        """
        Get list of object IDs currently in the room.

        Returns:
            List of object IDs in the room
        """
        return list(self._objects)

    def get_npcs(self) -> list[str]:
        """
        Get list of NPC IDs currently in the room.

        Returns:
            List of NPC IDs in the room
        """
        return list(self._npcs)

    def has_player(self, player_id: uuid.UUID | str) -> bool:
        """
        Check if a player is in the room.

        Args:
            player_id: The ID of the player to check (UUID or string)

        Returns:
            True if the player is in the room, False otherwise
        """
        # Convert to string for set lookup (Room uses set[str] for _players)
        player_id_str = str(player_id) if isinstance(player_id, uuid.UUID) else player_id
        return player_id_str in self._players

    def has_object(self, object_id: str) -> bool:
        """
        Check if an object is in the room.

        Args:
            object_id: The ID of the object to check

        Returns:
            True if the object is in the room, False otherwise
        """
        return object_id in self._objects

    def has_npc(self, npc_id: str) -> bool:
        """
        Check if an NPC is in the room.

        Args:
            npc_id: The ID of the NPC to check

        Returns:
            True if the NPC is in the room, False otherwise
        """
        return npc_id in self._npcs

    def get_occupant_count(self) -> int:
        """
        Get the total number of occupants in the room.

        Returns:
            Total count of players, objects, and NPCs in the room
        """
        return len(self._players) + len(self._objects) + len(self._npcs)

    def is_empty(self) -> bool:
        """
        Check if the room has no occupants.

        Returns:
            True if the room is empty, False otherwise
        """
        return self.get_occupant_count() == 0

    def get_containers(self) -> list:
        """
        Get list of containers in this room.

        Returns:
            List of container data dictionaries
        """
        return list(self._containers)

    def to_dict(self) -> dict:
        """
        Convert the room to a dictionary representation.

        Returns:
            Dictionary containing room data and current occupants
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "plane": self.plane,
            "zone": self.zone,
            "sub_zone": self.sub_zone,
            "environment": self.environment,
            "exits": self.exits,
            "containers": self.get_containers(),
            "players": self.get_players(),
            "objects": self.get_objects(),
            "npcs": self.get_npcs(),
            "occupant_count": self.get_occupant_count(),
        }

    def __str__(self) -> str:
        """String representation of the room."""
        return f"Room({self.id}: {self.name})"

    def __repr__(self) -> str:
        """Detailed string representation of the room."""
        return (
            f"Room(id='{self.id}', name='{self.name}', "
            f"players={len(self._players)}, objects={len(self._objects)}, "
            f"npcs={len(self._npcs)})"
        )
