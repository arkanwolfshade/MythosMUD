# SpellRegistry

> 46 nodes

## Key Concepts

- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **spell_targeting_service()** (5 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **.movement_service()** (4 connections) — `server/game/magic/spell_effects.py`
- **.list_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **.connection_manager()** (3 connections) — `server/game/magic/spell_effects.py`
- **.get_spell()** (3 connections) — `server/game/magic/spell_registry.py`
- **.get_spell_by_name()** (3 connections) — `server/game/magic/spell_registry.py`
- **.__init__()** (3 connections) — `server/game/magic/spell_registry.py`
- **.search_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **SpellRepositoryClass** (3 connections)
- **.get_all_spell_ids()** (2 connections) — `server/game/magic/spell_registry.py`
- **.is_loaded()** (2 connections) — `server/game/magic/spell_registry.py`
- **Initialize MagicService and attach to app.state.** (1 connections) — `server/app/lifespan_magic.py`
- *... and 21 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (23 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (10 shared connections)
- [TargetMatch](TargetMatch.md) (6 shared connections)
- [SpellEffectType](SpellEffectType.md) (5 shared connections)
- [Spell](Spell.md) (5 shared connections)
- [SpellLearningService](SpellLearningService.md) (4 shared connections)
- [magic.py](magic.py.md) (3 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (3 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (3 shared connections)
- [SpellMaterial](SpellMaterial.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 112 (85%)
- INFERRED: 20 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*