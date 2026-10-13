"""
NPC disposition as sent to the client (#1025).

Mirrors ``server.models.npc.NPCDefinitionType`` value for value (kept in step by
``server/tests/unit/constants/test_npc_disposition.py``) but is import-free, so realtime leaf modules can use it
without pulling in SQLAlchemy. Each value is also the kind of an ``npc.<disposition>`` ``MessageCategory``, which
is how the client colours an NPC in the Occupants panel and, mid-line, in message segments.

Phantom hostiles (ADR-024) are always ``AGGRESSIVE_MOB``: they must look exactly like a real hostile.
"""

from enum import StrEnum
from typing import TypedDict


class NpcDisposition(StrEnum):
    """What a player should expect of an NPC on sight."""

    SHOPKEEPER = "shopkeeper"
    QUEST_GIVER = "quest_giver"
    PASSIVE_MOB = "passive_mob"
    AGGRESSIVE_MOB = "aggressive_mob"


class NpcOccupant(TypedDict):
    """One NPC in a ``room_occupants`` / ``room_update`` / ``game_state`` ``npcs`` list."""

    name: str
    disposition: NpcDisposition


DEFAULT_NPC_DISPOSITION = NpcDisposition.PASSIVE_MOB
"""Least alarming fallback for a missing or unrecognised NPC type."""
