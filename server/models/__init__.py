"""
Database models for MythosMUD.

This package contains all database models including:
- User model (FastAPI Users)
- Player model (game data)
- Invite model (custom invite system)
- NPC models (NPC subsystem)
"""

from .alias import Alias
from .calendar import HolidayModel, NPCScheduleModel
from .container import ContainerComponent, ContainerLockState, ContainerSourceType
from .emote import Emote, EmoteAlias
from .game import AttributeType, Stats, StatusEffect, StatusEffectType
from .health import HealthErrorResponse, HealthResponse, HealthStatus
from .invite import Invite
from .item import ItemComponentState, ItemInstance, ItemPrototype
from .lucidity import LucidityAdjustmentLog, LucidityCooldown, LucidityExposureState, PlayerLucidity
from .npc import NPCDefinition, NPCDefinitionType, NPCRelationship, NPCSpawnRule
from .player import Player, PlayerExploration, PlayerInventory
from .player_effect import PlayerEffect
from .player_spells import PlayerSpell
from .spell import Spell, SpellEffectType, SpellMaterial, SpellRangeType, SpellSchool, SpellTargetType
from .spell_db import SpellDB
from .user import User
from .world import RoomLink, RoomModel, Subzone, Zone, ZoneConfigurationMapping

# ARCHITECTURE FIX Phase 3.1: Removed setup_relationships import
# Relationships now defined directly in model files using string references

__all__ = [
    "User",
    "Player",
    "PlayerInventory",
    "PlayerExploration",
    "HolidayModel",
    "NPCScheduleModel",
    "PlayerLucidity",
    "LucidityAdjustmentLog",
    "LucidityExposureState",
    "LucidityCooldown",
    "Invite",
    "Alias",
    "Emote",
    "EmoteAlias",
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
    "NPCRelationship",
    "ContainerComponent",
    "ContainerSourceType",
    "ContainerLockState",
    "Spell",
    "SpellSchool",
    "SpellTargetType",
    "SpellRangeType",
    "SpellEffectType",
    "SpellMaterial",
    "PlayerEffect",
    "PlayerSpell",
    "SpellDB",
    "Zone",
    "Subzone",
    "RoomModel",
    "RoomLink",
    "ZoneConfigurationMapping",
]
