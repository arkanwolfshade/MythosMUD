"""
NPC Combat Rewards Management.

This module calculates the XP reward for defeating an NPC. Awarding it is
LevelService's job (#879 -- single XP/level authority); this module no longer
touches persistence or game mechanics directly.
"""

from typing import Any, cast


class NPCCombatRewards:
    """Calculates XP rewards for NPC combat."""

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
            return cast(int, base_stats.get("xp_value", 0))
        return 0
