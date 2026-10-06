"""
Utility threat for buffs and debuffs (#833, ADR-016 section 3).

A support caster who applies a status effect or stat modifier in a fight draws the NPC's attention even though
they dealt no damage, so a buffer or debuffer can pull. Healing and damage threat already exist; this is the third
source.
"""

from __future__ import annotations

import uuid

from server.models.combat import CombatParticipantType
from server.schemas.shared import TargetMatch, TargetType
from server.services.aggro_threat import add_utility_threat
from server.services.combat_service import CombatService
from server.services.combat_service_npc import resolve_npc_participant_id_in_combat


def add_utility_threat_for_spell(
    combat_service: CombatService | None, caster_id: uuid.UUID, target: TargetMatch
) -> None:
    """
    Add utility threat in the caster's combat for a successfully applied buff or debuff. No-op outside combat.

    A debuff on an NPC draws only that NPC. A buff on the caster or an ally draws every NPC in the fight, as
    healing does. Targets that are neither a player nor an NPC (a location, say) add nothing.
    """
    if combat_service is None or target.target_type not in (TargetType.PLAYER, TargetType.NPC):
        return
    combat_id = combat_service.get_combat_id_for_participant(caster_id)
    if combat_id is None:
        return
    combat = combat_service.get_combat(combat_id)
    if combat is None:
        return

    if target.target_type == TargetType.NPC:
        npc_id = resolve_npc_participant_id_in_combat(combat_service, combat, str(target.target_id))
        drawn = [] if npc_id is None else [npc_id]
    else:
        drawn = [pid for pid, p in combat.participants.items() if p.participant_type == CombatParticipantType.NPC]

    for npc_id in drawn:
        add_utility_threat(combat, npc_id, caster_id, npc_participant=combat.participants.get(npc_id))
