"""
Player Respawn Service for managing player resurrection and limbo state.

This service handles player death transitions, limbo room placement, and respawn mechanics.
As documented in the Pnakotic Manuscripts, resurrection requires careful navigation of
the spaces between worlds.
"""

# pylint: disable=too-many-locals,too-many-statements  # Reason: Respawn service requires many intermediate variables for complex respawn logic. Respawn service legitimately requires many statements for comprehensive respawn operations.

import random
import uuid
from collections.abc import Sequence
from datetime import UTC, datetime, timedelta
from typing import Any

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.events.event_types import PlayerDeliriumRespawnedEvent, PlayerRespawnedEvent
from server.models.game import PositionState
from server.models.lucidity import LucidityActionCode
from server.models.player import Player
from server.structured_logging.enhanced_logging_config import get_logger

from ..exceptions import DatabaseError


def _utc_now() -> datetime:
    """Return naive UTC timestamp suitable for PostgreSQL TIMESTAMP WITHOUT TIME ZONE."""
    return datetime.now(UTC).replace(tzinfo=None)


logger = get_logger(__name__)

# Default respawn location (arena center; tutorial exit and death/lucidity respawn)
DEFAULT_RESPAWN_ROOM = "limbo_arena_arena_arena_5_5"

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
    - Restoring player DP and moving to respawn room
    - Publishing respawn events for UI updates
    - Clearing combat state when player respawns
    """

    def __init__(self, event_bus: Any | None = None, player_combat_service: Any | None = None) -> None:
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

    @staticmethod
    def _normalize_current_dp(stats: dict[str, Any]) -> int:
        """Return current_dp as an int, defaulting to 0 for non-numeric values."""
        current_dp = stats.get("current_dp", 0)
        if isinstance(current_dp, int | float):
            return int(current_dp)
        return 0

    def _can_move_to_limbo(self, player: Player, death_location: str) -> tuple[bool, int]:
        """Return (allowed, current_dp_int) for limbo movement gate checks."""
        if death_location == "catatonia_failover":
            return True, 0

        stats = player.get_stats() or {}
        current_dp_int = self._normalize_current_dp(stats)
        player_is_dead = player.is_dead()

        # Require actual DP <= -10; do not rely on is_dead() alone (defense against bad/stale stats)
        allowed = not (current_dp_int > -10 or not player_is_dead)
        return allowed, current_dp_int

    def _publish_delirium_respawn_event(
        self,
        player_id: uuid.UUID,
        player_name: str,
        respawn_room: str,
        old_lucidity: int,
        new_lucidity: int,
        old_room: str,
    ) -> None:
        """Publish delirium respawn event when event bus is available."""
        if not self._event_bus:
            return
        event = PlayerDeliriumRespawnedEvent(
            player_id=player_id,
            player_name=player_name,
            respawn_room_id=respawn_room,
            old_lucidity=old_lucidity,
            new_lucidity=new_lucidity,
            delirium_location=old_room if old_room != LIMBO_ROOM_ID else None,
        )
        self._event_bus.publish(event)

    async def _apply_sanitarium_liability_update(
        self,
        player_id: uuid.UUID,
        lucidity_record: Any,
        lucidity_service: Any,
        decode_liabilities: Any,
        encode_liabilities: Any,
        liability_catalog: Sequence[str],
        random_module: Any,
    ) -> None:
        """Increase existing liability stacks or add one liability if none exist."""
        liabilities = decode_liabilities(lucidity_record.liabilities)
        if liabilities:
            for liability in liabilities:
                liability["stacks"] = min(liability["stacks"] + 1, 5)  # Cap at 5 stacks
            lucidity_record.liabilities = encode_liabilities(liabilities)
            return

        liability_code = random_module.choice(liability_catalog)  # nosec B311 - Game mechanics, not security-critical
        await lucidity_service.add_liability(player_id, liability_code)

    async def _clear_respawn_combat_state(self, player_id: uuid.UUID, respawn_context: str) -> None:
        """Clear combat state for a respawning player, logging and swallowing DB errors."""
        if not self._player_combat_service:
            return
        try:
            await self._player_combat_service.clear_player_combat_state(player_id)
            logger.info(
                "Cleared combat state for respawned player", player_id=player_id, respawn_context=respawn_context
            )
        except (DatabaseError, SQLAlchemyError) as e:
            logger.error(
                "Error clearing combat state for respawned player",
                player_id=player_id,
                respawn_context=respawn_context,
                error=str(e),
                exc_info=True,
            )

    def _publish_standard_respawn_event(
        self,
        player_id: uuid.UUID,
        player_name: str,
        respawn_room: str,
        stats: dict[str, Any],
        old_room: str,
    ) -> None:
        """Publish standard respawn event when event bus is available."""
        if not self._event_bus:
            return
        event = PlayerRespawnedEvent(
            player_id=player_id,
            player_name=player_name,
            respawn_room_id=respawn_room,
            old_dp=stats.get("current_dp", 0),
            new_dp=stats.get("max_dp", 100),
            death_room_id=old_room if old_room != LIMBO_ROOM_ID else None,
        )
        self._event_bus.publish(event)

    @staticmethod
    def _apply_standard_respawn_state(player: Player, respawn_room: str) -> tuple[int, int, str]:
        """Restore full health and move player to respawn_room; return (old_dp, max_dp, old_room)."""
        old_dp = player.restore_to_full_health()
        stats = player.get_stats()
        max_dp = stats.get("max_dp", 100)
        old_room = player.current_room_id
        player.current_room_id = respawn_room
        return old_dp, max_dp, old_room

    @staticmethod
    def _log_standard_respawn(
        player: Player, player_id: uuid.UUID, respawn_room: str, old_dp: int, max_dp: int, old_room: str
    ) -> None:
        """Log standard respawn details."""
        logger.info(
            "Player respawned",
            player_id=player_id,
            player_name=player.name,
            respawn_room=respawn_room,
            old_dp=old_dp,
            new_dp=max_dp,
            max_dp=max_dp,
            from_limbo=old_room == LIMBO_ROOM_ID,
        )

    @staticmethod
    def _apply_sanitarium_player_state(player: Player, respawn_room: str) -> tuple[dict[str, Any], str]:
        """Set posture to standing and move player to respawn room; return (stats, old_room)."""
        stats = player.get_stats()
        stats["position"] = PositionState.STANDING
        player.set_stats(stats)
        old_room = player.current_room_id
        player.current_room_id = respawn_room
        return stats, old_room

    @staticmethod
    def _log_sanitarium_respawn(
        player: Player, player_id: uuid.UUID, respawn_room: str, old_lucidity: int, new_lucidity: int, old_room: str
    ) -> None:
        """Log sanitarium respawn details."""
        logger.info(
            "Player respawned from sanitarium",
            player_id=player_id,
            player_name=player.name,
            respawn_room=respawn_room,
            old_lucidity=old_lucidity,
            new_lucidity=new_lucidity,
            from_room=old_room,
        )

    @staticmethod
    def _log_delirium_respawn(
        player: Player, player_id: uuid.UUID, respawn_room: str, old_lucidity: int, new_lucidity: int, old_room: str
    ) -> None:
        """Log delirium respawn details."""
        logger.info(
            "Player respawned from delirium",
            player_id=player_id,
            player_name=player.name,
            respawn_room=respawn_room,
            old_lucidity=old_lucidity,
            new_lucidity=new_lucidity,
            from_room=old_room,
        )

    async def _prepare_delirium_respawn(
        self, player_id: uuid.UUID, player: Player, session: AsyncSession
    ) -> tuple[str, str, int, int] | None:
        """Apply delirium-specific lucidity/location updates and return respawn context."""
        from ..models.lucidity import PlayerLucidity

        lucidity_record = await session.get(PlayerLucidity, player_id)
        if not lucidity_record:
            logger.warning("Lucidity record not found for delirium respawn", player_id=player_id)
            return None

        old_lucidity = lucidity_record.current_lcd
        new_lucidity = 10  # Restore to 10 lucidity after delirium respawn
        lucidity_record.current_lcd = new_lucidity
        lucidity_record.current_tier = "lucid"  # Reset tier to lucid
        lucidity_record.last_updated_at = _utc_now()

        respawn_room = DEFAULT_RESPAWN_ROOM
        player.restore_to_full_health()
        old_room = player.current_room_id
        player.current_room_id = respawn_room
        return respawn_room, old_room, old_lucidity, new_lucidity

    async def _prepare_sanitarium_respawn(
        self, player_id: uuid.UUID, player: Player, session: AsyncSession
    ) -> tuple[str, dict[str, Any], str, int, int] | None:
        """Apply sanitarium-specific lucidity/liability/state updates and return respawn context."""
        from ..models.lucidity import PlayerLucidity
        from ..services.lucidity_service import (
            LIABILITY_CATALOG,
            LucidityService,
            decode_liabilities,
            encode_liabilities,
            resolve_tier,
        )

        lucidity_record = await session.get(PlayerLucidity, player_id)
        if not lucidity_record:
            logger.warning("Lucidity record not found for sanitarium respawn", player_id=player_id)
            return None

        old_lucidity = lucidity_record.current_lcd
        new_lucidity = 1  # Reset to 1 (Deranged tier) per spec
        lucidity_record.current_lcd = new_lucidity
        lucidity_record.current_tier = resolve_tier(new_lucidity)
        lucidity_record.last_updated_at = _utc_now()

        lucidity_service = LucidityService(session)
        await self._apply_sanitarium_liability_update(
            player_id=player_id,
            lucidity_record=lucidity_record,
            lucidity_service=lucidity_service,
            decode_liabilities=decode_liabilities,
            encode_liabilities=encode_liabilities,
            liability_catalog=LIABILITY_CATALOG,
            random_module=random,
        )

        respawn_room = DEFAULT_RESPAWN_ROOM
        stats, old_room = self._apply_sanitarium_player_state(player, respawn_room)
        debrief_expires_at = _utc_now() + timedelta(days=365)  # Far future expiration
        await lucidity_service.set_cooldown(player_id, LucidityActionCode.DEBRIEF_PENDING, debrief_expires_at)

        return respawn_room, stats, old_room, old_lucidity, new_lucidity

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

            # Player must be at -10 or lower DP before moving to limbo (death transition).
            # Catatonia failover is the only exception (lucidity-based, not DP).
            can_move, current_dp_int = self._can_move_to_limbo(player, death_location)
            if not can_move:
                logger.warning(
                    "Refusing to move player to limbo: DP must be -10 or lower",
                    player_id=player_id,
                    current_dp=current_dp_int,
                )
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

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error moving player to limbo", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error("Unexpected error moving player to limbo", player_id=player_id, error=str(e), exc_info=True)
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
                respawn_room_str = str(respawn_room).strip()
                if respawn_room_str:
                    logger.debug(
                        "Using custom respawn room from player record",
                        player_id=player_id,
                        respawn_room=respawn_room_str,
                    )
                    return respawn_room_str
            logger.debug("Using default respawn room", player_id=player_id, respawn_room=DEFAULT_RESPAWN_ROOM)
            return DEFAULT_RESPAWN_ROOM

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error getting respawn room, using default", player_id=player_id, error=str(e))
            return DEFAULT_RESPAWN_ROOM
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error("Unexpected error getting respawn room, using default", player_id=player_id, error=str(e))
            return DEFAULT_RESPAWN_ROOM

    async def respawn_player(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Respawn a dead player at their respawn location with full DP.

        This method:
        1. Restores player DP to their max_dp (not hardcoded 100)
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

            old_dp, max_dp, old_room = self._apply_standard_respawn_state(player, respawn_room)

            # BUGFIX #244: clear combat state on resurrection to prevent stale combat continuity.
            await self._clear_respawn_combat_state(player_id=player_id, respawn_context="standard")

            # Commit changes using async API
            await session.commit()

            self._log_standard_respawn(player, player_id, respawn_room, old_dp, max_dp, old_room)

            self._publish_standard_respawn_event(
                player_id=player_id,
                player_name=str(player.name),
                respawn_room=respawn_room,
                stats={"current_dp": old_dp, "max_dp": max_dp},
                old_room=old_room,
            )

            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error("Unexpected error respawning player", player_id=player_id, error=str(e), exc_info=True)
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

            prepared = await self._prepare_delirium_respawn(player_id, player, session)
            if not prepared:
                return False
            respawn_room, old_room, old_lucidity, new_lucidity = prepared

            await self._clear_respawn_combat_state(player_id=player_id, respawn_context="delirium")

            # Commit changes using async API
            await session.commit()

            self._log_delirium_respawn(player, player_id, respawn_room, old_lucidity, new_lucidity, old_room)

            self._publish_delirium_respawn_event(
                player_id=player_id,
                player_name=str(player.name),
                respawn_room=respawn_room,
                old_lucidity=old_lucidity,
                new_lucidity=new_lucidity,
                old_room=old_room,
            )

            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player from delirium", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error(
                "Unexpected error respawning player from delirium", player_id=player_id, error=str(e), exc_info=True
            )
            await session.rollback()
            return False

    async def respawn_player_from_sanitarium(self, player_id: uuid.UUID, session: AsyncSession) -> bool:  # pylint: disable=too-many-locals  # Reason: Respawn processing requires many intermediate variables for complex respawn logic
        """
        Respawn a player from sanitarium failover at LCD -100.

        This method:
        1. Sets player lucidity to 1 (Deranged tier)
        2. Moves player to Sanitarium (default respawn room)
        3. Increases liability stages (or adds one if none exist)
        4. Publishes sanitarium respawn event for UI updates

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
                logger.warning("Player not found for sanitarium respawn", player_id=player_id)
                return False

            prepared = await self._prepare_sanitarium_respawn(player_id, player, session)
            if not prepared:
                return False
            respawn_room, stats, old_room, old_lucidity, new_lucidity = prepared

            await self._clear_respawn_combat_state(player_id=player_id, respawn_context="sanitarium")

            # Commit changes using async API (includes debrief flag)
            await session.commit()

            self._log_sanitarium_respawn(player, player_id, respawn_room, old_lucidity, new_lucidity, old_room)

            self._publish_standard_respawn_event(
                player_id=player_id,
                player_name=str(player.name),
                respawn_room=respawn_room,
                stats=stats,
                old_room=old_room,
            )

            return True

        except (DatabaseError, SQLAlchemyError) as e:
            logger.error("Error respawning player from sanitarium", player_id=player_id, error=str(e), exc_info=True)
            await session.rollback()
            return False
        except Exception as e:  # pylint: disable=broad-except  # Also catch generic exceptions for test compatibility
            logger.error(
                "Unexpected error respawning player from sanitarium", player_id=player_id, error=str(e), exc_info=True
            )
            await session.rollback()
            return False
