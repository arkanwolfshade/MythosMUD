# Server Game (4)

> 113 nodes

## Key Concepts

- **magic_service.py** (39 connections) — `server/game/magic/magic_service.py`
- **PlayerSpellRepository** (36 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (35 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **SpellLearningService** (30 connections) — `server/game/magic/spell_learning_service.py`
- **MagicService** (29 connections) — `server/game/magic/magic_service.py`
- **SpellTargetingService** (29 connections) — `server/game/magic/spell_targeting.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_learning_service.py** (21 connections) — `server/game/magic/spell_learning_service.py`
- **spell_targeting.py** (20 connections) — `server/game/magic/spell_targeting.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **magic.py** (19 connections) — `server/container/bundles/magic.py`
- **MagicBundle** (18 connections) — `server/container/bundles/magic.py`
- **MagicServiceOptionalDeps** (17 connections) — `server/game/magic/magic_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **spell_registry.py** (15 connections) — `server/game/magic/spell_registry.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellRepository** (14 connections) — `server/persistence/repositories/spell_repository.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (13 connections) — `server/container/bundles/magic.py`
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **spell_materials.py** (10 connections) — `server/game/magic/spell_materials.py`
- **FastAPI** (9 connections)
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- *... and 88 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (37 shared connections)
- [Server Models (13)](Server_Models_%2813%29.md) (26 shared connections)
- [Server Game (2)](Server_Game_%282%29.md) (22 shared connections)
- [Server Game (14)](Server_Game_%2814%29.md) (21 shared connections)
- [Server App](Server_App.md) (17 shared connections)
- [Server Infrastructure](Server_Infrastructure.md) (12 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (10 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (9 shared connections)
- [Server Services (12)](Server_Services_%2812%29.md) (8 shared connections)
- [Server Game (18)](Server_Game_%2818%29.md) (8 shared connections)
- [Server Game (7)](Server_Game_%287%29.md) (7 shared connections)
- [Server Game (39)](Server_Game_%2839%29.md) (7 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/app/test_lifespan_startup.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 601 (84%)
- INFERRED: 116 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*