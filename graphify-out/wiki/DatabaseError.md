# DatabaseError

> 681 nodes

## Key Concepts

- **DatabaseError** (264 connections) — `server/exceptions.py`
- **server/exceptions.py** (246 connections) — `server/exceptions.py`
- **log_and_raise()** (196 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **sqlalchemy.md** (89 connections) — `.claude/rules/sqlalchemy.md`
- **database.py** (82 connections) — `server/database.py`
- **models/user.py** (63 connections) — `server/models/user.py`
- **error_logging.py** (62 connections) — `server/utils/error_logging.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **users.py** (49 connections) — `server/auth/users.py`
- **test_database_extended.py** (44 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_argon2_utils.py** (43 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **rooms.py** (40 connections) — `server/api/rooms.py`
- **admin_commands.py** (33 connections) — `server/commands/admin_commands.py`
- **persistence/repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **DialogueDefinitionRepository** (30 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **admin_mute_commands.py** (29 connections) — `server/commands/admin_mute_commands.py`
- **player_repository.py** (29 connections) — `server/persistence/repositories/player_repository.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **Skill** (26 connections) — `server/models/skill.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **test_quest_instance_repository.py** (23 connections) — `server/tests/unit/persistence/test_quest_instance_repository.py`
- **player_schema_converter.py** (22 connections) — `server/game/player_schema_converter.py`
- *... and 656 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (176 shared connections)
- [models/player.py](models-player.py.md) (94 shared connections)
- [DatabaseManager](DatabaseManager.md) (62 shared connections)
- [pytest.md](pytest.md.md) (60 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (37 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (27 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (26 shared connections)
- [command_service.py](command_service.py.md) (26 shared connections)
- [database_config_helpers.py](database_config_helpers.py.md) (25 shared connections)
- [test_container_persistence_crud.py](test_container_persistence_crud.py.md) (24 shared connections)
- [AuthenticationError](AuthenticationError.md) (22 shared connections)
- [Player](Player.md) (22 shared connections)

## Source Files

- `.claude/rules/sqlalchemy.md`
- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/populate_test_npc_databases.py`
- `scripts/verify_and_load_seed.py`
- `server/alembic/versions/2025_11_12_add_item_tables.py`
- `server/api/player_helpers.py`
- `server/api/rooms.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/auth/__init__.py`
- `server/auth/argon2_utils.py`
- `server/auth/email_utils.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/commands/admin_commands.py`
- `server/commands/admin_mute_commands.py`

## Audit Trail

- EXTRACTED: 2589 (92%)
- INFERRED: 219 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*