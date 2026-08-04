# coercion int inventory

> 95 nodes

## Key Concepts

- **SpellLearningService** (43 connections) — `server/game/magic/spell_learning_service.py`
- **PlayerSpellRepository** (38 connections) — `server/persistence/repositories/player_spell_repository.py`
- **SpellRegistry** (37 connections) — `server/game/magic/spell_registry.py`
- **lifespan_magic.py** (34 connections) — `server/app/lifespan_magic.py`
- **spell_learning_service.py** (22 connections) — `server/game/magic/spell_learning_service.py`
- **initialize_magic_services()** (15 connections) — `server/app/lifespan_magic.py`
- **test_spell_learning_service.py** (15 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **_initialize_magic_service()** (13 connections) — `server/app/lifespan_magic.py`
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
- **._validate_prerequisites()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (5 connections)
- **.learn_spell_from_book()** (5 connections) — `server/game/magic/spell_learning_service.py`
- **.learn_spell_from_npc()** (5 connections) — `server/game/magic/spell_learning_service.py`
- *... and 70 more nodes in this community*

## Relationships

- [NPC Combat](NPC_Combat.md) (30 shared connections)
- [nats services service](nats_services_service.md) (22 shared connections)
- [spell game magic](spell_game_magic.md) (19 shared connections)
- [commands magic rationale](commands_magic_rationale.md) (12 shared connections)
- [game models player](game_models_player.md) (11 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (11 shared connections)
- [player respawn event](player_respawn_event.md) (7 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (5 shared connections)
- [target resolution service](target_resolution_service.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [subject nats manager](subject_nats_manager.md) (3 shared connections)
- [regeneration service magic](regeneration_service_magic.md) (2 shared connections)

## Source Files

- `server/app/lifespan_magic.py`
- `server/commands/magic_commands.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_learning_service.py`
- `server/game/magic/spell_registry.py`
- `server/persistence/repositories/player_spell_repository.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`
- `server/tests/unit/game/magic/test_spell_registry.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`

## Audit Trail

- EXTRACTED: 399 (88%)
- INFERRED: 54 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*