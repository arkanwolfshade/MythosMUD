# close db()

> 417 nodes

## Key Concepts

- **.get_instance()** (88 connections) — `server/database.py`
- **.reset_instance()** (87 connections) — `server/database.py`
- **database.py** (75 connections) — `server/database.py`
- **__init__.py** (70 connections) — `server/schemas/__init__.py`
- **user.py** (57 connections) — `server/models/user.py`
- **get_async_session()** (54 connections) — `server/database.py`
- **users.py** (47 connections) — `server/auth/users.py`
- **test_database_extended.py** (43 connections) — `server/tests/unit/infrastructure/test_database_extended.py`
- **test_database_error_handling.py** (41 connections) — `server/tests/unit/infrastructure/test_database_error_handling.py`
- **get_admin_auth_service()** (39 connections) — `server/services/admin_auth_service.py`
- **test_database_init.py** (36 connections) — `server/tests/unit/infrastructure/test_database_init.py`
- **rooms.py** (35 connections) — `server/api/rooms.py`
- **validate_admin_permission()** (31 connections) — `server/api/admin/npc_router_core.py`
- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_instances_api.py** (26 connections) — `server/api/admin/npc_instances_api.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **npc_population_api.py** (22 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (22 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **npc_admin_mgmt_api.py** (20 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **admin_auth_service.py** (19 connections) — `server/services/admin_auth_service.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **reset_database()** (16 connections) — `server/database.py`
- **npc_router_core.py** (15 connections) — `server/api/admin/npc_router_core.py`
- *... and 392 more nodes in this community*

## Relationships

- [.initialize()](initialize%28%29.md) (72 shared connections)
- [Connection Manager](Connection_Manager.md) (63 shared connections)
- [real time](real_time.md) (58 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (37 shared connections)
- [world](world.md) (26 shared connections)
- [memory leak metrics](memory_leak_metrics.md) (18 shared connections)
- [equipment helpers](equipment_helpers.md) (16 shared connections)
- [main()](main%28%29.md) (14 shared connections)
- [get current tick()](get_current_tick%28%29.md) (12 shared connections)
- [ExitStack](ExitStack.md) (12 shared connections)
- [init](init.md) (11 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (11 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/api/rooms.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/database.py`
- `server/models/user.py`

## Audit Trail

- EXTRACTED: 2167 (96%)
- INFERRED: 81 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*