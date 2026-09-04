"""
Room-related player event handlers.

This module handles player room entry/exit events and room occupant management.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-lines,missing-class-docstring,missing-function-docstring,too-few-public-methods  # Reason: Room handlers are large; Protocol stubs (PEP 544)

from __future__ import annotations

import uuid
from collections.abc import Awaitable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol, cast, overload

from sqlalchemy.exc import SQLAlchemyError
from structlog.stdlib import BoundLogger

from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from .envelope import build_event
from .message_builders import MessageBuilder
from .player_event_handlers_utils import PlayerEventHandlerUtils
from .player_name_utils import PlayerNameExtractor
from .room_occupant_manager import RoomOccupantManager

JsonMap = dict[str, object]
OccupantSnap = list[JsonMap | str]


class _NamedRoom(Protocol):
    name: object

    def to_dict(self) -> object: ...


class _RoomPersistence(Protocol):
    def get_room_by_id(self, room_id: str) -> _NamedRoom | None: ...


class RoomConnectionManager(Protocol):
    async_persistence: _RoomPersistence | None
    sequence_counter: int

    async def broadcast_to_room(
        self, room_id: str, message: Mapping[str, object], exclude_player: str | None = None
    ) -> None: ...

    async def subscribe_to_room(self, player_id: uuid.UUID, room_id: str) -> None: ...

    async def unsubscribe_from_room(self, player_id: uuid.UUID, room_id: str) -> None: ...

    async def send_personal_message(self, player_id: uuid.UUID, event: Mapping[str, object]) -> None: ...

    async def convert_room_players_uuids_to_names(self, room_data: JsonMap) -> JsonMap: ...


class RoomChatLogger(Protocol):
    def log_player_joined_room(self, *, player_id: str, player_name: str, room_id: str, room_name: object) -> None: ...

    def log_player_left_room(self, *, player_id: str, player_name: str, room_id: str, room_name: object) -> None: ...


class RoomSyncOrdering(Protocol):
    @overload
    def process_event_with_ordering(self, event: PlayerEnteredRoom) -> PlayerEnteredRoom: ...

    @overload
    def process_event_with_ordering(self, event: PlayerLeftRoom) -> PlayerLeftRoom: ...

    def process_event_with_ordering(
        self, event: PlayerEnteredRoom | PlayerLeftRoom
    ) -> PlayerEnteredRoom | PlayerLeftRoom: ...


class OccupantsUpdateFn(Protocol):
    def __call__(self, room_id: str, exclude_player: str | None = None) -> Awaitable[None]: ...


def _as_map(value: object) -> JsonMap:
    if not isinstance(value, dict):
        return {}
    typed = cast(dict[object, object], value)
    return {str(k): v for k, v in typed.items()}


def _as_occupant_snap(value: object) -> OccupantSnap:
    if not isinstance(value, list):
        return []
    result: OccupantSnap = []
    for item in cast(list[object], value):
        if isinstance(item, str):
            result.append(item)
        else:
            result.append(_as_map(item))
    return result


def _snapshot_payload(utils: PlayerEventHandlerUtils, raw: object) -> tuple[OccupantSnap, JsonMap]:
    snap = _as_occupant_snap(raw)
    data = _as_map(cast(object, utils.build_occupants_snapshot_data(snap)))
    return snap, data


@dataclass
class PlayerRoomEventHandlerDeps:
    """Constructor bundle so Lizard does not count eight service args."""

    connection_manager: RoomConnectionManager | None
    room_sync_service: RoomSyncOrdering
    chat_logger: RoomChatLogger
    message_builder: MessageBuilder
    name_extractor: PlayerNameExtractor
    occupant_manager: RoomOccupantManager
    utils: PlayerEventHandlerUtils
    logger: BoundLogger


class PlayerRoomEventHandler:
    """Handles room-related player events (entered, left, occupants)."""

    connection_manager: RoomConnectionManager | None
    room_sync_service: RoomSyncOrdering
    chat_logger: RoomChatLogger
    message_builder: MessageBuilder
    name_extractor: PlayerNameExtractor
    occupant_manager: RoomOccupantManager
    utils: PlayerEventHandlerUtils
    _logger: BoundLogger

    def __init__(self, deps: PlayerRoomEventHandlerDeps) -> None:
        """Initialize room event handler from a deps bundle."""
        self.connection_manager = deps.connection_manager
        self.room_sync_service = deps.room_sync_service
        self.chat_logger = deps.chat_logger
        self.message_builder = deps.message_builder
        self.name_extractor = deps.name_extractor
        self.occupant_manager = deps.occupant_manager
        self.utils = deps.utils
        self._logger = deps.logger

    async def log_player_movement(
        self, player_id: uuid.UUID | str, player_name: str, room_id: str, movement_type: str
    ) -> None:
        """
        Log player movement for AI processing.

        Args:
            player_id: The player's ID
            player_name: The player's name
            room_id: The room ID
            movement_type: Type of movement ("joined" or "left")
        """
        # Defensive check: if no connection_manager, skip logging
        if not self.connection_manager:
            return

        try:
            room = (
                self.connection_manager.async_persistence.get_room_by_id(room_id)
                if self.connection_manager.async_persistence
                else None
            )
            room_name = str(room.name) if room is not None and room.name else room_id

            if movement_type == "joined":
                self.chat_logger.log_player_joined_room(
                    player_id=str(player_id),
                    player_name=player_name,
                    room_id=room_id,
                    room_name=room_name,
                )
            elif movement_type == "left":
                self.chat_logger.log_player_left_room(
                    player_id=str(player_id),
                    player_name=player_name,
                    room_id=room_id,
                    room_name=room_name,
                )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error logging player movement", error=str(e), movement_type=movement_type)

    async def broadcast_player_entered_message(
        self, message: JsonMap, room_id_str: str | None, exclude_player_id: str | None
    ) -> None:
        """
        Broadcast player entered message to room occupants.

        Args:
            message: The player entered message
            room_id_str: The room ID as string
            exclude_player_id: Player ID to exclude from broadcast
        """
        if room_id_str is not None and self.connection_manager is not None:
            await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

    async def subscribe_player_to_room(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Subscribe player to room for receiving broadcasts.

        Args:
            player_id: The player's ID (UUID or string)
            room_id: The room ID
        """
        player_id_uuid = self.utils.normalize_player_id(player_id)
        if not player_id_uuid:
            self._logger.warning("Failed to convert player_id to UUID for room subscription", player_id=player_id)
            return

        try:
            if self.connection_manager is None:
                return
            await self.connection_manager.subscribe_to_room(player_id_uuid, room_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.warning(
                "Failed to subscribe player to room", player_id=player_id, room_id=room_id, error=str(e)
            )

    async def _send_room_name_message(self, player_id_uuid: uuid.UUID, room_id: str, room_name: str) -> None:
        """
        Send room name as a message to the Game Info panel.

        Args:
            player_id_uuid: The player's UUID
            room_id: The room ID
            room_name: The room name
        """
        cm = self.connection_manager
        if cm is None:
            return
        room_name_event = build_event(
            "command_response",
            {
                "result": room_name,
                "suppress_chat": False,
                "is_html": False,
            },
            player_id=player_id_uuid,
            connection_manager=self.connection_manager,
        )
        await cm.send_personal_message(player_id_uuid, room_name_event)
        self._logger.debug(
            "Sent room name message to player",
            player_id=player_id_uuid,
            room_id=room_id,
            room_name=room_name,
        )

    async def _prepare_room_data(self, room: _NamedRoom, _room_id: str) -> JsonMap:
        """
        Prepare room data for client, removing occupant fields.

        Args:
            room: The room object
            _room_id: The room ID (unused, kept for interface consistency)

        Returns:
            Prepared room data dictionary
        """
        cm = self.connection_manager
        room_data = _as_map(room.to_dict() if hasattr(room, "to_dict") else room)
        if cm is not None:
            room_data = await cm.convert_room_players_uuids_to_names(room_data)
            for key in ("players", "npcs", "occupants", "occupant_count"):
                if key in room_data:
                    del room_data[key]
        return room_data

    async def send_room_update_to_player(
        self, player_id: uuid.UUID | str, room_id: str, include_occupants: bool = False
    ) -> None:
        """
        Send full room update to a player.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)
            room_id: The room ID
            include_occupants: If True, include players/npcs/occupants in payload (for entering player only)
        """
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, cannot send room update", player_id=player_id, room_id=room_id
            )
            return

        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        try:
            room = (
                self.connection_manager.async_persistence.get_room_by_id(room_id)
                if self.connection_manager.async_persistence
                else None
            )
            if not room:
                return

            occupants_info = await self.occupant_manager.get_room_occupants(
                room_id, ensure_player_included=player_id if include_occupants else None
            )
            occupants_snap, occupants_data = _snapshot_payload(self.utils, occupants_info)
            occupant_names = [str(name) for name in self.utils.extract_occupant_names(occupants_snap)]
            room_data = await self._prepare_room_data(room, room_id)
            if include_occupants:
                room_data["players"] = occupants_data.get("players", [])
                room_data["npcs"] = occupants_data.get("npcs", [])
                room_data["occupants"] = occupants_data.get("occupants", [])
                room_data["occupant_count"] = occupants_data.get("count", 0)
            room_update_event = _as_map(self.message_builder.build_room_update_message(room_id, room_data))
            await self.connection_manager.send_personal_message(player_id_uuid, room_update_event)
            if include_occupants:
                self._logger.info(
                    "OCCUPANT_DEBUG: Sent room_update WITH occupants to entering player",
                    player_id=str(player_id_uuid),
                    room_id=room_id,
                    occupants_in_payload=room_data.get("occupant_count", 0),
                    occupant_names=occupant_names,
                )
            self._logger.debug(
                "Sent room_update to player",
                player_id=player_id_uuid,
                room_id=room_id,
                occupants=occupant_names,
            )

            if room.name:
                await self._send_room_name_message(player_id_uuid, room_id, str(room.name))
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error sending room update to player", player_id=player_id_uuid, error=str(e))

    def _log_occupants_info(
        self,
        player_id_uuid: uuid.UUID,
        room_id: str,
        occupants_snapshot: OccupantSnap,
        occupants_data: JsonMap,
    ) -> None:
        """
        Log occupants snapshot preparation and sending.

        Args:
            player_id_uuid: The player's UUID
            room_id: The room ID
            occupants_snapshot: List of occupant information
            occupants_data: Structured occupants data
        """
        npc_count, player_count = self.utils.count_occupants_by_type(occupants_snapshot)
        players_raw = occupants_data.get("players", [])
        npcs_raw = occupants_data.get("npcs", [])
        players_list: list[object] = list(cast(list[object], players_raw)) if isinstance(players_raw, list) else []
        npcs_list: list[object] = list(cast(list[object], npcs_raw)) if isinstance(npcs_raw, list) else []
        self._logger.info(
            "Sending room_occupants event with data to player",
            player_id=player_id_uuid,
            room_id=room_id,
            total_occupants=len(occupants_snapshot),
            npc_count=npc_count,
            player_count=player_count,
            players_count=len(players_list),
            npcs_count=len(npcs_list),
            players=players_list,
            npcs=npcs_list,
        )
        if not npcs_list:
            # Log as warning to help identify NPC spawning issues
            self._logger.info(
                "No NPCs included in occupants snapshot - player may not see NPCs",
                player_id=player_id_uuid,
                room_id=room_id,
            )

    def build_room_occupants_message(self, room_id: str, occupants_data: JsonMap) -> JsonMap:
        """
        Build room occupants message for sending to player.

        Args:
            room_id: The room ID
            occupants_data: Structured occupants data

        Returns:
            Dictionary containing the room_occupants event message
        """
        return {
            "event_type": "room_occupants",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self.message_builder.get_next_sequence(),
            "room_id": room_id,
            "data": occupants_data,
        }

    async def query_room_occupants_snapshot(self, player_id_uuid: uuid.UUID, room_id: str) -> OccupantSnap:
        """
        Query room occupants snapshot for a player.

        Args:
            player_id_uuid: The player's UUID
            room_id: The room ID

        Returns:
            List of occupant information
        """
        self._logger.debug(
            "Querying room occupants for personal snapshot",
            player_id=player_id_uuid,
            room_id=room_id,
        )
        return _as_occupant_snap(
            await self.occupant_manager.get_room_occupants(room_id, ensure_player_included=player_id_uuid)
        )

    async def send_occupants_snapshot_to_player(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Send occupants snapshot to a player.

        CRITICAL: This method MUST include NPCs when querying room occupants.
        This is the primary mechanism for updating the entering player's Occupants panel.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)
            room_id: The room ID
        """
        # Defensive check: if no connection_manager, cannot send updates
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, cannot send occupants snapshot", player_id=player_id, room_id=room_id
            )
            return

        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        try:
            occupants_snapshot = await self.query_room_occupants_snapshot(player_id_uuid, room_id)
            _, occupants_data = _snapshot_payload(self.utils, occupants_snapshot)
            self._log_occupants_info(player_id_uuid, room_id, occupants_snapshot, occupants_data)
            personal = self.build_room_occupants_message(room_id, occupants_data)
            await self.connection_manager.send_personal_message(player_id_uuid, personal)
            npcs_sent = occupants_data.get("npcs", [])
            self._logger.debug(
                "Occupants snapshot sent successfully to player",
                player_id=player_id_uuid,
                room_id=room_id,
                npcs_count=len(cast(list[object], npcs_sent)) if isinstance(npcs_sent, list) else 0,
            )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error(
                "Error sending occupants snapshot to player",
                player_id=player_id_uuid,
                room_id=room_id,
                error=str(e),
                exc_info=True,
            )

    async def send_room_state_to_player(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Send single authoritative room_state (room metadata + occupants) to a player.

        Client treats room_state as authoritative for that room_id (replace, do not merge).
        Sent to entering player and can be sent on room changes.

        Args:
            player_id: The player's ID (UUID or string)
            room_id: The room ID
        """
        if not self.connection_manager:
            return
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        try:
            room = (
                self.connection_manager.async_persistence.get_room_by_id(room_id)
                if self.connection_manager.async_persistence
                else None
            )
            if not room:
                return
            occupants_info = await self.occupant_manager.get_room_occupants(room_id, ensure_player_included=player_id)
            occupants_snap, occupants_data = _snapshot_payload(self.utils, occupants_info)
            occupant_names = [str(name) for name in self.utils.extract_occupant_names(occupants_snap)]
            room_data = await self._prepare_room_data(room, room_id)
            room_data["players"] = occupants_data.get("players", [])
            room_data["npcs"] = occupants_data.get("npcs", [])
            room_data["occupants"] = occupants_data.get("occupants", [])
            room_data["occupant_count"] = occupants_data.get("count", 0)
            room_state_event = _as_map(self.message_builder.build_room_state_message(room_id, room_data))
            await self.connection_manager.send_personal_message(player_id_uuid, room_state_event)
            self._logger.debug(
                "Sent room_state (authoritative) to player",
                player_id=player_id_uuid,
                room_id=room_id,
                occupant_count=room_data.get("occupant_count", 0),
                occupant_names=occupant_names,
            )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error(
                "Error sending room_state to player",
                player_id=str(player_id),
                room_id=room_id,
                error=str(e),
            )

    async def get_room_state_event(self, player_id: uuid.UUID | str, room_id: str) -> JsonMap | None:
        """
        Build authoritative room_state event for a room (same as send_room_state_to_player, without sending).

        Used for request/response: include in command_response when player enters a room so client
        can set room state from the response and not rely on push event ordering.

        Args:
            player_id: The player's ID (UUID or string)
            room_id: The room ID

        Returns:
            room_state event dict or None if room/occupants unavailable
        """
        if not self.connection_manager:
            return None
        try:
            room = (
                self.connection_manager.async_persistence.get_room_by_id(room_id)
                if self.connection_manager.async_persistence
                else None
            )
            if not room:
                return None
            occupants_info = await self.occupant_manager.get_room_occupants(room_id, ensure_player_included=player_id)
            room_data = await self._prepare_room_data(room, room_id)
            _, occupants_data = _snapshot_payload(self.utils, occupants_info)
            room_data["players"] = occupants_data.get("players", [])
            room_data["npcs"] = occupants_data.get("npcs", [])
            room_data["occupants"] = occupants_data.get("occupants", [])
            room_data["occupant_count"] = occupants_data.get("count", 0)
            return _as_map(self.message_builder.build_room_state_message(room_id, room_data))
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.debug(
                "get_room_state_event failed",
                player_id=str(player_id),
                room_id=room_id,
                error=str(e),
            )
            return None

    async def send_room_updates_to_entering_player(
        self, player_id: uuid.UUID | str, player_name: str, room_id: str
    ) -> None:
        """
        Send room updates and occupants snapshot to entering player.

        Args:
            player_id: The player's ID (UUID or string)
            player_name: The player's name
            room_id: The room ID
        """
        player_id_uuid = self.utils.normalize_player_id(player_id)
        if not player_id_uuid:
            # Fallback to string if conversion fails; send room_occupants first
            self._logger.info(
                "Sending occupants snapshot to entering player (string fallback)",
                player_id=player_id,
                player_name=player_name,
                room_id=room_id,
            )
            await self.send_occupants_snapshot_to_player(player_id, room_id)
            await self.send_room_update_to_player(player_id, room_id, include_occupants=True)
            return

        # Send room_state first (authoritative single source); client replaces room for this room_id.
        try:
            await self.send_room_state_to_player(player_id_uuid, room_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as room_state_err:
            self._logger.debug(
                "Send room_state to entering player failed (non-fatal)",
                player_id=player_id_uuid,
                room_id=room_id,
                error=str(room_state_err),
            )
        # Send room_occupants BEFORE room_update so the client always has occupants first.
        # This avoids race where room_update (empty occupants) can overwrite if order varies.
        self._logger.info(
            "Sending occupants snapshot to entering player",
            player_id=player_id,
            player_name=player_name,
            room_id=room_id,
        )
        try:
            await self.send_occupants_snapshot_to_player(player_id_uuid, room_id)
            self._logger.debug(
                "Occupants snapshot sent to entering player",
                player_id=player_id,
                room_id=room_id,
            )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as snapshot_error:
            self._logger.error(
                "Failed to send occupants snapshot to entering player",
                player_id=player_id,
                room_id=room_id,
                error=str(snapshot_error),
                exc_info=True,
            )

        await self.send_room_update_to_player(player_id_uuid, room_id, include_occupants=True)
        # Re-send room_occupants after room_update so client has a second chance to apply occupants
        # (handles race where game_state or ordering could overwrite)
        try:
            await self.send_occupants_snapshot_to_player(player_id_uuid, room_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as re_send_error:
            self._logger.debug(
                "Re-send room_occupants after room_update failed (non-fatal)",
                player_id=player_id_uuid,
                room_id=room_id,
                error=str(re_send_error),
            )

    async def _process_player_entered_event(
        self, processed_event: PlayerEnteredRoom
    ) -> tuple[str, str | None, str] | None:
        """
        Process player entered event and return player name and normalized IDs.

        Args:
            processed_event: The processed PlayerEnteredRoom event

        Returns:
            Tuple of (player_name, exclude_player_id, room_id_str) or None if processing fails
        """
        player_info = await self.utils.get_player_info(processed_event.player_id)
        if not player_info:
            return None
        player_name = player_info[1]

        exclude_player_id, room_id_str = self.utils.normalize_event_ids(
            processed_event.player_id, processed_event.room_id
        )

        if room_id_str is None:
            self._logger.error(
                "Room ID is None, cannot process player entered event",
                player_id=processed_event.player_id,
                room_id=processed_event.room_id,
            )
            return None

        return player_name, exclude_player_id, room_id_str

    async def handle_player_entered(
        self, event: PlayerEnteredRoom, send_occupants_update: OccupantsUpdateFn | None = None
    ) -> None:
        """
        Handle player entering a room with enhanced synchronization.

        Args:
            event: The PlayerEnteredRoom event
            send_occupants_update: Optional callable to send room occupants update
        """
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player entered event",
                player_id=event.player_id,
                room_id=event.room_id,
            )
            return

        try:
            processed_event = self.room_sync_service.process_event_with_ordering(event)
            self._logger.debug(
                "Handling player entered event with synchronization",
                player_id=processed_event.player_id,
                room_id=processed_event.room_id,
            )

            result = await self._process_player_entered_event(processed_event)
            if not result:
                return
            player_name, exclude_player_id, room_id_str = result

            await self.log_player_movement(processed_event.player_id, player_name, processed_event.room_id, "joined")
            message = _as_map(self.message_builder.create_player_entered_message(processed_event, player_name))
            self._logger.debug(
                "Broadcasting player_entered",
                exclude_player=exclude_player_id,
                room_id=room_id_str,
            )

            await self.broadcast_player_entered_message(message, room_id_str, exclude_player_id)

            # Send room occupants update to all players in the room
            if send_occupants_update is not None:
                await send_occupants_update(room_id_str, exclude_player=exclude_player_id)

            await self.subscribe_player_to_room(processed_event.player_id, room_id_str)
            await self.send_room_updates_to_entering_player(processed_event.player_id, player_name, room_id_str)

            self._logger.info(
                "Player entered room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player entered event", error=str(e), exc_info=True)

    async def unsubscribe_player_from_room(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Unsubscribe a player from a room.

        Args:
            player_id: The player's ID (UUID or string)
            room_id: The room ID
        """
        try:
            player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
            if self.connection_manager is None:
                return
            await self.connection_manager.unsubscribe_from_room(player_id_uuid, room_id)
        except (ValueError, AttributeError):
            self._logger.warning("Failed to convert player_id to UUID for room unsubscription", player_id=player_id)

    async def broadcast_player_left_message(
        self, message: JsonMap, room_id_str: str | None, exclude_player_id: str | None, is_disconnecting: bool
    ) -> None:
        """
        Broadcast player left message to room occupants.

        Args:
            message: The player left message
            room_id_str: The room ID as string
            exclude_player_id: Player ID to exclude from broadcast
            is_disconnecting: Whether the player is disconnecting (skip message if True)
        """
        if room_id_str is not None and not is_disconnecting and self.connection_manager is not None:
            await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

    async def handle_player_left(self, event: PlayerLeftRoom, send_occupants_update: OccupantsUpdateFn) -> None:
        """
        Handle player leaving a room with enhanced synchronization.

        Args:
            event: The PlayerLeftRoom event
            send_occupants_update: Callable to send room occupants update
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player left event",
                player_id=event.player_id,
                room_id=event.room_id,
            )
            return

        try:
            # Process event with proper ordering to prevent race conditions
            processed_event = self.room_sync_service.process_event_with_ordering(event)

            self._logger.debug(
                "Handling player left event with synchronization",
                player_id=processed_event.player_id,
                room_id=processed_event.room_id,
            )

            # Get player information
            player_info = await self.utils.get_player_info(processed_event.player_id)
            if not player_info:
                return
            player_name = player_info[1]

            # Log player movement for AI processing
            await self.log_player_movement(processed_event.player_id, player_name, processed_event.room_id, "left")

            # Create real-time message with processed event
            message = _as_map(self.message_builder.create_player_left_message(processed_event, player_name))

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(processed_event.player_id) if processed_event.player_id else None
            room_id_str = str(processed_event.room_id) if processed_event.room_id else None

            # Check if this is a disconnect (not a movement)
            is_disconnecting = self.utils.is_player_disconnecting(processed_event.player_id)

            self._logger.debug(
                "Broadcasting player_left",
                exclude_player=exclude_player_id,
                room_id=room_id_str,
                is_disconnecting=is_disconnecting,
            )

            # Broadcast to remaining room occupants (excluding the leaving player)
            await self.broadcast_player_left_message(message, room_id_str, exclude_player_id, is_disconnecting)

            # CRITICAL FIX: Send room occupants update BEFORE unsubscribing player
            # This ensures the update can still query the leaving player from room tracking
            # if needed, and correctly shows remaining players
            if room_id_str is not None and exclude_player_id is not None:
                await send_occupants_update(room_id_str, exclude_player=exclude_player_id)

            # Unsubscribe player from the room AFTER sending occupants update
            await self.unsubscribe_player_from_room(processed_event.player_id, processed_event.room_id)

            self._logger.info(
                "Player left room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player left event", error=str(e), exc_info=True)
