"""
Events module for MythosMUD.

This module provides the event system for tracking room state changes,
player movements, and other game events. The system uses an in-memory
pub/sub pattern that can be extended to use Redis or other external
event systems in the future.

As noted in the Pnakotic Manuscripts, proper event tracking is essential
for maintaining awareness of the dimensional shifts that occur when
entities move between spaces.
"""

from .event_bus import EventBus
from .event_types import (
    BaseEvent,
    NPCEnteredRoom,
    NPCLeftRoom,
    ObjectAddedToRoom,
    ObjectRemovedFromRoom,
    PlayerEnteredRoom,
    PlayerLeftRoom,
)

__all__ = [
    "EventBus",
    "BaseEvent",
    "PlayerEnteredRoom",
    "PlayerLeftRoom",
    "ObjectAddedToRoom",
    "ObjectRemovedFromRoom",
    "NPCEnteredRoom",
    "NPCLeftRoom",
]
