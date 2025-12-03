"""
Player Death Service for managing player mortality and HP decay.

This service handles the mortally wounded state (0 to -10 HP), automatic HP decay,
and death detection. As documented in the Necronomicon's chapter on mortality,
the threshold between life and death requires careful management.

ASYNC MIGRATION (Phase 2):
All persistence calls wrapped in asyncio.to_thread() to prevent event loop blocking.
"""

import asyncio
import uuid
from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from server.events.event_types import PlayerDiedEvent, PlayerHPDecayEvent
from server.logging.enhanced_logging_config import get_logger, log_exception_once
from server.models.game import PositionState
from server.models.player import Player

logger = get_logger(__name__)


class PlayerDeathService:
    """
    Service for managing player death, mortally wounded state, and HP decay.

    This service handles:
    - Identifying mortally wounded players (0 >= HP > -10)
    - Processing HP decay (1 HP per tick, capped at -10)
    - Detecting and handling player death (HP <= -10)
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

        A player is considered mortally wounded if their HP is between 0 and -9 (inclusive).

        Args:
            session: Async database session for querying players

        Returns:
            List of Player objects that are mortally wounded
        """
        try:
            # Query all players from the database using async API
            result = await session.execute(select(Player))
            all_players = result.scalars().all()

            # Filter for mortally wounded players (0 >= HP > -10)
            mortally_wounded = []
            for player in all_players:
                stats = player.get_stats()
                current_hp = stats.get("current_health", 0)
                if 0 >= current_hp > -10:
                    mortally_wounded.append(player)

            logger.debug(
                "Found mortally wounded players",
                count=len(mortally_wounded),
                player_ids=[p.player_id for p in mortally_wounded],
            )

            return mortally_wounded

        except Exception as e:
            log_exception_once(
                logger,
                "error",
                "Error retrieving mortally wounded players",
                exc=e,
                exc_info=True,
            )
            return []

    async def get_dead_players(self, session: AsyncSession) -> list[Player]:
        """
        Get all players who are dead (HP <= -10).

        Args:
            session: Async database session for querying players

        Returns:
            List of Player objects that are dead
        """
        try:
            # Query all players from the database using async API
            result = await session.execute(select(Player))
            all_players = result.scalars().all()

            # Filter for dead players (HP <= -10)
            dead_players = []
            for player in all_players:
                stats = player.get_stats()
                current_hp = stats.get("current_health", 0)
                if current_hp <= -10:
                    dead_players.append(player)

            logger.debug(
                "Found dead players",
                count=len(dead_players),
                player_ids=[p.player_id for p in dead_players],
            )

            return dead_players

        except Exception as e:
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
        Process HP decay for a single mortally wounded player.

        Decreases player HP by 1, capped at -10. Returns True if decay was applied.

        Args:
            player_id: ID of the player to process
            session: Database session for player data access

        Returns:
            True if HP decay was applied, False otherwise
        """
        try:
            # Retrieve player from database using async API
            player = await session.get(Player, player_id)
            if not player:
                logger.warning("Player not found for HP decay", player_id=player_id)
                return False

            # Check if player is already dead (HP <= -10)
            if player.is_dead():
                logger.debug("Player already dead, skipping HP decay", player_id=player_id)
                return False

            # Get current stats and apply decay
            stats = player.get_stats()
            current_hp = stats.get("current_health", 0)
            old_hp = current_hp

            # Decrease HP by 1, cap at -10
            new_hp = max(current_hp - 1, -10)

            # Update player stats
            stats["current_health"] = new_hp

            # BUGFIX: Automatically change posture to lying when HP drops to <= 0
            # As documented in "Corporeal Collapse and Unconsciousness" - Dr. Armitage, 1928
            # When a player's life force drops to zero or below, their body automatically collapses
            if new_hp <= 0 and old_hp > 0:
                stats["position"] = PositionState.LYING
                logger.info(
                    "Player posture changed to lying (unconscious)",
                    player_id=player_id,
                    player_name=player.name,
                    hp=new_hp,
                )
            elif new_hp <= 0 and stats.get("position") != PositionState.LYING:
                # Ensure player is lying if already at <= 0 HP
                stats["position"] = PositionState.LYING

            player.set_stats(stats)

            # Commit changes to database using async API
            await session.commit()

            logger.info(
                "HP decay applied to player",
                player_id=player_id,
                player_name=player.name,
                old_hp=old_hp,
                new_hp=new_hp,
                delta=-1,
            )

            # Publish HP decay event if event bus is available
            if self._event_bus:
                event = PlayerHPDecayEvent(
                    player_id=player_id,
                    old_hp=old_hp,
                    new_hp=new_hp,
                    decay_amount=1,
                    room_id=str(player.current_room_id),
                )
                self._event_bus.publish(event)

            return True

        except Exception as e:
            log_exception_once(
                logger,
                "error",
                "Error processing HP decay for player",
                exc=e,
                exc_info=True,
                player_id=player_id,
            )
            await session.rollback()
            return False

    async def handle_player_death(
        self, player_id: uuid.UUID, death_location: str, killer_info: dict | None, session: AsyncSession
    ) -> bool:
        """
        Handle player death when HP reaches -10.

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
            stats = player.get_stats()
            if stats.get("position") != PositionState.LYING:
                stats["position"] = PositionState.LYING
                player.set_stats(stats)
                logger.debug(
                    "Set player posture to lying on death",
                    player_id=player_id,
                    player_name=player.name,
                )

            # Log death event
            logger.info(
                "Player died",
                player_id=player_id,
                player_name=player.name,
                death_location=death_location,
                killer_id=killer_info.get("killer_id") if killer_info else None,
                killer_name=killer_info.get("killer_name") if killer_info else None,
            )

            # BUGFIX #244: Clear player combat state when they die
            # As documented in "Mortality and Combat State Persistence" - Dr. Armitage, 1929
            # A player's combat essence must be severed upon death to prevent lingering in combat
            if self._player_combat_service:
                try:
                    await self._player_combat_service.clear_player_combat_state(player_id)
                    logger.info("Cleared combat state for deceased player", player_id=player_id)
                except Exception as e:
                    log_exception_once(
                        logger,
                        "error",
                        "Error clearing combat state for deceased player",
                        exc=e,
                        exc_info=True,
                        player_id=player_id,
                    )

            # Commit any pending changes using async API
            await session.commit()

            # Publish player died event if event bus is available
            if self._event_bus:
                # Get room name for death location display
                from ..persistence import get_persistence

                persistence = get_persistence()
                room = await asyncio.to_thread(persistence.get_room, death_location) if death_location else None
                room_name = room.name if room else death_location

                event = PlayerDiedEvent(
                    player_id=player_id,
                    player_name=str(player.name),
                    room_id=death_location,
                    death_location=room_name,  # Set death_location for client display
                    killer_id=killer_info.get("killer_id") if killer_info else None,
                    killer_name=killer_info.get("killer_name") if killer_info else None,
                )
                self._event_bus.publish(event)

            return True

        except Exception as e:
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
