"""
Room occupant management utilities.

This module handles querying and processing room occupants (players and NPCs),
providing structured data for real-time updates.

As documented in "Dimensional Occupancy Tracking" - Dr. Armitage, 1929
"""

import uuid
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..structured_logging.enhanced_logging_config import get_logger
from .npc_occupant_processor import NPCOccupantProcessor
from .occupant_formatter import OccupantFormatter
from .player_name_utils import PlayerNameExtractor
from .player_occupant_processor import PlayerOccupantProcessor
from .room_id_utils import RoomIDUtils


class RoomOccupantManager:
    """
    Manages room occupant queries and processing.

    Handles both players and NPCs, providing structured occupant data
    for real-time communication.
    """

    def __init__(self, connection_manager: Any, name_extractor: PlayerNameExtractor | None = None) -> None:
        """
        Initialize the room occupant manager.

        Args:
            connection_manager: ConnectionManager instance
            name_extractor: Optional PlayerNameExtractor instance
        """
        self.connection_manager = connection_manager
        self.name_extractor = name_extractor or PlayerNameExtractor()
        self._logger = get_logger("RoomOccupantManager")

        # Initialize helper processors
        self.room_id_utils = RoomIDUtils(connection_manager)
        self.npc_processor = NPCOccupantProcessor(connection_manager, self.room_id_utils)
        self.player_processor = PlayerOccupantProcessor(connection_manager, self.name_extractor)
        self.formatter = OccupantFormatter()

    async def get_room_occupants(
        self, room_id: str, ensure_player_included: uuid.UUID | str | None = None
    ) -> list[dict[str, Any] | str]:
        """
        Get the list of occupants in a room.

        Args:
            room_id: The room ID
            ensure_player_included: Optional player ID to ensure is included even if not in room._players yet
                                   (used to handle race conditions during movement)

        Returns:
            list[dict]: List of occupant information
        """
        occupants: list[dict[str, Any] | str] = []

        # Defensive check: if no connection_manager, return empty list
        if not self.connection_manager:
            self._logger.debug("Connection manager not available, cannot get room occupants", room_id=room_id)
            return occupants

        try:
            # Get room from async persistence
            async_persistence = self.connection_manager.async_persistence
            if not async_persistence:
                return occupants

            room = async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
            if not room:
                return occupants

            # Get player IDs in the room (returns list[str])
            player_id_strings = room.get_players()

            # Process players
            player_occupants = await self.player_processor.process_players_for_occupants(
                room_id, player_id_strings, ensure_player_included
            )
            occupants.extend(player_occupants)

            # Query and process NPCs
            npc_ids = await self.npc_processor.query_npcs_for_room(room_id, room)
            npc_occupants = self.npc_processor.process_npcs_for_occupants(npc_ids)
            occupants.extend(npc_occupants)

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error getting room occupants", error=str(e), exc_info=True)

        return occupants

    def separate_occupants_by_type(
        self, occupants_info: list[dict[str, Any] | str], room_id: str
    ) -> tuple[list[str], list[str], list[str]]:
        """
        Separate occupants into players, NPCs, and all occupants lists.

        Args:
            occupants_info: List of occupant information dictionaries or strings
            room_id: Room ID for logging

        Returns:
            Tuple of (players, npcs, all_occupants) lists
        """
        return self.formatter.separate_occupants_by_type(occupants_info, room_id)
