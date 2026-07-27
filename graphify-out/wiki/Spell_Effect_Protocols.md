# Spell Effect Protocols

> 140 nodes · cohesion 0.04

## Key Concepts

- **SpellEffects** (66 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (33 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects.py** (30 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectPlayer** (26 connections) — `server/game/magic/spell_effect_types.py`
- **NpcSpellDamageTarget** (25 connections) — `server/game/magic/spell_effect_types.py`
- **TargetMatch** (24 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (22 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (22 connections) — `server/game/magic/spell_effects.py`
- **UUID** (20 connections) — `server/game/magic/spell_effects_heal.py`
- **Spell** (20 connections) — `server/game/magic/spell_effects.py`
- **PlayerPersistenceSpellPort** (18 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectType** (18 connections) — `server/models/spell.py`
- **CombatService** (16 connections) — `server/game/magic/spell_effects_heal.py`
- **TargetMatch** (16 connections) — `server/game/magic/spell_effects_heal.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **NpcSpellDamageTarget** (13 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effects_heal.py`
- **NpcIntegrationStringIdPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **Spell** (12 connections) — `server/game/magic/spell_effects_heal.py`
- **CombatService** (12 connections) — `server/game/magic/spell_effects.py`
- **MovementService** (12 connections) — `server/game/magic/spell_effects.py`
- **NpcSpellDamageTarget** (12 connections) — `server/game/magic/spell_effects.py`
- **NpcLifecycleManagerPort** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- *... and 115 more nodes in this community*

## Relationships

- [[Magic Service Bundle]] (29 shared connections)
- [[Spell Registry Costs]] (23 shared connections)
- [[Combat Service Bundle]] (23 shared connections)
- [[Combat Command Handler]] (15 shared connections)
- [[Game Magic Spell]] (12 shared connections)
- [[Distributed Event Bus]] (11 shared connections)
- [[Player Combat XP]] (6 shared connections)
- [[Combat NPC Lookup]] (6 shared connections)
- [[Spell Effects Tests]] (6 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[Combat Aggro Threat]] (4 shared connections)
- [[Magic Game Service]] (4 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/models/spell.py`

## Audit Trail

- EXTRACTED: 616 (71%)
- INFERRED: 253 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
