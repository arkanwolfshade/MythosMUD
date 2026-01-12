"""
Player occupant processing utilities.

This module handles querying and processing player occupants for rooms.

As documented in "Dimensional Occupancy Tracking" - Dr. Armitage, 1929
"""

# pylint: disable=too-few-public-methods  # Reason: Utility class with focused responsibility, minimal public interface

import uuid
from typing import Any

from ..structured_logging.enhanced_logging_config import get_logger
from .disconnect_grace_period import is_player_in_grace_period
from .login_grace_period import is_player_in_login_grace_period
from .player_name_utils import PlayerNameExtractor


class PlayerOccupantProcessor:
    """Processes player occupants for rooms."""

    def __init__(self, connection_manager: Any, name_extractor: PlayerNameExtractor) -> None:
        """
        Initialize player occupant processor.

        Args:
            connection_manager: ConnectionManager instance
            name_extractor: PlayerNameExtractor instance
        """
        self.connection_manager = connection_manager
        self.name_extractor = name_extractor
        self._logger = get_logger("PlayerOccupantProcessor")

    def _ensure_player_included_in_list(
        self, room_id: str, player_id_strings: list[str], ensure_player_included: uuid.UUID | str | None
    ) -> None:
        """
        Ensure a player is included in the player ID strings list if specified.

        Args:
            room_id: The room ID for logging
            player_id_strings: List of player ID strings to potentially modify
            ensure_player_included: Optional player ID to ensure is included
        """
        if not ensure_player_included:
            return

        ensure_player_id_str = str(ensure_player_included)
        if ensure_player_id_str not in player_id_strings:
            player_id_strings.append(ensure_player_id_str)
            self._logger.debug(
                "Added ensure_player_included to player list",
                room_id=room_id,
                player_id=ensure_player_id_str,
                reason="Player not in room._players yet (race condition during movement)",
            )

    def _convert_player_ids_to_uuids(
        self, player_id_strings: list[str]
    ) -> tuple[list[uuid.UUID], dict[uuid.UUID, str]]:
        """
        Convert player ID strings to UUIDs for batch loading.

        Args:
            player_id_strings: List of player ID strings

        Returns:
            Tuple of (player_id_uuids list, player_id_mapping dictionary)
        """
        player_id_uuids: list[uuid.UUID] = []
        player_id_mapping: dict[uuid.UUID, str] = {}

        for player_id_str in player_id_strings:
            try:
                player_id_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                player_id_uuids.append(player_id_uuid)
                player_id_mapping[player_id_uuid] = player_id_str
            except (ValueError, AttributeError):
                self._logger.debug("Invalid player ID format", player_id=player_id_str)
                continue

        return player_id_uuids, player_id_mapping

    def _create_player_occupant_info(
        self, player_id_uuid: uuid.UUID, player_id_str: str, player: Any
    ) -> dict[str, Any] | None:
        """
        Create occupant information dictionary for a single player.

        Args:
            player_id_uuid: The player UUID
            player_id_str: The player ID string
            player: The player object

        Returns:
            Occupant information dictionary or None if player name is invalid
        """
        # Extract and validate player name
        player_name = self.name_extractor.extract_and_validate_player_name(player, player_id_str, player_id_uuid)
        if not player_name:
            return None

        # Check if player is in disconnect grace period and add "(linkdead)" indicator
        # Also check if player is in login grace period and add "(warded)" indicator
        try:
            if is_player_in_grace_period(player_id_uuid, self.connection_manager):
                player_name = f"{player_name} (linkdead)"
            # Check login grace period (can have both indicators)
            if is_player_in_login_grace_period(player_id_uuid, self.connection_manager):
                player_name = f"{player_name} (warded)"
        except (AttributeError, ImportError, TypeError):
            # If we can't check grace period, use name as-is
            pass

        # Check if player is online (player_websockets uses UUID keys)
        is_online = player_id_uuid in self.connection_manager.player_websockets

        return {
            "player_id": player_id_str,
            "player_name": player_name,
            "level": getattr(player, "level", 1),
            "online": is_online,
        }

    async def process_players_for_occupants(
        self, room_id: str, player_id_strings: list[str], ensure_player_included: uuid.UUID | str | None
    ) -> list[dict[str, Any]]:
        """
        Process players and convert to occupant information.

        Args:
            room_id: The room ID
            player_id_strings: List of player ID strings
            ensure_player_included: Optional player ID to ensure is included

        Returns:
            List of player occupant information dictionaries
        """
        occupants: list[dict[str, Any]] = []

        # CRITICAL FIX: If ensure_player_included is provided and not in the room's _players set,
        # add it to ensure the player is included even during race conditions
        self._ensure_player_included_in_list(room_id, player_id_strings, ensure_player_included)

        # Convert string IDs to UUIDs for batch loading
        player_id_uuids, player_id_mapping = self._convert_player_ids_to_uuids(player_id_strings)

        # OPTIMIZATION: Batch load all players at once to eliminate N+1 queries
        # Note: Using protected method for performance optimization - this is intentional
        players = await self.connection_manager._get_players_batch(player_id_uuids)  # noqa: SLF001  # pylint: disable=protected-access

        self._logger.debug(
            "Batch loaded players for room occupants",
            room_id=room_id,
            requested_count=len(player_id_uuids),
            loaded_count=len(players),
            player_ids=[str(pid) for pid in player_id_uuids],
        )

        # Convert to occupant information using batch-loaded players
        for player_id_uuid in player_id_uuids:
            player = players.get(player_id_uuid)
            player_id_str = player_id_mapping[player_id_uuid]

            if not player:
                self._logger.warning(
                    "Player not found in batch load, skipping from occupants",
                    player_id=player_id_str,
                    player_id_uuid=str(player_id_uuid),
                    batch_loaded_count=len(players),
                    batch_loaded_ids=[str(pid) for pid in players.keys()],
                )
                continue

            occupant_info = self._create_player_occupant_info(player_id_uuid, player_id_str, player)
            if occupant_info:
                occupants.append(occupant_info)
                self._logger.debug(
                    "Added player to occupants",
                    player_id=player_id_str,
                    player_name=occupant_info["player_name"],
                )

        return occupants
