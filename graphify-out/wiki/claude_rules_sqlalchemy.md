# claude rules sqlalchemy

> 349 nodes

## Key Concepts

- **DatabaseError** (264 connections) — `server/exceptions.py`
- **server/exceptions.py** (246 connections) — `server/exceptions.py`
- **log_and_raise()** (196 connections) — `server/utils/error_logging.py`
- **get_session_maker()** (97 connections) — `server/database.py`
- **sqlalchemy.md** (89 connections) — `.claude/rules/sqlalchemy.md`
- **database.py** (82 connections) — `server/database.py`
- **error_logging.py** (62 connections) — `server/utils/error_logging.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **PlayerSpellRepository** (35 connections) — `server/persistence/repositories/player_spell_repository.py`
- **database_helpers.py** (32 connections) — `server/database_helpers.py`
- **persistence/repositories/__init__.py** (31 connections) — `server/persistence/repositories/__init__.py`
- **PlayerRepository** (30 connections) — `server/persistence/repositories/player_repository.py`
- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **player_repository.py** (29 connections) — `server/persistence/repositories/player_repository.py`
- **database_config_helpers.py** (25 connections) — `server/database_config_helpers.py`
- **PlayerSkillRepository** (24 connections) — `server/persistence/repositories/player_skill_repository.py`
- **room_service.py** (23 connections) — `server/game/room_service.py`
- **player_spell_repository.py** (22 connections) — `server/persistence/repositories/player_spell_repository.py`
- **dialogue_definition_repository.py** (21 connections) — `server/persistence/repositories/dialogue_definition_repository.py`
- **player_skill_repository.py** (20 connections) — `server/persistence/repositories/player_skill_repository.py`
- **PlayerSpell** (19 connections) — `server/models/player_spells.py`
- **profession_repository.py** (19 connections) — `server/persistence/repositories/profession_repository.py`
- **skill_repository.py** (19 connections) — `server/persistence/repositories/skill_repository.py`
- **test_profession_repository.py** (19 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **row_to_player()** (18 connections) — `server/persistence/repositories/player_repository_mappers.py`
- *... and 324 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (70 shared connections)
- [server async persistence](server_async_persistence.md) (47 shared connections)
- [integration](integration.md) (46 shared connections)
- [fixturerequest](fixturerequest.md) (29 shared connections)
- [server services container service](server_services_container_service.md) (29 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (27 shared connections)
- [server game skill service](server_game_skill_service.md) (26 shared connections)
- [server error types errorseverity](server_error_types_errorseverity.md) (24 shared connections)
- [server container persistence container data](server_container_persistence_container_data.md) (24 shared connections)
- [server async persistence asyncpersistencelayer init](server_async_persistence_asyncpersistencelayer_init.md) (21 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (21 shared connections)
- [server tests unit persistence test](server_tests_unit_persistence_test.md) (20 shared connections)

## Source Files

- `.claude/rules/sqlalchemy.md`
- `e2e-tests/load-tests/get_invite_codes.py`
- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/populate_test_npc_databases.py`
- `scripts/verify_and_load_seed.py`
- `server/alembic/versions/2025_11_12_add_item_tables.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/container/bundles/game.py`
- `server/database.py`
- `server/database_config_helpers.py`
- `server/database_helpers.py`
- `server/exceptions.py`
- `server/game/room_service.py`
- `server/game/skill_service.py`
- `server/models/dialogue.py`
- `server/models/player_spells.py`
- `server/persistence/repositories/__init__.py`
- `server/persistence/repositories/dialogue_definition_repository.py`

## Audit Trail

- EXTRACTED: 1772 (91%)
- INFERRED: 176 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*