"""
Real-time event handler for MythosMUD.

This module provides the RealTimeEventHandler class that bridges EventBus events
to real-time communication, enabling players to see each other in the game world.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.
"""

import time

from ..events import EventBus
from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from ..logging_config import get_logger
from .connection_manager import connection_manager


class RealTimeEventHandler:
    """
    Bridges EventBus events to real-time communication.

    This class subscribes to game events and converts them into real-time
    messages that are broadcast to connected clients. It serves as the
    critical link between the event system and the real-time communication
    layer.
    """

    def __init__(self, event_bus: EventBus | None = None):
        """
        Initialize the real-time event handler.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global
                instance.
        """
        self.event_bus = event_bus or EventBus()
        self.connection_manager = connection_manager
        self._logger = get_logger("RealTimeEventHandler")
        self._sequence_counter = 0

        # Subscribe to relevant game events
        self._subscribe_to_events()

        self._logger.info("RealTimeEventHandler initialized")

    def _subscribe_to_events(self):
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left)

        self._logger.info("Subscribed to PlayerEnteredRoom and PlayerLeftRoom events")

    def _get_next_sequence(self) -> int:
        """Get the next sequence number for events."""
        self._sequence_counter += 1
        return self._sequence_counter

    async def _handle_player_entered(self, event: PlayerEnteredRoom):
        """
        Handle player entering a room.

        Args:
            event: The PlayerEnteredRoom event
        """
        try:
            self._logger.debug(f"Handling player entered event: {event.player_id} -> {event.room_id}")

            # Get player information
            player = self.connection_manager._get_player(event.player_id)
            if not player:
                self._logger.warning(f"Player not found for entered event: {event.player_id}")
                return

            player_name = getattr(player, "name", event.player_id)

            # Create real-time message
            message = self._create_player_entered_message(event, player_name)

            # Subscribe player to the room
            await self.connection_manager.subscribe_to_room(event.player_id, event.room_id)

            # Broadcast to room occupants (excluding the entering player)
            await self.connection_manager.broadcast_to_room(event.room_id, message, exclude_player=event.player_id)

            # Send room occupants update to the entering player
            await self._send_room_occupants_update(event.room_id, event.player_id)

            self._logger.info(f"Player {player_name} entered room {event.room_id}")

        except Exception as e:
            self._logger.error(f"Error handling player entered event: {e}", exc_info=True)

    async def _handle_player_left(self, event: PlayerLeftRoom):
        """
        Handle player leaving a room.

        Args:
            event: The PlayerLeftRoom event
        """
        try:
            self._logger.debug(f"Handling player left event: {event.player_id} <- {event.room_id}")

            # Get player information
            player = self.connection_manager._get_player(event.player_id)
            if not player:
                self._logger.warning(f"Player not found for left event: {event.player_id}")
                return

            player_name = getattr(player, "name", event.player_id)

            # Create real-time message
            message = self._create_player_left_message(event, player_name)

            # Unsubscribe player from the room
            await self.connection_manager.unsubscribe_from_room(event.player_id, event.room_id)

            # Broadcast to remaining room occupants
            await self.connection_manager.broadcast_to_room(event.room_id, message)

            # Send room occupants update to remaining players
            await self._send_room_occupants_update(event.room_id)

            self._logger.info(f"Player {player_name} left room {event.room_id}")

        except Exception as e:
            self._logger.error(f"Error handling player left event: {e}", exc_info=True)

    def _create_player_entered_message(self, event: PlayerEnteredRoom, player_name: str) -> dict:
        """
        Create a real-time message for player entering a room.

        Args:
            event: The PlayerEnteredRoom event
            player_name: The name of the player

        Returns:
            dict: The formatted message
        """
        return {
            "event_type": "player_entered",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "sequence_number": self._get_next_sequence(),
            "room_id": event.room_id,
            "data": {
                "player_id": event.player_id,
                "player_name": player_name,
                "message": f"{player_name} enters the room.",
            },
        }

    def _create_player_left_message(self, event: PlayerLeftRoom, player_name: str) -> dict:
        """
        Create a real-time message for player leaving a room.

        Args:
            event: The PlayerLeftRoom event
            player_name: The name of the player

        Returns:
            dict: The formatted message
        """
        return {
            "event_type": "player_left",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "sequence_number": self._get_next_sequence(),
            "room_id": event.room_id,
            "data": {
                "player_id": event.player_id,
                "player_name": player_name,
                "message": f"{player_name} leaves the room.",
            },
        }

    async def _send_room_occupants_update(self, room_id: str, exclude_player: str = None):
        """
        Send room occupants update to players in the room.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        try:
            # Get room occupants
            occupants = self._get_room_occupants(room_id)

            # Create occupants update message
            message = {
                "event_type": "room_occupants",
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "sequence_number": self._get_next_sequence(),
                "room_id": room_id,
                "data": {"occupants": occupants, "count": len(occupants)},
            }

            # Send to room occupants
            await self.connection_manager.broadcast_to_room(room_id, message, exclude_player=exclude_player)

        except Exception as e:
            self._logger.error(f"Error sending room occupants update: {e}", exc_info=True)

    def _get_room_occupants(self, room_id: str) -> list[dict]:
        """
        Get the list of occupants in a room.

        Args:
            room_id: The room ID

        Returns:
            list[dict]: List of occupant information
        """
        occupants = []

        try:
            # Get room from persistence
            persistence = self.connection_manager.persistence
            if not persistence:
                return occupants

            room = persistence.get_room(room_id)
            if not room:
                return occupants

            # Get player IDs in the room
            player_ids = room.get_players()

            # Convert to occupant information
            for player_id in player_ids:
                player = self.connection_manager._get_player(player_id)
                if player:
                    occupant_info = {
                        "player_id": player_id,
                        "player_name": getattr(player, "name", player_id),
                        "level": getattr(player, "level", 1),
                        "online": player_id in self.connection_manager.player_websockets,
                    }
                    occupants.append(occupant_info)

        except Exception as e:
            self._logger.error(f"Error getting room occupants: {e}", exc_info=True)

        return occupants

    def shutdown(self):
        """Shutdown the event handler."""
        self._logger.info("Shutting down RealTimeEventHandler")
        # Note: EventBus will handle its own shutdown


# Global instance
real_time_event_handler: RealTimeEventHandler | None = None


def get_real_time_event_handler() -> RealTimeEventHandler:
    """
    Get the global RealTimeEventHandler instance.

    Returns:
        RealTimeEventHandler: The global event handler instance
    """
    global real_time_event_handler
    if real_time_event_handler is None:
        real_time_event_handler = RealTimeEventHandler()
    return real_time_event_handler
