"""
NPC subsystem for MythosMUD.

This package provides the NPC (Non-Player Character) subsystem including
threading, message queues, behaviors, and integration with the main game systems.

As noted in the Pnakotic Manuscripts, proper management of non-human entities
is essential for maintaining the delicate balance between order and chaos
in our eldritch digital realm.
"""

from .behaviors import (
    AggressiveMobNPC,
    BehaviorEngine,
    NPCBase,
    PassiveMobNPC,
    ShopkeeperNPC,
)
from .combat_integration import NPCCombatIntegration
from .communication_integration import NPCCommunicationIntegration
from .event_reaction_system import NPCEventReaction, NPCEventReactionSystem, NPCEventReactionTemplates
from .lifecycle_manager import NPCLifecycleEvent, NPCLifecycleManager, NPCLifecycleRecord, NPCLifecycleState
from .movement_integration import NPCMovementIntegration
from .population_control import NPCPopulationController, PopulationStats, ZoneConfiguration

# from .spawning_service import NPCSpawningService, NPCSpawnRequest, NPCSpawnResult
from .threading import (
    NPCActionMessage,
    NPCActionType,
    NPCCommunicationBridge,
    NPCMessageQueue,
    NPCThreadManager,
)

# REMOVED: Import of duplicate NPCLifecycleManager from threading.py
# The authoritative NPCLifecycleManager is imported from lifecycle_manager above

__all__ = [
    "NPCActionMessage",
    "NPCActionType",
    "NPCMessageQueue",
    "NPCThreadManager",
    "NPCCommunicationBridge",
    "NPCBase",
    "BehaviorEngine",
    "ShopkeeperNPC",
    "PassiveMobNPC",
    "AggressiveMobNPC",
    "NPCCombatIntegration",
    "NPCCommunicationIntegration",
    "NPCEventReaction",
    "NPCEventReactionSystem",
    "NPCEventReactionTemplates",
    "NPCMovementIntegration",
    "NPCPopulationController",
    "PopulationStats",
    "ZoneConfiguration",
    "NPCLifecycleEvent",
    "NPCLifecycleManager",
    "NPCLifecycleRecord",
    "NPCLifecycleState",
    # "NPCSpawnRequest",
    # "NPCSpawnResult",
    # "NPCSpawningService",
]
