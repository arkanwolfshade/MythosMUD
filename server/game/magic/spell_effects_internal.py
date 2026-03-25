"""
Internal helpers for spell_effects.py (coercion, combat room lookup).

Keeps the main engine module under the line-count budget; see ADR patterns for spell routing.
"""

from __future__ import annotations

from server.services.combat_service import CombatService
from server.services.combat_service_npc import get_combat_id_for_npc


def coerce_effect_int_times_mastery(raw: object, mastery: float) -> int:
    """Parse effect_data numeric (int, float, or numeric string) and apply mastery multiplier."""
    if isinstance(raw, (int, float)):
        return int(raw * mastery)
    if isinstance(raw, str) and raw.strip():
        try:
            return int(float(raw) * mastery)
        except ValueError:
            return 0
    return 0


def coerce_effect_float_times_mastery_as_int(raw: object, mastery: float) -> int:
    """Coerce to float first, then apply mastery (lucidity-style deltas)."""
    if isinstance(raw, (int, float)):
        base = float(raw)
    elif isinstance(raw, str) and raw.strip():
        try:
            base = float(raw)
        except ValueError:
            base = 0.0
    else:
        base = 0.0
    return int(base * mastery)


def combat_room_id_for_npc_spell(cs: CombatService | None, npc_target_id: str) -> str | None:
    """Active combat room_id for an NPC, if any."""
    if cs is None:
        return None
    combat_id = get_combat_id_for_npc(cs, npc_target_id)
    if not combat_id:
        return None
    combat = cs.get_combat(combat_id)
    if combat and combat.room_id:
        return combat.room_id
    return None
