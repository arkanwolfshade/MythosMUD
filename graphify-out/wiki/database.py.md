# database.py

> 160 nodes

## Key Concepts

- **database.py** (79 connections) — `server/database.py`
- **models/user.py** (56 connections) — `server/models/user.py`
- **get_async_session()** (53 connections) — `server/database.py`
- **users.py** (46 connections) — `server/auth/users.py`
- **get_admin_auth_service()** (39 connections) — `server/services/admin_auth_service.py`
- **rooms.py** (35 connections) — `server/api/rooms.py`
- **validate_admin_permission()** (31 connections) — `server/api/admin/npc_router_core.py`
- **npc_definitions_api.py** (29 connections) — `server/api/admin/npc_definitions_api.py`
- **npc_instances_api.py** (26 connections) — `server/api/admin/npc_instances_api.py`
- **npc_population_api.py** (22 connections) — `server/api/admin/npc_population_api.py`
- **npc_spawn_rules_api.py** (22 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **npc_schemas.py** (21 connections) — `server/api/admin/npc_schemas.py`
- **npc_admin_mgmt_api.py** (20 connections) — `server/api/admin/npc_admin_mgmt_api.py`
- **admin_auth_service.py** (19 connections) — `server/services/admin_auth_service.py`
- **AdminAction** (15 connections) — `server/services/admin_auth_service.py`
- **npc_router_core.py** (15 connections) — `server/api/admin/npc_router_core.py`
- **async_persistence_direct_queries.py** (15 connections) — `server/async_persistence_direct_queries.py`
- **_update_npc_definition_internal()** (13 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_definition()** (12 connections) — `server/api/admin/npc_definitions_api.py`
- **create_npc_spawn_rule()** (12 connections) — `server/api/admin/npc_spawn_rules_api.py`
- **get_npc_definition()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **get_npc_definitions()** (11 connections) — `server/api/admin/npc_definitions_api.py`
- **move_npc_instance()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **spawn_npc_instance()** (11 connections) — `server/api/admin/npc_instances_api.py`
- **get_npc_spawn_rules()** (11 connections) — `server/api/admin/npc_spawn_rules_api.py`
- *... and 135 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (50 shared connections)
- [User](User.md) (41 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (31 shared connections)
- [npc_admin.py](npc_admin.py.md) (23 shared connections)
- [update_room_position](update_room_position.md) (13 shared connections)
- [log_and_raise](log_and_raise.md) (13 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (12 shared connections)
- [test_users.py](test_users.py.md) (11 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (11 shared connections)
- [DatabaseError](DatabaseError.md) (10 shared connections)
- [maps.py](maps.py.md) (9 shared connections)
- [DatabaseManager](DatabaseManager.md) (8 shared connections)

## Source Files

- `scripts/add_flavor_text_column.py`
- `scripts/load_seed_using_project_db.py`
- `scripts/verify_and_load_seed.py`
- `server/api/__init__.py`
- `server/api/admin/__init__.py`
- `server/api/admin/npc.py`
- `server/api/admin/npc_admin_mgmt_api.py`
- `server/api/admin/npc_definitions_api.py`
- `server/api/admin/npc_instances_api.py`
- `server/api/admin/npc_population_api.py`
- `server/api/admin/npc_router_core.py`
- `server/api/admin/npc_schemas.py`
- `server/api/admin/npc_spawn_rules_api.py`
- `server/api/rooms.py`
- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`
- `server/async_persistence_room_loader.py`
- `server/auth/email_utils.py`
- `server/auth/users.py`
- `server/database.py`

## Audit Trail

- EXTRACTED: 1053 (100%)
- INFERRED: 4 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*