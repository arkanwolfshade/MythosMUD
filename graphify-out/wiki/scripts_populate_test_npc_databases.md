# scripts populate test npc databases

> 40 nodes

## Key Concepts

- **DatabaseError** (255 connections) — `server/exceptions.py`
- **test_skill_use_log_repository.py** (11 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **populate_test_npc_databases.py** (7 connections) — `scripts/populate_test_npc_databases.py`
- **UUID** (7 connections)
- **.is_room_explored()** (6 connections) — `server/services/exploration_service.py`
- **main()** (5 connections) — `scripts/populate_test_npc_databases.py`
- **.get_explored_rooms()** (5 connections) — `server/services/exploration_service.py`
- **._mark_explored_in_session()** (5 connections) — `server/services/exploration_service.py`
- **AsyncSession** (5 connections)
- **get_npc_data_from_source()** (4 connections) — `scripts/populate_test_npc_databases.py`
- **populate_database()** (4 connections) — `scripts/populate_test_npc_databases.py`
- **test_create_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_delete_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_get_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **test_update_container_database_error()** (4 connections) — `server/tests/unit/persistence/test_container_persistence_extended_crud.py`
- **get_npc_database_url()** (3 connections) — `scripts/populate_test_npc_databases.py`
- **_mock_session()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **test_get_skill_ids_used_at_level()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **test_record_use()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **test_record_use_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- **asyncio** (3 connections)
- **fixture** (1 connections)
- *... and 15 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (35 shared connections)
- [server error handlers pydantic error](server_error_handlers_pydantic_error.md) (16 shared connections)
- [composed](composed.md) (13 shared connections)
- [server services exploration service explorationservice](server_services_exploration_service_explorationservice.md) (13 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (12 shared connections)
- [draft7validator](draft7validator.md) (9 shared connections)
- [server container persistence container data](server_container_persistence_container_data.md) (9 shared connections)
- [server persistence container data](server_persistence_container_data.md) (9 shared connections)
- [server game skill service skillservice](server_game_skill_service_skillservice.md) (8 shared connections)
- [server tests unit persistence test](server_tests_unit_persistence_test.md) (7 shared connections)
- [baseevent](baseevent.md) (7 shared connections)
- [server async persistence asyncpersistencelayer create](server_async_persistence_asyncpersistencelayer_create.md) (6 shared connections)

## Source Files

- `scripts/populate_test_npc_databases.py`
- `server/exceptions.py`
- `server/services/exploration_service.py`
- `server/tests/unit/persistence/repositories/test_skill_use_log_repository.py`
- `server/tests/unit/persistence/test_container_persistence_extended_crud.py`

## Audit Trail

- EXTRACTED: 192 (60%)
- INFERRED: 130 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*