# spell game magic

> 100 nodes

## Key Concepts

- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **combat_room_id_for_npc_spell()** (8 connections) — `server/game/magic/spell_effects_internal.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **test_spell_effects_internal.py** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_internal.py`
- **Protocol** (7 connections)
- **_add_healing_threat_if_in_combat()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_lookup_npc_by_id_or_uuid()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- *... and 75 more nodes in this community*

## Relationships

- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (37 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (21 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (10 shared connections)
- [Error Conversion](Error_Conversion.md) (6 shared connections)
- [subject admin controller](subject_admin_controller.md) (5 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (4 shared connections)
- [room validator toolkit](room_validator_toolkit.md) (3 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (2 shared connections)
- [services ascii map](services_ascii_map.md) (2 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [quest game service](quest_game_service.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`

## Audit Trail

- EXTRACTED: 454 (97%)
- INFERRED: 12 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*