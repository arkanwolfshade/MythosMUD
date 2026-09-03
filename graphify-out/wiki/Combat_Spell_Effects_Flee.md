# Combat Spell Effects (Flee)

> 269 nodes

## Key Concepts

- **TargetMatch** (160 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (136 connections) — `server/models/spell.py`
- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **TargetType** (41 connections) — `server/schemas/shared/target_resolution.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **run_flee_effect()** (25 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **test_spell_effect_flee.py** (18 connections) — `server/tests/unit/game/magic/test_spell_effect_flee.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects_support.py** (14 connections) — `server/tests/unit/game/magic/test_spell_effects_support.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **process_create_object_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- *... and 244 more nodes in this community*

## Relationships

- [Test Spell](Test_Spell.md) (37 shared connections)
- [Test Spell Effects](Test_Spell_Effects.md) (34 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (29 shared connections)
- [Lifespan Magic](Lifespan_Magic.md) (27 shared connections)
- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (26 shared connections)
- [Combat Service Attack](Combat_Service_Attack.md) (25 shared connections)
- [Magic Service](Magic_Service.md) (21 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (20 shared connections)
- [Combat Taunt](Combat_Taunt.md) (13 shared connections)
- [Spell Learning Service](Spell_Learning_Service.md) (10 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (8 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (7 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effect_flee.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/game/magic/test_spell_effects_support.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 879 (88%)
- INFERRED: 119 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*