# Combat Attack Service

> 499 nodes

## Key Concepts

- **TargetMatch** (121 connections) — `server/schemas/shared/target_resolution.py`
- **Spell** (93 connections) — `server/models/spell.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (48 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_heal.py** (40 connections) — `server/game/magic/spell_effects_heal.py`
- **SpellLearningService** (38 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_effects.py** (38 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (37 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (35 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **MagicService** (30 connections) — `server/game/magic/magic_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **SpellTargetingService** (29 connections) — `server/game/magic/spell_targeting.py`
- **test_damage_grace_period.py** (27 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **SpellEffectsDeps** (25 connections) — `server/game/magic/spell_effects.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (18 connections) — `server/game/magic/magic_service.py`
- **run_flee_effect()** (18 connections) — `server/game/magic/spell_effect_flee.py`
- **NpcSpellDamageTarget** (18 connections) — `server/game/magic/spell_effect_types.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **spell_effect_flee.py** (17 connections) — `server/game/magic/spell_effect_flee.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- *... and 474 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (147 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (35 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (26 shared connections)
- [Security Headers Middleware](Security_Headers_Middleware.md) (25 shared connections)
- [NPC Admin Commands](NPC_Admin_Commands.md) (15 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (15 shared connections)
- [Player Domain Model](Player_Domain_Model.md) (12 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (11 shared connections)
- [Command Factory Tests](Command_Factory_Tests.md) (11 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (8 shared connections)
- [Player Name Validation](Player_Name_Validation.md) (7 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (7 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effect_flee.py`
- `server/game/magic/spell_effect_types.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_heal.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/game.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/schemas/shared/target_resolution.py`

## Audit Trail

- EXTRACTED: 2188 (92%)
- INFERRED: 188 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*