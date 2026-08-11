# Distributed Event Bus

> 69 nodes

## Key Concepts

- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (18 connections) — `server/game/magic/spell_effect_types.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectsEngineHealPort** (14 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
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
- **combat_service_state.py** (6 connections) — `server/services/combat_service_state.py`
- **UUID** (5 connections)
- **PlayerServiceHealPort** (5 connections) — `server/game/magic/spell_effect_types.py`
- *... and 44 more nodes in this community*

## Relationships

- [Player Respawn Service](Player_Respawn_Service.md) (25 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (14 shared connections)
- [Magic Service Bundle](Magic_Service_Bundle.md) (11 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (7 shared connections)
- [Health Check Models](Health_Check_Models.md) (4 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [Lucidity State Models](Lucidity_State_Models.md) (2 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (2 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service_state.py`

## Audit Trail

- EXTRACTED: 316 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*