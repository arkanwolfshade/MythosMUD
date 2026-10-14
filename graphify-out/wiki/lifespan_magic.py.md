# lifespan_magic.py

> 83 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_row_to_spell_dict()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **.get_all_spells()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- *... and 58 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (25 shared connections)
- [SpellEffects](SpellEffects.md) (20 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [SpellEffectType](SpellEffectType.md) (7 shared connections)
- [TargetMatch](TargetMatch.md) (6 shared connections)
- [SpellLearningService](SpellLearningService.md) (5 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (3 shared connections)
- [magic_service.py](magic_service.py.md) (3 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [TargetType](TargetType.md) (3 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (3 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 208 (90%)
- INFERRED: 23 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*