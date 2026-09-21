# spell_effects.py

> 94 nodes

## Key Concepts

- **spell_effects.py** (53 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (10 connections)
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **get_combat_service()** (8 connections) — `server/services/combat_service_state.py`
- **test_spell_effects_internal.py** (8 connections) — `server/tests/unit/game/magic/test_spell_effects_internal.py`
- **._create_combat_service_with_nats()** (7 connections) — `server/container/bundles/combat.py`
- **_lookup_npc_by_id_or_uuid()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_resolve_npc_id_for_event()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **Protocol** (7 connections)
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_apply_npc_damage_only()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_player_damage()** (6 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 69 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (49 shared connections)
- [get_logger](get_logger.md) (15 shared connections)
- [CombatService](CombatService.md) (13 shared connections)
- [CombatInstance](CombatInstance.md) (13 shared connections)
- [run_flee_effect](run_flee_effect.md) (4 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (3 shared connections)
- [SpellEffectType](SpellEffectType.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [NPCDefinition](NPCDefinition.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [CorruptionTier](CorruptionTier.md) (2 shared connections)

## Source Files

- `server/container/bundles/combat.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`

## Audit Trail

- EXTRACTED: 242 (88%)
- INFERRED: 33 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*