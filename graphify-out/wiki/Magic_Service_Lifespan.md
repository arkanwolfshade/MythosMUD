# Magic Service Lifespan

> 173 nodes

## Key Concepts

- **ApplicationContainer** (150 connections) — `server/container/main.py`
- **lifespan_magic.py** (36 connections) — `server/app/lifespan_magic.py`
- **SpellRegistry** (28 connections) — `server/game/magic/spell_registry.py`
- **test_application_container.py** (28 connections) — `server/tests/unit/test_application_container.py`
- **PlayerSpellRepository** (25 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellEffectsDeps** (21 connections) — `server/game/magic/spell_effects.py`
- **magic.py** (21 connections) — `server/container/bundles/magic.py`
- **MPRegenerationService** (17 connections) — `server/game/magic/mp_regeneration_service.py`
- **test_application_container_main.py** (17 connections) — `server/tests/unit/container/test_application_container_main.py`
- **SpellRepository** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (14 connections) — `server/container/bundles/magic.py`
- **_initialize_magic_service()** (11 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **_initialize_spell_effects()** (10 connections) — `server/app/lifespan_magic.py`
- **reset_container()** (10 connections) — `server/container/main.py`
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **_create_learning_mp_regen_and_magic()** (9 connections) — `server/container/bundles/magic.py`
- **_flatten_bundle()** (9 connections) — `server/container/main.py`
- **FastAPI** (9 connections)
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **MagicBundle** (7 connections) — `server/container/bundles/magic.py`
- **.__init__()** (7 connections) — `server/container/main.py`
- **.reset_instance()** (7 connections) — `server/container/main.py`
- *... and 148 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (51 shared connections)
- [Community 88](Community_88.md) (21 shared connections)
- [Community 55](Community_55.md) (19 shared connections)
- [Community 130](Community_130.md) (15 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (13 shared connections)
- [Magic & Tick Services](Magic_&_Tick_Services.md) (12 shared connections)
- [API Response Models](API_Response_Models.md) (9 shared connections)
- [Community 416](Community_416.md) (8 shared connections)
- [Community 195](Community_195.md) (7 shared connections)
- [Community 50](Community_50.md) (7 shared connections)
- [Community 563](Community_563.md) (5 shared connections)
- [Community 118](Community_118.md) (5 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/container/bundles/magic.py`
- `server/container/main.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/container/test_application_container_main.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 483 (88%)
- INFERRED: 65 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*