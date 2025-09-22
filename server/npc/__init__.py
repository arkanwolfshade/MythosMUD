"""
NPC subsystem for MythosMUD.

This package provides the NPC (Non-Player Character) subsystem including
threading, message queues, behaviors, and integration with the main game systems.

As noted in the Pnakotic Manuscripts, proper management of non-human entities
is essential for maintaining the delicate balance between order and chaos
in our eldritch digital realm.
"""

from .threading import (
    NPCActionMessage,
    NPCActionType,
    NPCCommunicationBridge,
    NPCLifecycleManager,
    NPCMessageQueue,
    NPCThreadManager,
)

__all__ = [
    "NPCActionMessage",
    "NPCActionType",
    "NPCMessageQueue",
    "NPCThreadManager",
    "NPCCommunicationBridge",
    "NPCLifecycleManager",
]
