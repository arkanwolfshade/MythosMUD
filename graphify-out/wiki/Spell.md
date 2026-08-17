# Spell

> 112 nodes

## Key Concepts

- **Spell** (136 connections) — `server/models/spell.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (10 connections)
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_publish_npc_events()** (8 connections) — `server/game/magic/spell_effects_heal.py`
- **_is_heal_other_self_target()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_lookup_npc_by_id_or_uuid()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **_resolve_npc_id_for_event()** (7 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_heal()** (7 connections) — `server/game/magic/spell_effects.py`
- **Protocol** (7 connections)
- **NpcIntegrationStringIdPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- **NpcLifecycleManagerPort** (6 connections) — `server/game/magic/spell_effect_types.py`
- *... and 87 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (47 shared connections)
- [SpellEffectType](SpellEffectType.md) (25 shared connections)
- [AliasStorage](AliasStorage.md) (15 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (15 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (15 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (13 shared connections)
- [SpellLearningService](SpellLearningService.md) (10 shared connections)
- [spell_effects_status.py](spell_effects_status.py.md) (7 shared connections)
- [spell_effects_support.py](spell_effects_support.py.md) (6 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (6 shared connections)
- [SpellRegistry](SpellRegistry.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`

## Audit Trail

- EXTRACTED: 312 (76%)
- INFERRED: 97 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*