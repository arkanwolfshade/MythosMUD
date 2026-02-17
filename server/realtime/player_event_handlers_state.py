"""
Player state update event handlers.

This module handles player state updates (XP, DP, death, decay).
"""

import uuid
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..events.event_types import PlayerDPUpdated
from ..services.player_combat_service import PlayerXPAwardEvent
from .player_event_handlers_utils import PlayerEventHandlerUtils


class PlayerStateEventHandler:
    """Handles player state update events (XP, DP, death, decay)."""

    def __init__(
        self,
        connection_manager: Any,
        utils: PlayerEventHandlerUtils,
        logger: Any,
    ) -> None:
        """
        Initialize state event handler.

        Args:
            connection_manager: ConnectionManager instance
            utils: PlayerEventHandlerUtils instance
            logger: Logger instance
        """
        self.connection_manager = connection_manager
        self.utils = utils
        self._logger = logger

    async def handle_player_xp_awarded(self, event: PlayerXPAwardEvent) -> None:
        """
        Handle player XP award events by sending updates to the client.

        Args:
            event: The PlayerXPAwardEvent containing XP award information
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player XP awarded event", player_id=event.player_id
            )
            return

        try:
            player_id_str = str(event.player_id)

            # Get the current player data to send updated XP
            player = await self.connection_manager.get_player(uuid.UUID(player_id_str))
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

            # ARCHITECTURE: Server-initiated events (XP updates) sent via WebSocket
            await self.connection_manager.send_personal_message(
                player_id_str,
                xp_update_event,
            )

            self._logger.info(
                "Sent XP award update to player",
                player_id=player_id_str,
                xp_amount=event.xp_amount,
                new_level=event.new_level,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player XP award event", error=str(e), exc_info=True)

    async def handle_player_dp_updated(self, event: PlayerDPUpdated) -> None:
        """
        Handle player DP update events by sending updates to the client.

        Args:
            event: The PlayerDPUpdated event containing DP change information
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player DP updated event", player_id=event.player_id
            )
            return

        try:
            # CRITICAL DEBUG: Log at the very start to verify handler is being called
            self._logger.info(
                "handle_player_dp_updated called",
                event_type=type(event).__name__,
                player_id=event.player_id,
                old_dp=event.old_dp,
                new_dp=event.new_dp,
                max_dp=event.max_dp,
            )
            # event.player_id is now UUID (changed from str to match codebase)
            player_id = event.player_id
            player_id_str = str(player_id)  # For logging and string operations
            self._logger.info(
                "Received PlayerDPUpdated event",
                player_id=player_id_str,
                old_dp=event.old_dp,
                new_dp=event.new_dp,
                max_dp=event.max_dp,
                damage_taken=event.damage_taken,
            )

            # Check if connection manager is available
            if not self.connection_manager:
                self._logger.error(
                    "Connection manager is not available for DP update",
                    player_id=player_id_str,
                )
                return

            # Get the current player data to send updated DP and stats
            # CRITICAL: Try to get player from connection manager, but if not found,
            # still send the DP update event with the data from the event itself
            # get_player expects UUID, and event.player_id is now UUID
            player = await self.connection_manager.get_player(player_id)

            # Get full player stats including posture/position
            if player:
                stats = player.get_stats() if hasattr(player, "get_stats") else {}
                player_name = player.name
                current_room_id = getattr(player, "current_room_id", None)
            else:
                # Player not in connection manager - use event data only
                self._logger.debug(
                    "Player not in connection manager for DP update, using event data only",
                    player_id=player_id_str,
                )
                stats = {}  # Will be updated from player_update event if available
                player_name = "Unknown"  # Will be updated from player_update event if available
                current_room_id = None

            # Posture: when DP <= 0 player is incapacitated and prone (lying)
            position = stats.get("position") if isinstance(stats, dict) else None
            if event.new_dp <= 0:
                posture = "lying"
            elif position is not None:
                posture = getattr(position, "value", str(position)) if hasattr(position, "value") else str(position)
            else:
                posture = "standing"

            # #region agent log
            try:
                import json

                with open("e:\\projects\\GitHub\\MythosMUD\\.cursor\\debug.log", "a", encoding="utf-8") as _f:
                    _f.write(
                        json.dumps(
                            {
                                "hypothesisId": "H1",
                                "location": "player_event_handlers_state:DP_update",
                                "message": "DP update sending posture to client",
                                "data": {"new_dp": event.new_dp, "posture": posture, "stats_position": position},
                                "timestamp": __import__("time", fromlist=["time"]).time() * 1000,
                            },
                            ensure_ascii=True,
                        )
                        + "\n"
                    )
            except (OSError, TypeError, AttributeError, ValueError):
                # Debug log must never affect DP update flow; absorb file/serialization errors
                pass
            # #endregion

            # Create player update event with new DP and full stats
            player_update_data = {
                "player_id": player_id_str,
                "name": player_name,
                "dp": event.new_dp,
                "max_dp": event.max_dp,
                "current_room_id": current_room_id,
                "stats": {
                    **stats,
                    "current_dp": event.new_dp,
                    "max_dp": event.max_dp,
                    "position": posture,
                },  # Ensure DP is set even if stats are empty
            }

            # Send personal message to the player
            from .envelope import build_event

            dp_update_event = build_event(
                "player_dp_updated",
                {
                    "old_dp": event.old_dp,
                    "new_dp": event.new_dp,
                    "max_dp": event.max_dp,
                    "damage_taken": event.damage_taken,
                    "posture": posture,
                    "player": player_update_data,
                },
                player_id=player_id_str,
            )

            # player_id is now UUID (changed from str to match codebase), so we can use it directly
            # ARCHITECTURE: Server-initiated events (DP updates) sent via WebSocket
            await self.connection_manager.send_personal_message(
                player_id,
                dp_update_event,
            )

            self._logger.info(
                "Sent DP update to player",
                player_id=player_id_str,
                old_dp=event.old_dp,
                new_dp=event.new_dp,
                damage_taken=event.damage_taken,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player DP update event", error=str(e), exc_info=True)

    async def handle_player_died(self, event: Any) -> None:
        """
        Handle player death events by sending death notification to the client.

        Args:
            event: The PlayerDiedEvent containing death information
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player died event",
                player_id=getattr(event, "player_id", None),
            )
            return

        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # Send personal message to the player
            from .envelope import build_event

            death_location_value = event.death_location or event.room_id
            # Client requires current_dp <= -10 to show respawn modal; we only send death at -10
            death_event = build_event(
                "player_died",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "death_location": death_location_value,  # Use death_location if available, fallback to room_id
                    "current_dp": -10,  # Death is only sent at -10 DP so client can gate modal
                    "killer_id": event.killer_id,
                    "killer_name": event.killer_name,
                    "message": "You have died. The darkness claims you utterly.",
                },
                player_id=player_id_str,
            )

            # ARCHITECTURE: Server-initiated events (death) sent via WebSocket
            # CRITICAL FIX: Convert player_id_str to UUID for send_personal_message
            from uuid import UUID

            try:
                player_id_uuid = UUID(player_id_str) if isinstance(player_id_str, str) else player_id_str
                delivery_status = await self.connection_manager.send_personal_message(
                    player_id_uuid,
                    death_event,
                )
                self._logger.info(
                    "Sent death notification to player",
                    player_id=player_id_str,
                    room_id=event.room_id,
                    delivery_status=delivery_status,
                )
            except (ValueError, TypeError) as uuid_error:
                self._logger.error(
                    "Failed to send death notification - invalid player_id format",
                    player_id=player_id_str,
                    error=str(uuid_error),
                    exc_info=True,
                )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player died event", error=str(e), exc_info=True)

    async def handle_player_dp_decay(self, event: Any) -> None:
        """
        Handle player DP decay events by sending decay notification to the client.

        Args:
            event: The PlayerDPDecayEvent containing DP decay information
        """
        # Defensive check: if no connection_manager, skip handling
        if not self.connection_manager:
            self._logger.debug(
                "Connection manager not available, skipping player DP decay event",
                player_id=getattr(event, "player_id", None),
            )
            return

        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # Send personal message to the player
            from .envelope import build_event

            decay_event = build_event(
                "player_dp_decay",
                {
                    "player_id": player_id_str,
                    "old_dp": event.old_dp,
                    "new_dp": event.new_dp,
                    "decay_amount": event.decay_amount,
                    "room_id": event.room_id,
                },
                player_id=player_id_str,
            )

            # ARCHITECTURE: Server-initiated events (DP decay) sent via WebSocket
            await self.connection_manager.send_personal_message(
                player_id_str,
                decay_event,
            )

            self._logger.debug("Sent DP decay notification to player", player_id=player_id_str, new_dp=event.new_dp)

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player DP decay event", error=str(e), exc_info=True)
