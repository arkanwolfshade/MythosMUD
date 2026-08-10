# Combat Attack Service

> 257 nodes

## Key Concepts

- **CombatService** (182 connections) — `server/services/combat_service.py`
- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **combat_service_npc.py** (30 connections) — `server/services/combat_service_npc.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **NpcSpellDamageTarget** (18 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectPlayer** (15 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectsEngineHealPort** (14 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **get_combat_id_for_npc()** (13 connections) — `server/services/combat_service_npc.py`
- **UUID** (12 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (11 connections)
- **get_npc_participant_current_room()** (11 connections) — `server/services/combat_service_npc.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_internal.py** (10 connections) — `server/game/magic/spell_effects_internal.py`
- **_get_uuid_mapping()** (10 connections) — `server/services/combat_service_npc.py`
- **find_participant_uuid_by_string_id()** (10 connections) — `server/services/combat_service_npc.py`
- *... and 232 more nodes in this community*

## Relationships

- [NPC Service Tests](NPC_Service_Tests.md) (89 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (37 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (32 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (26 shared connections)
- [Logging Correct Patterns](Logging_Correct_Patterns.md) (23 shared connections)
- [NPC Services Bundle](NPC_Services_Bundle.md) (20 shared connections)
- [test_profession_meets_stat_requirements_multiple_not_met](test_profession_meets_stat_requirements_multiple_not_met.md) (15 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (13 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (12 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (11 shared connections)
- [Health Check Models](Health_Check_Models.md) (10 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (8 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service.py`
- `server/services/combat_service_npc.py`
- `server/services/combat_service_state.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/game/magic/test_spell_effects.py`

## Audit Trail

- EXTRACTED: 1238 (93%)
- INFERRED: 89 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*