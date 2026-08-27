# Any

> 136 nodes

## Key Concepts

- **SpellEffects** (55 connections) — `server/game/magic/spell_effects.py`
- **magic_service.py** (48 connections) — `server/game/magic/magic_service.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (32 connections) — `server/game/magic/spell_registry.py`
- **test_damage_grace_period.py** (28 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **SpellEffectsDeps** (20 connections) — `server/game/magic/spell_effects.py`
- **MPRegenerationService** (18 connections) — `server/game/magic/mp_regeneration_service.py`
- **spell_registry.py** (16 connections) — `server/game/magic/spell_registry.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **_create_registry_and_targeting()** (14 connections) — `server/container/bundles/magic.py`
- **initialize_magic_services()** (13 connections) — `server/app/lifespan_magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (9 connections) — `server/container/bundles/magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **MagicBundle** (7 connections) — `server/container/bundles/magic.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **test_negative_status_effect_blocked_during_grace_period()** (7 connections) — `server/tests/unit/services/test_damage_grace_period.py`
- *... and 111 more nodes in this community*

## Relationships

- [eventHandlers/types.ts](eventHandlers-types.ts.md) (36 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (33 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (30 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (18 shared connections)
- [test_combat_cleanup_handler.py](test_combat_cleanup_handler.py.md) (14 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (12 shared connections)
- [test_metrics.py](test_metrics.py.md) (11 shared connections)
- [get_logger](get_logger.md) (10 shared connections)
- [debugLogger](debugLogger.md) (9 shared connections)
- [WebSocketMessageValidator](WebSocketMessageValidator.md) (8 shared connections)
- [MythosMUDError](MythosMUDError.md) (6 shared connections)
- [test_container_persistence_extended_crud.py](test_container_persistence_extended_crud.py.md) (6 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/game/magic/test_spell_effects.py`
- `server/tests/unit/services/test_damage_grace_period.py`

## Audit Trail

- EXTRACTED: 412 (85%)
- INFERRED: 73 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*