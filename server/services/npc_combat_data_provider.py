"""
NPC Combat Data Provider.

This module provides data retrieval and preparation for NPC combat,
including NPC instances, definitions, player data, and combat participant data.
"""

from typing import Any
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError

from ..models.combat import CombatParticipantType
from ..structured_logging.enhanced_logging_config import get_logger
from .combat_types import CombatParticipantData

logger = get_logger(__name__)


class NPCCombatDataProvider:
    """Provides data retrieval and preparation for NPC combat."""

    def __init__(self, async_persistence: Any):
        """
        Initialize the data provider.

        Args:
            async_persistence: Async persistence layer instance
        """
        self._persistence = async_persistence

    def get_npc_instance(self, npc_id: str) -> Any | None:
        """
        Get NPC instance from the spawning service.

        Args:
            npc_id: ID of the NPC

        Returns:
            NPC instance if found, None otherwise
        """
        try:
            from .npc_instance_service import get_npc_instance_service

            npc_instance_service = get_npc_instance_service()
            if hasattr(npc_instance_service, "lifecycle_manager"):
                lifecycle_manager = npc_instance_service.lifecycle_manager
                if lifecycle_manager and npc_id in lifecycle_manager.active_npcs:
                    return lifecycle_manager.active_npcs[npc_id]

            return None

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error getting NPC instance", npc_id=npc_id, error=str(e))
            return None

    async def get_npc_definition(self, npc_id: str) -> Any | None:
        """
        Get NPC definition for an NPC instance.

        Args:
            npc_id: ID of the NPC

        Returns:
            NPC definition if found, None otherwise
        """
        try:
            import asyncio

            # Try to get from lifecycle manager if available
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = await asyncio.to_thread(self._persistence.get_npc_lifecycle_manager)
                if lifecycle_manager:
                    keys = list(lifecycle_manager.lifecycle_records.keys())
                else:
                    keys = []
                logger.debug(
                    "_get_npc_definition lookup",
                    npc_id=npc_id,
                    has_lifecycle_manager=bool(lifecycle_manager),
                    lifecycle_records_count=len(keys),
                    npc_id_in_keys=npc_id in keys if lifecycle_manager else False,
                )
                if lifecycle_manager and npc_id in lifecycle_manager.lifecycle_records:
                    return lifecycle_manager.lifecycle_records[npc_id].definition

            return None

        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error getting NPC definition", npc_id=npc_id, error=str(e))
            return None

    async def get_player_name(self, player_id: str) -> str:
        """
        Get player name for messaging.

        Args:
            player_id: ID of the player

        Returns:
            Player name, or "Unknown Player" if not found
        """
        try:
            # Convert player_id to UUID if it's a string
            player_id_uuid = UUID(player_id) if isinstance(player_id, str) else player_id
            player = await self._persistence.get_player_by_id(player_id_uuid)
            return str(player.name) if player else "Unknown Player"
        except (OSError, ValueError, TypeError) as e:
            logger.error("Error getting player name", player_id=player_id, error=str(e), error_type=type(e).__name__)
            return "Unknown Player"

    async def get_player_room_id(self, player_id: str) -> str | None:
        """
        Get the current room ID for a player.

        Args:
            player_id: ID of the player

        Returns:
            Room ID if found, None otherwise
        """
        try:
            # Convert player_id to UUID if it's a string
            player_id_uuid = UUID(player_id) if isinstance(player_id, str) else player_id
            player = await self._persistence.get_player_by_id(player_id_uuid)
            if player:
                return str(player.current_room_id)
            return None
        except (ValueError, AttributeError, ImportError, SQLAlchemyError, TypeError) as e:
            logger.error("Error getting player room ID", player_id=player_id, error=str(e))
            return None

    async def get_player_combat_data(
        self, player_id: str, attacker_uuid: UUID, player_name: str
    ) -> CombatParticipantData:
        """
        Get player combat participant data from persistence.

        Args:
            player_id: ID of the attacking player
            attacker_uuid: UUID of the attacker
            player_name: Name of the player

        Returns:
            CombatParticipantData for the player

        BUGFIX: Was hardcoded to 100, causing DP to reset between combats
        """
        # Fetch actual player stats from persistence to ensure correct DP
        # Convert player_id to UUID if it's a string
        player_id_uuid = UUID(player_id) if isinstance(player_id, str) else player_id
        player = await self._persistence.get_player_by_id(player_id_uuid)
        if not player:
            logger.error("Player not found when starting combat", player_id=player_id)
            raise ValueError(f"Player {player_id} not found")

        player_stats = player.get_stats()
        attacker_dp = player_stats.get("current_dp", 100)
        attacker_max_dp = player_stats.get("max_dp", 100)
        attacker_dex = player_stats.get("dexterity", 10)

        logger.info(
            "Starting combat with player stats",
            player_id=player_id,
            current_dp=attacker_dp,
            max_dp=attacker_max_dp,
            dex=attacker_dex,
        )

        return CombatParticipantData(
            participant_id=attacker_uuid,
            name=player_name,
            current_dp=attacker_dp,
            max_dp=attacker_max_dp,
            dexterity=attacker_dex,
            participant_type=CombatParticipantType.PLAYER,
        )

    def get_npc_combat_data(self, npc_instance: Any, target_uuid: UUID) -> CombatParticipantData:
        """
        Get NPC combat participant data from NPC instance.

        Args:
            npc_instance: NPC instance
            target_uuid: UUID of the target

        Returns:
            CombatParticipantData for the NPC
        """
        # Get NPC stats properly from the NPC instance
        npc_stats = npc_instance.get_stats()
        npc_current_dp = npc_stats.get("determination_points", npc_stats.get("dp", 100))
        # Check both max_dp and max_dp keys (NPCs may use either)
        npc_max_dp = npc_stats.get("max_dp", npc_stats.get("max_dp", 100))
        npc_id = getattr(npc_instance, "id", "unknown")
        logger.info(
            "DEBUG: NPC stats extraction",
            npc_id=npc_id,
            npc_name=npc_instance.name,
            npc_stats_keys=list(npc_stats.keys()),
            npc_max_dp=npc_max_dp,
            has_max_dp="max_dp" in npc_stats,
        )
        npc_dexterity = npc_stats.get("dexterity", 10)

        return CombatParticipantData(
            participant_id=target_uuid,
            name=npc_instance.name,
            current_dp=npc_current_dp,
            max_dp=npc_max_dp,
            dexterity=npc_dexterity,
            participant_type=CombatParticipantType.NPC,
        )
