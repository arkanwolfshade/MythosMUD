"""
Utility functions for player event handlers.

This module contains helper functions used across player event handling.
"""

import uuid
from typing import Any

from .disconnect_grace_period import is_player_in_grace_period
from .player_name_utils import PlayerNameExtractor


class PlayerEventHandlerUtils:
    """Utility functions for player event handling."""

    def __init__(self, connection_manager: Any, name_extractor: PlayerNameExtractor, logger: Any) -> None:
        """
        Initialize utility functions.

        Args:
            connection_manager: ConnectionManager instance
            name_extractor: PlayerNameExtractor instance
            logger: Logger instance
        """
        self.connection_manager = connection_manager
        self.name_extractor = name_extractor
        self._logger = logger

    def normalize_player_id(self, player_id: uuid.UUID | str) -> uuid.UUID | None:
        """
        Normalize player ID to UUID format.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)

        Returns:
            UUID object or None if conversion fails
        """
        try:
            return uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        except (ValueError, TypeError):
            self._logger.warning("Invalid player_id format, cannot convert to UUID", player_id=player_id)
            return None

    async def get_player_info(self, player_id: uuid.UUID | str) -> tuple[Any, str] | None:
        """
        Get player information and name (async version).

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)

        Returns:
            tuple: (player, player_name) or None if player not found
        """
        # Defensive check: if no connection_manager, cannot get player info
        if not self.connection_manager:
            self._logger.debug("Connection manager not available, cannot get player info", player_id=player_id)
            return None

        # Normalize player ID to UUID
        player_id_uuid = self.normalize_player_id(player_id)
        if not player_id_uuid:
            return None

        # Get player from connection manager
        player = await self.connection_manager.get_player(player_id_uuid)
        if not player:
            self._logger.warning("Player not found", player_id=player_id_uuid)
            return None

        # Extract and validate player name
        player_name = self.name_extractor.extract_player_name(player, player_id_uuid)
        player_name = self.name_extractor.validate_player_name_not_uuid(player_name, player_id_uuid, player)

        return (player, player_name)

    def normalize_event_ids(
        self, player_id: uuid.UUID | str | None, room_id: uuid.UUID | str | None
    ) -> tuple[str | None, str | None]:
        """
        Normalize event IDs to strings for comparison and logging.

        Args:
            player_id: The player ID (UUID or string)
            room_id: The room ID (UUID or string)

        Returns:
            Tuple of (exclude_player_id, room_id_str) as strings or None
        """
        exclude_player_id = str(player_id) if player_id else None
        room_id_str = str(room_id) if room_id else None
        return exclude_player_id, room_id_str

    def _extract_name_from_occupant(self, occ: dict[str, Any] | str) -> str | None:
        """
        Extract name from a single occupant entry.

        Args:
            occ: Occupant information (dict or str)

        Returns:
            Extracted name or None
        """
        if isinstance(occ, dict):
            return occ.get("player_name") or occ.get("npc_name") or occ.get("name")
        if isinstance(occ, str):
            return occ
        # Defensive return for unexpected types (unreachable in normal flow)
        return None  # type: ignore[unreachable]

    def extract_occupant_names(self, occupants_info: list[dict[str, Any] | str]) -> list[str]:
        """
        Extract occupant names from occupant information.

        Args:
            occupants_info: List of occupant information dictionaries or strings

        Returns:
            list: List of occupant names (validated to exclude UUIDs)
        """
        names: list[str] = []
        for occ in occupants_info or []:
            name = self._extract_name_from_occupant(occ)
            if name and self.name_extractor.is_valid_name_for_occupant(name):
                names.append(name)
        return names

    def add_valid_name_to_lists(
        self, name: str | None, players: list[str], npcs: list[str], all_occupants: list[str], is_player: bool = False
    ) -> None:
        """
        Add a valid name to the appropriate lists.

        Args:
            name: The name to validate and add
            players: List of player names
            npcs: List of NPC names
            all_occupants: Flat list of all occupants
            is_player: Whether this is a player name (True) or NPC name (False)
        """
        if not name or not self.name_extractor.is_valid_name_for_occupant(name):
            return

        # Type narrowing: is_valid_name_for_occupant returns True only for non-empty strings
        if not isinstance(name, str):
            raise TypeError("name must be str if is_valid_name_for_occupant returns True")

        if is_player:
            players.append(name)
        else:
            npcs.append(name)
        all_occupants.append(name)

    def process_dict_occupant(
        self, occ: dict[str, Any], players: list[str], npcs: list[str], all_occupants: list[str]
    ) -> None:
        """
        Process a dictionary occupant and add to appropriate lists.

        Args:
            occ: Dictionary containing occupant information
            players: List of player names
            npcs: List of NPC names
            all_occupants: Flat list of all occupants
        """
        if "player_name" in occ:
            player_name = occ.get("player_name")
            self.add_valid_name_to_lists(player_name, players, npcs, all_occupants, is_player=True)
        elif "npc_name" in occ:
            npc_name = occ.get("npc_name")
            self.add_valid_name_to_lists(npc_name, players, npcs, all_occupants, is_player=False)
        else:
            name = occ.get("name")
            if name and self.name_extractor.is_valid_name_for_occupant(name):
                # Type narrowing: is_valid_name_for_occupant returns True only for non-empty strings
                if not isinstance(name, str):
                    raise TypeError("name must be str if is_valid_name_for_occupant returns True")
                all_occupants.append(name)

    def build_occupants_snapshot_data(self, occupants_snapshot: list[dict[str, Any] | str]) -> dict[str, Any]:
        """
        Build structured occupants data from snapshot.

        Args:
            occupants_snapshot: List of occupant information

        Returns:
            Dictionary with players, npcs, occupants, and count
        """
        players: list[str] = []
        npcs: list[str] = []
        all_occupants: list[str] = []  # Flat list for backward compatibility

        for occ in occupants_snapshot or []:
            if isinstance(occ, dict):
                self.process_dict_occupant(occ, players, npcs, all_occupants)
            elif isinstance(occ, str):
                if self.name_extractor.is_valid_name_for_occupant(occ):
                    all_occupants.append(occ)

        return {
            # Structured data for new UI (separate columns)
            "players": players,
            "npcs": npcs,
            # Backward compatibility: flat list for legacy clients
            "occupants": all_occupants,
            "count": len(all_occupants),
        }

    def count_occupants_by_type(self, occupants_snapshot: list[dict[str, Any] | str]) -> tuple[int, int]:
        """
        Count NPCs and players in occupants snapshot.

        Args:
            occupants_snapshot: List of occupant information

        Returns:
            Tuple of (npc_count, player_count)
        """
        npc_count = sum(1 for occ in occupants_snapshot if isinstance(occ, dict) and "npc_name" in occ)
        player_count = sum(1 for occ in occupants_snapshot if isinstance(occ, dict) and "player_name" in occ)
        return npc_count, player_count

    def is_player_disconnecting(self, player_id: uuid.UUID | str) -> bool:
        """
        Check if a player is currently disconnecting.

        Args:
            player_id: The player's ID (UUID or string)

        Returns:
            True if player is disconnecting, False otherwise
        """
        if not self.connection_manager:
            return False

        try:
            player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
            return player_id_uuid in self.connection_manager.disconnecting_players
        except (ValueError, AttributeError):
            return False

    def is_player_in_grace_period(self, player_id: uuid.UUID | str) -> bool:
        """
        Check if a player is currently in grace period after disconnect.

        Args:
            player_id: The player's ID (UUID or string)

        Returns:
            True if player is in grace period, False otherwise
        """
        if not self.connection_manager:
            return False

        try:
            player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
            return is_player_in_grace_period(player_id_uuid, self.connection_manager)
        except (ValueError, AttributeError, ImportError):
            return False
