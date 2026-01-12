"""
NPC event handlers for real-time communication.

This module handles all NPC-related events (entered, left).

As documented in "NPC Event Propagation Protocols" - Dr. Armitage, 1928
"""

import asyncio
import uuid
from typing import Any, cast

from ..app.tracked_task_manager import get_global_tracked_manager
from ..events.event_types import NPCEnteredRoom, NPCLeftRoom
from ..structured_logging.enhanced_logging_config import get_logger
from .message_builders import MessageBuilder


class NPCEventHandler:
    """Handles all NPC-related real-time events."""

    def __init__(
        self,
        connection_manager: Any,
        task_registry: Any | None,
        message_builder: MessageBuilder,
        send_occupants_update: Any,
    ) -> None:
        """
        Initialize the NPC event handler.

        Args:
            connection_manager: ConnectionManager instance
            task_registry: Optional TaskRegistry instance
            message_builder: MessageBuilder instance
            send_occupants_update: Callable to send room occupants update
        """
        self.connection_manager = connection_manager
        self.task_registry = task_registry
        self.message_builder = message_builder
        self.send_occupants_update = send_occupants_update
        self._logger = get_logger("NPCEventHandler")

    def _get_npc_instance(self, npc_id: str) -> Any | None:
        """
        Get NPC instance from lifecycle manager.

        Args:
            npc_id: The NPC ID

        Returns:
            NPC instance or None if not found
        """
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return None

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
                return None

            return lifecycle_manager.active_npcs[npc_id]
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC instance retrieval errors unpredictable, must return None
            self._logger.debug("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    def _get_behavior_config_from_instance(self, npc_instance: Any) -> Any | None:
        """
        Extract behavior_config from NPC instance.

        Args:
            npc_instance: The NPC instance

        Returns:
            Behavior config or None if not found
        """
        # Try private attribute first
        behavior_config = getattr(npc_instance, "_behavior_config", None)
        if behavior_config:
            return behavior_config

        # Try public method
        if hasattr(npc_instance, "get_behavior_config"):
            behavior_config = npc_instance.get_behavior_config()
            if behavior_config:
                return behavior_config

        # Try public attribute as fallback
        return getattr(npc_instance, "behavior_config", None)

    def _parse_behavior_config(self, behavior_config: Any) -> dict[str, Any] | None:
        """
        Parse behavior_config if it's a JSON string.

        Args:
            behavior_config: The behavior config (string or dict)

        Returns:
            Parsed config dict or None if parsing fails
        """
        if not isinstance(behavior_config, str):
            return behavior_config if isinstance(behavior_config, dict) else None

        import json

        try:
            return json.loads(behavior_config)
        except (json.JSONDecodeError, ValueError):
            return None

    def _extract_spawn_message_from_config(self, behavior_config: dict[str, Any]) -> str | None:
        """
        Extract spawn_message from behavior_config.

        Args:
            behavior_config: The parsed behavior config dict

        Returns:
            Spawn message string or None if not found
        """
        spawn_message = behavior_config.get("spawn_message")
        return cast(str, spawn_message) if spawn_message else None

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
            npc_instance = self._get_npc_instance(npc_id)
            if not npc_instance:
                return None

            npc_name = getattr(npc_instance, "name", "An NPC")
            behavior_config = self._get_behavior_config_from_instance(npc_instance)

            if not behavior_config:
                return f"{npc_name} appears."

            parsed_config = self._parse_behavior_config(behavior_config)
            if not parsed_config:
                return f"{npc_name} appears."

            spawn_message = self._extract_spawn_message_from_config(parsed_config)
            return spawn_message if spawn_message else f"{npc_name} appears."

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC spawn message retrieval errors unpredictable, must return None
            self._logger.debug("Error getting NPC spawn message", npc_id=npc_id, error=str(e))
            return None

    def _get_npc_name(self, npc_id: str) -> str | None:
        """
        Get the name of an NPC by ID.

        Args:
            npc_id: The NPC ID

        Returns:
            NPC name or None if not found
        """
        try:
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return None

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
                return None

            npc_instance = lifecycle_manager.active_npcs[npc_id]
            npc_name = getattr(npc_instance, "name", None)
            return npc_name if npc_name else None
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC name retrieval errors unpredictable, must return None
            self._logger.debug("Error getting NPC name", npc_id=npc_id, error=str(e))
            return None

    async def _determine_direction_from_rooms(self, from_room_id: str, to_room_id: str) -> str | None:
        """
        Determine the direction from one room to another by checking room exits.

        Args:
            from_room_id: Source room ID
            to_room_id: Destination room ID

        Returns:
            Direction string (e.g., "north", "south") or None if not found
        """
        try:
            async_persistence = self.connection_manager.async_persistence
            if not async_persistence:
                return None

            from_room = async_persistence.get_room_by_id(from_room_id)  # Sync method, uses cache
            if not from_room:
                return None

            # Check each exit to find the one that leads to to_room_id
            for direction, target_room_id in from_room.exits.items():
                if target_room_id == to_room_id:
                    return direction

            return None
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Direction determination errors unpredictable, must return None
            self._logger.debug(
                "Error determining direction from rooms", error=str(e), from_room=from_room_id, to_room=to_room_id
            )
            return None

    def _get_npc_departure_message(self, npc_id: str) -> str | None:
        """
        Get the departure message for an NPC from its behavior_config.

        If no custom departure message is defined, returns a default message: "<npc-name> leaves."

        Args:
            npc_id: The NPC ID

        Returns:
            Departure message (custom or default), or None if NPC not found
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
            behavior_config = getattr(npc_instance, "_behavior_config", None)
            if not behavior_config:
                # Try alternative attribute name
                behavior_config = getattr(npc_instance, "behavior_config", None)

            if behavior_config:
                # Parse the behavior_config if it's a JSON string
                import json

                if isinstance(behavior_config, str):
                    try:
                        behavior_config = json.loads(behavior_config)
                    except (json.JSONDecodeError, ValueError):
                        # If parsing fails, use default message
                        return f"{npc_name} leaves."

                # Get the departure_message from the behavior_config
                departure_message = behavior_config.get("departure_message")
                if departure_message:
                    return cast(str, departure_message)

            # Return default message if no custom message is defined
            return f"{npc_name} leaves."

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC departure message retrieval errors unpredictable, must return None
            self._logger.debug("Error getting NPC departure message", npc_id=npc_id, error=str(e))
            return None

    async def _send_room_message(self, room_id: str, message: str, message_type: str = "npc_spawn") -> None:
        """
        Send a message to all players in a room.

        Args:
            room_id: The room ID
            message: The message to send
            message_type: Type of message (default: "npc_spawn", use "system" for movement messages)
        """
        try:
            # Get all players in the room using room_manager (same as broadcast_to_room)
            from .envelope import build_event

            # Use room_manager.get_room_subscribers() instead of room._players
            # room._players may not be accurate as Room instances are recreated from persistence
            # room_manager tracks actual online players in rooms
            if not self.connection_manager or not hasattr(self.connection_manager, "room_manager"):
                self._logger.warning(
                    "Connection manager or room manager not available for sending room message", room_id=room_id
                )
                return

            # Get all player IDs subscribed to this room (as strings, same as broadcast_to_room)
            player_ids_str = await self.connection_manager.room_manager.get_room_subscribers(room_id)
            player_ids = [
                uuid.UUID(pid_str) for pid_str in player_ids_str
            ]  # Convert to UUIDs for send_personal_message

            # Send the message to each player in the room
            for player_id in player_ids:
                # Create the message event
                message_event = build_event(
                    "room_message",
                    {
                        "message": message,
                        "room_id": room_id,
                        "message_type": message_type,
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
                            self.connection_manager.send_personal_message(
                                player_id,
                                message_event,
                            ),
                            f"event_handler/room_message_{room_id}_{player_id}",
                            "event_handler",
                        )
                    else:
                        tracked_manager = get_global_tracked_manager()
                        tracked_manager.create_tracked_task(
                            self.connection_manager.send_personal_message(
                                player_id,
                                message_event,
                            ),
                            task_name=f"event_handler/room_message_{room_id}_{player_id}",
                            task_type="event_handler",
                        )
                except RuntimeError:
                    # No running event loop - log and skip async operation
                    self._logger.debug("No event loop available for room message broadcast")

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Room message sending errors unpredictable, must handle gracefully
            self._logger.error("Error sending room message", room_id=room_id, error=str(e), exc_info=True)

    async def handle_npc_entered(self, event: NPCEnteredRoom) -> None:
        """
        Handle NPC entering a room.

        This method broadcasts NPC appearance and triggers occupant updates.
        Room state (NPC presence) is mutated only by domain sources (e.g., Room.npc_entered).

        Args:
            event: NPCEnteredRoom event containing NPC and room information
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping NPC entered event",
                npc_id=event.npc_id,
                room_id=event.room_id,
            )
            return

        try:
            self._logger.info("NPC entered room", npc_id=event.npc_id, room_id=event.room_id)

            # Get the room from async persistence
            async_persistence = self.connection_manager.async_persistence
            if not async_persistence:
                self._logger.warning("Async persistence layer not available for NPC room entry")
                return

            room = async_persistence.get_room_by_id(event.room_id)  # Sync method, uses cache
            if not room:
                self._logger.warning("Room not found for NPC entry", room_id=event.room_id)
                return

            # Get NPC name for movement messages
            npc_name = self._get_npc_name(event.npc_id)
            if not npc_name:
                npc_name = "An NPC"

            # Check if this is a movement (has from_room_id) or a spawn (no from_room_id)
            if event.from_room_id:
                # This is a movement - create directional message
                direction = await self._determine_direction_from_rooms(event.from_room_id, event.room_id)
                movement_message = self.message_builder.create_npc_movement_message(npc_name, direction, "entered")
                # Send movement message to all players in the room as system message
                await self._send_room_message(event.room_id, movement_message, message_type="system")
            else:
                # This is a spawn - use spawn message from behavior_config
                spawn_message = self._get_npc_spawn_message(event.npc_id)
                if spawn_message:
                    # Send the spawn message to all players in the room
                    await self._send_room_message(event.room_id, spawn_message)

            # Schedule room update broadcast (async operation)
            try:
                # Use get_running_loop() instead of deprecated get_event_loop()
                # get_running_loop() raises RuntimeError if no loop is running
                _ = asyncio.get_running_loop()  # Verify loop exists
                # Schedule the async operation to run later
                if self.task_registry:
                    self.task_registry.register_task(
                        self.send_occupants_update(event.room_id),
                        f"event_handler/room_occupants_{event.room_id}",
                        "event_handler",
                    )
                else:
                    # Task 4.4: Replace with tracked task creation to prevent memory leaks
                    tracked_manager = get_global_tracked_manager()
                    tracked_manager.create_tracked_task(
                        self.send_occupants_update(event.room_id),
                        task_name=f"event_handler/room_occupants_{event.room_id}",
                        task_type="event_handler",
                    )
            except RuntimeError:
                # No running event loop - log and skip async operation
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug("Processed NPC entered event", npc_id=event.npc_id, room_id=event.room_id)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC entered event handling errors unpredictable, must handle gracefully
            self._logger.error("Error handling NPC entered room event", error=str(e), exc_info=True)

    async def handle_npc_left(self, event: NPCLeftRoom) -> None:
        """
        Handle NPC leaving a room.

        This method broadcasts NPC departure and triggers occupant updates.
        Room state is mutated by domain sources only.

        Args:
            event: NPCLeftRoom event containing NPC and room information
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping NPC left event", npc_id=event.npc_id, room_id=event.room_id
            )
            return

        try:
            self._logger.info("NPC left room", npc_id=event.npc_id, room_id=event.room_id)

            # Get the room from async persistence
            async_persistence = self.connection_manager.async_persistence
            if not async_persistence:
                self._logger.warning("Async persistence layer not available for NPC room exit")
                return

            room = async_persistence.get_room_by_id(event.room_id)  # Sync method, uses cache
            if not room:
                self._logger.warning("Room not found for NPC exit", room_id=event.room_id)
                return

            # Get NPC name for movement messages
            npc_name = self._get_npc_name(event.npc_id)
            if not npc_name:
                npc_name = "An NPC"

            # Check if this is a movement (has to_room_id) or a departure (no to_room_id)
            if event.to_room_id:
                # This is a movement - create directional message
                direction = await self._determine_direction_from_rooms(event.room_id, event.to_room_id)
                movement_message = self.message_builder.create_npc_movement_message(npc_name, direction, "left")
                # Send movement message to all players in the room as system message
                await self._send_room_message(event.room_id, movement_message, message_type="system")
            else:
                # This is a departure (not movement) - use departure message from behavior_config
                departure_message = self._get_npc_departure_message(event.npc_id)
                if departure_message:
                    # Send the departure message to all players in the room
                    await self._send_room_message(event.room_id, departure_message)

            # Schedule room update broadcast (async operation)
            try:
                # Use get_running_loop() instead of deprecated get_event_loop()
                # get_running_loop() raises RuntimeError if no loop is running
                _ = asyncio.get_running_loop()  # Verify loop exists
                # Schedule the async operation to run later
                if self.task_registry:
                    self.task_registry.register_task(
                        self.send_occupants_update(event.room_id),
                        f"event_handler/room_occupants_{event.room_id}",
                        "event_handler",
                    )
                else:
                    # Task 4.4: Replace with tracked task creation to prevent memory leaks
                    tracked_manager = get_global_tracked_manager()
                    tracked_manager.create_tracked_task(
                        self.send_occupants_update(event.room_id),
                        task_name=f"event_handler/room_occupants_{event.room_id}",
                        task_type="event_handler",
                    )
            except RuntimeError:
                # No running event loop - log and skip async operation
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug("Processed NPC left event", npc_id=event.npc_id, room_id=event.room_id)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC left event handling errors unpredictable, must handle gracefully
            self._logger.error("Error handling NPC left room event", error=str(e), exc_info=True)
