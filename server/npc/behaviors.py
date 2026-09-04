"""
NPC behavior system for MythosMUD.

This module provides the core NPC behavior system including base classes,
behavior engines, and specific NPC type implementations.

As noted in the Pnakotic Manuscripts, proper behavioral programming is essential
for maintaining the delicate balance between order and chaos in our eldritch
entity management systems.

This module now serves as a compatibility layer, re-exporting classes from
separate modules to maintain backward compatibility while reducing file complexity.
"""

# Re-export all classes for backward compatibility
from .aggressive_mob_npc import AggressiveMobNPC
from .behavior_engine import BehaviorEngine
from .npc_base import NPCBase
from .passive_mob_npc import PassiveMobNPC
from .shopkeeper_npc import ShopkeeperNPC

__all__ = [
    "BehaviorEngine",
    "NPCBase",
    "ShopkeeperNPC",
    "PassiveMobNPC",
    "AggressiveMobNPC",
]
