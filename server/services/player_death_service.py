"""
Player Death Service for managing player mortality and DP decay.

This service handles the mortally wounded state (0 to -10 DP), automatic DP decay,
and death detection. As documented in the Necronomicon's chapter on mortality,
the threshold between life and death requires careful management.

ASYNC MIGRATION (Phase 2):
All persistence calls wrapped in asyncio.to_thread() to prevent event loop blocking.
"""

import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from server.events.event_types import PlayerDiedEvent, PlayerDPDecayEvent
from server.models.game import PositionState
from server.models.player import Player
from server.structured_logging.enhanced_logging_config import get_logger, log_exception_once

logger = get_logger(__name__)


class PlayerDeathService:
    """
    Service for managing player death, mortally wounded state, and DP decay.

    This service handles:
    - Identifying mortally wounded players (0 >= DP > -10)
    - Processing DP decay (1 DP per tick, capped at -10)
    - Detecting and handling player death (DP <= -10)
    - Publishing appropriate events for UI updates
    - Clearing combat state when player dies
    """

    def __init__(self, event_bus: Any = None, player_combat_service: Any = None) -> None:
        """
        Initialize the player death service.

        Args:
            event_bus: Optional event bus for publishing events
            player_combat_service: Optional player combat service for clearing combat state
        """
        self._event_bus = event_bus
        self._player_combat_service = player_combat_service
        logger.info(
            "PlayerDeathService initialized",
            event_bus_available=bool(event_bus),
            player_combat_service_available=bool(player_combat_service),
        )

    async def get_mortally_wounded_players(self, session: AsyncSession) -> list[Player]:
        """
        Get all players currently in the mortally wounded state.

        A player is considered mortally wounded if their DP is between 0 and -9 (inclusive).

        Args:
            session: Async database session for querying players

        Returns:
            List of Player objects that are mortally wounded
        """
        try:
            # Query all players from the database using async API
            result = await session.execute(select(Player))
            all_players = result.scalars().all()

            # Filter for mortally wounded players (0 >= DP > -10)
            mortally_wounded = []
            for player in all_players:
                stats = player.get_stats()
                current_dp = stats.get("current_dp", 0)  # current_dp represents DP
                if 0 >= current_dp > -10:
                    mortally_wounded.append(player)
        except Exception as e:  # pylint: disable=broad-exception-caught  # Reason: Player stats retrieval errors unpredictable, must return empty list
            logger.error("Error getting mortally wounded players", error=str(e), exc_info=True)
            return []

        logger.debug(
            "Found mortally wounded players",
            count=len(mortally_wounded),
            player_ids=[p.player_id for p in mortally_wounded],
        )

        return mortally_wounded

    async def get_dead_players(self, session: AsyncSession) -> list[Player]:
        """
        Get all players who are dead (DP <= -10).

        Args:
            session: Async database session for querying players

        Returns:
            List of Player objects that are dead
        """
        try:
            # Query all players from the database using async API
            result = await session.execute(select(Player))
            all_players = result.scalars().all()

            # Filter for dead players (DP <= -10)
            dead_players = []
            for player in all_players:
                stats = player.get_stats()
                current_dp = stats.get("current_dp", 0)  # current_dp represents DP
                if current_dp <= -10:
                    dead_players.append(player)

            logger.debug(
                "Found dead players",
                count=len(dead_players),
                player_ids=[p.player_id for p in dead_players],
            )

            return dead_players

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            log_exception_once(
                logger,
                "error",
                "Error retrieving dead players",
                exc=e,
                exc_info=True,
            )
            return []

    async def process_mortally_wounded_tick(self, player_id: uuid.UUID, session: AsyncSession) -> bool:
        """
        Process DP decay for a single mortally wounded player.

        Decreases player DP by 1, capped at 0. Returns True if decay was applied.

        Args:
            player_id: ID of the player to process
            session: Database session for player data access

        Returns:
            True if DP decay was applied, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for DP decay", player_id=player_id)
                return False

            # Check if player is already dead (DP <= -10)
            if player.is_dead():
                logger.debug("Player already dead, skipping DP decay", player_id=player_id)
                return False

            # Get current stats and apply decay
            stats = player.get_stats()
            current_dp = stats.get("current_dp", 0)  # current_dp represents DP
            old_dp = current_dp

            # Decrease DP by 1, cap at -10
            new_dp = max(current_dp - 1, -10)

            # Update player stats
            stats["current_dp"] = new_dp

            # BUGFIX: Automatically change posture to lying when DP drops to <= 0
            # As documented in "Corporeal Collapse and Unconsciousness" - Dr. Armitage, 1928
            # When a player's determination points drop to zero or below, their body automatically collapses
            if new_dp <= 0 and old_dp > 0:
                stats["position"] = PositionState.LYING
                logger.info(
                    "Player posture changed to lying (unconscious)",
                    player_id=player_id,
                    player_name=player.name,
                    dp=new_dp,
                )
            elif new_dp <= 0 and stats.get("position") != PositionState.LYING:
                # Ensure player is lying if already at <= 0 DP
                stats["position"] = PositionState.LYING

            player.set_stats(stats)

            # Commit changes to database using async API
            await session.commit()

            logger.info(
                "DP decay applied to player",
                player_id=player_id,
                player_name=player.name,
                old_dp=old_dp,
                new_dp=new_dp,
                delta=-1,
            )

            # Publish DP decay event if event bus is available
            if self._event_bus:
                event = PlayerDPDecayEvent(
                    player_id=player_id,
                    old_dp=old_dp,
                    new_dp=new_dp,
                    decay_amount=1,
                    room_id=str(player.current_room_id),
                )
                self._event_bus.publish(event)

            return True

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # Reason: DP decay errors unpredictable, must log and return False
            log_exception_once(
                logger,
                "error",
                "Error processing DP decay for player",
                exc=e,
                exc_info=True,
                player_id=player_id,
            )
            await session.rollback()
            return False

    async def _ensure_player_posture_lying(self, player: Player, player_id: uuid.UUID) -> None:
        """
        Ensure player posture is set to lying when dead.

        Args:
            player: Player object to update
            player_id: ID of the player for logging
        """
        stats = player.get_stats()
        if stats.get("position") != PositionState.LYING:
            stats["position"] = PositionState.LYING
            player.set_stats(stats)
            logger.debug(
                "Set player posture to lying on death",
                player_id=player_id,
                player_name=player.name,
            )

    async def _clear_player_combat_state(self, player_id: uuid.UUID) -> None:
        """
        Clear player combat state when they die.

        BUGFIX #244: As documented in "Mortality and Combat State Persistence" - Dr. Armitage, 1929
        A player's combat essence must be severed upon death to prevent lingering in combat.

        Args:
            player_id: ID of the player whose combat state should be cleared
        """
        if not self._player_combat_service:
            return

        try:
            await self._player_combat_service.clear_player_combat_state(player_id)
            logger.info("Cleared combat state for deceased player", player_id=player_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            log_exception_once(
                logger,
                "error",
                "Error clearing combat state for deceased player",
                exc=e,
                exc_info=True,
                player_id=player_id,
            )

    def _get_room_name_for_death(self, death_location: str) -> str:
        """
        Get room name for death location display.

        Args:
            death_location: Room ID where the player died

        Returns:
            Room name if available, otherwise the room ID or "Unknown"
        """
        if not death_location:
            return "Unknown"

        from ..container import ApplicationContainer

        container = ApplicationContainer.get_instance()
        if container and container.async_persistence:
            try:
                room = container.async_persistence.get_room_by_id(death_location)
                # Handle case where get_room_by_id might return a coroutine (if mocked as async)
                if hasattr(room, "__await__"):
                    # It's a coroutine, can't await in sync context - just return location
                    return death_location
                return room.name if room and hasattr(room, "name") else death_location
            except (AttributeError, TypeError):
                # If room lookup fails, just return the location
                return death_location

        return death_location

    def _publish_death_event(
        self, player_id: uuid.UUID, player_name: str, death_location: str, killer_info: dict | None
    ) -> None:
        """
        Publish player died event if event bus is available.

        Args:
            player_id: ID of the player who died
            player_name: Name of the player who died
            death_location: Room ID where the player died
            killer_info: Optional dict with killer_id and killer_name
        """
        if not self._event_bus:
            return

        room_name = self._get_room_name_for_death(death_location)

        event = PlayerDiedEvent(
            player_id=player_id,
            player_name=str(player_name),
            room_id=death_location,
            death_location=room_name,
            killer_id=killer_info.get("killer_id") if killer_info else None,
            killer_name=killer_info.get("killer_name") if killer_info else None,
        )
        self._event_bus.publish(event)

    async def handle_player_death(
        self, player_id: uuid.UUID, death_location: str, killer_info: dict | None, session: AsyncSession
    ) -> bool:
        """
        Handle player death when DP reaches 0.

        Records death location and killer information, then triggers respawn sequence.

        Args:
            player_id: ID of the player who died
            death_location: Room ID where the player died
            killer_info: Optional dict with killer_id and killer_name
            session: Async database session for player data access

        Returns:
            True if death was handled successfully, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for death handling", player_id=player_id)
                return False

            # Ensure player posture is set to lying when dead
            await self._ensure_player_posture_lying(player, player_id)

            # Log death event
            logger.info(
                "Player died",
                player_id=player_id,
                player_name=player.name,
                death_location=death_location,
                killer_id=killer_info.get("killer_id") if killer_info else None,
                killer_name=killer_info.get("killer_name") if killer_info else None,
            )

            # Clear player combat state when they die
            await self._clear_player_combat_state(player_id)

            # Commit any pending changes using async API
            await session.commit()

            # Publish player died event if event bus is available
            self._publish_death_event(player_id, str(player.name), death_location, killer_info)

            return True

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError, Exception) as e:  # pylint: disable=broad-exception-caught  # Reason: Player death handling errors unpredictable, must log and return False
            log_exception_once(
                logger,
                "error",
                "Error handling player death",
                exc=e,
                exc_info=True,
                player_id=player_id,
            )
            await session.rollback()
            return False
