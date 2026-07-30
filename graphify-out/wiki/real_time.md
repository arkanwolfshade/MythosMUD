# real time

> 439 nodes

## Key Concepts

- **DatabaseError** (432 connections) — `server/exceptions.py`
- **exceptions.py** (196 connections) — `server/exceptions.py`
- **log_and_raise()** (164 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (91 connections) — `server/database.py`
- **database.py** (75 connections) — `server/database.py`
- **error_logging.py** (55 connections) — `server/utils/error_logging.py`
- **MovementService** (43 connections) — `server/game/movement_service.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **PlayerRepository** (31 connections) — `server/persistence/repositories/player_repository.py`
- **go_command.py** (28 connections) — `server/commands/go_command.py`
- **__init__.py** (28 connections) — `server/persistence/repositories/__init__.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **database_config_helpers.py** (24 connections) — `server/database_config_helpers.py`
- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **player_spell_repository.py** (20 connections) — `server/persistence/repositories/player_spell_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **player_skill_repository.py** (18 connections) — `server/persistence/repositories/player_skill_repository.py`
- **._initialize_database()** (17 connections) — `server/database.py`
- **profession_repository.py** (17 connections) — `server/persistence/repositories/profession_repository.py`
- **QuestDefinitionRepository** (17 connections) — `server/persistence/repositories/quest_definition_repository.py`
- **skill_repository.py** (17 connections) — `server/persistence/repositories/skill_repository.py`
- **UUID** (16 connections)
- **ExperienceRepository** (16 connections) — `server/persistence/repositories/experience_repository.py`
- **health_repository.py** (16 connections) — `server/persistence/repositories/health_repository.py`
- *... and 414 more nodes in this community*

## Relationships

- [TerminalButtonProps](TerminalButtonProps.md) (98 shared connections)
- [. init ()](_init_%28%29.md) (68 shared connections)
- [close db()](close_db%28%29.md) (65 shared connections)
- [.initialize()](initialize%28%29.md) (50 shared connections)
- [bench cache npc](bench_cache_npc.md) (49 shared connections)
- [datetime](datetime.md) (47 shared connections)
- [Any](Any.md) (32 shared connections)
- [Player](Player.md) (32 shared connections)
- [disconnect grace period](disconnect_grace_period.md) (30 shared connections)
- [metrics](metrics.md) (25 shared connections)
- [container persistence](container_persistence.md) (25 shared connections)
- [NPCCombatIntegrationService](NPCCombatIntegrationService.md) (24 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/populate_test_npc_databases.py`
- `scripts/verify_and_load_seed.py`
- `server/async_persistence_room_loader.py`
- `server/commands/go_command.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/exceptions.py`
- `server/game/character_creation_service.py`
- `server/game/mechanics.py`
- `server/game/movement_service.py`
- `server/models/quest.py`
- `server/persistence/item_instance_persistence.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/experience_repository.py`
- `server/persistence/repositories/health_repository.py`
- `server/persistence/repositories/item_repository.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/persistence/repositories/player_repository.py`

## Audit Trail

- EXTRACTED: 2482 (85%)
- INFERRED: 424 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*