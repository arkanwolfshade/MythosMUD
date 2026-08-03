# spell game magic

> 203 nodes

## Key Concepts

- **TargetMatch** (122 connections) — `server/schemas/shared/target_resolution.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **test_spell_effects.py** (37 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
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
- **PlayerPersistenceSpellPort** (10 connections) — `server/game/magic/spell_effect_types.py`
- **_run_standard_heal_after_validation()** (10 connections) — `server/game/magic/spell_effects_heal.py`
- **._process_damage()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_lucidity_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **._process_corruption_adjust()** (9 connections) — `server/game/magic/spell_effects.py`
- **get_npc_instance_for_steal_life()** (9 connections) — `server/game/magic/spell_effects_heal.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **._process_heal()** (8 connections) — `server/game/magic/spell_effects.py`
- **._add_spell_damage_threat_to_combat()** (8 connections) — `server/game/magic/spell_effects.py`
- **._publish_npc_damage_and_death_events()** (8 connections) — `server/game/magic/spell_effects.py`
- *... and 178 more nodes in this community*

## Relationships

- [spell models rationale](spell_models_rationale.md) (47 shared connections)
- [Item Instances](Item_Instances.md) (46 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (24 shared connections)
- [combat commands handler](combat_commands_handler.md) (17 shared connections)
- [game models player](game_models_player.md) (8 shared connections)
- [spell game magic](spell_game_magic.md) (7 shared connections)
- [target resolution service](target_resolution_service.md) (6 shared connections)
- [magic completion game](magic_completion_game.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [calendar models rationale](calendar_models_rationale.md) (4 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (4 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (2 shared connections)

## Source Files

- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_targeting.py`
- `server/schemas/shared/target_resolution.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/schemas/test_target_resolution.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 865 (95%)
- INFERRED: 45 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*