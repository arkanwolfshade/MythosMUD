# server commands combat taunt rationale

> 172 nodes

## Key Concepts

- **TargetMatch** (152 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (120 connections) — `server/models/spell.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (41 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects_heal.py** (29 connections) — `server/tests/unit/game/magic/test_spell_effects_heal.py`
- **run_heal_effect()** (26 connections) — `server/game/magic/spell_effects_heal.py`
- **spell_effects_support.py** (20 connections) — `server/game/magic/spell_effects_support.py`
- **NpcSpellDamageTarget** (17 connections) — `server/game/magic/spell_effect_types.py`
- **._dispatch_effect()** (15 connections) — `server/game/magic/spell_effects.py`
- **SpellEffectsEngineHealPort** (12 connections) — `server/game/magic/spell_effect_types.py`
- **asyncio** (12 connections)
- **SpellEffectPlayer** (11 connections) — `server/game/magic/spell_effect_types.py`
- **get_npc_instance_for_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_run_steal_life()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_apply_target_damage()** (11 connections) — `server/game/magic/spell_effects_heal.py`
- **process_create_object_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **process_stat_modify_effect()** (11 connections) — `server/game/magic/spell_effects_support.py`
- **spell_effect_types.py** (11 connections) — `server/game/magic/spell_effect_types.py`
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **_steal_life_resolve_target_dp()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (10 connections)
- **_add_healing_threat_if_in_combat()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **coerce_effect_int_times_mastery()** (9 connections) — `server/game/magic/spell_effects_internal.py`
- *... and 147 more nodes in this community*

## Relationships

- [server game magic spell effects](server_game_magic_spell_effects.md) (66 shared connections)
- [server game magic spell registry](server_game_magic_spell_registry.md) (31 shared connections)
- [server container bundles combat combatbundle](server_container_bundles_combat_combatbundle.md) (29 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (26 shared connections)
- [server game magic casting state](server_game_magic_casting_state.md) (18 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (16 shared connections)
- [server game magic spell effect](server_game_magic_spell_effect.md) (14 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (12 shared connections)
- [server game magic spell learning](server_game_magic_spell_learning.md) (11 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (10 shared connections)
- [server tests unit game magic](server_tests_unit_game_magic.md) (10 shared connections)
- [server game magic spell targeting](server_game_magic_spell_targeting.md) (9 shared connections)

## Source Files

- `server/commands/combat_taunt.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/models/spell.py`
- `server/schemas/shared/target_resolution.py`
- `server/services/combat_service_state.py`
- `server/tests/unit/game/magic/test_spell_effects_heal.py`

## Audit Trail

- EXTRACTED: 573 (84%)
- INFERRED: 112 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*