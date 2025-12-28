"""
Real-time event handler for MythosMUD.

This module provides the RealTimeEventHandler class that bridges EventBus events
to real-time communication, enabling players to see each other in the game world.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.

Refactored to delegate to specialized modules for better maintainability.
"""

import uuid
from typing import Any

from ..events import EventBus
from ..events.event_types import (
    NPCEnteredRoom,
    NPCLeftRoom,
    PlayerDeliriumRespawnedEvent,
    PlayerDiedEvent,
    PlayerDPDecayEvent,
    PlayerDPUpdated,
    PlayerEnteredRoom,
    PlayerLeftRoom,
    PlayerRespawnedEvent,
)
from ..structured_logging.enhanced_logging_config import get_logger
from ..services.chat_logger import chat_logger
from ..services.player_combat_service import PlayerXPAwardEvent
from ..services.room_sync_service import get_room_sync_service
from .message_builders import MessageBuilder
from .npc_event_handlers import NPCEventHandler
from .player_event_handlers import PlayerEventHandler
from .player_name_utils import PlayerNameExtractor
from .room_occupant_manager import RoomOccupantManager


class RealTimeEventHandler:
    """
    Bridges EventBus events to real-time communication.

    This class subscribes to game events and converts them into real-time
    messages that are broadcast to connected clients. It serves as the
    critical link between the event system and the real-time communication
    layer.

    Refactored to delegate to specialized handler modules for better
    maintainability and reduced complexity.
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
        self.connection_manager = connection_manager
        self._logger = get_logger("RealTimeEventHandler")
        self._sequence_counter = 0

        # Task registry for tracking child tasks spawned by event broadcasting
        self.task_registry = task_registry

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        # Room synchronization service for enhanced event processing
        self.room_sync_service = get_room_sync_service()

        # Initialize specialized modules (after setting up sequence counter)
        self._initialize_modules()

        # Subscribe to relevant game events
        self._subscribe_to_events()

        self._logger.info("RealTimeEventHandler initialized with modular architecture")

    def _initialize_modules(self) -> None:
        """Initialize specialized handler modules."""
        # Player name extraction utilities
        self.name_extractor = PlayerNameExtractor()

        # Room occupant management
        self.occupant_manager = RoomOccupantManager(self.connection_manager, self.name_extractor)

        # Message building utilities
        self.message_builder = MessageBuilder(self._get_next_sequence)

        # Player event handler
        self.player_handler = PlayerEventHandler(
            connection_manager=self.connection_manager,
            room_sync_service=self.room_sync_service,
            chat_logger=self.chat_logger,
            task_registry=self.task_registry,
            message_builder=self.message_builder,
            name_extractor=self.name_extractor,
            occupant_manager=self.occupant_manager,
        )

        # NPC event handler (needs send_occupants_update callback)
        # Create a bound method reference for the callback
        self.npc_handler = NPCEventHandler(
            connection_manager=self.connection_manager,
            task_registry=self.task_registry,
            message_builder=self.message_builder,
            send_occupants_update=self._send_room_occupants_update_internal,
        )

    def _get_next_sequence(self) -> int:
        """Get the next sequence number for events."""
        self._sequence_counter += 1
        return self._sequence_counter

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left)
        self.event_bus.subscribe(PlayerXPAwardEvent, self._handle_player_xp_awarded)
        self.event_bus.subscribe(PlayerDPUpdated, self._handle_player_dp_updated)

        # Log subscription for debugging
        self._logger.info(
            "Subscribed to game events",
            event_types=[
                "PlayerEnteredRoom",
                "PlayerLeftRoom",
                "NPCEnteredRoom",
                "NPCLeftRoom",
                "PlayerXPAwardEvent",
                "PlayerDPUpdated",
            ],
            event_bus_id=id(self.event_bus),
        )

        # Subscribe to death/respawn events
        self.event_bus.subscribe(PlayerDiedEvent, self._handle_player_died)
        self.event_bus.subscribe(PlayerDPDecayEvent, self._handle_player_dp_decay)
        self.event_bus.subscribe(PlayerRespawnedEvent, self._handle_player_respawned)
        self.event_bus.subscribe(PlayerDeliriumRespawnedEvent, self._handle_player_delirium_respawned)

        self._logger.info("Subscribed to all player and NPC events")

    # Event handler delegation methods
    async def _handle_player_entered(self, event: PlayerEnteredRoom) -> None:
        """Delegate player entered event to specialized handler."""
        await self.player_handler.handle_player_entered(event, self._send_room_occupants_update_internal)

    async def _handle_player_left(self, event: PlayerLeftRoom) -> None:
        """Delegate player left event to specialized handler."""
        await self.player_handler.handle_player_left(event, self._send_room_occupants_update_internal)

    async def _handle_npc_entered(self, event: NPCEnteredRoom) -> None:
        """Delegate NPC entered event to specialized handler."""
        await self.npc_handler.handle_npc_entered(event)

    async def _handle_npc_left(self, event: NPCLeftRoom) -> None:
        """Delegate NPC left event to specialized handler."""
        await self.npc_handler.handle_npc_left(event)

    async def _handle_player_xp_awarded(self, event: PlayerXPAwardEvent) -> None:
        """Delegate player XP awarded event to specialized handler."""
        await self.player_handler.handle_player_xp_awarded(event)

    async def _handle_player_dp_updated(self, event: PlayerDPUpdated) -> None:
        """Delegate player DP updated event to specialized handler."""
        await self.player_handler.handle_player_dp_updated(event)

    async def _handle_player_died(self, event: PlayerDiedEvent) -> None:
        """Delegate player died event to specialized handler."""
        await self.player_handler.handle_player_died(event)

    async def _handle_player_dp_decay(self, event: PlayerDPDecayEvent) -> None:
        """Delegate player DP decay event to specialized handler."""
        await self.player_handler.handle_player_dp_decay(event)

    async def _handle_player_respawned(self, event: PlayerRespawnedEvent) -> None:
        """Delegate player respawned event to specialized handler."""
        await self.player_handler.handle_player_respawned(event)

    async def _handle_player_delirium_respawned(self, event: PlayerDeliriumRespawnedEvent) -> None:
        """Delegate player delirium respawned event to specialized handler."""
        await self.player_handler.handle_player_delirium_respawned(event)

    # Internal method for NPC handler callback (defined before NPC handler initialization)
    async def _send_room_occupants_update_internal(self, room_id: str, exclude_player: str | None = None) -> None:
        """
        Internal implementation for sending room occupants update.

        This method is used as a callback for the NPC handler and is also
        called by the public send_room_occupants_update method.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        try:
            # Get room occupants with structured data
            occupants_info: list[dict[str, Any] | str] = await self.occupant_manager.get_room_occupants(room_id)

            # Separate players and NPCs while maintaining backward compatibility
            players, npcs, all_occupants = self.occupant_manager.separate_occupants_by_type(occupants_info, room_id)

            # Convert room_id to string for JSON serialization
            room_id_str = str(room_id) if room_id else ""

            # Log what we're about to send
            self._logger.debug(
                "Sending room_occupants event",
                room_id=room_id_str,
                players=players,
                npcs=npcs,
                all_occupants=all_occupants,
                players_count=len(players),
                npcs_count=len(npcs),
            )

            # Build and send the message
            message = self.message_builder.build_occupants_update_message(room_id_str, players, npcs, all_occupants)
            await self.connection_manager.broadcast_to_room(room_id, message, exclude_player=exclude_player)

        except (ValueError, TypeError, KeyError, AttributeError, RuntimeError) as e:
            self._logger.error("Error sending room occupants update", error=str(e), exc_info=True)

    # Public API methods (called externally)
    async def send_room_occupants_update(self, room_id: str, exclude_player: str | None = None) -> None:
        """
        Send room occupants update to players in the room (public API).

        Preserves player/NPC distinction by sending structured data with separate
        players and npcs arrays, enabling the client UI to display them in separate columns.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        await self._send_room_occupants_update_internal(room_id, exclude_player)

    async def _get_room_occupants(self, room_id: str) -> list[dict[str, Any] | str]:
        """
        Get room occupants (public API for backward compatibility).

        Args:
            room_id: The room ID

        Returns:
            List of occupant information dictionaries or strings
        """
        return await self.occupant_manager.get_room_occupants(room_id)

    def _create_player_entered_message(self, event: PlayerEnteredRoom, player_name: str) -> dict[str, Any]:
        """
        Create player entered message (public API for tests).

        Args:
            event: The PlayerEnteredRoom event
            player_name: The player's name

        Returns:
            Message dictionary
        """
        return self.message_builder.create_player_entered_message(event, player_name)

    def _create_player_left_message(self, event: PlayerLeftRoom, player_name: str) -> dict[str, Any]:
        """
        Create player left message (public API for tests).

        Args:
            event: The PlayerLeftRoom event
            player_name: The player's name

        Returns:
            Message dictionary
        """
        return self.message_builder.create_player_left_message(event, player_name)

    async def _send_occupants_snapshot_to_player(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Send occupants snapshot to a specific player (public API for websocket_handler).

        Args:
            player_id: The player's ID
            room_id: The room ID
        """
        # Delegate to player handler's public method
        await self.player_handler.send_occupants_snapshot_to_player(player_id, room_id)

    def shutdown(self) -> None:
        """Shutdown the event handler."""
        self._logger.info("Shutting down RealTimeEventHandler")
        # Note: EventBus will handle its own shutdown
