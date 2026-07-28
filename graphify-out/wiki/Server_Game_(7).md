# Server Game (7)

> 90 nodes

## Key Concepts

- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **Protocol** (7 connections)
- **_add_healing_threat_if_in_combat()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_lookup_npc_by_id_or_uuid()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (7 connections) — `server/game/magic/spell_effects_internal.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **_is_heal_other_self_target()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_player_damage()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_resolve_npc_id_for_event()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 65 more nodes in this community*

## Relationships

- [Server Game (2)](Server_Game_%282%29.md) (33 shared connections)
- [Server Services (9)](Server_Services_%289%29.md) (23 shared connections)
- [Server Game (4)](Server_Game_%284%29.md) (7 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (7 shared connections)
- [Server Commands](Server_Commands.md) (6 shared connections)
- [Server Game (24)](Server_Game_%2824%29.md) (4 shared connections)
- [Server Services (29)](Server_Services_%2829%29.md) (4 shared connections)
- [Server Models (6)](Server_Models_%286%29.md) (3 shared connections)
- [Server Services (13)](Server_Services_%2813%29.md) (3 shared connections)
- [Server Npc](Server_Npc.md) (2 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (1 shared connections)
- [Server Game (14)](Server_Game_%2814%29.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service_state.py`

## Audit Trail

- EXTRACTED: 411 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*