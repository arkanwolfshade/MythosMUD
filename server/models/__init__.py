"""
Database models for MythosMUD.

This package contains all database models including:
- User model (FastAPI Users)
- Player model (game data)
- Invite model (custom invite system)
- NPC models (NPC subsystem)
"""

from .alias import Alias
from .game import AttributeType, Stats, StatusEffect, StatusEffectType
from .health import HealthErrorResponse, HealthResponse, HealthStatus
from .invite import Invite
from .npc import NPCDefinition, NPCDefinitionType, NPCSpawnRule
from .player import Player
from .relationships import setup_relationships
from .user import User

__all__ = [
    "User",
    "Player",
    "Invite",
    "Alias",
    "setup_relationships",
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
]
