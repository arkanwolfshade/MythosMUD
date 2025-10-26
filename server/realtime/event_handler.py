"""
Real-time event handler for MythosMUD.

This module provides the RealTimeEventHandler class that bridges EventBus events
to real-time communication, enabling players to see each other in the game world.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.
"""

from datetime import UTC, datetime

from ..app.tracked_task_manager import get_global_tracked_manager
from ..events import EventBus
from ..events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerLeftRoom
from ..logging.enhanced_logging_config import get_logger
from ..services.chat_logger import chat_logger
from ..services.player_combat_service import PlayerXPAwardEvent
from ..services.room_sync_service import get_room_sync_service
from .connection_manager import connection_manager


class RealTimeEventHandler:
    """
    Bridges EventBus events to real-time communication.

    This class subscribes to game events and converts them into real-time
    messages that are broadcast to connected clients. It serves as the
    critical link between the event system and the real-time communication
    layer.
    """

    def __init__(self, event_bus: EventBus | None = None, task_registry=None):
        """
        Initialize the real-time event handler.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global
                instance.
            task_registry: Optional TaskRegistry instance for current lifecycle task tracking
        """
        self.event_bus = event_bus or EventBus()
        self.connection_manager = connection_manager
        self._logger = get_logger("RealTimeEventHandler")
        self._sequence_counter = 0

        # Task registry for tracking child tasks spawned by event broadcasting
        self.task_registry = task_registry

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        # Room synchronization service for enhanced event processing
        self.room_sync_service = get_room_sync_service()

        # Subscribe to relevant game events
        self._subscribe_to_events()

        self._logger.info("RealTimeEventHandler initialized with enhanced room synchronization")

    def _subscribe_to_events(self):
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left)
        self.event_bus.subscribe(PlayerXPAwardEvent, self._handle_player_xp_awarded)

        self._logger.info("Subscribed to PlayerEnteredRoom, PlayerLeftRoom, NPCEnteredRoom, and NPCLeftRoom events")

    def _get_next_sequence(self) -> int:
        """Get the next sequence number for events."""
        self._sequence_counter += 1
        return self._sequence_counter

    async def _handle_player_entered(self, event: PlayerEnteredRoom):
        """
        Handle player entering a room with enhanced synchronization.

        Args:
            event: The PlayerEnteredRoom event
        """
        try:
            # Process event with proper ordering to prevent race conditions
            processed_event = self.room_sync_service._process_event_with_ordering(event)

            self._logger.debug(
                f"Handling player entered event with synchronization: {processed_event.player_id} -> {processed_event.room_id}"
            )

            # Get player information
            player = self.connection_manager._get_player(processed_event.player_id)
            if not player:
                self._logger.warning("Player not found for entered event", player_id=processed_event.player_id)
                return

            player_name = getattr(player, "name", processed_event.player_id)

            # Log player movement for AI processing
            try:
                room = (
                    self.connection_manager.persistence.get_room(processed_event.room_id)
                    if self.connection_manager.persistence
                    else None
                )
                room_name = getattr(room, "name", processed_event.room_id) if room else processed_event.room_id

                self.chat_logger.log_player_joined_room(
                    player_id=processed_event.player_id,
                    player_name=player_name,
                    room_id=processed_event.room_id,
                    room_name=room_name,
                )
            except Exception as e:
                self._logger.error("Error logging player joined room", error=str(e))

            # Create real-time message with processed event
            message = self._create_player_entered_message(processed_event, player_name)

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(processed_event.player_id) if processed_event.player_id else None
            room_id_str = str(processed_event.room_id) if processed_event.room_id else None

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
                        n = occ.get("player_name") or occ.get("npc_name") or occ.get("name")
                        if n:
                            names.append(n)
                    elif isinstance(occ, str):
                        names.append(occ)
                # Convert room_id to string for JSON serialization
                room_id_str = str(processed_event.room_id) if processed_event.room_id else ""

                personal = {
                    "event_type": "room_occupants",
                    "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                    "sequence_number": self._get_next_sequence(),
                    "room_id": room_id_str,
                    "data": {"occupants": names, "count": len(names)},
                }
                await self.connection_manager.send_personal_message(exclude_player_id, personal)
            except Exception as e:
                self._logger.error("Error sending personal occupants update", error=str(e))

            self._logger.info(
                "Player entered room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except Exception as e:
            self._logger.error("Error handling player entered event", error=str(e), exc_info=True)

    async def _handle_player_left(self, event: PlayerLeftRoom):
        """
        Handle player leaving a room with enhanced synchronization.

        Args:
            event: The PlayerLeftRoom event
        """
        try:
            # Process event with proper ordering to prevent race conditions
            processed_event = self.room_sync_service._process_event_with_ordering(event)

            self._logger.debug(
                f"Handling player left event with synchronization: {processed_event.player_id} <- {processed_event.room_id}"
            )

            # Get player information
            player = self.connection_manager._get_player(processed_event.player_id)
            if not player:
                self._logger.warning("Player not found for left event", player_id=processed_event.player_id)
                return

            player_name = getattr(player, "name", processed_event.player_id)

            # Log player movement for AI processing
            try:
                room = (
                    self.connection_manager.persistence.get_room(processed_event.room_id)
                    if self.connection_manager.persistence
                    else None
                )
                room_name = getattr(room, "name", processed_event.room_id) if room else processed_event.room_id

                self.chat_logger.log_player_left_room(
                    player_id=processed_event.player_id,
                    player_name=player_name,
                    room_id=processed_event.room_id,
                    room_name=room_name,
                )
            except Exception as e:
                self._logger.error("Error logging player left room", error=str(e))

            # Create real-time message with processed event
            message = self._create_player_left_message(processed_event, player_name)

            # Unsubscribe player from the room
            await self.connection_manager.unsubscribe_from_room(processed_event.player_id, processed_event.room_id)

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(processed_event.player_id) if processed_event.player_id else None
            room_id_str = str(processed_event.room_id) if processed_event.room_id else None

            self._logger.debug(
                f"Broadcasting player_left: exclude_player={exclude_player_id} (type: {type(exclude_player_id)})"
            )

            # Broadcast to remaining room occupants (excluding the leaving player)
            await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Send room occupants update to remaining players
            await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)

            self._logger.info(
                "Player left room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except Exception as e:
            self._logger.error("Error handling player left event", error=str(e), exc_info=True)

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
                    name = occ.get("player_name") or occ.get("npc_name") or occ.get("name")
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
            self._logger.error("Error sending room occupants update", error=str(e), exc_info=True)

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

            # Get NPC IDs in the room
            npc_ids = room.get_npcs()

            # Convert NPCs to occupant information
            for npc_id in npc_ids:
                # Extract NPC name from the NPC ID (format: npc_name_room_id_timestamp_random)
                npc_name = npc_id.split("_")[0].replace("_", " ").title()
                occupant_info = {
                    "npc_id": npc_id,
                    "npc_name": npc_name,
                    "type": "npc",
                }
                occupants.append(occupant_info)

        except Exception as e:
            self._logger.error("Error getting room occupants", error=str(e), exc_info=True)

        return occupants

    def _handle_npc_entered(self, event: NPCEnteredRoom):
        """
        Handle NPC entering a room.

        This method updates the room state to include the NPC in the occupant list
        and broadcasts the room update to all players in the room.

        Args:
            event: NPCEnteredRoom event containing NPC and room information
        """
        try:
            self._logger.info("NPC entered room", npc_id=event.npc_id, room_id=event.room_id)

            # Get the room from persistence
            persistence = self.connection_manager.persistence
            if not persistence:
                self._logger.warning("Persistence layer not available for NPC room entry")
                return

            room = persistence.get_room(event.room_id)
            if not room:
                self._logger.warning("Room not found for NPC entry", room_id=event.room_id)
                return

            # Add NPC to room's occupant list
            room.npc_entered(event.npc_id)

            # Schedule room update broadcast (async operation)
            import asyncio

            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # Schedule the async operation to run later
                    if self.task_registry:
                        self.task_registry.register_task(
                            self._send_room_occupants_update(event.room_id),
                            f"event_handler/room_occupants_{event.room_id}",
                            "event_handler",
                        )
                    else:
                        # Task 4.4: Replace with tracked task creation to prevent memory leaks
                        tracked_manager = get_global_tracked_manager()
                        tracked_manager.create_tracked_task(
                            self._send_room_occupants_update(event.room_id),
                            task_name=f"event_handler/room_occupants_{event.room_id}",
                            task_type="event_handler",
                        )
                else:
                    # If no event loop is running, just log that we can't broadcast
                    self._logger.debug("No event loop available for room occupants update broadcast")
            except RuntimeError:
                # No event loop available, just log that we can't broadcast
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug(
                "NPC successfully added to room occupant list", npc_id=event.npc_id, room_id=event.room_id
            )

        except Exception as e:
            self._logger.error("Error handling NPC entered room event", error=str(e), exc_info=True)

    def _handle_npc_left(self, event: NPCLeftRoom):
        """
        Handle NPC leaving a room.

        This method updates the room state to remove the NPC from the occupant list
        and broadcasts the room update to all players in the room.

        Args:
            event: NPCLeftRoom event containing NPC and room information
        """
        try:
            self._logger.info("NPC left room", npc_id=event.npc_id, room_id=event.room_id)

            # Get the room from persistence
            persistence = self.connection_manager.persistence
            if not persistence:
                self._logger.warning("Persistence layer not available for NPC room exit")
                return

            room = persistence.get_room(event.room_id)
            if not room:
                self._logger.warning("Room not found for NPC exit", room_id=event.room_id)
                return

            # Remove NPC from room's occupant list
            room.npc_left(event.npc_id)

            # Schedule room update broadcast (async operation)
            import asyncio

            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # Schedule the async operation to run later
                    if self.task_registry:
                        self.task_registry.register_task(
                            self._send_room_occupants_update(event.room_id),
                            f"event_handler/room_occupants_{event.room_id}",
                            "event_handler",
                        )
                    else:
                        # Task 4.4: Replace with tracked task creation to prevent memory leaks
                        tracked_manager = get_global_tracked_manager()
                        tracked_manager.create_tracked_task(
                            self._send_room_occupants_update(event.room_id),
                            task_name=f"event_handler/room_occupants_{event.room_id}",
                            task_type="event_handler",
                        )
                else:
                    # If no event loop is running, just log that we can't broadcast
                    self._logger.debug("No event loop available for room occupants update broadcast")
            except RuntimeError:
                # No event loop available, just log that we can't broadcast
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug(
                "NPC successfully removed from room occupant list", npc_id=event.npc_id, room_id=event.room_id
            )

        except Exception as e:
            self._logger.error("Error handling NPC left room event", error=str(e), exc_info=True)

    def shutdown(self):
        """Shutdown the event handler."""
        self._logger.info("Shutting down RealTimeEventHandler")
        # Note: EventBus will handle its own shutdown

    async def _handle_player_xp_awarded(self, event: PlayerXPAwardEvent):
        """
        Handle player XP award events by sending updates to the client.

        Args:
            event: The PlayerXPAwardEvent containing XP award information
        """
        try:
            player_id_str = str(event.player_id)

            # Get the current player data to send updated XP
            player = self.connection_manager._get_player(player_id_str)
            if not player:
                self._logger.warning("Player not found for XP award event", player_id=player_id_str)
                return

            # Create player update event with new XP
            player_update_data = {
                "player_id": player_id_str,
                "name": player.name,
                "level": player.level,
                "xp": player.experience_points,
                "current_room_id": getattr(player, "current_room_id", None),
            }

            # Send personal message to the player
            from .envelope import build_event
            xp_update_event = build_event(
                "player_xp_updated",
                {
                    "xp_amount": event.xp_amount,
                    "new_level": event.new_level,
                    "player": player_update_data,
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, xp_update_event)

            self._logger.info(
                "Sent XP award update to player",
                player_id=player_id_str,
                xp_amount=event.xp_amount,
                new_level=event.new_level,
            )

        except Exception as e:
            self._logger.error("Error handling player XP award event", error=str(e), exc_info=True)


# Global instance
real_time_event_handler: RealTimeEventHandler | None = None


def get_real_time_event_handler(event_bus=None, task_registry=None) -> RealTimeEventHandler:
    """
    Get the global RealTimeEventHandler instance.

    Args:
        event_bus: Optional EventBus instance. If None, will get the global instance.
        task_registry: Optional TaskRegistry instance for task lifecycle tracking

    Returns:
        RealTimeEventHandler: The global event handler instance
    """
    global real_time_event_handler
    if real_time_event_handler is None:
        real_time_event_handler = RealTimeEventHandler(event_bus=event_bus, task_registry=task_registry)
    # If we've passed a task_registry after init, update the instance
    elif task_registry and not real_time_event_handler.task_registry:
        real_time_event_handler.task_registry = task_registry
    return real_time_event_handler
