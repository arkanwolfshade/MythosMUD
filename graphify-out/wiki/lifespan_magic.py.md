# lifespan_magic.py

> 42 nodes

## Key Concepts

- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- **.process_tick_regeneration()** (6 connections) — `server/game/magic/mp_regeneration_service.py`
- **Any** (5 connections)
- **UUID** (5 connections)
- **_validate_magic_prerequisites()** (4 connections) — `server/app/lifespan_magic.py`
- **._get_regen_multiplier()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_item()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_meditation()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.restore_mp_from_rest()** (4 connections) — `server/game/magic/mp_regeneration_service.py`
- **.__init__()** (3 connections) — `server/game/magic/mp_regeneration_service.py`
- **SpellRepositoryClass** (3 connections)
- **Magic system initialization for application startup. Extracted from…** (1 connections) — `server/app/lifespan_magic.py`
- **Initialize MagicService and attach to app.state.** (1 connections) — `server/app/lifespan_magic.py`
- *... and 17 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (9 shared connections)
- [TargetMatch](TargetMatch.md) (7 shared connections)
- [magic_service.py](magic_service.py.md) (6 shared connections)
- [test_mp_regeneration_service.py](test_mp_regeneration_service.py.md) (4 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (3 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [SpellLearningService](SpellLearningService.md) (2 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (2 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`

## Audit Trail

- EXTRACTED: 125 (91%)
- INFERRED: 12 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*