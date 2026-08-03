# coercion int inventory

> 110 nodes

## Key Concepts

- **SpellLearningService** (43 connections) — `server/game/magic/spell_learning_service.py`
- **PlayerSpellRepository** (38 connections) — `server/persistence/repositories/player_spell_repository.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **MagicBundle** (22 connections) — `server/container/bundles/magic.py`
- **magic.py** (20 connections) — `server/container/bundles/magic.py`
- **MPRegenerationService** (20 connections) — `server/game/magic/mp_regeneration_service.py`
- **SpellRepository** (16 connections) — `server/persistence/repositories/spell_repository.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **_create_registry_and_targeting()** (15 connections) — `server/container/bundles/magic.py`
- **test_spell_learning_service.py** (15 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
- **mp_regeneration_service.py** (13 connections) — `server/game/magic/mp_regeneration_service.py`
- **_create_learning_mp_regen_and_magic()** (11 connections) — `server/container/bundles/magic.py`
- **FastAPI** (9 connections)
- **_initialize_spell_targeting_service()** (9 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_effects()** (9 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_learning_service()** (8 connections) — `server/app/lifespan_magic.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.learn_spell()** (8 connections) — `server/game/magic/spell_learning_service.py`
- **.combat_service()** (7 connections) — `server/game/magic/spell_effects.py`
- **UUID** (7 connections)
- **_initialize_spell_repositories()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_spell_registry()** (6 connections) — `server/app/lifespan_magic.py`
- **_initialize_mp_regeneration_service()** (6 connections) — `server/app/lifespan_magic.py`
- **_link_magic_to_combat()** (6 connections) — `server/app/lifespan_magic.py`
- *... and 85 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (27 shared connections)
- [spell game magic](spell_game_magic.md) (25 shared connections)
- [game models player](game_models_player.md) (22 shared connections)
- [Database Config](Database_Config.md) (13 shared connections)
- [NPC Combat](NPC_Combat.md) (10 shared connections)
- [player respawn event](player_respawn_event.md) (9 shared connections)
- [models npc rationale](models_npc_rationale.md) (8 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (8 shared connections)
- [player service game](player_service_game.md) (7 shared connections)
- [magic completion game](magic_completion_game.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)
- [regeneration service magic](regeneration_service_magic.md) (5 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/container/bundles/magic.py`
- `server/game/magic/mp_regeneration_service.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/container/test_container_bundles.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 489 (89%)
- INFERRED: 58 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*