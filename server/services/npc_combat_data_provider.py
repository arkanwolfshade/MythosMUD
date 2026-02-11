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

    def __init__(self, async_persistence: Any) -> None:
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

        Uses persistence.get_npc_lifecycle_manager when available; otherwise
        falls back to the instance service lifecycle (same source as get_npc_instance)
        so that XP mapping works when persistence does not expose the lifecycle manager.

        Args:
            npc_id: ID of the NPC (lifecycle key, e.g. string from _generate_npc_id or instance id)

        Returns:
            NPC definition if found, None otherwise
        """
        try:
            import asyncio

            lifecycle_manager = None
            if hasattr(self._persistence, "get_npc_lifecycle_manager"):
                lifecycle_manager = await asyncio.to_thread(self._persistence.get_npc_lifecycle_manager)

            if not lifecycle_manager:
                from .npc_instance_service import get_npc_instance_service

                npc_instance_service = get_npc_instance_service()
                if hasattr(npc_instance_service, "lifecycle_manager"):
                    lifecycle_manager = npc_instance_service.lifecycle_manager

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

        combat_stats = player.get_combat_stats()

        logger.info(
            "Starting combat with player stats",
            player_id=player_id,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
            dex=combat_stats["dexterity"],
        )

        return CombatParticipantData(
            participant_id=attacker_uuid,
            name=player_name,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
            dexterity=combat_stats["dexterity"],
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
        if hasattr(npc_instance, "get_combat_stats"):
            combat_stats = npc_instance.get_combat_stats()
        else:
            npc_stats = npc_instance.get_stats()
            combat_stats = {
                "current_dp": int(npc_stats.get("determination_points", npc_stats.get("dp", 100))),
                "max_dp": int(npc_stats.get("max_dp", npc_stats.get("max_hp", 100))),
                "dexterity": int(npc_stats.get("dexterity", 10)),
            }

        npc_id = getattr(npc_instance, "id", getattr(npc_instance, "npc_id", "unknown"))
        logger.info(
            "NPC combat stats from model",
            npc_id=npc_id,
            npc_name=npc_instance.name,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
        )

        return CombatParticipantData(
            participant_id=target_uuid,
            name=npc_instance.name,
            current_dp=combat_stats["current_dp"],
            max_dp=combat_stats["max_dp"],
            dexterity=combat_stats["dexterity"],
            participant_type=CombatParticipantType.NPC,
        )
