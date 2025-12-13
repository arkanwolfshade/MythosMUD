"""
Player event handlers for real-time communication.

This module handles all player-related events (entered, left, XP, DP, death, respawn).

As documented in "Player Event Propagation Protocols" - Dr. Armitage, 1928
"""

from typing import Any

from ..events.event_types import PlayerDPUpdated, PlayerEnteredRoom, PlayerLeftRoom
from ..logging.enhanced_logging_config import get_logger
from ..services.player_combat_service import PlayerXPAwardEvent
from .message_builders import MessageBuilder
from .player_event_handlers_respawn import PlayerRespawnEventHandler
from .player_event_handlers_room import PlayerRoomEventHandler
from .player_event_handlers_state import PlayerStateEventHandler
from .player_event_handlers_utils import PlayerEventHandlerUtils
from .player_name_utils import PlayerNameExtractor
from .room_occupant_manager import RoomOccupantManager


class PlayerEventHandler:
    """Handles all player-related real-time events."""

    def __init__(
        self,
        connection_manager: Any,
        room_sync_service: Any,
        chat_logger: Any,
        task_registry: Any | None,
        message_builder: MessageBuilder,
        name_extractor: PlayerNameExtractor,
        occupant_manager: RoomOccupantManager,
    ) -> None:
        """
        Initialize the player event handler.

        Args:
            connection_manager: ConnectionManager instance
            room_sync_service: RoomSyncService instance
            chat_logger: ChatLogger instance
            task_registry: Optional TaskRegistry instance
            message_builder: MessageBuilder instance
            name_extractor: PlayerNameExtractor instance
            occupant_manager: RoomOccupantManager instance
        """
        self.connection_manager = connection_manager
        self.room_sync_service = room_sync_service
        self.chat_logger = chat_logger
        self.task_registry = task_registry
        self.message_builder = message_builder
        self.name_extractor = name_extractor
        self.occupant_manager = occupant_manager
        self._logger = get_logger("PlayerEventHandler")
        self._initialize_handlers()

    def _initialize_handlers(self) -> None:
        """Initialize utility functions and specialized handlers."""
        self._utils = PlayerEventHandlerUtils(self.connection_manager, self.name_extractor, self._logger)
        self._room_handler = PlayerRoomEventHandler(
            connection_manager=self.connection_manager,
            room_sync_service=self.room_sync_service,
            chat_logger=self.chat_logger,
            message_builder=self.message_builder,
            name_extractor=self.name_extractor,
            occupant_manager=self.occupant_manager,
            utils=self._utils,
            logger=self._logger,
        )
        self._state_handler = PlayerStateEventHandler(
            connection_manager=self.connection_manager,
            utils=self._utils,
            logger=self._logger,
        )
        self._respawn_handler = PlayerRespawnEventHandler(
            connection_manager=self.connection_manager,
            utils=self._utils,
            logger=self._logger,
        )

    # Room-related methods (delegated to room handler)
    async def handle_player_entered(self, event: PlayerEnteredRoom, send_occupants_update: Any | None = None) -> None:
        """
        Handle player entering a room with enhanced synchronization.

        Args:
            event: The PlayerEnteredRoom event
            send_occupants_update: Optional callable to send room occupants update
        """
        await self._room_handler.handle_player_entered(event, send_occupants_update)

    async def handle_player_left(self, event: PlayerLeftRoom, send_occupants_update: Any) -> None:
        """
        Handle player leaving a room with enhanced synchronization.

        Args:
            event: The PlayerLeftRoom event
            send_occupants_update: Callable to send room occupants update
        """
        await self._room_handler.handle_player_left(event, send_occupants_update)

    async def send_occupants_snapshot_to_player(self, player_id: Any, room_id: str) -> None:
        """
        Send occupants snapshot to a player.

        CRITICAL: This method MUST include NPCs when querying room occupants.
        This is the primary mechanism for updating the entering player's Occupants panel.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)
            room_id: The room ID
        """
        await self._room_handler.send_occupants_snapshot_to_player(player_id, room_id)

    # State update methods (delegated to state handler)
    async def handle_player_xp_awarded(self, event: PlayerXPAwardEvent) -> None:
        """
        Handle player XP award events by sending updates to the client.

        Args:
            event: The PlayerXPAwardEvent containing XP award information
        """
        await self._state_handler.handle_player_xp_awarded(event)

    async def handle_player_dp_updated(self, event: PlayerDPUpdated) -> None:
        """
        Handle player DP update events by sending updates to the client.

        Args:
            event: The PlayerDPUpdated event containing DP change information
        """
        await self._state_handler.handle_player_dp_updated(event)

    async def handle_player_died(self, event: Any) -> None:
        """
        Handle player death events by sending death notification to the client.

        Args:
            event: The PlayerDiedEvent containing death information
        """
        await self._state_handler.handle_player_died(event)

    async def handle_player_dp_decay(self, event: Any) -> None:
        """
        Handle player DP decay events by sending decay notification to the client.

        Args:
            event: The PlayerDPDecayEvent containing DP decay information
        """
        await self._state_handler.handle_player_dp_decay(event)

    # Respawn methods (delegated to respawn handler)
    async def handle_player_respawned(self, event: Any) -> None:
        """
        Handle player respawn events by sending respawn notification to the client.

        Args:
            event: The PlayerRespawnedEvent containing respawn information
        """
        await self._respawn_handler.handle_player_respawned(event)

    async def handle_player_delirium_respawned(self, event: Any) -> None:
        """
        Handle player delirium respawn events by sending respawn notification to the client.

        Args:
            event: The PlayerDeliriumRespawnedEvent containing delirium respawn information
        """
        await self._respawn_handler.handle_player_delirium_respawned(event)
