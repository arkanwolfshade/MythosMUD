# Magic Spell Service

> 199 nodes

## Key Concepts

- **ApplicationContainer** (140 connections) — `server/container/main.py`
- **magic_service.py** (39 connections) — `server/game/magic/magic_service.py`
- **PlayerSpellRepository** (36 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **SpellTargetingService** (31 connections) — `server/game/magic/spell_targeting.py`
- **SpellLearningService** (30 connections) — `server/game/magic/spell_learning_service.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **test_lifespan_startup.py** (26 connections) — `server/tests/unit/app/test_lifespan_startup.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **magic.py** (19 connections) — `server/container/bundles/magic.py`
- **MagicBundle** (18 connections) — `server/container/bundles/magic.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **initialize_container_and_legacy_services()** (14 connections) — `server/app/lifespan_startup.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **_startup_application()** (13 connections) — `server/app/lifespan.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **FastAPI** (13 connections)
- **_create_registry_and_targeting()** (13 connections) — `server/container/bundles/magic.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- *... and 174 more nodes in this community*

## Relationships

- [Memory Task Runtime](Memory_Task_Runtime.md) (61 shared connections)
- [spell models rationale](spell_models_rationale.md) (44 shared connections)
- [NATS Messaging](NATS_Messaging.md) (31 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (30 shared connections)
- [spell game magic](spell_game_magic.md) (24 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (19 shared connections)
- [magic healing game](magic_healing_game.md) (18 shared connections)
- [magic completion game](magic_completion_game.md) (17 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (16 shared connections)
- [Item Instances](Item_Instances.md) (14 shared connections)
- [System Metrics](System_Metrics.md) (12 shared connections)
- [aggro threat services](aggro_threat_services.md) (9 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/app/lifespan_event_subscriptions.py`
- `server/app/lifespan_magic.py`
- `server/app/lifespan_startup.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/container/main.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/test_application_container.py`

## Audit Trail

- EXTRACTED: 1007 (87%)
- INFERRED: 144 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*