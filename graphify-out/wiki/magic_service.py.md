# magic_service.py

> 111 nodes

## Key Concepts

- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **spell.py** (29 connections) — `server/models/spell.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **test_spell_registry.py** (19 connections) — `server/tests/unit/game/magic/test_spell_registry.py`
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- *... and 86 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (35 shared connections)
- [TargetMatch](TargetMatch.md) (31 shared connections)
- [SpellEffectType](SpellEffectType.md) (29 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (15 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (12 shared connections)
- [SpellLearningService](SpellLearningService.md) (11 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (11 shared connections)
- [User](User.md) (10 shared connections)
- [CombatService](CombatService.md) (9 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (9 shared connections)
- [test_spell_effects.py](test_spell_effects.py.md) (8 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (6 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_registry.py`

## Audit Trail

- EXTRACTED: 366 (90%)
- INFERRED: 42 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*