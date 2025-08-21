"""
Real-time event handler for MythosMUD.

This module provides the RealTimeEventHandler class that bridges EventBus events
to real-time communication, enabling players to see each other in the game world.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.
"""

from datetime import UTC, datetime

from ..events import EventBus
from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from ..logging_config import get_logger
from ..services.chat_logger import chat_logger
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

        # Chat logger for AI processing
        self.chat_logger = chat_logger

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

            # Log player movement for AI processing
            try:
                room = (
                    self.connection_manager.persistence.get_room(event.room_id)
                    if self.connection_manager.persistence
                    else None
                )
                room_name = getattr(room, "name", event.room_id) if room else event.room_id

                self.chat_logger.log_player_joined_room(
                    player_id=event.player_id, player_name=player_name, room_id=event.room_id, room_name=room_name
                )
            except Exception as e:
                self._logger.error(f"Error logging player joined room: {e}")

            # Create real-time message
            message = self._create_player_entered_message(event, player_name)

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(event.player_id) if event.player_id else None
            room_id_str = str(event.room_id) if event.room_id else None

            self._logger.debug(
                f"Broadcasting player_entered: exclude_player={exclude_player_id} (type: {type(exclude_player_id)})"
            )

            # Broadcast to room occupants (excluding the entering player)
            await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Subscribe player to the room so they will receive subsequent broadcasts
            await self.connection_manager.subscribe_to_room(exclude_player_id, room_id_str)

            # Send room occupants update to the entering player as a personal message
            # so they immediately see who is present on joining
            await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)
            try:
                # Also send a direct occupants snapshot to the entering player
                occupants_info = self._get_room_occupants(room_id_str)
                names: list[str] = []
                for occ in occupants_info or []:
                    if isinstance(occ, dict):
                        n = occ.get("player_name") or occ.get("name")
                        if n:
                            names.append(n)
                    elif isinstance(occ, str):
                        names.append(occ)

                personal = {
                    "event_type": "room_occupants",
                    "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                    "sequence_number": self._get_next_sequence(),
                    "room_id": room_id_str,
                    "data": {"occupants": names, "count": len(names)},
                }
                await self.connection_manager.send_personal_message(exclude_player_id, personal)
            except Exception as e:
                self._logger.error(f"Error sending personal occupants update: {e}")

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

            # Log player movement for AI processing
            try:
                room = (
                    self.connection_manager.persistence.get_room(event.room_id)
                    if self.connection_manager.persistence
                    else None
                )
                room_name = getattr(room, "name", event.room_id) if room else event.room_id

                self.chat_logger.log_player_left_room(
                    player_id=event.player_id, player_name=player_name, room_id=event.room_id, room_name=room_name
                )
            except Exception as e:
                self._logger.error(f"Error logging player left room: {e}")

            # Create real-time message
            message = self._create_player_left_message(event, player_name)

            # Unsubscribe player from the room
            await self.connection_manager.unsubscribe_from_room(event.player_id, event.room_id)

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(event.player_id) if event.player_id else None
            room_id_str = str(event.room_id) if event.room_id else None

            self._logger.debug(
                f"Broadcasting player_left: exclude_player={exclude_player_id} (type: {type(exclude_player_id)})"
            )

            # Broadcast to remaining room occupants (excluding the leaving player)
            await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Send room occupants update to remaining players
            await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)

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

    def _create_player_left_message(self, event: PlayerLeftRoom, player_name: str) -> dict:
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

    async def _send_room_occupants_update(self, room_id: str, exclude_player: str = None):
        """
        Send room occupants update to players in the room.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        try:
            # Get room occupants
            occupants_info = self._get_room_occupants(room_id)

            # Transform to list of names for client UI consistency
            occupant_names: list[str] = []
            for occ in occupants_info or []:
                if isinstance(occ, dict):
                    name = occ.get("player_name") or occ.get("name")
                    if name:
                        occupant_names.append(name)
                elif isinstance(occ, str):
                    occupant_names.append(occ)

            # Create occupants update message
            # Convert room_id to string for JSON serialization
            room_id_str = str(room_id) if room_id else ""

            message = {
                "event_type": "room_occupants",
                "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "sequence_number": self._get_next_sequence(),
                "room_id": room_id_str,
                "data": {"occupants": occupant_names, "count": len(occupant_names)},
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
