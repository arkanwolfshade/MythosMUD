"""
NPC Combat Lifecycle Management.

This module handles NPC despawning and lifecycle operations during combat,
with defensive error handling to prevent player disconnections.
"""

# pylint: disable=too-few-public-methods  # Reason: Lifecycle class with focused responsibility, minimal public interface

import asyncio
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class NPCCombatLifecycle:  # pylint: disable=too-few-public-methods  # Reason: Lifecycle class with focused responsibility, minimal public interface
    """Manages NPC lifecycle operations during combat."""

    def __init__(self, async_persistence: Any):
        """
        Initialize the lifecycle manager.

        Args:
            async_persistence: Async persistence layer instance
        """
        self._persistence = async_persistence

    async def despawn_npc_safely(self, npc_id: str, room_id: str) -> None:
        """
        Despawn NPC with defensive error handling.

        Args:
            npc_id: ID of the NPC to despawn
            room_id: ID of the room where the NPC is located
        """
        logger.debug("Despawning NPC", npc_id=npc_id, room_id=room_id)
        try:
            await self._despawn_npc(str(npc_id), room_id)
            logger.debug("NPC despawned successfully", npc_id=npc_id, room_id=room_id)
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as despawn_error:
            # CRITICAL: Don't let despawn errors disconnect player
            logger.error(
                "Error despawning NPC - preventing disconnect",
                npc_id=npc_id,
                room_id=room_id,
                error=str(despawn_error),
                exc_info=True,
            )
            # Continue - despawn failure shouldn't disconnect player

    async def _despawn_npc(self, npc_id: str, _room_id: str) -> None:
        """
        Despawn an NPC.

        Args:
            npc_id: ID of the NPC to despawn
            _room_id: ID of the room (unused, kept for compatibility)
        """
        try:
            # Try lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = await asyncio.to_thread(self._persistence.get_npc_lifecycle_manager)
                if lifecycle_manager:
                    # Record the death for 30-second respawn suppression
                    lifecycle_manager.record_npc_death(npc_id)
                    lifecycle_manager.despawn_npc(npc_id, "combat_death")
                    return

            # Fallback: try lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = await asyncio.to_thread(self._persistence.get_npc_lifecycle_manager)
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    del lifecycle_manager.active_npcs[npc_id]

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error despawning NPC", npc_id=npc_id, error=str(e))
