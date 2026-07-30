# message handler factory

> 246 nodes

## Key Concepts

- **PlayerService** (140 connections) — `server/game/player_service.py`
- **magic_service.py** (39 connections) — `server/game/magic/magic_service.py`
- **PlayerSpellRepository** (36 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **SpellTargetingService** (31 connections) — `server/game/magic/spell_targeting.py`
- **SpellLearningService** (30 connections) — `server/game/magic/spell_learning_service.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **magic_service_completion.py** (25 connections) — `server/game/magic/magic_service_completion.py`
- **MagicServiceCompletionMixin** (21 connections) — `server/game/magic/magic_service_completion.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **magic.py** (19 connections) — `server/container/bundles/magic.py`
- **MagicBundle** (18 connections) — `server/container/bundles/magic.py`
- **CastingStateManager** (18 connections) — `server/game/magic/casting_state_manager.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellMaterialsService** (15 connections) — `server/game/magic/spell_materials.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (13 connections) — `server/container/bundles/magic.py`
- **UUID** (12 connections)
- **spell_costs.py** (12 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- *... and 221 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (111 shared connections)
- [CombatService](CombatService.md) (29 shared connections)
- [Player](Player.md) (22 shared connections)
- [world](world.md) (20 shared connections)
- [real time](real_time.md) (19 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (18 shared connections)
- [Any](Any.md) (18 shared connections)
- [.initialize()](initialize%28%29.md) (18 shared connections)
- [test magic commands](test_magic_commands.md) (17 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (14 shared connections)
- [command execution request](command_execution_request.md) (13 shared connections)
- [test command parser](test_command_parser.md) (8 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/casting_state_manager.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/magic_service_completion.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/game/player_service.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 1092 (85%)
- INFERRED: 190 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*