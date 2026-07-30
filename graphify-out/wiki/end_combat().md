# .end combat()

> 214 nodes

## Key Concepts

- **TargetMatch** (122 connections) — `server/schemas/shared/target_resolution.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects.py** (37 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **run_heal_effect()** (15 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellEffectPlayer** (14 connections) — `server/game/magic/spell_effect_types.py`
- **SpellEffectsEngineHealPort** (13 connections) — `server/game/magic/spell_effect_types.py`
- **UUID** (13 connections)
- **UUID** (12 connections)
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **_steal_life_resolve_target_dp()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **Any** (10 connections)
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- *... and 189 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (57 shared connections)
- [message handler factory](message_handler_factory.md) (41 shared connections)
- [. initialize handlers()](_initialize_handlers%28%29.md) (25 shared connections)
- [CombatService](CombatService.md) (25 shared connections)
- [test player event handlers room](test_player_event_handlers_room.md) (12 shared connections)
- [test command service](test_command_service.md) (9 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (7 shared connections)
- [Any](Any.md) (6 shared connections)
- [close db()](close_db%28%29.md) (4 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 940 (97%)
- INFERRED: 27 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*