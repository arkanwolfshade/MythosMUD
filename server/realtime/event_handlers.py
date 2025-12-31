"""
Event handlers for NATS message handler.

This module handles all event-type messages from NATS and broadcasts them
to WebSocket clients.
"""

import uuid
from collections.abc import Callable
from typing import Any

from ..realtime.envelope import build_event
from ..services.nats_exceptions import NATSError
from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger("communications.event_handlers")


class EventHandler:
    """Handler for NATS event messages."""

    def __init__(self, connection_manager):
        """
        Initialize event handler.

        Args:
            connection_manager: ConnectionManager instance for broadcasting
        """
        self.connection_manager = connection_manager

    def get_event_handler_map(self) -> dict[str, Callable[[dict[str, Any]], Any]]:
        """
        Get mapping of event types to their handler methods.

        Returns:
            Dictionary mapping event_type strings to handler coroutine methods
        """
        return {
            "player_entered": self.handle_player_entered_event,
            "player_left": self.handle_player_left_event,
            "game_tick": self.handle_game_tick_event,
            "combat_started": self.handle_combat_started_event,
            "combat_ended": self.handle_combat_ended_event,
            "player_attacked": self.handle_player_attacked_event,
            "npc_attacked": self.handle_npc_attacked_event,
            "npc_took_damage": self.handle_npc_took_damage_event,
            "npc_died": self.handle_npc_died_event,
        }

    def validate_event_message(self, event_type: str | None, data: dict[str, Any]) -> bool:
        """
        Validate that event message has required fields.

        Args:
            event_type: Event type string
            data: Event data dictionary

        Returns:
            True if valid, False otherwise
        """
        if not event_type or not data:
            logger.warning("Invalid event message - missing required fields", event_type=event_type, data=data)
            return False
        return True

    async def handle_event_message(self, message_data: dict[str, Any]):
        """
        Handle incoming event messages from NATS.

        Args:
            message_data: Event message data from NATS
        """
        try:
            logger.info("Handling event message", message_data=message_data)

            # Extract event details
            event_type = message_data.get("event_type")
            data = message_data.get("event_data", {})

            # Debug logging for all messages
            logger.debug("NATS message received", event_type=event_type, data=data)

            # Validate required fields
            if not self.validate_event_message(event_type, data):
                return

            # Type narrowing: validate_event_message ensures event_type is not None
            assert event_type is not None, "event_type should not be None after validation"
            event_type_str: str = event_type

            # Route event based on type using dispatch map
            handler_map = self.get_event_handler_map()
            handler = handler_map.get(event_type_str)

            if handler:
                # Special handling for npc_attacked event (has additional logging)
                if event_type_str == "npc_attacked":
                    logger.debug("NPC attacked event received in NATS handler", data=data)
                await handler(data)
            else:
                logger.debug("Unknown event type received", event_type=event_type_str)

        except NATSError as e:
            logger.error("Error handling event message", error=str(e), message_data=message_data)

    async def handle_player_entered_event(self, data: dict[str, Any]):
        """
        Handle player_entered event.

        Args:
            data: Event data containing player and room information
        """
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player entered event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("player_entered", room_id, data)

            logger.debug(
                "Player entered event broadcasted",
                room_id=room_id,
                player_id=data.get("player_id"),
            )

        except NATSError as e:
            logger.error("Error handling player entered event", error=str(e), data=data)

    async def handle_player_left_event(self, data: dict[str, Any]):
        """
        Handle player_left event.

        Args:
            data: Event data containing player and room information
        """
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player left event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("player_left", room_id, data)

            logger.debug(
                "Player left event broadcasted",
                room_id=room_id,
                player_id=data.get("player_id"),
            )

        except NATSError as e:
            logger.error("Error handling player left event", error=str(e), data=data)

    async def handle_game_tick_event(self, data: dict[str, Any]):
        """
        Handle game_tick event.

        Args:
            data: Event data containing tick information
        """
        try:
            # Broadcast globally using injected connection_manager
            await self.connection_manager.broadcast_global_event("game_tick", data)

            logger.debug(
                "Game tick event broadcasted",
                tick_number=data.get("tick_number"),
            )

        except NATSError as e:
            logger.error("Error handling game tick event", error=str(e), data=data)

    async def handle_combat_started_event(self, data: dict[str, Any]):
        """Handle combat_started event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Combat started event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("combat_started", room_id, data)
            logger.debug("Combat started event broadcasted", room_id=room_id)

            # Send player updates with in_combat status to all players in combat
            participants = data.get("participants", {})
            if participants:
                for participant_id_str, _participant_data in participants.items():
                    try:
                        # Get player by ID to send update
                        participant_id_uuid = (
                            uuid.UUID(participant_id_str) if isinstance(participant_id_str, str) else participant_id_str
                        )
                        player = await self.connection_manager.get_player(participant_id_uuid)
                        if player:
                            # Send player update with in_combat status
                            player_update_event = build_event(
                                "player_update",
                                {
                                    "player_id": participant_id_str,
                                    "in_combat": True,
                                },
                                player_id=participant_id_str,
                            )
                            await self.connection_manager.send_personal_message(participant_id_str, player_update_event)
                            logger.debug("Sent player update with in_combat=True", player_id=participant_id_str)
                    except (NATSError, RuntimeError) as e:
                        logger.warning(
                            "Error sending player update for combat start", player_id=participant_id_str, error=str(e)
                        )

        except NATSError as e:
            logger.error("Error handling combat started event", error=str(e), data=data)

    async def handle_combat_ended_event(self, data: dict[str, Any]):
        """Handle combat_ended event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Combat ended event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("combat_ended", room_id, data)
            logger.debug("Combat ended event broadcasted", room_id=room_id)

            # Send player updates with in_combat status to all players who were in combat
            participants = data.get("participants", {})
            if participants:
                for participant_id_str in participants:
                    try:
                        # Get player by ID to send update
                        participant_id_uuid = (
                            uuid.UUID(participant_id_str) if isinstance(participant_id_str, str) else participant_id_str
                        )
                        player = await self.connection_manager.get_player(participant_id_uuid)
                        if player:
                            # Send player update with in_combat status
                            player_update_event = build_event(
                                "player_update",
                                {
                                    "player_id": participant_id_str,
                                    "in_combat": False,
                                },
                                player_id=participant_id_str,
                            )
                            await self.connection_manager.send_personal_message(participant_id_str, player_update_event)
                            logger.debug("Sent player update with in_combat=False", player_id=participant_id_str)
                    except (NATSError, RuntimeError) as e:
                        logger.warning(
                            "Error sending player update for combat end", player_id=participant_id_str, error=str(e)
                        )

        except NATSError as e:
            logger.error("Error handling combat ended event", error=str(e), data=data)

    async def handle_player_attacked_event(self, data: dict[str, Any]):
        """Handle player_attacked event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("Player attacked event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("player_attacked", room_id, data)
            logger.debug("Player attacked event broadcasted", room_id=room_id)

        except NATSError as e:
            logger.error("Error handling player attacked event", error=str(e), data=data)

    async def handle_npc_attacked_event(self, data: dict[str, Any]):
        """Handle npc_attacked event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("NPC attacked event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("npc_attacked", room_id, data)
            logger.debug("NPC attacked event broadcasted", room_id=room_id)

        except NATSError as e:
            logger.error("Error handling NPC attacked event", error=str(e), data=data)

    async def handle_npc_took_damage_event(self, data: dict[str, Any]):
        """Handle npc_took_damage event."""
        try:
            room_id = data.get("room_id")
            if not room_id:
                logger.warning("NPC took damage event missing room_id", data=data)
                return

            # Broadcast to room using injected connection_manager
            await self.connection_manager.broadcast_room_event("npc_took_damage", room_id, data)
            logger.debug("NPC took damage event broadcasted", room_id=room_id)

        except NATSError as e:
            logger.error("Error handling NPC took damage event", error=str(e), data=data)

    async def handle_npc_died_event(self, data: dict[str, Any]):
        """
        Handle npc_died event - NATS to EventBus bridge pattern.

        ARCHITECTURE NOTE - Dual Event Path by Design:
        This handler implements the NATS→EventBus bridge pattern, which is NOT redundant:

        1. NATS Path (Inter-Service Communication):
           - CombatService publishes NPCDiedEvent → NATS → NATSMessageHandler (here)
           - Purpose: Broadcast death to WebSocket clients for UI updates

        2. EventBus Path (Internal Game Logic):
           - NATSMessageHandler publishes NPCDied → EventBus → NPCLifecycleManager
           - Purpose: Trigger respawn queue processing with configured delay

        This separation of concerns follows NATS.mdc best practices:
        - NATS handles distributed messaging and client broadcasting
        - EventBus handles internal domain logic and game state management
        - Bridge pattern prevents tight coupling between communication and domain layers

        AI Agent: This is the ONLY place that bridges NATS npc_died messages to EventBus.
                  CombatService publishes to NATS only, not EventBus directly.
                  Removing this bridge would break NPC respawning entirely!

        Note: NPC removal from room is handled by the NPCLeftRoom event published
        by the lifecycle manager. This handler broadcasts the death event to clients
        AND publishes to EventBus for respawn queue processing.
        """
        try:
            room_id = data.get("room_id")
            npc_id = data.get("npc_id")
            npc_name = data.get("npc_name")

            if not room_id:
                logger.warning("NPC died event missing room_id", data=data)
                return

            if not npc_id:
                logger.warning("NPC died event missing npc_id", data=data)
                return

            # Import here to avoid circular imports
            from server.events.event_types import NPCDied

            # Broadcast death event to room clients using injected connection_manager
            # AI: Room state mutation is handled by NPCLeftRoom event from lifecycle manager
            # AI: This prevents duplicate removal attempts and maintains single source of truth
            await self.connection_manager.broadcast_room_event("npc_died", room_id, data)
            logger.debug("NPC died event broadcasted", room_id=room_id, npc_id=npc_id, npc_name=npc_name)

            # AI Agent: CRITICAL - Publish to EventBus so lifecycle manager can queue for respawn
            #           This ensures ALL NPCs (required and optional) respect respawn delay
            event_bus = self.connection_manager.event_bus
            if event_bus:
                npc_died_event = NPCDied(npc_id=str(npc_id), room_id=room_id, cause=data.get("cause", "combat"))
                event_bus.publish(npc_died_event)
                logger.info(
                    "NPCDied event published to EventBus for respawn queue",
                    npc_id=npc_id,
                    npc_name=npc_name,
                )

        except NATSError as e:
            logger.error("Error handling NPC died event", error=str(e), data=data)
