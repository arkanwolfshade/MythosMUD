# spell game magic

> 285 nodes

## Key Concepts

- **TargetMatch** (158 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (124 connections) — `server/models/spell.py`
- **SpellEffects** (61 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **test_spell_effects.py** (45 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellTargetingService** (32 connections) — `server/game/magic/spell_targeting.py`
- **test_spell_effects_heal.py** (28 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **test_spell_targeting.py** (28 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
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
- **spell_effects_internal.py** (11 connections) — `server/game/magic/spell_effects_internal.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- *... and 260 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (66 shared connections)
- [game models player](game_models_player.md) (51 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (25 shared connections)
- [player respawn event](player_respawn_event.md) (20 shared connections)
- [character creation service](character_creation_service.md) (18 shared connections)
- [magic completion game](magic_completion_game.md) (15 shared connections)
- [admin commands setstat](admin_commands_setstat.md) (13 shared connections)
- [models npc rationale](models_npc_rationale.md) (12 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (12 shared connections)
- [combat commands handler](combat_commands_handler.md) (11 shared connections)
- [subject nats manager](subject_nats_manager.md) (9 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (8 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`
- `server/tests/unit/game/magic/test_spell_effects_internal.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/schemas/test_target_resolution.py`

## Audit Trail

- EXTRACTED: 1342 (94%)
- INFERRED: 93 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*