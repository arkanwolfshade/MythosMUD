"""
Occupant formatting utilities.

This module handles formatting and separating occupants by type.

As documented in "Dimensional Occupancy Tracking" - Dr. Armitage, 1929
"""

from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger


class OccupantFormatter:
    """Formats and separates occupants by type."""

    def __init__(self) -> None:
        """Initialize occupant formatter."""
        self._logger = get_logger("OccupantFormatter")

    @staticmethod
    def _is_uuid_string(value: str) -> bool:
        """
        Check if a string looks like a UUID.

        Args:
            value: The string to check

        Returns:
            True if string matches UUID format, False otherwise
        """
        return len(value) == 36 and value.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in value)

    def _is_valid_name_for_occupant(self, name: Any) -> bool:
        """
        Check if a name is valid for use as an occupant name.

        Args:
            name: The name to validate

        Returns:
            True if name is valid (non-empty string, not UUID), False otherwise
        """
        return name and isinstance(name, str) and not self._is_uuid_string(name)

    def _add_valid_name_to_lists(self, name: str, target_list: list[str], all_occupants: list[str]) -> None:
        """
        Add a valid name to both target list and all occupants list.

        Args:
            name: The valid name to add
            target_list: The specific list to add to (players or npcs)
            all_occupants: The list of all occupants
        """
        target_list.append(name)
        all_occupants.append(name)

    def _process_player_name_for_update(
        self, player_name: Any, players: list[str], all_occupants: list[str], room_id: str
    ) -> None:
        """
        Process a player name and add to appropriate lists if valid.

        Args:
            player_name: The player name to process
            players: List to append player names to
            all_occupants: List to append all occupant names to
            room_id: Room ID for logging
        """
        if self._is_valid_name_for_occupant(player_name):
            self._add_valid_name_to_lists(player_name, players, all_occupants)
        elif player_name:
            self._logger.warning(
                "Skipping player with UUID as name in room_occupants update",
                player_name=player_name,
                room_id=room_id,
            )

    def _process_npc_name_for_update(
        self, npc_name: Any, npcs: list[str], all_occupants: list[str], room_id: str
    ) -> None:
        """
        Process an NPC name and add to appropriate lists if valid.

        Args:
            npc_name: The NPC name to process
            npcs: List to append NPC names to
            all_occupants: List to append all occupant names to
            room_id: Room ID for logging
        """
        if self._is_valid_name_for_occupant(npc_name):
            self._add_valid_name_to_lists(npc_name, npcs, all_occupants)
        elif npc_name:
            self._logger.warning(
                "Skipping NPC with UUID as name in room_occupants update",
                npc_name=npc_name,
                room_id=room_id,
            )

    def _process_dict_occupant_for_update(
        self, occ: dict[str, Any], players: list[str], npcs: list[str], all_occupants: list[str], room_id: str
    ) -> None:
        """
        Process a dictionary occupant and add to appropriate lists if valid.

        Args:
            occ: Occupant information dictionary
            players: List to append player names to
            npcs: List to append NPC names to
            all_occupants: List to append all occupant names to
            room_id: Room ID for logging
        """
        if "player_name" in occ:
            self._process_player_name_for_update(occ.get("player_name"), players, all_occupants, room_id)
        elif "npc_name" in occ:
            self._process_npc_name_for_update(occ.get("npc_name"), npcs, all_occupants, room_id)
        else:
            # Fallback for other formats
            name = occ.get("name")
            if self._is_valid_name_for_occupant(name):
                # Type narrowing: _is_valid_name_for_occupant returns True only for non-empty strings
                assert isinstance(name, str), "name must be str if _is_valid_name_for_occupant returns True"
                all_occupants.append(name)

    def _process_string_occupant_for_update(self, occ: str, all_occupants: list[str], room_id: str) -> None:
        """
        Process a string occupant (legacy format) and add to list if valid.

        Args:
            occ: Occupant name string
            all_occupants: List to append occupant names to
            room_id: Room ID for logging
        """
        if not self._is_uuid_string(occ):
            all_occupants.append(occ)
        else:
            self._logger.warning(
                "Skipping UUID string in legacy occupant format",
                occupant=occ,
                room_id=room_id,
            )

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
        players: list[str] = []
        npcs: list[str] = []
        all_occupants: list[str] = []

        for occ in occupants_info or []:
            if isinstance(occ, dict):
                self._process_dict_occupant_for_update(occ, players, npcs, all_occupants, room_id)
            elif isinstance(occ, str):
                self._process_string_occupant_for_update(occ, all_occupants, room_id)

        return players, npcs, all_occupants
