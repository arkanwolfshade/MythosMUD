# spell_effects_heal.py

> 73 nodes · cohesion 0.05

## Key Concepts

- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **Protocol** (7 connections)
- **_add_healing_threat_if_in_combat()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_lookup_npc_by_id_or_uuid()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **_is_heal_other_self_target()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_resolve_npc_id_for_event()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_player_damage()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **PlayerServiceHealPort** (5 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (5 connections)
- **_coerce_effect_int()** (5 connections) — `server/game/magic/spell_effects_heal.py`
- **_get_npc_lifecycle_manager()** (5 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 48 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (39 shared connections)
- [CombatService](CombatService.md) (17 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [aggro_threat.py](aggro_threat.py.md) (2 shared connections)
- [SpellRegistry](SpellRegistry.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects_heal.py`

## Audit Trail

- EXTRACTED: 314 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*