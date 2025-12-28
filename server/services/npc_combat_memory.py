"""
NPC Combat Memory Management.

This module handles NPC combat memory - tracking which players have attacked
which NPCs, enabling NPCs to remember their attackers for retaliation.
"""

from ..structured_logging.enhanced_logging_config import get_logger

logger = get_logger(__name__)


class NPCCombatMemory:
    """Manages NPC combat memory - tracking attackers."""

    def __init__(self):
        """Initialize combat memory storage."""
        self._npc_combat_memory: dict[str, str] = {}

    def get_attacker(self, npc_id: str) -> str | None:
        """
        Get the last attacker for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            ID of the last attacker, or None if no memory
        """
        return self._npc_combat_memory.get(npc_id)

    def record_attack(self, npc_id: str, attacker_id: str) -> bool:
        """
        Record that an NPC was attacked by a player.

        Args:
            npc_id: ID of the NPC
            attacker_id: ID of the attacker

        Returns:
            True if this is the first engagement (NPC had no previous attacker)
        """
        first_engagement = npc_id not in self._npc_combat_memory
        self._npc_combat_memory[npc_id] = attacker_id
        return first_engagement

    def clear_memory(self, npc_id: str) -> bool:
        """
        Clear combat memory for an NPC.

        Args:
            npc_id: ID of the NPC

        Returns:
            True if memory was cleared
        """
        if npc_id in self._npc_combat_memory:
            del self._npc_combat_memory[npc_id]
            logger.debug("Cleared combat memory for NPC", npc_id=npc_id)
            return True
        return False

    def has_memory(self, npc_id: str) -> bool:
        """
        Check if an NPC has combat memory.

        Args:
            npc_id: ID of the NPC

        Returns:
            True if NPC has combat memory
        """
        return npc_id in self._npc_combat_memory
