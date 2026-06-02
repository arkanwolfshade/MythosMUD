"""
Player respawn event handlers.

This module handles player respawn and delirium respawn events.
"""

# pylint: disable=too-many-lines  # Reason: Respawn handler requires comprehensive room data preparation, occupant extraction, and event building logic

from __future__ import annotations

import uuid
from collections.abc import Callable
from typing import NotRequired, TypedDict, cast

from anyio import sleep
from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from ..async_persistence import AsyncPersistenceLayer
from ..events.event_types import PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from ..models.player import Player
from ..models.room import Room
from ..utils.int_coercion import coerce_int
from .connection_manager import ConnectionManager
from .player_event_handlers_utils import PlayerEventHandlerUtils


class RespawnPlayerStatsPayload(TypedDict):
    """Nested stats object in WebSocket respawn player payloads."""

    current_dp: int
    max_dp: int
    lucidity: int
    max_lucidity: int
    position: str
    occult_knowledge: int
    fear: int
    corruption: int
    cult_affiliation: int
    strength: NotRequired[object | None]
    dexterity: NotRequired[object | None]
    constitution: NotRequired[object | None]
    intelligence: NotRequired[object | None]
    wisdom: NotRequired[object | None]
    charisma: NotRequired[object | None]


class RespawnPlayerEventPayload(TypedDict):
    """Client-facing player snapshot sent in respawn WebSocket events."""

    id: str
    name: str
    level: int
    xp: int
    stats: RespawnPlayerStatsPayload
    position: str
    in_combat: bool


def _occupant_str_field(occ: dict[str, object], field_keys: tuple[str, ...]) -> str | None:
    """Return the first string value found for any of the given occupant dict keys."""
    for key in field_keys:
        value = occ.get(key)
        if isinstance(value, str):
            return value
    return None


def _is_npc_occupant_row(occ: dict[str, object]) -> bool:
    """True when the occupant row should be classified as an NPC."""
    return bool(occ.get("is_npc")) or "npc_name" in occ


def _append_unique_valid_occupant(
    name: str | None,
    *,
    primary: list[str],
    occupant_names: list[str],
    validate_name: Callable[[object], bool],
) -> None:
    """Append a validated name to primary and occupant lists when not already present."""
    if not name or not validate_name(name) or name in primary:
        return
    primary.append(name)
    if name not in occupant_names:
        occupant_names.append(name)


def _ensure_respawned_player_in_lists(
    respawned_player_name: str,
    *,
    player_names: list[str],
    occupant_names: list[str],
    validate_name: Callable[[object], bool],
) -> None:
    """Ensure the respawned player appears in player and occupant name lists."""
    if not respawned_player_name or not validate_name(respawned_player_name):
        return
    if respawned_player_name not in occupant_names:
        occupant_names.append(respawned_player_name)
    if respawned_player_name not in player_names:
        player_names.append(respawned_player_name)


class PlayerRespawnEventHandler:
    """Handles player respawn events (respawn, delirium respawn)."""

    connection_manager: ConnectionManager | None
    _logger: BoundLogger

    def __init__(
        self,
        connection_manager: ConnectionManager | None,
        utils: PlayerEventHandlerUtils,
        logger: BoundLogger,
    ) -> None:
        """
        Initialize respawn event handler.

        Args:
            connection_manager: ConnectionManager instance
            utils: PlayerEventHandlerUtils instance
            logger: Logger instance
        """
        self.connection_manager = connection_manager
        self.utils = utils
        self._logger = logger

    def update_connection_manager_position(self, player_id_str: str, updated_position: str) -> None:
        """
        Update connection manager's in-memory position state.

        As documented in "Resurrection and In-Memory State Synchronization" - Dr. Armitage, 1930
        Connection manager's online_players tracking must reflect correct posture after respawn.

        Args:
            player_id_str: The player ID as string
            updated_position: The updated position value
        """
        connection_manager = self.connection_manager
        if not connection_manager or not hasattr(connection_manager, "online_players"):
            return

        player_uuid = uuid.UUID(player_id_str)
        if player_uuid in connection_manager.online_players:
            connection_manager.online_players[player_uuid]["position"] = updated_position
            self._logger.debug(
                "Updated connection manager position state",
                player_id=player_id_str,
                position=updated_position,
            )

    @staticmethod
    def _position_from_stats(stats: dict[str, object]) -> str:
        """Resolve posture string from player stats JSON."""
        position_raw = stats.get("position", "standing")
        return position_raw if isinstance(position_raw, str) else "standing"

    def _build_respawn_player_payload(
        self,
        player: Player,
        stats: dict[str, object],
        updated_position: str,
        lucidity: int,
    ) -> RespawnPlayerEventPayload:
        """Build client-expected player payload for respawn events."""
        stats_payload: RespawnPlayerStatsPayload = {
            "current_dp": coerce_int(stats.get("current_dp"), default=100),
            "max_dp": coerce_int(stats.get("max_dp"), default=100),
            "lucidity": lucidity,
            "max_lucidity": coerce_int(stats.get("max_lucidity"), default=100),
            "occult_knowledge": coerce_int(stats.get("occult_knowledge"), default=0),
            "fear": coerce_int(stats.get("fear"), default=0),
            "corruption": coerce_int(stats.get("corruption"), default=0),
            "cult_affiliation": coerce_int(stats.get("cult_affiliation"), default=0),
            "position": updated_position,
        }
        for stat_key in (
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ):
            if stat_key in stats:
                stats_payload[stat_key] = stats.get(stat_key)
        return {
            "id": str(player.player_id),
            "name": player.name,
            "level": player.level,
            "xp": player.experience_points,
            "stats": stats_payload,
            "position": updated_position,
            "in_combat": False,
        }

    async def get_player_data_for_respawn(self, player_id_str: str) -> tuple[RespawnPlayerEventPayload | None, str]:
        """
        Get updated player data for respawn event.

        As documented in "Resurrection and Client State Synchronization" - Dr. Armitage, 1930
        Client must receive updated player state including corrected posture after respawn.

        Args:
            player_id_str: The player ID as string

        Returns:
            Tuple of (player_data dict or None, updated_position string)
        """
        if not self.connection_manager or not hasattr(self.connection_manager, "persistence"):
            return None, "standing"

        async_persistence = cast(AsyncPersistenceLayer | None, self.connection_manager.async_persistence)
        if not async_persistence:
            return None, "standing"

        try:
            player = await async_persistence.get_player_by_id(uuid.UUID(player_id_str))
            if not player:
                return None, "standing"

            stats = player.get_stats()
            updated_position = self._position_from_stats(stats)
            lucidity = coerce_int(stats.get("lucidity"), default=100)

            # Update connection manager's in-memory position state
            self.update_connection_manager_position(player_id_str, updated_position)

            player_data = self._build_respawn_player_payload(player, stats, updated_position, lucidity)
            self._logger.debug(
                "Retrieved player data for respawn event",
                player_id=player_id_str,
                position=updated_position,
            )
            return player_data, updated_position
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.warning(
                "Failed to retrieve player data for respawn event",
                player_id=player_id_str,
                error=str(e),
            )
            return None, "standing"

    async def send_respawn_event_with_retry(
        self, player_id_uuid: uuid.UUID, respawn_event: dict[str, object], max_wait_time: float = 2.0
    ) -> None:
        """
        Send respawn event with retry logic to handle temporary connection unavailability.

        As documented in "Resurrection and Connection Synchronization" - Dr. Armitage, 1930
        The respawn event is critical and must be delivered even if connection is temporarily unavailable.
        Strategy: Poll for connection availability and send immediately when available.

        Args:
            player_id_uuid: The player's UUID
            respawn_event: The respawn event dictionary
            max_wait_time: Maximum time to wait for connection (default 2.0 seconds)
        """
        connection_manager = self.connection_manager
        if not connection_manager:
            return

        poll_interval = 0.05  # Check connection every 50ms
        max_polls = int(max_wait_time / poll_interval)  # 40 polls over 2 seconds

        for _poll_count in range(max_polls):
            has_websocket = player_id_uuid in connection_manager.player_websockets

            if not has_websocket:
                await sleep(poll_interval)
                continue

            # Connection available - try sending immediately
            # ARCHITECTURE: Server-initiated events (respawn) sent via WebSocket
            delivery_status = await connection_manager.send_personal_message(
                player_id_uuid,
                respawn_event,
            )
            # Check if message was actually delivered
            websocket_delivered = coerce_int(delivery_status.get("websocket_delivered"), default=0) > 0
            active_connections = coerce_int(delivery_status.get("active_connections"), default=0)
            if websocket_delivered and active_connections > 0:
                # Message actually delivered to active connection
                return

            # Wait before next poll
            await sleep(poll_interval)

    @staticmethod
    def _build_fallback_respawn_player_payload(
        player_id_str: str,
        player: object,
        event: PlayerRespawnedEvent,
        stats: dict[str, object],
    ) -> RespawnPlayerEventPayload:
        """Build respawn player payload from connection-manager player when persistence lookup fails."""
        # CRITICAL: Use event.new_dp as max_dp if stats don't have it (event.new_dp is the restored max_dp)
        actual_max_dp = stats.get("max_dp") if stats.get("max_dp") is not None else event.new_dp
        position = stats.get("position", "standing")
        position_str = position if isinstance(position, str) else "standing"
        stats_payload: RespawnPlayerStatsPayload = {
            "current_dp": coerce_int(stats.get("current_dp"), default=event.new_dp),
            "max_dp": coerce_int(actual_max_dp, default=event.new_dp),
            "lucidity": coerce_int(stats.get("lucidity"), default=100),
            "max_lucidity": coerce_int(stats.get("max_lucidity"), default=100),
            "occult_knowledge": coerce_int(stats.get("occult_knowledge"), default=0),
            "fear": coerce_int(stats.get("fear"), default=0),
            "corruption": coerce_int(stats.get("corruption"), default=0),
            "cult_affiliation": coerce_int(stats.get("cult_affiliation"), default=0),
            "position": position_str,
        }
        for stat_key in (
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
        ):
            if stat_key in stats:
                stats_payload[stat_key] = stats.get(stat_key)
        return {
            "id": player_id_str,
            "name": getattr(player, "name", event.player_name),
            "level": getattr(player, "level", 1),
            "xp": getattr(player, "experience_points", 0),
            "stats": stats_payload,
            "position": position_str,
            "in_combat": False,
        }

    async def _fetch_fallback_player_data_for_respawn(
        self,
        player_id_str: str,
        player_id_uuid: uuid.UUID,
        event: PlayerRespawnedEvent,
    ) -> RespawnPlayerEventPayload | None:
        """Try connection-manager player lookup when persistence-based respawn data is unavailable."""
        connection_manager = self.connection_manager
        if connection_manager is None:
            return None
        try:
            player = await connection_manager.get_player(player_id_uuid)
            if not player:
                return None
            stats = player.get_stats() if hasattr(player, "get_stats") else {}
            return self._build_fallback_respawn_player_payload(player_id_str, player, event, stats)
        except (AttributeError, ValueError, TypeError) as fallback_err:
            self._logger.warning(
                "Failed to get player data via fallback method",
                player_id=player_id_str,
                error=str(fallback_err),
            )
            return None

    async def _resolve_player_data_for_respawn_event(
        self,
        player_id_str: str,
        player_id_uuid: uuid.UUID,
        event: PlayerRespawnedEvent,
    ) -> RespawnPlayerEventPayload | None:
        """Resolve player snapshot for respawn, falling back to connection-manager state when needed."""
        player_data, _ = await self.get_player_data_for_respawn(player_id_str)
        if player_data:
            return player_data
        return await self._fetch_fallback_player_data_for_respawn(player_id_str, player_id_uuid, event)

    def _build_player_respawned_event(
        self,
        event: PlayerRespawnedEvent,
        player_id_str: str,
        player_data: RespawnPlayerEventPayload | None,
        room_data: dict[str, object] | None,
        npc_names: list[str],
        player_names: list[str],
        occupant_names: list[str],
    ) -> dict[str, object]:
        """Build the player_respawned WebSocket event envelope."""
        from .envelope import build_event

        return build_event(
            "player_respawned",
            {
                "player_id": player_id_str,
                "player_name": event.player_name,
                "respawn_room_id": event.respawn_room_id,
                "old_dp": event.old_dp,
                "new_dp": event.new_dp,
                "message": "The sanitarium calls you back from the threshold. You have been restored to life.",
                "player": player_data,
                "room": room_data,
                # CRITICAL: Also include top-level players/npcs/occupants for client projector compatibility
                "players": player_names if player_names else None,
                "npcs": npc_names if npc_names else None,
                "occupants": occupant_names if occupant_names else None,
                "occupant_count": len(occupant_names) if occupant_names else 0,
            },
            player_id=player_id_str,
        )

    async def _send_room_occupants_after_respawn(
        self,
        player_id_str: str,
        player_id_uuid: uuid.UUID,
        respawn_room_id: str,
        room_data: dict[str, object] | None,
        occupant_names: list[str],
    ) -> None:
        """Send room_occupants so the client lists the respawned player in the room."""
        if not room_data or not occupant_names:
            return
        try:
            from .envelope import build_event

            room_occupants_event = build_event(
                "room_occupants",
                {
                    "room_id": respawn_room_id,
                    "occupants": occupant_names,
                    "sequence_number": 0,  # Use 0 for respawn-initiated update
                },
                player_id=player_id_str,
            )
            await self.send_respawn_event_with_retry(player_id_uuid, room_occupants_event)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as occupants_err:
            self._logger.warning(
                "Could not send room_occupants event after respawn",
                player_id=player_id_str,
                error=str(occupants_err),
            )

    async def handle_player_respawned(self, event: PlayerRespawnedEvent) -> None:
        """
        Handle player respawn events by sending respawn notification to the client.

        CRITICAL: After respawn, client needs:
        1. Updated player data (stats, max_dp)
        2. Room data (NPCs, occupants, room description)
        3. Room occupants update (so player appears in occupants list)

        Args:
            event: The PlayerRespawnedEvent containing respawn information
        """
        try:
            player_id_str = str(event.player_id)
            player_id_uuid = uuid.UUID(player_id_str)

            player_data = await self._resolve_player_data_for_respawn_event(player_id_str, player_id_uuid, event)

            room_data, npc_names, player_names, occupant_names = await self._prepare_room_data_for_respawn(
                event.respawn_room_id, event.player_name
            )

            respawn_event = self._build_player_respawned_event(
                event, player_id_str, player_data, room_data, npc_names, player_names, occupant_names
            )
            await self.send_respawn_event_with_retry(player_id_uuid, respawn_event)

            await self._send_room_occupants_after_respawn(
                player_id_str, player_id_uuid, event.respawn_room_id, room_data, occupant_names
            )

            self._logger.info(
                "Sent respawn notification to player",
                player_id=player_id_str,
                respawn_room=event.respawn_room_id,
                player_data_included=player_data is not None,
                room_data_included=room_data is not None,
                occupants_count=len(occupant_names),
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player respawn event", error=str(e), exc_info=True)

    async def _prepare_room_data_for_respawn(
        self, room_id: str, respawned_player_name: str
    ) -> tuple[dict[str, object] | None, list[str], list[str], list[str]]:
        """Prepare room data with NPC and player names for a respawn event."""
        room_data = None
        occupant_names: list[str] = []
        npc_names: list[str] = []
        player_names: list[str] = []

        try:
            from ..async_persistence import get_async_persistence
            from .websocket_initial_state import prepare_room_data_with_occupants

            async_persistence = get_async_persistence()
            room = async_persistence.get_room_by_id(room_id)
            if not room:
                return None, npc_names, player_names, occupant_names

            connection_manager = self.connection_manager
            if connection_manager is None:
                return self._room_data_from_persistence_room(room, respawned_player_name)

            room_data, _ = await prepare_room_data_with_occupants(room, room_id, connection_manager)
            room_occupants = await connection_manager.get_room_occupants(room_id)
            if room_data:
                npc_names, player_names, occupant_names = await self._enrich_room_data_with_occupant_names(
                    room_data, room_occupants, respawned_player_name
                )

        except (AttributeError, KeyError, ValueError, TypeError, ImportError) as room_err:
            self._logger.warning(
                "Could not get room data for respawn event",
                room_id=room_id,
                error=str(room_err),
            )

        return room_data, npc_names, player_names, occupant_names

    def _room_data_from_persistence_room(
        self, room: Room, respawned_player_name: str
    ) -> tuple[dict[str, object], list[str], list[str], list[str]]:
        """Build room payload from persistence when no live connection manager is available."""
        room_data = cast(dict[str, object], room.to_dict())
        npc_names, player_names, occupant_names = self._extract_occupant_names(None, respawned_player_name)
        return room_data, npc_names, player_names, occupant_names

    async def _enrich_room_data_with_occupant_names(
        self,
        room_data: dict[str, object],
        room_occupants: list[dict[str, object]] | None,
        respawned_player_name: str,
    ) -> tuple[list[str], list[str], list[str]]:
        """Merge live occupants into room_data and return name lists for the respawn payload."""
        npc_names, player_names, occupant_names = self._extract_occupant_names(room_occupants, respawned_player_name)
        npc_names = await self._convert_npc_ids_to_names(
            cast(list[str], room_data.get("npcs", [])), npc_names, occupant_names
        )
        player_names = self._merge_player_lists(
            cast(list[str], room_data.get("players", [])), player_names, occupant_names
        )
        room_data["npcs"] = npc_names
        room_data["players"] = player_names
        room_data["occupants"] = occupant_names
        room_data["occupant_count"] = len(occupant_names)
        return npc_names, player_names, occupant_names

    def _extract_occupant_names(
        self, room_occupants: list[dict[str, object]] | None, respawned_player_name: str
    ) -> tuple[list[str], list[str], list[str]]:
        """
        Extract NPC and player names from room occupants.

        Args:
            room_occupants: List of occupant dictionaries
            respawned_player_name: Name of the respawned player

        Returns:
            Tuple of (npc_names, player_names, occupant_names)
        """
        from .websocket_helpers import validate_occupant_name

        npc_names: list[str] = []
        player_names: list[str] = []
        occupant_names: list[str] = []

        for occ in room_occupants or []:
            if _is_npc_occupant_row(occ):
                npc_name = _occupant_str_field(occ, ("npc_name", "name", "player_name"))
                _append_unique_valid_occupant(
                    npc_name,
                    primary=npc_names,
                    occupant_names=occupant_names,
                    validate_name=validate_occupant_name,
                )
            else:
                player_name = _occupant_str_field(occ, ("player_name", "name"))
                _append_unique_valid_occupant(
                    player_name,
                    primary=player_names,
                    occupant_names=occupant_names,
                    validate_name=validate_occupant_name,
                )

        _ensure_respawned_player_in_lists(
            respawned_player_name,
            player_names=player_names,
            occupant_names=occupant_names,
            validate_name=validate_occupant_name,
        )

        return npc_names, player_names, occupant_names

    async def _convert_npc_ids_to_names(
        self, existing_npcs: list[str], npc_names: list[str], occupant_names: list[str]
    ) -> list[str]:
        """
        Convert NPC IDs to names if they're still UUIDs.

        Args:
            existing_npcs: List of NPC IDs/names from room_data
            npc_names: Current list of NPC names
            occupant_names: Current list of all occupant names

        Returns:
            Updated list of NPC names
        """
        result = list(npc_names)

        for npc_id in existing_npcs:
            if npc_id not in result:
                # If it looks like an ID, try to get name from lifecycle manager
                if "_" in npc_id or len(npc_id) > 20:
                    npc_name = self._get_npc_name_from_lifecycle_manager(npc_id)
                    if npc_name:
                        result.append(npc_name)
                        if npc_name not in occupant_names:
                            occupant_names.append(npc_name)
                else:
                    # Already a name
                    result.append(npc_id)
                    if npc_id not in occupant_names:
                        occupant_names.append(npc_id)

        return result

    def _get_npc_name_from_lifecycle_manager(self, npc_id: str) -> str | None:
        """
        Get NPC name from lifecycle manager.

        Args:
            npc_id: NPC ID to look up

        Returns:
            NPC name or None if not found
        """
        if not self.connection_manager:
            return None

        from .websocket_initial_state import get_npc_lifecycle_manager_from_connection_manager

        npc_lifecycle_manager = get_npc_lifecycle_manager_from_connection_manager(self.connection_manager)
        if not npc_lifecycle_manager:
            return None

        npc = npc_lifecycle_manager.active_npcs.get(npc_id)
        if npc is None:
            return None
        return npc.name

    def _merge_player_lists(
        self, existing_players: list[str], player_names: list[str], occupant_names: list[str]
    ) -> list[str]:
        """
        Merge existing player list with extracted player names.

        Args:
            existing_players: Existing player list from room_data
            player_names: Current list of player names
            occupant_names: Current list of all occupant names

        Returns:
            Merged list of player names
        """
        result = list(player_names)

        for existing_player in existing_players:
            if existing_player not in result:
                result.append(existing_player)
                if existing_player not in occupant_names:
                    occupant_names.append(existing_player)

        return result

    async def get_current_lucidity(self, player_uuid: uuid.UUID, default_lucidity: int) -> int:
        """
        Get current lucidity from PlayerLucidity table.

        Args:
            player_uuid: The player's UUID
            default_lucidity: Default lucidity value if record not found

        Returns:
            Current lucidity value
        """
        from ..database import get_async_session
        from ..models.lucidity import PlayerLucidity

        current_lucidity = default_lucidity
        async for session in get_async_session():
            lucidity_record = await session.get(PlayerLucidity, player_uuid)
            if lucidity_record:
                current_lucidity = lucidity_record.current_lcd
            break
        return current_lucidity

    async def _fetch_delirium_respawn_player_snapshot(
        self, player_id_str: str, default_lucidity: int
    ) -> tuple[RespawnPlayerEventPayload, str]:
        """Load player stats, lucidity, and client payload for delirium respawn."""
        player_uuid = uuid.UUID(player_id_str)
        connection_manager = self.connection_manager
        if not connection_manager:
            raise ValueError(f"Connection manager unavailable for player: {player_id_str}")
        async_persistence = cast(AsyncPersistenceLayer | None, connection_manager.async_persistence)
        if not async_persistence:
            raise ValueError(f"Async persistence unavailable for player: {player_id_str}")
        player = await async_persistence.get_player_by_id(player_uuid)
        if not player:
            raise ValueError(f"Player not found: {player_id_str}")

        stats = player.get_stats()
        updated_position = self._position_from_stats(stats)
        self.update_connection_manager_position(player_id_str, updated_position)
        current_lucidity = await self.get_current_lucidity(player_uuid, default_lucidity)
        player_data = self._build_respawn_player_payload(player, stats, updated_position, current_lucidity)
        return player_data, updated_position

    async def get_player_data_for_delirium_respawn(
        self, player_id_str: str, default_lucidity: int
    ) -> tuple[RespawnPlayerEventPayload | None, str]:
        """
        Get updated player data for delirium respawn event.

        Args:
            player_id_str: The player ID as string
            default_lucidity: Default lucidity value from event

        Returns:
            Tuple of (player_data dict or None, updated_position string)
        """
        if not self.connection_manager or not hasattr(self.connection_manager, "persistence"):
            return None, "standing"

        async_persistence = cast(AsyncPersistenceLayer | None, self.connection_manager.async_persistence)
        if not async_persistence:
            return None, "standing"

        try:
            player_data, updated_position = await self._fetch_delirium_respawn_player_snapshot(
                player_id_str, default_lucidity
            )
            self._logger.debug(
                "Retrieved player data for delirium respawn event",
                player_id=player_id_str,
                position=updated_position,
                lucidity=player_data["stats"]["lucidity"],
            )
            return player_data, updated_position
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.warning(
                "Failed to retrieve player data for delirium respawn event",
                player_id=player_id_str,
                error=str(e),
            )
            return None, "standing"

    async def handle_player_delirium_respawned(self, event: PlayerDeliriumRespawnedEvent) -> None:
        """
        Handle player delirium respawn events by sending respawn notification to the client.

        Args:
            event: The PlayerDeliriumRespawnedEvent containing delirium respawn information
        """
        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # Get updated player data to include in event payload
            player_data, _ = await self.get_player_data_for_delirium_respawn(player_id_str, event.new_lucidity)

            # Send personal message to the player
            from .envelope import build_event

            respawn_event = build_event(
                "player_delirium_respawned",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "respawn_room_id": event.respawn_room_id,
                    "old_lucidity": event.old_lucidity,
                    "new_lucidity": event.new_lucidity,
                    "message": "You have been restored to lucidity and returned to the Sanitarium.",
                    "player": player_data,
                },
                player_id=player_id_str,
            )

            # Retry sending respawn event to handle temporary connection unavailability
            player_id_uuid = uuid.UUID(player_id_str)
            await self.send_respawn_event_with_retry(player_id_uuid, respawn_event)

            self._logger.info(
                "Sent delirium respawn notification to player",
                player_id=player_id_str,
                respawn_room=event.respawn_room_id,
                new_lucidity=event.new_lucidity,
                player_data_included=player_data is not None,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player delirium respawn event", error=str(e), exc_info=True)
