"""
Player Respawn Service for managing player resurrection and limbo state.

This service handles player death transitions, limbo room placement, and respawn mechanics.
As documented in the Pnakotic Manuscripts, resurrection requires careful navigation of
the spaces between worlds.
"""

from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from server.events.event_types import PlayerRespawnedEvent
from server.logging.enhanced_logging_config import get_logger
from server.models.player import Player

logger = get_logger(__name__)

# Default respawn location (Arkham Sanitarium foyer)
DEFAULT_RESPAWN_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"

# Limbo room for death state isolation
LIMBO_ROOM_ID = "limbo_death_void"


class PlayerRespawnService:
    """
    Service for managing player respawn and limbo state.

    This service handles:
    - Moving dead players to limbo (isolated from game world)
    - Determining respawn location (custom or default)
    - Restoring player HP and moving to respawn room
    - Publishing respawn events for UI updates
    """

    def __init__(self, event_bus: Any = None) -> None:
        """
        Initialize the player respawn service.

        Args:
            event_bus: Optional event bus for publishing events
        """
        self._event_bus = event_bus
        logger.info("PlayerRespawnService initialized", event_bus_available=bool(event_bus))

    async def move_player_to_limbo(self, player_id: str, death_location: str, session: AsyncSession) -> bool:
        """
        Move a dead player to the limbo room.

        The limbo room completely isolates the player from the game world
        during the death/respawn sequence.

        Args:
            player_id: ID of the player to move
            death_location: Room ID where the player died (for reference)
            session: Async database session for player data access

        Returns:
            True if player was moved to limbo, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for limbo movement", player_id=player_id)
                return False

            # Move player to limbo room
            old_room = player.current_room_id
            player.current_room_id = LIMBO_ROOM_ID

            # Commit changes using async API
            await session.commit()

            logger.info(
                "Player moved to limbo",
                player_id=player_id,
                player_name=player.name,
                from_room=old_room,
                death_location=death_location,
            )

            return True

        except Exception as e:
            logger.error("Error moving player to limbo", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False

    async def get_respawn_room(self, player_id: str, session: AsyncSession) -> str:
        """
        Get the respawn room for a player.

        Returns the player's custom respawn room if set, otherwise returns
        the default respawn room (Arkham Sanitarium foyer).

        Args:
            player_id: ID of the player
            session: Async database session for player data access

        Returns:
            Room ID for respawn location
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for respawn room lookup, using default", player_id=player_id)
                return DEFAULT_RESPAWN_ROOM

            # Return custom respawn room if set, otherwise default
            respawn_room = player.respawn_room_id
            if respawn_room:
                logger.debug("Using custom respawn room", player_id=player_id, respawn_room=respawn_room)
                return str(respawn_room)
            else:
                logger.debug("Using default respawn room", player_id=player_id, respawn_room=DEFAULT_RESPAWN_ROOM)
                return DEFAULT_RESPAWN_ROOM

        except Exception as e:
            logger.error("Error getting respawn room, using default", player_id=player_id, error=str(e))
            return DEFAULT_RESPAWN_ROOM

    async def respawn_player(self, player_id: str, session: AsyncSession) -> bool:
        """
        Respawn a dead player at their respawn location with full HP.

        This method:
        1. Restores player HP to 100
        2. Moves player from limbo to respawn room
        3. Publishes respawn event for UI updates

        Args:
            player_id: ID of the player to respawn
            session: Database session for player data access

        Returns:
            True if respawn was successful, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for respawn", player_id=player_id)
                return False

            # Get respawn room using async API
            respawn_room = await self.get_respawn_room(player_id, session)

            # Get current stats and restore HP
            stats = player.get_stats()
            old_hp = stats.get("current_health", -10)
            stats["current_health"] = 100

            # Update player stats and location
            player.set_stats(stats)
            old_room = player.current_room_id
            player.current_room_id = respawn_room

            # Commit changes using async API
            await session.commit()

            logger.info(
                "Player respawned",
                player_id=player_id,
                player_name=player.name,
                respawn_room=respawn_room,
                old_hp=old_hp,
                new_hp=100,
                from_limbo=old_room == LIMBO_ROOM_ID,
            )

            # Publish respawn event if event bus is available
            if self._event_bus:
                from datetime import UTC, datetime

                event = PlayerRespawnedEvent(
                    timestamp=datetime.now(UTC),
                    event_type="PlayerRespawnedEvent",
                    player_id=player_id,
                    player_name=player.name,
                    respawn_room_id=respawn_room,
                    old_hp=old_hp,
                    new_hp=100,
                    death_room_id=old_room if old_room != LIMBO_ROOM_ID else None,
                )
                self._event_bus.publish(event)

            return True

        except Exception as e:
            logger.error("Error respawning player", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
