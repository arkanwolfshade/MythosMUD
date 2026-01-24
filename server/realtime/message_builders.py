"""
Message building utilities for real-time events.

This module provides utilities for creating structured messages
for real-time communication with clients.

As documented in "Event Message Protocols" - Dr. Armitage, 1928
"""

from collections.abc import Callable
from datetime import UTC, datetime
from typing import Any, cast

from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom


class MessageBuilder:
    """Utility class for building real-time event messages."""

    def __init__(self, sequence_counter: Any) -> None:
        """
        Initialize the message builder.

        Args:
            sequence_counter: Callable that returns the next sequence number
        """
        self._sequence_counter = sequence_counter

    def _get_next_sequence(self) -> int:
        """Get the next sequence number."""
        if callable(self._sequence_counter):
            result: int = cast(Callable[[], int], self._sequence_counter)()
            return result
        return 0

    def get_next_sequence(self) -> int:
        """
        Get the next sequence number (public API).

        Returns:
            The next sequence number for message ordering
        """
        return self._get_next_sequence()

    def create_player_entered_message(self, event: PlayerEnteredRoom, player_name: str) -> dict[str, Any]:
        """
        Create a real-time message for player entering a room.

        Args:
            event: The PlayerEnteredRoom event
            player_name: The name of the player

        Returns:
            dict: The formatted message
        """
        # Convert UUIDs to strings for JSON serialization
        player_id = str(event.player_id) if event.player_id else ""
        room_id = str(event.room_id) if event.room_id else ""

        return {
            "event_type": "player_entered",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self._get_next_sequence(),
            "room_id": room_id,
            "data": {
                "player_id": player_id,
                "player_name": player_name,
                "message": f"{player_name} enters the room.",
            },
        }

    def create_player_left_message(self, event: PlayerLeftRoom, player_name: str) -> dict[str, Any]:
        """
        Create a real-time message for player leaving a room.

        Args:
            event: The PlayerLeftRoom event
            player_name: The name of the player

        Returns:
            dict: The formatted message
        """
        # Convert UUIDs to strings for JSON serialization
        player_id = str(event.player_id) if event.player_id else ""
        room_id = str(event.room_id) if event.room_id else ""

        return {
            "event_type": "player_left",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self._get_next_sequence(),
            "room_id": room_id,
            "data": {
                "player_id": player_id,
                "player_name": player_name,
                "message": f"{player_name} leaves the room.",
            },
        }

    def create_npc_movement_message(self, npc_name: str, direction: str | None, movement_type: str) -> str:
        """
        Create an NPC movement message with direction.

        Args:
            npc_name: Name of the NPC
            direction: Direction of movement (e.g., "north", "south") or None
            movement_type: "left" or "entered"

        Returns:
            Formatted movement message
        """
        if movement_type == "left":
            if direction:
                return f"{npc_name} left {direction}."
            return f"{npc_name} left the room."
        if movement_type == "entered":
            if direction:
                return f"{npc_name} entered from {direction}."
            return f"{npc_name} entered the room."
        return f"{npc_name} moved."

    def build_occupants_update_message(
        self, room_id_str: str, players: list[str], npcs: list[str], all_occupants: list[str]
    ) -> dict[str, Any]:
        """
        Build the room occupants update message.

        Args:
            room_id_str: Room ID as string
            players: List of player names
            npcs: List of NPC names
            all_occupants: List of all occupant names

        Returns:
            Message dictionary for room occupants update
        """
        return {
            "event_type": "room_occupants",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self._get_next_sequence(),
            "room_id": room_id_str,
            "data": {
                # Structured data for new UI (separate columns)
                "players": players,
                "npcs": npcs,
                # Backward compatibility: flat list for legacy clients
                "occupants": all_occupants,
                "count": len(all_occupants),
            },
        }

    def build_room_update_message(self, room_id: str, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Build a room update message.

        Args:
            room_id: The room ID
            room_data: The room data dictionary

        Returns:
            Room update message dictionary
        """
        return {
            "event_type": "room_update",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self._get_next_sequence(),
            "room_id": room_id,
            "data": {
                "room": room_data,
                "entities": [],
                # CRITICAL: Do NOT include occupants in room_update - only in room_occupants events
                # This prevents room_update from overwriting structured NPC/player data
            },
        }
