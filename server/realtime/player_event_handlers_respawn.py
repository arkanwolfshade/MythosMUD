"""
Player respawn event handlers.

This module handles player respawn and delirium respawn events.
"""

import asyncio
import uuid
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from .player_event_handlers_utils import PlayerEventHandlerUtils


class PlayerRespawnEventHandler:
    """Handles player respawn events (respawn, delirium respawn)."""

    def __init__(
        self,
        connection_manager: Any,
        utils: PlayerEventHandlerUtils,
        logger: Any,
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
        if not hasattr(self.connection_manager, "online_players"):
            return

        player_uuid = uuid.UUID(player_id_str)
        if player_uuid in self.connection_manager.online_players:
            self.connection_manager.online_players[player_uuid]["position"] = updated_position
            self._logger.debug(
                "Updated connection manager position state",
                player_id=player_id_str,
                position=updated_position,
            )

    async def get_player_data_for_respawn(self, player_id_str: str) -> tuple[dict[str, Any] | None, str]:
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

        async_persistence = self.connection_manager.async_persistence
        if not async_persistence:
            return None, "standing"

        try:
            player = await async_persistence.get_player_by_id(uuid.UUID(player_id_str))
            if not player:
                return None, "standing"

            stats = player.get_stats()
            updated_position = stats.get("position", "standing")

            # Update connection manager's in-memory position state
            self.update_connection_manager_position(player_id_str, updated_position)

            # Convert player to client-expected format
            player_data = {
                "id": str(player.player_id),
                "name": player.name,
                "level": player.level,
                "xp": player.experience_points,
                "stats": {
                    "current_dp": stats.get("current_dp", 100),
                    "max_dp": stats.get("max_dp", 100),
                    "lucidity": stats.get("lucidity", 100),
                    "max_lucidity": stats.get("max_lucidity", 100),
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
            return player_data, updated_position
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.warning(
                "Failed to retrieve player data for respawn event",
                player_id=player_id_str,
                error=str(e),
            )
            return None, "standing"

    async def send_respawn_event_with_retry(
        self, player_id_uuid: uuid.UUID, respawn_event: dict[str, Any], max_wait_time: float = 2.0
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
        poll_interval = 0.05  # Check connection every 50ms
        max_polls = int(max_wait_time / poll_interval)  # 40 polls over 2 seconds

        for _poll_count in range(max_polls):
            has_websocket = player_id_uuid in self.connection_manager.player_websockets

            if not has_websocket:
                await asyncio.sleep(poll_interval)
                continue

            # Connection available - try sending immediately
            # ARCHITECTURE: Server-initiated events (respawn) sent via WebSocket
            delivery_status = await self.connection_manager.send_personal_message(
                player_id_uuid,
                respawn_event,
            )
            # Check if message was actually delivered
            websocket_delivered = delivery_status.get("websocket_delivered", 0) > 0
            active_connections = delivery_status.get("active_connections", 0)
            if websocket_delivered and active_connections > 0:
                # Message actually delivered to active connection
                return

            # Wait before next poll
            await asyncio.sleep(poll_interval)

    async def handle_player_respawned(self, event: Any) -> None:
        """
        Handle player respawn events by sending respawn notification to the client.

        Args:
            event: The PlayerRespawnedEvent containing respawn information
        """
        try:
            # Convert UUID to string for build_event (which expects str)
            player_id_str = str(event.player_id)

            # Get updated player data to include in event payload
            player_data, _ = await self.get_player_data_for_respawn(player_id_str)

            # Send personal message to the player
            from .envelope import build_event

            respawn_event = build_event(
                "player_respawned",
                {
                    "player_id": player_id_str,
                    "player_name": event.player_name,
                    "respawn_room_id": event.respawn_room_id,
                    "old_dp": event.old_dp,
                    "new_dp": event.new_dp,
                    "message": "The sanitarium calls you back from the threshold. You have been restored to life.",
                    "player": player_data,  # BUGFIX: Include updated player data with corrected posture
                },
                player_id=player_id_str,
            )

            # Retry sending respawn event to handle temporary connection unavailability
            player_id_uuid = uuid.UUID(player_id_str)
            await self.send_respawn_event_with_retry(player_id_uuid, respawn_event)

            self._logger.info(
                "Sent respawn notification to player",
                player_id=player_id_str,
                respawn_room=event.respawn_room_id,
                player_data_included=player_data is not None,
            )

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.error("Error handling player respawn event", error=str(e), exc_info=True)

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

    async def get_player_data_for_delirium_respawn(
        self, player_id_str: str, default_lucidity: int
    ) -> tuple[dict[str, Any] | None, str]:
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

        async_persistence = self.connection_manager.async_persistence
        if not async_persistence:
            return None, "standing"

        try:
            player = await async_persistence.get_player_by_id(uuid.UUID(player_id_str))
            if not player:
                return None, "standing"

            stats = player.get_stats()
            updated_position = stats.get("position", "standing")

            # Update connection manager's in-memory position state
            self.update_connection_manager_position(player_id_str, updated_position)

            # Get updated lucidity from PlayerLucidity table
            player_uuid = uuid.UUID(player_id_str)
            current_lucidity = await self.get_current_lucidity(player_uuid, default_lucidity)

            # Convert player to client-expected format
            player_data = {
                "id": str(player.player_id),
                "name": player.name,
                "level": player.level,
                "xp": player.experience_points,
                "stats": {
                    "current_dp": stats.get("current_dp", 100),
                    "max_dp": stats.get("max_dp", 100),
                    "lucidity": current_lucidity,
                    "max_lucidity": stats.get("max_lucidity", 100),
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
                    "position": updated_position,
                },
                "position": updated_position,
                "in_combat": False,  # Combat state cleared during respawn
            }
            self._logger.debug(
                "Retrieved player data for delirium respawn event",
                player_id=player_id_str,
                position=updated_position,
                lucidity=current_lucidity,
            )
            return player_data, updated_position
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            self._logger.warning(
                "Failed to retrieve player data for delirium respawn event",
                player_id=player_id_str,
                error=str(e),
            )
            return None, "standing"

    async def handle_player_delirium_respawned(self, event: Any) -> None:
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
