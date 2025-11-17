"""
Real-time event handler for MythosMUD.

This module provides the RealTimeEventHandler class that bridges EventBus events
to real-time communication, enabling players to see each other in the game world.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.
"""

from datetime import UTC, datetime
from typing import Any, cast

from ..app.tracked_task_manager import get_global_tracked_manager
from ..events import EventBus
from ..events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerHPUpdated, PlayerLeftRoom
from ..logging.enhanced_logging_config import get_logger
from ..services.chat_logger import chat_logger
from ..services.player_combat_service import PlayerXPAwardEvent
from ..services.room_sync_service import get_room_sync_service
from .connection_manager import _get_npc_name_from_instance


class RealTimeEventHandler:
    """
    Bridges EventBus events to real-time communication.

    This class subscribes to game events and converts them into real-time
    messages that are broadcast to connected clients. It serves as the
    critical link between the event system and the real-time communication
    layer.
    """

    def __init__(
        self, event_bus: EventBus | None = None, task_registry: Any | None = None, connection_manager=None
    ) -> None:
        """
        Initialize the real-time event handler.

        Args:
            event_bus: Optional EventBus instance. If None, will get the global instance.
            task_registry: Optional TaskRegistry instance for current lifecycle task tracking
            connection_manager: ConnectionManager instance (injected dependency)

        AI Agent: connection_manager now injected as parameter instead of using global import
        """
        self.event_bus = event_bus or EventBus()
        self.connection_manager = connection_manager  # AI Agent: Injected dependency
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

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left)
        self.event_bus.subscribe(PlayerXPAwardEvent, self._handle_player_xp_awarded)
        self.event_bus.subscribe(PlayerHPUpdated, self._handle_player_hp_updated)

        # Subscribe to death/respawn events
        from ..events.event_types import PlayerDiedEvent, PlayerHPDecayEvent, PlayerRespawnedEvent

        self.event_bus.subscribe(PlayerDiedEvent, self._handle_player_died)
        self.event_bus.subscribe(PlayerHPDecayEvent, self._handle_player_hp_decay)
        self.event_bus.subscribe(PlayerRespawnedEvent, self._handle_player_respawned)

        self._logger.info("Subscribed to PlayerEnteredRoom, PlayerLeftRoom, NPCEnteredRoom, and NPCLeftRoom events")

    def _get_next_sequence(self) -> int:
        """Get the next sequence number for events."""
        self._sequence_counter += 1
        return self._sequence_counter

    async def _handle_player_entered(self, event: PlayerEnteredRoom) -> None:
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
            if room_id_str is not None:
                await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Subscribe player to the room so they will receive subsequent broadcasts
            if exclude_player_id is not None and room_id_str is not None:
                await self.connection_manager.subscribe_to_room(exclude_player_id, room_id_str)

            # Send room occupants update to the entering player as a personal message
            # so they immediately see who is present on joining
            if room_id_str is not None and exclude_player_id is not None:
                await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)
            try:
                # Send full room update to the entering player so their Room Info panel updates
                if room_id_str is not None and exclude_player_id is not None:
                    # Get room data
                    room = (
                        self.connection_manager.persistence.get_room(room_id_str)
                        if self.connection_manager.persistence
                        else None
                    )
                    if room:
                        # Get room occupants and transform to names
                        occupants_info = self._get_room_occupants(room_id_str)
                        occupant_names: list[str] = []
                        for occ in occupants_info or []:
                            if isinstance(occ, dict):
                                n = occ.get("player_name") or occ.get("npc_name") or occ.get("name")
                                if n:
                                    occupant_names.append(n)
                            elif isinstance(occ, str):
                                occupant_names.append(occ)

                        # Create room_update event with full room data
                        room_data = room.to_dict() if hasattr(room, "to_dict") else room
                        room_update_event = {
                            "event_type": "room_update",
                            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                            "sequence_number": self._get_next_sequence(),
                            "room_id": room_id_str,
                            "data": {
                                "room": room_data,
                                "entities": [],
                                "occupants": occupant_names,
                                "occupant_count": len(occupant_names),
                            },
                        }
                        # Send as personal message to entering player
                        await self.connection_manager.send_personal_message(exclude_player_id, room_update_event)
                        self._logger.debug(
                            "Sent room_update to entering player",
                            player_id=exclude_player_id,
                            room_id=room_id_str,
                            occupants=occupant_names,
                        )

                # Also send a direct occupants snapshot to the entering player
                if room_id_str is None:
                    occupants_snapshot: list[dict[str, Any] | str] | None = []
                else:
                    occupants_snapshot = self._get_room_occupants(room_id_str)
                names: list[str] = []
                for occ in occupants_snapshot or []:
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
                if exclude_player_id is not None:
                    await self.connection_manager.send_personal_message(exclude_player_id, personal)
            except Exception as e:
                self._logger.error("Error sending personal room update and occupants", error=str(e))

            self._logger.info(
                "Player entered room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except Exception as e:
            self._logger.error("Error handling player entered event", error=str(e), exc_info=True)

    async def _handle_player_left(self, event: PlayerLeftRoom) -> None:
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
            if room_id_str is not None:
                await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Send room occupants update to remaining players
            if room_id_str is not None and exclude_player_id is not None:
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

    async def _send_room_occupants_update(self, room_id: str, exclude_player: str | None = None) -> None:
        """
        Send room occupants update to players in the room.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        try:
            # Get room occupants
            occupants_info: list[dict[str, Any] | str] = self._get_room_occupants(room_id)

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

    def _get_room_occupants(self, room_id: str) -> list[dict[str, Any] | str]:
        """
        Get the list of occupants in a room.

        Args:
            room_id: The room ID

        Returns:
            list[dict]: List of occupant information
        """
        occupants: list[dict[str, Any] | str] = []

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
                # Get NPC name from the actual NPC instance, preserving original case from database
                npc_name = _get_npc_name_from_instance(npc_id)
                if npc_name:
                    occupant_info = {
                        "npc_id": npc_id,
                        "npc_name": npc_name,
                        "type": "npc",
                    }
                    occupants.append(occupant_info)
                else:
                    # Fallback: Extract NPC name from the NPC ID if instance not found
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

    def _handle_npc_entered(self, event: NPCEnteredRoom) -> None:
        """
        Handle NPC entering a room.

        This method broadcasts NPC appearance and triggers occupant updates.
        Room state (NPC presence) is mutated only by domain sources (e.g., Room.npc_entered).

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

            # Get the NPC's spawn message from behavior_config (if available)
            spawn_message = self._get_npc_spawn_message(event.npc_id)
            if spawn_message:
                # Send the spawn message to all players in the room
                self._send_room_message(event.room_id, spawn_message)

            # Schedule room update broadcast (async operation)
            import asyncio

            try:
                # Use get_running_loop() instead of deprecated get_event_loop()
                # get_running_loop() raises RuntimeError if no loop is running
                _ = asyncio.get_running_loop()  # Verify loop exists
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
            except RuntimeError:
                # No running event loop - log and skip async operation
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug("Processed NPC entered event", npc_id=event.npc_id, room_id=event.room_id)

        except Exception as e:
            self._logger.error("Error handling NPC entered room event", error=str(e), exc_info=True)

    def _handle_npc_left(self, event: NPCLeftRoom) -> None:
        """
        Handle NPC leaving a room.

        This method triggers occupant updates. Room state is mutated by domain sources only.

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

            # Schedule room update broadcast (async operation)
            import asyncio

            try:
                # Use get_running_loop() instead of deprecated get_event_loop()
                # get_running_loop() raises RuntimeError if no loop is running
                _ = asyncio.get_running_loop()  # Verify loop exists
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
            except RuntimeError:
                # No running event loop - log and skip async operation
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug("Processed NPC left event", npc_id=event.npc_id, room_id=event.room_id)

        except Exception as e:
            self._logger.error("Error handling NPC left room event", error=str(e), exc_info=True)

    def shutdown(self) -> None:
        """Shutdown the event handler."""
        self._logger.info("Shutting down RealTimeEventHandler")
        # Note: EventBus will handle its own shutdown

    async def _handle_player_xp_awarded(self, event: PlayerXPAwardEvent) -> None:
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

    def _get_npc_spawn_message(self, npc_id: str) -> str | None:
        """
        Get the spawn message for an NPC from its behavior_config.

        If no custom spawn message is defined, returns a default message: "<npc-name> appears."

        Args:
            npc_id: The NPC ID

        Returns:
            Spawn message (custom or default), or None if NPC not found
        """
        try:
            # Get the NPC instance from the lifecycle manager
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return None

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
                return None

            npc_instance = lifecycle_manager.active_npcs[npc_id]

            # Get the NPC name for the default message
            npc_name = getattr(npc_instance, "name", "An NPC")

            # Get the behavior_config from the NPC instance
            behavior_config = getattr(npc_instance, "behavior_config", None)
            if behavior_config:
                # Parse the behavior_config if it's a JSON string
                import json

                if isinstance(behavior_config, str):
                    try:
                        behavior_config = json.loads(behavior_config)
                    except (json.JSONDecodeError, ValueError):
                        # If parsing fails, use default message
                        return f"{npc_name} appears."

                # Get the spawn_message from the behavior_config
                spawn_message = behavior_config.get("spawn_message")
                if spawn_message:
                    return cast(str, spawn_message)

            # Return default message if no custom message is defined
            return f"{npc_name} appears."

        except Exception as e:
            self._logger.debug("Error getting NPC spawn message", npc_id=npc_id, error=str(e))
            return None

    def _send_room_message(self, room_id: str, message: str) -> None:
        """
        Send a message to all players in a room.

        Args:
            room_id: The room ID
            message: The message to send
        """
        try:
            # Get all players in the room
            from ..persistence import get_persistence
            from .envelope import build_event

            persistence = get_persistence()
            room = persistence.get_room(room_id)
            if not room:
                self._logger.warning("Room not found for sending room message", room_id=room_id)
                return

            # Get all player IDs in the room
            player_ids = list(room._players)  # Get the player IDs from the room

            # Send the message to each player in the room
            import asyncio

            for player_id in player_ids:
                # Create the message event
                message_event = build_event(
                    "room_message",
                    {
                        "message": message,
                        "room_id": room_id,
                        "message_type": "npc_spawn",
                    },
                    player_id=player_id,
                )

                # Schedule the async message send
                try:
                    # Use get_running_loop() instead of deprecated get_event_loop()
                    # get_running_loop() raises RuntimeError if no loop is running
                    _ = asyncio.get_running_loop()  # Verify loop exists
                    # Create a task to send the message
                    if self.task_registry:
                        self.task_registry.register_task(
                            self.connection_manager.send_personal_message(player_id, message_event),
                            f"event_handler/room_message_{room_id}_{player_id}",
                            "event_handler",
                        )
                    else:
                        from ..async_utils.tracked_task_manager import get_global_tracked_manager

                        tracked_manager = get_global_tracked_manager()
                        tracked_manager.create_tracked_task(
                            self.connection_manager.send_personal_message(player_id, message_event),
                            task_name=f"event_handler/room_message_{room_id}_{player_id}",
                            task_type="event_handler",
                        )
                except RuntimeError:
                    # No running event loop - log and skip async operation
                    self._logger.debug("No event loop available for room message broadcast")

        except Exception as e:
            self._logger.error("Error sending room message", room_id=room_id, error=str(e), exc_info=True)

    async def _handle_player_hp_updated(self, event: PlayerHPUpdated) -> None:
        """
        Handle player HP update events by sending updates to the client.

        Args:
            event: The PlayerHPUpdated event containing HP change information
        """
        try:
            player_id_str = event.player_id

            # Get the current player data to send updated HP
            player = self.connection_manager._get_player(player_id_str)
            if not player:
                self._logger.warning("Player not found for HP update event", player_id=player_id_str)
                return

            # Create player update event with new HP
            player_update_data = {
                "player_id": player_id_str,
                "name": player.name,
                "health": event.new_hp,
                "max_health": event.max_hp,
                "current_room_id": getattr(player, "current_room_id", None),
            }

            # Send personal message to the player
            from .envelope import build_event

            hp_update_event = build_event(
                "player_hp_updated",
                {
                    "old_hp": event.old_hp,
                    "new_hp": event.new_hp,
                    "max_hp": event.max_hp,
                    "damage_taken": event.damage_taken,
                    "player": player_update_data,
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, hp_update_event)

            self._logger.info(
                "Sent HP update to player",
                player_id=player_id_str,
                old_hp=event.old_hp,
                new_hp=event.new_hp,
                damage_taken=event.damage_taken,
            )

        except Exception as e:
            self._logger.error("Error handling player HP update event", error=str(e), exc_info=True)

    async def _handle_player_died(self, event: Any) -> None:
        """
        Handle player death events by sending death notification to the client.

        Args:
            event: The PlayerDiedEvent containing death information
        """
        try:
            player_id_str = event.player_id

            # Send personal message to the player
            from .envelope import build_event

            death_event = build_event(
                "player_died",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "death_location": event.room_id,
                    "killer_id": event.killer_id,
                    "killer_name": event.killer_name,
                    "message": "You have died. The darkness claims you utterly.",
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, death_event)

            self._logger.info("Sent death notification to player", player_id=player_id_str, room_id=event.room_id)

        except Exception as e:
            self._logger.error("Error handling player died event", error=str(e), exc_info=True)

    async def _handle_player_hp_decay(self, event: Any) -> None:
        """
        Handle player HP decay events by sending decay notification to the client.

        Args:
            event: The PlayerHPDecayEvent containing HP decay information
        """
        try:
            player_id_str = event.player_id

            # Send personal message to the player
            from .envelope import build_event

            decay_event = build_event(
                "player_hp_decay",
                {
                    "player_id": player_id_str,
                    "old_hp": event.old_hp,
                    "new_hp": event.new_hp,
                    "decay_amount": event.decay_amount,
                    "room_id": event.room_id,
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, decay_event)

            self._logger.debug("Sent HP decay notification to player", player_id=player_id_str, new_hp=event.new_hp)

        except Exception as e:
            self._logger.error("Error handling player HP decay event", error=str(e), exc_info=True)

    async def _handle_player_respawned(self, event: Any) -> None:
        """
        Handle player respawn events by sending respawn notification to the client.

        Args:
            event: The PlayerRespawnedEvent containing respawn information
        """
        try:
            player_id_str = event.player_id

            # Send personal message to the player
            from .envelope import build_event

            respawn_event = build_event(
                "player_respawned",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "respawn_room_id": event.respawn_room_id,
                    "old_hp": event.old_hp,
                    "new_hp": event.new_hp,
                    "message": "The sanitarium calls you back from the threshold. You have been restored to life.",
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, respawn_event)

            self._logger.info(
                "Sent respawn notification to player",
                player_id=player_id_str,
                respawn_room=event.respawn_room_id,
            )

        except Exception as e:
            self._logger.error("Error handling player respawn event", error=str(e), exc_info=True)


# AI Agent: Global singleton removed - use ApplicationContainer.real_time_event_handler instead
# Migration complete: All code now uses dependency injection via container
