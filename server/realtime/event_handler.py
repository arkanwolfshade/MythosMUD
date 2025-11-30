"""
Real-time event handler for MythosMUD.

This module provides the RealTimeEventHandler class that bridges EventBus events
to real-time communication, enabling players to see each other in the game world.

As noted in the Pnakotic Manuscripts, proper event propagation is essential
for maintaining awareness of the dimensional shifts that occur throughout our
eldritch architecture.
"""

import uuid
from datetime import UTC, datetime
from typing import Any, cast

from ..app.tracked_task_manager import get_global_tracked_manager
from ..events import EventBus
from ..events.event_types import NPCEnteredRoom, NPCLeftRoom, PlayerEnteredRoom, PlayerHPUpdated, PlayerLeftRoom
from ..logging.enhanced_logging_config import get_logger
from ..services.chat_logger import chat_logger
from ..services.player_combat_service import PlayerXPAwardEvent
from ..services.room_sync_service import get_room_sync_service


class RealTimeEventHandler:
    """
    Bridges EventBus events to real-time communication.

    This class subscribes to game events and converts them into real-time
    messages that are broadcast to connected clients. It serves as the
    critical link between the event system and the real-time communication
    layer.
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
        self.connection_manager = connection_manager  # AI Agent: Injected dependency
        self._logger = get_logger("RealTimeEventHandler")
        self._sequence_counter = 0

        # Task registry for tracking child tasks spawned by event broadcasting
        self.task_registry = task_registry

        # Chat logger for AI processing
        self.chat_logger = chat_logger

        # Room synchronization service for enhanced event processing
        self.room_sync_service = get_room_sync_service()

        # Subscribe to relevant game events
        self._subscribe_to_events()

        self._logger.info("RealTimeEventHandler initialized with enhanced room synchronization")

    def _subscribe_to_events(self) -> None:
        """Subscribe to relevant game events."""
        self.event_bus.subscribe(PlayerEnteredRoom, self._handle_player_entered)
        self.event_bus.subscribe(PlayerLeftRoom, self._handle_player_left)
        self.event_bus.subscribe(NPCEnteredRoom, self._handle_npc_entered)
        self.event_bus.subscribe(NPCLeftRoom, self._handle_npc_left)
        self.event_bus.subscribe(PlayerXPAwardEvent, self._handle_player_xp_awarded)
        self.event_bus.subscribe(PlayerHPUpdated, self._handle_player_hp_updated)

        # Log subscription for debugging
        self._logger.info(
            "Subscribed to game events",
            event_types=[
                "PlayerEnteredRoom",
                "PlayerLeftRoom",
                "NPCEnteredRoom",
                "NPCLeftRoom",
                "PlayerXPAwardEvent",
                "PlayerHPUpdated",
            ],
            event_bus_id=id(self.event_bus),
        )

        # Subscribe to death/respawn events
        from ..events.event_types import PlayerDiedEvent, PlayerHPDecayEvent, PlayerRespawnedEvent

        self.event_bus.subscribe(PlayerDiedEvent, self._handle_player_died)
        self.event_bus.subscribe(PlayerHPDecayEvent, self._handle_player_hp_decay)
        self.event_bus.subscribe(PlayerRespawnedEvent, self._handle_player_respawned)

        self._logger.info("Subscribed to PlayerEnteredRoom, PlayerLeftRoom, NPCEnteredRoom, and NPCLeftRoom events")

    def _get_next_sequence(self) -> int:
        """Get the next sequence number for events."""
        self._sequence_counter += 1
        return self._sequence_counter

    def _get_player_info(self, player_id: uuid.UUID | str) -> tuple[Any, str] | None:
        """
        Get player information and name.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)

        Returns:
            tuple: (player, player_name) or None if player not found
        """
        # Convert to UUID if string (for backward compatibility)
        try:
            player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        except (ValueError, TypeError):
            # Invalid UUID string - log and return None
            self._logger.warning("Invalid player_id format, cannot convert to UUID", player_id=player_id)
            return None
        player = self.connection_manager._get_player(player_id_uuid)
        if not player:
            # Structlog handles UUID objects automatically, no need to convert to string
            self._logger.warning("Player not found", player_id=player_id_uuid)
            return None
        # CRITICAL: NEVER use UUID as fallback for player name - security issue
        player_name = getattr(player, "name", None)
        if not player_name or not isinstance(player_name, str) or not player_name.strip():
            # Try to get name from related User object if player.name is not available
            if hasattr(player, "user"):
                try:
                    user = getattr(player, "user", None)
                    if user:
                        player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                except Exception as e:
                    self._logger.debug("Error accessing user relationship for player name", error=str(e))

            # If still no name, use placeholder (NEVER use UUID)
            if not player_name or not isinstance(player_name, str) or not player_name.strip():
                self._logger.warning(
                    "Player name not found, using placeholder",
                    player_id=player_id_uuid,
                    has_name_attr=hasattr(player, "name"),
                    name_value=getattr(player, "name", "NOT_FOUND"),
                )
                player_name = "Unknown Player"

        # CRITICAL: Final validation - ensure player_name is NEVER a UUID
        if isinstance(player_name, str):
            is_uuid_string = (
                len(player_name) == 36
                and player_name.count("-") == 4
                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
            )
            if is_uuid_string:
                self._logger.error(
                    "CRITICAL: Player name is a UUID string, this should never happen",
                    player_id=player_id_uuid,
                    player_name=player_name,
                    player_name_from_db=getattr(player, "name", "NOT_FOUND"),
                )
                player_name = "Unknown Player"

        return (player, player_name)

    def _log_player_movement(
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
        try:
            room = (
                self.connection_manager.persistence.get_room(room_id) if self.connection_manager.persistence else None
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
        except Exception as e:
            self._logger.error("Error logging player movement", error=str(e), movement_type=movement_type)

    def _extract_occupant_names(self, occupants_info: list[dict[str, Any] | str]) -> list[str]:
        """
        Extract occupant names from occupant information.

        Args:
            occupants_info: List of occupant information dictionaries or strings

        Returns:
            list: List of occupant names (validated to exclude UUIDs)
        """
        names: list[str] = []
        for occ in occupants_info or []:
            if isinstance(occ, dict):
                n = occ.get("player_name") or occ.get("npc_name") or occ.get("name")
                if n and isinstance(n, str):
                    # Validate that name is not a UUID string
                    # UUID format: 36 chars, 4 dashes, hex characters
                    if not (len(n) == 36 and n.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in n)):
                        names.append(n)
                    else:
                        self._logger.warning(
                            "Skipping UUID string in _extract_occupant_names",
                            name=n,
                            occupant_type="player"
                            if "player_name" in occ
                            else "npc"
                            if "npc_name" in occ
                            else "unknown",
                        )
            elif isinstance(occ, str):
                # Validate that string is not a UUID
                if not (len(occ) == 36 and occ.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in occ)):
                    names.append(occ)
                else:
                    self._logger.warning("Skipping UUID string in legacy occupant format", occupant=occ)
        return names

    async def _send_room_update_to_player(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Send full room update to a player.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)
            room_id: The room ID
        """
        # Convert to UUID if string (send_personal_message accepts UUID)
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        try:
            room = (
                self.connection_manager.persistence.get_room(room_id) if self.connection_manager.persistence else None
            )
            if not room:
                return

            # Get room occupants and transform to names
            occupants_info = self._get_room_occupants(room_id)
            occupant_names = self._extract_occupant_names(occupants_info)

            # Create room_update event with full room data
            room_data = room.to_dict() if hasattr(room, "to_dict") else room
            # CRITICAL: Convert player UUIDs to names - NEVER send UUIDs to client
            if isinstance(room_data, dict):
                room_data = self.connection_manager._convert_room_players_uuids_to_names(room_data)
                # CRITICAL FIX: Remove occupant fields from room_data - room_update should NEVER include these
                # Occupants are ONLY sent via room_occupants events to prevent data conflicts
                # This prevents room_update from overwriting structured NPC data
                room_data.pop("players", None)
                room_data.pop("npcs", None)
                room_data.pop("occupants", None)
                room_data.pop("occupant_count", None)
            room_update_event = {
                "event_type": "room_update",
                "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "sequence_number": self._get_next_sequence(),
                "room_id": room_id,
                "data": {
                    "room": room_data,
                    "entities": [],
                    # CRITICAL: Do NOT include occupants in room_update - only in room_occupants events
                    # This prevents room_update from overwriting structured NPC/player data
                },
            }
            # Send as personal message
            await self.connection_manager.send_personal_message(player_id_uuid, room_update_event)
            self._logger.debug(
                "Sent room_update to player",
                # Structlog handles UUID objects automatically, no need to convert to string
                player_id=player_id_uuid,
                room_id=room_id,
                occupants=occupant_names,
            )

            # Send room name as a message to the Game Info panel
            # AI Agent: Only room name is needed in Game Info panel since full description is in Room Info panel
            if room.name:
                from .envelope import build_event

                room_name_event = build_event(
                    "command_response",
                    {
                        "result": room.name,
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
                    room_name=room.name,
                )
        except Exception as e:
            # Structlog handles UUID objects automatically, no need to convert to string
            self._logger.error("Error sending room update to player", player_id=player_id_uuid, error=str(e))

    async def _send_occupants_snapshot_to_player(self, player_id: uuid.UUID | str, room_id: str) -> None:
        """
        Send occupants snapshot to a player.

        Args:
            player_id: The player's ID (UUID or string for backward compatibility)
            room_id: The room ID
        """
        # Convert to UUID if string (send_personal_message accepts UUID)
        player_id_uuid = uuid.UUID(player_id) if isinstance(player_id, str) else player_id
        try:
            occupants_snapshot = self._get_room_occupants(room_id)

            # CRITICAL FIX: Use structured format (players/npcs) instead of legacy flat list
            # This ensures the client receives separate players and NPCs arrays for proper display
            players: list[str] = []
            npcs: list[str] = []
            all_occupants: list[str] = []  # Flat list for backward compatibility

            for occ in occupants_snapshot or []:
                if isinstance(occ, dict):
                    if "player_name" in occ:
                        player_name = occ.get("player_name")
                        if player_name and isinstance(player_name, str):
                            # Skip if it looks like a UUID
                            if not (
                                len(player_name) == 36
                                and player_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                            ):
                                players.append(player_name)
                                all_occupants.append(player_name)
                    elif "npc_name" in occ:
                        npc_name = occ.get("npc_name")
                        if npc_name and isinstance(npc_name, str):
                            # Skip if it looks like a UUID
                            if not (
                                len(npc_name) == 36
                                and npc_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in npc_name)
                            ):
                                npcs.append(npc_name)
                                all_occupants.append(npc_name)
                    else:
                        name = occ.get("name")
                        if name and isinstance(name, str):
                            if not (
                                len(name) == 36
                                and name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in name)
                            ):
                                all_occupants.append(name)
                elif isinstance(occ, str):
                    # Legacy format: just a name string
                    if not (
                        len(occ) == 36 and occ.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in occ)
                    ):
                        all_occupants.append(occ)

            personal = {
                "event_type": "room_occupants",
                "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "sequence_number": self._get_next_sequence(),
                "room_id": room_id,
                "data": {
                    # Structured data for new UI (separate columns)
                    "players": players,
                    "npcs": npcs,
                    # Backward compatibility: flat list for legacy clients
                    "occupants": all_occupants,
                    "count": len(all_occupants),
                },
            }
            self._logger.debug(
                "Sending room_occupants event with data",
                player_id=player_id_uuid,
                room_id=room_id,
                players_count=len(players),
                npcs_count=len(npcs),
                total_count=len(all_occupants),
                players=players,
                npcs=npcs,
                occupants=all_occupants,
            )
            await self.connection_manager.send_personal_message(player_id_uuid, personal)
        except Exception as e:
            # Structlog handles UUID objects automatically, no need to convert to string
            self._logger.error("Error sending occupants snapshot to player", player_id=player_id_uuid, error=str(e))

    async def _handle_player_entered(self, event: PlayerEnteredRoom) -> None:
        """
        Handle player entering a room with enhanced synchronization.

        Args:
            event: The PlayerEnteredRoom event
        """
        try:
            # Process event with proper ordering to prevent race conditions
            processed_event = self.room_sync_service._process_event_with_ordering(event)

            self._logger.debug(
                "Handling player entered event with synchronization",
                player_id=processed_event.player_id,
                room_id=processed_event.room_id,
            )

            # Get player information
            player_info = self._get_player_info(processed_event.player_id)
            if not player_info:
                return
            player, player_name = player_info

            # Log player movement for AI processing
            self._log_player_movement(processed_event.player_id, player_name, processed_event.room_id, "joined")

            # Create real-time message with processed event
            message = self._create_player_entered_message(processed_event, player_name)

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(processed_event.player_id) if processed_event.player_id else None
            room_id_str = str(processed_event.room_id) if processed_event.room_id else None

            self._logger.debug(
                "Broadcasting player_entered",
                exclude_player=exclude_player_id,
                room_id=room_id_str,
            )

            # Broadcast to room occupants (excluding the entering player)
            if room_id_str is not None:
                await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Subscribe player to the room so they will receive subsequent broadcasts
            # Convert string player_id to UUID for subscribe_to_room (which expects UUID)
            if processed_event.player_id and room_id_str is not None:
                try:
                    player_id_uuid = (
                        uuid.UUID(processed_event.player_id)
                        if isinstance(processed_event.player_id, str)
                        else processed_event.player_id
                    )
                    await self.connection_manager.subscribe_to_room(player_id_uuid, room_id_str)
                except (ValueError, AttributeError):
                    self._logger.warning(
                        "Failed to convert player_id to UUID for room subscription", player_id=processed_event.player_id
                    )

            # Send room occupants update to the entering player as a personal message
            # so they immediately see who is present on joining
            if room_id_str is not None and processed_event.player_id:
                await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)
                # Functions accept UUID | str, so convert string to UUID if needed
                try:
                    player_id_for_personal = (
                        uuid.UUID(processed_event.player_id)
                        if isinstance(processed_event.player_id, str)
                        else processed_event.player_id
                    )
                    await self._send_room_update_to_player(player_id_for_personal, room_id_str)
                    await self._send_occupants_snapshot_to_player(player_id_for_personal, room_id_str)
                except (ValueError, AttributeError):
                    # Fallback to string if conversion fails
                    await self._send_room_update_to_player(processed_event.player_id, room_id_str)
                    await self._send_occupants_snapshot_to_player(processed_event.player_id, room_id_str)

            self._logger.info(
                "Player entered room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except Exception as e:
            self._logger.error("Error handling player entered event", error=str(e), exc_info=True)

    async def _handle_player_left(self, event: PlayerLeftRoom) -> None:
        """
        Handle player leaving a room with enhanced synchronization.

        Args:
            event: The PlayerLeftRoom event
        """
        try:
            # Process event with proper ordering to prevent race conditions
            processed_event = self.room_sync_service._process_event_with_ordering(event)

            self._logger.debug(
                "Handling player left event with synchronization",
                player_id=processed_event.player_id,
                room_id=processed_event.room_id,
            )

            # Get player information
            player_info = self._get_player_info(processed_event.player_id)
            if not player_info:
                return
            player, player_name = player_info

            # Log player movement for AI processing
            self._log_player_movement(processed_event.player_id, player_name, processed_event.room_id, "left")

            # Create real-time message with processed event
            message = self._create_player_left_message(processed_event, player_name)

            # Unsubscribe player from the room
            # Convert string player_id to UUID for unsubscribe_from_room (which expects UUID)
            try:
                player_id_uuid = (
                    uuid.UUID(processed_event.player_id)
                    if isinstance(processed_event.player_id, str)
                    else processed_event.player_id
                )
                await self.connection_manager.unsubscribe_from_room(player_id_uuid, processed_event.room_id)
            except (ValueError, AttributeError):
                self._logger.warning(
                    "Failed to convert player_id to UUID for room unsubscription", player_id=processed_event.player_id
                )

            # CRITICAL FIX: Ensure player_id is always a string for proper comparison
            exclude_player_id = str(processed_event.player_id) if processed_event.player_id else None
            room_id_str = str(processed_event.room_id) if processed_event.room_id else None

            self._logger.debug(
                "Broadcasting player_left",
                exclude_player=exclude_player_id,
                room_id=room_id_str,
            )

            # Broadcast to remaining room occupants (excluding the leaving player)
            if room_id_str is not None:
                await self.connection_manager.broadcast_to_room(room_id_str, message, exclude_player=exclude_player_id)

            # Send room occupants update to remaining players
            if room_id_str is not None and exclude_player_id is not None:
                await self._send_room_occupants_update(room_id_str, exclude_player=exclude_player_id)

            self._logger.info(
                "Player left room with enhanced synchronization",
                player_name=player_name,
                room_id=processed_event.room_id,
            )

        except Exception as e:
            self._logger.error("Error handling player left event", error=str(e), exc_info=True)

    def _create_player_entered_message(self, event: PlayerEnteredRoom, player_name: str) -> dict:
        """
        Create a real-time message for player entering a room.

        Args:
            event: The PlayerEnteredRoom event
            player_name: The name of the player

        Returns:
            dict: The formatted message
        """
        # Convert UUIDs to strings for JSON serialization
        player_id = str(event.player_id) if event.player_id else ""
        room_id = str(event.room_id) if event.room_id else ""

        return {
            "event_type": "player_entered",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self._get_next_sequence(),
            "room_id": room_id,
            "data": {
                "player_id": player_id,
                "player_name": player_name,
                "message": f"{player_name} enters the room.",
            },
        }

    def _create_player_left_message(self, event: PlayerLeftRoom, player_name: str) -> dict:
        """
        Create a real-time message for player leaving a room.

        Args:
            event: The PlayerLeftRoom event
            player_name: The name of the player

        Returns:
            dict: The formatted message
        """
        # Convert UUIDs to strings for JSON serialization
        player_id = str(event.player_id) if event.player_id else ""
        room_id = str(event.room_id) if event.room_id else ""

        return {
            "event_type": "player_left",
            "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "sequence_number": self._get_next_sequence(),
            "room_id": room_id,
            "data": {
                "player_id": player_id,
                "player_name": player_name,
                "message": f"{player_name} leaves the room.",
            },
        }

    async def _send_room_occupants_update(self, room_id: str, exclude_player: str | None = None) -> None:
        """
        Send room occupants update to players in the room.

        Preserves player/NPC distinction by sending structured data with separate
        players and npcs arrays, enabling the client UI to display them in separate columns.

        Args:
            room_id: The room ID
            exclude_player: Optional player ID to exclude from the update
        """
        try:
            # Get room occupants with structured data (includes player_name, npc_name, type)
            occupants_info: list[dict[str, Any] | str] = self._get_room_occupants(room_id)

            # Separate players and NPCs while maintaining backward compatibility
            players: list[str] = []
            npcs: list[str] = []
            all_occupants: list[str] = []  # Flat list for backward compatibility

            for occ in occupants_info or []:
                if isinstance(occ, dict):
                    # Check if it's a player
                    if "player_name" in occ:
                        player_name = occ.get("player_name")
                        # Validate that player_name is not a UUID string
                        if player_name and isinstance(player_name, str):
                            # Skip if it looks like a UUID (36 chars, 4 dashes, hex)
                            if not (
                                len(player_name) == 36
                                and player_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                            ):
                                players.append(player_name)
                                all_occupants.append(player_name)
                            else:
                                self._logger.warning(
                                    "Skipping player with UUID as name in room_occupants update",
                                    player_name=player_name,
                                    room_id=room_id,
                                )
                    # Check if it's an NPC
                    elif "npc_name" in occ:
                        npc_name = occ.get("npc_name")
                        # Validate that npc_name is not a UUID string
                        if npc_name and isinstance(npc_name, str):
                            # Skip if it looks like a UUID
                            if not (
                                len(npc_name) == 36
                                and npc_name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in npc_name)
                            ):
                                npcs.append(npc_name)
                                all_occupants.append(npc_name)
                            else:
                                self._logger.warning(
                                    "Skipping NPC with UUID as name in room_occupants update",
                                    npc_name=npc_name,
                                    room_id=room_id,
                                )
                    # Fallback for other formats
                    else:
                        name = occ.get("name")
                        if name and isinstance(name, str):
                            # Skip if it looks like a UUID
                            if not (
                                len(name) == 36
                                and name.count("-") == 4
                                and all(c in "0123456789abcdefABCDEF-" for c in name)
                            ):
                                all_occupants.append(name)
                elif isinstance(occ, str):
                    # Legacy format: just a name string
                    # Validate it's not a UUID
                    if not (
                        len(occ) == 36 and occ.count("-") == 4 and all(c in "0123456789abcdefABCDEF-" for c in occ)
                    ):
                        all_occupants.append(occ)
                    else:
                        self._logger.warning(
                            "Skipping UUID string in legacy occupant format",
                            occupant=occ,
                            room_id=room_id,
                        )

            # Create occupants update message with structured data
            # Convert room_id to string for JSON serialization
            room_id_str = str(room_id) if room_id else ""

            # CRITICAL DEBUG: Log what we're about to send
            self._logger.debug(
                "Sending room_occupants event",
                room_id=room_id_str,
                players=players,
                npcs=npcs,
                all_occupants=all_occupants,
                players_count=len(players),
                npcs_count=len(npcs),
            )

            message = {
                "event_type": "room_occupants",
                "timestamp": datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
                "sequence_number": self._get_next_sequence(),
                "room_id": room_id_str,
                "data": {
                    # Structured data for new UI (separate columns)
                    "players": players,
                    "npcs": npcs,
                    # Backward compatibility: flat list for legacy clients
                    "occupants": all_occupants,
                    "count": len(all_occupants),
                },
            }

            # Send to room occupants
            await self.connection_manager.broadcast_to_room(room_id, message, exclude_player=exclude_player)

        except Exception as e:
            self._logger.error("Error sending room occupants update", error=str(e), exc_info=True)

    def _get_room_occupants(self, room_id: str) -> list[dict[str, Any] | str]:
        """
        Get the list of occupants in a room.

        Args:
            room_id: The room ID

        Returns:
            list[dict]: List of occupant information
        """
        occupants: list[dict[str, Any] | str] = []

        try:
            # Get room from persistence
            persistence = self.connection_manager.persistence
            if not persistence:
                return occupants

            room = persistence.get_room(room_id)
            if not room:
                return occupants

            # Get player IDs in the room (returns list[str])
            player_id_strings = room.get_players()

            # Convert string IDs to UUIDs for batch loading
            player_id_uuids: list[uuid.UUID] = []
            player_id_mapping: dict[uuid.UUID, str] = {}  # Map UUID back to original string ID
            for player_id_str in player_id_strings:
                try:
                    player_id_uuid = uuid.UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                    player_id_uuids.append(player_id_uuid)
                    player_id_mapping[player_id_uuid] = player_id_str
                except (ValueError, AttributeError):
                    # Skip invalid player IDs
                    self._logger.debug("Invalid player ID format", player_id=player_id_str)
                    continue

            # OPTIMIZATION: Batch load all players at once to eliminate N+1 queries
            players = self.connection_manager._get_players_batch(player_id_uuids)

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

                if player:
                    # Extract player name - Player model has a 'name' column that should always exist
                    # Use direct attribute access first, then getattr as fallback
                    # CRITICAL: Extract player name - ensure we never use UUID as fallback
                    # Player model has a 'name' column that should always exist (nullable=False)
                    if hasattr(player, "name"):
                        player_name = player.name
                    else:
                        player_name = getattr(player, "name", None)

                    # CRITICAL: If player_name is None, empty, or UUID, we must skip this player
                    # NEVER use player_id_str as a fallback name
                    if not player_name:
                        self._logger.warning(
                            "Player name is None or empty, skipping from occupants",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                            has_name_attr=hasattr(player, "name"),
                            player_type=type(player).__name__,
                        )
                        continue

                    # CRITICAL: Ensure player_name is a string, not UUID
                    if not isinstance(player_name, str):
                        self._logger.warning(
                            "Player name is not a string, skipping from occupants",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                            player_name=player_name,
                            player_name_type=type(player_name).__name__,
                        )
                        continue

                    # CRITICAL: Strip whitespace and check if empty after stripping
                    player_name = player_name.strip()
                    if not player_name:
                        self._logger.warning(
                            "Player name is empty after stripping, skipping from occupants",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                        )
                        continue

                    # Debug logging to diagnose name extraction issues
                    self._logger.debug(
                        "Extracting player name",
                        player_id=player_id_str,
                        player_id_uuid=str(player_id_uuid),
                        has_name_attr=hasattr(player, "name"),
                        name_value=getattr(player, "name", "NOT_FOUND"),
                        name_type=type(getattr(player, "name", None)).__name__ if hasattr(player, "name") else "N/A",
                        player_type=type(player).__name__,
                    )

                    # Ensure player_name is a valid string (not None, not empty, not UUID)
                    if not player_name or not isinstance(player_name, str) or not player_name.strip():
                        # Try fallback: username attribute (from User model)
                        if hasattr(player, "username"):
                            player_name = player.username
                        else:
                            player_name = getattr(player, "username", None)

                    # Try to get name from related User object if still not found
                    if (not player_name or not isinstance(player_name, str) or not player_name.strip()) and hasattr(
                        player, "user"
                    ):
                        try:
                            user = getattr(player, "user", None)
                            if user:
                                if hasattr(user, "username") and user.username:
                                    player_name = user.username
                                elif hasattr(user, "display_name") and user.display_name:
                                    player_name = user.display_name
                                else:
                                    player_name = getattr(user, "username", None) or getattr(user, "display_name", None)
                        except Exception as e:
                            self._logger.debug("Error accessing user relationship", error=str(e))

                    # CRITICAL: Final validation - ensure player_name is valid and not a UUID
                    # NEVER use player_id_str as a fallback name - always skip if name is invalid
                    if not player_name or not isinstance(player_name, str) or not player_name.strip():
                        # Last resort: log warning and skip this player (don't use UUID as name)
                        self._logger.warning(
                            "Player name not found or invalid, skipping from occupants",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                            player_type=type(player).__name__,
                            has_name_attr=hasattr(player, "name"),
                            name_value=getattr(player, "name", "NOT_FOUND"),
                            has_username_attr=hasattr(player, "username"),
                            username_value=getattr(player, "username", "NOT_FOUND"),
                            has_user_attr=hasattr(player, "user"),
                        )
                        continue

                    # CRITICAL: Safety check - ensure player_name is not the UUID string
                    # UUID format: 8-4-4-4-12 hex digits with dashes (36 chars total)
                    # Check both exact match and UUID pattern match
                    is_uuid_pattern = (
                        len(player_name) == 36
                        and player_name.count("-") == 4
                        and all(c in "0123456789abcdefABCDEF-" for c in player_name)
                    )
                    if player_name == player_id_str or is_uuid_pattern:
                        # player_name looks like a UUID - this shouldn't happen
                        # NEVER use UUID as name - skip this player
                        self._logger.warning(
                            "Player name appears to be UUID, skipping from occupants",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                            player_name=player_name,
                            player_type=type(player).__name__,
                            has_name_attr=hasattr(player, "name"),
                            name_value=getattr(player, "name", "NOT_FOUND"),
                            is_exact_match=(player_name == player_id_str),
                            is_uuid_pattern=is_uuid_pattern,
                        )
                        continue

                    # CRITICAL: Additional safety check - ensure player_name is not equal to UUID string representation
                    if str(player_id_uuid) == player_name or str(player_id_uuid).lower() == player_name.lower():
                        self._logger.warning(
                            "Player name matches UUID string representation, skipping from occupants",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                            player_name=player_name,
                        )
                        continue

                    # Check if player is online (player_websockets uses UUID keys)
                    is_online = player_id_uuid in self.connection_manager.player_websockets

                    # CRITICAL: Final check before adding - ensure player_name is not a UUID
                    # This is a defensive check in case any validation was missed
                    if player_name == player_id_str or str(player_id_uuid) == player_name:
                        self._logger.error(
                            "CRITICAL: Attempted to add player with UUID as name - this should never happen",
                            player_id=player_id_str,
                            player_id_uuid=str(player_id_uuid),
                            player_name=player_name,
                        )
                        continue

                    occupant_info = {
                        "player_id": player_id_str,
                        "player_name": player_name,
                        "level": getattr(player, "level", 1),
                        "online": is_online,
                    }
                    occupants.append(occupant_info)
                    self._logger.debug(
                        "Added player to occupants",
                        player_id=player_id_str,
                        player_name=player_name,
                    )
                else:
                    # Player not found in batch load - log and skip (don't add UUID)
                    self._logger.warning(
                        "Player not found in batch load, skipping from occupants",
                        player_id=player_id_str,
                        player_id_uuid=str(player_id_uuid),
                        batch_loaded_count=len(players),
                        batch_loaded_ids=[str(pid) for pid in players.keys()],
                    )

            # CRITICAL FIX: Get NPCs from lifecycle manager instead of Room instance
            # Room instances are recreated from persistence and lose in-memory NPC tracking
            # NPCs are actually tracked in the lifecycle manager with their current_room_id
            npc_ids: list[str] = []
            try:
                self._logger.info(
                    "Querying NPCs from lifecycle manager",
                    room_id=room_id,
                    step="starting_npc_query",
                )
                from ..services.npc_instance_service import get_npc_instance_service

                npc_instance_service = get_npc_instance_service()
                self._logger.debug(
                    "Retrieved NPC instance service",
                    room_id=room_id,
                    service_available=(npc_instance_service is not None),
                    has_lifecycle_manager=(
                        npc_instance_service is not None and hasattr(npc_instance_service, "lifecycle_manager")
                    ),
                )
                if npc_instance_service and hasattr(npc_instance_service, "lifecycle_manager"):
                    lifecycle_manager = npc_instance_service.lifecycle_manager
                    self._logger.debug(
                        "Retrieved lifecycle manager",
                        room_id=room_id,
                        manager_available=(lifecycle_manager is not None),
                        has_active_npcs=(lifecycle_manager is not None and hasattr(lifecycle_manager, "active_npcs")),
                    )
                    if lifecycle_manager and hasattr(lifecycle_manager, "active_npcs"):
                        active_npcs_dict = lifecycle_manager.active_npcs
                        total_active_npcs = len(active_npcs_dict)
                        self._logger.info(
                            "Scanning active NPCs for room match",
                            room_id=room_id,
                            total_active_npcs=total_active_npcs,
                        )
                        # Query all active NPCs to find those in this room
                        # NPCs use current_room attribute (not current_room_id)
                        npcs_checked = 0
                        npcs_matched = 0
                        for npc_id, npc_instance in active_npcs_dict.items():
                            npcs_checked += 1
                            # Check both current_room and current_room_id for compatibility
                            current_room = getattr(npc_instance, "current_room", None)
                            current_room_id = getattr(npc_instance, "current_room_id", None)
                            npc_room_id = current_room or current_room_id
                            npc_name = getattr(npc_instance, "name", "Unknown")

                            self._logger.debug(
                                "Checking NPC for room match",
                                room_id=room_id,
                                npc_id=npc_id,
                                npc_name=npc_name,
                                npc_current_room=current_room,
                                npc_current_room_id=current_room_id,
                                npc_room_id_used=npc_room_id,
                                matches_room=(npc_room_id == room_id),
                            )

                            if npc_room_id == room_id:
                                npc_ids.append(npc_id)
                                npcs_matched += 1
                                self._logger.info(
                                    "Found NPC in room",
                                    room_id=room_id,
                                    npc_id=npc_id,
                                    npc_name=npc_name,
                                )

                        self._logger.info(
                            "Completed NPC query from lifecycle manager",
                            room_id=room_id,
                            npc_count=len(npc_ids),
                            npcs_checked=npcs_checked,
                            npcs_matched=npcs_matched,
                            npc_ids=npc_ids[:5],  # Log first 5 for debugging
                        )
                    else:
                        self._logger.warning(
                            "Lifecycle manager or active_npcs not available",
                            room_id=room_id,
                            lifecycle_manager_available=(lifecycle_manager is not None),
                            has_active_npcs_attr=(
                                lifecycle_manager is not None and hasattr(lifecycle_manager, "active_npcs")
                            ),
                        )
                else:
                    self._logger.warning(
                        "NPC instance service not available",
                        room_id=room_id,
                        service_available=(npc_instance_service is not None),
                        has_lifecycle_manager_attr=(
                            npc_instance_service is not None and hasattr(npc_instance_service, "lifecycle_manager")
                        ),
                    )
            except Exception as npc_query_error:
                self._logger.error(
                    "Error querying NPCs from lifecycle manager",
                    room_id=room_id,
                    error=str(npc_query_error),
                    error_type=type(npc_query_error).__name__,
                    exc_info=True,
                )
                # Fallback to room.get_npcs() if lifecycle manager query fails
                npc_ids = room.get_npcs() if hasattr(room, "get_npcs") else []
                self._logger.warning(
                    "Fell back to room.get_npcs() after lifecycle manager query failed",
                    room_id=room_id,
                    fallback_npc_count=len(npc_ids),
                )

            # OPTIMIZATION: Batch load all NPC names at once to eliminate N+1 queries
            npc_names = self.connection_manager._get_npcs_batch(list(npc_ids))

            # Convert NPCs to occupant information using batch-loaded names
            for npc_id in npc_ids:
                npc_name = npc_names.get(npc_id, npc_id.split("_")[0].replace("_", " ").title())
                occupant_info = {
                    "npc_id": npc_id,
                    "npc_name": npc_name,
                    "type": "npc",
                }
                occupants.append(occupant_info)

        except Exception as e:
            self._logger.error("Error getting room occupants", error=str(e), exc_info=True)

        return occupants

    def _handle_npc_entered(self, event: NPCEnteredRoom) -> None:
        """
        Handle NPC entering a room.

        This method broadcasts NPC appearance and triggers occupant updates.
        Room state (NPC presence) is mutated only by domain sources (e.g., Room.npc_entered).

        Args:
            event: NPCEnteredRoom event containing NPC and room information
        """
        try:
            self._logger.info("NPC entered room", npc_id=event.npc_id, room_id=event.room_id)

            # Get the room from persistence
            persistence = self.connection_manager.persistence
            if not persistence:
                self._logger.warning("Persistence layer not available for NPC room entry")
                return

            room = persistence.get_room(event.room_id)
            if not room:
                self._logger.warning("Room not found for NPC entry", room_id=event.room_id)
                return

            # Get the NPC's spawn message from behavior_config (if available)
            spawn_message = self._get_npc_spawn_message(event.npc_id)
            if spawn_message:
                # Send the spawn message to all players in the room
                self._send_room_message(event.room_id, spawn_message)

            # Schedule room update broadcast (async operation)
            import asyncio

            try:
                # Use get_running_loop() instead of deprecated get_event_loop()
                # get_running_loop() raises RuntimeError if no loop is running
                _ = asyncio.get_running_loop()  # Verify loop exists
                # Schedule the async operation to run later
                if self.task_registry:
                    self.task_registry.register_task(
                        self._send_room_occupants_update(event.room_id),
                        f"event_handler/room_occupants_{event.room_id}",
                        "event_handler",
                    )
                else:
                    # Task 4.4: Replace with tracked task creation to prevent memory leaks
                    tracked_manager = get_global_tracked_manager()
                    tracked_manager.create_tracked_task(
                        self._send_room_occupants_update(event.room_id),
                        task_name=f"event_handler/room_occupants_{event.room_id}",
                        task_type="event_handler",
                    )
            except RuntimeError:
                # No running event loop - log and skip async operation
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug("Processed NPC entered event", npc_id=event.npc_id, room_id=event.room_id)

        except Exception as e:
            self._logger.error("Error handling NPC entered room event", error=str(e), exc_info=True)

    def _handle_npc_left(self, event: NPCLeftRoom) -> None:
        """
        Handle NPC leaving a room.

        This method triggers occupant updates. Room state is mutated by domain sources only.

        Args:
            event: NPCLeftRoom event containing NPC and room information
        """
        try:
            self._logger.info("NPC left room", npc_id=event.npc_id, room_id=event.room_id)

            # Get the room from persistence
            persistence = self.connection_manager.persistence
            if not persistence:
                self._logger.warning("Persistence layer not available for NPC room exit")
                return

            room = persistence.get_room(event.room_id)
            if not room:
                self._logger.warning("Room not found for NPC exit", room_id=event.room_id)
                return

            # Schedule room update broadcast (async operation)
            import asyncio

            try:
                # Use get_running_loop() instead of deprecated get_event_loop()
                # get_running_loop() raises RuntimeError if no loop is running
                _ = asyncio.get_running_loop()  # Verify loop exists
                # Schedule the async operation to run later
                if self.task_registry:
                    self.task_registry.register_task(
                        self._send_room_occupants_update(event.room_id),
                        f"event_handler/room_occupants_{event.room_id}",
                        "event_handler",
                    )
                else:
                    # Task 4.4: Replace with tracked task creation to prevent memory leaks
                    tracked_manager = get_global_tracked_manager()
                    tracked_manager.create_tracked_task(
                        self._send_room_occupants_update(event.room_id),
                        task_name=f"event_handler/room_occupants_{event.room_id}",
                        task_type="event_handler",
                    )
            except RuntimeError:
                # No running event loop - log and skip async operation
                self._logger.debug("No event loop available for room occupants update broadcast")

            self._logger.debug("Processed NPC left event", npc_id=event.npc_id, room_id=event.room_id)

        except Exception as e:
            self._logger.error("Error handling NPC left room event", error=str(e), exc_info=True)

    def shutdown(self) -> None:
        """Shutdown the event handler."""
        self._logger.info("Shutting down RealTimeEventHandler")
        # Note: EventBus will handle its own shutdown

    async def _handle_player_xp_awarded(self, event: PlayerXPAwardEvent) -> None:
        """
        Handle player XP award events by sending updates to the client.

        Args:
            event: The PlayerXPAwardEvent containing XP award information
        """
        try:
            player_id_str = str(event.player_id)

            # Get the current player data to send updated XP
            player = self.connection_manager._get_player(player_id_str)
            if not player:
                self._logger.warning("Player not found for XP award event", player_id=player_id_str)
                return

            # Create player update event with new XP
            player_update_data = {
                "player_id": player_id_str,
                "name": player.name,
                "level": player.level,
                "xp": player.experience_points,
                "current_room_id": getattr(player, "current_room_id", None),
            }

            # Send personal message to the player
            from .envelope import build_event

            xp_update_event = build_event(
                "player_xp_updated",
                {
                    "xp_amount": event.xp_amount,
                    "new_level": event.new_level,
                    "player": player_update_data,
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, xp_update_event)

            self._logger.info(
                "Sent XP award update to player",
                player_id=player_id_str,
                xp_amount=event.xp_amount,
                new_level=event.new_level,
            )

        except Exception as e:
            self._logger.error("Error handling player XP award event", error=str(e), exc_info=True)

    def _get_npc_spawn_message(self, npc_id: str) -> str | None:
        """
        Get the spawn message for an NPC from its behavior_config.

        If no custom spawn message is defined, returns a default message: "<npc-name> appears."

        Args:
            npc_id: The NPC ID

        Returns:
            Spawn message (custom or default), or None if NPC not found
        """
        try:
            # Get the NPC instance from the lifecycle manager
            from ..services.npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if not npc_instance_service or not hasattr(npc_instance_service, "lifecycle_manager"):
                return None

            lifecycle_manager = npc_instance_service.lifecycle_manager
            if not lifecycle_manager or npc_id not in lifecycle_manager.active_npcs:
                return None

            npc_instance = lifecycle_manager.active_npcs[npc_id]

            # Get the NPC name for the default message
            npc_name = getattr(npc_instance, "name", "An NPC")

            # Get the behavior_config from the NPC instance
            behavior_config = getattr(npc_instance, "behavior_config", None)
            if behavior_config:
                # Parse the behavior_config if it's a JSON string
                import json

                if isinstance(behavior_config, str):
                    try:
                        behavior_config = json.loads(behavior_config)
                    except (json.JSONDecodeError, ValueError):
                        # If parsing fails, use default message
                        return f"{npc_name} appears."

                # Get the spawn_message from the behavior_config
                spawn_message = behavior_config.get("spawn_message")
                if spawn_message:
                    return cast(str, spawn_message)

            # Return default message if no custom message is defined
            return f"{npc_name} appears."

        except Exception as e:
            self._logger.debug("Error getting NPC spawn message", npc_id=npc_id, error=str(e))
            return None

    def _send_room_message(self, room_id: str, message: str) -> None:
        """
        Send a message to all players in a room.

        Args:
            room_id: The room ID
            message: The message to send
        """
        try:
            # Get all players in the room
            from ..persistence import get_persistence
            from .envelope import build_event

            persistence = get_persistence()
            room = persistence.get_room(room_id)
            if not room:
                self._logger.warning("Room not found for sending room message", room_id=room_id)
                return

            # Get all player IDs in the room
            player_ids = list(room._players)  # Get the player IDs from the room

            # Send the message to each player in the room
            import asyncio

            for player_id in player_ids:
                # Create the message event
                message_event = build_event(
                    "room_message",
                    {
                        "message": message,
                        "room_id": room_id,
                        "message_type": "npc_spawn",
                    },
                    player_id=player_id,
                )

                # Schedule the async message send
                try:
                    # Use get_running_loop() instead of deprecated get_event_loop()
                    # get_running_loop() raises RuntimeError if no loop is running
                    _ = asyncio.get_running_loop()  # Verify loop exists
                    # Create a task to send the message
                    if self.task_registry:
                        self.task_registry.register_task(
                            self.connection_manager.send_personal_message(player_id, message_event),
                            f"event_handler/room_message_{room_id}_{player_id}",
                            "event_handler",
                        )
                    else:
                        from ..async_utils.tracked_task_manager import get_global_tracked_manager

                        tracked_manager = get_global_tracked_manager()
                        tracked_manager.create_tracked_task(
                            self.connection_manager.send_personal_message(player_id, message_event),
                            task_name=f"event_handler/room_message_{room_id}_{player_id}",
                            task_type="event_handler",
                        )
                except RuntimeError:
                    # No running event loop - log and skip async operation
                    self._logger.debug("No event loop available for room message broadcast")

        except Exception as e:
            self._logger.error("Error sending room message", room_id=room_id, error=str(e), exc_info=True)

    async def _handle_player_hp_updated(self, event: PlayerHPUpdated) -> None:
        """
        Handle player HP update events by sending updates to the client.

        Args:
            event: The PlayerHPUpdated event containing HP change information
        """
        try:
            # CRITICAL DEBUG: Log at the very start to verify handler is being called
            self._logger.info(
                "_handle_player_hp_updated called",
                event_type=type(event).__name__,
                player_id=event.player_id,
                old_hp=event.old_hp,
                new_hp=event.new_hp,
                max_hp=event.max_hp,
            )
            player_id_str = event.player_id
            self._logger.info(
                "Received PlayerHPUpdated event",
                player_id=player_id_str,
                old_hp=event.old_hp,
                new_hp=event.new_hp,
                max_hp=event.max_hp,
                damage_taken=event.damage_taken,
            )

            # Check if connection manager is available
            if not self.connection_manager:
                self._logger.error(
                    "Connection manager is not available for HP update",
                    player_id=player_id_str,
                )
                return

            # Get the current player data to send updated HP and stats
            # CRITICAL: Try to get player from connection manager, but if not found,
            # still send the HP update event with the data from the event itself
            player = self.connection_manager._get_player(player_id_str)

            # Get full player stats including posture/position
            if player:
                stats = player.get_stats() if hasattr(player, "get_stats") else {}
                player_name = player.name
                current_room_id = getattr(player, "current_room_id", None)
            else:
                # Player not in connection manager - use event data only
                self._logger.debug(
                    "Player not in connection manager for HP update, using event data only",
                    player_id=player_id_str,
                )
                stats = {}  # Will be updated from player_update event if available
                player_name = "Unknown"  # Will be updated from player_update event if available
                current_room_id = None

            # Create player update event with new HP and full stats
            player_update_data = {
                "player_id": player_id_str,
                "name": player_name,
                "health": event.new_hp,
                "max_health": event.max_hp,
                "current_room_id": current_room_id,
                "stats": {
                    **stats,
                    "current_health": event.new_hp,
                    "max_health": event.max_hp,
                },  # Ensure HP is set even if stats are empty
            }

            # Send personal message to the player
            from .envelope import build_event

            hp_update_event = build_event(
                "player_hp_updated",
                {
                    "old_hp": event.old_hp,
                    "new_hp": event.new_hp,
                    "max_hp": event.max_hp,
                    "damage_taken": event.damage_taken,
                    "player": player_update_data,
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, hp_update_event)

            self._logger.info(
                "Sent HP update to player",
                player_id=player_id_str,
                old_hp=event.old_hp,
                new_hp=event.new_hp,
                damage_taken=event.damage_taken,
            )

        except Exception as e:
            self._logger.error("Error handling player HP update event", error=str(e), exc_info=True)

    async def _handle_player_died(self, event: Any) -> None:
        """
        Handle player death events by sending death notification to the client.

        Args:
            event: The PlayerDiedEvent containing death information
        """
        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # Send personal message to the player
            from .envelope import build_event

            death_event = build_event(
                "player_died",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "death_location": event.death_location
                    or event.room_id,  # Use death_location if available, fallback to room_id
                    "killer_id": event.killer_id,
                    "killer_name": event.killer_name,
                    "message": "You have died. The darkness claims you utterly.",
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, death_event)

            self._logger.info("Sent death notification to player", player_id=player_id_str, room_id=event.room_id)

        except Exception as e:
            self._logger.error("Error handling player died event", error=str(e), exc_info=True)

    async def _handle_player_hp_decay(self, event: Any) -> None:
        """
        Handle player HP decay events by sending decay notification to the client.

        Args:
            event: The PlayerHPDecayEvent containing HP decay information
        """
        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # Send personal message to the player
            from .envelope import build_event

            decay_event = build_event(
                "player_hp_decay",
                {
                    "player_id": player_id_str,
                    "old_hp": event.old_hp,
                    "new_hp": event.new_hp,
                    "decay_amount": event.decay_amount,
                    "room_id": event.room_id,
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, decay_event)

            self._logger.debug("Sent HP decay notification to player", player_id=player_id_str, new_hp=event.new_hp)

        except Exception as e:
            self._logger.error("Error handling player HP decay event", error=str(e), exc_info=True)

    async def _handle_player_respawned(self, event: Any) -> None:
        """
        Handle player respawn events by sending respawn notification to the client.

        Args:
            event: The PlayerRespawnedEvent containing respawn information
        """
        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # BUGFIX: Get updated player data to include in event payload
            # As documented in "Resurrection and Client State Synchronization" - Dr. Armitage, 1930
            # Client must receive updated player state including corrected posture after respawn
            player_data = None
            updated_position = "standing"
            if self.connection_manager and hasattr(self.connection_manager, "persistence"):
                persistence = self.connection_manager.persistence
                if persistence:
                    try:
                        # Get player from persistence to retrieve updated stats including position
                        player = persistence.get_player(uuid.UUID(player_id_str))
                        if player:
                            stats = player.get_stats()
                            updated_position = stats.get("position", "standing")

                            # BUGFIX: Update connection manager's in-memory position state
                            # As documented in "Resurrection and In-Memory State Synchronization" - Dr. Armitage, 1930
                            # Connection manager's online_players tracking must reflect correct posture after respawn
                            if hasattr(self.connection_manager, "online_players"):
                                player_uuid = uuid.UUID(player_id_str)
                                if player_uuid in self.connection_manager.online_players:
                                    self.connection_manager.online_players[player_uuid]["position"] = updated_position
                                    self._logger.debug(
                                        "Updated connection manager position state",
                                        player_id=player_id_str,
                                        position=updated_position,
                                    )

                            # Convert player to client-expected format
                            player_data = {
                                "id": str(player.player_id),
                                "name": player.name,
                                "level": player.level,
                                "xp": player.experience_points,
                                "stats": {
                                    "current_health": stats.get("current_health", 100),
                                    "max_health": stats.get("max_health", 100),
                                    "sanity": stats.get("sanity", 100),
                                    "max_sanity": stats.get("max_sanity", 100),
                                    "strength": stats.get("strength"),
                                    "dexterity": stats.get("dexterity"),
                                    "constitution": stats.get("constitution"),
                                    "intelligence": stats.get("intelligence"),
                                    "wisdom": stats.get("wisdom"),
                                    "charisma": stats.get("charisma"),
                                    "occult_knowledge": stats.get("occult_knowledge", 0),
                                    "fear": stats.get("fear", 0),
                                    "corruption": stats.get("corruption", 0),
                                    "cult_affiliation": stats.get("cult_affiliation", 0),
                                    "position": updated_position,  # CRITICAL: Include updated position
                                },
                                "position": updated_position,  # Also include at top level for compatibility
                                "in_combat": False,  # Combat state cleared during respawn
                            }
                            self._logger.debug(
                                "Retrieved player data for respawn event",
                                player_id=player_id_str,
                                position=updated_position,
                            )
                    except Exception as e:
                        self._logger.warning(
                            "Failed to retrieve player data for respawn event",
                            player_id=player_id_str,
                            error=str(e),
                        )

            # Send personal message to the player
            from .envelope import build_event

            respawn_event = build_event(
                "player_respawned",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "respawn_room_id": event.respawn_room_id,
                    "old_hp": event.old_hp,
                    "new_hp": event.new_hp,
                    "message": "The sanitarium calls you back from the threshold. You have been restored to life.",
                    "player": player_data,  # BUGFIX: Include updated player data with corrected posture
                },
                player_id=player_id_str,
            )

            await self.connection_manager.send_personal_message(player_id_str, respawn_event)

            self._logger.info(
                "Sent respawn notification to player",
                player_id=player_id_str,
                respawn_room=event.respawn_room_id,
                player_data_included=player_data is not None,
            )

        except Exception as e:
            self._logger.error("Error handling player respawn event", error=str(e), exc_info=True)


# AI Agent: Global singleton removed - use ApplicationContainer.real_time_event_handler instead
# Migration complete: All code now uses dependency injection via container
