"""
NPC Combat Rewards Management.

This module handles XP calculation and rewards for NPC combat,
including defensive error handling to prevent player disconnections.
"""

from typing import Any
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from ..game.mechanics import GameMechanicsService
from ..logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class NPCCombatRewards:
    """Manages XP rewards for NPC combat."""

    def __init__(self, async_persistence: Any, game_mechanics: GameMechanicsService):
        """
        Initialize the rewards manager.

        Args:
            async_persistence: Async persistence layer instance
            game_mechanics: GameMechanicsService instance
        """
        self._persistence = async_persistence
        self._game_mechanics = game_mechanics

    async def calculate_xp_reward(self, npc_definition: Any | None) -> int:
        """
        Calculate XP reward from NPC definition.

        Args:
            npc_definition: NPC definition object

        Returns:
            XP reward value (0 if not found)
        """
        if not npc_definition:
            return 0

        base_stats = npc_definition.get_base_stats()
        if isinstance(base_stats, dict):
            # Use xp_value from the database (not xp_reward)
            return base_stats.get("xp_value", 0)
        return 0

    async def check_player_connection_state(self, player_id: str) -> None:
        """
        Check and log player connection state before operations.

        Args:
            player_id: ID of the player to check
        """
        try:
            from ..container import ApplicationContainer

            container = ApplicationContainer.get_instance()
            connection_manager = getattr(container, "connection_manager", None) if container else None
            player_uuid = UUID(player_id) if self._is_valid_uuid(player_id) else None
            if player_uuid and connection_manager is not None:
                has_websocket = player_uuid in connection_manager.player_websockets
                has_sse = False  # SSE connections not supported in WebSocket-only system
                logger.debug(
                    "Player connection state before XP award",
                    player_id=player_id,
                    has_websocket=has_websocket,
                    has_sse=has_sse,
                )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as conn_check_error:
            logger.warning(
                "Could not check connection state before XP award",
                player_id=player_id,
                error=str(conn_check_error),
            )

    async def award_xp_to_killer(self, killer_id: str, npc_id: str, xp_reward: int) -> None:
        """
        Award XP to the killer with defensive error handling.

        Args:
            killer_id: ID of the player who killed the NPC
            npc_id: ID of the killed NPC
            xp_reward: XP amount to award
        """
        logger.info(
            "Awarding XP to player for NPC kill",
            player_id=killer_id,
            npc_id=npc_id,
            xp_reward=xp_reward,
        )

        # Check connection state before XP award
        await self.check_player_connection_state(killer_id)

        # CRITICAL FIX: Use GameMechanicsService.gain_experience() to prevent
        # XP awards from overwriting combat damage with stale health values
        try:
            success, message = self._game_mechanics.gain_experience(killer_id, xp_reward, f"killed_{npc_id}")
            if success:
                logger.info(
                    "Awarded XP to player",
                    player_id=killer_id,
                    xp_reward=xp_reward,
                    npc_id=npc_id,
                )
            else:
                logger.warning(
                    "Failed to award XP to player",
                    player_id=killer_id,
                    xp_reward=xp_reward,
                    message=message,
                )
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            # CRITICAL: Don't let XP award errors disconnect player
            logger.error(
                "Error awarding XP to player - preventing disconnect",
                player_id=killer_id,
                error=str(e),
                exc_info=True,
            )
            # Continue - don't raise exception

    def _is_valid_uuid(self, uuid_string: str) -> bool:
        """Check if a string is a valid UUID."""
        try:
            UUID(uuid_string)
            return True
        except ValueError:
            return False
