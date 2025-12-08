"""
Player Respawn Service for managing player resurrection and limbo state.

This service handles player death transitions, limbo room placement, and respawn mechanics.
As documented in the Pnakotic Manuscripts, resurrection requires careful navigation of
the spaces between worlds.
"""

import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from server.events.event_types import PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from server.logging.enhanced_logging_config import get_logger
from server.models.game import PositionState
from server.models.player import Player


def _utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


logger = get_logger(__name__)

# Default respawn location (Arkham Sanitarium foyer)
DEFAULT_RESPAWN_ROOM = "earth_arkhamcity_sanitarium_room_foyer_001"

# Limbo room for death state isolation
# NOTE: Room ID is generated as {plane}_{zone}_{sub_zone}_{stable_id}
# For limbo room: limbo_death_void_limbo_death_void
LIMBO_ROOM_ID = "limbo_death_void_limbo_death_void"


class PlayerRespawnService:
    """
    Service for managing player respawn and limbo state.

    This service handles:
    - Moving dead players to limbo (isolated from game world)
    - Determining respawn location (custom or default)
    - Restoring player HP and moving to respawn room
    - Publishing respawn events for UI updates
    - Clearing combat state when player respawns
    """

    def __init__(self, event_bus: Any = None, player_combat_service: Any = None) -> None:
        """
        Initialize the player respawn service.

        Args:
            event_bus: Optional event bus for publishing events
            player_combat_service: Optional player combat service for clearing combat state
        """
        self._event_bus = event_bus
        self._player_combat_service = player_combat_service
        logger.info(
            "PlayerRespawnService initialized",
            event_bus_available=bool(event_bus),
            player_combat_service_available=bool(player_combat_service),
        )

    async def move_player_to_limbo(self, player_id: uuid.UUID, death_location: str, session: AsyncSession) -> bool:
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
            player.current_room_id = LIMBO_ROOM_ID  # type: ignore[assignment]

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

    async def get_respawn_room(self, player_id: uuid.UUID, session: AsyncSession) -> str:
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

    async def respawn_player(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Respawn a dead player at their respawn location with full HP.

        This method:
        1. Restores player HP to their max_health (not hardcoded 100)
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

            # Get current stats and restore HP to max health
            stats = player.get_stats()
            old_hp = stats.get("current_health", -10)
            max_hp = stats.get("max_health", 100)  # Default to 100 if max_health not found
            stats["current_health"] = max_hp  # Restore to max health, not hardcoded 100

            # BUGFIX: Restore posture to standing when player respawns
            # As documented in "Resurrection and Corporeal Restoration" - Dr. Armitage, 1930
            # Upon resurrection, the body is restored to full function including upright posture
            stats["position"] = PositionState.STANDING

            # Update player stats and location
            player.set_stats(stats)
            old_room = player.current_room_id
            player.current_room_id = respawn_room  # type: ignore[assignment]

            # BUGFIX #244: Clear player combat state when they respawn
            # As documented in "Resurrection and Combat Continuity" - Dr. Armitage, 1930
            # Combat state must be cleared upon resurrection to prevent dimensional entanglement
            if self._player_combat_service:
                try:
                    await self._player_combat_service.clear_player_combat_state(player_id)
                    logger.info("Cleared combat state for respawned player", player_id=player_id)
                except Exception as e:
                    logger.error(
                        "Error clearing combat state for respawned player",
                        player_id=player_id,
                        error=str(e),
                        exc_info=True,
                    )

            # Commit changes using async API
            await session.commit()

            logger.info(
                "Player respawned",
                player_id=player_id,
                player_name=player.name,
                respawn_room=respawn_room,
                old_hp=old_hp,
                new_hp=max_hp,
                max_hp=max_hp,
                from_limbo=old_room == LIMBO_ROOM_ID,
            )

            # Publish respawn event if event bus is available
            if self._event_bus:
                event = PlayerRespawnedEvent(
                    player_id=player_id,
                    player_name=str(player.name),
                    respawn_room_id=respawn_room,
                    old_hp=old_hp,
                    new_hp=max_hp,  # Use max_hp instead of hardcoded 100
                    death_room_id=old_room if old_room != LIMBO_ROOM_ID else None,  # type: ignore[arg-type]
                )
                self._event_bus.publish(event)

            return True

        except Exception as e:
            logger.error("Error respawning player", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False

    async def respawn_player_from_delirium(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Respawn a delirious player at the Sanitarium with restored lucidity.

        This method:
        1. Sets player lucidity to 10
        2. Moves player to Sanitarium (default respawn room)
        3. Publishes delirium respawn event for UI updates

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
                logger.warning("Player not found for delirium respawn", player_id=player_id)
                return False

            # Get current lucidity from PlayerLucidity table
            from ..models.lucidity import PlayerLucidity

            lucidity_record = await session.get(PlayerLucidity, player_id)
            if not lucidity_record:
                logger.warning("Lucidity record not found for delirium respawn", player_id=player_id)
                return False

            old_lucidity = lucidity_record.current_lcd
            new_lucidity = 10  # Restore to 10 lucidity after delirium respawn

            # Update lucidity
            lucidity_record.current_lcd = new_lucidity
            lucidity_record.current_tier = "lucid"  # Reset tier to lucid
            lucidity_record.last_updated_at = _utc_now()

            # Get respawn room (always Sanitarium for delirium respawn)
            respawn_room = DEFAULT_RESPAWN_ROOM

            # Get current stats and ensure posture is standing
            stats = player.get_stats()
            stats["position"] = PositionState.STANDING

            # Update player stats and location
            player.set_stats(stats)
            old_room = player.current_room_id
            player.current_room_id = respawn_room  # type: ignore[assignment]

            # Clear player combat state when they respawn from delirium
            if self._player_combat_service:
                try:
                    await self._player_combat_service.clear_player_combat_state(player_id)
                    logger.info("Cleared combat state for delirium respawned player", player_id=player_id)
                except Exception as e:
                    logger.error(
                        "Error clearing combat state for delirium respawned player",
                        player_id=player_id,
                        error=str(e),
                        exc_info=True,
                    )

            # Commit changes using async API
            await session.commit()

            logger.info(
                "Player respawned from delirium",
                player_id=player_id,
                player_name=player.name,
                respawn_room=respawn_room,
                old_lucidity=old_lucidity,
                new_lucidity=new_lucidity,
                from_room=old_room,
            )

            # Publish delirium respawn event if event bus is available
            if self._event_bus:
                event = PlayerDeliriumRespawnedEvent(
                    player_id=player_id,
                    player_name=str(player.name),
                    respawn_room_id=respawn_room,
                    old_lucidity=old_lucidity,
                    new_lucidity=new_lucidity,
                    delirium_location=old_room if old_room != LIMBO_ROOM_ID else None,  # type: ignore[arg-type]
                )
                self._event_bus.publish(event)

            return True

        except Exception as e:
            logger.error("Error respawning player from delirium", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
