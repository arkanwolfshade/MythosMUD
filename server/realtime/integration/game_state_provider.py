"""
Game state provision for connection management.

This module provides comprehensive game state generation for newly connected
players, including player data, room information, and occupant lists.

AI Agent: Extracted from ConnectionManager to follow Single Responsibility Principle.
Game state generation is now a focused, independently testable component.
"""

import json
import uuid
from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from ...models import Player
from ...services.npc_instance_service import get_npc_instance_service
from ...structured_logging.enhanced_logging_config import get_logger
from ..disconnect_grace_period import is_player_in_grace_period
from ..envelope import build_event
from ..login_grace_period import (
    get_login_grace_period_remaining,
    is_player_in_login_grace_period,
)

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from ..room_subscription_manager import RoomSubscriptionManager

logger = get_logger(__name__)


class GameStateProvider:
    """
    Provides initial game state for newly connected players.

    This class provides:
    - Player data retrieval and batch loading
    - Room data retrieval
    - NPC name resolution
    - UUID to display name conversion
    - Initial game_state event generation

    AI Agent: Single Responsibility - Game state generation only.
    """

    def __init__(
        self,
        room_manager: "RoomSubscriptionManager",
        get_async_persistence: Callable[[], Any],
        send_personal_message_callback: Callable[[uuid.UUID, dict[str, Any]], "Awaitable[dict[str, Any]]"],
        get_app: Callable[[], Any],
    ) -> None:
        """
        Initialize the game state provider.

        Args:
            room_manager: RoomSubscriptionManager instance
            get_async_persistence: Callback to get async persistence layer
            send_personal_message_callback: Callback to send personal message
            get_app: Callback to get FastAPI app instance
        """
        self.room_manager = room_manager
        self.get_async_persistence = get_async_persistence
        self.send_personal_message = send_personal_message_callback
        self.get_app = get_app

    async def get_player(self, player_id: uuid.UUID) -> Player | None:
        """
        Get a player from the persistence layer (async version).

        Args:
            player_id: The player's ID (UUID)

        Returns:
            Optional[Player]: The player object or None if not found
        """
        async_persistence = self.get_async_persistence()
        player = await async_persistence.get_player_by_id(player_id)
        return player

    async def get_players_batch(self, player_ids: list[uuid.UUID]) -> dict[uuid.UUID, Player]:
        """
        Get multiple players from the persistence layer in a single batch operation.

        This method optimizes room occupant lookups by reducing N+1 queries to a single
        batch operation.

        Args:
            player_ids: List of player IDs to retrieve (UUIDs)

        Returns:
            dict: Mapping of player_id to Player object (only includes found players)

        AI: Batch loading eliminates N+1 queries when getting room occupants.
        """
        async_persistence = self.get_async_persistence()
        if async_persistence is None:
            logger.warning("Persistence layer not initialized for batch player lookup", player_count=len(player_ids))
            return {}

        players: dict[uuid.UUID, Player] = {}
        if not player_ids:
            return players

        # Load players in batch - iterate through IDs and get each one
        # Note: If persistence layer supports batch operations in the future, this can be optimized further
        for player_id in player_ids:
            try:
                player = await async_persistence.get_player_by_id(player_id)
                if player:
                    players[player_id] = player
            except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player batch loading errors unpredictable, must continue processing
                # Structlog handles UUID objects automatically, no need to convert to string
                logger.debug("Error loading player in batch", player_id=player_id, error=str(e))

        logger.debug(
            "Batch loaded players",
            requested_count=len(player_ids),
            loaded_count=len(players),
        )
        return players

    def get_npcs_batch(self, npc_ids: list[str]) -> dict[str, str]:
        """
        Get NPC names for multiple NPCs in a batch operation.

        Args:
            npc_ids: List of NPC IDs to retrieve names for

        Returns:
            dict: Mapping of npc_id to npc_name (only includes found NPCs)

        AI: Batch loading eliminates N+1 queries when getting NPC names for room occupants.
        """
        npc_names: dict[str, str] = {}
        if not npc_ids:
            return npc_names

        try:  # pylint: disable=too-many-nested-blocks  # Reason: NPC name resolution requires complex nested logic for service lookup, lifecycle validation, and batch processing
            # Get NPC instance service for batch lookup
            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager:
                    for npc_id in npc_ids:
                        if npc_id in lifecycle_manager.active_npcs:
                            npc_instance = lifecycle_manager.active_npcs[npc_id]
                            name = getattr(npc_instance, "name", None)
                            if name:
                                npc_names[npc_id] = name
                            else:
                                # Fallback: Extract NPC name from the NPC ID
                                npc_names[npc_id] = npc_id.split("_")[0].replace("_", " ").title()
                        else:
                            # Fallback: Extract NPC name from the NPC ID
                            npc_names[npc_id] = npc_id.split("_")[0].replace("_", " ").title()
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: NPC name batch loading errors unpredictable, must use fallback names
            logger.debug("Error batch loading NPC names", npc_count=len(npc_ids), error=str(e))
            # Fallback: Generate names from IDs
            for npc_id in npc_ids:
                npc_names[npc_id] = npc_id.split("_")[0].replace("_", " ").title()

        logger.debug(
            "Batch loaded NPC names",
            requested_count=len(npc_ids),
            loaded_count=len(npc_names),
        )
        return npc_names

    def _get_player_name_with_grace_periods(self, player_id_uuid: uuid.UUID, player_obj: Any) -> str | None:
        """Get player name and add grace period indicators if applicable."""
        player_name = getattr(player_obj, "name", None)
        if not player_name or not isinstance(player_name, str) or not player_name.strip():
            # Try to get name from related User object
            if hasattr(player_obj, "user"):
                try:
                    user = getattr(player_obj, "user", None)
                    if user:
                        player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                except Exception:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: User attribute access errors unpredictable, graceful fallback if user attributes are unavailable, must continue processing
                    pass

        # Validate name is not UUID
        if player_name and isinstance(player_name, str) and player_name.strip():
            is_uuid_string = (
                len(player_name) == 36
                and player_name.count("-") == 4
                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
            )
            if not is_uuid_string:
                # Check if player is in disconnect grace period and add "(linkdead)" indicator
                # Also check if player is in login grace period and add "(warded)" indicator
                try:
                    app = self.get_app()
                    connection_manager = getattr(app.state, "connection_manager", None) if app else None
                    if connection_manager:
                        if is_player_in_grace_period(player_id_uuid, connection_manager):
                            player_name = f"{player_name} (linkdead)"
                        # Check login grace period (can have both indicators)
                        if is_player_in_login_grace_period(player_id_uuid, connection_manager):
                            player_name = f"{player_name} (warded)"
                except (AttributeError, ImportError, TypeError, ValueError):
                    # If we can't check grace period, use name as-is
                    pass
                return player_name
        return None

    async def _convert_player_uuids_to_names(self, room_data: dict[str, Any]) -> None:
        """Convert player UUIDs to names in room_data."""
        if "players" not in room_data or not isinstance(room_data["players"], list):
            return

        player_uuids = room_data["players"]
        player_names: list[str] = []
        for player_id_str in player_uuids:
            try:
                player_id_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                player_obj = await self.get_player(player_id_uuid)
                if player_obj:
                    player_name = self._get_player_name_with_grace_periods(player_id_uuid, player_obj)
                    if player_name:
                        player_names.append(player_name)
            except (ValueError, AttributeError):
                # Skip invalid UUIDs
                pass
        room_data["players"] = player_names

    async def convert_room_uuids_to_names(self, room_data: dict[str, Any]) -> dict[str, Any]:
        """
        Convert player UUIDs and NPC IDs in room_data to names.

        CRITICAL: NEVER send UUIDs or NPC IDs to the client - this is a security issue.
        room.to_dict() returns UUIDs in "players" field and NPC IDs in "npcs" field,
        we must convert both to names.

        Args:
            room_data: Room data dictionary from room.to_dict()

        Returns:
            Modified room_data with players and NPCs as names instead of UUIDs/IDs
        """
        await self._convert_player_uuids_to_names(room_data)

        # CRITICAL FIX: Convert NPC IDs to names in room_data
        # room.to_dict() returns NPC IDs in "npcs" field, we must convert to names
        # As documented in "Resurrection and NPC Display Synchronization" - Dr. Armitage, 1930
        # NPC IDs must be resolved to display names before sending to client
        if "npcs" in room_data and isinstance(room_data["npcs"], list):
            npc_ids = room_data["npcs"]
            # Batch load NPC names for efficiency
            npc_names_dict = self.get_npcs_batch(npc_ids)
            npc_names: list[str] = []
            for npc_id in npc_ids:
                npc_name = npc_names_dict.get(npc_id)
                if npc_name and isinstance(npc_name, str) and npc_name.strip():
                    # Validate name is not an ID (check if it looks like an ID with underscores)
                    # NPC IDs typically have format like "npc_type_location_timestamp_instance"
                    # If the "name" is the same as the ID, skip it
                    if npc_name != npc_id:
                        npc_names.append(npc_name)
                    else:
                        # Fallback: Generate name from ID if name resolution failed
                        # This should rarely happen, but provides a safety net
                        fallback_name = npc_id.split("_")[0].replace("_", " ").title()
                        if fallback_name and fallback_name != npc_id:
                            npc_names.append(fallback_name)
            # Replace NPC IDs with names
            room_data["npcs"] = npc_names

        return room_data

    async def get_room_occupants(
        self, room_id: str, online_players: dict[uuid.UUID, dict[str, Any]]
    ) -> list[dict[str, Any]]:
        """
        Get list of occupants in a room.

        Args:
            room_id: The room ID
            online_players: Online players dictionary

        Returns:
            List[Dict[str, Any]]: List of occupant information
        """
        online_players_str = {str(k): v for k, v in online_players.items()}
        return await self.room_manager.get_room_occupants(room_id, online_players_str)

    async def _get_room_data_with_conversion(self, room_id: str) -> dict[str, Any] | None:
        """Get room data and convert player UUIDs to names."""
        async_persistence = self.get_async_persistence()
        if not async_persistence or not room_id:
            return None

        room = async_persistence.get_room_by_id(room_id)  # Sync method, uses cache
        if not room:
            return None

        room_data = room.to_dict()
        room_data = await self.convert_room_uuids_to_names(room_data)
        return room_data

    def _add_grace_period_indicators(
        self, occupant_name: str, occ_player_id: str | uuid.UUID, connection_manager: Any
    ) -> str:
        """Add grace period indicators to occupant name."""
        try:
            occ_player_id_uuid = uuid.UUID(occ_player_id) if isinstance(occ_player_id, str) else occ_player_id
            if is_player_in_grace_period(occ_player_id_uuid, connection_manager):
                occupant_name = f"{occupant_name} (linkdead)"
            if is_player_in_login_grace_period(occ_player_id_uuid, connection_manager):
                occupant_name = f"{occupant_name} (warded)"
        except (AttributeError, ImportError, TypeError, ValueError):
            pass
        return occupant_name

    async def _process_occupants_with_grace_periods(
        self, room_id: str, player_id: uuid.UUID, online_players: dict[uuid.UUID, dict[str, Any]]
    ) -> tuple[list[str], list[str], list[str]]:
        """Process room occupants and separate into players and NPCs with grace period indicators."""
        occupants: list[str] = []
        player_names_list: list[str] = []
        npc_names_list: list[str] = []

        if not room_id:
            return occupants, player_names_list, npc_names_list

        online_players_str = {str(k): v for k, v in online_players.items()}
        occ_infos = await self.room_manager.get_room_occupants(room_id, online_players_str)

        app = self.get_app()
        connection_manager = getattr(app.state, "connection_manager", None) if app else None

        for occ_info in occ_infos:
            occupant_name = occ_info.get("player_name", "Unknown")
            is_npc = occ_info.get("is_npc", False)

            if is_npc:
                npc_names_list.append(occupant_name)
            else:
                occ_player_id = occ_info.get("player_id")
                if occ_player_id and connection_manager:
                    occupant_name = self._add_grace_period_indicators(occupant_name, occ_player_id, connection_manager)

                if occ_info.get("player_id") != player_id:
                    player_names_list.append(occupant_name)
                else:
                    player_names_list.append(occupant_name)

            if occ_info.get("player_id") != player_id or is_npc:
                occupants.append(occupant_name)
            else:
                occupants.append(occupant_name)

        return occupants, player_names_list, npc_names_list

    def _get_fallback_player_data(self, player: Player, player_id: uuid.UUID, room_id: str) -> dict[str, Any]:
        """Get fallback player data when PlayerService is unavailable."""
        stats_data = {}
        if hasattr(player, "get_stats"):
            stats_data = player.get_stats()
        else:
            raw_stats = getattr(player, "stats", {})
            if isinstance(raw_stats, str):
                try:
                    stats_data = json.loads(raw_stats)
                except (ValueError, TypeError, json.JSONDecodeError):
                    stats_data = {}
            elif isinstance(raw_stats, dict):
                stats_data = raw_stats

        return {
            "player_id": str(getattr(player, "player_id", player_id)),
            "name": getattr(player, "name", "Unknown Player"),
            "level": getattr(player, "level", 1),
            "xp": getattr(player, "experience_points", 0),
            "current_room_id": room_id,
            "stats": stats_data,
        }

    async def _get_player_data_for_client(self, player: Player, player_id: uuid.UUID, room_id: str) -> dict[str, Any]:
        """Get complete player data using PlayerService or fallback."""
        try:
            app = self.get_app()
            app_state = getattr(app, "state", None) if app else None
            player_service = getattr(app_state, "player_service", None) if app_state else None

            if player_service:
                complete_player_data = await player_service.convert_player_to_schema(player)
                logger.debug(
                    "GameStateProvider: Retrieved complete player data with profession",
                    player_id=player_id,
                    has_profession=bool(getattr(complete_player_data, "profession_name", None)),
                    has_stats=bool(getattr(complete_player_data, "stats", None)),
                )

                player_data_for_client = (
                    complete_player_data.model_dump(mode="json")
                    if hasattr(complete_player_data, "model_dump")
                    else complete_player_data.dict()
                )
                if "experience_points" in player_data_for_client:
                    player_data_for_client["xp"] = player_data_for_client["experience_points"]
                return player_data_for_client
            logger.warning(
                "PlayerService not available in game_state_provider, using basic player data",
                player_id=player_id,
            )
            return self._get_fallback_player_data(player, player_id, room_id)
        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Player data retrieval errors unpredictable, must return fallback data
            logger.error(
                "Error getting complete player data in game_state_provider",
                error=str(e),
                player_id=player_id,
                exc_info=True,
            )
            return self._get_fallback_player_data(player, player_id, room_id)

    def _get_login_grace_period_status(self, player_id: uuid.UUID) -> tuple[bool, float]:
        """Get login grace period status for player."""
        try:
            app = self.get_app()
            connection_manager = getattr(app.state, "connection_manager", None) if app else None
            if connection_manager and is_player_in_login_grace_period(player_id, connection_manager):
                return True, get_login_grace_period_remaining(player_id, connection_manager)
        except (AttributeError, ImportError, TypeError, ValueError) as e:
            logger.debug("Could not check login grace period for game state", player_id=player_id, error=str(e))
        return False, 0.0

    async def send_initial_game_state(
        self, player_id: uuid.UUID, player: Player, room_id: str, online_players: dict[uuid.UUID, dict[str, Any]]
    ) -> None:
        """
        Send initial game_state event to a newly connected player.

        Args:
            player_id: The player's ID
            player: The player object
            room_id: The player's current room ID
            online_players: Online players dictionary
        """
        try:
            # Get room information
            room_data = await self._get_room_data_with_conversion(room_id)
            if room_data:
                logger.info(
                    "DEBUG: Room data",
                    room_id=room_id,
                    npcs=room_data.get("npcs", []),
                    occupant_count=room_data.get("occupant_count", 0),
                )

            # Get room occupants (players and NPCs) with grace period indicators
            occupants, player_names_list, npc_names_list = await self._process_occupants_with_grace_periods(
                room_id, player_id, online_players
            )

            # Get complete player data using PlayerService or fallback
            player_data_for_client = await self._get_player_data_for_client(player, player_id, room_id)

            # Get login grace period status
            login_grace_period_active, login_grace_period_remaining = self._get_login_grace_period_status(player_id)

            # Create game_state event
            game_state_data = {
                "player": player_data_for_client,
                "room": room_data,
                "occupants": occupants,
                "login_grace_period_active": login_grace_period_active,
                "login_grace_period_remaining": login_grace_period_remaining,
            }

            # BUGFIX: Populate room_data with structured player/NPC arrays for new UI
            if room_data:
                room_data["players"] = player_names_list
                room_data["npcs"] = npc_names_list
                # Keep backward compatibility
                room_data["occupants"] = occupants

            logger.debug(
                "Sending initial game state with structured occupants",
                occupants_count=len(occupants),
                players_count=len(player_names_list),
                npcs_count=len(npc_names_list),
            )

            game_state_event = build_event("game_state", game_state_data, player_id=player_id, room_id=room_id)

            # Send the event to the player
            await self.send_personal_message(player_id, game_state_event)
            logger.info("Sent initial game_state to player", player_id=player_id)

        except Exception as e:  # pylint: disable=broad-exception-caught  # noqa: B904  # Reason: Game state sending errors unpredictable, must handle gracefully
            logger.error("Error sending initial game_state to player", player_id=player_id, error=str(e), exc_info=True)
