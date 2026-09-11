"""
NPC <-> player corruption relationship (#815 PR-4).

An NPC's corruption is a static trait (`base_stats["corruption"]`, #815 PR-3's exploration found
it already parses through `parse_stats` with no schema change needed). This module holds *both*
halves of what that trait does to a player it perceives as corrupted, deliberately co-located:

- A discrete tier matrix for **speech** -- three outcomes a writer can actually author, selected
  inside `register_default_reactions_for_npc` as a variant of the greeting reaction, never a
  competing one (two reactions racing on the same event would be a coin flip: NPCEventReactionSystem
  only executes the first one whose condition matches).
- A continuous curve for **aggro** -- threat math wants a gradient, not a bucket, applied in
  `server/services/aggro_threat.py` alongside the existing `_aggression_scale`.

Keeping the duplicated NPC<->player corruption relation in one file, rather than reinventing it
independently in the reaction system and in aggro_threat.py, is the point of this module.
"""

from __future__ import annotations

from ..events.event_types import PlayerEnteredRoom
from ..models.corruption import CorruptionTier
from ..services.corruption_tier_cache import corruption_tier_cache
from .event_reaction_system import NPCEventReaction

# Matches CorruptionTier.MARKED (#815 PR-1) -- an NPC at or above this reads as "one of them" to a
# tainted player, same threshold the ambient room badge uses to go public.
NPC_TAINTED_THRESHOLD = 25

WELCOME_LINE = "Something in their bearing recognizes something in yours. They incline their head, unhurried."
RECOIL_LINE = "They go still as you approach, then step back half a pace, as if from a bad smell."


def build_corruption_aware_greeting(npc_id: str, npc_corruption: int, normal_greeting: str) -> NPCEventReaction:
    """
    A greeting reaction whose message depends on the entering player's corruption tier.

    - Player `pure`/`touched` (the permanent scar stays private, per #815 PR-2): the NPC's normal
      greeting, unchanged.
    - Player `marked`+ and this NPC is itself tainted (>= NPC_TAINTED_THRESHOLD): WELCOME_LINE.
    - Player `marked`+ and this NPC is not: RECOIL_LINE.

    Replaces `NPCEventReactionTemplates.player_entered_room_greeting` for shopkeeper/passive_mob
    NPCs -- it is a variant of that reaction, not an addition alongside it.
    """

    def condition(event: PlayerEnteredRoom, npc_context: dict[str, object]) -> bool:
        return event.room_id == npc_context.get("current_room")

    def action(event: PlayerEnteredRoom, npc_context: dict[str, object]) -> bool:
        room_id = npc_context.get("current_room")
        if not room_id or room_id == "unknown":
            return False
        # Circular import: chat_npc_system -> npc package -> this module (same pattern as the
        # plain templates in event_reaction_system.py).
        from ..game.chat_npc_system import schedule_npc_room_speech

        message = _pick_greeting(npc_corruption, normal_greeting, event.player_id)
        raw_name = npc_context.get("name")
        schedule_npc_room_speech(
            npc_id=npc_id,
            room_id=str(room_id),
            message=message,
            npc_name=raw_name if isinstance(raw_name, str) else None,
        )
        return True

    return NPCEventReaction(event_type=PlayerEnteredRoom, condition=condition, action=action, priority=1)


def _pick_greeting(npc_corruption: int, normal_greeting: str, player_id: str) -> str:
    tier = corruption_tier_cache.get_tier(player_id)
    if tier in (CorruptionTier.PURE, CorruptionTier.TOUCHED):
        return normal_greeting
    return WELCOME_LINE if npc_corruption >= NPC_TAINTED_THRESHOLD else RECOIL_LINE


def corruption_hostility_scale(npc_corruption: int | None, player_corruption: int | None) -> float:
    """
    Threat multiplier from the corruption gap between an NPC and a player, mirroring
    `aggro_threat._aggression_scale`'s shape (a 0.5-anchored linear scale).

    Kinship (similar corruption) softens hostility; opposition (a pure NPC facing a corrupted
    player, or vice versa) sharpens it. Missing data on *either* side scales as neutral (1.0),
    matching `_aggression_scale`'s `None => 1.0` convention -- two participants who are genuinely
    both untainted (0 and 0) is a real kinship signal and should discount, but a pair where
    corruption was simply never populated is not, and must not discount by accident.
    """
    if npc_corruption is None or player_corruption is None:
        return 1.0
    gap_fraction = abs(npc_corruption - player_corruption) / 100.0
    return 0.5 + gap_fraction


__all__ = [
    "NPC_TAINTED_THRESHOLD",
    "RECOIL_LINE",
    "WELCOME_LINE",
    "build_corruption_aware_greeting",
    "corruption_hostility_scale",
]
