"""
Room-related player event handlers.

This module handles player room entry/exit events and room occupant management.
"""

# pylint: disable=too-many-instance-attributes,too-many-arguments,too-many-positional-arguments,too-many-lines  # Reason: Event handlers require many service attributes and complex event processing logic. Room event handlers require extensive event handling logic for comprehensive room event management.

import uuid
from datetime import UTC, datetime
from typing import Any, cast

from sqlalchemy.exc import SQLAlchemyError

from ..events.event_types import PlayerEnteredRoom, PlayerLeftRoom
from .message_builders import MessageBuilder
from .player_event_handlers_utils import PlayerEventHandlerUtils
from .player_name_utils import PlayerNameExtractor
from .room_occupant_manager import RoomOccupantManager


class PlayerRoomEventHandler:
    """Handles room-related player events (entered, left, occupants)."""

    def __init__(
        self,
        connection_manager: Any,
        room_sync_service: Any,
        chat_logger: Any,
        message_builder: MessageBuilder,
        name_extractor: PlayerNameExtractor,
        occupant_manager: RoomOccupantManager,
        utils: PlayerEventHandlerUtils,
        logger: Any,
    ) -> None:
        """
        Initialize room event handler.

        Args:
            connection_manager: ConnectionManager instance
            room_sync_service: RoomSyncService instance
            chat_logger: ChatLogger instance
            message_builder: MessageBuilder instance
            name_extractor: PlayerNameExtractor instance
            occupant_manager: RoomOccupantManager instance
            utils: PlayerEventHandlerUtils instance
            logger: Logger instance
        """
        self.connection_manager = connection_manager
        self.room_sync_service = room_sync_service
        self.chat_logger = chat_logger
        self.message_builder = message_builder
        self.name_extractor = name_extractor
        self.occupant_manager = occupant_manager
        self.utils = utils
        self._logger = logger

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
            room_name = getattr(room, "name", room_id) if room else room_id

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
        self, message: dict[str, Any], room_id_str: str | None, exclude_player_id: str | None
    ) -> None:
        """
        Broadcast player entered message to room occupants.

        Args:
            message: The player entered message
            room_id_str: The room ID as string
            exclude_player_id: Player ID to exclude from broadcast
        """
        if room_id_str is not None:
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
        from .envelope import build_event

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
        await self.connection_manager.send_personal_message(player_id_uuid, room_name_event)
        self._logger.debug(
            "Sent room name message to player",
            player_id=player_id_uuid,
            room_id=room_id,
            room_name=room_name,
        )

    async def _prepare_room_data(self, room: Any, _room_id: str) -> dict[str, Any]:
        """
        Prepare room data for client, removing occupant fields.

        Args:
            room: The room object
            _room_id: The room ID (unused, kept for interface consistency)

        Returns:
            Prepared room data dictionary
        """
        room_data = room.to_dict() if hasattr(room, "to_dict") else room
        if isinstance(room_data, dict):
            room_data = await self.connection_manager.convert_room_players_uuids_to_names(room_data)
            # CRITICAL FIX: Remove occupant fields from room_data - room_update should NEVER include these
            room_data.pop("players", None)
            room_data.pop("npcs", None)
            room_data.pop("occupants", None)
            room_data.pop("occupant_count", None)
        return cast(dict[str, Any], room_data)

    async def send_room_update_to_player(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Send full room update to a player.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)
            room_id: The room ID
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

            occupants_info = await self.occupant_manager.get_room_occupants(room_id)
            occupant_names = self.utils.extract_occupant_names(occupants_info)
            room_data = await self._prepare_room_data(room, room_id)
            room_update_event = self.message_builder.build_room_update_message(room_id, room_data)
            await self.connection_manager.send_personal_message(player_id_uuid, room_update_event)
            self._logger.debug(
                "Sent room_update to player",
                player_id=player_id_uuid,
                room_id=room_id,
                occupants=occupant_names,
            )

            if room.name:
                await self._send_room_name_message(player_id_uuid, room_id, room.name)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error sending room update to player", player_id=player_id_uuid, error=str(e))

    def _log_occupants_info(
        self,
        player_id_uuid: uuid.UUID,
        room_id: str,
        occupants_snapshot: list[dict[str, Any] | str],
        occupants_data: dict[str, Any],
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
        self._logger.info(
            "Sending room_occupants event with data to player",
            player_id=player_id_uuid,
            room_id=room_id,
            total_occupants=len(occupants_snapshot),
            npc_count=npc_count,
            player_count=player_count,
            players_count=len(occupants_data["players"]),
            npcs_count=len(occupants_data["npcs"]),
            players=occupants_data["players"],
            npcs=occupants_data["npcs"],
        )
        if not occupants_data["npcs"]:
            # Log as warning to help identify NPC spawning issues
            self._logger.warning(
                "No NPCs included in occupants snapshot - player may not see NPCs",
                player_id=player_id_uuid,
                room_id=room_id,
            )

    def build_room_occupants_message(self, room_id: str, occupants_data: dict[str, Any]) -> dict[str, Any]:
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

    async def query_room_occupants_snapshot(
        self, player_id_uuid: uuid.UUID, room_id: str
    ) -> list[dict[str, Any] | str]:
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
        occupants_snapshot = await self.occupant_manager.get_room_occupants(
            room_id, ensure_player_included=player_id_uuid
        )
        return occupants_snapshot

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
            occupants_data = self.utils.build_occupants_snapshot_data(occupants_snapshot)
            self._log_occupants_info(player_id_uuid, room_id, occupants_snapshot, occupants_data)
            personal = self.build_room_occupants_message(room_id, occupants_data)
            await self.connection_manager.send_personal_message(player_id_uuid, personal)
            self._logger.debug(
                "Occupants snapshot sent successfully to player",
                player_id=player_id_uuid,
                room_id=room_id,
                npcs_count=len(occupants_data["npcs"]),
            )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error(
                "Error sending occupants snapshot to player",
                player_id=player_id_uuid,
                room_id=room_id,
                error=str(e),
                exc_info=True,
            )

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
            # Fallback to string if conversion fails
            await self.send_room_update_to_player(player_id, room_id)
            self._logger.info(
                "Sending occupants snapshot to entering player (string fallback)",
                player_id=player_id,
                player_name=player_name,
                room_id=room_id,
            )
            await self.send_occupants_snapshot_to_player(player_id, room_id)
            return

        await self.send_room_update_to_player(player_id_uuid, room_id)

        # CRITICAL: Send personal occupants snapshot with enhanced logging
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
        _, player_name = player_info

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

    async def handle_player_entered(self, event: PlayerEnteredRoom, send_occupants_update: Any | None = None) -> None:
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
            message = self.message_builder.create_player_entered_message(processed_event, player_name)
            self._logger.debug(
                "Broadcasting player_entered",
                exclude_player=exclude_player_id,
                room_id=room_id_str,
            )

            await self.broadcast_player_entered_message(message, room_id_str, exclude_player_id)

            # Send room occupants update to all players in the room
            if send_occupants_update is not None and room_id_str is not None:
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
            await self.connection_manager.unsubscribe_from_room(player_id_uuid, room_id)
        except (ValueError, AttributeError):
            self._logger.warning("Failed to convert player_id to UUID for room unsubscription", player_id=player_id)

    async def broadcast_player_left_message(
        self, message: dict[str, Any], room_id_str: str | None, exclude_player_id: str | None, is_disconnecting: bool
    ) -> None:
        """
        Broadcast player left message to room occupants.

        Args:
            message: The player left message
            room_id_str: The room ID as string
            exclude_player_id: Player ID to exclude from broadcast
            is_disconnecting: Whether the player is disconnecting (skip message if True)
        """
        if room_id_str is not None and not is_disconnecting:
            await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

    async def handle_player_left(self, event: PlayerLeftRoom, send_occupants_update: Any) -> None:
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
            _, player_name = player_info

            # Log player movement for AI processing
            await self.log_player_movement(processed_event.player_id, player_name, processed_event.room_id, "left")

            # Create real-time message with processed event
            message = self.message_builder.create_player_left_message(processed_event, player_name)

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
