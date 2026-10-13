# Magic & Tick Services

> 157 nodes

## Key Concepts

- **Spell** (108 connections) — `server/models/spell.py`
- **TargetMatch** (87 connections) — `server/schemas/shared/target_resolution.py`
- **_MagicServiceCore** (44 connections) — `server/game/magic/magic_service.py`
- **spell_effects_heal.py** (31 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **SpellTargetingService** (26 connections) — `server/game/magic/spell_targeting.py`
- **run_heal_effect()** (25 connections) — `server/game/magic/spell_effects_heal.py`
- **UUID** (21 connections)
- **JsonMap** (12 connections)
- **asyncio** (12 connections)
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **.can_cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **.cast_spell()** (10 connections) — `server/game/magic/magic_service.py`
- **._execute_instant_or_delayed_cast()** (10 connections) — `server/game/magic/magic_service.py`
- **UUID** (10 connections)
- **._get_spell_and_validate_target()** (9 connections) — `server/game/magic/magic_service.py`
- **._start_delayed_cast()** (9 connections) — `server/game/magic/magic_service.py`
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_standard_heal_after_validation()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **TargetMatch** (9 connections)
- *... and 132 more nodes in this community*

## Relationships

- [Community 50](Community_50.md) (35 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (30 shared connections)
- [Community 195](Community_195.md) (22 shared connections)
- [Community 187](Community_187.md) (15 shared connections)
- [Spell Effects & Combat Wiring](Spell_Effects_&_Combat_Wiring.md) (14 shared connections)
- [Community 45](Community_45.md) (14 shared connections)
- [Community 784](Community_784.md) (13 shared connections)
- [Magic Service Lifespan](Magic_Service_Lifespan.md) (12 shared connections)
- [Community 416](Community_416.md) (11 shared connections)
- [Community 452](Community_452.md) (5 shared connections)
- [Community 55](Community_55.md) (5 shared connections)
- [Community 283](Community_283.md) (5 shared connections)

## Source Files

- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`

## Audit Trail

- EXTRACTED: 508 (88%)
- INFERRED: 72 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*