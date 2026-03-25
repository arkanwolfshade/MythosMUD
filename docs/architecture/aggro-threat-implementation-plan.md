# Aggro and Threat System Implementation Plan

This document summarizes the implementation of the room-based aggro and threat system
(ADR-016). For the design and formulas, see [aggro-threat-system.md](aggro-threat-system.md).

## Status

Implemented. All phases are in place: data model, threat API, UpdateAggro, damage/healing/
taunt/stealth integration, NPC target selection from aggro, target-switch broadcast,
lifecycle cleanup, unit and integration tests, client handler, and documentation.

## Key Modules and Files

| Area                    | Location                                                                                                                                                                                                                                                             |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hate list / target      | [server/models/combat.py](../../server/models/combat.py) – `npc_hate_lists`, `npc_current_target` on `CombatInstance`                                                                                                                                                |
| Threat + UpdateAggro    | [server/services/aggro_threat.py](../../server/services/aggro_threat.py)                                                                                                                                                                                             |
| Config                  | [server/config/models.py](../../server/config/models.py) – `GameConfig`: `aggro_stability_margin`, `aggro_healing_threat_factor`, `aggro_damage_threat_multiplier`                                                                                                   |
| Damage integration      | [server/services/combat_service_attack.py](../../server/services/combat_service_attack.py); spell damage in [server/game/magic/spell_effects.py](../../server/game/magic/spell_effects.py)                                                                           |
| Healing integration     | [server/game/magic/spell_effects_heal.py](../../server/game/magic/spell_effects_heal.py)                                                                                                                                                                             |
| Taunt command           | [server/commands/combat.py](../../server/commands/combat.py) – taunt with room check                                                                                                                                                                                 |
| Stealth wipe            | [server/services/aggro_threat.py](../../server/services/aggro_threat.py) – `on_player_entered_stealth()`; call when stealth is entered                                                                                                                               |
| NPC target selection    | [server/services/combat_turn_participant_actions.py](../../server/services/combat_turn_participant_actions.py) – UpdateAggro then `get_npc_current_target`; fallback to `_select_npc_target`                                                                         |
| Target-switch broadcast | [server/services/combat_messaging_integration.py](../../server/services/combat_messaging_integration.py) – `broadcast_combat_target_switch()`                                                                                                                        |
| Combat end cleanup      | [server/services/combat_service.py](../../server/services/combat_service.py) – call `clear_aggro_for_combat(combat)` on end; dead excluded in UpdateAggro candidate selection                                                                                        |
| NPC aggro metadata      | [server/services/combat_types.py](../../server/services/combat_types.py) – `CombatParticipantData.npc_type`, `aggression_level`; [npc_combat_data_provider.py](../../server/services/npc_combat_data_provider.py) – reads from instance + `get_behavior_config()`    |
| Unit tests              | [server/tests/unit/services/test_aggro_threat.py](../../server/tests/unit/services/test_aggro_threat.py)                                                                                                                                                             |
| Integration tests       | [server/tests/integration/test_aggro_flow.py](../../server/tests/integration/test_aggro_flow.py)                                                                                                                                                                     |
| Client                  | [client/src/components/ui-v2/eventHandlers/combatHandlers.ts](../../client/src/components/ui-v2/eventHandlers/combatHandlers.ts) – `handleCombatTargetSwitch`; [projector.ts](../../client/src/components/ui-v2/eventLog/projector.ts) – `combat_target_switch` case |

## Constants (locked)

- **Stability margin:** 0.10 (10%); config: `aggro_stability_margin`.
- **Healing threat factor:** 0.5; config: `aggro_healing_threat_factor`.
- **Stealth:** Option A (wipe) – player removed from hate list on stealth enter.

## Integration with NPC static data (behavior_config / npc_type)

At combat join, each NPC's `npc_type` and `behavior_config.aggression_level` (0–10) are read from the
NPC instance and stored on the combat participant ([CombatParticipantData](../../server/services/combat_types.py),
then [CombatParticipant](../../server/models/combat.py)). [get_npc_combat_data](../../server/services/npc_combat_data_provider.py)
reads `npc_type` and `get_behavior_config().get("aggression_level")` (clamped 0–10).

- **passive_mob:** Damage does not add threat; only taunt and healing add threat. Healers can pull passive mobs.
- **aggressive_mob** (and other npc_types when in combat): Damage, healing, and taunt add threat as normal.
- **aggression_level:** Scales the effective threat multiplier: `0.5 + 0.05 * level` (0 → 0.5x, 10 → 1.0x). Applied to
  both damage and healing threat. If missing, treated as 10 (full threat).

See [ADR-016](decisions/ADR-016-aggro-threat-management.md) for the full decision.

## References

- [ADR-016: Aggro and Threat Management System](decisions/ADR-016-aggro-threat-management.md)
- [Aggro and Threat System Design](aggro-threat-system.md)
