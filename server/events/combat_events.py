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


@dataclass
class CombatEndedEvent(BaseEvent):
    """Event fired when combat ends."""

    combat_id: UUID
    room_id: str
    reason: str
    duration_seconds: int
    participants: dict[str, Any]  # final participant states


@dataclass
class PlayerAttackedEvent(BaseEvent):  # pylint: disable=too-many-instance-attributes  # Reason: Combat event requires many fields to capture complete attack state
    """Event fired when a player attacks."""

    combat_id: UUID
    room_id: str
    attacker_id: UUID
    attacker_name: str
    target_id: UUID
    target_name: str
    damage: int
    action_type: str
    target_current_dp: int
    target_max_dp: int


@dataclass
class NPCAttackedEvent(BaseEvent):  # pylint: disable=too-many-instance-attributes  # Reason: Combat event requires many fields to capture complete attack state
    """Event fired when an NPC is attacked."""

    combat_id: UUID
    room_id: str
    attacker_id: UUID
    attacker_name: str
    npc_id: UUID
    npc_name: str
    damage: int
    action_type: str
    target_current_dp: int
    target_max_dp: int


@dataclass
class NPCTookDamageEvent(BaseEvent):
    """Event fired when an NPC takes damage."""

    combat_id: UUID
    room_id: str
    npc_id: UUID
    npc_name: str
    damage: int
    current_dp: int
    max_dp: int


@dataclass
class NPCDiedEvent(BaseEvent):
    """Event fired when an NPC dies."""

    combat_id: UUID
    room_id: str
    npc_id: str | UUID  # AI Agent: Accept both string IDs (from lifecycle) and UUIDs (from combat)
    npc_name: str
    xp_reward: int


@dataclass
class CombatTurnAdvancedEvent(BaseEvent):
    """Event fired when combat turn advances."""

    combat_id: UUID
    room_id: str
    current_turn: int
    combat_round: int
    next_participant: str


@dataclass
class CombatTimeoutEvent(BaseEvent):
    """Event fired when combat times out."""

    combat_id: UUID
    room_id: str
    timeout_minutes: int
    last_activity: datetime
