# DatabaseError

> 570 nodes

## Key Concepts

- **DatabaseError** (264 connections) — `server/exceptions.py`
- **server/exceptions.py** (244 connections) — `server/exceptions.py`
- **log_and_raise()** (196 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **database.py** (80 connections) — `server/database.py`
- **error_logging.py** (61 connections) — `server/utils/error_logging.py`
- **Profession** (53 connections) — `server/models/profession.py`
- **test_async_persistence_core.py** (40 connections) — `server/tests/unit/infrastructure/test_async_persistence_core.py`
- **persistence/repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **test_profession.py** (30 connections) — `server/tests/unit/models/test_profession.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **ExperienceRepository** (28 connections) — `server/persistence/repositories/experience_repository.py`
- **player_repository.py** (28 connections) — `server/persistence/repositories/player_repository.py`
- **Skill** (26 connections) — `server/models/skill.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **npc_spawn_rules_api.py** (24 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **asyncio** (23 connections)
- **connection_helpers.py** (22 connections) — `server/realtime/connection_helpers.py`
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **player_spell_repository.py** (21 connections) — `server/persistence/repositories/player_spell_repository.py`
- **connection_manager_api.py** (21 connections) — `server/realtime/connection_manager_api.py`
- **emote_service.py** (20 connections) — `server/game/emote_service.py`
- **dialogue_definition_repository.py** (20 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **test_quest_definition_repository.py** (20 connections) — `server/tests/unit/persistence/test_quest_definition_repository.py`
- *... and 545 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (126 shared connections)
- [Player](Player.md) (88 shared connections)
- [MythosMUDError](MythosMUDError.md) (35 shared connections)
- [item_instance_persistence.py](item_instance_persistence.py.md) (34 shared connections)
- [DatabaseManager](DatabaseManager.md) (34 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (34 shared connections)
- [ValidationError](ValidationError.md) (26 shared connections)
- [get_async_session](get_async_session.md) (26 shared connections)
- [container_persistence/container_persistence.py](container_persistence-container_persistence.py.md) (24 shared connections)
- [QuestInstanceRepository](QuestInstanceRepository.md) (24 shared connections)
- [persistence/container_persistence.py](persistence-container_persistence.py.md) (22 shared connections)
- [ContainerData](ContainerData.md) (21 shared connections)

## Source Files

- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/populate_test_npc_databases.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/auth/argon2_utils.py`
- `server/auth_utils.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/exceptions.py`
- `server/game/emote_service.py`
- `server/game/mechanics.py`
- `server/game/skill_service.py`
- `server/models/dialogue.py`
- `server/models/profession.py`
- `server/models/quest.py`
- `server/models/skill.py`
- `server/persistence/item_instance_persistence_async.py`
- `server/persistence/repositories/__init__.py`

## Audit Trail

- EXTRACTED: 1990 (89%)
- INFERRED: 247 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*