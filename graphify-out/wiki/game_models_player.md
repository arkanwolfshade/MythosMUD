# game models player

> 327 nodes

## Key Concepts

- **Spell** (84 connections) — `server/models/spell.py`
- **SpellEffects** (56 connections) — `server/game/magic/spell_effects.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **_MagicServiceCore** (42 connections) — `server/game/magic/magic_service.py`
- **magic_service.py** (39 connections) — `server/game/magic/magic_service.py`
- **test_spell_effects.py** (37 connections) — `server/tests/unit/game/magic/test_spell_effects.py`
- **PlayerSpellRepository** (36 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **SpellLearningService** (30 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **UUID** (20 connections)
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **Any** (18 connections)
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellMaterialsService** (15 connections) — `server/game/magic/spell_materials.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- *... and 302 more nodes in this community*

## Relationships

- [target resolution service](target_resolution_service.md) (58 shared connections)
- [spell game magic](spell_game_magic.md) (43 shared connections)
- [command inventory factories](command_inventory_factories.md) (37 shared connections)
- [Error Conversion](Error_Conversion.md) (26 shared connections)
- [Database Config](Database_Config.md) (23 shared connections)
- [command inventory models](command_inventory_models.md) (20 shared connections)
- [commands admin mute](commands_admin_mute.md) (16 shared connections)
- [command factories exploration](command_factories_exploration.md) (15 shared connections)
- [magic completion game](magic_completion_game.md) (14 shared connections)
- [NPC Combat](NPC_Combat.md) (13 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (12 shared connections)
- [startup npc services](startup_npc_services.md) (8 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 1400 (90%)
- INFERRED: 153 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*