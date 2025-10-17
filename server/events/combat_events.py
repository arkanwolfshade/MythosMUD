"""
Combat-specific events for the MUD.

This module defines combat-related events that extend the existing
event system to handle combat actions and state changes.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID

from server.events.event_types import BaseEvent


@dataclass
class CombatStartedEvent(BaseEvent):
    """Event fired when combat begins."""

    combat_id: UUID
    room_id: str
    participants: dict[str, Any]  # participant info
    turn_order: list[str]
    timestamp: datetime


@dataclass
class CombatEndedEvent(BaseEvent):
    """Event fired when combat ends."""

    combat_id: UUID
    room_id: str
    reason: str
    duration_seconds: int
    participants: dict[str, Any]  # final participant states
    timestamp: datetime


@dataclass
class PlayerAttackedEvent(BaseEvent):
    """Event fired when a player attacks."""

    combat_id: UUID
    attacker_id: UUID
    attacker_name: str
    target_id: UUID
    target_name: str
    damage: int
    action_type: str
    timestamp: datetime


@dataclass
class NPCAttackedEvent(BaseEvent):
    """Event fired when an NPC is attacked."""

    combat_id: UUID
    attacker_id: UUID
    attacker_name: str
    npc_id: UUID
    npc_name: str
    damage: int
    action_type: str
    timestamp: datetime


@dataclass
class NPCTookDamageEvent(BaseEvent):
    """Event fired when an NPC takes damage."""

    combat_id: UUID
    npc_id: UUID
    npc_name: str
    damage: int
    current_hp: int
    max_hp: int
    timestamp: datetime


@dataclass
class NPCDiedEvent(BaseEvent):
    """Event fired when an NPC dies."""

    combat_id: UUID
    npc_id: UUID
    npc_name: str
    xp_reward: int
    timestamp: datetime


@dataclass
class CombatTurnAdvancedEvent(BaseEvent):
    """Event fired when combat turn advances."""

    combat_id: UUID
    room_id: str
    current_turn: int
    combat_round: int
    next_participant: str
    timestamp: datetime


@dataclass
class CombatTimeoutEvent(BaseEvent):
    """Event fired when combat times out."""

    combat_id: UUID
    room_id: str
    timeout_minutes: int
    last_activity: datetime
    timestamp: datetime
