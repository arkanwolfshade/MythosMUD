"""
Database models for MythosMUD.

This package contains all database models including:
- User model (FastAPI Users)
- Player model (game data)
- Invite model (custom invite system)
- NPC models (NPC subsystem)
"""

from .alias import Alias
from .container import ContainerComponent, ContainerLockState, ContainerSourceType
from .game import AttributeType, Stats, StatusEffect, StatusEffectType
from .health import HealthErrorResponse, HealthResponse, HealthStatus
from .invite import Invite
from .item import ItemComponentState, ItemInstance, ItemPrototype
from .npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from .player import Player
from .sanity import PlayerSanity, SanityAdjustmentLog, SanityCooldown, SanityExposureState
from .user import User

# ARCHITECTURE FIX Phase 3.1: Removed setup_relationships import
# Relationships now defined directly in model files using string references

__all__ = [
    "User",
    "Player",
    "PlayerSanity",
    "SanityAdjustmentLog",
    "SanityExposureState",
    "SanityCooldown",
    "Invite",
    "Alias",
    "ItemPrototype",
    "ItemInstance",
    "ItemComponentState",
    "Stats",
    "AttributeType",
    "StatusEffect",
    "StatusEffectType",
    "HealthResponse",
    "HealthErrorResponse",
    "HealthStatus",
    "NPCDefinition",
    "NPCDefinitionType",
    "NPCSpawnRule",
    "ContainerComponent",
    "ContainerSourceType",
    "ContainerLockState",
]
